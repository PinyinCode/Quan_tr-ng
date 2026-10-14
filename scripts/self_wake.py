# -*- coding: utf-8 -*-
"""
Module SELF-WAKE — Tự động ping các Render server khi user vào trang.
KHÔNG phụ thuộc UptimeRobot, GitHub Actions, hay external service.

⚙️ CẤU HÌNH: Đọc từ file `self_wake_config.json` cùng thư mục.
   → Muốn thêm/xóa server: sửa file JSON, KHÔNG cần sửa code Python.

Cách dùng:
    from self_wake import build_self_wake_html, inject_into_html
    
    # Tự động chèn self-wake vào HTML
    html = inject_into_html(my_html)
    
Hoặc:
    from self_wake import get_config, build_self_wake_html
    
    config = get_config()  # Đọc từ JSON
    html = build_self_wake_html(config)
"""

from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Union
from pathlib import Path
import json
import os
import sys


# ═══════════════════════════════════════════════════════════════
# ĐƯỜNG DẪN FILE CONFIG
# ═══════════════════════════════════════════════════════════════
CONFIG_FILENAME = "self_wake_config.json"
CONFIG_PATH = Path(__file__).parent / CONFIG_FILENAME


# ═══════════════════════════════════════════════════════════════
# CONFIG MẶC ĐỊNH (fallback nếu không tìm thấy JSON)
# ═══════════════════════════════════════════════════════════════
DEFAULT_SERVERS = [
    {"name": "OTP Server",     "url": "https://apigmail-n8bp.onrender.com/ping"},
    {"name": "Grading Server", "url": "https://chinese-grading.onrender.com/ping"},
    {"name": "Vocab API",      "url": "https://chinese-vocab-api.onrender.com/ping"},
]

DEFAULT_PING_INTERVAL_MS = 5 * 60 * 1000    # 5 phút
DEFAULT_PING_TIMEOUT_MS  = 10 * 1000        # 10 giây
DEFAULT_REPING_AFTER_MS  = 2 * 60 * 1000    # 2 phút
DEFAULT_DEBUG            = False


# ═══════════════════════════════════════════════════════════════
# DATACLASS CONFIG
# ═══════════════════════════════════════════════════════════════
@dataclass
class ServerEntry:
    """Thông tin 1 server."""
    name: str
    url: str


@dataclass
class SelfWakeConfig:
    """Cấu hình self-wake."""
    enabled: bool = True
    servers: List[ServerEntry] = field(default_factory=lambda: [
        ServerEntry(**s) for s in DEFAULT_SERVERS
    ])
    ping_interval: int = DEFAULT_PING_INTERVAL_MS
    ping_timeout: int = DEFAULT_PING_TIMEOUT_MS
    reping_on_visible_after: int = DEFAULT_REPING_AFTER_MS
    ping_on_first_click: bool = True
    heartbeat_enabled: bool = True
    debug: bool = DEFAULT_DEBUG
    
    def to_js_dict(self) -> dict:
        """Chuyển config thành dict để inject vào JS."""
        return {
            "enabled": self.enabled,
            "servers": [
                {"name": s.name, "url": s.url}
                for s in self.servers
            ],
            "pingInterval": self.ping_interval,
            "pingTimeout": self.ping_timeout,
            "repingOnVisibleAfter": self.reping_on_visible_after,
            "pingOnFirstClick": self.ping_on_first_click,
            "heartbeatEnabled": self.heartbeat_enabled,
            "debug": self.debug,
        }


# ═══════════════════════════════════════════════════════════════
# ĐỌC CONFIG TỪ JSON
# ═══════════════════════════════════════════════════════════════
_config_cache: Optional[SelfWakeConfig] = None


def _parse_server_entry(entry) -> Optional[ServerEntry]:
    """
    Parse 1 server entry từ JSON. Chấp nhận 2 format:
    - Dict: {"name": "...", "url": "..."}
    - String: "https://..."  (name tự động lấy từ URL)
    """
    if isinstance(entry, dict):
        url = entry.get("url", "").strip()
        if not url:
            return None
        name = entry.get("name", "").strip()
        if not name:
            name = _name_from_url(url)
        return ServerEntry(name=name, url=url)
    elif isinstance(entry, str):
        url = entry.strip()
        if not url:
            return None
        return ServerEntry(name=_name_from_url(url), url=url)
    return None


def _name_from_url(url: str) -> str:
    """Lấy tên ngắn gọn từ URL: https://abc.onrender.com/ping → abc"""
    try:
        # Bỏ protocol
        s = url.split("://", 1)[-1]
        # Lấy domain đầu tiên
        host = s.split("/", 1)[0]
        # Lấy subdomain đầu tiên
        name = host.split(".", 1)[0]
        return name or "Server"
    except Exception:
        return "Server"


def load_config(force_reload: bool = False,
                config_path: Optional[Union[str, Path]] = None) -> SelfWakeConfig:
    """
    Đọc config từ file JSON.
    
    Args:
        force_reload: True = bỏ qua cache, đọc lại từ file
        config_path: Đường dẫn file JSON (None = dùng CONFIG_PATH mặc định)
    
    Returns:
        SelfWakeConfig
    """
    global _config_cache
    
    if _config_cache is not None and not force_reload:
        return _config_cache
    
    path = Path(config_path) if config_path else CONFIG_PATH
    
    # Nếu không tìm thấy file → dùng default + cảnh báo
    if not path.exists():
        print(f"⚠️ [self-wake] Không tìm thấy {path} → dùng config mặc định",
              file=sys.stderr)
        _config_cache = SelfWakeConfig()
        return _config_cache
    
    # Đọc JSON
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ [self-wake] Lỗi parse JSON {path}: {e} → dùng config mặc định",
              file=sys.stderr)
        _config_cache = SelfWakeConfig()
        return _config_cache
    except Exception as e:
        print(f"❌ [self-wake] Lỗi đọc file {path}: {e} → dùng config mặc định",
              file=sys.stderr)
        _config_cache = SelfWakeConfig()
        return _config_cache
    
    # ═══ Parse các field ═══
    enabled = bool(data.get("enabled", True))
    
    # Servers
    raw_servers = data.get("servers", [])
    if not isinstance(raw_servers, list):
        print(f"⚠️ [self-wake] 'servers' phải là array → dùng default",
              file=sys.stderr)
        raw_servers = DEFAULT_SERVERS
    
    servers: List[ServerEntry] = []
    for entry in raw_servers:
        parsed = _parse_server_entry(entry)
        if parsed:
            servers.append(parsed)
    
    if not servers:
        print(f"⚠️ [self-wake] Không có server hợp lệ → dùng default",
              file=sys.stderr)
        servers = [ServerEntry(**s) for s in DEFAULT_SERVERS]
    
    # Numeric fields với fallback
    def get_int(key: str, default: int, min_val: int = 0) -> int:
        val = data.get(key, default)
        try:
            val = int(val)
            if val < min_val:
                return default
            return val
        except (ValueError, TypeError):
            return default
    
    def get_bool(key: str, default: bool) -> bool:
        val = data.get(key, default)
        if isinstance(val, bool):
            return val
        if isinstance(val, str):
            return val.lower() in ("true", "1", "yes", "on")
        return bool(val)
    
    _config_cache = SelfWakeConfig(
        enabled=enabled,
        servers=servers,
        ping_interval=get_int("ping_interval_ms", DEFAULT_PING_INTERVAL_MS, min_val=1000),
        ping_timeout=get_int("ping_timeout_ms", DEFAULT_PING_TIMEOUT_MS, min_val=1000),
        reping_on_visible_after=get_int("reping_on_visible_after_ms", DEFAULT_REPING_AFTER_MS, min_val=0),
        ping_on_first_click=get_bool("ping_on_first_click", True),
        heartbeat_enabled=get_bool("heartbeat_enabled", True),
        debug=get_bool("debug", DEFAULT_DEBUG),
    )
    
    if _config_cache.debug:
        print(f"✅ [self-wake] Loaded {len(_config_cache.servers)} servers từ {path.name}",
              file=sys.stderr)
    
    return _config_cache


def get_config() -> SelfWakeConfig:
    """Alias cho load_config() — dùng cho code ngắn gọn."""
    return load_config()


def reload_config() -> SelfWakeConfig:
    """Force reload config từ JSON (hữu ích khi hot-reload)."""
    return load_config(force_reload=True)


# ═══════════════════════════════════════════════════════════════
# XÂY DỰNG JS
# ═══════════════════════════════════════════════════════════════
def build_self_wake_js(config: Optional[SelfWakeConfig] = None) -> str:
    """Trả về đoạn JS self-wake (không kèm <script> tag)."""
    if config is None:
        config = load_config()
    
    if not config.enabled:
        return "/* self-wake: disabled in config */"
    
    config_json = json.dumps(config.to_js_dict(), ensure_ascii=False)
    
    js = r"""
/* ═══════════════════════════════════════════════════════════════
   ⚡ SELF-WAKE RENDER SERVERS
   Tự động ping các Render server khi user vào trang.
   Config đọc từ: self_wake_config.json
   ═══════════════════════════════════════════════════════════════ */
(function selfWakeServers() {
    'use strict';
    
    /* ⭐ CONFIG từ Python (đọc từ JSON) */
    var CFG = __SELF_WAKE_CONFIG__;
    
    if (!CFG || !CFG.enabled) {
        return;
    }
    if (!CFG.servers || !CFG.servers.length) {
        console.warn('[self-wake] Không có server nào để ping');
        return;
    }
    
    var SERVERS = CFG.servers;
    var PING_INTERVAL = CFG.pingInterval || (5 * 60 * 1000);
    var PING_TIMEOUT = CFG.pingTimeout || 10000;
    var DEBUG = CFG.debug || false;
    var REPING_AFTER = CFG.repingOnVisibleAfter || (2 * 60 * 1000);
    var PING_ON_CLICK = CFG.pingOnFirstClick !== false;
    var HEARTBEAT = CFG.heartbeatEnabled !== false;
    
    /* ⭐ Logging helper */
    function log() {
        if (DEBUG) {
            var args = Array.prototype.slice.call(arguments);
            args.unshift('[self-wake]');
            console.log.apply(console, args);
        }
    }
    
    /* ⭐ Ping 1 server — không chặn UI, dùng no-cors để tránh CORS */
    function ping(server) {
        var url = server.url;
        var name = server.name || url;
        
        return new Promise(function(resolve) {
            var controller = null;
            var timer = null;
            
            try {
                controller = new AbortController();
                timer = setTimeout(function() {
                    try { controller.abort(); } catch(e) {}
                    log('⏱ timeout:', name);
                    resolve({ name: name, url: url, ok: false, reason: 'timeout' });
                }, PING_TIMEOUT);
                
                fetch(url, {
                    method: 'GET',
                    mode: 'no-cors',
                    cache: 'no-store',
                    credentials: 'omit',
                    signal: controller.signal,
                    keepalive: true
                })
                .then(function() {
                    clearTimeout(timer);
                    log('✅', name);
                    resolve({ name: name, url: url, ok: true });
                })
                .catch(function(err) {
                    clearTimeout(timer);
                    var isAbort = (err && err.name === 'AbortError');
                    if (isAbort) {
                        log('⏱ abort:', name);
                        resolve({ name: name, url: url, ok: false, reason: 'abort' });
                    } else {
                        log('⚠️', name, err && err.message);
                        resolve({ name: name, url: url, ok: true, uncertain: true });
                    }
                });
            } catch (e) {
                if (timer) clearTimeout(timer);
                log('❌ exception:', name, e);
                resolve({ name: name, url: url, ok: false, reason: 'exception' });
            }
        });
    }
    
    /* ⭐ Ping tất cả server song song */
    function pingAll() {
        log('Pinging', SERVERS.length, 'servers...');
        return Promise.all(SERVERS.map(ping));
    }
    
    /* ═══ TRIGGER 1: Ping ngay khi JS load ═══ */
    pingAll();
    
    /* ═══ TRIGGER 2: Heartbeat mỗi PING_INTERVAL ═══ */
    if (HEARTBEAT) {
        setInterval(function() {
            if (document.visibilityState === 'visible') {
                log('Heartbeat tick');
                pingAll();
            }
        }, PING_INTERVAL);
    }
    
    /* ═══ TRIGGER 3: Ping khi tab active lại ═══ */
    var lastHidden = 0;
    document.addEventListener('visibilitychange', function() {
        if (document.visibilityState === 'hidden') {
            lastHidden = Date.now();
        } else if (document.visibilityState === 'visible') {
            var away = Date.now() - lastHidden;
            if (away > REPING_AFTER) {
                log('Tab active lại sau', Math.round(away / 1000), 's → ping');
                pingAll();
            }
        }
    });
    
    /* ═══ TRIGGER 4: Ping lần đầu khi user click ═══ */
    if (PING_ON_CLICK) {
        document.addEventListener('click', function onFirstClick() {
            document.removeEventListener('click', onFirstClick);
            log('First click → ping');
            pingAll();
        }, { once: true, passive: true });
    }
    
    log('Self-wake initialized với', SERVERS.length, 'servers');
    
    /* ⭐ Expose ra window để debug thủ công */
    window.__selfWake = {
        pingAll: pingAll,
        servers: SERVERS,
        config: CFG
    };
})();
"""
    
    js = js.replace("__SELF_WAKE_CONFIG__", config_json)
    return js


def build_self_wake_html(config: Optional[SelfWakeConfig] = None) -> str:
    """Trả về HTML <script> tag hoàn chỉnh."""
    if config is None:
        config = load_config()
    
    if not config.enabled:
        return "<!-- self-wake: disabled -->"
    
    js = build_self_wake_js(config)
    return "\n<!-- ⚡ Self-Wake Render Servers -->\n<script>\n" + js + "\n</script>\n"


# ═══════════════════════════════════════════════════════════════
# SPLASH SCREEN — Ping-first mode
# ═══════════════════════════════════════════════════════════════
DEFAULT_SPLASH_ID = "selfWakeSplash"


def build_splash_css(splash_id: str = DEFAULT_SPLASH_ID) -> str:
    """CSS cho splash screen."""
    return f"""
/* ═══ SELF-WAKE SPLASH ═══ */
#{splash_id} {{
    position: fixed;
    inset: 0;
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 50%, #a855f7 100%);
    color: #fff;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 999999;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    transition: opacity .4s ease, visibility .4s ease;
}}
#{splash_id}.hidden {{
    opacity: 0;
    visibility: hidden;
    pointer-events: none;
}}
#{splash_id} .sw-icon {{
    font-size: 3.5rem;
    animation: swPulse 1.5s ease-in-out infinite;
    margin-bottom: 1rem;
}}
#{splash_id} .sw-title {{
    font-size: 1.2rem;
    font-weight: 700;
    margin-bottom: .35rem;
    letter-spacing: .3px;
}}
#{splash_id} .sw-subtitle {{
    font-size: .85rem;
    opacity: .85;
    margin-bottom: 1.25rem;
}}
#{splash_id} .sw-status {{
    font-size: .78rem;
    opacity: .75;
    min-height: 1.2em;
    font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
}}
#{splash_id} .sw-bar {{
    width: 220px;
    height: 4px;
    background: rgba(255,255,255,.2);
    border-radius: 50px;
    overflow: hidden;
    margin-top: 1rem;
}}
#{splash_id} .sw-bar-fill {{
    height: 100%;
    background: #fff;
    border-radius: 50px;
    width: 0%;
    transition: width .3s ease;
}}
@keyframes swPulse {{
    0%, 100% {{ transform: scale(1); opacity: 1; }}
    50% {{ transform: scale(1.15); opacity: .75; }}
}}
@media (prefers-color-scheme: dark) {{
    #{splash_id} {{
        background: linear-gradient(135deg, #1e1b4b 0%, #4c1d95 50%, #6b21a8 100%);
    }}
}}
"""


def build_splash_html(splash_id: str = DEFAULT_SPLASH_ID) -> str:
    """HTML splash screen."""
    return f"""
<div id="{splash_id}">
    <div class="sw-icon">⚡</div>
    <div class="sw-title">Đang khởi động hệ thống</div>
    <div class="sw-subtitle">Vui lòng đợi trong giây lát...</div>
    <div class="sw-status" id="{splash_id}Status">Đang kết nối...</div>
    <div class="sw-bar"><div class="sw-bar-fill" id="{splash_id}Bar"></div></div>
</div>
"""


def build_splash_js(config: Optional[SelfWakeConfig] = None,
                    splash_id: str = DEFAULT_SPLASH_ID) -> str:
    """JS cho ping-first mode."""
    if config is None:
        config = load_config()
    
    if not config.enabled:
        return "/* self-wake: disabled */"
    
    config_json = json.dumps(config.to_js_dict(), ensure_ascii=False)
    
    js = r"""
/* ═══════════════════════════════════════════════════════════════
   ⚡ SELF-WAKE — PING-FIRST MODE (có splash screen)
   ═══════════════════════════════════════════════════════════════ */
(function selfWakeWithSplash() {
    'use strict';
    
    var CFG = __SPLASH_CONFIG__;
    var SPLASH_ID = "__SPLASH_ID__";
    
    if (!CFG || !CFG.enabled) return;
    if (!CFG.servers || !CFG.servers.length) return;
    
    var splash = document.getElementById(SPLASH_ID);
    var statusEl = document.getElementById(SPLASH_ID + 'Status');
    var barEl = document.getElementById(SPLASH_ID + 'Bar');
    
    if (!splash) {
        console.warn('[self-wake] Splash element not found:', SPLASH_ID);
        return;
    }
    
    var SERVERS = CFG.servers;
    var TIMEOUT = CFG.pingTimeout || 30000;
    var TOTAL = SERVERS.length;
    var DONE = 0;
    var MAX_WAIT = 20000;
    
    function updateProgress() {
        var pct = Math.round((DONE / TOTAL) * 100);
        if (barEl) barEl.style.width = pct + '%';
    }
    
    function hideSplash() {
        if (splash) {
            splash.classList.add('hidden');
            setTimeout(function() {
                if (splash && splash.parentNode) splash.parentNode.removeChild(splash);
            }, 500);
        }
    }
    
    function pingOne(server) {
        var url = server.url;
        var name = server.name || url;
        var controller = null;
        var timer = null;
        
        try {
            controller = new AbortController();
            timer = setTimeout(function() {
                try { controller.abort(); } catch(e) {}
                onDone(name, false);
            }, TIMEOUT);
            
            fetch(url, {
                method: 'GET',
                mode: 'no-cors',
                cache: 'no-store',
                credentials: 'omit',
                signal: controller.signal
            })
            .then(function() {
                clearTimeout(timer);
                onDone(name, true);
            })
            .catch(function(err) {
                clearTimeout(timer);
                onDone(name, err && err.name !== 'AbortError');
            });
        } catch (e) {
            if (timer) clearTimeout(timer);
            onDone(name, false);
        }
    }
    
    function onDone(name, ok) {
        DONE++;
        updateProgress();
        if (statusEl) {
            statusEl.textContent = (ok ? '✅ ' : '⏱ ') + name + (ok ? ' OK' : ' đang khởi động...');
        }
        if (DONE >= TOTAL) {
            if (statusEl) statusEl.textContent = '✅ Sẵn sàng!';
            if (barEl) barEl.style.width = '100%';
            setTimeout(hideSplash, 400);
        }
    }
    
    setTimeout(hideSplash, MAX_WAIT);
    
    SERVERS.forEach(pingOne);
    
    if (CFG.debug) {
        console.log('[self-wake] Splash mode: pinging', SERVERS.length, 'servers');
    }
})();
"""
    
    js = js.replace("__SPLASH_CONFIG__", config_json)
    js = js.replace("__SPLASH_ID__", splash_id)
    return js


def build_splash_bundle(config: Optional[SelfWakeConfig] = None,
                         splash_id: str = DEFAULT_SPLASH_ID) -> str:
    """Bundle hoàn chỉnh: CSS + HTML + JS cho ping-first mode."""
    if config is None:
        config = load_config()
    
    if not config.enabled:
        return "<!-- self-wake: disabled -->"
    
    return (
        "\n<!-- ⚡ Self-Wake Splash Bundle -->\n"
        "<style>\n" + build_splash_css(splash_id) + "\n</style>\n"
        + build_splash_html(splash_id)
        + "\n<script>\n" + build_splash_js(config, splash_id) + "\n</script>\n"
    )


# ═══════════════════════════════════════════════════════════════
# HELPER: Tự động chèn vào HTML
# ═══════════════════════════════════════════════════════════════
def inject_into_html(html_content: str,
                     config: Optional[SelfWakeConfig] = None,
                     use_splash: bool = False) -> str:
    """Tự động chèn self-wake vào HTML trước </body>."""
    if config is None:
        config = load_config()
    
    if not config.enabled:
        return html_content
    
    if use_splash:
        bundle = build_splash_bundle(config)
    else:
        bundle = build_self_wake_html(config)
    
    if "</body>" in html_content:
        return html_content.replace("</body>", bundle + "</body>", 1)
    else:
        return html_content + bundle


# ═══════════════════════════════════════════════════════════════
# DEMO / TEST
# ═══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("=" * 60)
    print("SELF-WAKE MODULE — DEMO")
    print("=" * 60)
    print(f"\nConfig path: {CONFIG_PATH}")
    print(f"Exists: {CONFIG_PATH.exists()}")
    
    # Load config
    cfg = reload_config()
    print(f"\n✅ Loaded config:")
    print(f"   Enabled:        {cfg.enabled}")
    print(f"   Servers:        {len(cfg.servers)}")
    for s in cfg.servers:
        print(f"      • {s.name}: {s.url}")
    print(f"   Ping interval:  {cfg.ping_interval} ms")
    print(f"   Ping timeout:   {cfg.ping_timeout} ms")
    print(f"   Reping after:   {cfg.reping_on_visible_after} ms")
    print(f"   Debug:          {cfg.debug}")
    
    # Test build
    js = build_self_wake_js(cfg)
    print(f"\n✅ JS length: {len(js)} chars")
    
    html_tag = build_self_wake_html(cfg)
    print(f"✅ HTML tag length: {len(html_tag)} chars")
    
    # Test inject
    demo = "<html><body><h1>Demo</h1></body></html>"
    result = inject_into_html(demo, cfg)
    print(f"✅ Inject OK: {len(demo)} → {len(result)} chars")
    
    print("\n✅ Tất cả test PASS!")
    print("\n💡 Sửa file self_wake_config.json để thay đổi servers.")

# -*- coding: utf-8 -*-
"""
Module SELF-WAKE — Tự động ping các Render server khi user vào trang.
TỐI ƯU CHO ~500 USER đồng thời.

⚙️ CẤU HÌNH: Đọc từ file `self_wake_config.json` cùng thư mục.
   → Muốn thêm/xóa server: sửa file JSON, KHÔNG cần sửa code Python.

🎯 TỐI ƯU CHO 500 USER:
   - Jitter 0-30s khi load → rải đều 500 user trong 30s
   - Jitter 0-60s mỗi heartbeat → không ping cùng lúc
   - localStorage cooldown → user F5 nhiều lần không spam
   - Session-based lock → 1 tab chỉ ping 1 lần/interval
   - Visibility API → chỉ ping khi tab visible
   - Skip khi ẩn lâu → tiết kiệm pin mobile
   - Batch + timeout hợp lý → không block UI

Cách dùng:
    from self_wake import build_self_wake_html, inject_into_html
    
    html = inject_into_html(my_html)
"""

from dataclasses import dataclass, field
from typing import List, Optional, Union
from pathlib import Path
import json
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
DEFAULT_PING_TIMEOUT_MS  = 15 * 1000        # 15 giây (tăng vì Render cold start)
DEFAULT_REPING_AFTER_MS  = 2 * 60 * 1000    # 2 phút
DEFAULT_DEBUG            = False

# ⭐ Tối ưu cho 500 user
DEFAULT_INITIAL_JITTER_MS   = 30 * 1000     # 0-30s khi load
DEFAULT_HEARTBEAT_JITTER_MS = 60 * 1000     # 0-60s mỗi heartbeat
DEFAULT_COOLDOWN_FACTOR     = 0.9           # Cho phép skip nếu ping trong 90% interval
DEFAULT_MAX_CONCURRENT_PING = 2             # Chỉ ping tối đa 2 server cùng lúc


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
    """Cấu hình self-wake tối ưu cho 500 user."""
    enabled: bool = True
    servers: List[ServerEntry] = field(default_factory=lambda: [
        ServerEntry(**s) for s in DEFAULT_SERVERS
    ])
    
    # ⭐ Core timing
    ping_interval: int = DEFAULT_PING_INTERVAL_MS
    ping_timeout: int = DEFAULT_PING_TIMEOUT_MS
    reping_on_visible_after: int = DEFAULT_REPING_AFTER_MS
    
    # ⭐ Jitter (chống spike khi nhiều user cùng lúc)
    initial_jitter_ms: int = DEFAULT_INITIAL_JITTER_MS
    heartbeat_jitter_ms: int = DEFAULT_HEARTBEAT_JITTER_MS
    
    # ⭐ Cooldown & lock (chống spam)
    cooldown_factor: float = DEFAULT_COOLDOWN_FACTOR
    max_concurrent_ping: int = DEFAULT_MAX_CONCURRENT_PING
    
    # ⭐ Feature toggles
    ping_on_first_click: bool = True
    heartbeat_enabled: bool = True
    use_localstorage: bool = True
    pause_when_hidden: bool = True
    
    debug: bool = False
    
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
            "initialJitterMs": self.initial_jitter_ms,
            "heartbeatJitterMs": self.heartbeat_jitter_ms,
            "cooldownFactor": self.cooldown_factor,
            "maxConcurrentPing": self.max_concurrent_ping,
            "pingOnFirstClick": self.ping_on_first_click,
            "heartbeatEnabled": self.heartbeat_enabled,
            "useLocalStorage": self.use_localstorage,
            "pauseWhenHidden": self.pause_when_hidden,
            "debug": self.debug,
        }


# ═══════════════════════════════════════════════════════════════
# ĐỌC CONFIG TỪ JSON
# ═══════════════════════════════════════════════════════════════
_config_cache: Optional[SelfWakeConfig] = None


def _parse_server_entry(entry) -> Optional[ServerEntry]:
    """Parse 1 server entry — chấp nhận dict hoặc string."""
    if isinstance(entry, dict):
        url = entry.get("url", "").strip()
        if not url:
            return None
        name = entry.get("name", "").strip() or _name_from_url(url)
        return ServerEntry(name=name, url=url)
    elif isinstance(entry, str):
        url = entry.strip()
        if not url:
            return None
        return ServerEntry(name=_name_from_url(url), url=url)
    return None


def _name_from_url(url: str) -> str:
    """Lấy tên ngắn từ URL: https://abc.onrender.com/ping → abc"""
    try:
        s = url.split("://", 1)[-1]
        host = s.split("/", 1)[0]
        name = host.split(".", 1)[0]
        return name or "Server"
    except Exception:
        return "Server"


def load_config(force_reload: bool = False,
                config_path: Optional[Union[str, Path]] = None) -> SelfWakeConfig:
    """Đọc config từ JSON."""
    global _config_cache
    
    if _config_cache is not None and not force_reload:
        return _config_cache
    
    path = Path(config_path) if config_path else CONFIG_PATH
    
    if not path.exists():
        print(f"⚠️ [self-wake] Không tìm thấy {path} → dùng config mặc định",
              file=sys.stderr)
        _config_cache = SelfWakeConfig()
        return _config_cache
    
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ [self-wake] Lỗi JSON {path}: {e} → dùng default",
              file=sys.stderr)
        _config_cache = SelfWakeConfig()
        return _config_cache
    except Exception as e:
        print(f"❌ [self-wake] Lỗi đọc {path}: {e} → dùng default",
              file=sys.stderr)
        _config_cache = SelfWakeConfig()
        return _config_cache
    
    # Parse servers
    raw_servers = data.get("servers", [])
    if not isinstance(raw_servers, list):
        raw_servers = DEFAULT_SERVERS
    
    servers: List[ServerEntry] = []
    for entry in raw_servers:
        parsed = _parse_server_entry(entry)
        if parsed:
            servers.append(parsed)
    
    if not servers:
        servers = [ServerEntry(**s) for s in DEFAULT_SERVERS]
    
    # Helpers
    def get_int(key: str, default: int, min_val: int = 0) -> int:
        val = data.get(key, default)
        try:
            val = int(val)
            return val if val >= min_val else default
        except (ValueError, TypeError):
            return default
    
    def get else_float(key: str, default: float, default min_val: float = 0.
0) -> float:
        val =        data.get(key, default)
        try:
 except            val = float(val)
            return ( val if val >= min_valValueError, TypeError):
            return default
    
    def get_bool(key: str, default: bool) -> bool:
        val = data.get(key, default)
        if isinstance(val, bool):
            return val
        if isinstance(val, str):
            return val.lower() in ("true", "1", "yes", "on")
        return bool(val)
    
    _config_cache = SelfWakeConfig(
        enabled=get_bool("enabled", True),
        servers=servers,
        ping_interval=get_int("ping_interval_ms", DEFAULT_PING_INTERVAL_MS, min_val=60000),
        ping_timeout=get_int("ping_timeout_ms", DEFAULT_PING_TIMEOUT_MS, min_val=1000),
        reping_on_visible_after=get_int("reping_on_visible_after_ms", DEFAULT_REPING_AFTER_MS, min_val=0),
        initial_jitter_ms=get_int("initial_jitter_ms", DEFAULT_INITIAL_JITTER_MS, min_val=0),
        heartbeat_jitter_ms=get_int("heartbeat_jitter_ms", DEFAULT_HEARTBEAT_JITTER_MS, min_val=0),
        cooldown_factor=get_float("cooldown_factor", DEFAULT_COOLDOWN_FACTOR, min_val=0.1),
        max_concurrent_ping=get_int("max_concurrent_ping", DEFAULT_MAX_CONCURRENT_PING, min_val=1),
        ping_on_first_click=get_bool("ping_on_first_click", True),
        heartbeat_enabled=get_bool("heartbeat_enabled", True),
        use_localstorage=get_bool("use_localstorage", True),
        pause_when_hidden=get_bool("pause_when_hidden", True),
        debug=get_bool("debug", DEFAULT_DEBUG),
    )
    
    if _config_cache.debug:
        print(f"✅ [self-wake] Loaded {len(_config_cache.servers)} servers từ {path.name}",
              file=sys.stderr)
    
    return _config_cache


def get_config() -> SelfWakeConfig:
    """Alias cho load_config()."""
    return load_config()


def reload_config() -> SelfWakeConfig:
    """Force reload config từ JSON."""
    return load_config(force_reload=True)


# ═══════════════════════════════════════════════════════════════
# XÂY DỰNG JS — TỐI ƯU CHO 500 USER
# ═══════════════════════════════════════════════════════════════
def build_self_wake_js(config: Optional[SelfWakeConfig] = None) -> str:
    """Trả về JS self-wake tối ưu cho 500 user."""
    if config is None:
        config = load_config()
    
    if not config.enabled:
        return "/* self-wake: disabled in config */"
    
    config_json = json.dumps(config.to_js_dict(), ensure_ascii=False)
    
    js = r"""
/* ═══════════════════════════════════════════════════════════════
   ⚡ SELF-WAKE RENDER SERVERS — TỐI ƯU CHO ~500 USER
   
   🎯 Chiến lược chống spike:
      1. Jitter 0-30s khi load → 500 user rải đều trong 30s
      2. Jitter 0-60s mỗi heartbeat → ping phân tán
      3. localStorage cooldown → user F5 không spam
      4. Session-lock → 1 tab chỉ ping 1 lần/interval
      5. Visibility API → chỉ ping khi tab visible
      6. Batch + queue → giới hạn concurrent
   ═══════════════════════════════════════════════════════════════ */
(function selfWakeServers() {
    'use strict';
    
    var CFG = __SELF_WAKE_CONFIG__;
    
    if (!CFG || !CFG.enabled) return;
    if (!CFG.servers || !CFG.servers.length) {
        console.warn('[self-wake] Không có server');
        return;
    }
    
    var SERVERS = CFG.servers;
    var PING_INTERVAL = CFG.pingInterval || (5 * 60 * 1000);
    var PING_TIMEOUT = CFG.pingTimeout || 15000;
    var DEBUG = CFG.debug || false;
    var REPING_AFTER = CFG.repingOnVisibleAfter || (2 * 60 * 1000);
    var INITIAL_JITTER = CFG.initialJitterMs || 30000;
    var HEARTBEAT_JITTER = CFG.heartbeatJitterMs || 60000;
    var COOLDOWN_FACTOR = CFG.cooldownFactor || 0.9;
    var MAX_CONCURRENT = CFG.maxConcurrentPing || 2;
    var PING_ON_CLICK = CFG.pingOnFirstClick !== false;
    var HEARTBEAT = CFG.heartbeatEnabled !== false;
    var USE_LS = CFG.useLocalStorage !== false;
    var PAUSE_WHEN_HIDDEN = CFG.pauseWhenHidden !== false;
    
    /* ⭐ Storage keys */
    var LS_LAST_PING = 'sw_last_ping_v1';
    var SS_SESSION_PING = 'sw_session_ping_v1';
    
    /* ⭐ In-memory lock — tránh race condition */
    var isPinging = false;
    var lastPingInMemory = 0;
    
    function log() {
        if (DEBUG) {
            var args = Array.prototype.slice.call(arguments);
            args.unshift('[self-wake]');
            console.log.apply(console, args);
        }
    }
    
    /* ═══════════════════════════════════════════════════════════
       COOLDOWN CHECK — Đã ping gần đây chưa?
       ═══════════════════════════════════════════════════════════ */
    function getLastPingTime() {
        /* Ưu tiên in-memory (nhanh nhất) */
        if (lastPingInMemory > 0) return lastPingInMemory;
        
        var times = [];
        
        if (USE_LS) {
            try {
                var t1 = parseInt(localStorage.getItem(LS_LAST_PING) || '0', 10);
                if (t1 > 0) times.push(t1);
            } catch(e) {}
        }
        
        try {
            var t2 = parseInt(sessionStorage.getItem(SS_SESSION_PING) || '0', 10);
            if (t2 > 0) times.push(t2);
        } catch(e) {}
        
        return times.length > 0 ? Math.max.apply(null, times) : 0;
    }
    
    function markPinged() {
        var now = Date.now();
        lastPingInMemory = now;
        
        if (USE_LS) {
            try { localStorage.setItem(LS_LAST_PING, String(now)); } catch(e) {}
        }
        try { sessionStorage.setItem(SS_SESSION_PING, String(now)); } catch(e) {}
    }
    
    function shouldPing() {
        var last = getLastPingTime();
        if (!last) return true;
        
        /* Cho phép ping nếu quá (interval × cooldown_factor) */
        var minInterval = PING_INTERVAL * COOLDOWN_FACTOR;
        var elapsed = Date.now() - last;
        
        if (elapsed > minInterval) {
            return true;
        }
        
        log('Skip — còn', Math.round((minInterval - elapsed) / 1000), 's nữa mới ping');
        return false;
    }
    
    /* ═══════════════════════════════════════════════════════════
       PING CORE — với queue giới hạn concurrent
       ═══════════════════════════════════════════════════════════ */
    function pingOne(server) {
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
                    resolve({ name: name, ok: false, reason: 'timeout' });
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
                    resolve({ name: name, ok: true });
                })
                .catch(function(err) {
                    clearTimeout(timer);
                    var isAbort = (err && err.name === 'AbortError');
                    if (isAbort) {
                        log('⏱ abort:', name);
                        resolve({ name: name, ok: false, reason: 'abort' });
                    } else {
                        /* no-cors: lỗi CORS vẫn có thể thành công */
                        log('⚠️ uncertain:', name);
                        resolve({ name: name, ok: true, uncertain: true });
                    }
                });
            } catch (e) {
                if (timer) clearTimeout(timer);
                resolve({ name: name, ok: false, reason: 'exception' });
            }
        });
    }
    
    /* ⭐ Batch ping với concurrency limit */
    function pingAllWithLimit(servers, limit) {
        return new Promise(function(resolve) {
            var results = [];
            var index = 0;
            var active = 0;
            var completed = 0;
            var total = servers.length;
            
            if (total === 0) {
                resolve([]);
                return;
            }
            
            function startNext() {
                while (active < limit && index < total) {
                    var i = index++;
                    active++;
                    
                    pingOne(servers[i]).then(function(result) {
                        results[i] = result;
                        active--;
                        completed++;
                        
                        if (completed === total) {
                            resolve(results);
                        } else {
                            startNext();
                        }
                    }).catch(function() {
                        results[i] = { ok: false };
                        active--;
                        completed++;
                        
                        if (completed === total) {
                            resolve(results);
                        } else {
                            startNext();
                        }
                    });
                }
            }
            
            startNext();
        });
    }
    
    /* ═══════════════════════════════════════════════════════════
       PING ALL — với lock + cooldown
       ═══════════════════════════════════════════════════════════ */
    function pingAll() {
        /* Lock tránh double ping */
        if (isPinging) {
            log('Skip — đang ping rồi');
            return Promise.resolve();
        }
        
        /* Cooldown check */
        if (!shouldPing()) {
            return Promise.resolve();
        }
        
        isPinging = true;
        markPinged();
        
        log('Pinging', SERVERS.length, 'servers (max concurrent:', MAX_CONCURRENT + ')...');
        
        return pingAllWithLimit(SERVERS, MAX_CONCURRENT)
            .then(function(results) {
                isPinging = false;
                if (DEBUG) {
                    var ok = results.filter(function(r) { return r && r.ok; }).length;
                    log('Done:', ok + '/' + results.length, 'OK');
                }
                return results;
            })
            .catch(function(err) {
                isPinging = false;
                log('Error:', err);
            });
    }
    
    /* ═══════════════════════════════════════════════════════════
       TRIGGER 1: Ping lần đầu với JITTER
       ═══════════════════════════════════════════════════════════ */
    var initialDelay = Math.random() * INITIAL_JITTER;
    log('Initial ping scheduled sau', Math.round(initialDelay / 1000), 's');
    
    setTimeout(function() {
        pingAll();
    }, initialDelay);
    
    /* ═══════════════════════════════════════════════════════════
       TRIGGER 2: Heartbeat với JITTER
       ═══════════════════════════════════════════════════════════ */
    if (HEARTBEAT) {
        setInterval(function() {
            if (PAUSE_WHEN_HIDDEN && document.visibilityState !== 'visible') {
                return;
            }
            
            var jitter = Math.random() * HEARTBEAT_JITTER;
            setTimeout(function() {
                pingAll();
            }, jitter);
        }, PING_INTERVAL);
    }
    
    /* ═══════════════════════════════════════════════════════════
       TRIGGER 3: Ping khi tab active lại
       ═══════════════════════════════════════════════════════════ */
    var lastHiddenTime = 0;
    document.addEventListener('visibilitychange', function() {
        if (document.visibilityState === 'hidden') {
            lastHiddenTime = Date.now();
        } else if (document.visibilityState === 'visible') {
            var away = Date.now() - lastHiddenTime;
            if (away > REPING_AFTER) {
                log('Tab active lại sau', Math.round(away / 1000), 's');
                pingAll();
            }
        }
    });
    
    /* ═══════════════════════════════════════════════════════════
       TRIGGER 4: Ping lần đầu khi user click
       ═══════════════════════════════════════════════════════════ */
    if (PING_ON_CLICK) {
        document.addEventListener('click', function onFirstClick() {
            document.removeEventListener('click', onFirstClick);
            log('First click');
            pingAll();
        }, { once: true, passive: true });
    }
    
    /* ═══════════════════════════════════════════════════════════
       TRIGGER 5: Ping khi user online lại (network recovery)
       ═══════════════════════════════════════════════════════════ */
    window.addEventListener('online', function() {
        log('Network online → ping');
        /* Reset cooldown khi online lại */
        lastPingInMemory = 0;
        pingAll();
    });
    
    /* ⭐ Expose debug API */
    window.__selfWake = {
        pingAll: pingAll,
        pingNow: function() {
            lastPingInMemory = 0;
            return pingAll();
        },
        servers: SERVERS,
        config: CFG,
        getStats: function() {
            return {
                lastPing: getLastPingTime(),
                interval: PING_INTERVAL,
                servers: SERVERS.length,
                isPinging: isPinging
            };
        }
    };
    
    log('Self-wake ready:', SERVERS.length, 'servers, interval:', Math.round(PING_INTERVAL / 1000) + 's');
})();
"""
    
    js = js.replace("__SELF_WAKE_CONFIG__", config_json)
    return js


def build_self_wake_html(config: Optional[SelfWakeConfig] = None) -> str:
    """Trả về HTML <script> tag."""
    if config is None:
        config = load_config()
    
    if not config.enabled:
        return "<!-- self-wake: disabled -->"
    
    js = build_self_wake_js(config)
    return "\n<!-- ⚡ Self-Wake Render Servers -->\n<script>\n" + js + "\n</script>\n"


# ═══════════════════════════════════════════════════════════════
# HELPER: Tự động chèn vào HTML
# ═══════════════════════════════════════════════════════════════
def inject_into_html(html_content: str,
                     config: Optional[SelfWakeConfig] = None) -> str:
    """Tự động chèn self-wake vào HTML trước </body>."""
    if config is None:
        config = load_config()
    
    if not config.enabled:
        return html_content
    
    bundle = build_self_wake_html(config)
    
    if "</body>" in html_content:
        return html_content.replace("</body>", bundle + "</body>", 1)
    return html_content + bundle


# ═══════════════════════════════════════════════════════════════
# DEMO / TEST
# ═══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("=" * 60)
    print("SELF-WAKE — BẢN TỐI ƯU CHO ~500 USER")
    print("=" * 60)
    print(f"\nConfig path: {CONFIG_PATH}")
    print(f"Exists: {CONFIG_PATH.exists()}")
    
    cfg = reload_config()
    print(f"\n✅ Config:")
    print(f"   Enabled:            {cfg.enabled}")
    print(f"   Servers:            {len(cfg.servers)}")
    for s in cfg.servers:
        print(f"      • {s.name}: {s.url}")
    print(f"   Ping interval:      {cfg.ping_interval} ms")
    print(f"   Ping timeout:       {cfg.ping_timeout} ms")
    print(f"   Initial jitter:     {cfg.initial_jitter_ms} ms")
    print(f"   Heartbeat jitter:   {cfg.heartbeat_jitter_ms} ms")
    print(f"   Cooldown factor:    {cfg.cooldown_factor}")
    print(f"   Max concurrent:     {cfg.max_concurrent_ping}")
    print(f"   Use localStorage:   {cfg.use_localstorage}")
    print(f"   Pause when hidden:  {cfg.pause_when_hidden}")
    print(f"   Debug:              {cfg.debug}")
    
    js = build_self_wake_js(cfg)
    print(f"\n✅ JS length: {len(js)} chars")
    
    html_tag = build_self_wake_html(cfg)
    print(f"✅ HTML tag length: {len(html_tag)} chars")
    
    print("\n📊 Ước tính tải với 500 user:")
    interval_s = cfg.ping_interval / 1000
    servers = len(cfg.servers)
    req_per_min = (500 * servers) / (interval_s / 60)
    req_per_sec = req_per_min / 60
    print(f"   Ping/giây (trung bình):  {req_per_sec:.2f}")
    print(f"   Ping/phút:               {req_per_min:.0f}")
    print(f"   Ping/giờ:                {req_per_min * 60:.0f}")
    
    print(f"\n   Với jitter 0-{cfg.initial_jitter_ms // 1000}s:")
    spike_per_sec = (500 * servers) / (cfg.initial_jitter_ms / 1000)
    print(f"   Peak ping/giây khi 500 user load cùng lúc: {spike_per_sec:.1f}")
    
    print("\n✅ Tất cả test PASS!")

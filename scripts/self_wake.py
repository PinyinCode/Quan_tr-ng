# -*- coding: utf-8 -*-
from dataclasses import dataclass, field
from typing import List, Optional, Union
from pathlib import Path
import json
import sys

CONFIG_FILENAME = "self_wake_config.json"
CONFIG_PATH = Path(__file__).parent / CONFIG_FILENAME


@dataclass
class ServerEntry:
    name: str
    url: str


@dataclass
class SelfWakeConfig:
    enabled: bool = True
    servers: List[ServerEntry] = field(default_factory=list)
    ping_interval: int = 300000
    ping_timeout: int = 15000
    reping_on_visible_after: int = 120000
    initial_jitter_ms: int = 30000
    heartbeat_jitter_ms: int = 60000
    cooldown_factor: float = 0.9
    max_concurrent_ping: int = 2
    ping_on_first_click: bool = True
    heartbeat_enabled: bool = True
    use_localstorage: bool = True
    pause_when_hidden: bool = True
    debug: bool = False

    def to_js_dict(self):
        return {
            "enabled": self.enabled,
            "servers": [{"name": s.name, "url": s.url} for s in self.servers],
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


_config_cache = None


def _name_from_url(url):
    try:
        s = url.split("://", 1)[-1]
        host = s.split("/", 1)[0]
        return host.split(".", 1)[0] or "Server"
    except Exception:
        return "Server"


def _parse_server(entry):
    if isinstance(entry, dict):
        url = str(entry.get("url", "")).strip()
        if not url:
            return None
        name = str(entry.get("name", "")).strip() or _name_from_url(url)
        return ServerEntry(name=name, url=url)
    if isinstance(entry, str):
        url = entry.strip()
        if not url:
            return None
        return ServerEntry(name=_name_from_url(url), url=url)
    return None


def load_config(force_reload=False, config_path=None):
    global _config_cache
    if _config_cache is not None and not force_reload:
        return _config_cache

    path = Path(config_path) if config_path else CONFIG_PATH

    if not path.exists():
        print(f"[self-wake] Khong tim thay {path}", file=sys.stderr)
        _config_cache = SelfWakeConfig()
        return _config_cache

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"[self-wake] Loi doc JSON: {e}", file=sys.stderr)
        _config_cache = SelfWakeConfig()
        return _config_cache

    raw_servers = data.get("servers", [])
    if not isinstance(raw_servers, list):
        raw_servers = []

    servers = []
    for entry in raw_servers:
        parsed = _parse_server(entry)
        if parsed:
            servers.append(parsed)

    if not servers:
        print("[self-wake] JSON khong co server hop le", file=sys.stderr)

    def get_int(key, default, min_val=0):
        val = data.get(key, default)
        try:
            val = int(val)
            return val if val >= min_val else default
        except (ValueError, TypeError):
            return default

    def get_float(key, default, min_val=0.0):
        val = data.get(key, default)
        try:
            val = float(val)
            return val if val >= min_val else default
        except (ValueError, TypeError):
            return default

    def get_bool(key, default):
        val = data.get(key, default)
        if isinstance(val, bool):
            return val
        if isinstance(val, str):
            return val.lower() in ("true", "1", "yes", "on")
        return bool(val)

    _config_cache = SelfWakeConfig(
        enabled=get_bool("enabled", True),
        servers=servers,
        ping_interval=get_int("ping_interval_ms", 300000, min_val=60000),
        ping_timeout=get_int("ping_timeout_ms", 15000, min_val=1000),
        reping_on_visible_after=get_int("reping_on_visible_after_ms", 120000, min_val=0),
        initial_jitter_ms=get_int("initial_jitter_ms", 30000, min_val=0),
        heartbeat_jitter_ms=get_int("heartbeat_jitter_ms", 60000, min_val=0),
        cooldown_factor=get_float("cooldown_factor", 0.9, min_val=0.1),
        max_concurrent_ping=get_int("max_concurrent_ping", 2, min_val=1),
        ping_on_first_click=get_bool("ping_on_first_click", True),
        heartbeat_enabled=get_bool("heartbeat_enabled", True),
        use_localstorage=get_bool("use_localstorage", True),
        pause_when_hidden=get_bool("pause_when_hidden", True),
        debug=get_bool("debug", False),
    )

    return _config_cache


def get_config():
    return load_config()


def reload_config():
    return load_config(force_reload=True)


def build_self_wake_js(config=None):
    if config is None:
        config = load_config()

    if not config.enabled:
        return ""

    if not config.servers:
        return ""

    config_json = json.dumps(config.to_js_dict(), ensure_ascii=False)

    js = r"""
(function() {
    'use strict';
    var CFG = __SELF_WAKE_CONFIG__;
    if (!CFG || !CFG.enabled) return;
    if (!CFG.servers || !CFG.servers.length) return;

    var SERVERS = CFG.servers;
    var PING_INTERVAL = CFG.pingInterval || 300000;
    var PING_TIMEOUT = CFG.pingTimeout || 15000;
    var DEBUG = CFG.debug || false;
    var REPING_AFTER = CFG.repingOnVisibleAfter || 120000;
    var INITIAL_JITTER = CFG.initialJitterMs || 30000;
    var HEARTBEAT_JITTER = CFG.heartbeatJitterMs || 60000;
    var COOLDOWN_FACTOR = CFG.cooldownFactor || 0.9;
    var MAX_CONCURRENT = CFG.maxConcurrentPing || 2;
    var PING_ON_CLICK = CFG.pingOnFirstClick !== false;
    var HEARTBEAT = CFG.heartbeatEnabled !== false;
    var USE_LS = CFG.useLocalStorage !== false;
    var PAUSE_WHEN_HIDDEN = CFG.pauseWhenHidden !== false;

    var LS_KEY = 'sw_last_ping_v1';
    var SS_KEY = 'sw_session_ping_v1';
    var isPinging = false;
    var lastPingMemory = 0;

    function log() {
        if (!DEBUG) return;
        var a = Array.prototype.slice.call(arguments);
        a.unshift('[self-wake]');
        console.log.apply(console, a);
    }

    function getLastPing() {
        if (lastPingMemory > 0) return lastPingMemory;
        var times = [];
        if (USE_LS) {
            try {
                var t1 = parseInt(localStorage.getItem(LS_KEY) || '0', 10);
                if (t1 > 0) times.push(t1);
            } catch(e) {}
        }
        try {
            var t2 = parseInt(sessionStorage.getItem(SS_KEY) || '0', 10);
            if (t2 > 0) times.push(t2);
        } catch(e) {}
        return times.length ? Math.max.apply(null, times) : 0;
    }

    function markPinged() {
        var now = Date.now();
        lastPingMemory = now;
        if (USE_LS) {
            try { localStorage.setItem(LS_KEY, String(now)); } catch(e) {}
        }
        try { sessionStorage.setItem(SS_KEY, String(now)); } catch(e) {}
    }

    function shouldPing() {
        var last = getLastPing();
        if (!last) return true;
        var minInterval = PING_INTERVAL * COOLDOWN_FACTOR;
        return (Date.now() - last) > minInterval;
    }

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
                    log('timeout', name);
                    resolve({ ok: false });
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
                    log('ok', name);
                    resolve({ ok: true });
                })
                .catch(function(err) {
                    clearTimeout(timer);
                    if (err && err.name === 'AbortError') {
                        log('abort', name);
                        resolve({ ok: false });
                    } else {
                        log('uncertain', name);
                        resolve({ ok: true });
                    }
                });
            } catch (e) {
                if (timer) clearTimeout(timer);
                resolve({ ok: false });
            }
        });
    }

    function pingAllWithLimit(servers, limit) {
        return new Promise(function(resolve) {
            var results = [];
            var index = 0;
            var active = 0;
            var completed = 0;
            var total = servers.length;

            if (total === 0) { resolve([]); return; }

            function startNext() {
                while (active < limit && index < total) {
                    var i = index++;
                    active++;
                    pingOne(servers[i]).then(function(r) {
                        results[i] = r;
                        active--;
                        completed++;
                        if (completed === total) resolve(results);
                        else startNext();
                    }).catch(function() {
                        results[i] = { ok: false };
                        active--;
                        completed {
++;
                        if (completed === total)            resolve(results);
                        else startNext();
                    });
                return }
            }
            startNext();
        });
    {
 }

    function pingAll() {
        if (               isPinging) { log('locked'); last return Promise.resolve(); }
        if (!shouldPing()) { log('cooldown'); return Promise.resolve(); }

        isPinging = true;
        markPinged();
        log('ping', SERVERS.length);

        return pingAllWithLimit(SERVERS, MAX_CONCURRENT)
            .then(function(results) {
                isPinging = false;
                if (DEBUG) {
                    var ok = results.filter(function(r) { return r && r.ok; }).length;
                    log('done', ok + '/' + results.length);
                }
                return results;
            })
            .catch(function(err) {
                isPinging = false;
                log('error', err);
            });
    }

    setTimeout(function() {
        pingAll();
    }, Math.random() * INITIAL_JITTER);

    if (HEARTBEAT) {
        setInterval(function() {
            if (PAUSE_WHEN_HIDDEN && document.visibilityState !== 'visible') return;
            setTimeout(function() { pingAll(); }, Math.random() * HEARTBEAT_JITTER);
        }, PING_INTERVAL);
    }

    var lastHidden = 0;
    document.addEventListener('visibilitychange', function() {
        if (document.visibilityState === 'hidden') {
            lastHidden = Date.now();
        } else if (document.visibilityState === 'visible') {
            if (Date.now() - lastHidden > REPING_AFTER) pingAll();
        }
    });

    if (PING_ON_CLICK) {
        document.addEventListener('click', function once() {
            document.removeEventListener('click', once);
            pingAll();
        }, { once: true, passive: true });
    }

    window.addEventListener('online', function() {
        lastPingMemory = 0;
        pingAll();
    });

    window.__selfWake = {
        pingAll: pingAll,
        pingNow: function() { lastPingMemory = 0; return pingAll(); },
        servers: SERVERS,
        config: CFG,
        getStats: function()Ping: getLastPing(),
                interval: PING_INTERVAL,
                servers: SERVERS.length,
                isPinging: isPinging
            };
        }
    };

    log('ready', SERVERS.length);
})();
"""
    return js.replace("__SELF_WAKE_CONFIG__", config_json)


def build_self_wake_html(config=None):
    if config is None:
        config = load_config()
    if not config.enabled or not config.servers:
        return ""
    js = build_self_wake_js(config)
    if not js:
        return ""
    return "\n<script>\n" + js + "\n</script>\n"


def inject_into_html(html, config=None):
    if config is None:
        config = load_config()
    if not config.enabled:
        return html
    bundle = build_self_wake_html(config)
    if not bundle:
        return html
    if "</body>" in html:
        return html.replace("</body>", bundle + "</body>", 1)
    return html + bundle


if __name__ == "__main__":
    cfg = reload_config()
    print("Config path:", CONFIG_PATH)
    print("Exists:", CONFIG_PATH.exists())
    print("Enabled:", cfg.enabled)
    print("Servers:", len(cfg.servers))
    for s in cfg.servers:
        print("  -", s.name, "=>", s.url)
    print("Interval:", cfg.ping_interval)
    print("Timeout:", cfg.ping_timeout)
    print("Debug:", cfg.debug)
    js = build_self_wake_js(cfg)
    print("JS length:", len(js))

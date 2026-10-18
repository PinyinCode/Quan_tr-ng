# -*- coding: utf-8 -*-
"""
Module SERVER STATUS — Hiển thị trạng thái 1 server chính (đã gộp 5-in-1).
Đọc URL từ self_wake_config.json — không hardcode.
"""

import json
import os


CONFIG_FILENAME = "self_wake_config.json"
CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), CONFIG_FILENAME)


def load_servers():
    """Đọc danh sách server từ self_wake_config.json."""
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        servers = data.get("servers", [])
        result = []
        for s in servers:
            if isinstance(s, dict) and s.get("url"):
                result.append({
                    "name": s.get("name", "Server"),
                    "url": s["url"],
                    "enabled": data.get("enabled", True),
                })
        return result, data
    except Exception as e:
        print(f"[server-status] Lỗi đọc JSON: {e}")
        return [], {}


def build_server_status_css():
    """CSS cho badge trạng thái server."""
    return r"""
/* ═══════════════════════════════════════════════════════════════
   ⚡ SERVER STATUS BADGE
   ═══════════════════════════════════════════════════════════════ */
.server-status-list {
    display: flex;
    gap: .5rem;
    flex-wrap: wrap;
    margin-bottom: 1rem;
    padding: .65rem .85rem;
    background: linear-gradient(135deg, rgba(59,130,246,.05), rgba(124,58,237,.03));
    border: 1px solid var(--border);
    border-radius: 12px;
    align-items: center;
}
[data-theme="dark"] .server-status-list {
    background: linear-gradient(135deg, rgba(59,130,246,.1), rgba(124,58,237,.06));
}
.server-status-label {
    font-size: .72rem;
    font-weight: 800;
    color: var(--text-3);
    text-transform: uppercase;
    letter-spacing: .4px;
    margin-right: .35rem;
    display: flex;
    align-items: center;
    gap: .3rem;
}
.server-badge {
    display: inline-flex;
    align-items: center;
    gap: .35rem;
    padding: .3rem .7rem;
    border-radius: 50px;
    font-size: .72rem;
    font-weight: 700;
    border: 1.5px solid;
    transition: all .3s ease;
    white-space: nowrap;
    cursor: pointer;
    user-select: none;
}
.server-badge:hover {
    transform: translateY(-1px);
    box-shadow: 0 3px 10px rgba(0,0,0,.1);
}
.server-badge.status-unknown {
    background: rgba(148,163,184,.12);
    color: #64748b;
    border-color: rgba(148,163,184,.3);
}
.server-badge.status-active {
    background: rgba(22,163,74,.12);
    color: #16a34a;
    border-color: rgba(22,163,74,.4);
}
.server-badge.status-waking {
    background: rgba(245,158,11,.12);
    color: #d97706;
    border-color: rgba(245,158,11,.45);
    animation: serverBadgePulse 1.5s infinite;
}
.server-badge.status-slow {
    background: rgba(234,88,12,.12);
    color: #ea580c;
    border-color: rgba(234,88,12,.5);
    animation: serverBadgePulse 1s infinite;
}
.server-badge.status-error {
    background: rgba(220,38,38,.12);
    color: #dc2626;
    border-color: rgba(220,38,38,.5);
}
.server-badge .dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: currentColor;
    flex-shrink: 0;
}
.server-badge.status-active .dot {
    box-shadow: 0 0 0 3px rgba(22,163,74,.2);
    animation: serverDotPulse 2s infinite;
}
.server-badge .ms {
    font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
    font-size: .68rem;
    opacity: .8;
    margin-left: .15rem;
}
@keyframes serverBadgePulse {
    0%, 100% { opacity: 1; }
    50% { opacity: .65; }
}
@keyframes serverDotPulse {
    0%, 100% { box-shadow: 0 0 0 3px rgba(22,163,74,.2); }
    50% { box-shadow: 0 0 0 6px rgba(22,163,74,.05); }
}
.server-status-refresh {
    margin-left: auto;
    background: transparent;
    border: 1.5px solid var(--border);
    color: var(--text-3);
    padding: .25rem .55rem;
    border-radius: 50px;
    font-size: .68rem;
    font-weight: 700;
    cursor: pointer;
    font-family: inherit;
    display: inline-flex;
    align-items: center;
    gap: .25rem;
    transition: all .15s;
}
.server-status-refresh:hover {
    border-color: var(--primary);
    color: var(--primary);
    background: var(--primary-light);
}
.server-status-refresh.spinning i {
    animation: serverSpin .8s linear infinite;
}
@keyframes serverSpin {
    to { transform: rotate(360deg); }
}
@media (max-width: 600px) {
    .server-status-list { gap: .35rem; padding: .5rem .65rem; }
    .server-status-label { font-size: .65rem; }
    .server-badge { padding: .25rem .55rem; font-size: .68rem; }
}
"""


def build_server_status_html():
    """HTML cho section trạng thái server — CHỈ 1 SERVER CHÍNH."""
    servers, config = load_servers()
    
    if not servers:
        return ""
    
    if not config.get("enabled", True):
        return ""
    
    # ⭐ Chỉ lấy server đầu tiên (server chính)
    main = servers[0]
    name = main["name"]
    url = main["url"]
    
    return (
        '<div class="server-status-list" id="serverStatusList">'
        '<span class="server-status-label">'
        '<i class="fas fa-server"></i> Server:'
        '</span>'
        '<span class="server-badge status-unknown" '
        'data-url="' + url + '" '
        'data-name="' + name + '" '
        'title="' + name + ': ' + url + '">'
        '<span class="dot"></span>'
        '<span class="name">' + name + '</span>'
        '<span class="ms"></span>'
        '</span>'
        '<button class="server-status-refresh" id="serverStatusRefresh" '
        'title="Kiểm tra lại" type="button">'
        '<i class="fas fa-sync-alt"></i>'
        '</button>'
        '</div>'
    )


def build_server_status_js():
    """JS kiểm tra trạng thái — CHỈ 1 SERVER CHÍNH."""
    servers, config = load_servers()
    
    if not servers or not config.get("enabled", True):
        return ""
    
    # ⭐ Chỉ lấy server đầu tiên
    main = servers[0]
    server_json = json.dumps(
        {"name": main["name"], "url": main["url"]},
        ensure_ascii=False
    )
    timeout = config.get("ping_timeout_ms", 15000)
    
    return r"""
/* ═══════════════════════════════════════════════════════════════
   ⚡ SERVER STATUS CHECKER — Chỉ ping 1 server
   ═══════════════════════════════════════════════════════════════ */
(function() {
    'use strict';
    
    var SERVER = __SERVER_JSON__;
    var TIMEOUT = __TIMEOUT__;
    
    if (!SERVER) return;
    
    var STATUS = { ok: false, ms: 0, state: 'unknown' };
    
    function log() {
        // Bật nếu cần debug
    }
    
    async function checkOne() {
        var t0 = Date.now();
        try {
            var controller = new AbortController();
            var timer = setTimeout(function() { controller.abort(); }, TIMEOUT);
            
            await fetch(SERVER.url, {
                method: 'GET',
                mode: 'no-cors',
                cache: 'no-store',
                credentials: 'omit',
                signal: controller.signal
            });
            
            clearTimeout(timer);
            var ms = Date.now() - t0;
            var state;
            if (ms < 1000) state = 'active';
            else if (ms < 5000) state = 'waking';
            else state = 'slow';
            
            STATUS = { ok: true, ms: ms, state: state };
            log('OK', SERVER.name, ms + 'ms', state);
            return STATUS;
        } catch(e) {
            var ms2 = Date.now() - t0;
            STATUS = { 
                ok: false, 
                ms: ms2, 
                state: (e.name === 'AbortError') ? 'slow' : 'error' 
            };
            log('FAIL', SERVER.name, e.name, ms2 + 'ms');
            return STATUS;
        }
    }
    
    function renderBadge() {
        var badge = document.querySelector('.server-badge[data-name="' + SERVER.name + '"]');
        if (!badge) return;
        
        var st = STATUS;
        badge.className = 'server-badge';
        
        var stateClass, stateText;
        if (st.state === 'active') { stateClass = 'status-active'; stateText = st.ms + 'ms'; }
        else if (st.state === 'waking') { stateClass = 'status-waking'; stateText = Math.round(st.ms / 1000) + 's'; }
        else if (st.state === 'slow') { stateClass = 'status-slow'; stateText = Math.round(st.ms / 1000) + 's'; }
        else if (st.state === 'error') { stateClass = 'status-error'; stateText = 'lỗi'; }
        else { stateClass = 'status-unknown'; stateText = '...'; }
        
        badge.classList.add(stateClass);
        var msEl = badge.querySelector('.ms');
        if (msEl) msEl.textContent = stateText;
    }
    
    async function checkAll() {
        var refreshBtn = document.getElementById('serverStatusRefresh');
        if (refreshBtn) refreshBtn.classList.add('spinning');
        
        STATUS = { ok: false, ms: 0, state: 'unknown' };
        var badge = document.querySelector('.server-badge[data-name="' + SERVER.name + '"]');
        if (badge) {
            badge.className = 'server-badge status-unknown';
            var msEl = badge.querySelector('.ms');
            if (msEl) msEl.textContent = '...';
        }
        
        await checkOne();
        renderBadge();
        
        if (refreshBtn) refreshBtn.classList.remove('spinning');
    }
    
    function bindRefresh() {
        var btn = document.getElementById('serverStatusRefresh');
        if (btn && !btn._bound) {
            btn._bound = true;
            btn.addEventListener('click', checkAll);
        }
    }
    
    function init() {
        bindRefresh();
        setTimeout(checkAll, 2000);
    }
    
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
    
    setInterval(checkAll, 5 * 60 * 1000);
    
    window.__serverStatus = { checkAll: checkAll, STATUS: STATUS };
})();
""".replace("__SERVER_JSON__", server_json).replace("__TIMEOUT__", str(timeout))


def build_server_status_bundle():
    """Trả về bundle hoàn chỉnh: CSS + HTML + JS."""
    css = build_server_status_css()
    html = build_server_status_html()
    js = build_server_status_js()
    
    if not html or not js:
        return ""
    
    return (
        "\n<!-- ⚡ SERVER STATUS -->\n"
        "<style>\n" + css + "\n</style>\n"
        + html
        + "\n<script>\n" + js + "\n</script>\n"
    )


if __name__ == "__main__":
    print("=" * 60)
    print("SERVER STATUS MODULE — DEMO (1 server)")
    print("=" * 60)
    print("\nConfig path:", CONFIG_PATH)
    
    servers, config = load_servers()
    print("\nServers loaded:", len(servers))
    if servers:
        print("  • Main Server:", servers[0]["name"], "=>", servers[0]["url"])
    
    css = build_server_status_css()
    html = build_server_status_html()
    js = build_server_status_js()
    
    print("\nCSS length:", len(css), "chars")
    print("HTML length:", len(html), "chars")
    print("JS length:", len(js), "chars")
    print("Bundle length:", len(build_server_status_bundle()), "chars")
    print("\n✅ Module sẵn sàng")

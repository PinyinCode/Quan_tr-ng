# -*- coding: utf-8 -*-
"""
banner_fix.py — Ẩn banner ngay khi load, chỉ cho hiện khi có user thật.
"""

BANNER_FIX_JS = r"""
(function() {
    'use strict';

    var HIDE_STYLE_ID = '__banner_fix_hide_style__';
    var TIMEOUT_MS    = 3000;
    var MAX_LATE_MS   = 15000;
    var LOAD_START    = Date.now();

    function injectHideCSS() {
        if (document.getElementById(HIDE_STYLE_ID)) return;
        var style = document.createElement('style');
        style.id = HIDE_STYLE_ID;
        style.textContent =
            '#expiryBanner { display: none !important; }\n' +
            '#demoBanner   { display: none !important; }';
        (document.head || document.documentElement).appendChild(style);
        console.log('[banner_fix] 🛡️ Chèn CSS ẩn banner');
    }

    function removeHideCSS() {
        var el = document.getElementById(HIDE_STYLE_ID);
        if (el) {
            el.remove();
            console.log('[banner_fix] 🔓 Gỡ CSS ẩn banner');
        }
    }

    var __timeout = false, __resolved = false, __timer = null;

    function startTimer() {
        if (__timer) clearTimeout(__timer);
        __resolved = false;
        __timeout  = false;
        LOAD_START = Date.now();

        /* ⭐ Ẩn banner NGAY từ đầu */
        injectHideCSS();

        __timer = setTimeout(function() {
            if (__resolved) return;
            __timeout = true;
            console.warn('[banner_fix] ⏱️ Timeout ' + (TIMEOUT_MS/1000) + 's — giữ ẩn');

            var ls = document.getElementById('loadingScreen');
            if (ls) ls.classList.add('hidden');
            var st = document.getElementById('stickyTop');
            if (st && st.style.display === 'none') st.style.display = 'block';
            var mc = document.getElementById('mainContent');
            if (mc && mc.style.display === 'none') mc.style.display = 'block';
            var fg = document.getElementById('fabGroup');
            if (fg && fg.style.display === 'none') fg.style.display = 'flex';
        }, TIMEOUT_MS);
    }

    function resolveTimer() {
        __resolved = true;
        if (__timer) { clearTimeout(__timer); __timer = null; }

        if (__timeout) {
            var elapsed = Date.now() - LOAD_START;
            if (elapsed < MAX_LATE_MS) {
                __timeout = false;
                updateAllBanners();
            }
            return;
        }

        /* ⭐ Chỉ gỡ CSS khi đã có currentUser thật */
        var cu = (typeof currentUser !== 'undefined') ? currentUser : null;
        if (cu) {
            removeHideCSS();
            updateAllBanners();
        } else {
            console.log('[banner_fix] resolveTimer — chưa có user, giữ ẩn');
        }
    }

    function updateAllBanners() {
        if (__timeout) { injectHideCSS(); return; }

        try {
            if (typeof isEmergencyModeActive === 'function' && isEmergencyModeActive()) {
                injectHideCSS(); return;
            }
        } catch(e) {}

        var cu = (typeof currentUser !== 'undefined') ? currentUser : null;
        var hasFbUser = false;
        try { hasFbUser = !!(window.auth && window.auth.currentUser); } catch(e) {}

        if (!cu) {
            if (!hasFbUser) {
                removeHideCSS();
                var eb = document.getElementById('expiryBanner');
                var db = document.getElementById('demoBanner');
                if (eb) eb.style.display = 'none';
                if (db) db.style.display = 'flex';
            } else {
                injectHideCSS();
            }
            return;
        }

        var role = String(cu.role || '').toLowerCase();
        var isAdmin = (role === 'admin' || role === 'super_admin' || role === 'sub_admin');
        if (isAdmin || cu.isPermanent === true) { injectHideCSS(); return; }

        if (!cu.expiresAt) { injectHideCSS(); return; }

        var expDate = null;
        try {
            expDate = (typeof getExpiryDate === 'function') ? getExpiryDate(cu.expiresAt) : null;
        } catch(e) {}
        if (!expDate || isNaN(expDate.getTime())) { injectHideCSS(); return; }

        var daysLeft = Math.ceil((expDate.getTime() - Date.now()) / 86400000);
        if (daysLeft > 7) { injectHideCSS(); return; }

        removeHideCSS();
        var db2 = document.getElementById('demoBanner');
        if (db2) db2.style.display = 'none';
    }

    window.updateAllBanners        = updateAllBanners;
    window.__bannerFixResolveTimer = resolveTimer;
    window.__bannerFixStartTimer   = startTimer;
    window.__bannerFixGetState     = function() {
        return { resolved: __resolved, timeout: __timeout,
                 timerActive: !!__timer, elapsedMs: Date.now() - LOAD_START };
    };

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', startTimer);
    } else {
        startTimer();
    }

    /* ⭐ onAuthStateChanged — có hoặc không có user đều resolve
         NHƯNG resolveTimer() chỉ gỡ CSS khi currentUser có giá trị */
    var hookInt = setInterval(function() {
        try {
            if (typeof firebase !== 'undefined' && firebase.auth) {
                var a = firebase.auth();
                if (!a.__bannerFixHooked) {
                    a.__bannerFixHooked = true;
                    a.onAuthStateChanged(function() { resolveTimer(); });
                    clearInterval(hookInt);
                }
            }
        } catch(e) {}
    }, 500);
    setTimeout(function() { clearInterval(hookInt); }, 30000);

    setInterval(function() {
        try { updateAllBanners(); } catch(e) {}
    }, 30000);

    console.log('[banner_fix] ✅ Loaded — ẩn ngay từ đầu, timeout ' + (TIMEOUT_MS/1000) + 's');
})();
"""


def apply_banner_fix(js: str) -> str:
    if not js:
        return BANNER_FIX_JS
    return js + "\n\n" + BANNER_FIX_JS


def build_banner_fix_js() -> str:
    return BANNER_FIX_JS

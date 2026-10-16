# -*- coding: utf-8 -*-
"""
banner_fix.py — Module độc lập ẩn banner khi Firestore chết/slow.

CÁCH TIẾP CẬN ĐƠN GIẢN:
  - Dùng CSS `display: none !important` để ẩn banner — không bị JS nào ghi đè
  - Chỉ chạy khi cần (Firestore timeout / emergency mode / admin)
  - Còn lại thì bỏ CSS → banner hoạt động bình thường

CÁCH DÙNG trong build.py:
    import banner_fix
    ...
    auth_js = banner_fix.apply_banner_fix(auth_js)
"""


BANNER_FIX_JS = r"""

/* ═══════════════════════════════════════════════════════════════════
   🩹 BANNER FIX — Dùng CSS !important để ẩn banner chắc chắn 100%
   Không phụ thuộc vào việc override hàm JS (tránh bị closure cản trở)
   ═══════════════════════════════════════════════════════════════════ */
(function() {
    'use strict';

    var HIDE_STYLE_ID = '__banner_fix_hide_style__';
    var TIMEOUT_MS = 3000;

    /* ─── Hàm chèn CSS ẩn banner ─── */
    function injectHideCSS() {
        if (document.getElementById(HIDE_STYLE_ID)) return;
        var style = document.createElement('style');
        style.id = HIDE_STYLE_ID;
        style.textContent = [
            '#expiryBanner { display: none !important; }',
            '#demoBanner   { display: none !important; }'
        ].join('\n');
        (document.head || document.documentElement).appendChild(style);
        console.log('[banner_fix] 🛡️ Đã chèn CSS ẩn hết banner');
    }

    /* ─── Hàm gỡ CSS ẩn banner (cho phép banner hiện lại theo logic gốc) ─── */
    function removeHideCSS() {
        var el = document.getElementById(HIDE_STYLE_ID);
        if (el) {
            el.remove();
            console.log('[banner_fix] 🔓 Đã gỡ CSS ẩn banner');
        }
    }

    /* ─── State ─── */
    var __timeout = false;
    var __resolved = false;
    var __timer = null;

    function startTimer() {
        if (__timer) clearTimeout(__timer);
        __resolved = false;
        __timeout = false;
        removeHideCSS();

        __timer = setTimeout(function() {
            if (__resolved) return;
            __timeout = true;
            console.warn('[banner_fix] ⏱️ Firestore timeout sau ' +
                         (TIMEOUT_MS / 1000) + 's — ẨN HẾT BANNER');

            injectHideCSS();

            /* Tránh treo loading screen */
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
        if (!__timeout) removeHideCSS();
    }

    /* ═══════════════════════════════════════════════════════════════
       UPDATE ALL BANNERS — dùng CSS !important để chắc chắn ẩn
       ═══════════════════════════════════════════════════════════════ */
    function updateAllBanners() {
        /* Nếu đang timeout → giữ nguyên CSS ẩn */
        if (__timeout) {
            injectHideCSS();
            return;
        }

        /* Emergency mode → ẩn */
        try {
            if (typeof isEmergencyModeActive === 'function' && isEmergencyModeActive()) {
                injectHideCSS();
                return;
            }
        } catch(e) {}

        /* Không có user → để banner mặc định (demo) */
        var cu = (typeof currentUser !== 'undefined') ? currentUser : null;
        var hasFirebaseUser = false;
        try { hasFirebaseUser = !!(window.auth && window.auth.currentUser); } catch(e) {}

        if (!cu) {
            if (!hasFirebaseUser) {
                /* Guest thật → cho demoBanner hiện */
                removeHideCSS();
                var db = document.getElementById('demoBanner');
                var eb = document.getElementById('expiryBanner');
                if (eb) eb.style.display = 'none';
                if (db) db.style.display = 'flex';
            } else {
                injectHideCSS();
            }
            return;
        }

        /* Admin / vĩnh viễn → ẩn */
        var role = String(cu.role || '').toLowerCase();
        var isAdmin = (role === 'admin' || role === 'super_admin' || role === 'sub_admin');
        if (isAdmin || cu.isPermanent === true) { injectHideCSS(); return; }

        /* Không có expiresAt → ẩn */
        if (!cu.expiresAt) { injectHideCSS(); return; }

        /* Tính ngày còn lại */
        var expDate = null;
        try {
            expDate = (typeof getExpiryDate === 'function') ? getExpiryDate(cu.expiresAt) : null;
        } catch(e) {}
        if (!expDate || isNaN(expDate.getTime())) { injectHideCSS(); return; }

        var daysLeft = Math.ceil((expDate.getTime() - Date.now()) / (24 * 60 * 60 * 1000));

        /* Còn > 7 ngày → ẩn */
        if (daysLeft > 7) { injectHideCSS(); return; }

        /* Sắp hết hạn → bỏ CSS ẩn để banner hiện (logic gốc vẽ nội dung) */
        removeHideCSS();
        var db2 = document.getElementById('demoBanner');
        if (db2) db2.style.display = 'none';

        /* Gọi lại hàm gốc để vẽ nội dung banner */
        try {
            if (typeof window.__originalRenderExpiryBanner === 'function') {
                window.__originalRenderExpiryBanner();
            }
        } catch(e) {}
    }

    /* Expose toàn cục */
    window.updateAllBanners = updateAllBanners;
    window.__bannerFixInjectCSS = injectHideCSS;
    window.__bannerFixRemoveCSS = removeHideCSS;
    window.__bannerFixStartTimer = startTimer;
    window.__bannerFixResolveTimer = resolveTimer;
    window.__bannerFixGetState = function() {
        return { resolved: __resolved, timeout: __timeout, timerActive: !!__timer };
    };

    /* ═══════════════════════════════════════════════════════════════
       HOOK
       ═══════════════════════════════════════════════════════════════ */

    /* 1. Bắt đầu đếm khi DOM ready */
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', startTimer);
    } else {
        startTimer();
    }

    /* 2. Hook vào firebase auth */
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

    /* 3. Định kỳ update mỗi 30s */
    setInterval(function() {
        try { updateAllBanners(); } catch(e) {}
    }, 30000);

    /* 4. Cho phép test bằng tay */
    window.__debugBannerFix = function() {
        var state = window.__bannerFixGetState();
        var cu = (typeof currentUser !== 'undefined') ? currentUser : null;
        var result = {
            timeoutState: state,
            hideCSSPresent: !!document.getElementById(HIDE_STYLE_ID),
            currentUser: cu ? {
                email: cu.email, role: cu.role, tier: cu.tier,
                expiresAt: cu.expiresAt, isPermanent: cu.isPermanent
            } : null,
            bannerComputed: {
                expiry: (function() {
                    var b = document.getElementById('expiryBanner');
                    return b ? window.getComputedStyle(b).display : null;
                })(),
                demo: (function() {
                    var b = document.getElementById('demoBanner');
                    return b ? window.getComputedStyle(b).display : null;
                })()
            }
        };
        console.table(result);
        return result;
    };

    console.log('[banner_fix] ✅ Module loaded — dùng CSS !important, timeout ' +
                (TIMEOUT_MS / 1000) + 's');
})();
"""


def apply_banner_fix(js: str) -> str:
    """Chèn JS fix vào cuối chuỗi JS."""
    if not js:
        return BANNER_FIX_JS
    return js + "\n\n" + BANNER_FIX_JS


def build_banner_fix_js() -> str:
    return BANNER_FIX_JS

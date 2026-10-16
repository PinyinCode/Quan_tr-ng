# -*- coding: utf-8 -*-
"""
banner_fix.py — Module độc lập fix banner hiện sai khi Firestore chết/slow.

VẤN ĐỀ:
  - Firestore không trả lời (quota/timeout) → currentUser null hoặc cache rỗng
  - Banner mặc định đang hiển thị trạng thái DEMO
  - Khi user thực ra là admin/active nhưng Firestore chưa kịp trả → banner báo sai

GIẢI PHÁP:
  1. Timeout guard 10s: hết 10s Firestore không phản hồi → ẩn HẾT banner
  2. Ghi đè renderExpiryBanner() + updateDemoBannerByTier() cũ
     bằng 1 hàm duy nhất updateAllBanners() logic phẳng
  3. Tự hook vào auth.signInWithPopup / signOut / showLoginModal để reset timer
  4. Định kỳ re-render banner 30s/lần để đề phòng state thay đổi âm thầm

CÁCH DÙNG trong build.py:
    import banner_fix
    ...
    auth_css, auth_html, auth_js = build_all_auth(CONFIG)
    auth_js = banner_fix.apply_banner════_fix(auth_js)   # ⭐ 1 d════òng duy nhất

Không đụ════ng accounts_template.py gốc════════ → dễ rollback, dễ test.
"""


BANNER_FIX_JS = r"""

/* ═══════════════════════════════════════════════════════════════════
   🩹 BANNER FIX — Module độc lập
   Override các hàm banner cũ để logic phẳng, tránh hiện sai khi Firestore chết
   ═══════════════════════════════════════════════════════════════════ */
(function() {
    'use strict';

    /* ═══════════════════════════════════════════════════════════════
       ⏱️ TIMEOUT GUARD — Firestore không trả lời trong 10s → ẩn hết banner
       ═══════════════════════════════════════════════════════════════ */
    var TIMEOUT_MS = 10000;
    var __resolved = false;
    var __timeout  = false;
    var __timer    = null;

    function hideAllBannersNow() {
        ['expiryBanner', 'demoBanner'].forEach(function(id) {
            var el = document.getElementById(id);
            if (el) el.style.display = 'none';
        });
    }

    function startTimer() {
        if (__timer) clearTimeout(__timer);
        __resolved = false;
        __timeout  = false;

        __timer = setTimeout(function() {
            if (__resolved) return;
            __timeout = true;
            console.warn('[banner_fix] ⏱️ Firestore không phản hồi sau ' +
                         (TIMEOUT_MS / 1000) + 's — ẩn hết banner');

            hideAllBannersNow();

            /* Tránh treo loading screen khi Firebase chết */
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
        if (__timer) {
            clearTimeout(__timer);
            __timer = null;
        }
    }

    /* Expose ra window */
    window.__bannerFixStartTimer   = startTimer;
    window.__bannerFixResolveTimer = resolveTimer;
    window.__bannerFixGetState = function() {
        return { resolved: __resolved, timeout: __timeout, timerActive: !!__timer };
    };

    /* ═══════════════════════════════════════════
       🎨 UPDATE ALL BANNERS — 1 hàm duy nhất quyết định banner nào hiện
       ═══════════════════════════════════════════════════════════════ */
    function updateAllBanners() {
        var expiryBanner = document.getElementById('expiryBanner');
        var demoBanner   = document.getElementById('demoBanner');

        function hideAll() {
            if (expiryBanner) expiryBanner.style.display = 'none';
            if (demoBanner)   demoBanner.style.display = 'none';
        }

        /* ── 1. TIMEOUT → ẩn hết ── */
        if (__timeout === true) { hideAll(); return; }

        /* ── 2. EMERGENCY MODE → ẩn hết ── */
        try {
            if (typeof isEmergencyModeActive === 'function' && isEmergencyModeActive()) {
                hideAll(); return;
            }
        } catch(e) {}

        /* ── 3. KHÔNG CÓ USER ── */
        var hasFirebaseUser = false;
        try { hasFirebaseUser = !!(window.auth && window.auth.currentUser); } catch(e) {}

        var cu = (typeof currentUser !== 'undefined') ? currentUser : null;

        if (!cu) {
            if (expiryBanner) expiryBanner.style.display = 'none';

            if (demoBanner && !hasFirebaseUser) {
                renderDemoBanner();
            } else if (demoBanner) {
                demoBanner.style.display = 'none';
            }
            return;
        }

        /* ── 4. ADMIN / VĨNH VIỄN → ẩn hết ── */
        var role = String(cu.role || '').toLowerCase();
        var isAdmin = (role === 'admin' || role === 'super_admin' || role === 'sub_admin');
        if (isAdmin || cu.isPermanent === true) { hideAll(); return; }

        /* ── 5. KHÔNG CÓ expiresAt → vĩnh viễn ── */
        if (!cu.expiresAt) { hideAll(); return; }

        /* ── 6. Tính ngày còn lại ── */
        var expDate = null;
        try {
            expDate = (typeof getExpiryDate === 'function')
                      ? getExpiryDate(cu.expiresAt) : null;
        } catch(e) {}

        if (!expDate || isNaN(expDate.getTime())) { hideAll(); return; }

        var daysLeft = Math.ceil((expDate.getTime() - Date.now()) / (24 * 60 * 60 * 1000));

        /* ── 7. Còn > 7 ngày → ẩn hết ── */
        if (daysLeft > 7) { hideAll(); return; }

        /* ── 8. Sắp hết hạn → hiện expiry banner ── */
        if (demoBanner) demoBanner.style.display = 'none';
        renderExpiryBannerContent(expDate, daysLeft);
    }

    /* ═══════════════════════════════════════════════════════════════
       📅 VẼ NỘI DUNG EXPIRY BANNER
       ═══════════════════════════════════════════════════════════════ */
    function renderExpiryBannerContent(expDate, daysLeft) {
        var banner = document.getElementById('expiryBanner');
        if (!banner) return;

        var isExpired  = daysLeft <= 0;
        var isUrgent   = !isExpired && daysLeft <= 3;
        var expDateStr = expDate.toLocaleDateString('vi-VN');
        var tier = (typeof currentUser !== 'undefined' && currentUser.tier) || 'active';

        /* Class màu */
        banner.classList.remove('urgent', 'expired');
        if (isExpired) banner.classList.add('expired');
        else if (isUrgent) banner.classList.add('urgent');

        /* Icon */
        var iconWrap = document.getElementById('expiryBannerIcon') ||
                       banner.querySelector('.expiry-banner-icon');
        if (iconWrap) {
            if (isExpired)     iconWrap.innerHTML = '<i class="fas fa-exclamation-triangle"></i>';
            else if (isUrgent) iconWrap.innerHTML = '<i class="fas fa-exclamation-circle"></i>';
            else               iconWrap.innerHTML = '<i class="fas fa-hourglass-half"></i>';
        }

        /* Title */
        var titleEl = document.getElementById('expiryBannerTitle') ||
                      banner.querySelector('.expiry-banner-text .title');
        if (titleEl) {
            if (isExpired)             titleEl.innerHTML = '❌ Tài khoản đã HẾT HẠN!';
            else if (isUrgent)         titleEl.innerHTML = '🔥 Chỉ còn ' + daysLeft + ' ngày!';
            else if (tier === 'trial') titleEl.innerHTML = '🎁 Trial còn ' + daysLeft + ' ngày';
            else                       titleEl.innerHTML = '⏰ Tài khoản sắp hết hạn';
        }

        /* Description */
        var descEl = document.getElementById('expiryBannerDesc') ||
                     banner.querySelector('.expiry-banner-text .desc');
        if (descEl) {
            if (isExpired) {
                descEl.innerHTML = 'Đã hết hạn vào <b>' + expDateStr + '</b> (' +
                    Math.abs(daysLeft) + ' ngày trước). Gia hạn ngay để mở khóa toàn bộ!';
            } else if (isUrgent) {
                descEl.innerHTML = 'Tài khoản sẽ hết hạn vào <b>' + expDateStr + '</b> — ' +
                    'chỉ còn <b>' + daysLeft + ' ngày</b>. Gia hạn ngay để không bị gián đoạn!';
            } else if (tier === 'trial') {
                descEl.innerHTML = 'Còn <b>' + daysLeft + ' ngày</b> dùng thử (đến <b>' +
                    expDateStr + '</b>). Nâng cấp để mở khóa toàn bộ!';
            } else {
                descEl.innerHTML = 'Còn <b>' + daysLeft + ' ngày</b> sử dụng (đến <b>' +
                    expDateStr + '</b>). Gia hạn sớm để yên tâm học tập!';
            }
        }

        /* Button */
        var contactBtn = document.getElementById('expiryContactBtn') ||
                         banner.querySelector('.expiry-banner-btn');
        if (contactBtn) {
            contactBtn.innerHTML = '<i class="fas fa-gem"></i> Gia hạn ngay';
            contactBtn.onclick = function(e) {
                e.preventDefault();
                if (typeof openRenewalModal === 'function') openRenewalModal();
            };
        }

        banner.style.display = 'flex';
    }

    /* ═══════════════════════════════════════════════════════════════
       🎁 VẼ NỘI DUNG DEMO BANNER (chỉ khi guest)
       ═══════════════════════════════════════════════════════════════ */
    function renderDemoBanner() {
        var banner = document.getElementById('demoBanner');
        if (!banner) return;

        var btn     = document.getElementById('demoBannerBtn');
        var btnText = document.getElementById('demoBannerBtnText');
        var titleEl = document.getElementById('demoBannerTitle');
        var descEl  = document.getElementById('demoBannerDesc');
        var iconEl  = banner.querySelector('.demo-banner-icon');

        var remaining = (typeof getDemoRemaining === 'function') ? getDemoRemaining() : 100;

        if (titleEl) titleEl.innerHTML = 'Đăng nhập miễn phí để mở khóa toàn bộ';
        if (descEl) {
            descEl.innerHTML = 'Đăng nhập bằng <b>Gmail</b> để xem <b>toàn bộ kho câu</b>, ' +
                'không giới hạn nghe và luyện viết.<br>' +
                'Nghe + Luyện viết còn lại hôm nay: ' +
                '<b style="color:#16a34a">' + remaining + '</b> lượt.';
        }
        if (btnText) btnText.textContent = 'Đăng nhập bằng Gmail';
        if (btn) {
            var icon = btn.querySelector('i');
            if (icon) icon.className = 'fas fa-sign-in-alt';
            btn.onclick = function(e) {
                e.preventDefault();
                e.stopPropagation();
                if (typeof showLoginModal === 'function') showLoginModal();
            };
        }
        if (iconEl) iconEl.innerHTML = '<i class="fas fa-gift"></i>';
        banner.style.background = '';
        banner.style.borderColor = '';

        banner.style.display = 'flex';
    }

    /* ═══════════════════════════════════════════════════════════════
       🔁 GHI ĐÈ HÀM CŨ
       Sau khi file này chạy, mọi lời gọi renderExpiryBanner() /
       updateDemoBannerByTier() sẽ trỏ về updateAllBanners() mới.
       ═══════════════════════════════════════════════════════════════ */
    window.updateAllBanners       = updateAllBanners;
    window.renderExpiryBanner     = updateAllBanners;
    window.updateDemoBannerByTier = updateAllBanners;

    /* ═══════════════════════════════════════════════════════════════
       🔌 HOOK VÀO CÁC ĐIỂM QUAN TRỌNG
       ═══════════════════════════════════════════════════════════════ */

    /* 1. Bắt đầu đếm khi DOM ready */
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', startTimer);
    } else {
        startTimer();
    }

    /* 2. Hook vào firebase.auth().onAuthStateChanged */
    function hookAuth() {
        try {
            if (typeof firebase === 'undefined' || !firebase.auth) return false;
            var fbAuth = firebase.auth();
            if (!fbAuth) return false;
            if (fbAuth.__bannerFixHooked) return true;

            fbAuth.onAuthStateChanged(function() {
                resolveTimer();
                /* Đợi Firestore trả lời rồi mới vẽ lại banner */
                setTimeout(function() {
                    if (typeof window.updateAllBanners === 'function') {
                        try { window.updateAllBanners(); } catch(e) {}
                    }
                }, 500);
            });
            fbAuth.__bannerFixHooked = true;
            return true;
        } catch(e) { return false; }
    }

    var hookInterval = setInterval(function() {
        if (hookAuth()) clearInterval(hookInterval);
    }, 500);
    setTimeout(function() { clearInterval(hookInterval); }, 30000);

    /* 3. Hook vào auth.signInWithPopup / signOut để reset timer */
    setTimeout(function() {
        try {
            if (typeof auth === 'undefined' || !auth) return;

            if (auth.signInWithPopup && !auth.__bannerFixSignIn) {
                var origSignIn = auth.signInWithPopup.bind(auth);
                auth.signInWithPopup = function() {
                    startTimer();
                    return origSignIn.apply(null, arguments);
                };
                auth.__bannerFixSignIn = true;
            }

            if (auth.signOut && !auth.__bannerFixSignOut) {
                var origSignOut = auth.signOut.bind(auth);
                auth.signOut = function() {
                    startTimer();
                    return origSignOut.apply(null, arguments);
                };
                auth.__bannerFixSignOut = true;
            }
        } catch(e) {}
    }, 1500);

    /* 4. Hook vào showLoginModal để reset timer */
    setTimeout(function() {
        var origShowLogin = window.showLoginModal;
        if (typeof origShowLogin === 'function' && !origShowLogin.__bannerFixWrapped) {
            window.showLoginModal = function() {
                startTimer();
                return origShowLogin.apply(this, arguments);
            };
            window.showLoginModal.__bannerFixWrapped = true;
        }
    }, 2000);

    /* 5. Re-render banner mỗi 30s để đề phòng state thay đổi âm thầm */
    setInterval(function() {
        if (typeof window.updateAllBanners === 'function') {
            try { window.updateAllBanners(); } catch(e) {}
        }
    }, 30000);

    /* ═══════════════════════════════════════════════════════════════
       🐛 DEBUG — Dùng: mở F12 → gõ __debugBannerFix()
       ═══════════════════════════════════════════════════════════════ */
    window.__debugBannerFix = function() {
        var state = window.__bannerFixGetState();
        var cu = (typeof currentUser !== 'undefined') ? currentUser : null;

        var result = {
            timeoutState: state,
            currentUser: cu ? {
                email: cu.email,
                role: cu.role,
                tier: cu.tier,
                expiresAt: cu.expiresAt,
                isPermanent: cu.isPermanent
            } : null,
            bannerVisible: {
                expiry: (function() {
                    var b = document.getElementById('expiryBanner');
                    return b ? (b.style.display !== 'none') : null;
                })(),
                demo: (function() {
                    var b = document.getElementById('demoBanner');
                    return b ? (b.style.display !== 'none') : null;
                })()
            }
        };
        console.table(result);
        return result;
    };

    console.log('[banner_fix] ✅ Module loaded — timeout guard ' +
                (TIMEOUT_MS / 1000) + 's');
})();
"""


def apply_banner_fix(js: str) -> str:
    """
    Chèn BANNER_FIX_JS vào cuối chuỗi JS của accounts_template.

    Args:
        js: Chuỗi JS từ build_all_auth() (phần tử thứ 3 của tuple trả về)

    Returns:
        Chuỗi JS đã được chèn fix ở cuối
    """
    if not js:
        return BANNER_FIX_JS
    return js + "\n\n" + BANNER_FIX_JS


def build_banner_fix_js() -> str:
    """Trả về riêng JS fix (nếu cần nhúng ở nơi khác)."""
    return BANNER_FIX_JS

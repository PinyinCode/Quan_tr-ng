# -*- coding: utf-8 -*-
"""Module đặt mật khẩu lần đầu + đăng nhập Email/Password trong loginModal.

✅ FIX (2026-10):
   - BỎ hoàn toàn elfLoginModal riêng — form email nằm thẳng trong loginModal
   - BỎ injectEmailButton() — không cần nút "Đăng nhập bằng Email" nữa
   - Nút Google chuyển xuống DƯỚI form email (ưu tiên email/password)
   - Thêm checkbox "Lưu tài khoản" (chỉ lưu email, KHÔNG lưu mật khẩu)
   - Thêm nút "Quên mật khẩu?" + switch Đăng nhập ↔ Đăng ký trong cùng modal
   - Giữ elfSetPwdModal (đặt mật khẩu lần đầu khi login Google)
"""


def build_login_fallback_css():
    return r"""
/* ═══════════════════════════════════════════════════════════
   FORM ĐĂNG NHẬP TRONG LOGIN MODAL
   ═══════════════════════════════════════════════════════════ */
.login-field{margin-bottom:.85rem;text-align:left}
.login-field label{display:block;font-size:.72rem;font-weight:700;color:#475569;margin-bottom:.35rem;text-transform:uppercase;letter-spacing:.3px}
[data-theme="dark"] .login-field label{color:#cbd5e1}
.login-field input{width:100%;padding:.75rem .9rem;border-radius:10px;border:1.5px solid #e2e8f0;background:#fff;color:#0f172a;font-size:.9rem;font-family:inherit;outline:none;transition:.15s;box-sizing:border-box}
.login-field input:focus{border-color:#7c3aed;box-shadow:0 0 0 3px rgba(124,58,237,.15)}
[data-theme="dark"] .login-field input{background:#0f172a;border-color:#475569;color:#f1f5f9}
[data-theme="dark"] .login-field input:focus{border-color:#a78bfa;box-shadow:0 0 0 3px rgba(167,139,250,.2)}

.login-pwd-wrap{position:relative}
.login-pwd-wrap input{padding-right:2.6rem}
.login-pwd-toggle{position:absolute;right:.5rem;top:50%;transform:translateY(-50%);width:32px;height:32px;border:none;background:transparent;color:#94a3b8;cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:.85rem;border-radius:8px;transition:.15s}
.login-pwd-toggle:hover{background:#f1f5f9;color:#7c3aed}
[data-theme="dark"] .login-pwd-toggle:hover{background:#334155;color:#a78bfa}

.login-extras{display:flex;align-items:center;justify-content:space-between;gap:.5rem;margin:.35rem 0 1rem;flex-wrap:wrap}
.login-checkbox{display:flex;align-items:center;gap:.45rem;font-size:.78rem;color:#475569;cursor:pointer;user-select:none;font-weight:500}
.login-checkbox input[type="checkbox"]{width:16px;height:16px;accent-color:#7c3aed;cursor:pointer;flex-shrink:0;margin:0}
[data-theme="dark"] .login-checkbox{color:#cbd5e1}
.login-link{background:none;border:none;color:#7c3aed;font-size:.78rem;font-weight:700;cursor:pointer;font-family:inherit;padding:.2rem .35rem;border-radius:6px;transition:.15s}
.login-link:hover{background:rgba(124,58,237,.1);text-decoration:underline}
[data-theme="dark"] .login-link{color:#a78bfa}
[data-theme="dark"] .login-link:hover{background:rgba(167,139,250,.15)}

.login-submit-btn{display:flex;align-items:center;justify-content:center;gap:.5rem;width:100%;padding:.85rem 1.25rem;border-radius:12px;border:none;background:linear-gradient(135deg,#7c3aed,#4f46e5);color:#fff;font-size:.92rem;font-weight:800;font-family:inherit;cursor:pointer;transition:.2s;box-shadow:0 4px 14px rgba(124,58,237,.35);letter-spacing:.2px}
.login-submit-btn:hover:not(:disabled){transform:translateY(-2px);box-shadow:0 8px 22px rgba(124,58,237,.5)}
.login-submit-btn:active:not(:disabled){transform:translateY(0) scale(.98)}
.login-submit-btn:disabled{opacity:.6;cursor:not-allowed;transform:none;box-shadow:none}

.login-divider{display:flex;align-items:center;gap:.75rem;margin:1.25rem 0;color:#94a3b8;font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.5px}
.login-divider::before,.login-divider::after{content:'';flex:1;height:1px;background:#e2e8f0}
[data-theme="dark"] .login-divider::before,[data-theme="dark"] .login-divider::after{background:#475569}

.login-switch{display:flex;align-items:center;justify-content:center;gap:.35rem;margin-top:1rem;font-size:.82rem;color:#64748b}
[data-theme="dark"] .login-switch{color:#94a3b8}

.login-error{margin-top:.85rem;padding:.7rem .9rem;border-radius:10px;font-size:.82rem;display:none;text-align:left;line-height:1.45}
.login-error.show{display:block}
.login-error.error{background:#fee2e2;color:#dc2626}
.login-error.success{background:#dcfce7;color:#15803d}
.login-error.info{background:#dbeafe;color:#1e40af}
[data-theme="dark"] .login-error.error{background:rgba(220,38,38,.2);color:#fca5a5}
[data-theme="dark"] .login-error.success{background:rgba(22,163,74,.2);color:#4ade80}
[data-theme="dark"] .login-error.info{background:rgba(59,130,246,.2);color:#93c5fd}

/* ═══════════════════════════════════════════════════════════
   MODAL ĐẶT MẬT KHẨU LẦN ĐẦU
   ═══════════════════════════════════════════════════════════ */
.elf-modal{position:fixed;inset:0;background:rgba(15,23,42,.85);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);z-index:3100;display:none;align-items:center;justify-content:center;padding:1.25rem;overflow-y:auto;animation:elfFadeIn .2s ease}
.elf-modal.show{display:flex}
@keyframes elfFadeIn{from{opacity:0}to{opacity:1}}
.elf-box{background:#fff;border-radius:20px;padding:2rem 1.75rem;max-width:440px;width:100%;max-height:calc(100vh - 2.5rem);overflow-y:auto;box-shadow:0 24px 70px rgba(0,0,0,.35);text-align:center;position:relative;animation:elfSlideUp .32s cubic-bezier(.34,1.56,.64,1)}
[data-theme="dark"] .elf-box{background:#1e293b;color:#f1f5f9}
@keyframes elfSlideUp{from{transform:translateY(30px) scale(.95);opacity:0}to{transform:translateY(0) scale(1);opacity:1}}
.elf-close{position:absolute;top:12px;right:12px;width:34px;height:34px;border-radius:50%;border:none;background:#f1f5f9;color:#475569;cursor:pointer;font-size:1rem;display:flex;align-items:center;justify-content:center;transition:.15s}
.elf-close:hover{background:#fee2e2;color:#dc2626}
[data-theme="dark"] .elf-close{background:#334155;color:#cbd5e1}
[data-theme="dark"] .elf-close:hover{background:#7f1d1d;color:#fecaca}
.elf-logo{width:64px;height:64px;background:linear-gradient(135deg,#4f46e5,#7c3aed);border-radius:18px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:1.75rem;margin:0 auto 1.25rem;box-shadow:0 8px 20px rgba(124,58,237,.35)}
.elf-logo.success{background:linear-gradient(135deg,#16a34a,#22c55e)}
.elf-title{font-size:1.3rem;color:#0f172a;margin-bottom:.4rem;font-weight:800}
[data-theme="dark"] .elf-title{color:#f1f5f9}
.elf-subtitle{color:#64748b;font-size:.85rem;margin-bottom:1.5rem;line-height:1.55}
[data-theme="dark"] .elf-subtitle{color:#94a3b8}
.elf-account-info{display:flex;align-items:center;gap:.75rem;padding:.85rem 1rem;background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;margin-bottom:1.25rem;text-align:left}
[data-theme="dark"] .elf-account-info{background:#0f172a;border-color:#334155}
.elf-account-avatar{width:42px;height:42px;border-radius:50%;background:linear-gradient(135deg,#7c3aed,#4f46e5);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:1.15rem;flex-shrink:0;overflow:hidden}
.elf-account-avatar img{width:100%;height:100%;object-fit:cover}
.elf-account-info .elf-acc-text{flex:1;min-width:0}
.elf-account-info .elf-acc-name{font-weight:700;font-size:.9rem;color:#0f172a;margin-bottom:.15rem;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.elf-account-info .elf-acc-email{font-size:.75rem;color:#64748b;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
[data-theme="dark"] .elf-account-info .elf-acc-name{color:#f1f5f9}
[data-theme="dark"] .elf-account-info .elf-acc-email{color:#94a3b8}
.elf-field{margin-bottom:.75rem;text-align:left}
.elf-field label{display:block;font-size:.72rem;font-weight:700;color:#475569;margin-bottom:.35rem;text-transform:uppercase;letter-spacing:.3px}
[data-theme="dark"] .elf-field label{color:#cbd5e1}
.elf-field input{width:100%;padding:.7rem .9rem;border-radius:10px;border:1.5px solid #e2e8f0;background:#fff;color:#0f172a;font-size:.9rem;font-family:inherit;outline:none;transition:.15s;box-sizing:border-box}
.elf-field input:focus{border-color:#4f46e5;box-shadow:0 0 0 3px rgba(79,70,229,.15)}
[data-theme="dark"] .elf-field input{background:#0f172a;border-color:#475569;color:#f1f5f9}
[data-theme="dark"] .elf-field input:focus{border-color:#818cf8;box-shadow:0 0 0 3px rgba(129,140,248,.2)}
.elf-pwd-wrap{position:relative}
.elf-pwd-wrap input{padding-right:2.6rem}
.elf-pwd-toggle{position:absolute;right:.6rem;top:50%;transform:translateY(-50%);width:32px;height:32px;border:none;background:transparent;color:#94a3b8;cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:.85rem;border-radius:8px;transition:.15s}
.elf-pwd-toggle:hover{background:#f1f5f9;color:#4f46e5}
[data-theme="dark"] .elf-pwd-toggle:hover{background:#334155;color:#a78bfa}
.elf-strength{margin-top:.35rem;display:flex;gap:.25rem}
.elf-strength-bar{flex:1;height:4px;border-radius:2px;background:#e2e8f0;transition:.25s}
.elf-strength-bar.weak{background:#dc2626}
.elf-strength-bar.medium{background:#f59e0b}
.elf-strength-bar.strong{background:#16a34a}
.elf-btn{display:flex;align-items:center;justify-content:center;gap:.5rem;width:100%;padding:.85rem 1.25rem;border-radius:12px;border:none;background:linear-gradient(135deg,#4f46e5,#7c3aed);color:#fff;font-size:.92rem;font-weight:800;font-family:inherit;cursor:pointer;transition:.2s;box-shadow:0 4px 14px rgba(124,58,237,.35);letter-spacing:.2px;margin-top:.25rem}
.elf-btn:hover:not(:disabled){transform:translateY(-2px);box-shadow:0 8px 22px rgba(124,58,237,.5)}
.elf-btn:active:not(:disabled){transform:translateY(0) scale(.98)}
.elf-btn:disabled{opacity:.6;cursor:not-allowed;transform:none;box-shadow:none}
.elf-btn.ghost{background:transparent;color:#64748b;border:none;box-shadow:none;font-weight:600;font-size:.82rem}
.elf-btn.ghost:hover:not(:disabled){color:#4f46e5;text-decoration:underline}
[data-theme="dark"] .elf-btn.ghost{color:#94a3b8}
[data-theme="dark"] .elf-btn.ghost:hover{color:#a78bfa}
.elf-msg{padding:.75rem .9rem;border-radius:10px;font-size:.82rem;margin-top:1rem;display:none;text-align:left;line-height:1.45}
.elf-msg.show{display:block}
.elf-msg.error{background:#fee2e2;color:#dc2626}
.elf-msg.success{background:#dcfce7;color:#15803d}
[data-theme="dark"] .elf-msg.error{background:rgba(220,38,38,.2);color:#fca5a5}
[data-theme="dark"] .elf-msg.success{background:rgba(22,163,74,.2);color:#4ade80}
.elf-tip-banner{display:flex;align-items:flex-start;gap:.6rem;padding:.7rem .85rem;background:linear-gradient(135deg,rgba(79,70,229,.08),rgba(124,58,237,.06));border:1px solid rgba(124,58,237,.25);border-radius:12px;margin-bottom:1.25rem;font-size:.78rem;color:#5b21b6;line-height:1.5;text-align:left}
[data-theme="dark"] .elf-tip-banner{background:linear-gradient(135deg,rgba(124,58,237,.15),rgba(79,70,229,.1));border-color:rgba(165,180,252,.3);color:#c4b5fd}
.elf-tip-banner i{color:#7c3aed;margin-top:.15rem;flex-shrink:0;font-size:1rem}
.elf-tip-banner b{color:#4f46e5}
[data-theme="dark"] .elf-tip-banner b{color:#a78bfa}
.elf-footer{margin-top:1.25rem;padding-top:1rem;border-top:1px solid #e2e8f0;font-size:.72rem;color:#94a3b8;line-height:1.55;text-align:center}
.elf-footer b{color:#4f46e5}
[data-theme="dark"] .elf-footer{border-color:#475569;color:#94a3b8}
[data-theme="dark"] .elf-footer b{color:#a78bfa}
.elf-spinner{display:inline-block;width:15px;height:15px;border:2px solid rgba(255,255,255,.35);border-top-color:#fff;border-radius:50%;animation:elfSpin .7s linear infinite}
@keyframes elfSpin{to{transform:rotate(360deg)}}
@media(max-width:500px){
.elf-box{padding:1.5rem 1.25rem;border-radius:16px}
.elf-logo{width:56px;height:56px;font-size:1.5rem}
.elf-title{font-size:1.15rem}
.elf-subtitle{font-size:.8rem}
.elf-btn{font-size:.88rem;padding:.8rem 1.1rem}
}
"""


def build_login_fallback_html():
    return r"""
<div class="elf-modal" id="elfSetPwdModal">
    <div class="elf-box">
        <button class="elf-close" id="elfSetPwdClose" type="button" aria-label="Đóng sau">
            <i class="fas fa-times"></i>
        </button>
        <div class="elf-logo"><i class="fas fa-shield-halved"></i></div>
        <div class="elf-title">Đặt mật khẩu đăng nhập</div>
        <div class="elf-subtitle">Đặt mật khẩu để lần sau có thể đăng nhập bằng email ngay cả khi Google gặp sự cố.</div>
        <div class="elf-account-info">
            <div class="elf-account-avatar" id="elfSetAvatar">?</div>
            <div class="elf-acc-text">
                <div class="elf-acc-name" id="elfSetName">-</div>
                <div class="elf-acc-email" id="elfSetEmail">-</div>
            </div>
        </div>
        <div class="elf-tip-banner">
            <i class="fas fa-lightbulb"></i>
            <div><b>Gợi ý:</b> Đặt mật khẩu dễ nhớ (tối thiểu 6 ký tự) để đăng nhập nhanh hơn. Bạn vẫn có thể dùng Google như bình thường.</div>
        </div>
        <form id="elfSetPwdForm" autocomplete="on" novalidate>
            <div class="elf-field">
                <label>Mật khẩu mới</label>
                <div class="elf-pwd-wrap">
                    <input type="password" id="elfSetPwd1" placeholder="Tối thiểu 6 ký tự" autocomplete="new-password" required minlength="6">
                    <button type="button" class="elf-pwd-toggle" data-elf-pwd="elfSetPwd1" aria-label="Hiện/ẩn mật khẩu"><i class="fas fa-eye"></i></button>
                </div>
                <div class="elf-strength" id="elfSetStrength">
                    <div class="elf-strength-bar"></div>
                    <div class="elf-strength-bar"></div>
                    <div class="elf-strength-bar"></div>
                </div>
            </div>
            <div class="elf-field">
                <label>Nhập lại mật khẩu</label>
                <div class="elf-pwd-wrap">
                    <input type="password" id="elfSetPwd2" placeholder="Nhập lại mật khẩu" autocomplete="new-password" required minlength="6">
                    <button type="button" class="elf-pwd-toggle" data-elf-pwd="elfSetPwd2" aria-label="Hiện/ẩn mật khẩu"><i class="fas fa-eye"></i></button>
                </div>
            </div>
            <button type="submit" class="elf-btn" id="elfSetPwdSubmit">
                <i class="fas fa-check"></i> Lưu mật khẩu
            </button>
            <button type="button" class="elf-btn ghost" id="elfSetPwdSkip" style="margin-top:.5rem;">Để sau</button>
        </form>
        <div class="elf-msg" id="elfSetMsg"></div>
        <div class="elf-footer">
            <i class="fas fa-lock" style="color:#4f46e5"></i>
            Mật khẩu được gắn vào <b>cùng tài khoản Google</b> của bạn — không tạo tài khoản mới.
        </div>
    </div>
</div>
"""


def build_login_fallback_js():
    return r"""
(function() {
    'use strict';

    var PWD_ASKED_KEY = 'elf_pwd_asked_';
    var SAVED_EMAIL_KEY = 'elf_saved_email';

    function $(id) { return document.getElementById(id); }

    function waitAuth(cb) {
        var tries = 0;
        var t = setInterval(function() {
            tries++;
            try {
                if (typeof auth !== 'undefined' && auth && typeof firebase !== 'undefined') {
                    clearInterval(t);
                    cb();
                    return;
                }
            } catch(e) {}
            if (tries > 40) clearInterval(t);
        }, 250);
    }

    /* ═══════════════════════════════════════════════════════════
       MESSAGE HELPERS
       ═══════════════════════════════════════════════════════════ */
    function showLoginMsg(msg, type) {
        var el = $('loginError');
        if (!el) return;
        el.className = 'login-error show' + (type ? ' ' + type : '');
        el.innerHTML = msg;
    }
    function clearLoginMsg() {
        var el = $('loginError');
        if (!el) return;
        el.className = 'login-error';
        el.innerHTML = '';
    }
    function showElfMsg(msg, type) {
        var el = $('elfSetMsg');
        if (!el) return;
        el.className = 'elf-msg show' + (type ? ' ' + type : '');
        el.innerHTML = msg;
    }
    function clearElfMsg() {
        var el = $('elfSetMsg');
        if (!el) return;
        el.className = 'elf-msg';
        el.innerHTML = '';
    }

    /* ═══════════════════════════════════════════════════════════
       LƯU EMAIL (KHÔNG LƯU MẬT KHẨU)
       ═══════════════════════════════════════════════════════════ */
    function saveEmailHint(email, remember) {
        try {
            if (remember && email) {
                localStorage.setItem(SAVED_EMAIL_KEY, String(email).toLowerCase().trim());
            } else {
                localStorage.removeItem(SAVED_EMAIL_KEY);
            }
        } catch(e) {}
    }
    function restoreEmailHint() {
        try {
            var saved = localStorage.getItem(SAVED_EMAIL_KEY);
            if (!saved) return;
            var inp = $('loginEmail');
            if (inp && !inp.value) inp.value = saved;
            var cb = $('loginSaveAccount');
            if (cb) cb.checked = true;
        } catch(e) {}
    }

    /* ═══════════════════════════════════════════════════════════
       PASSWORD TOGGLES
       ═══════════════════════════════════════════════════════════ */
    function bindPwdToggles() {
        document.querySelectorAll('.login-pwd-toggle, .elf-pwd-toggle').forEach(function(btn) {
            if (btn.__elfBound) return;
            btn.__elfBound = true;
            btn.addEventListener('click', function(e) {
                e.preventDefault();
                var id = this.dataset.pwd || this.dataset.elfPwd;
                var inp = $(id);
                if (!inp) return;
                var isPwd = inp.type === 'password';
                inp.type = isPwd ? 'text' : 'password';
                var icon = this.querySelector('i');
                if (icon) icon.className = isPwd ? 'fas fa-eye-slash' : 'fas fa-eye';
            });
        });
    }

    /* ═══════════════════════════════════════════════════════════
       SWITCH ĐĂNG NHẬP ↔ ĐĂNG KÝ
       ═══════════════════════════════════════════════════════════ */
    var currentForm = 'login';

    function updateLoginSwitchUI() {
        var txt = $('loginSwitchText');
        var btn = $('loginSwitchBtn');
        var title = $('loginTitle');
        var subtitle = $('loginSubtitle');
        if (currentForm === 'login') {
            if (txt) txt.textContent = 'Chưa có tài khoản?';
            if (btn) btn.textContent = 'Đăng ký ngay';
            if (title) title.textContent = 'Đăng nhập để mở khóa';
            if (subtitle) subtitle.innerHTML = 'Đăng nhập để sử dụng <b>toàn bộ câu</b>, tất cả bộ lọc HSK1-6, chủ đề đầy đủ, luyện viết không giới hạn và nhiều tính năng khác.';
        } else {
            if (txt) txt.textContent = 'Đã có tài khoản?';
            if (btn) btn.textContent = 'Đăng nhập';
            if (title) title.textContent = 'Tạo tài khoản mới';
            if (subtitle) subtitle.innerHTML = 'Đăng ký để nhận <b>3 ngày dùng thử miễn phí</b> — không cần thẻ tín dụng.';
        }
    }

    function showLoginForm() {
        currentForm = 'login';
        var lf = $('loginForm');
        var rf = $('registerForm');
        var gBtn = $('googleLoginBtn');
        var div = document.querySelector('.login-divider');
        if (lf) lf.style.display = '';
        if (rf) rf.style.display = 'none';
        if (gBtn) gBtn.style.display = '';
        if (div) div.style.display = '';
        clearLoginMsg();
        updateLoginSwitchUI();
    }

    function showRegisterForm() {
        currentForm = 'register';
        var lf = $('loginForm');
        var rf = $('registerForm');
        var gBtn = $('googleLoginBtn');
        var div = document.querySelector('.login-divider');
        if (lf) lf.style.display = 'none';
        if (rf) rf.style.display = '';
        if (gBtn) gBtn.style.display = 'none';
        if (div) div.style.display = 'none';
        clearLoginMsg();
        updateLoginSwitchUI();
        setTimeout(function() {
            var inp = $('regEmail');
            if (inp) inp.focus();
        }, 100);
    }

    /* ═══════════════════════════════════════════════════════════
       ĐĂNG NHẬP EMAIL/PASSWORD
       ═══════════════════════════════════════════════════════════ */
    async function doEmailLogin(e) {
        if (e) e.preventDefault();
        var emailEl = $('loginEmail');
        var pwdEl = $('loginPwd');
        var rememberEl = $('loginSaveAccount');
        var btn = $('loginSubmitBtn');
        if (!emailEl || !pwdEl) return;

        var email = (emailEl.value || '').trim().toLowerCase();
        var pwd = pwdEl.value || '';
        var remember = rememberEl ? rememberEl.checked : true;

        if (!email || !email.includes('@')) {
            showLoginMsg('Email không hợp lệ.', 'error');
            return;
        }
        if (!pwd) {
            showLoginMsg('Vui lòng nhập mật khẩu.', 'error');
            return;
        }

        var orig = btn.innerHTML;
        btn.disabled = true;
        btn.innerHTML = '<span class="elf-spinner"></span> Đang đăng nhập...';

        try {
            var persistence = remember
                ? firebase.auth.Auth.Persistence.LOCAL
                : firebase.auth.Auth.Persistence.SESSION;
            try { await auth.setPersistence(persistence); } catch(_e) {}

            await auth.signInWithEmailAndPassword(email, pwd);

            saveEmailHint(email, remember);
            showLoginMsg('✅ Đăng nhập thành công!', 'success');

            setTimeout(function() {
                var m = $('loginModal');
                if (m) m.classList.remove('show');
            }, 600);

        } catch (err) {
            console.error('[Login]', err);
            var msg = 'Lỗi: ' + (err.code || err.message);
            if (err.code === 'auth/user-not-found') {
                msg = 'Không tìm thấy tài khoản với email này.<br>Bạn có muốn <b>Đăng ký</b>?';
            } else if (err.code === 'auth/wrong-password' || err.code === 'auth/invalid-credential') {
                msg = 'Sai mật khẩu. Vui lòng thử lại hoặc bấm <b>Quên mật khẩu</b>.';
            } else if (err.code === 'auth/invalid-email') {
                msg = 'Email không đúng định dạng.';
            } else if (err.code === 'auth/too-many-requests') {
                msg = 'Bạn đã thử quá nhiều lần. Vui lòng đợi vài phút.';
            } else if (err.code === 'auth/operation-not-allowed') {
                msg = '⚠️ Chưa bật <b>Email/Password</b> trên Firebase Console.';
            } else if (err.code === 'auth/invalid-login-credentials') {
                msg = 'Email hoặc mật khẩu không đúng.<br>Nếu bạn từng đăng nhập bằng Google, hãy dùng <b>Quên mật khẩu</b> để tạo mật khẩu mới.';
            }
            showLoginMsg(msg, 'error');
        } finally {
            btn.disabled = false;
            btn.innerHTML = orig;
        }
    }

    /* ═══════════════════════════════════════════════════════════
       ĐĂNG KÝ EMAIL/PASSWORD
       ═══════════════════════════════════════════════════════════ */
    async function doEmailRegister(e) {
        if (e) e.preventDefault();
        var emailEl = $('regEmail');
        var nameEl = $('regName');
        var pwdEl = $('regPwd');
        var pwd2El = $('regPwd2');
        var rememberEl = $('regSaveAccount');
        var btn = $('registerSubmitBtn');
        if (!emailEl || !pwdEl || !pwd2El) return;

        var email = (emailEl.value || '').trim().toLowerCase();
        var name = (nameEl ? nameEl.value : '').trim();
        var pwd = pwdEl.value || '';
        var pwd2 = pwd2El.value || '';
        var remember = rememberEl ? rememberEl.checked : true;

        if (!email || !email.includes('@')) {
            showLoginMsg('Email không hợp lệ.', 'error');
            return;
        }
        if (pwd.length < 6) {
            showLoginMsg('Mật khẩu phải từ 6 ký tự trở lên.', 'error');
            return;
        }
        if (pwd !== pwd2) {
            showLoginMsg('Mật khẩu nhập lại không khớp.', 'error');
            return;
        }

        var orig = btn.innerHTML;
        btn.disabled = true;
        btn.innerHTML = '<span class="elf-spinner"></span> Đang tạo tài khoản...';

        try {
            var persistence = remember
                ? firebase.auth.Auth.Persistence.LOCAL
                : firebase.auth.Auth.Persistence.SESSION;
            try { await auth.setPersistence(persistence); } catch(_e) {}

            var cred = await auth.createUserWithEmailAndPassword(email, pwd);
            if (name && cred.user) {
                try { await cred.user.updateProfile({ displayName: name }); } catch(_e) {}
            }

            saveEmailHint(email, remember);
            showLoginMsg('✅ Tạo tài khoản thành công! Đang đăng nhập...', 'success');

            setTimeout(function() {
                var m = $('loginModal');
                if (m) m.classList.remove('show');
            }, 800);

        } catch (err) {
            console.error('[Register]', err);
            var msg = 'Lỗi: ' + (err.code || err.message);
            if (err.code === 'auth/email-already-in-use') {
                msg = 'Email này đã được đăng ký.<br>Vui lòng chuyển sang <b>Đăng nhập</b>.';
            } else if (err.code === 'auth/weak-password') {
                msg = 'Mật khẩu quá yếu. Vui lòng dùng mật khẩu từ 6 ký tự.';
            } else if (err.code === 'auth/operation-not-allowed') {
                msg = '⚠️ Chưa bật <b>Email/Password</b> trên Firebase Console.';
            }
            showLoginMsg(msg, 'error');
        } finally {
            btn.disabled = false;
            btn.innerHTML = orig;
        }
    }

    /* ═══════════════════════════════════════════════════════════
       QUÊN MẬT KHẨU
       ═══════════════════════════════════════════════════════════ */
    async function doForgot() {
        var emailEl = $('loginEmail');
        var email = emailEl ? (emailEl.value || '').trim().toLowerCase() : '';
        if (!email || !email.includes('@')) {
            showLoginMsg('Vui lòng nhập email vào ô <b>Email</b> phía trên, rồi bấm lại "Quên mật khẩu".', 'error');
            return;
        }
        if (!confirm('Gửi email khôi phục mật khẩu đến:\n\n' + email + ' ?')) return;

        try {
            await auth.sendPasswordResetEmail(email);
            showLoginMsg('✅ Đã gửi email khôi phục!<br>Kiểm tra hộp thư (kể cả mục Spam).', 'success');
        } catch (err) {
            console.error('[Forgot]', err);
            var msg = 'Lỗi: ' + (err.code || err.message);
            if (err.code === 'auth/user-not-found') {
                msg = 'Không tìm thấy tài khoản với email này.';
            }
            showLoginMsg(msg, 'error');
        }
    }

    /* ═══════════════════════════════════════════════════════════
       ĐẶT MẬT KHẨU LẦN ĐẦU (sau khi login Google)
       ═══════════════════════════════════════════════════════════ */
    function openSetPwdModal() {
        var m = $('elfSetPwdModal');
        if (!m) return;
        m.classList.add('show');
        clearElfMsg();
        try {
            var u = auth.currentUser;
            if (u) {
                var av = $('elfSetAvatar');
                var nm = $('elfSetName');
                var em = $('elfSetEmail');
                if (em) em.textContent = u.email || '';
                var name = u.displayName || (u.email || '').split('@')[0];
                if (nm) nm.textContent = name;
                if (av) {
                    if (u.photoURL) av.innerHTML = '<img src="' + u.photoURL + '" alt="">';
                    else av.textContent = (name.charAt(0) || '?').toUpperCase();
                }
            }
        } catch(e) {}
        setTimeout(function() {
            var inp = $('elfSetPwd1');
            if (inp) inp.focus();
        }, 150);
    }

    function closeSetPwdModal() {
        var m = $('elfSetPwdModal');
        if (!m) return;
        m.classList.remove('show');
        clearElfMsg();
    }

    function userHasPassword(user) {
        if (!user) return false;
        try {
            var providers = user.providerData || [];
            for (var i = 0; i < providers.length; i++) {
                if (providers[i].providerId === 'password') return true;
            }
        } catch(e) {}
        return false;
    }

    function userHasGoogle(user) {
        if (!user) return false;
        try {
            var providers = user.providerData || [];
            for (var i = 0; i < providers.length; i++) {
                if (providers[i].providerId === 'google.com') return true;
            }
        } catch(e) {}
        return false;
    }

    function anyBusyModalOpen() {
        var busy = ['adminModal', 'importModal', 'editExpiryModal', 'changeNameModal',
                    'renewalModal', 'permissionModal', 'onboardingModal', 'voiceModal',
                    'writerModal', 'practiceFullModal', 'chatModal', 'loginModal',
                    'dvlVerifyModal', 'dvlModal'];
        for (var i = 0; i < busy.length; i++) {
            var m = $(busy[i]);
            if (m && m.classList.contains('show')) return true;
        }
        return false;
    }

    function checkAndAskSetPassword(user) {
        if (!user || !user.email) return;
        if (!userHasGoogle(user)) return;
        if (userHasPassword(user)) return;

        var email = user.email.toLowerCase();
        try {
            if (sessionStorage.getItem(PWD_ASKED_KEY + email) === '1') return;
        } catch(e) {}

        if (anyBusyModalOpen()) {
            /* Đợi 1.5s rồi check lại — KHÔNG đệ quy vô hạn */
            setTimeout(function() { checkAndAskSetPassword(user); }, 1500);
            return;
        }

        try { sessionStorage.setItem(PWD_ASKED_KEY + email, '1'); } catch(e) {}

        setTimeout(openSetPwdModal, 1500);
    }

    async function handleSetPassword(e) {
        if (e) e.preventDefault();

        var p1 = ($('elfSetPwd1') || {}).value || '';
        var p2 = ($('elfSetPwd2') || {}).value || '';
        var btn = $('elfSetPwdSubmit');

        if (p1.length < 6) {
            showElfMsg('Mật khẩu phải từ 6 ký tự trở lên.', 'error');
            return;
        }
        if (p1 !== p2) {
            showElfMsg('Mật khẩu nhập lại không khớp.', 'error');
            return;
        }

        var user = auth.currentUser;
        if (!user || !user.email) {
            showElfMsg('Không tìm thấy thông tin tài khoản. Vui lòng thử lại.', 'error');
            return;
        }

        var orig = btn.innerHTML;
        btn.disabled = true;
        btn.innerHTML = '<span class="elf-spinner"></span> Đang lưu...';

        try {
            var credential = firebase.auth.EmailAuthProvider.credential(user.email, p1);
            await user.linkWithCredential(credential);

            try { sessionStorage.removeItem(PWD_ASKED_KEY + user.email.toLowerCase()); } catch(e) {}

            showElfMsg('✅ Đặt mật khẩu thành công!<br>Lần sau bạn có thể đăng nhập bằng Email.', 'success');

            setTimeout(function() {
                closeSetPwdModal();
                if (typeof showUserChangedToast === 'function') {
                    showUserChangedToast('🔐 Đã đặt mật khẩu đăng nhập', 'success');
                }
            }, 1500);

        } catch (err) {
            console.error('[ELF SetPwd]', err);
            var msg = 'Lỗi: ' + (err.code || err.message);
            if (err.code === 'auth/provider-already-linked') {
                msg = 'Tài khoản này đã có mật khẩu. Không cần đặt lại.';
            } else if (err.code === 'auth/email-already-in-use') {
                msg = 'Email này đã có mật khẩu riêng. Vui lòng dùng <b>Quên mật khẩu</b> để đặt lại.';
            } else if (err.code === 'auth/weak-password') {
                msg = 'Mật khẩu quá yếu. Vui lòng dùng mật khẩu từ 6 ký tự.';
            } else if (err.code === 'auth/requires-recent-login') {
                msg = 'Phiên đăng nhập đã cũ.<br>Vui lòng đăng xuất và đăng nhập lại Google.';
            } else if (err.code === 'auth/credential-already-in-use') {
                msg = 'Email này đã được liên kết với tài khoản khác.<br>Vui lòng liên hệ hỗ trợ hoặc dùng <b>Quên mật khẩu</b>.';
            } else if (err.code === 'auth/operation-not-allowed') {
                msg = '⚠️ Chưa bật <b>Email/Password</b> trên Firebase Console.';
            }
            showElfMsg(msg, 'error');
        } finally {
            btn.disabled = false;
            btn.innerHTML = orig;
        }
    }

    function handleSkipSetPassword() {
        closeSetPwdModal();
    }

    function updateStrength(pwd) {
        var bars = document.querySelectorAll('#elfSetStrength .elf-strength-bar');
        if (!bars.length) return;
        var score = 0;
        if (pwd.length >= 6) score++;
        if (pwd.length >= 10) score++;
        if (/[A-Z]/.test(pwd) && /[a-z]/.test(pwd)) score++;
        if (/[0-9]/.test(pwd)) score++;
        if (/[^A-Za-z0-9]/.test(pwd)) score++;

        var level = 0;
        if (score >= 4) level = 3;
        else if (score >= 3) level =  ═2;
        else if (score >= 2) level = 1;

        bars.forEach(function(b, i) {
            b.className = 'elf-strength-bar';
            if (i < level) {
                if (level === 1) b.classList.add('weak');
                else if (level === 2) b.classList.add('medium');
                else if (level === 3) b.classList.add('strong');
            }
        });
    }

    /* ═══════════════════════════════════════════════════════════
       NÚT GOOGLE trong loginModal
      ══════════════════════════════════════════════════════════ */
    function bindGoogleButton() {
        var btn = $('googleLoginBtn');
        if (!btn || btn.__elfBound) return;
        btn.__elfBound = true;

        btn.addEventListener('click', async function(e) {
            e.preventDefault();
            e.stopPropagation();

            var orig = btn.innerHTML;
            btn.disabled = true;
            btn.innerHTML = '<span class="elf-spinner"></span> Đang đăng nhập...';

            var provider = new firebase.auth.GoogleAuthProvider();
            provider.setCustomParameters({ prompt: 'select_account' });

            try {
                var result = await auth.signInWithPopup(provider);
                if (result && result.user) {
                    var m = $('loginModal');
                    if (m) m.classList.remove('show');
                }
            } catch (err) {
                console.error('[Google]', err);
                var msg = '';
                if (err.code === 'auth/popup-closed-by-user' ||
                    err.code === 'auth/cancelled-popup-request') {
                    /* Im lặng */
                } else if (err.code === 'auth/popup-blocked') {
                    msg = 'Trình duyệt đã chặn popup. Vui lòng cho phép popup rồi thử lại.';
                } else if (err.code === 'auth/web-storage-unsupported' ||
                           (err.message && err.message.indexOf('missing initial state') !== -1)) {
                    msg = 'Trình duyệt đang chặn storage. Vui lòng tắt ẩn danh hoặc cho phép cookie.';
                } else {
                    msg = 'Lỗi đăng nhập Google: <b>' + (err.code || err.message) + '</b>';
                }
                if (msg) showLoginMsg(msg, 'error');
            } finally {
                btn.disabled = false;
                btn.innerHTML = orig;
            }
        });
    }

    /* ═══════════════════════════════════════════════════════════
       HOOK: mở loginModal → reset form
       ═══════════════════════════════════════════════════════════ */
    function hookLoginModalOpen() {
        var origShow = window.showLoginModal;
        if (typeof origShow === 'function' && !origShow.__elfHooked) {
            window.showLoginModal = function() {
                currentForm = 'login';
                showLoginForm();
                restoreEmailHint();
                clearLoginMsg();
                origShow.apply(this, arguments);
            };
            window.showLoginModal.__elfHooked = true;
        }
    }

    /* ═══════════════════════════════════════════════════════════
       INIT
       ═══════════════════════════════════════════════════════════ */
    function initElf() {
        /* ═══ LOGIN FORM ═══ */
        var lf = $('loginForm');
        if (lf && !lf.__elfBound) {
            lf.__elfBound = true;
            lf.addEventListener('submit', doEmailLogin);
        }

        /* ═══ REGISTER FORM ═══ */
        var rf = $('registerForm');
        if (rf && !rf.__elfBound) {
            rf.__elfBound = true;
            rf.addEventListener('submit', doEmailRegister);
        }

        /* ═══ SWITCH LOGIN ↔ REGISTER ═══ */
        var swBtn = $('loginSwitchBtn');
        if (swBtn && !swBtn.__elfBound) {
            swBtn.__elfBound = true;
            swBtn.addEventListener('click', function() {
                if (currentForm === 'login') showRegisterForm();
                else showLoginForm();
            });
        }

        /* ═══ FORGOT PASSWORD ═══ */
        var forgot = $('loginForgotBtn');
        if (forgot && !forgot.__elfBound) {
            forgot.__elfBound = true;
            forgot.addEventListener('click', doForgot);
        }

        /* ═══ GOOGLE BUTTON ═══ */
        bindGoogleButton();

        /* ═══ PWD TOGGLES ═══ */
        bindPwdToggles();

        /* ═══ SET PASSWORD MODAL (sau khi login Google) ═══ */
        var closeBtn = $('elfSetPwdClose');
        if (closeBtn && !closeBtn.__elfBound) {
            closeBtn.__elfBound = true;
            closeBtn.addEventListener('click', handleSkipSetPassword);
        }
        var pwdModal = $('elfSetPwdModal');
        if (pwdModal && !pwdModal.__elfBound) {
            pwdModal.__elfBound = true;
            pwdModal.addEventListener('click', function(e) {
                if (e.target === pwdModal) handleSkipSetPassword();
            });
        }
        var skipBtn = $('elfSetPwdSkip');
        if (skipBtn && !skipBtn.__elfBound) {
            skipBtn.__elfBound = true;
            skipBtn.addEventListener('click', handleSkipSetPassword);
        }
        var setForm = $('elfSetPwdForm');
        if (setForm && !setForm.__elfBound) {
            setForm.__elfBound = true;
            setForm.addEventListener('submit', handleSetPassword);
        }
        var pwd1 = $('elfSetPwd1');
        if (pwd1 && !pwd1.__elfBound) {
            pwd1.__elfBound = true;
            pwd1.addEventListener('input', function() {
                updateStrength(this.value);
            });
        }

        /* ═══ HOOK loginModal OPEN ═══ */
        hookLoginModalOpen();

        /* ═══ RESTORE EMAIL khi load ═══ */
        restoreEmailHint();

        /* ═══ AUTH STATE — check đặt mật khẩu ═══ */
        if (auth && !auth.__elfHooked) {
            auth.__elfHooked = true;
            auth.onAuthStateChanged(function(user) {
                checkAndAskSetPassword(user);
            });
        }

        /* ═══ ESC key ═══ */
        document.addEventListener('keydown', function(e) {
            if (e.key !== 'Escape') return;
            var m1 = $('elfSetPwdModal');
            if (m1 && m1.classList.contains('show')) {
                handleSkipSetPassword();
                return;
            }
        });

        /* ═══ Retry hook login modal nếu chưa có ═══ */
        var tries = 0;
        var retry = setInterval(function() {
            tries++;
            hookLoginModalOpen();
            bindGoogleButton();
            bindPwdToggles();
            if (tries > 30) clearInterval(retry);
        }, 500);
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded',(SAVED function() {
            waitAuth(initElf);
        });
    } else {
        waitAuth(initElf);
    }

    /* ═══════════════════════════════════════════════════════════
       PUBLIC API
       ═══════════════════════════════════════════════════════════ */
    window.__elfOpenSetPwd = openSetPwdModal;
    window.__elfDebug = {
        openSetPwd: openSetPwdModal,
        hasPassword: function() {
            return auth && auth.currentUser ? userHasPassword(auth.currentUser) : false;
        },
        resetAskedFlag: function() {
            try {
                var u = auth.currentUser;
                if (u && u.email) {
                    sessionStorage.removeItem(PWD_ASKED_KEY + u.email.toLowerCase());
                }
            } catch(e) {}
        },
        clearSavedEmail: function() {
            try { localStorage.removeItem_EMAIL_KEY); } catch(e) {}
        },
        showRegister: showRegisterForm,
        showLogin: showLoginForm
    };

    console.log('[Login Fallback] Module loaded OK — form email trong loginModal');
})();
"""


if __name__ == "__main__":
    css = build_login_fallback_css()
    html = build_login_fallback_html()
    js = build_login_fallback_js()

    print("CSS:  %d ky tu" % len(css))
    print("HTML: %d ky tu" % len(html))
    print("JS:   %d ky tu" % len(js))

    assert 'elfSetPwdModal' in html
    assert 'elfLoginModal' not in html, "elfLoginModal phải bị xóa"
    assert 'injectEmailButton' not in js, "injectEmailButton phải bị xóa"
    assert 'linkWithCredential' in js
    assert 'signInWithEmailAndPassword' in js
    assert 'sendPasswordResetEmail' in js
    assert 'bindGoogleButton' in js
    assert 'loginForm' in js
    assert 'registerForm' in sang js

    print("Module san dung")

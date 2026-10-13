# -*- coding: utf-8 -*-
"""Module giới hạn 2 thiết bị — xác nhận qua OTP (Gmail API qua server bank).

✅ Tính năng:
   - Super admin BYPASS device limit
   - Super admin VẪN THẤY nút "Yêu cầu chờ duyệt" + duyệt được
   - Máy thứ 3 login → gửi OTP qua server → user nhập OTP 6 số
   - Fallback: admin duyệt thủ công
   - Không còn phụ thuộc Firebase Email Link (5 mail/ngày)
"""

# ⚠️ SỬA URL SERVER CỦA BẠN
SERVER_URL = 'https://bank-email-server.onrender.com'


def build_device_css():
    return r"""
.dvl-modal{position:fixed;inset:0;background:rgba(15,23,42,.85);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);z-index:4300;display:none;align-items:center;justify-content:center;padding:1.25rem;overflow-y:auto;animation:dvlFadeIn .2s ease}
.dvl-modal.show{display:flex}
@keyframes dvlFadeIn{from{opacity:0}to{opacity:1}}
.dvl-box{background:var(--surface);border-radius:20px;padding:1.75rem 1.5rem;max-width:560px;width:100%;max-height:calc(100vh - 2.5rem);overflow-y:auto;box-shadow:0 24px 70px rgba(0,0,0,.35);text-align:left;position:relative;animation:dvlSlideUp .32s cubic-bezier(.34,1.56,.64,1);color:var(--text)}
@keyframes dvlSlideUp{from{transform:translateY(30px) scale(.95);opacity:0}to{transform:translateY(0) scale(1);opacity:1}}
.dvl-close{position:absolute;top:12px;right:12px;width:34px;height:34px;border-radius:50%;border:none;background:var(--surface-2);color:var(--text-2);cursor:pointer;font-size:1rem;display:flex;align-items:center;justify-content:center;transition:.15s}
.dvl-close:hover{background:var(--danger-light);color:var(--danger)}
.dvl-icon{width:56px;height:56px;border-radius:16px;background:linear-gradient(135deg,#06b6d4,#0891b2);color:#fff;font-size:1.5rem;display:flex;align-items:center;justify-content:center;margin-bottom:1rem;box-shadow:0 8px 20px rgba(6,182,212,.35)}
.dvl-icon.warn{background:linear-gradient(135deg,#f59e0b,#d97706);box-shadow:0 8px 20px rgba(245,158,11,.35)}
.dvl-icon.danger{background:linear-gradient(135deg,#dc2626,#b91c1c);box-shadow:0 8px 20px rgba(220,38,38,.35)}
.dvl-icon.mail{background:linear-gradient(135deg,#4f46e5,#7c3aed);box-shadow:0 8px 20px rgba(124,58,237,.35)}
.dvl-title{font-size:1.2rem;font-weight:800;margin-bottom:.4rem;color:var(--text)}
.dvl-subtitle{font-size:.82rem;color:var(--text-2);margin-bottom:1.25rem;line-height:1.55}
.dvl-email-highlight{display:inline-block;padding:.15rem .55rem;background:linear-gradient(135deg,rgba(79,70,229,.12),rgba(124,58,237,.08));border:1px solid rgba(124,58,237,.3);border-radius:6px;color:#4f46e5;font-weight:800;font-size:.85rem;word-break:break-all}
[data-theme="dark"] .dvl-email-highlight{color:#a78bfa;background:rgba(124,58,237,.2)}
.dvl-count-box{display:flex;align-items:center;justify-content:center;gap:.75rem;padding:1rem;background:linear-gradient(135deg,rgba(6,182,212,.08),rgba(8,145,178,.05));border:1.5px solid rgba(6,182,212,.3);border-radius:14px;margin-bottom:1.25rem}
.dvl-count-box.warn{background:linear-gradient(135deg,rgba(245,158,11,.1),rgba(217,119,6,.05));border-color:rgba(245,158,11,.4)}
.dvl-count-num{font-size:2rem;font-weight:900;color:#0891b2;line-height:1;min-width:2.5rem;text-align:center}
.dvl-count-box.warn .dvl-count-num{color:#d97706}
.dvl-count-label{font-size:.82rem;color:var(--text-2);font-weight:600;line-height:1.4}
.dvl-count-label b{color:var(--text);font-weight:800}
.dvl-list{display:flex;flex-direction:column;gap:.6rem;margin-bottom:1rem;max-height:380px;overflow-y:auto;padding-right:.25rem}
.dvl-list::-webkit-scrollbar{width:6px}
.dvl-list::-webkit-scrollbar-track{background:transparent}
.dvl-list::-webkit-scrollbar-thumb{background:var(--border-strong);border-radius:3px}
.dvl-item{display:flex;align-items:center;gap:.75rem;padding:.85rem 1rem;background:var(--surface-2);border:1.5px solid var(--border);border-radius:12px;transition:.15s;position:relative}
.dvl-item:hover{border-color:var(--border-strong)}
.dvl-item.current{background:linear-gradient(135deg,rgba(6,182,212,.08),rgba(8,145,178,.04));border-color:rgba(6,182,212,.4)}
.dvl-item.current::after{content:'THIẾT BỊ NÀY';position:absolute;top:-8px;left:12px;font-size:.6rem;font-weight:900;padding:.15rem .5rem;border-radius:50px;background:linear-gradient(135deg,#06b6d4,#0891b2);color:#fff;letter-spacing:.5px;box-shadow:0 2px 6px rgba(6,182,212,.4)}
.dvl-item-icon{width:42px;height:42px;border-radius:10px;background:var(--surface);border:1px solid var(--border);display:flex;align-items:center;justify-content:center;font-size:1.15rem;color:var(--primary);flex-shrink:0}
.dvl-item.current .dvl-item-icon{background:linear-gradient(135deg,#06b6d4,#0891b2);color:#fff;border-color:transparent}
.dvl-item-info{flex:1;min-width:0}
.dvl-item-name{font-weight:700;font-size:.88rem;color:var(--text);margin-bottom:.15rem;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.dvl-item-meta{font-size:.72rem;color:var(--text-3);display:flex;align-items:center;gap:.5rem;flex-wrap:wrap}
.dvl-item-meta .dvl-tag{display:inline-flex;align-items:center;gap:.25rem;padding:.1rem .45rem;border-radius:50px;background:var(--surface);border:1px solid var(--border);font-weight:600}
.dvl-item-meta .dvl-tag.ok{background:rgba(22,163,74,.1);color:#16a34a;border-color:rgba(22,163,74,.3)}
.dvl-item-meta .dvl-tag.info{background:rgba(59,130,246,.1);color:#2563eb;border-color:rgba(59,130,246,.3)}
.dvl-remove-btn{width:36px;height:36px;border-radius:10px;border:1.5px solid var(--border);background:var(--surface);color:var(--text-2);cursor:pointer;display:inline-flex;align-items:center;justify-content:center;font-size:.85rem;flex-shrink:0;transition:.15s}
.dvl-remove-btn:hover{background:var(--danger-light);color:var(--danger);border-color:var(--danger);transform:scale(1.05)}
.dvl-remove-btn:disabled{opacity:.4;cursor:not-allowed;transform:none}
.dvl-warning{display:flex;align-items:flex-start;gap:.6rem;padding:.85rem 1rem;background:linear-gradient(135deg,rgba(245,158,11,.1),rgba(251,191,36,.05));border:1.5px solid rgba(245,158,11,.35);border-radius:12px;font-size:.78rem;color:#92400e;line-height:1.5;margin-bottom:1rem}
[data-theme="dark"] .dvl-warning{background:linear-gradient(135deg,rgba(245,158,11,.15),rgba(251,191,36,.08));color:#fcd34d}
.dvl-warning i{color:#f59e0b;margin-top:.15rem;flex-shrink:0;font-size:1rem}
.dvl-warning b{color:#dc2626}
[data-theme="dark"] .dvl-warning b{color:#fca5a5}
.dvl-warning.error{background:linear-gradient(135deg,rgba(220,38,38,.1),rgba(185,28,28,.05));border-color:rgba(220,38,38,.35);color:#991b1b}
[data-theme="dark"] .dvl-warning.error{color:#fca5a5}
.dvl-warning.error i{color:#dc2626}
.dvl-actions{display:flex;gap:.6rem;justify-content:flex-end;padding-top:1rem;border-top:1px solid var(--border);flex-wrap:wrap}
.dvl-btn{padding:.7rem 1.15rem;border-radius:10px;border:1.5px solid var(--border);background:var(--surface);color:var(--text);font-size:.85rem;font-weight:700;font-family:inherit;cursor:pointer;display:inline-flex;align-items:center;gap:.4rem;transition:.15s}
.dvl-btn:hover:not(:disabled){background:var(--surface-2);border-color:var(--primary);color:var(--primary)}
.dvl-btn:disabled{opacity:.5;cursor:not-allowed}
.dvl-btn.primary{background:linear-gradient(135deg,#06b6d4,#0891b2);color:#fff;border-color:transparent;box-shadow:0 4px 12px rgba(6,182,212,.3)}
.dvl-btn.primary:hover:not(:disabled){transform:translateY(-1px);box-shadow:0 6px 18px rgba(6,182,212,.5);color:#fff}
.dvl-btn.violet{background:linear-gradient(135deg,#4f46e5,#7c3aed);color:#fff;border-color:transparent;box-shadow:0 4px 12px rgba(124,58,237,.3)}
.dvl-btn.violet:hover:not(:disabled){transform:translateY(-1px);box-shadow:0 6px 18px rgba(124,58,237,.5);color:#fff}
.dvl-btn.danger{background:linear-gradient(135deg,#dc2626,#b91c1c);color:#fff;border-color:transparent;box-shadow:0 4px 12px rgba(220,38,38,.3)}
.dvl-btn.danger:hover:not(:disabled){transform:translateY(-1px);box-shadow:0 6px 18px rgba(220,38,38,.5);color:#fff}
.dvl-btn.green{background:linear-gradient(135deg,#16a34a,#22c55e);color:#fff;border-color:transparent;box-shadow:0 4px 12px rgba(22,163,74,.3)}
.dvl-btn.green:hover:not(:disabled){transform:translateY(-1px);box-shadow:0 6px 18px rgba(22,163,74,.5);color:#fff}
.dvl-btn.small{padding:.45rem .9rem;font-size:.78rem;border-radius:8px}
.dvl-timer{display:inline-flex;align-items:center;gap:.35rem;padding:.35rem .75rem;background:rgba(220,38,38,.1);border:1.5px solid rgba(220,38,38,.3);border-radius:50px;font-size:.85rem;font-weight:800;color:#dc2626;font-variant-numeric:tabular-nums;margin-top:.5rem}
[data-theme="dark"] .dvl-timer{color:#fca5a5;background:rgba(220,38,38,.2)}
.dvl-timer i{animation:dvlPulse 1s infinite}
@keyframes dvlPulse{0%,100%{opacity:1}50%{opacity:.4}}
.dvl-otp-wrap{margin:1.25rem 0}
.dvl-otp-label{display:block;font-size:.72rem;font-weight:700;color:var(--text-2);margin-bottom:.5rem;text-transform:uppercase;letter-spacing:.5px}
.dvl-otp-input{width:100%;padding:1rem;font-size:1.75rem;font-weight:900;text-align:center;letter-spacing:.75rem;border:2px solid var(--border);border-radius:12px;background:var(--surface);color:var(--text);font-family:monospace;outline:none;box-sizing:border-box;transition:.15s}
.dvl-otp-input:focus{border-color:#4f46e5;box-shadow:0 0 0 4px rgba(79,70,229,.15)}
.dvl-otp-input.error{border-color:#dc2626;box-shadow:0 0 0 4px rgba(220,38,38,.15)}
.dvl-otp-error{color:#dc2626;font-size:.78rem;margin-top:.5rem;text-align:center;display:none}
[data-theme="dark"] .dvl-otp-error{color:#fca5a5}
.dvl-steps{margin:1rem 0;padding:1rem;background:linear-gradient(135deg,rgba(79,70,229,.06),rgba(124,58,237,.03));border:1px solid rgba(124,58,237,.2);border-radius:12px;display:flex;flex-direction:column;gap:.6rem}
.dvl-step{display:flex;align-items:flex-start;gap:.6rem;font-size:.8rem;color:var(--text-2);line-height:1.5}
.dvl-step .num{width:22px;height:22px;border-radius:50%;background:linear-gradient(135deg,#4f46e5,#7c3aed);color:#fff;display:flex;align-items:center;justify-content:center;font-size:.68rem;font-weight:900;flex-shrink:0;line-height:1}
.dvl-step b{color:var(--text)}
.dvl-dropdown-btn{display:flex;align-items:center;gap:.5rem;width:100%;padding:.65rem .75rem;border:none;border-radius:var(--radius-sm);background:transparent;color:var(--text);font-size:.85rem;font-weight:600;cursor:pointer;transition:.15s;font-family:inherit;text-align:left}
.dvl-dropdown-btn:hover{background:var(--surface-2)}
.dvl-dropdown-btn i{color:#06b6d4;width:16px}
.dvl-dropdown-btn .dvl-badge{margin-left:auto;padding:.1rem .5rem;border-radius:50px;background:linear-gradient(135deg,#06b6d4,#0891b2);color:#fff;font-size:.65rem;font-weight:800;letter-spacing:.3px;box-shadow:0 2px 6px rgba(6,182,212,.4)}
.dvl-dropdown-btn .dvl-badge.warn{background:linear-gradient(135deg,#f59e0b,#d97706);box-shadow:0 2px 6px rgba(245,158,11,.4)}
.u-btn.dvl-btn-row{background:rgba(6,182,212,.1);color:#0891b2;border-color:rgba(6,182,212,.4)}
.u-btn.dvl-btn-row:hover{background:#06b6d4;color:#fff;border-color:#06b6d4;transform:scale(1.08)}
[data-theme="dark"] .u-btn.dvl-btn-row{background:rgba(6,182,212,.2);color:#67e8f9}
.dvl-spinner{display:inline-block;width:14px;height:14px;border:2px solid rgba(255,255,255,.35);border-top-color:#fff;border-radius:50%;animation:dvlSpin .7s linear infinite}
@keyframes dvlSpin{to{transform:rotate(360deg)}}
@media (max-width:500px){
.dvl-box{padding:1.4rem 1.15rem;border-radius:16px}
.dvl-icon{width:48px;height:48px;font-size:1.25rem}
.dvl-title{font-size:1.05rem}
.dvl-count-num{font-size:1.6rem}
.dvl-actions{flex-direction:column-reverse}
.dvl-btn{width:100%;justify-content:center}
.dvl-item{padding:.7rem .8rem}
.dvl-item-icon{width:36px;height:36px;font-size:1rem}
.dvl-otp-input{font-size:1.5rem;letter-spacing:.5rem}
}
"""


def build_device_html():
    return r"""
<!-- MODAL QUẢN LÝ THIẾT BỊ -->
<div class="dvl-modal" id="dvlModal">
    <div class="dvl-box">
        <button class="dvl-close" id="dvlCloseBtn" type="button" aria-label="Đóng"><i class="fas fa-times"></i></button>
        <div class="dvl-icon" id="dvlIcon"><i class="fas fa-mobile-screen-button"></i></div>
        <div class="dvl-title" id="dvlTitle">Quản lý thiết bị</div>
        <div class="dvl-subtitle" id="dvlSubtitle">Tài khoản của bạn chỉ được đăng nhập trên tối đa <b>2 thiết bị</b>.</div>
        <div class="dvl-count-box" id="dvlCountBox">
            <div class="dvl-count-num" id="dvlCountNum">0</div>
            <div class="dvl-count-label" id="dvlCountLabel">/ 2 thiết bị đang hoạt động</div>
        </div>
        <div class="dvl-list" id="dvlList"><div style="text-align:center;padding:2rem 1rem;color:var(--text-3)"><i class="fas fa-spinner fa-pulse"></i> Đang tải...</div></div>
        <div class="dvl-warning" id="dvlWarning" style="display:none">
            <i class="fas fa-exclamation-triangle"></i>
            <div>Bạn đã đạt giới hạn <b>2 thiết bị</b>. Vui lòng xóa bớt 1 thiết bị để đăng nhập máy mới.</div>
        </div>
        <div class="dvl-actions">
            <button type="button" class="dvl-btn" id="dvlLogoutOthersBtn"><i class="fas fa-sign-out-alt"></i> Đăng xuất thiết bị khác</button>
            <button type="button" class="dvl-btn primary" id="dvlDoneBtn"><i class="fas fa-check"></i> Xong</button>
        </div>
    </div>
</div>

<!-- MODAL XÁC NHẬN OTP -->
<div class="dvl-modal" id="dvlVerifyModal">
    <div class="dvl-box">
        <div class="dvl-icon mail"><i class="fas fa-envelope-circle-check"></i></div>
        <div class="dvl-title">Xác nhận đăng nhập thiết bị mới</div>
        <div class="dvl-subtitle">
            Tài khoản của bạn đã đăng nhập trên <b>2 thiết bị</b> khác.
            Chúng tôi đã gửi <b>mã OTP 6 số</b> đến email của bạn.
        </div>
        <div style="text-align:center;margin-bottom:1rem">
            <span class="dvl-email-highlight" id="dvlVerifyEmail">user@example.com</span>
        </div>
        <div class="dvl-otp-wrap">
            <label class="dvl-otp-label">Nhập mã OTP 6 số</label>
            <input type="text" id="dvlOtpInput" class="dvl-otp-input" maxlength="6" inputmode="numeric" pattern="[0-9]*" placeholder="••••••" autocomplete="one-time-code">
            <div class="dvl-otp-error" id="dvlOtpError"></div>
        </div>
        <div style="text-align:center;margin-top:.5rem">
            <div class="dvl-timer" id="dvlTimer">
                <i class="fas fa-hourglass-half"></i> Còn lại: <span id="dvlTimerCount">10:00</span>
            </div>
        </div>
        <div class="dvl-warning" style="margin-top:1rem">
            <i class="fas fa-shield-alt"></i>
            <div>Không nhận được mail? Kiểm tra <b>Spam</b>, hoặc liên hệ admin qua <b>Zalo/Facebook</b> để được duyệt tay.</div>
        </div>
        <div class="dvl-actions">
            <button type="button" class="dvl-btn" id="dvlVerifyCancelBtn"><i class="fas fa-times"></i> Hủy</button>
            <button type="button" class="dvl-btn violet" id="dvlVerifyResendBtn"><i class="fas fa-paper-plane"></i> Gửi lại OTP</button>
            <button type="button" class="dvl-btn primary" id="dvlVerifyCheckBtn"><i class="fas fa-check"></i> Xác nhận</button>
        </div>
    </div>
</div>

<!-- MODAL XÁC NHẬN THÀNH CÔNG -->
<div class="dvl-modal" id="dvlVerifySuccessModal">
    <div class="dvl-box">
        <div class="dvl-icon" style="background:linear-gradient(135deg,#16a34a,#22c55e)"><i class="fas fa-check"></i></div>
        <div class="dvl-title">Xác nhận thành công</div>
        <div class="dvl-subtitle">Thiết bị mới đã được đăng nhập. Thiết bị cũ nhất đã bị đăng xuất khỏi tài khoản.</div>
        <div class="dvl-actions">
            <button type="button" class="dvl-btn green" id="dvlSuccessContinueBtn"><i class="fas fa-arrow-right"></i> Tiếp tục</button>
        </div>
    </div>
</div>
"""


def build_device_js():
    # Thay __SERVER_URL__ bằng giá trị thực
    js = r"""
(function() {
    'use strict';

    var MAX_DEVICES = 2;
    var VERIFY_TIMEOUT = 10 * 60 * 1000;
    var SERVER_URL = '__SERVER_URL__';
    var DEVICE_ID_KEY = 'dvl_device_id';
    var DEVICE_NAME_KEY = 'dvl_device_name';

    var currentDeviceId = null;
    var _timerInterval = null;
    var _verifyExpireAt = null;
    var _verifyPoller = null;

    function $(id) { return document.getElementById(id); }
    function esc(s) {
        if (s == null) return '';
        return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;')
            .replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');
    }

    /* ═══ SUPER ADMIN ═══ */
    function __dvlIsSuperAdmin(email) {
        if (!email) return false;
        var sa = '';
        try {
            if (typeof SUPER_ADMIN !== 'undefined' && SUPER_ADMIN) {
                sa = String(SUPER_ADMIN).toLowerCase().trim();
            }
        } catch(e) {}
        if (!sa) return false;
        return String(email).toLowerCase().trim() === sa;
    }

    function __dvlHasAdminRights() {
        if (typeof currentUser === 'undefined' || !currentUser) return false;
        if (currentUser.role === 'admin') return true;
        if (__dvlIsSuperAdmin(currentUser.email)) return true;
        return false;
    }

    function timeAgo(ms) {
        if (!ms) return 'Vừa xong';
        var s = Math.floor((Date.now() - ms) / 1000);
        if (s < 60) return 'Vừa xong';
        if (s < 3600) return Math.floor(s / 60) + ' phút trước';
        if (s < 86400) return Math.floor(s / 3600) + ' giờ trước';
        return Math.floor(s / 86400) + ' ngày trước';
    }

    function detectDeviceName() {
        try {
            var ua = navigator.userAgent || '';
            var name = 'Thiết bị';
            if (/iPhone/i.test(ua)) name = 'iPhone';
            else if (/iPad/i.test(ua)) name = 'iPad';
            else if (/Android/i.test(ua)) {
                var m = ua.match(/Android\s+([\d.]+)/);
                name = 'Android' + (m ? ' ' + m[1] : '');
            } else if (/Windows NT 10/.test(ua)) name = 'Windows 10/11';
            else if (/Windows NT 6\.3/.test(ua)) name = 'Windows 8.1';
            else if (/Windows NT 6\.2/.test(ua)) name = 'Windows 8';
            else if (/Windows NT 6\.1/.test(ua)) name = 'Windows 7';
            else if (/Windows/i.test(ua)) name = 'Windows';
            else if (/Macintosh/i.test(ua)) name = 'MacBook';
            else if (/Mac OS X/i.test(ua)) name = 'Mac';
            else if (/Linux/i.test(ua)) name = 'Linux';
            var browser = '';
            if (/Edg\//.test(ua)) browser = 'Edge';
            else if (/Chrome\//.test(ua) && !/Edg/.test(ua)) browser = 'Chrome';
            else if (/Firefox\//.test(ua)) browser = 'Firefox';
            else if (/Safari\//.test(ua) && !/Chrome/.test(ua)) browser = 'Safari';
            else if (/OPR\//.test(ua) || /Opera/.test(ua)) browser = 'Opera';
            return name + (browser ? ' · ' + browser : '');
        } catch(e) { return 'Thiết bị'; }
    }

    function detectDeviceType() {
        try {
            var ua = navigator.userAgent || '';
            if (/Mobile|iPhone|Android.*Mobile/i.test(ua)) return 'mobile';
            if (/iPad|Tablet|Android/i.test(ua)) return 'tablet';
            return 'desktop';
        } catch(e) { return 'desktop'; }
    }

    function generateDeviceId() {
        try {
            var saved = localStorage.getItem(DEVICE_ID_KEY);
            if (saved && saved.length > 8) return saved;
        } catch(e) {}
        var id = 'dev_' + Date.now().toString(36) + '_' +
                 Math.random().toString(36).substring(2, 10) +
                 Math.random().toString(36).substring(2, 10);
        try { localStorage.setItem(DEVICE_ID_KEY, id); } catch(e) {}
        return id;
    }

    function getDeviceId() {
        if (currentDeviceId) return currentDeviceId;
        currentDeviceId = generateDeviceId();
        return currentDeviceId;
    }

    function getDeviceName() {
        try {
            var saved = localStorage.getItem(DEVICE_NAME_KEY);
            if (saved) return saved;
        } catch(e) {}
        var name = detectDeviceName();
        try { localStorage.setItem(DEVICE_NAME_KEY, name); } catch(e) {}
        return name;
    }

    function getDeviceIcon(type) {
        if (type === 'mobile') return 'fa-mobile-screen-button';
        if (type === 'tablet') return 'fa-tablet-screen-button';
        return 'fa-desktop';
    }

    async function loadDevices(email) {
        if (!db || !email) return [];
        try {
            var doc = await db.collection('allowed_users').doc(email.toLowerCase()).get();
            if (!doc.exists) return [];
            var data = doc.data() || {};
            return Array.isArray(data.devices) ? data.devices : [];
        } catch(e) { return []; }
    }

    async function saveDevices(email, devices) {
        if (!db || !email) return false;
        try {
            await db.collection('allowed_users').doc(email.toLowerCase()).set({
                devices: devices,
                devicesUpdatedAt: firebase.firestore.FieldValue.serverTimestamp()
            }, { merge: true });
            return true;
        } catch(e) { return false; }
    }

    /* ═══ GỬI OTP QUA SERVER ═══ */
    async function sendVerifyEmail(email) {
        if (!email) return { ok: false, reason: 'no_email' };

        try {
            var res = await fetch(SERVER_URL + '/api/device/send-otp', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    email: email,
                    deviceId: getDeviceId(),
                    deviceName: getDeviceName()
                })
            });
            var data = await res.json();
            if (data.ok) {
                console.log('[DVL] ✅ Đã gửi OTP đến:', email);
                return { ok: true };
            }
            return { ok: false, reason: data.error || 'server_error', waitSec: data.waitSec };
        } catch(e) {
            console.error('[DVL] ❌ Send OTP error:', e);
            return { ok: false, reason: 'network_error' };
        }
    }

    async function verifyOtpWithServer(email, otp) {
        try {
            var res = await fetch(SERVER_URL + '/api/device/verify-otp', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email: email, otp: otp })
            });
            return await res.json();
        } catch(e) {
            console.error('[DVL] ❌ Verify OTP error:', e);
            return { ok: false, error: 'Lỗi kết nối server' };
        }
    }

    /* ═══ REGISTER DEVICE ═══ */
    async function registerCurrentDevice(email) {
        if (!email || !db) return { allowed: true };

        if (__dvlIsSuperAdmin(email)) {
            console.log('[DVL] Super admin — bypass');
            return { allowed: true, isSuperAdmin: true };
        }

        var deviceId = getDeviceId();
        var now = Date.now();
        var devices = await loadDevices(email);

        var found = -1;
        for (var i = 0; i < devices.length; i++) {
            if (devices[i].id === deviceId) { found = i; break; }
        }

        if (found >= 0) {
            devices[found].lastSeen = now;
            devices[found].name = getDeviceName();
            devices[found].type = detectDeviceType();
            await saveDevices(email, devices);
            return { allowed: true };
        }

        try {
            var pendingSnap = await db.collection('allowed_users').doc(email.toLowerCase())
                .collection('pending_devices').where('deviceId', '==', deviceId).limit(1).get();

            if (!pendingSnap.empty) {
                var pdoc = pendingSnap.docs[0];
                var pd = pdoc.data();

                if (pd.status === 'confirmed') {
                    await completeVerification(email);
                    return { allowed: true, verified: true };
                }

                if (pd.expireAt) {
                    var expMs = pd.expireAt.toMillis ? pd.expireAt.toMillis() : pd.expireAt.seconds * 1000;
                    if (Date.now() > expMs) {
                        try { await pdoc.ref.delete(); } catch(e) {}
                    } else {
                        return {
                            allowed: false,
                            needsVerify: true,
                            expireAt: expMs,
                            existing: true
                        };
                    }
                }
            }
        } catch(e) {}

        if (devices.length < MAX_DEVICES) {
            devices.push({
                id: deviceId, name: getDeviceName(), type: detectDeviceType(),
                userAgent: (navigator.userAgent || '').substring(0, 200),
                firstSeen: now, lastSeen: now
            });
            await saveDevices(email, devices);
            return { allowed: true, isNew: true };
        }

        /* Đã đủ → tạo pending + gửi OTP */
        try {
            await db.collection('allowed_users').doc(email.toLowerCase())
                .collection('pending_devices').doc(deviceId).set({
                    deviceId: deviceId,
                    deviceName: getDeviceName(),
                    deviceType: detectDeviceType(),
                    userAgent: (navigator.userAgent || '').substring(0, 200),
                    createdAt: firebase.firestore.FieldValue.serverTimestamp(),
                    expireAt: firebase.firestore.Timestamp.fromMillis(now + VERIFY_TIMEOUT),
                    status: 'pending',
                    emailSent: false
                });
        } catch(e) {}

        var emailResult = await sendVerifyEmail(email);

        try {
            await db.collection('allowed_users').doc(email.toLowerCase())
                .collection('pending_devices').doc(deviceId)
                .update({
                    emailSent: emailResult.ok === true,
                    emailError: emailResult.ok ? null : (emailResult.reason || 'unknown')
                });
        } catch(_e) {}

        return {
            allowed: false,
            needsVerify: true,
            expireAt: now + VERIFY_TIMEOUT,
            devices: devices,
            emailSent: emailResult.ok === true,
            emailError: emailResult.ok ? null : emailResult.reason
        };
    }

    async function completeVerification(email) {
        if (!email || !db) return false;
        if (__dvlIsSuperAdmin(email)) return false;

        var deviceId = getDeviceId();
        var deviceName = getDeviceName();
        var deviceType = detectDeviceType();
        var now = Date.now();

        var devices = await loadDevices(email);
        devices.sort(function(a, b) { return (a.lastSeen || 0) - (b.lastSeen || 0); });
        var kickedDevice = devices.shift();

        if (kickedDevice) {
            try {
                await db.collection('allowed_users').doc(email.toLowerCase())
                    .collection('kicked_devices').doc(kickedDevice.id).set({
                        deviceId: kickedDevice.id,
                        deviceName: kickedDevice.name || 'Thiết bị',
                        kickedAt: firebase.firestore.FieldValue.serverTimestamp(),
                        kickedBy: deviceName,
                        reason: 'device_verified_new_login'
                    });
            } catch(e) {}
        }

        devices.push({
            id: deviceId, name: deviceName, type: deviceType,
            userAgent: (navigator.userAgent || '').substring(0, 200),
            firstSeen: now, lastSeen: now
        });

        await saveDevices(email, devices);

        try {
            var snap = await db.collection('allowed_users').doc(email.toLowerCase())
                .collection('pending_devices').where('deviceId', '==', deviceId).get();
            var batch = db.batch();
            snap.forEach(function(d) { batch.delete(d.ref); });
            await batch.commit();
        } catch(e) {}

        return true;
    }

    async function checkIfKicked(email) {
        if (!email || !db) return false;
        if (__dvlIsSuperAdmin(email)) return false;

        var deviceId = getDeviceId();
        try {
            var doc = await db.collection('allowed_users').doc(email.toLowerCase())
                .collection('kicked_devices').doc(deviceId).get();

            if (doc.exists) {
                await doc.ref.delete();
                if (typeof showUserChangedToast === 'function') {
                    showUserChangedToast('⚠️ Thiết bị đã bị đăng xuất do có máy mới xác nhận', 'error');
                } else {
                    alert('⚠️ Thiết bị đã bị đăng xuất');
                }
                if (typeof auth !== 'undefined' && auth) auth.signOut();
                return true;
            }
        } catch(e) {}
        return false;
    }

    /* ═══ UI MODALS ═══ */
    function renderDeviceList(containerEl, devices, email, isLimitView) {
        if (!containerEl) return;
        if (!devices || devices.length === 0) {
            containerEl.innerHTML = '<div style="text-align:center;padding:2rem 1rem;color:var(--text-3)"><i class="fas fa-inbox" style="font-size:2rem;opacity:.4;margin-bottom:.5rem;display:block"></i>Chưa có thiết bị nào</div>';
            return;
        }

        var currentId = getDeviceId();
        var sorted = devices.slice().sort(function(a, b) {
            if (a.id === currentId) return -1;
            if (b.id === currentId) return 1;
            return (b.lastSeen || 0) - (a.lastSeen || 0);
        });

        var html = '';
        sorted.forEach(function(d) {
            var isCurrent = (d.id === currentId);
            var icon = getDeviceIcon(d.type || 'desktop');
            var lastSeen = d.lastSeen ? timeAgo(d.lastSeen) : 'Không rõ';
            var firstSeen = d.firstSeen ? new Date(d.firstSeen).toLocaleDateString('vi-VN') : '';

            var removeBtn = '';
            if (!isLimitView) {
                if (isCurrent) {
                    removeBtn = '<button class="dvl-remove-btn" disabled><i class="fas fa-lock"></i></button>';
                } else {
                    removeBtn = '<button class="dvl-remove-btn" data-device-id="' + esc(d.id) + '"><i class="fas fa-trash"></i></button>';
                }
            }

            html += '<div class="dvl-item' + (isCurrent ? ' current' : '') + '" data-device-id="' + esc(d.id) + '">' +
                '<div class="dvl-item-icon"><i class="fas ' + icon + '"></i></div>' +
                '<div class="dvl-item-info">' +
                    '<div class="dvl-item-name">' + esc(d.name || 'Thiết bị') + '</div>' +
                    '<div class="dvl-item-meta">' +
                        '<span class="dvl-tag ' + (isCurrent ? 'ok' : 'info') + '"><i class="fas fa-clock"></i> ' + lastSeen + '</span>' +
                        (firstSeen ? '<span>Thêm: ' + firstSeen + '</span>' : '') +
                    '</div>' +
                '</div>' + removeBtn +
            '</div>';
        });

        containerEl.innerHTML = html;

        if (!isLimitView) {
            containerEl.querySelectorAll('.dvl-remove-btn[data-device-id]').forEach(function(btn) {
                btn.addEventListener('click', function() {
                    removeDevice(email, this.dataset.deviceId);
                });
            });
        }
    }

    async function removeDevice(email, deviceId) {
        if (!confirm('Xóa thiết bị này?\n\nThiết bị đó sẽ bị đăng xuất.')) return;
        try {
            var devices = await loadDevices(email);
            var filtered = devices.filter(function(d) { return d.id !== deviceId; });
            await saveDevices(email, filtered);
            updateModalUI(email, filtered);
            renderDeviceList($('dvlList'), filtered, email, false);
            if (typeof showUserChangedToast === 'function') showUserChangedToast('📱 Đã xóa thiết bị', 'success');
        } catch(e) { alert('Lỗi: ' + e.message); }
    }

    function updateModalUI(email, devices) {
        var count = devices.length;
        if ($('dvlCountNum')) $('dvlCountNum').textContent = count;
        if ($('dvlCountLabel')) $('dvlCountLabel').innerHTML = '/ ' + MAX_DEVICES + ' thiết bị đang hoạt động';
        if ($('dvlCountBox')) {
            $('dvlCountBox').classList.remove('warn');
            if (count >= MAX_DEVICES) $('dvlCountBox').classList.add('warn');
        }
        if ($('dvlWarning')) $('dvlWarning').style.display = (count >= MAX_DEVICES) ? 'flex' : 'none';
        if ($('dvlIcon')) {
            $('dvlIcon').classList.remove('warn', 'danger');
            if (count >= MAX_DEVICES) $('dvlIcon').classList.add('warn');
        }
    }

    async function openManageModal() {
        if (typeof currentUser === 'undefined' || !currentUser || !currentUser.email) return;
        if (__dvlIsSuperAdmin(currentUser.email)) return;

        var modal = $('dvlModal');
        if (!modal) return;
        $('dvlTitle').textContent = 'Quản lý thiết bị';
        $('dvlSubtitle').innerHTML = 'Tài khoản của bạn chỉ được đăng nhập trên tối đa <b>2 thiết bị</b>.';
        $('dvlCountBox').style.display = 'flex';
        $('dvlLogoutOthersBtn').style.display = 'inline-flex';
        modal.classList.add('show');

        $('dvlList').innerHTML = '<div style="text-align:center;padding:2rem 1rem;color:var(--text-3)"><i class="fas fa-spinner fa-pulse"></i> Đang tải...</div>';
        var devices = await loadDevices(currentUser.email);
        updateModalUI(currentUser.email, devices);
        renderDeviceList($('dvlList'), devices, currentUser.email, false);
    }

    function closeManageModal() {
        var m = $('dvlModal');
        if (m) m.classList.remove('show');
    }

    function showVerifyModal(email, expireAt, emailSent, emailError) {
        var modal = $('dvlVerifyModal');
        if (!modal) return;

        if ($('dvlVerifyEmail')) $('dvlVerifyEmail').textContent = email;
        if ($('dvlOtpInput')) $('dvlOtpInput').value = '';
        if ($('dvlOtpError')) $('dvlOtpError').style.display = 'none';
        if ($('dvlOtpInput')) $('dvlOtpInput').classList.remove('error');

        /* Nếu mail lỗi → báo */
        if (emailSent === false && emailError && emailError !== 'not_sent') {
            var errMsg = emailError;
            if (emailError === 'network_error') errMsg = 'Không kết nối được server gửi OTP.';
            alert('⚠️ Không gửi được OTP: ' + errMsg + '\n\nVui lòng liên hệ admin để được duyệt tay.');
        }

        modal.classList.add('show');
        _verifyExpireAt = expireAt || (Date.now() + VERIFY_TIMEOUT);
        startTimer();

        /* Auto-submit khi đủ 6 số */
        var otpInput = $('dvlOtpInput');
        if (otpInput && !otpInput.__dvlBound) {
            otpInput.__dvlBound = true;
            otpInput.addEventListener('input', function() {
                this.value = this.value.replace(/\D/g, '').slice(0, 6);
                if ($('dvlOtpError')) $('dvlOtpError').style.display = 'none';
                this.classList.remove('error');
                if (this.value.length === 6) {
                    setTimeout(function() {
                        var btn = $('dvlVerifyCheckBtn');
                        if (btn && !btn.disabled) btn.click();
                    }, 300);
                }
            });
        }

        /* Nút Hủy */
        var cancelBtn = $('dvlVerifyCancelBtn');
        if (cancelBtn) {
            cancelBtn.onclick = function() {
                stopTimer();
                modal.classList.remove('show');
                if (typeof auth !== 'undefined' && auth) auth.signOut();
            };
        }

        /* Nút Gửi lại OTP */
        var resendBtn = $('dvlVerifyResendBtn');
        if (resendBtn) {
            resendBtn.onclick = async function() {
                var orig = resendBtn.innerHTML;
                resendBtn.disabled = true;
                resendBtn.innerHTML = '<span class="dvl-spinner"></span> Đang gửi...';

                var result = await sendVerifyEmail(email);
                if (result.ok) {
                    resendBtn.innerHTML = '<i class="fas fa-check"></i> Đã gửi';
                    if ($('dvlOtpInput')) $('dvlOtpInput').value = '';
                    setTimeout(function() {
                        resendBtn.disabled = false;
                        resendBtn.innerHTML = orig;
                    }, 3000);
                } else {
                    alert('❌ Không gửi được OTP.\n\nLý do: ' + (result.reason || 'Không rõ'));
                    resendBtn.disabled = false;
                    resendBtn.innerHTML = orig;
                }
            };
        }

        /* Nút Xác nhận */
        var checkBtn = $('dvlVerifyCheckBtn');
        if (checkBtn) {
            checkBtn.onclick = async function() {
                var otp = ($('dvlOtpInput') ? $('dvlOtpInput').value : '').trim();
                var otpError = $('dvlOtpError');
                var otpInput = $('dvlOtpInput');

                if (!/^\d{6}$/.test(otp)) {
                    if (otpError) { otpError.style.display = 'block'; otpError.textContent = 'Vui lòng nhập đủ 6 số'; }
                    if (otpInput) otpInput.classList.add('error');
                    return;
                }
                if (otpError) otpError.style.display = 'none';
                if (otpInput) otpInput.classList.remove('error');

                var orig = checkBtn.innerHTML;
                checkBtn.disabled = true;
                checkBtn.innerHTML = '<span class="dvl-spinner"></span> Đang xác thực...';

                var result = await verifyOtpWithServer(email, otp);

                if (result.ok) {
                    checkBtn.innerHTML = '<i class="fas fa-check"></i> Thành công!';

                    /* Confirm pending trong Firestore */
                    try {
                        await db.collection('allowed_users').doc(email.toLowerCase())
                            .collection('pending_devices').doc(getDeviceId())
                            .update({
                                status: 'confirmed',
                                confirmedAt: firebase.firestore.FieldValue.serverTimestamp(),
                                confirmedVia: 'otp_email'
                            });
                    } catch(_e) {}

                    stopTimer();
                    await completeVerification(email);
                    modal.classList.remove('show');
                    showSuccessModal();
                } else {
                    if (otpError) {
                        otpError.style.display = 'block';
                        otpError.textContent = result.error || 'Mã OTP không đúng';
                    }
                    if (otpInput) otpInput.classList.add('error');
                    checkBtn.disabled = false;
                    checkBtn.innerHTML = orig;
                }
            };
        }
    }

    function showSuccessModal() {
        var m = $('dvlVerifySuccessModal');
        if (!m) return;
        m.classList.add('show');
        var btn = $('dvlSuccessContinueBtn');
        if (btn) {
            btn.onclick = function() {
                m.classList.remove('show');
                location.reload();
            };
        }
    }

    function startTimer() {
        stopTimer();
        updateTimerDisplay();
        _timerInterval = setInterval(function() {
            var remain = _verifyExpireAt - Date.now();
            if (remain <= 0) {
                stopTimer();
                var modal = $('dvlVerifyModal');
                if (modal) modal.classList.remove('show');
                if (typeof auth !== 'undefined' && auth) auth.signOut();
                return;
            }
            updateTimerDisplay();
        }, 1000);
    }

    function updateTimerDisplay() {
        var remain = Math.max(0, _verifyExpireAt - Date.now());
        var m = Math.floor(remain / 60000);
        var s = Math.floor((remain % 60000) / 1000);
        if ($('dvlTimerCount')) $('dvlTimerCount').textContent = String(m).padStart(2, '0') + ':' + String(s).padStart(2, '0');
    }

    function stopTimer() {
        if (_timerInterval) { clearInterval(_timerInterval); _timerInterval = null; }
    }

    async function logoutOtherDevices() {
        if (typeof currentUser === 'undefined' || !currentUser || !currentUser.email) return;
        if (__dvlIsSuperAdmin(currentUser.email)) return;

        var currentId = getDeviceId();
        var devices = await loadDevices(currentUser.email);
        var keep = devices.filter(function(d) { return d.id === currentId; });

        if (keep.length === devices.length) { alert('Bạn chỉ có 1 thiết bị đang đăng nhập.'); return; }
        if (!confirm('Đăng xuất tất cả thiết bị khác?\n\nChỉ giữ lại thiết bị hiện tại.')) return;

        await saveDevices(currentUser.email, keep);
        updateModalUI(currentUser.email, keep);
        renderDeviceList($('dvlList'), keep, currentUser.email, false);
        if (typeof showUserChangedToast === 'function') showUserChangedToast('📱 Đã đăng xuất thiết bị khác', 'success');
    }

    /* ═══ DROPDOWN BUTTONS ═══ */
    function injectDropdownButton() {
        var dropdown = document.getElementById('userDropdown');
        if (!dropdown) return false;

        var curEmail = '';
        try {
            if (typeof currentUser !== 'undefined' && currentUser && currentUser.email) curEmail = currentUser.email;
            else if (typeof auth !== 'undefined' && auth && auth.currentUser) curEmail = auth.currentUser.email || '';
        } catch(e) {}

        if (__dvlIsSuperAdmin(curEmail)) {
            var oldBtn = dropdown.querySelector('#dvlManageBtn');
            if (oldBtn) oldBtn.remove();
            return true;
        }

        if (!dropdown.querySelector('#dvlManageBtn')) {
            var logoutBtn = dropdown.querySelector('#logoutBtn');
            if (logoutBtn) {
                var btn = document.createElement('button');
                btn.type = 'button';
                btn.id = 'dvlManageBtn';
                btn.className = 'dvl-dropdown-btn';
                btn.innerHTML = '<i class="fas fa-mobile-screen-button"></i> Quản lý thiết bị<span class="dvl-badge" id="dvlDropdownBadge">0/' + MAX_DEVICES + '</span>';
                btn.addEventListener('click', function(e) {
                    e.stopPropagation();
                    var dd = document.getElementById('userDropdown');
                    if (dd) dd.classList.remove('show');
                    openManageModal();
                });
                logoutBtn.parentNode.insertBefore(btn, logoutBtn);
            }
        }
        return true;
    }

    async function updateDropdownBadge() {
        if (typeof currentUser === 'undefined' || !currentUser || !currentUser.email) return;
        if (__dvlIsSuperAdmin(currentUser.email)) {
            var b = $('dvlDropdownBadge');
            if (b) b.style.display = 'none';
            return;
        }
        var badge = $('dvlDropdownBadge');
        if (!badge) return;
        badge.style.display = '';
        var devices = await loadDevices(currentUser.email);
        badge.textContent = devices.length + '/' + MAX_DEVICES;
        badge.classList.remove('warn');
        if (devices.length >= MAX_DEVICES) badge.classList.add('warn');
    }

    /* ═══ ADMIN PENDING ═══ */
    async function updatePendingBadge() {
        if (!db || !__dvlHasAdminRights()) return;
        try {
            var snap = await db.collectionGroup('pending_devices').where('status', '==', 'pending').get();
            var badge = $('dvlPendingBadge');
            if (badge) {
                badge.textContent = snap.size;
                badge.style.display = snap.size > 0 ? 'inline-block' : 'none';
            }
        } catch(e) {}
    }

    function injectAdminPendingButton() {
        if (!__dvlHasAdminRights()) return;
        var dropdown = document.getElementById('userDropdown');
        if (!dropdown) return;
        if (dropdown.querySelector('#dvlPendingBtn')) return;
        var logoutBtn = dropdown.querySelector('#logoutBtn');
        if (!logoutBtn) return;

        var btn = document.createElement('button');
        btn.type = 'button';
        btn.id = 'dvlPendingBtn';
        btn.className = 'dvl-dropdown-btn';
        btn.innerHTML = '<i class="fas fa-clock" style="color:#f59e0b"></i> Yêu cầu chờ duyệt<span class="dvl-badge warn" id="dvlPendingBadge" style="display:none">0</span>';
        btn.addEventListener('click', function(e) {
            e.stopPropagation();
            var dd = document.getElementById('userDropdown');
            if (dd) dd.classList.remove('show');
            openPendingList();
        });
        logoutBtn.parentNode.insertBefore(btn, logoutBtn);
        updatePendingBadge();
    }

    async function openPendingList() {
        if (!__dvlHasAdminRights()) { alert('Chỉ admin mới có quyền này.'); return; }
        var modal = $('dvlModal');
        if (!modal) return;
        $('dvlTitle').textContent = 'Yêu cầu chờ duyệt';
        $('dvlSubtitle').innerHTML = 'Danh sách thiết bị đang chờ admin xác nhận.';
        $('dvlCountBox').style.display = 'none';
        $('dvlWarning').style.display = 'none';
        $('dvlLogoutOthersBtn').style.display = 'none';
        modal.classList.add('show');

        var list = $('dvlList');
        list.innerHTML = '<div style="text-align:center;padding:2rem;color:var(--text-3)"><i class="fas fa-spinner fa-pulse"></i> Đang tải...</div>';

        try {
            var snap = await db.collectionGroup('pending_devices').where('status', '==', 'pending').get();
            if (snap.empty) {
                list.innerHTML = '<div style="text-align:center;padding:2rem;color:var(--text-3)"><i class="fas fa-inbox" style="font-size:2rem;opacity:.4;display:block;margin-bottom:.5rem"></i>Không có yêu cầu nào</div>';
                return;
            }

            var items = [];
            snap.forEach(function(doc) {
                items.push({ doc: doc, data: doc.data(), email: doc.ref.parent.parent.id });
            });
            items.sort(function(a, b) {
                var ta = a.data.createdAt ? a.data.createdAt.toMillis() : 0;
                var tb = b.data.createdAt ? b.data.createdAt.toMillis() : 0;
                return tb - ta;
            });

            var html = '';
            items.forEach(function(item) {
                var d = item.data;
                var created = d.createdAt && d.createdAt.toMillis ? new Date(d.createdAt.toMillis()).toLocaleString('vi-VN') : 'Không rõ';
                var expMs = d.expireAt ? (d.expireAt.toMillis ? d.expireAt.toMillis() : d.expireAt.seconds * 1000) : 0;
                var remain = expMs ? Math.max(0, Math.floor((expMs - Date.now()) / 1000)) : 0;
                var remainStr = remain > 0 ? Math.floor(remain / 60) + 'p ' + (remain % 60) + 's' : 'Hết hạn';

                var emailStatus = d.emailSent
                    ? '<span class="dvl-tag ok"><i class="fas fa-envelope"></i> Đã gửi OTP</span>'
                    : '<span class="dvl-tag" style="background:rgba(220,38,38,.1);color:#dc2626;border-color:rgba(220,38,38,.3)"><i class="fas fa-envelope"></i> OTP lỗi</span>';

                html += '<div class="dvl-item" data-email="' + esc(item.email) + '" data-device-id="' + esc(d.deviceId) + '">' +
                    '<div class="dvl-item-icon"><i class="fas ' + getDeviceIcon(d.deviceType || 'desktop') + '"></i></div>' +
                    '<div class="dvl-item-info">' +
                        '<div class="dvl-item-name">' + esc(item.email) + '</div>' +
                        '<div class="dvl-item-meta">' +
                            '<span class="dvl-tag info"><i class="fas fa-mobile"></i> ' + esc(d.deviceName || 'Thiết bị') + '</span>' +
                            emailStatus +
                            '<span><i class="fas fa-clock"></i> ' + created + '</span>' +
                            '<span style="color:' + (remain > 0 ? '#16a34a' : '#dc2626') + '">⏱ ' + remainStr + '</span>' +
                        '</div>' +
                    '</div>' +
                    '<button class="dvl-btn green small dvl-approve-btn"><i class="fas fa-check"></i> Duyệt</button>' +
                '</div>';
            });

            list.innerHTML = html;

            list.querySelectorAll('.dvl-approve-btn').forEach(function(btn) {
                btn.onclick = async function(e) {
                    e.stopPropagation();
                    var item = this.closest('.dvl-item');
                    var email = item.dataset.email;
                    var deviceId = item.dataset.deviceId;
                    if (!confirm('Xác nhận cho thiết bị này đăng nhập?\n\nUser: ' + email)) return;

                    var orig = this.innerHTML;
                    this.disabled = true;
                    this.innerHTML = '<span class="dvl-spinner"></span>';

                    try {
                        await db.collection('allowed_users').doc(email)
                            .collection('pending_devices').doc(deviceId)
                            .update({
                                status: 'confirmed',
                                confirmedAt: firebase.firestore.FieldValue.serverTimestamp(),
                                confirmedBy: currentUser.email,
                                confirmedVia: 'admin_panel'
                            });

                        item.style.opacity = '0.5';
                        item.style.pointerEvents = 'none';
                        this.innerHTML = '<i class="fas fa-check"></i> Đã duyệt';
                        this.style.background = 'linear-gradient(135deg,#16a34a,#22c55e)';
                        updatePendingBadge();
                        if (typeof showUserChangedToast === 'function') showUserChangedToast('✅ Đã duyệt cho ' + email, 'success');
                    } catch(err) {
                        alert('Lỗi: ' + err.message);
                        this.disabled = false;
                        this.innerHTML = orig;
                    }
                };
            });
        } catch(e) {
            list.innerHTML = '<div style="text-align:center;padding:2rem;color:#dc2626">Lỗi: ' + esc(e.message) + '</div>';
        }
    }

    /* ═══ ADMIN VIEW DEVICE ═══ */
    function injectAdminDeviceButton() {
        var userList = document.getElementById('userList');
        if (!userList) return;
        userList.querySelectorAll('.user-row[data-email]').forEach(function(row) {
            if (row.querySelector('.dvl-btn-row')) return;
            var actions = row.querySelector('.u-actions');
            if (!actions) return;
            var email = row.dataset.email;
            if (!email) return;

            var btn = document.createElement('button');
            btn.type = 'button';
            btn.className = 'u-btn dvl-btn-row';
            btn.title = 'Xem thiết bị';
            btn.innerHTML = '<i class="fas fa-mobile-screen-button"></i>';
            btn.addEventListener('click', function(e) {
                e.preventDefault(); e.stopPropagation();
                openAdminDeviceView(email);
            });
            var deleteBtn = actions.querySelector('.u-btn.danger');
            if (deleteBtn) actions.insertBefore(btn, deleteBtn);
            else actions.appendChild(btn);
        });
    }

    async function openAdminDeviceView(email) {
        if (!__dvlHasAdminRights()) { alert('Chỉ admin mới có quyền này.'); return; }
        var modal = $('dvlModal');
        if (!modal) return;
        $('dvlTitle').textContent = 'Thiết bị của user';
        $('dvlSubtitle').innerHTML = 'Danh sách thiết bị của: <b>' + esc(email) + '</b>.';
        $('dvlCountBox').style.display = 'flex';
        $('dvlWarning').style.display = 'none';
        $('dvlLogoutOthersBtn').style.display = 'none';
        modal.classList.add('show');

        $('dvlList').innerHTML = '<div style="text-align:center;padding:2rem;color:var(--text-3)"><i class="fas fa-spinner fa-pulse"></i> Đang tải...</div>';
        var devices = await loadDevices(email);
        updateModalUI(email, devices);
        renderDeviceList($('dvlList'), devices, email, false);
    }

    /* ═══ INIT ═══ */
    function initDvl() {
        var closeBtn = $('dvlCloseBtn');
        if (closeBtn && !closeBtn.__dvlBound) { closeBtn.__dvlBound = true; closeBtn.addEventListener('click', closeManageModal); }
        var doneBtn = $('dvlDoneBtn');
        if (doneBtn && !doneBtn.__dvlBound) { doneBtn.__dvlBound = true; doneBtn.addEventListener('click', closeManageModal); }
        var modal = $('dvlModal');
        if (modal && !modal.__dvlBound) {
            modal.__dvlBound = true;
            modal.addEventListener('click', function(e) { if (e.target === modal) closeManageModal(); });
        }
        var logoutOthers = $('dvlLogoutOthersBtn');
        if (logoutOthers && !logoutOthers.__dvlBound) { logoutOthers.__dvlBound = true; logoutOthers.addEventListener('click', logoutOtherDevices); }

        document.addEventListener('keydown', function(e) {
            if (e.key !== 'Escape') return;
            var m1 = $('dvlModal');
            if (m1 && m1.classList.contains('show')) { closeManageModal(); return; }
            var m2 = $('dvlVerifyModal');
            if (m2 && m2.classList.contains('show')) {
                stopTimer();
                m2.classList.remove('show');
                if (typeof auth !== 'undefined' && auth) auth.signOut();
            }
        });

        var tries = 0;
        var injectTimer = setInterval(function() {
            tries++;
            try {
                injectDropdownButton();
                injectAdminDeviceButton();
                injectAdminPendingButton();
            } catch(e) {}
            if (tries > 120) clearInterval(injectTimer);
        }, 500);

        if (typeof auth !== 'undefined' && auth && !auth.__dvlHooked) {
            auth.__dvlHooked = true;
            auth.onAuthStateChanged(function(user) {
                if (user && user.email) {
                    setTimeout(updateDropdownBadge, 1500);
                    setTimeout(function() { if (__dvlHasAdminRights()) updatePendingBadge(); }, 2000);
                }
            });
        }

        var userList = document.getElementById('userList');
        if (userList && !userList.__dvlObserved) {
            userList.__dvlObserved = true;
            var mo = new MutationObserver(function() { try { injectAdminDeviceButton(); } catch(e) {} });
            mo.observe(userList, { childList: true, subtree: true });
        }

        setInterval(function() {
            if (typeof currentUser !== 'undefined' && currentUser && currentUser.email) {
                checkIfKicked(currentUser.email);
            }
        }, 30000);

        setInterval(function() { if (__dvlHasAdminRights()) updatePendingBadge(); }, 30000);
    }

    /* ═══ PUBLIC API ═══ */
    window.__dvlCheckAndRegister = registerCurrentDevice;
    window.__dvlShowVerifyModal = showVerifyModal;
    window.__dvlOpenManage = openManageModal;
    window.__dvlOpenPending = openPendingList;
    window.__dvlSendVerifyEmail = sendVerifyEmail;
    window.__dvlMaxDevices = MAX_DEVICES;
    window.__dvlIsSuperAdmin = __dvlIsSuperAdmin;

    window.__dvlDebug = {
        openManage: openManageModal,
        openPending: openPendingList,
        openAdmin: openAdminDeviceView,
        getDeviceId: getDeviceId,
        isSuperAdmin: __dvlIsSuperAdmin,
        hasAdminRights: __dvlHasAdminRights,
        loadDevices: loadDevices,
        register: registerCurrentDevice,
        checkKicked: checkIfKicked
    };

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initDvl);
    } else {
        initDvl();
    }

    console.log('[Device Limiter] Module loaded — OTP qua server bank');
})()
"""
    return js.replace('__SERVER_URL__', SERVER_URL)


if __name__ == "__main__":
    css = build_device_css()
    html = build_device_html()
    js = build_device_js()

    print("CSS:  %d ký tự" % len(css))
    print("HTML: %d ký tự" % len(html))
    print("JS:   %d ký tự" % len(js))
    print("✅ Module sẵn sàng — OTP qua server bank")

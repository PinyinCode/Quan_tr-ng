# -*- coding: utf-8 -*-
"""Module giới hạn 2 thiết bị — xác nhận qua EMAIL hoặc ADMIN duyệt.

✅ FIX 2026-10:
   - Super admin BYPASS device limit (không bị chặn login máy 3)
   - Super admin VẪN THẤY nút "Yêu cầu chờ duyệt" + duyệt được
   - Super admin VẪN xem được thiết bị của user khác
   - Máy thứ 3 login → tạo pending + gửi email + báo admin
   - User có 2 cách xác nhận: bấm link mail HOẶC nhờ admin duyệt
   - Tab cũ poll 5s → tự vào khi có confirm
"""


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
.dvl-steps{margin:1rem 0;padding:1rem;background:linear-gradient(135deg,rgba(79,70,229,.06),rgba(124,58,237,.03));border:1px solid rgba(124,58,237,.2);border-radius:12px;display:flex;flex-direction:column;gap:.6rem}
.dvl-steps.admin{background:linear-gradient(135deg,rgba(245,158,11,.08),rgba(217,119,6,.04));border-color:rgba(245,158,11,.3)}
.dvl-step{display:flex;align-items:flex-start;gap:.6rem;font-size:.8rem;color:var(--text-2);line-height:1.5}
.dvl-step .num{width:22px;height:22px;border-radius:50%;background:linear-gradient(135deg,#4f46e5,#7c3aed);color:#fff;display:flex;align-items:center;justify-content:center;font-size:.68rem;font-weight:900;flex-shrink:0;line-height:1}
.dvl-step .num.warn{background:linear-gradient(135deg,#f59e0b,#d97706)}
.dvl-step b{color:var(--text)}
.dvl-steps-header{font-weight:800;font-size:.85rem;margin-bottom:.5rem;display:flex;align-items:center;gap:.4rem}
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
}
"""


def build_device_html():
    return r"""
<!-- ═══════════ MODAL QUẢN LÝ THIẾT BỊ (dùng chung user + admin) ═══════════ -->
<div class="dvl-modal" id="dvlModal">
    <div class="dvl-box">
        <button class="dvl-close" id="dvlCloseBtn" type="button" aria-label="Đóng">
            <i class="fas fa-times"></i>
        </button>
        <div class="dvl-icon" id="dvlIcon"><i class="fas fa-mobile-screen-button"></i></div>
        <div class="dvl-title" id="dvlTitle">Quản lý thiết bị</div>
        <div class="dvl-subtitle" id="dvlSubtitle">
            Tài khoản của bạn chỉ được đăng nhập trên tối đa <b>2 thiết bị</b>.
        </div>
        <div class="dvl-count-box" id="dvlCountBox">
            <div class="dvl-count-num" id="dvlCountNum">0</div>
            <div class="dvl-count-label" id="dvlCountLabel">/ 2 thiết bị đang hoạt động</div>
        </div>
        <div class="dvl-list" id="dvlList">
            <div style="text-align:center;padding:2rem 1rem;color:var(--text-3)"><i class="fas fa-spinner fa-pulse"></i> Đang tải...</div>
        </div>
        <div class="dvl-warning" id="dvlWarning" style="display:none">
            <i class="fas fa-exclamation-triangle"></i>
            <div>Bạn đã đạt giới hạn <b>2 thiết bị</b>. Vui lòng xóa bớt 1 thiết bị để đăng nhập máy mới.</div>
        </div>
        <div class="dvl-actions">
            <button type="button" class="dvl-btn" id="dvlLogoutOthersBtn">
                <i class="fas fa-sign-out-alt"></i> Đăng xuất thiết bị khác
            </button>
            <button type="button" class="dvl-btn primary" id="dvlDoneBtn">
                <i class="fas fa-check"></i> Xong
            </button>
        </div>
    </div>
</div>

<!-- ═══════════ MODAL XÁC NHẬN ĐĂNG NHẬP THIẾT BỊ MỚI ═══════════ -->
<div class="dvl-modal" id="dvlVerifyModal">
    <div class="dvl-box">
        <div class="dvl-icon mail"><i class="fas fa-envelope-circle-check"></i></div>
        <div class="dvl-title">Xác nhận đăng nhập thiết bị mới</div>
        <div class="dvl-subtitle">
            Tài khoản của bạn đã đăng nhập trên <b>2 thiết bị</b> khác.
            Để bảo mật, bạn cần xác nhận bằng <b>1 trong 2 cách</b> sau:
        </div>

        <div style="text-align:center;margin-bottom:1rem">
            <span class="dvl-email-highlight" id="dvlVerifyEmail">user@example.com</span>
        </div>

        <!-- Cách 1: Email -->
        <div class="dvl-steps" id="dvlStepEmail">
            <div class="dvl-steps-header" style="color:#4f46e5">
                <i class="fas fa-envelope"></i> Cách 1: Xác nhận qua email
            </div>
            <div class="dvl-step">
                <span class="num">1</span>
                <div>Mở email <b id="dvlEmailInline">user@example.com</b> (kiểm tra cả <b>Spam</b>)</div>
            </div>
            <div class="dvl-step">
                <span class="num">2</span>
                <div>Bấm vào <b>link xác nhận</b> trong email</div>
            </div>
            <div class="dvl-step">
                <span class="num">3</span>
                <div>Quay lại tab này — máy mới sẽ tự vào, máy cũ nhất bị đăng xuất</div>
            </div>
        </div>

        <!-- Cảnh báo nếu mail không gửi được -->
        <div class="dvl-warning error" id="dvlEmailErrorBox" style="display:none">
            <i class="fas fa-exclamation-triangle"></i>
            <div id="dvlEmailErrorMsg">Không gửi được email. Vui lòng dùng <b>Cách 2</b> (nhờ admin duyệt).</div>
        </div>

        <!-- Cách 2: Admin -->
        <div class="dvl-steps admin" id="dvlStepAdmin">
            <div class="dvl-steps-header" style="color:#d97706">
                <i class="fas fa-user-shield"></i> Cách 2: Nhờ admin duyệt
            </div>
            <div class="dvl-step">
                <span class="num warn">1</span>
                <div>Liên hệ admin qua <b>Zalo / Facebook / Hotline</b></div>
            </div>
            <div class="dvl-step">
                <span class="num warn">2</span>
                <div>Admin sẽ thấy yêu cầu trong panel và bấm <b>Duyệt</b></div>
            </div>
            <div class="dvl-step">
                <span class="num warn">3</span>
                <div>Trang này sẽ tự vào app sau khi admin duyệt</div>
            </div>
        </div>

        <div style="text-align:center;margin-top:.75rem">
            <div class="dvl-timer" id="dvlTimer">
                <i class="fas fa-hourglass-half"></i> Còn lại: <span id="dvlTimerCount">05:00</span>
            </div>
        </div>

        <div class="dvl-warning" style="margin-top:1rem">
            <i class="fas fa-shield-alt"></i>
            <div>
                Nếu <b>KHÔNG phải bạn</b> đang đăng nhập máy mới, hãy bấm <b>Hủy</b> và đổi mật khẩu ngay.
            </div>
        </div>

        <div class="dvl-actions">
            <button type="button" class="dvl-btn" id="dvlVerifyCancelBtn">
                <i class="fas fa-times"></i> Hủy
            </button>
            <button type="button" class="dvl-btn violet" id="dvlVerifyResendBtn">
                <i class="fas fa-paper-plane"></i> Gửi lại email
            </button>
            <button type="button" class="dvl-btn primary" id="dvlVerifyCheckBtn">
                <i class="fas fa-sync-alt"></i> Tôi đã xác nhận
            </button>
        </div>
    </div>
</div>

<!-- ═══════════ MODAL XÁC NHẬN THÀNH CÔNG ═══════════ -->
<div class="dvl-modal" id="dvlVerifySuccessModal">
    <div class="dvl-box">
        <div class="dvl-icon" style="background:linear-gradient(135deg,#16a34a,#22c55e)"><i class="fas fa-check"></i></div>
        <div class="dvl-title">Xác nhận thành công</div>
        <div class="dvl-subtitle">
            Thiết bị mới đã được đăng nhập. Thiết bị cũ nhất đã bị đăng xuất khỏi tài khoản.
        </div>
        <div class="dvl-actions">
            <button type="button" class="dvl-btn green" id="dvlSuccessContinueBtn">
                <i class="fas fa-arrow-right"></i> Tiếp tục
            </button>
        </div>
    </div>
</div>
"""


def build_device_js():
    return r"""
(function() {
    'use strict';

    var MAX_DEVICES = 2;
    var VERIFY_TIMEOUT = 5 * 60 * 1000;
    var DEVICE_ID_KEY = 'dvl_device_id';
    var DEVICE_NAME_KEY = 'dvl_device_name';
    var VERIFY_TOKEN_KEY = 'dvl_verify_token';

    var currentDeviceId = null;
    var _timerInterval = null;
    var _verifyExpireAt = null;
    var _verifyToken = null;
    var _verifyPoller = null;

    function $(id) { return document.getElementById(id); }
    function esc(s) {
        if (s == null) return '';
        return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;')
            .replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');
    }

    /* ═══════════════════════════════════════════════════════════
       ⭐ SUPER ADMIN — BYPASS device limit (nhưng vẫn được duyệt)
       ═══════════════════════════════════════════════════════════ */
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

    /* ⭐ Có quyền admin? (bao gồm cả super admin) */
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
        } catch(e) {
            return 'Thiết bị';
        }
    }

    function detectDeviceType() {
        try {
            var ua = navigator.userAgent || '';
            if (/Mobile|iPhone|Android.*Mobile/i.test(ua)) return 'mobile';
            if (/iPad|Tablet|Android/i.test(ua)) return 'tablet';
            return 'desktop';
        } catch(e) {
            return 'desktop';
        }
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

    function generateToken() {
        var chars = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
        var token = '';
        for (var i = 0; i < 24; i++) {
            token += chars.charAt(Math.floor(Math.random() * chars.length));
        }
        return token;
    }

    async function loadDevices(email) {
        if (!db || !email) return [];
        try {
            var doc = await db.collection('allowed_users').doc(email.toLowerCase()).get();
            if (!doc.exists) return [];
            var data = doc.data() || {};
            return Array.isArray(data.devices) ? data.devices : [];
        } catch(e) {
            console.warn('[DVL] Load error:', e);
            return [];
        }
    }

    async function saveDevices(email, devices) {
        if (!db || !email) return false;
        try {
            await db.collection('allowed_users').doc(email.toLowerCase()).set({
                devices: devices,
                devicesUpdatedAt: firebase.firestore.FieldValue.serverTimestamp()
            }, { merge: true });
            return true;
        } catch(e) {
            console.warn('[DVL] Save error:', e);
            return false;
        }
    }

    /* ═══════════════════════════════════════════════════════════
       Tạo yêu cầu xác nhận
       ═══════════════════════════════════════════════════════════ */
    async function createVerificationRequest(email) {
        if (!email || !db) return null;

        var deviceId = getDeviceId();
        var deviceName = getDeviceName();
        var deviceType = detectDeviceType();
        var token = generateToken();
        var now = Date.now();
        var expireAt = now + VERIFY_TIMEOUT;

        try {
            await db.collection('allowed_users').doc(email.toLowerCase())
                .collection('pending_devices').doc(deviceId).set({
                    deviceId: deviceId,
                    deviceName: deviceName,
                    deviceType: deviceType,
                    userAgent: (navigator.userAgent || '').substring(0, 200),
                    token: token,
                    createdAt: firebase.firestore.FieldValue.serverTimestamp(),
                    expireAt: firebase.firestore.Timestamp.fromMillis(expireAt),
                    status: 'pending',
                    emailSent: false,
                    emailAttempts: 0
                });

            try { sessionStorage.setItem(VERIFY_TOKEN_KEY, token); } catch(e) {}
            return token;
        } catch(e) {
            console.warn('[DVL] Create verify error:', e);
            return null;
        }
    }

    async function checkVerification(email) {
        if (!email || !db) return { confirmed: false };
        if (__dvlIsSuperAdmin(email)) return { confirmed: false };

        var deviceId = getDeviceId();
        try {
            var snap = await db.collection('allowed_users').doc(email.toLowerCase())
                .collection('pending_devices')
                .where('deviceId', '==', deviceId)
                .limit(1)
                .get();

            if (snap.empty) return { confirmed: false, notFound: true };

            var doc = snap.docs[0];
            var data = doc.data();

            if (data.status === 'confirmed') {
                return { confirmed: true, data: data };
            }

            if (data.expireAt) {
                var expireMs = data.expireAt.toMillis ? data.expireAt.toMillis() : data.expireAt.seconds * 1000;
                if (Date.now() > expireMs) {
                    return { confirmed: false, expired: true };
                }
                return { confirmed: false, expireAt: expireMs, token: data.token };
            }

            return { confirmed: false };
        } catch(e) {
            console.warn('[DVL] Check verify error:', e);
            return { confirmed: false };
        }
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
                .collection('pending_devices')
                .where('deviceId', '==', deviceId)
                .get();
            var batch = db.batch();
            snap.forEach(function(d) { batch.delete(d.ref); });
            await batch.commit();
        } catch(e) {}

        try { sessionStorage.removeItem(VERIFY_TOKEN_KEY); } catch(e) {}

        return true;
    }

    async function checkIfKicked(email) {
        if (!email || !db) return false;
        if (__dvlIsSuperAdmin(email)) return false;

        var deviceId = getDeviceId();
        try {
            var doc = await db.collection('allowed_users')
                .doc(email.toLowerCase())
                .collection('kicked_devices')
                .doc(deviceId)
                .get();

            if (doc.exists) {
                await doc.ref.delete();

                if (typeof showUserChangedToast === 'function') {
                    showUserChangedToast('⚠️ Thiết bị đã bị đăng xuất do có máy mới xác nhận', 'error');
                } else {
                    alert('⚠️ Thiết bị đã bị đăng xuất\n\nTài khoản của bạn vừa xác nhận đăng nhập trên thiết bị khác.');
                }

                if (typeof auth !== 'undefined' && auth) auth.signOut();
                return true;
            }
        } catch(e) {
            console.warn('[DVL] checkIfKicked error:', e);
        }
        return false;
    }

    /* ═══════════════════════════════════════════════════════════
       Đăng ký thiết bị khi login
       ═══════════════════════════════════════════════════════════ */
    async function registerCurrentDevice(email) {
        if (!email || !db) return { allowed: true };

        /* ⭐ SUPER ADMIN — BYPASS HOÀN TOÀN */
        if (__dvlIsSuperAdmin(email)) {
            console.log('[DVL] Super admin — bypass device limit');
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
                .collection('pending_devices')
                .where('deviceId', '==', deviceId)
                .limit(1)
                .get();

            if (!pendingSnap.empty) {
                var pdoc = pendingSnap.docs[0];
                var pd = pdoc.data();

                if (pd.status === 'confirmed') {
                    var ok = await completeVerification(email);
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
                            token: pd.token,
                            existing: true,
                            emailSent: pd.emailSent === true,
                            emailError: null
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

        var token = await createVerificationRequest(email);

        var emailResult = { ok: false, reason: 'not_sent' };
        try {
            emailResult = await sendVerifyEmail(email, token);

            try {
                await db.collection('allowed_users').doc(email.toLowerCase())
                    .collection('pending_devices').doc(deviceId)
                    .update({
                        emailSent: emailResult.ok === true,
                        emailAttempts: firebase.firestore.FieldValue.increment(1),
                        emailError: emailResult.ok ? null : (emailResult.reason || 'unknown')
                    });
            } catch(_e) {}
        } catch(e) {
            console.warn('[DVL] Email send failed (admin vẫn duyệt được):', e);
        }

        return {
            allowed: false,
            needsVerify: true,
            expireAt: now + VERIFY_TIMEOUT,
            token: token,
            devices: devices,
            emailSent: emailResult.ok === true,
            emailError: emailResult.ok ? null : emailResult.reason
        };
    }

    async function sendVerifyEmail(email, token) {
        if (!email || !auth) return { ok: false, reason: 'no_auth' };

        try {
            var currentHost = window.location.origin + window.location.pathname;
            var actionCodeSettings = {
                url: currentHost + '?dvl_verify=' + encodeURIComponent(token),
                handleCodeInApp: true
            };

            await auth.sendSignInLinkToEmail(email, actionCodeSettings);
            try { localStorage.setItem('dvl_pending_email', email); } catch(e) {}

            console.log('[DVL] ✅ Đã gửi email xác nhận đến:', email);
            return { ok: true };

        } catch(e) {
            console.error('[DVL] ❌ Send verify email error:', e.code, e.message);
            return { ok: false, reason: e.code || e.message };
        }
    }

    async function checkVerifyLink() {
        try {
            var params = new URLSearchParams(window.location.search);
            var token = params.get('dvl_verify');
            if (!token) return false;

            var pendingEmail = null;
            try { pendingEmail = localStorage.getItem('dvl_pending_email'); } catch(e) {}

            var email = pendingEmail ||
                        (auth && auth.currentUser ? auth.currentUser.email : null);

            if (!email) return false;

            if (__dvlIsSuperAdmin(email)) {
                var url0 = window.location.pathname;
                window.history.replaceState({}, document.title, url0);
                return false;
            }

            if (auth && auth.isSignInWithEmailLink && auth.isSignInWithEmailLink(email, window.location.href)) {
                try {
                    await auth.signInWithEmailLink(email, window.location.href);
                } catch(e) {
                    console.warn('[DVL] SignInWithEmailLink error:', e);
                }
            }

            if (db) {
                try {
                    var snap = await db.collection('allowed_users').doc(email.toLowerCase())
                        .collection('pending_devices')
                        .where('token', '==', token)
                        .limit(1)
                        .get();

                    if (snap.empty) {
                        try { localStorage.removeItem('dvl_pending_email'); } catch(e) {}
                        var url1 = window.location.pathname;
                        window.history.replaceState({}, document.title, url1);
                        return { verified: false, reason: 'not_found' };
                    }

                    var pdoc = snap.docs[0];
                    var pdata = pdoc.data();

                    var expMs = pdata.expireAt
                        ? (pdata.expireAt.toMillis ? pdata.expireAt.toMillis() : pdata.expireAt.seconds * 1000)
                        : 0;
                    if (expMs && Date.now() > expMs) {
                        try { await pdoc.ref.delete(); } catch(e) {}
                        var url2 = window.location.pathname;
                        window.history.replaceState({}, document.title, url2);
                        return { verified: false, reason: 'expired' };
                    }

                    if (pdata.status !== 'confirmed') {
                        await pdoc.ref.update({
                            status: 'confirmed',
                            confirmedAt: firebase.firestore.FieldValue.serverTimestamp(),
                            confirmedVia: 'email_link'
                        });
                    }

                    try { localStorage.removeItem('dvl_pending_email'); } catch(e) {}

                    var url3 = window.location.pathname;
                    window.history.replaceState({}, document.title, url3);

                    console.log('[DVL] ✅ Đã confirm pending cho deviceId:', pdata.deviceId);
                    return { verified: true, email: email, deviceId: pdata.deviceId };
                } catch(e) {
                    console.warn('[DVL] Confirm pending error:', e);
                    return { verified: false, reason: 'error' };
                }
            }

            return { verified: false, reason: 'no_db' };
        } catch(e) {
            console.warn('[DVL] checkVerifyLink error:', e);
            return false;
        }
    }

    /* ═══════════════════════════════════════════════════════════
       RENDER DANH SÁCH THIẾT BỊ
       ═══════════════════════════════════════════════════════════ */
    function renderDeviceList(containerEl, devices, email, isLimitView) {
        if (!containerEl) return;
        if (!devices || devices.length === 0) {
            containerEl.innerHTML = '<div style="text-align:center;padding:2rem 1rem;color:var(--text-3)">' +
                '<i class="fas fa-inbox" style="font-size:2rem;opacity:.4;margin-bottom:.5rem;display:block"></i>Chưa có thiết bị nào</div>';
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
                    removeBtn = '<button class="dvl-remove-btn" disabled title="Không thể xóa thiết bị đang dùng"><i class="fas fa-lock"></i></button>';
                } else {
                    removeBtn = '<button class="dvl-remove-btn" data-device-id="' + esc(d.id) + '" title="Xóa thiết bị này"><i class="fas fa-trash"></i></button>';
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
        if (!email || !deviceId) return;
        if (!confirm('Xóa thiết bị này?\n\nThiết bị đó sẽ bị đăng xuất.')) return;

        try {
            var devices = await loadDevices(email);
            var filtered = devices.filter(function(d) { return d.id !== deviceId; });
            await saveDevices(email, filtered);

            updateModalUI(email, filtered);
            renderDeviceList($('dvlList'), filtered, email, false);

            if (typeof showUserChangedToast === 'function') {
                showUserChangedToast('📱 Đã xóa thiết bị', 'success');
            }
        } catch(e) {
            alert('Lỗi xóa thiết bị: ' + e.message);
        }
    }

    function updateModalUI(email, devices) {
        var count = devices.length;
        var countNum = $('dvlCountNum');
        var countLabel = $('dvlCountLabel');
        var countBox = $('dvlCountBox');
        var warning = $('dvlWarning');
        var icon = $('dvlIcon');

        if (countNum) countNum.textContent = count;
        if (countLabel) countLabel.innerHTML = '/ ' + MAX_DEVICES + ' thiết bị đang hoạt động';

        if (countBox) {
            countBox.classList.remove('warn');
            if (count >= MAX_DEVICES) countBox.classList.add('warn');
        }
        if (warning) warning.style.display = (count >= MAX_DEVICES) ? 'flex' : 'none';
        if (icon) {
            icon.classList.remove('warn', 'danger');
            if (count >= MAX_DEVICES) icon.classList.add('warn');
        }
    }

    async function openManageModal() {
        if (typeof currentUser === 'undefined' || !currentUser || !currentUser.email) {
            alert('Vui lòng đăng nhập trước.');
            return;
        }

        if (__dvlIsSuperAdmin(currentUser.email)) return;

        var modal = $('dvlModal');
        if (!modal) return;

        $('dvlTitle').textContent = 'Quản lý thiết bị';
        $('dvlSubtitle').innerHTML = 'Tài khoản của bạn chỉ được đăng nhập trên tối đa <b>2 thiết bị</b>.';
        $('dvlCountBox').style.display = 'flex';
        $('dvlLogoutOthersBtn').style.display = 'inline-flex';

        modal.classList.add('show');

        var list = $('dvlList');
        if (list) list.innerHTML = '<div style="text-align:center;padding:2rem 1rem;color:var(--text-3)"><i class="fas fa-spinner fa-pulse"></i> Đang tải...</div>';

        var devices = await loadDevices(currentUser.email);
        updateModalUI(currentUser.email, devices);
        renderDeviceList(list, devices, currentUser.email, false);
    }

    function closeManageModal() {
        var m = $('dvlModal');
        if (m) m.classList.remove('show');
    }

    function showVerifyModal(email, expireAt, token, emailSent, emailError) {
        var modal = $('dvlVerifyModal');
        if (!modal) return;

        var emailEl = $('dvlVerifyEmail');
        if (emailEl) emailEl.textContent = email;
        var emailInline = $('dvlEmailInline');
        if (emailInline) emailInline.textContent = email;

        var errBox = $('dvlEmailErrorBox');
        var errMsg = $('dvlEmailErrorMsg');
        var stepEmail = $('dvlStepEmail');

        if (emailSent === false) {
            if (errBox) errBox.style.display = 'flex';
            if (errMsg) {
                var reason = emailError || 'Không rõ nguyên nhân';
                if (reason === 'auth/operation-not-allowed') reason = 'Chưa bật Email Link trên Firebase Console.';
                else if (reason === 'auth/unauthorized-continue-uri') reason = 'Domain chưa được add vào Authorized domains.';
                else if (reason === 'auth/quota-exceeded') reason = 'Đã vượt quota gửi mail hôm nay.';
                else if (reason === 'auth/invalid-email') reason = 'Email không hợp lệ.';
                else if (reason === 'auth/network-request-failed') reason = 'Lỗi mạng — thử lại sau.';
                errMsg.innerHTML = '<b>Không gửi được email:</b> ' + esc(reason) +
                                   '<br>Vui lòng dùng <b>Cách 2</b> (nhờ admin duyệt).';
            }
            if (stepEmail) stepEmail.style.opacity = '0.4';
        } else {
            if (errBox) errBox.style.display = 'none';
            if (stepEmail) stepEmail.style.opacity = '1';
        }

        if (token) {
            _verifyToken = token;
            try { sessionStorage.setItem(VERIFY_TOKEN_KEY, token); } catch(e) {}
        }

        modal.classList.add('show');

        _verifyExpireAt = expireAt || (Date.now() + VERIFY_TIMEOUT);
        startTimer();

        if (_verifyPoller) clearInterval(_verifyPoller);
        _verifyPoller = setInterval(async function() {
            if (!modal.classList.contains('show')) {
                clearInterval(_verifyPoller);
                _verifyPoller = null;
                return;
            }
            var res = await checkVerification(email);
            if (res.confirmed) {
                clearInterval(_verifyPoller);
                _verifyPoller = null;
                stopTimer();
                await completeVerification(email);
                modal.classList.remove('show');
                showSuccessModal();
            }
        }, 5000);

        var cancelBtn = $('dvlVerifyCancelBtn');
        if (cancelBtn) {
            cancelBtn.onclick = function() {
                stopTimer();
                if (_verifyPoller) { clearInterval(_verifyPoller); _verifyPoller = null; }
                modal.classList.remove('show');
                if (typeof auth !== 'undefined' && auth) auth.signOut();
            };
        }

        var resendBtn = $('dvlVerifyResendBtn');
        if (resendBtn) {
            resendBtn.onclick = async function() {
                var orig = resendBtn.innerHTML;
                resendBtn.disabled = true;
                resendBtn.innerHTML = '<span class="dvl-spinner"></span> Đang gửi...';

                var result = await sendVerifyEmail(email, _verifyToken);

                if (result.ok) {
                    resendBtn.innerHTML = '<i class="fas fa-check"></i> Đã gửi';
                    if (errBox) errBox.style.display = 'none';
                    if (stepEmail) stepEmail.style.opacity = '1';

                    try {
                        await db.collection('allowed_users').doc(email.toLowerCase())
                            .collection('pending_devices').doc(getDeviceId())
                            .update({
                                emailSent: true,
                                emailAttempts: firebase.firestore.FieldValue.increment(1),
                                emailError: null
                            });
                    } catch(_e) {}

                    setTimeout(function() {
                        resendBtn.disabled = false;
                        resendBtn.innerHTML = orig;
                    }, 3000);
                } else {
                    alert('❌ Không gửi được email.\n\nLý do: ' + (result.reason || 'Không rõ') +
                          '\n\n💡 Hãy dùng Cách 2 — nhờ admin duyệt.');
                    resendBtn.disabled = false;
                    resendBtn.innerHTML = orig;
                }
            };
        }

        var checkBtn = $('dvlVerifyCheckBtn');
        if (checkBtn) {
            checkBtn.onclick = async function() {
                var orig = checkBtn.innerHTML;
                checkBtn.disabled = true;
                checkBtn.innerHTML = '<span class="dvl-spinner"></span> Đang kiểm tra...';

                var res = await checkVerification(email);
                if (res.confirmed) {
                    stopTimer();
                    if (_verifyPoller) { clearInterval(_verifyPoller); _verifyPoller = null; }
                    await completeVerification(email);
                    modal.classList.remove('show');
                    showSuccessModal();
                } else {
                    alert('Chưa xác nhận.\n\nVui lòng:\n• Kiểm tra email (cả Spam) và bấm link\n• Hoặc nhờ admin duyệt trong panel');
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
                if (_verifyPoller) { clearInterval(_verifyPoller); _verifyPoller = null; }
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
        var el = $('dvlTimerCount');
        if (el) el.textContent = String(m).padStart(2, '0') + ':' + String(s).padStart(2, '0');
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

        if (keep.length === devices.length) {
            alert('Bạn chỉ có 1 thiết bị đang đăng nhập.');
            return;
        }

        if (!confirm('Đăng xuất tất cả thiết bị khác?\n\nChỉ giữ lại thiết bị hiện tại.')) return;

        await saveDevices(currentUser.email, keep);
        updateModalUI(currentUser.email, keep);
        renderDeviceList($('dvlList'), keep, currentUser.email, false);

        if (typeof showUserChangedToast === 'function') {
            showUserChangedToast('📱 Đã đăng xuất thiết bị khác', 'success');
        }
    }

    /* ═══════════════════════════════════════════════════════════
       Dropdown — nút "Quản lý thiết bị"
       ═══════════════════════════════════════════════════════════ */
    function injectDropdownButton() {
        var dropdown = document.getElementById('userDropdown');
        if (!dropdown) return false;

        var curEmail = '';
        try {
            if (typeof currentUser !== 'undefined' && currentUser && currentUser.email) {
                curEmail = currentUser.email;
            } else if (typeof auth !== 'undefined' && auth && auth.currentUser) {
                curEmail = auth.currentUser.email || '';
            }
        } catch(e) {}

        /* Super admin — vẫn hiện nút "Quản lý thiết bị" nếu muốn (nhưng không cần)
           Hiện tại: ẩn nút "Quản lý thiết bị" cho super admin để giữ dropdown gọn */
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
                    try {
                        var dd = document.getElementById('userDropdown');
                        if (dd) dd.classList.remove('show');
                    } catch(_e) {}
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
            var b = document.getElementById('dvlDropdownBadge');
            if (b) b.style.display = 'none';
            return;
        }

        var badge = document.getElementById('dvlDropdownBadge');
        if (!badge) return;
        badge.style.display = '';

        var devices = await loadDevices(currentUser.email);
        var count = devices.length;
        badge.textContent = count + '/' + MAX_DEVICES;
        badge.classList.remove('warn');
        if (count >= MAX_DEVICES) badge.classList.add('warn');
    }

    /* ═══════════════════════════════════════════════════════════
       ⭐ ADMIN — Tab "Yêu cầu chờ duyệt" (bao gồm cả super admin)
       ═══════════════════════════════════════════════════════════ */
    async function updatePendingBadge() {
        if (!db) return;
        if (!__dvlHasAdminRights()) return;

        try {
            var snap = await db.collectionGroup('pending_devices')
                .where('status', '==', 'pending')
                .get();

            var count = snap.size;
            var badge = document.getElementById('dvlPendingBadge');
            if (badge) {
                badge.textContent = count;
                badge.style.display = count > 0 ? 'inline-block' : 'none';
            }
            return count;
        } catch(e) {
            console.warn('[DVL] updatePendingBadge error:', e);
            return 0;
        }
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
        btn.innerHTML = '<i class="fas fa-clock" style="color:#f59e0b"></i> Yêu cầu chờ duyệt' +
                        '<span class="dvl-badge warn" id="dvlPendingBadge" style="display:none">0</span>';

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
        if (!__dvlHasAdminRights()) {
            alert('Chỉ admin mới có quyền này.');
            return;
        }

        var modal = $('dvlModal');
        if (!modal) return;

        $('dvlTitle').textContent = 'Yêu cầu chờ duyệt';
        $('dvlSubtitle').innerHTML = 'Danh sách thiết bị đang chờ admin xác nhận. Bấm <b>Duyệt</b> để cho phép đăng nhập.';
        $('dvlCountBox').style.display = 'none';
        $('dvlWarning').style.display = 'none';
        $('dvlLogoutOthersBtn').style.display = 'none';

        modal.classList.add('show');

        var list = $('dvlList');
        list.innerHTML = '<div style="text-align:center;padding:2rem;color:var(--text-3)"><i class="fas fa-spinner fa-pulse"></i> Đang tải...</div>';

        try {
            var snap = await db.collectionGroup('pending_devices')
                .where('status', '==', 'pending')
                .get();

            if (snap.empty) {
                list.innerHTML = '<div style="text-align:center;padding:2rem;color:var(--text-3)">' +
                    '<i class="fas fa-inbox" style="font-size:2rem;opacity:.4;display:block;margin-bottom:.5rem"></i>' +
                    'Không có yêu cầu nào</div>';
                return;
            }

            var items = [];
            snap.forEach(function(doc) {
                var d = doc.data();
                var email = doc.ref.parent.parent.id;
                items.push({ doc: doc, data: d, email: email });
            });
            items.sort(function(a, b) {
                var ta = a.data.createdAt ? a.data.createdAt.toMillis() : 0;
                var tb = b.data.createdAt ? b.data.createdAt.toMillis() : 0;
                return tb - ta;
            });

            var html = '';
            items.forEach(function(item) {
                var d = item.data;
                var email = item.email;
                var deviceId = d.deviceId;

                var created = d.createdAt && d.createdAt.toMillis
                    ? new Date(d.createdAt.toMillis()).toLocaleString('vi-VN')
                    : 'Không rõ';

                var expMs = d.expireAt ? (d.expireAt.toMillis ? d.expireAt.toMillis() : d.expireAt.seconds * 1000) : 0;
                var remain = expMs ? Math.max(0, Math.floor((expMs - Date.now()) / 1000)) : 0;
                var remainStr = remain > 0
                    ? Math.floor(remain / 60) + 'p ' + (remain % 60) + 's'
                    : 'Hết hạn';

                var emailStatus = d.emailSent
                    ? '<span class="dvl-tag ok"><i class="fas fa-envelope"></i> Đã gửi mail</span>'
                    : '<span class="dvl-tag" style="background:rgba(220,38,38,.1);color:#dc2626;border-color:rgba(220,38,38,.3)"><i class="fas fa-envelope"></i> Mail lỗi</span>';

                html += '<div class="dvl-item" data-email="' + esc(email) + '" data-device-id="' + esc(deviceId) + '">' +
                    '<div class="dvl-item-icon"><i class="fas ' + getDeviceIcon(d.deviceType || 'desktop') + '"></i></div>' +
                    '<div class="dvl-item-info">' +
                        '<div class="dvl-item-name">' + esc(email) + '</div>' +
                        '<div class="dvl-item-meta">' +
                            '<span class="dvl-tag info"><i class="fas fa-mobile"></i> ' + esc(d.deviceName || 'Thiết bị') + '</span>' +
                            emailStatus +
                            '<span><i class="fas fa-clock"></i> ' + created + '</span>' +
                            '<span style="color:' + (remain > 0 ? '#16a34a' : '#dc2626') + '">⏱ ' + remainStr + '</span>' +
                        '</div>' +
                    '</div>' +
                    '<button class="dvl-btn green small dvl-approve-btn">' +
                        '<i class="fas fa-check"></i> Duyệt' +
                    '</button>' +
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

                        if (typeof showUserChangedToast === 'function') {
                            showUserChangedToast('✅ Đã duyệt thiết bị cho ' + email, 'success');
                        }
                    } catch(err) {
                        alert('Lỗi: ' + err.message);
                        this.disabled = false;
                        this.innerHTML = orig;
                    }
                };
            });

        } catch(e) {
            console.error('[DVL] openPendingList error:', e);
            list.innerHTML = '<div style="text-align:center;padding:2rem;color:#dc2626">Lỗi: ' + esc(e.message) + '</div>';
        }
    }

    /* ═══════════════════════════════════════════════════════════
       Nút admin xem thiết bị của user (trong #userList)
       ═══════════════════════════════════════════════════════════ */
    function injectAdminDeviceButton() {
        var userList = document.getElementById('userList');
        if (!userList) return;

        var rows = userList.querySelectorAll('.user-row[data-email]');
        rows.forEach(function(row) {
            if (row.querySelector('.dvl-btn-row')) return;

            var actions = row.querySelector('.u-actions');
            if (!actions) return;

            var email = row.dataset.email;
            if (!email) return;

            var btn = document.createElement('button');
            btn.type = 'button';
            btn.className = 'u-btn dvl-btn-row';
            btn.title = 'Xem thiết bị của user';
            btn.innerHTML = '<i class="fas fa-mobile-screen-button"></i>';

            btn.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                openAdminDeviceView(email);
            });

            var deleteBtn = actions.querySelector('.u-btn.danger');
            if (deleteBtn) actions.insertBefore(btn, deleteBtn);
            else actions.appendChild(btn);
        });
    }

    async function openAdminDeviceView(email) {
        if (!__dvlHasAdminRights()) {
            alert('Chỉ admin mới có quyền này.');
            return;
        }

        var modal = $('dvlModal');
        if (!modal) return;

        $('dvlTitle').textContent = 'Thiết bị của user';
        $('dvlSubtitle').innerHTML = 'Danh sách thiết bị đăng nhập của user: <b>' + esc(email) + '</b>.';
        $('dvlCountBox').style.display = 'flex';
        $('dvlWarning').style.display = 'none';
        $('dvlLogoutOthersBtn').style.display = 'none';

        modal.classList.add('show');

        var list = $('dvlList');
        list.innerHTML = '<div style="text-align:center;padding:2rem;color:var(--text-3)"><i class="fas fa-spinner fa-pulse"></i> Đang tải...</div>';

        var devices = await loadDevices(email);
        updateModalUI(email, devices);
        renderDeviceList(list, devices, email, false);
    }

    /* ═══════════════════════════════════════════════════════════
       Màn hình tab mới sau khi confirm link
       ═══════════════════════════════════════════════════════════ */
    function renderVerifySuccessPage() {
        document.body.innerHTML =
            '<div style="position:fixed;inset:0;display:flex;align-items:center;' +
            'justify-content:center;background:#f8fafc;font-family:sans-serif;padding:2rem;z-index:99999">' +
                '<div style="text-align:center;max-width:400px">' +
                    '<div style="width:80px;height:80px;border-radius:50%;' +
                    'background:linear-gradient(135deg,#16a34a,#22c55e);color:#fff;' +
                    'display:flex;align-items:center;justify-content:center;' +
                    'font-size:2rem;margin:0 auto 1.5rem;box-shadow:0 8px 24px rgba(22,163,74,.4)">' +
                        '<i class="fas fa-check"></i>' +
                    '</div>' +
                    '<h1 style="font-size:1.5rem;color:#0f172a;margin-bottom:.75rem;font-weight:800">' +
                        'Đã xác nhận thiết bị' +
                    '</h1>' +
                    '<p style="color:#64748b;line-height:1.6;margin-bottom:1.5rem">' +
                        'Thiết bị đang chờ đăng nhập đã được xác nhận thành công. ' +
                        'Vui lòng <b>quay lại tab cũ</b> để tiếp tục sử dụng.' +
                    '</p>' +
                    '<button onclick="window.close()" style="' +
                    'padding:.75rem 1.5rem;border-radius:10px;border:none;' +
                    'background:#4f46e5;color:#fff;font-size:.95rem;font-weight:700;' +
                    'cursor:pointer;font-family:inherit">' +
                        'Đóng tab này' +
                    '</button>' +
                '</div>' +
            '</div>';
    }

    function renderVerifyErrorPage(reason) {
        var msg = 'Link xác nhận không hợp lệ hoặc đã được sử dụng.';
        if (reason === 'expired') msg = 'Link xác nhận đã hết hạn. Vui lòng quay lại tab cũ và bấm "Gửi lại email".';

        document.body.innerHTML =
            '<div style="position:fixed;inset:0;display:flex;align-items:center;' +
            'justify-content:center;background:#f8fafc;font-family:sans-serif;padding:2rem;z-index:99999">' +
                '<div style="text-align:center;max-width:400px">' +
                    '<div style="width:80px;height:80px;border-radius:50%;' +
                    'background:linear-gradient(135deg,#dc2626,#b91c1c);color:#fff;' +
                    'display:flex;align-items:center;justify-content:center;' +
                    'font-size:2rem;margin:0 auto 1.5rem;box-shadow:0 8px 24px rgba(220,38,38,.4)">' +
                        '<i class="fas fa-times"></i>' +
                    '</div>' +
                    '<h1 style="font-size:1.5rem;color:#0f172a;margin-bottom:.75rem;font-weight:800">' +
                        'Không thể xác nhận' +
                    '</h1>' +
                    '<p style="color:#64748b;line-height:1.6;margin-bottom:1.5rem">' +
                        esc(msg) +
                    '</p>' +
                    '<button onclick="window.close()" style="' +
                    'padding:.75rem 1.5rem;border-radius:10px;border:none;' +
                    'background:#64748b;color:#fff;font-size:.95rem;font-weight:700;' +
                    'cursor:pointer;font-family:inherit">' +
                        'Đóng tab này' +
                    '</button>' +
                '</div>' +
            '</div>';
    }

    /* ═══════════════════════════════════════════════════════════
       Init
       ═══════════════════════════════════════════════════════════ */
    function initDvl() {
        var closeBtn = $('dvlCloseBtn');
        if (closeBtn && !closeBtn.__dvlBound) {
            closeBtn.__dvlBound = true;
            closeBtn.addEventListener('click', closeManageModal);
        }
        var doneBtn = $('dvlDoneBtn');
        if (doneBtn && !doneBtn.__dvlBound) {
            doneBtn.__dvlBound = true;
            doneBtn.addEventListener('click', closeManageModal);
        }
        var modal = $('dvlModal');
        if (modal && !modal.__dvlBound) {
            modal.__dvlBound = true;
            modal.addEventListener('click', function(e) {
                if (e.target === modal) closeManageModal();
            });
        }

        var logoutOthers = $('dvlLogoutOthersBtn');
        if (logoutOthers && !logoutOthers.__dvlBound) {
            logoutOthers.__dvlBound = true;
            logoutOthers.addEventListener('click', logoutOtherDevices);
        }

        document.addEventListener('keydown', function(e) {
            if (e.key !== 'Escape') return;
            var m1 = $('dvlModal');
            if (m1 && m1.classList.contains('show')) { closeManageModal(); return; }
            var m2 = $('dvlVerifyModal');
            if (m2 && m2.classList.contains('show')) {
                stopTimer();
                if (_verifyPoller) { clearInterval(_verifyPoller); _verifyPoller = null; }
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
                    setTimeout(function() { updateDropdownBadge(); }, 1500);
                    setTimeout(function() {
                        if (__dvlHasAdminRights()) {
                            updatePendingBadge();
                        }
                    }, 2000);
                }
            });
        }

        var userList = document.getElementById('userList');
        if (userList && !userList.__dvlObserved) {
            userList.__dvlObserved = true;
            var mo = new MutationObserver(function() {
                try { injectAdminDeviceButton(); } catch(e) {}
            });
            mo.observe(userList, { childList: true, subtree: true });
        }

        setInterval(function() {
            if (typeof currentUser !== 'undefined' && currentUser && currentUser.email) {
                checkIfKicked(currentUser.email);
            }
        }, 30000);

        setInterval(function() {
            if (__dvlHasAdminRights()) {
                updatePendingBadge();
            }
        }, 30000);

        setTimeout(async function() {
            var res = await checkVerifyLink();
            if (!res) return;

            if (res.verified) {
                renderVerifySuccessPage();
            } else if (res.reason === 'expired' || res.reason === 'not_found') {
                renderVerifyErrorPage(res.reason);
            }
        }, 500);
    }

    /* ═══════════════════════════════════════════════════════════
       Public API
       ═══════════════════════════════════════════════════════════ */
    window.__dvlCheckAndRegister = registerCurrentDevice;
    window.__dvlSendVerifyEmail = sendVerifyEmail;
    window.__dvlShowVerifyModal = showVerifyModal;
    window.__dvlOpenManage = openManageModal;
    window.__dvlOpenAdmin = openAdminDeviceView;
    window.__dvlOpenPending = openPendingList;
    window.__dvlMaxDevices = MAX_DEVICES;
    window.__dvlIsSuperAdmin = __dvlIsSuperAdmin;
    window.__dvlHasAdminRights = __dvlHasAdminRights;

    window.__dvlDebug = {
        openManage: openManageModal,
        openAdmin: openAdminDeviceView,
        openPending: openPendingList,
        getDeviceId: getDeviceId,
        getDeviceName: getDeviceName,
        isSuperAdmin: __dvlIsSuperAdmin,
        hasAdminRights: __dvlHasAdminRights,
        resetDeviceId: function() {
            try { localStorage.removeItem(DEVICE_ID_KEY); } catch(e) {}
            currentDeviceId = null;
        },
        loadDevices: loadDevices,
        register: registerCurrentDevice,
        checkKicked: checkIfKicked,
        checkVerify: checkVerification,
        testSendMail: async function(email, token) {
            var res = await sendVerifyEmail(email || 'test@gmail.com', token || 'TESTTOKEN');
            console.log('Test send mail result:', res);
            return res;
        }
    };

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initDvl);
    } else {
        initDvl();
    }

    console.log('[Device Limiter] Module loaded — super admin vẫn duyệt được, max ' + MAX_DEVICES);
})()
"""


if __name__ == "__main__":
    css = build_device_css()
    html = build_device_html()
    js = build_device_js()

    print("CSS:  %d ky tu" % len(css))
    print("HTML: %d ky tu" % len(html))
    print("JS:   %d ky tu" % len(js))

    assert 'dvlVerifyModal' in html
    assert 'dvlVerifySuccessModal' in html
    assert 'dvlEmailErrorBox' in html
    assert 'dvlStepEmail' in html
    assert 'dvlStepAdmin' in html
    assert '__dvlHasAdminRights' in js
    assert 'registerCurrentDevice' in js
    assert 'sendVerifyEmail' in js
    assert 'checkVerifyLink' in js
    assert 'openPendingList' in js
    assert 'updatePendingBadge' in js
    assert 'injectAdminPendingButton' in js
    assert 'MAX_DEVICES = 2' in js
    assert '__dvlIsSuperAdmin' in js
    assert 'renderVerifySuccessPage' in js

    print("✅ Module san sang dung")

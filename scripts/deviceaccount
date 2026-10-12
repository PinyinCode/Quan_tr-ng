# -*- coding: utf-8 -*-
"""Theo dõi 1 thiết bị (fingerprint) đăng nhập nhiều tài khoản — chỉ cảnh báo admin."""


def build_dam_css():
    return r"""
.dam-modal{position:fixed;inset:0;background:rgba(15,23,42,.85);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);z-index:4400;display:none;align-items:center;justify-content:center;padding:1.25rem;overflow-y:auto;animation:damFadeIn .2s ease}
.dam-modal.show{display:flex}
@keyframes damFadeIn{from{opacity:0}to{opacity:1}}
.dam-box{background:var(--surface);border-radius:20px;padding:1.75rem 1.5rem;max-width:540px;width:100%;max-height:calc(100vh - 2.5rem);overflow-y:auto;box-shadow:0 24px 70px rgba(0,0,0,.35);text-align:left;position:relative;animation:damSlideUp .32s cubic-bezier(.34,1.56,.64,1);color:var(--text)}
@keyframes damSlideUp{from{transform:translateY(30px) scale(.95);opacity:0}to{transform:translateY(0) scale(1);opacity:1}}
.dam-icon{width:56px;height:56px;border-radius:16px;background:linear-gradient(135deg,#f59e0b,#d97706);color:#fff;font-size:1.5rem;display:flex;align-items:center;justify-content:center;margin-bottom:1rem;box-shadow:0 8px 20px rgba(245,158,11,.35)}
.dam-icon.danger{background:linear-gradient(135deg,#dc2626,#b91c1c);box-shadow:0 8px 20px rgba(220,38,38,.35)}
.dam-title{font-size:1.2rem;font-weight:800;margin-bottom:.4rem;color:var(--text)}
.dam-subtitle{font-size:.85rem;color:var(--text-2);margin-bottom:1.25rem;line-height:1.55}
.dam-info-box{padding:.85rem 1rem;background:linear-gradient(135deg,rgba(245,158,11,.08),rgba(251,191,36,.05));border:1.5px solid rgba(245,158,11,.35);border-radius:12px;font-size:.82rem;color:#92400e;line-height:1.55;margin-bottom:1.25rem}
[data-theme="dark"] .dam-info-box{background:linear-gradient(135deg,rgba(245,158,11,.15),rgba(251,191,36,.08));color:#fcd34d}
.dam-info-box b{color:#dc2626}
[data-theme="dark"] .dam-info-box b{color:#fca5a5}
.dam-btn{display:flex;align-items:center;justify-content:center;gap:.5rem;width:100%;padding:.75rem 1.15rem;border-radius:12px;border:none;background:linear-gradient(135deg,#4f46e5,#7c3aed);color:#fff;font-size:.88rem;font-weight:800;font-family:inherit;cursor:pointer;transition:.2s;box-shadow:0 4px 14px rgba(124,58,237,.35);margin-top:.5rem}
.dam-btn:hover{transform:translateY(-2px);box-shadow:0 8px 22px rgba(124,58,237,.5)}
.dam-btn.secondary{background:var(--surface-2);color:var(--text-2);border:1.5px solid var(--border);box-shadow:none}
.dam-btn.secondary:hover{background:var(--surface);border-color:var(--primary);color:var(--primary)}
.dam-list{display:flex;flex-direction:column;gap:.6rem;max-height:400px;overflow-y:auto;padding:.25rem}
.dam-item{padding:.85rem 1rem;background:var(--surface-2);border:1.5px solid var(--border);border-radius:12px;transition:.15s}
.dam-item:hover{border-color:var(--primary)}
.dam-item.warn{border-color:rgba(245,158,11,.4);background:linear-gradient(135deg,rgba(245,158,11,.05),rgba(251,191,36,.02))}
.dam-item.blocked{border-color:rgba(220,38,38,.4);background:linear-gradient(135deg,rgba(220,38,38,.06),rgba(185,28,28,.03))}
.dam-item.whitelisted{border-color:rgba(22,163,74,.4);background:linear-gradient(135deg,rgba(22,163,74,.05),rgba(34,197,94,.02))}
.dam-item-head{display:flex;justify-content:space-between;align-items:flex-start;gap:.5rem;margin-bottom:.5rem;flex-wrap:wrap}
.dam-item-device{font-weight:800;font-size:.88rem;color:var(--text);display:flex;align-items:center;gap:.4rem}
.dam-item-device i{color:#0891b2;font-size:1rem}
.dam-item-fp{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.7rem;color:var(--text-3);word-break:break-all;margin-top:.15rem}
.dam-item-browsers{display:flex;flex-wrap:wrap;gap:.25rem;margin-top:.35rem}
.dam-browser-tag{display:inline-flex;align-items:center;gap:.25rem;padding:.15rem .45rem;border-radius:6px;background:var(--surface);border:1px solid var(--border);font-size:.68rem;font-weight:600;color:var(--text-2)}
.dam-item-accounts{display:flex;flex-direction:column;gap:.3rem;margin:.5rem 0}
.dam-acc-row{display:flex;justify-content:space-between;gap:.5rem;font-size:.78rem;color:var(--text-2);padding:.3rem .55rem;border-radius:6px;background:var(--surface)}
.dam-acc-email{font-weight:600;word-break:break-all}
.dam-acc-time{color:var(--text-3);font-size:.7rem;white-space:nowrap}
.dam-item-actions{display:flex;gap:.35rem;margin-top:.5rem;padding-top:.5rem;border-top:1px solid var(--border);flex-wrap:wrap}
.dam-action-btn{padding:.4rem .7rem;border-radius:8px;border:1.5px solid var(--border);background:var(--surface);color:var(--text-2);font-size:.72rem;font-weight:700;cursor:pointer;font-family:inherit;display:inline-flex;align-items:center;gap:.3rem;transition:.15s}
.dam-action-btn:hover{background:var(--surface-2);border-color:var(--primary);color:var(--primary)}
.dam-action-btn.danger{border-color:rgba(220,38,38,.35);color:var(--danger)}
.dam-action-btn.danger:hover{background:var(--danger);color:#fff;border-color:var(--danger)}
.dam-action-btn.ok{border-color:rgba(22,163,74,.35);color:#16a34a}
.dam-action-btn.ok:hover{background:#16a34a;color:#fff;border-color:#16a34a}
.dam-badge{display:inline-flex;align-items:center;gap:.25rem;padding:.15rem .5rem;border-radius:50px;font-size:.65rem;font-weight:800;text-transform:uppercase;letter-spacing:.3px}
.dam-badge.warn{background:rgba(245,158,11,.15);color:#d97706}
.dam-badge.blocked{background:rgba(220,38,38,.15);color:var(--danger)}
.dam-badge.ok{background:rgba(22,163,74,.15);color:#16a34a}
.dam-badge.new{background:linear-gradient(135deg,#f59e0b,#d97706);color:#fff;animation:damPulse 1.5s ease-in-out infinite}
@keyframes damPulse{0%,100%{transform:scale(1)}50%{transform:scale(1.08)}}
.dam-empty{text-align:center;padding:2rem 1rem;color:var(--text-3);font-size:.85rem}
.dam-empty i{font-size:2rem;opacity:.4;margin-bottom:.5rem;display:block}
.dam-tabs{display:flex;gap:.4rem;margin-bottom:1rem;flex-wrap:wrap;padding:.3rem;background:var(--surface-2);border-radius:12px}
.dam-tab{flex:1;padding:.55rem .85rem;border:none;border-radius:9px;background:transparent;color:var(--text-2);font-size:.78rem;font-weight:700;font-family:inherit;cursor:pointer;transition:.2s;display:inline-flex;align-items:center;justify-content:center;gap:.35rem;min-width:0}
.dam-tab:hover{color:var(--primary)}
.dam-tab.active{background:var(--surface);color:var(--primary);box-shadow:0 2px 8px rgba(15,23,42,.08)}
.dam-tab .count{padding:.1rem .4rem;border-radius:50px;background:var(--border);font-size:.65rem;font-weight:800;min-width:20px;text-align:center}
.dam-tab.active .count{background:var(--primary);color:#fff}
.dam-spinner{display:inline-block;width:14px;height:14px;border:2px solid rgba(255,255,255,.35);border-top-color:#fff;border-radius:50%;animation:damSpin .7s linear infinite}
@keyframes damSpin{to{transform:rotate(360deg)}}
.dam-edit-close{position:absolute;top:12px;right:12px;width:34px;height:34px;border-radius:50%;border:none;background:var(--surface-2);color:var(--text-2);cursor:pointer;font-size:1rem;display:flex;align-items:center;justify-content:center;transition:.15s}
.dam-edit-close:hover{background:var(--danger-light);color:var(--danger)}
@media (max-width:500px){
.dam-box{padding:1.4rem 1.15rem;border-radius:16px}
.dam-icon{width:48px;height:48px;font-size:1.25rem}
.dam-title{font-size:1.05rem}
.dam-item{padding:.7rem .8rem}
.dam-item-actions{flex-direction:column}
.dam-action-btn{width:100%;justify-content:center}
.dam-tab{font-size:.7rem;padding:.5rem .5rem}
.dam-tab span:not(.count){display:none}
.dam-tab i{font-size:1rem}
}
"""


def build_dam_html():
    return r"""
<div class="dam-modal" id="damCooldownModal">
    <div class="dam-box">
        <div class="dam-icon"><i class="fas fa-hourglass-half"></i></div>
        <div class="dam-title">Vui lòng chờ 60 phút</div>
        <div class="dam-subtitle">
            Thiết bị này vừa đăng nhập <b id="damCooldownCount">0</b> tài khoản khác nhau trong vòng 60 phút qua.
        </div>

        <div class="dam-info-box">
            <i class="fas fa-shield-halved"></i>
            Để bảo vệ tài khoản, hệ thống <b>tạm chặn đăng nhập</b> trên thiết bị này trong:
            <br><br>
            <b id="damCooldownTime" style="font-size:1.3em">60:00</b>
            <br><br>
            Nếu bạn là người dùng hợp lệ (dùng chung máy với người khác), hãy liên hệ admin để được <b>whitelist</b>.
        </div>

        <button type="button" class="dam-btn secondary" id="damCooldownCloseBtn">
            <i class="fas fa-times"></i> Đóng
        </button>
    </div>
</div>

<div class="dam-modal" id="damBlockedModal">
    <div class="dam-box">
        <div class="dam-icon danger"><i class="fas fa-ban"></i></div>
        <div class="dam-title">Thiết bị đã bị chặn</div>
        <div class="dam-subtitle">
            Admin đã chặn thiết bị này khỏi hệ thống do phát hiện đăng nhập nhiều tài khoản.
        </div>
        <div class="dam-info-box">
            <i class="fas fa-info-circle"></i>
            Nếu bạn cho rằng đây là nhầm lẫn, vui lòng liên hệ admin kèm mã thiết bị:
            <br><br>
            <b id="damBlockedFp">—</b>
        </div>
        <button type="button" class="dam-btn secondary" id="damBlockedCloseBtn">
            <i class="fas fa-sign-out-alt"></i> Đăng xuất
        </button>
    </div>
</div>

<div class="dam-modal" id="damAdminModal">
    <div class="dam-box">
        <button class="dam-edit-close" id="damAdminCloseBtn"><i class="fas fa-times"></i></button>
        <div class="dam-icon"><i class="fas fa-user-secret"></i></div>
        <div class="dam-title">Quản lý thiết bị nghi vấn</div>
        <div class="dam-subtitle">
            Theo dõi thiết bị (theo vân tay fingerprint) đăng nhập nhiều tài khoản — kể cả khi đổi trình duyệt.
        </div>
        <div class="dam-tabs">
            <button type="button" class="dam-tab active" data-dam-tab="warn">
                <i class="fas fa-triangle-exclamation"></i>
                <span>Cảnh báo</span>
                <span class="count" id="damWarnCount">0</span>
            </button>
            <button type="button" class="dam-tab" data-dam-tab="blocked">
                <i class="fas fa-ban"></i>
                <span>Đã block</span>
                <span class="count" id="damBlockedCount">0</span>
            </button>
            <button type="button" class="dam-tab" data-dam-tab="whitelist">
                <i class="fas fa-check-circle"></i>
                <span>Whitelist</span>
                <span class="count" id="damWhitelistCount">0</span>
            </button>
        </div>
        <div class="dam-list" id="damList">
            <div class="dam-empty"><i class="fas fa-spinner fa-pulse"></i>Đang tải...</div>
        </div>
    </div>
</div>
"""


def build_dam_js():
    return r"""
(function() {
    'use strict';

    var MAX_ACCOUNTS_PER_DEVICE = 3;
    var COOLDOWN_MINUTES = 60;
    var COOLDOWN_MS = COOLDOWN_MINUTES * 60 * 1000;
    var FP_CACHE_KEY = 'dam_fingerprint_cache';

    var currentTab = 'warn';
    var allDevices = [];
    var warnDevices = [];
    var blockedDevices = [];
    var whitelistDevices = [];
    var _cooldownInterval = null;
    var _cooldownStartTime = 0;
    var _fpPromise = null;

    function $(id) { return document.getElementById(id); }
    function esc(s) {
        if (s == null) return '';
        return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;')
            .replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');
    }
    function timeAgo(ms) {
        if (!ms) return 'Vừa xong';
        var s = Math.floor((Date.now() - ms) / 1000);
        if (s < 60) return 'Vừa xong';
        if (s < 3600) return Math.floor(s / 60) + ' phút trước';
        if (s < 86400) return Math.floor(s / 3600) + ' giờ trước';
        return Math.floor(s / 86400) + ' ngày trước';
    }

    function detectBrowser() {
        try {
            var ua = navigator.userAgent || '';
            if (/Edg\//.test(ua)) return 'Edge';
            if (/OPR\//.test(ua) || /Opera/.test(ua)) return 'Opera';
            if (/CocCoc/.test(ua)) return 'CocCoc';
            if (/Brave/.test(ua)) return 'Brave';
            if (/Firefox\//.test(ua)) return 'Firefox';
            if (/Chrome\//.test(ua)) return 'Chrome';
            if (/Safari\//.test(ua)) return 'Safari';
            return 'Unknown';
        } catch(e) { return 'Unknown'; }
    }

    function detectOS() {
        try {
            var ua = navigator.userAgent || '';
            if (/Windows NT 10/.test(ua)) return 'Windows 10/11';
            if (/Windows NT 6\.3/.test(ua)) return 'Windows 8.1';
            if (/Windows NT 6\.2/.test(ua)) return 'Windows 8';
            if (/Windows NT 6\.1/.test(ua)) return 'Windows 7';
            if (/Windows/.test(ua)) return 'Windows';
            if (/iPhone/.test(ua)) return 'iPhone';
            if (/iPad/.test(ua)) return 'iPad';
            if (/Android/.test(ua)) return 'Android';
            if (/Macintosh/.test(ua)) return 'MacBook';
            if (/Mac OS X/.test(ua)) return 'Mac';
            if (/Linux/.test(ua)) return 'Linux';
            return 'Unknown';
        } catch(e) { return 'Unknown'; }
    }

    function getDeviceIcon() {
        var os = detectOS();
        if (os === 'iPhone' || os === 'Android') return 'fa-mobile-screen-button';
        if (os === 'iPad') return 'fa-tablet-screen-button';
        return 'fa-desktop';
    }

    function loadCachedFp() {
        try {
            var cached = localStorage.getItem(FP_CACHE_KEY);
            if (cached && cached.length > 5) return cached;
        } catch(e) {}
        return null;
    }

    function saveCachedFp(fp) {
        try { localStorage.setItem(FP_CACHE_KEY, fp); } catch(e) {}
    }

    function getFallbackFp() {
        try {
            var data = [
                navigator.userAgent || '',
                navigator.language || '',
                screen.width + 'x' + screen.height + 'x' + screen.colorDepth,
                Intl.DateTimeFormat().resolvedOptions().timeZone || '',
                navigator.hardwareConcurrency || 0,
                navigator.platform || ''
            ].join('|');
            var hash = 0;
            for (var i = 0; i < data.length; i++) {
                hash = ((hash << 5) - hash) + data.charCodeAt(i);
                hash = hash & hash;
            }
            return 'fb_' + Math.abs(hash).toString(36);
        } catch(e) { return 'fb_unknown'; }
    }

    async function getFingerprint() {
        if (_fpPromise) return _fpPromise;

        _fpPromise = (async function() {
            var cached = loadCachedFp();
            if (cached) return cached;

            if (typeof FingerprintJS === 'undefined') {
                console.warn('[DAM] FingerprintJS chưa load, dùng fallback');
                var fb = getFallbackFp();
                saveCachedFp(fb);
                return fb;
            }

            try {
                var fp = await FingerprintJS.load();
                var result = await fp.get();
                var visitorId = result.visitorId;
                if (visitorId && visitorId.length > 5) {
                    saveCachedFp(visitorId);
                    console.log('[DAM] Fingerprint:', visitorId);
                    return visitorId;
                }
            } catch(e) {
                console.warn('[DAM] FingerprintJS error:', e);
            }

            var fb2 = getFallbackFp();
            saveCachedFp(fb2);
            return fb2;
        })();

        return _fpPromise;
    }

    async function loadDeviceDoc(fp) {
        if (!db || !fp) return null;
        try {
            var doc = await db.collection('device_logins').doc(fp).get();
            if (!doc.exists) return null;
            return doc.data();
        } catch(e) {
            console.warn('[DAM] Load device error:', e);
            return null;
        }
    }

    async function saveDeviceDoc(fp, data) {
        if (!db || !fp) return false;
        try {
            await db.collection('device_logins').doc(fp).set(data, { merge: true });
            return true;
        } catch(e) {
            console.warn('[DAM] Save device error:', e);
            return false;
        }
    }

    async function registerAccountOnDevice(email) {
        if (!email || !db) return { allowed: true };

        var fp = await getFingerprint();
        if (!fp) return { allowed: true };

        var now = Date.now();
        var docData = await loadDeviceDoc(fp) || {};
        var accounts = Array.isArray(docData.accounts) ? docData.accounts : [];
        var emailLower = email.toLowerCase();

        if (docData.blocked === true) {
            return { blocked: true, fp: fp };
        }

        if (docData.whitelisted === true) {
            var foundWl = -1;
            for (var wl = 0; wl < accounts.length; wl++) {
                if (accounts[wl].email === emailLower) { foundWl = wl; break; }
            }
            if (foundWl < 0) {
                accounts.push({ email: emailLower, firstSeen: now, lastSeen: now, browser: detectBrowser(), os: detectOS() });
            } else {
                accounts[foundWl].lastSeen = now;
            }
            await saveDeviceDoc(fp, {
                accounts: accounts,
                lastSeen: firebase.firestore.FieldValue.serverTimestamp()
            });
            return { allowed: true, whitelisted: true };
        }

        var foundIdx = -1;
        for (var i = 0; i < accounts.length; i++) {
            if (accounts[i].email === emailLower) { foundIdx = i; break; }
        }

        if (foundIdx >= 0) {
            accounts[foundIdx].lastSeen = now;
            await saveDeviceDoc(fp, {
                accounts: accounts,
                lastSeen: firebase.firestore.FieldValue.serverTimestamp()
            });
            return { allowed: true };
        }

        var recent = accounts.filter(function(a) {
            return (now - (a.lastSeen || 0)) < COOLDOWN_MS;
        });

        if (recent.length >= MAX_ACCOUNTS_PER_DEVICE) {
            var sortedRecent = recent.slice().sort(function(a, b) {
                return (b.lastSeen || 0) - (a.lastSeen || 0);
            });
            var latestMs = sortedRecent[0].lastSeen || now;
            var remainMs = Math.max(0, (latestMs + COOLDOWN_MS) - now);
            return { cooldown: true, remainMs: remainMs, fp: fp, recentCount: recent.length };
        }

        accounts.push({
            email: emailLower,
            firstSeen: now,
            lastSeen: now,
            browser: detectBrowser(),
            os: detectOS()
        });

        await saveDeviceDoc(fp, {
            fp: fp,
            os: detectOS(),
            browsers: getUniqueBrowsers(accounts),
            accounts: accounts,
            firstSeen: docData.firstSeen || now,
            lastSeen: firebase.firestore.FieldValue.serverTimestamp()
        });

        if (accounts.length > MAX_ACCOUNTS_PER_DEVICE) {
            try {
                await db.collection('device_logins').doc(fp).update({
                    warned: true,
                    warnedAt: firebase.firestore.FieldValue.serverTimestamp(),
                    warnedCount: accounts.length
                });
            } catch(e) {}

            if (typeof notifyTelegramDeviceWarning === 'function') {
                try {
                    notifyTelegramDeviceWarning({
                        fp: fp,
                        os: detectOS(),
                        browsers: getUniqueBrowsers(accounts),
                        email: emailLower,
                        totalAccounts: accounts.length,
                        accounts: accounts.slice(-5).map(function(a) { return a.email; })
                    });
                } catch(_te) {}
            }
        }

        return { allowed: true };
    }

    function getUniqueBrowsers(accounts) {
        var set = {};
        accounts.forEach(function(a) {
            if (a.browser) set[a.browser] = true;
        });
        return Object.keys(set);
    }

    window.notifyTelegramDeviceWarning = function(info) {
        try {
            var tgToken = (typeof TELEGRAM_BOT_TOKEN !== 'undefined') ? TELEGRAM_BOT_TOKEN : '';
            var tgChat = (typeof TELEGRAM_CHAT_ID !== 'undefined') ? TELEGRAM_CHAT_ID : '';

            if (!tgToken || !tgChat || tgToken.indexOf('__') === 0 || tgToken.length < 20) {
                console.warn('[DAM] Chưa cấu hình Telegram');
                return;
            }

            var browsers = (info.browsers && info.browsers.length > 0) ? info.browsers.join(', ') : 'Không rõ';

            var msg = '⚠️ <b>CẢNH BÁO THIẾT BỊ NGHI VẤN</b>\n';
            msg += '━━━━━━━━━━━━━━━━━━━━\n';
            msg += '💻 OS: <b>' + esc(info.os || 'Không rõ') + '</b>\n';
            msg += '🌐 Trình duyệt: <b>' + esc(browsers) + '</b>\n';
            msg += '🔑 FP: <code>' + esc((info.fp || '').substring(0, 16)) + '...</code>\n';
            msg += '👥 Tổng tài khoản: <b>' + (info.totalAccounts || 0) + '</b>\n';
            msg += '⏱ Vừa login với: <b>' + esc(info.email) + '</b>\n\n';
            if (info.accounts && info.accounts.length > 0) {
                msg += '<b>5 tài khoản gần nhất:</b>\n';
                info.accounts.forEach(function(acc) { msg += '• ' + esc(acc) + '\n'; });
            }
            msg += '\n👉 Vào Admin Panel → nút 🔍 để xử lý.';

            fetch('https://api.telegram.org/bot' + tgToken + '/sendMessage', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    chat_id: tgChat,
                    text: msg,
                    parse_mode: 'HTML',
                    disable_web_page_preview: true
                })
            }).catch(function() {});
        } catch(e) {
            console.warn('[DAM] Telegram notify error:', e);
        }
    };

    async function loadAllDevices() {
        if (!db) return;
        try {
            var snap = await db.collection('device_logins')
                .orderBy('lastSeen', 'desc')
                .limit(200)
                .get();

            allDevices = [];
            snap.forEach(function(doc) {
                var data = doc.data() || {};
                data._id = doc.id;
                allDevices.push(data);
            });
        } catch(e) {
            console.warn('[DAM] Load all devices error:', e);
            allDevices = [];
        }
    }

    function categorizeDevices() {
        warnDevices = [];
        blockedDevices = [];
        whitelistDevices = [];

        allDevices.forEach(function(d) {
            var accounts = Array.isArray(d.accounts) ? d.accounts : [];
            var accountCount = accounts.length;

            if (d.blocked === true) {
                blockedDevices.push(d);
            } else if (d.whitelisted === true) {
                whitelistDevices.push(d);
            } else if (accountCount > MAX_ACCOUNTS_PER_DEVICE || d.warned === true) {
                warnDevices.push(d);
            }
        });

        var wc = $('damWarnCount');
        var bc = $('damBlockedCount');
        var wlc = $('damWhitelistCount');
        if (wc) wc.textContent = warnDevices.length;
        if (bc) bc.textContent = blockedDevices.length;
        if (wlc) wlc.textContent = whitelistDevices.length;
    }

    function renderDeviceItem(d, status) {
        var accounts = Array.isArray(d.accounts) ? d.accounts : [];
        var accountCount = accounts.length;
        var icon = getDeviceIcon(d.os || '');
        var lastMs = d.lastSeen ? (d.lastSeen.toMillis ? d.lastSeen.toMillis() : d.lastSeen.seconds * 1000) : 0;

        var statusBadge = '';
        if (status === 'warn') {
            statusBadge = '<span class="dam-badge new"><i class="fas fa-exclamation-triangle"></i> CẢNH BÁO</span>';
        } else if (status === 'blocked') {
            statusBadge = '<span class="dam-badge blocked"><i class="fas fa-ban"></i> ĐÃ BLOCK</span>';
        } else {
            statusBadge = '<span class="dam-badge ok"><i class="fas fa-check-circle"></i> WHITELIST</span>';
        }

        var browsersHtml = '';
        if (Array.isArray(d.browsers) && d.browsers.length > 0) {
            browsersHtml = '<div class="dam-item-browsers">';
            d.browsers.forEach(function(b) {
                browsersHtml += '<span class="dam-browser-tag"><i class="fas fa-globe"></i> ' + esc(b) + '</span>';
            });
            browsersHtml += '</div>';
        }

        var accRows = '';
        accounts.slice(-6).forEach(function(a) {
            accRows += '<div class="dam-acc-row">' +
                '<span class="dam-acc-email">' + esc(a.email) + '</span>' +
                '<span class="dam-acc-time">' + timeAgo(a.lastSeen || 0) + '</span>' +
            '</div>';
        });
        if (accounts.length > 6) {
            accRows += '<div class="dam-acc-row" style="opacity:.6;justify-content:center">' +
                '... và ' + (accounts.length - 6) + ' tài khoản khác</div>';
        }

        var actions = '';
        if (status === 'warn') {
            actions =
                '<button class="dam-action-btn danger" onclick="damBlockDevice(\'' + esc(d._id) + '\')">' +
                    '<i class="fas fa-ban"></i> Block thiết bị</button>' +
                '<button class="dam-action-btn ok" onclick="damWhitelistDevice(\'' + esc(d._id) + '\')">' +
                    '<i class="fas fa-check"></i> Whitelist</button>' +
                '<button class="dam-action-btn" onclick="damIgnoreWarning(\'' + esc(d._id) + '\')">' +
                    '<i class="fas fa-eye-slash"></i> Bỏ qua</button>';
        } else if (status === 'blocked') {
            actions =
                '<button class="dam-action-btn ok" onclick="damUnblockDevice(\'' + esc(d._id) + '\')">' +
                    '<i class="fas fa-unlock"></i> Mở block</button>' +
                '<button class="dam-action-btn ok" onclick="damWhitelistDevice(\'' + esc(d._id) + '\')">' +
                    '<i class="fas fa-check"></i> Whitelist</button>';
        } else {
            actions =
                '<button class="dam-action-btn" onclick="damRemoveWhitelist(\'' + esc(d._id) + '\')">' +
                    '<i class="fas fa-times"></i> Bỏ whitelist</button>';
        }

        return '<div class="dam-item ' + status + '">' +
            '<div class="dam-item-head">' +
                '<div>' +
                    '<div class="dam-item-device"><i class="fas ' + icon + '"></i> ' + esc(d.os || 'Thiết bị') + '</div>' +
                    '<div class="dam-item-fp">FP: ' + esc((d._id || '').substring(0, 20)) + '...</div>' +
                '</div>' +
                statusBadge +
            '</div>' +
            browsersHtml +
            '<div style="font-size:.75rem;color:var(--text-2);margin:.35rem 0">' +
                '<b style="color:var(--text)">' + accountCount + '</b> tài khoản · Lần cuối: ' + timeAgo(lastMs) +
            '</div>' +
            '<div class="dam-item-accounts">' + accRows + '</div>' +
            '<div class="dam-item-actions">' + actions + '</div>' +
        '</div>';
    }

    function renderList() {
        var listEl = $('damList');
        if (!listEl) return;

        var items = [];
        if (currentTab === 'warn') items = warnDevices;
        else if (currentTab === 'blocked') items = blockedDevices;
        else items = whitelistDevices;

        if (!items.length) {
            var emptyMsg = '';
            if (currentTab === 'warn') emptyMsg = 'Không có thiết bị nào bị cảnh báo';
            else if (currentTab === 'blocked') emptyMsg = 'Chưa block thiết bị nào';
            else emptyMsg = 'Chưa whitelist thiết bị nào';
            listEl.innerHTML = '<div class="dam-empty"><i class="fas fa-inbox"></i>' + emptyMsg + '</div>';
            return;
        }

        var html = '';
        items.forEach(function(d) { html += renderDeviceItem(d, currentTab); });
        listEl.innerHTML = html;
    }

    window.damBlockDevice = async function(fp) {
        if (!db || !fp) return;
        if (!confirm('BLOCK thiết bị này?\n\nMọi tài khoản sẽ không thể đăng nhập trên thiết bị này nữa.')) return;
        try {
            await db.collection('device_logins').doc(fp).update({
                blocked: true,
                blockedAt: firebase.firestore.FieldValue.serverTimestamp(),
                blockedBy: (typeof currentUser !== 'undefined' && currentUser) ? currentUser.email : 'unknown'
            });
            await loadAllDevices();
            categorizeDevices();
            renderList();
            if (typeof showUserChangedToast === 'function') {
                showUserChangedToast('🚫 Đã block thiết bị', 'error');
            }
        } catch(e) { alert('Lỗi: ' + e.message); }
    };

    window.damUnblockDevice = async function(fp) {
        if (!db || !fp) return;
        if (!confirm('Mở block cho thiết bị này?')) return;
        try {
            await db.collection('device_logins').doc(fp).update({
                blocked: false,
                unblockedAt: firebase.firestore.FieldValue.serverTimestamp(),
                unblockedBy: (typeof currentUser !== 'undefined' && currentUser) ? currentUser.email : 'unknown'
            });
            await loadAllDevices();
            categorizeDevices();
            renderList();
            if (typeof showUserChangedToast === 'function') {
                showUserChangedToast('✅ Đã mở block', 'success');
            }
        } catch(e) { alert('Lỗi: ' + e.message); }
    };

    window.damWhitelistDevice = async function(fp) {
        if (!db || !fp) return;
        if (!confirm('Whitelist thiết bị này?\n\nThiết bị sẽ KHÔNG bị cảnh báo khi login nhiều tài khoản.')) return;
        try {
            await db.collection('device_logins').doc(fp).update({
                whitelisted: true,
                blocked: false,
                whitelistedAt: firebase.firestore.FieldValue.serverTimestamp(),
                whitelistedBy: (typeof currentUser !== 'undefined' && currentUser) ? currentUser.email : 'unknown'
            });
            await loadAllDevices();
            categorizeDevices();
            renderList();
            if (typeof showUserChangedToast === 'function') {
                showUserChangedToast('✅ Đã whitelist thiết bị', 'success');
            }
        } catch(e) { alert('Lỗi: ' + e.message); }
    };

    window.damRemoveWhitelist = async function(fp) {
        if (!db || !fp) return;
        if (!confirm('Bỏ whitelist thiết bị này?')) return;
        try {
            await db.collection('device_logins').doc(fp).update({
                whitelisted: false,
                removedAt: firebase.firestore.FieldValue.serverTimestamp()
            });
            await loadAllDevices();
            categorizeDevices();
            renderList();
        } catch(e) { alert('Lỗi: ' + e.message); }
    };

    window.damIgnoreWarning = async function(fp) {
        if (!db || !fp) return;
        if (!confirm('Bỏ qua cảnh báo cho thiết bị này?')) return;
        try {
            await db.collection('device_logins').doc(fp).update({
                warned: false,
                ignoredAt: firebase.firestore.FieldValue.serverTimestamp()
            });
            await loadAllDevices();
            categorizeDevices();
            renderList();
        } catch(e) { alert('Lỗi: ' + e.message); }
    };

    function bindTabs() {
        document.querySelectorAll('.dam-tab').forEach(function(tab) {
            if (tab.__damBound) return;
            tab.__damBound = true;
            tab.addEventListener('click', function() {
                currentTab = this.dataset.damTab;
                document.querySelectorAll('.dam-tab').forEach(function(t) {
                    t.classList.toggle('active', t === tab);
                });
                renderList();
            });
        });
    }

    function showCooldownModal(remainMs, recentCount) {
        var modal = $('damCooldownModal');
        if (!modal) return;
        modal.classList.add('show');

        var countEl = $('damCooldownCount');
        if (countEl) countEl.textContent = recentCount || MAX_ACCOUNTS_PER_DEVICE;

        if (_cooldownInterval) clearInterval(_cooldownInterval);
        _cooldownStartTime = Date.now();

        function updateTimer() {
            var remain = remainMs - (Date.now() - _cooldownStartTime);
            if (remain <= 0) {
                clearInterval(_cooldownInterval);
                _cooldownInterval = null;
                modal.classList.remove('show');
                return;
            }
            var m = Math.floor(remain / 60000);
            var s = Math.floor((remain % 60000) / 1000);
            var timeEl = $('damCooldownTime');
            if (timeEl) timeEl.textContent = String(m).padStart(2, '0') + ':' + String(s).padStart(2, '0');
        }

        updateTimer();
        _cooldownInterval = setInterval(updateTimer, 1000);

        var closeBtn = $('damCooldownCloseBtn');
        if (closeBtn) {
            closeBtn.onclick = function() {
                modal.classList.remove('show');
                if (typeof auth !== 'undefined' && auth) auth.signOut();
            };
        }
    }

    function showBlockedModal(fp) {
        var modal = $('damBlockedModal');
        if (!modal) return;
        modal.classList.add('show');

        var fpEl = $('damBlockedFp');
        if (fpEl) fpEl.textContent = fp || '—';

        var closeBtn = $('damBlockedCloseBtn');
        if (closeBtn) {
            closeBtn.onclick = function() {
                modal.classList.remove('show');
                if (typeof auth !== 'undefined' && auth) auth.signOut();
            };
        }
    }

    function openDamAdminModal() {
        if (typeof currentUser === 'undefined' || !currentUser || currentUser.role !== 'admin') {
            alert('Chỉ admin mới có quyền này.');
            return;
        }
        var modal = $('damAdminModal');
        if (!modal) return;
        modal.classList.add('show');

        var listEl = $('damList');
        if (listEl) {
            listEl.innerHTML = '<div class="dam-empty"><i class="fas fa-spinner fa-pulse"></i>Đang tải...</div>';
        }

        loadAllDevices().then(function() {
            categorizeDevices();
            renderList();
        });
    }

    function initDam() {
        bindTabs();

        var closeBtn = $('damAdminCloseBtn');
        if (closeBtn && !closeBtn.__damBound) {
            closeBtn.__damBound = true;
            closeBtn.addEventListener('click', function() {
                $('damAdminModal').classList.remove('show');
            });
        }
        var modal = $('damAdminModal');
        if (modal && !modal.__damBound) {
            modal.__damBound = true;
            modal.addEventListener('click', function(e) {
                if (e.target === modal) modal.classList.remove('show');
            });
        }

        document.addEventListener('keydown', function(e) {
            if (e.key !== 'Escape') return;
            var m = $('damAdminModal');
            if (m && m.classList.contains('show')) m.classList.remove('show');
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initDam);
    } else {
        initDam();
    }

    window.__damRegisterAccount = registerAccountOnDevice;
    window.__damShowCooldown = showCooldownModal;
    window.__damShowBlocked = showBlockedModal;
    window.__damOpenAdmin = openDamAdminModal;
    window.openDamAdminModal = openDamAdminModal;
    window.openAdminDeviceView = function(email) {
        openDamAdminModal();
    };
    window.__damDebug = {
        register: registerAccountOnDevice,
        load: loadAllDevices,
        categorize: categorizeDevices,
        openAdmin: openDamAdminModal,
        getFingerprint: getFingerprint,
        resetFp: function() {
            try { localStorage.removeItem(FP_CACHE_KEY); } catch(e) {}
            _fpPromise = null;
        },
        maxAccounts: MAX_ACCOUNTS_PER_DEVICE,
        cooldownMin: COOLDOWN_MINUTES
    };

    console.log('[DAM] Module loaded OK — max ' + MAX_ACCOUNTS_PER_DEVICE + ' accounts/device (fingerprint), cooldown ' + COOLDOWN_MINUTES + 'min');
})();
"""


if __name__ == "__main__":
    css = build_dam_css()
    html = build_dam_html()
    js = build_dam_js()

    print("CSS:  %d ky tu" % len(css))
    print("HTML: %d ky tu" % len(html))
    print("JS:   %d ky tu" % len(js))

    assert 'damCooldownModal' in html
    assert 'damBlockedModal' in html
    assert 'damAdminModal' in html
    assert 'registerAccountOnDevice' in js
    assert 'MAX_ACCOUNTS_PER_DEVICE = 3' in js
    assert 'COOLDOWN_MINUTES = 60' in js
    assert 'FingerprintJS' in js

    print("Module san sang dung")

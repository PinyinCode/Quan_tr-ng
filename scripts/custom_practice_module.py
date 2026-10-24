# -*- coding: utf-8 -*-
r"""
custom_practice_module.py - Tích hợp Modal Popup cảnh báo lỗi chính tả trực quan
"""

def build_custom_practice_css():
    return r"""
/* ═══════════════════════════════════════════════════════════ */
/* KHU VỰC LUYỆN TẬP TỰ DO - MODERN GLASSMORPHIC UI           */
/* ═══════════════════════════════════════════════════════════ */
.cp-card {
    background: linear-gradient(145deg, var(--surface, #ffffff), var(--surface-2, #f8fafc));
    border: 1px solid rgba(124, 58, 237, 0.15);
    border-radius: 24px;
    padding: 1.75rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 16px 40px -12px rgba(124, 58, 237, 0.12), 0 0 0 1px rgba(255, 255, 255, 0.8) inset;
    display: flex;
    flex-direction: column;
    gap: 1.25rem;
    position: relative;
    overflow: hidden;
}
.cp-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 5px;
    background: linear-gradient(90deg, #4f46e5, #7c3aed, #ec4899);
}
.cp-header-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
}
.cp-section-header {
    display: flex;
    align-items: center;
    gap: 12px;
}
.cp-icon-badge {
    color: #fff;
    font-size: 1rem;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 40px;
    border-radius: 14px;
    background: linear-gradient(135deg, #6366f1, #a855f7);
    box-shadow: 0 6px 16px rgba(168, 85, 247, 0.35);
}
.cp-title-group h3 {
    font-size: 1.15rem;
    font-weight: 800;
    color: var(--text, #1e1b4b);
    margin: 0;
}
.cp-title-group p {
    font-size: 0.8rem;
    color: var(--text-3, #64748b);
    margin: 2px 0 0 0;
}

.cp-token-badge {
    display: flex; align-items: center; gap: 6px;
    background: rgba(16, 185, 129, 0.1); color: #059669;
    padding: 4px 12px; border-radius: 50px;
    font-size: 0.75rem; font-weight: 800;
    border: 1px solid rgba(16, 185, 129, 0.2);
    transition: all 0.3s;
    cursor: pointer;
}
.cp-token-badge.warn { background: rgba(245, 158, 11, 0.1); color: #d97706; border-color: rgba(245, 158, 11, 0.2); }
.cp-token-badge.danger { background: rgba(220, 38, 38, 0.1); color: #dc2626; border-color: rgba(220, 38, 38, 0.2); }

.cp-btn-reset {
    padding: 0.45rem 0.9rem;
    border-radius: 50px;
    border: 1px solid var(--border, #e2e8f0);
    background: var(--surface, #ffffff);
    color: var(--text-3, #64748b);
    font-size: 0.75rem;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.2s;
}
.cp-btn-reset:hover { background: #fee2e2; color: #ef4444; border-color: #fca5a5; }

.cp-switch-container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: var(--surface-2, #f1f5f9);
    padding: 6px;
    border-radius: 16px;
    border: 1px solid var(--border, #e2e8f0);
    cursor: pointer;
    user-select: none;
    width: 100%;
    max-width: 320px;
    margin: 0 auto;
}
.cp-switch-label {
    flex: 1;
    text-align: center;
    padding: 8px;
    font-weight: 700;
    font-size: 0.85rem;
    color: var(--text-3, #64748b);
    border-radius: 12px;
    transition: all 0.3s ease;
}
.cp-switch-label.active {
    background: var(--surface, #ffffff);
    color: #7c3aed;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
.cp-switch-icon-box {
    width: 36px;
    height: 36px;
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    color: #fff;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 6px;
    transition: transform 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}
.cp-switch-container:hover .cp-switch-icon-box {
    transform: rotate(180deg);
}

.cp-textarea {
    width: 100%;
    padding: 1.25rem;
    border-radius: 16px;
    border: 1.5px solid var(--border, #e2e8f0);
    background: var(--surface, #ffffff);
    color: var(--text, #1e1b4b);
    font-family: var(--font-zh, inherit);
    font-size: 1.05rem;
    resize: none;
    min-height: 120px;
    max-height: 400px;
    line-height: 1.6;
    transition: all 0.25s ease;
}
.cp-textarea:focus {
    border-color: #a855f7;
    outline: none;
    box-shadow: 0 0 0 4px rgba(168, 85, 247, 0.15);
}

.cp-spell-container {
    display: none;
    flex-direction: column;
    gap: 0.5rem;
    background: rgba(245, 158, 11, 0.08);
    border: 1px solid rgba(245, 158, 11, 0.3);
    padding: 0.75rem 1rem;
    border-radius: 12px;
    font-size: 0.85rem;
    color: #92400e;
    margin-top: 6px;
    animation: fadeIn 0.3s ease;
}
.cp-spell-container.show { display: flex; }
.cp-spell-header {
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 6px;
}
.cp-spell-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
}
.cp-spell-chip {
    background: #ffffff;
    border: 1px solid #f59e0b;
    color: #b45309;
    padding: 4px 10px;
    border-radius: 8px;
    font-size: 0.8rem;
    font-weight: 600;
    box-shadow: 0 2px 4px rgba(0,0,0,0.02);
}

.cp-modal-overlay {
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(4px);
    display: none;
    align-items: center;
    justify-content: center;
    z-index: 9999;
    animation: fadeIn 0.2s ease;
}
.cp-modal-overlay.show { display: flex; }
.cp-modal-box {
    background: var(--surface, #ffffff);
    border: 1px solid rgba(245, 158, 11, 0.4);
    border-radius: 20px;
    padding: 1.5rem;
    width: 90%;
    max-width: 400px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    display: flex;
    flex-direction: column;
    gap: 1rem;
    text-align: center;
}
.cp-modal-icon {
    font-size: 2.5rem;
    color: #f59e0b;
}
.cp-modal-title {
    font-size: 1.1rem;
    font-weight: 800;
    color: var(--text, #1e1b4b);
    margin: 0;
}
.cp-modal-desc {
    font-size: 0.85rem;
    color: var(--text-3, #64748b);
    line-height: 1.5;
    margin: 0;
}
.cp-modal-words {
    background: rgba(245, 158, 11, 0.1);
    color: #d97706;
    padding: 8px;
    border-radius: 8px;
    font-weight: 700;
    font-size: 0.95rem;
    word-break: break-all;
}
.cp-modal-actions {
    display: flex;
    gap: 10px;
    margin-top: 5px;
}
.cp-modal-btn {
    flex: 1;
    padding: 10px;
    border-radius: 12px;
    font-weight: 700;
    font-size: 0.9rem;
    cursor: pointer;
    border: none;
    transition: all 0.2s;
}
.cp-modal-btn-cancel {
    background: var(--surface-2, #f1f5f9);
    color: var(--text-3, #64748b);
}
.cp-modal-btn-cancel:hover { background: #e2e8f0; }
.cp-modal-btn-proceed {
    background: linear-gradient(135deg, #f59e0b, #d97706);
    color: #fff;
    box-shadow: 0 4px 12px rgba(245, 158, 11, 0.3);
}
.cp-modal-btn-proceed:hover { opacity: 0.9; }

.cp-btn-start {
    width: 100%;
    height: 52px;
    border-radius: 16px;
    border: none;
    background: linear-gradient(135deg, #4f46e5, #7c3aed, #ec4899);
    color: #fff;
    font-weight: 800;
    font-size: 1.05rem;
    cursor: pointer;
    transition: all 0.3s;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.6rem;
}
.cp-btn-start:hover:not(:disabled) {
    transform: translateY(-2px);
    box-shadow: 0 12px 30px rgba(124, 58, 237, 0.5);
}
.cp-btn-start:disabled {
    background: #cbd5e1;
    cursor: not-allowed;
    transform: none;
    box-shadow: none;
}

.cp-btn-buy-token {
    width: 100%;
    height: 52px;
    border-radius: 16px;
    border: 2px dashed #f59e0b;
    background: rgba(245, 158, 11, 0.1);
    color: #d97706;
    font-weight: 800;
    font-size: 1rem;
    cursor: pointer;
    display: none;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    transition: all 0.2s;
}
.cp-btn-buy-token:hover { background: rgba(245, 158, 11, 0.2); }

.cp-progress-wrap {
    display: none;
    flex-direction: column;
    gap: 0.6rem;
    background: var(--surface-2, #f1f5f9);
    padding: 1rem;
    border-radius: 14px;
    border: 1px solid var(--border, #e2e8f0);
}
.cp-progress-wrap.show { display: flex; animation: fadeIn 0.3s ease; }
.cp-progress-bar-bg {
    width: 100%;
    height: 10px;
    background: var(--surface, #ffffff);
    border-radius: 50px;
    overflow: hidden;
}
.cp-progress-bar {
    height: 100%;
    width: 0%;
    background: linear-gradient(90deg, #6366f1, #a855f7, #ec4899);
    transition: width 0.3s ease;
}
@keyframes fadeIn { from { opacity: 0; transform: translateY(5px); } to { opacity: 1; transform: translateY(0); } }

.cp-history-item {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 12px;
    display: flex;
    flex-direction: column;
    gap: 6px;
    transition: all 0.2s;
}
.cp-history-item:hover { border-color: #a855f7; box-shadow: 0 4px 12px rgba(168,85,247,0.1); }
.cp-history-vi { font-size: 0.9rem; color: #1e293b; font-weight: 600; }
.cp-history-zh { font-size: 1.05rem; color: #7c3aed; font-weight: 700; }
.cp-history-pinyin { font-size: 0.8rem; color: #64748b; font-style: italic; }
.cp-history-time { font-size: 0.7rem; color: #94a3b8; text-align: right; margin-top: 4px; }

@media (min-width: 768px) {
    .cp-btn-start, .cp-btn-buy-token { width: auto; min-width: 280px; align-self: flex-end; }
}

.cp-token-badge.cooldown {
    background: rgba(100, 116, 139, 0.15) !important;
    color: #64748b !important;
    border-color: rgba(100, 116, 139, 0.3) !important;
    cursor: not-allowed !important;
}
.cp-token-badge.cooldown:hover {
    transform: none;
    box-shadow: none;
}
.cp-token-badge.cooldown .refresh-hint {
    display: none;
}
.cp-hidden {
    display: none !important;
}
"""

def build_custom_practice_html():
    return r"""
<div class="cp-card" id="cpSection">
    <div class="cp-header-row">
        <div class="cp-section-header">
            <div class="cp-icon-badge" style="background: linear-gradient(135deg, #3b82f6, #8b5cf6); box-shadow: 0 6px 16px rgba(59, 130, 246, 0.4);">
                <i class="fas fa-robot"></i>
            </div>
            <div class="cp-title-group">
                <h3>Trợ Lý Dịch Thuật</h3>
                <p>Dịch và tạo bài tập cá nhân hóa</p>
            </div>
        </div>
        <div style="display:flex; gap:8px; align-items:center;">
            <div class="cp-token-badge" id="cpTokenBadge" title="Bấm để cập nhật số Token mới nhất">
              <i class="fas fa-bolt"></i> <span id="cpTokenText">Đang tải...</span>
              <span class="refresh-hint">🔄</span>
            </div>
            <button class="cp-btn-reset" id="cpHistoryBtn" type="button" title="Xem lịch sử">
                <i class="fas fa-clock-rotate-left"></i>
            </button>
            <button class="cp-btn-reset" id="cpResetBtn" type="button" title="Làm mới">
                <i class="fas fa-rotate-right"></i>
            </button>
        </div>
    </div>

    <div class="cp-switch-container" id="cpSwitchBtn" title="Đảo chiều dịch">
        <span class="cp-switch-label active" id="cpLabelVi">Tiếng Việt</span>
        <div class="cp-switch-icon-box"><i class="fas fa-exchange-alt"></i></div>
        <span class="cp-switch-label" id="cpLabelZh">Tiếng Trung</span>
    </div>

    <div class="cp-input-wrapper">
        <textarea class="cp-textarea" id="cpInputZh" rows="4" placeholder="Nhập hoặc dán văn bản để Trợ lý dịch giúp bạn..."></textarea>
        <div class="cp-spell-container" id="cpSpellContainer">
            <div class="cp-spell-header">
                <i class="fas fa-triangle-exclamation"></i> Phát hiện từ nghi ngờ sai chính tả / dính phím:
            </div>
            <div class="cp-spell-chips" id="cpSpellChips"></div>
        </div>
        <div class="cp-char-count" id="cpCharCount" style="text-align:right;font-size:.75rem;font-weight:600;color:#64748b;margin-top:4px;">0 / 5000</div>
    </div>

    <button class="cp-btn-start" id="cpStartBtn" type="button">
        <i class="fas fa-rocket"></i> Bắt đầu luyện tập
    </button>
    <button class="cp-btn-buy-token" id="cpBuyTokenBtn" type="button">
        <i class="fas fa-shopping-cart"></i> Mua thêm Token
    </button>

    <div class="cp-progress-wrap" id="cpProgressWrap">
        <div class="cp-progress-text" id="cpProgressText" style="text-align:center;font-size:.8rem;font-weight:700;">Đang xử lý...</div>
        <div class="cp-progress-bar-bg"><div class="cp-progress-bar" id="cpProgressBar"></div></div>
    </div>
</div>

<div class="cp-modal-overlay" id="cpModalOverlay">
    <div class="cp-modal-box">
        <div class="cp-modal-icon"><i class="fas fa-triangle-exclamation"></i></div>
        <h4 class="cp-modal-title">Phát hiện từ nghi ngờ sai chính tả!</h4>
        <p class="cp-modal-desc">Hệ thống phát hiện các từ sau có dấu hiệu gõ nhầm hoặc dính phím:</p>
        <div class="cp-modal-words" id="cpModalWordsList"></div>
        <p class="cp-modal-desc" style="font-size:0.75rem;">Tiếp tục dịch có thể làm tốn Quota và kết quả không chuẩn xác.</p>
        <div class="cp-modal-actions">
            <button class="cp-modal-btn cp-modal-btn-cancel" id="cpModalFixBtn" type="button">Sửa lại văn bản</button>
            <button class="cp-modal-btn cp-modal-btn-proceed" id="cpModalProceedBtn" type="button">Vẫn tiếp tục dịch</button>
        </div>
    </div>
</div>

<div class="cp-modal-overlay" id="cpHistoryOverlay">
    <div class="cp-modal-box" style="max-width: 600px; text-align: left;">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom: 1px solid #eee; padding-bottom: 10px;">
            <div>
                <h4 class="cp-modal-title" style="font-size: 1.1rem; color: #1e1b4b; margin:0;"><i class="fas fa-history"></i> Lịch sử dịch gần đây</h4>
                <div id="cpHistoryCounter" style="font-size: 0.75rem; color: #64748b; margin-top: 2px; font-weight: 600;">Đang tải bộ đếm...</div>
            </div>
            <div style="display:flex; gap:8px; align-items:center;">
                <button id="cpSelectAllHistoryBtn" style="background:linear-gradient(135deg,#4f46e5,#7c3aed); color:#fff; border:none; padding:5px 10px; border-radius:8px; font-size:0.75rem; font-weight:700; cursor:pointer;" title="Chọn tất cả ra luyện tập">
                    <i class="fas fa-check-double"></i> Chọn tất cả
                </button>
                <button id="cpHistoryCloseBtn" style="background:none; border:none; font-size:1.2rem; cursor:pointer; color:#64748b;"><i class="fas fa-times"></i></button>
            </div>
        </div>
        <div id="cpHistoryList" style="max-height: 400px; overflow-y: auto; margin-top: 10px; display: flex; flex-direction: column; gap: 10px;">
        </div>
    </div>
</div>
"""

def build_custom_practice_js():
    return r"""
(function() {
    'use strict';
    var MAX_CHARS = 5000;
    var currentMode = 'vi2zh';
    var SERVER_API_URL = 'https://server-vopb.onrender.com/api/translate'; 

    var inputArea = document.getElementById('cpInputZh');
    var charCount = document.getElementById('cpCharCount');
    var startBtn = document.getElementById('cpStartBtn');
    var buyTokenBtn = document.getElementById('cpBuyTokenBtn');
    var resetBtn = document.getElementById('cpResetBtn');
    var tokenBadge = document.getElementById('cpTokenBadge');
    var tokenText = document.getElementById('cpTokenText');
    
    var switchBtn = document.getElementById('cpSwitchBtn');
    var labelZh = document.getElementById('cpLabelZh');
    var labelVi = document.getElementById('cpLabelVi');
    
    var progressWrap = document.getElementById('cpProgressWrap');
    var progressBar = document.getElementById('cpProgressBar');
    var progressText = document.getElementById('cpProgressText');

    var spellContainer = document.getElementById('cpSpellContainer');
    var spellChips = document.getElementById('cpSpellChips');

    var modalOverlay = document.getElementById('cpModalOverlay');
    var modalWordsList = document.getElementById('cpModalWordsList');
    var modalFixBtn = document.getElementById('cpModalFixBtn');
    var modalProceedBtn = document.getElementById('cpModalProceedBtn');

    var historyBtn = document.getElementById('cpHistoryBtn');
    var historyOverlay = document.getElementById('cpHistoryOverlay');
    var historyList = document.getElementById('cpHistoryList');
    var historyCloseBtn = document.getElementById('cpHistoryCloseBtn');
    var selectAllHistoryBtn = document.getElementById('cpSelectAllHistoryBtn');
    var historyCounter = document.getElementById('cpHistoryCounter');

    var myTokensUsed = 0;
    var myTokenQuota = 0;
    var myBonusTokens = 0;
    var currentUser = null;
    var resolveModalAction = null;
    var cachedHistoryData = [];
    var currentTodayCount = 0;
    var isUserAdmin = false;
    var currentReadRemain = 100;
    
    var TOKEN_REFRESH_COOLDOWN = 60000;
    var lastTokenRefreshTime = 0;
    var isTokenRefreshing = false;
    var cooldownTimerInterval = null;
    
    try {
        var savedTime = parseInt(localStorage.getItem('cp_last_token_refresh') || '0');
        if (savedTime > 0) lastTokenRefreshTime = savedTime;
    } catch(e) {}

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', loadPinyinPro);
    } else {
        loadPinyinPro();
    }

    // ⭐ HÀM KIỂM TRA TRẠNG THÁI HẾT HẠN (Ưu tiên kiểm tra biến toàn cục & banner DOM đầu tiên)
    function checkIsExpired() {
        if (window.APP_TIER === 'expired' || window.APP_TIER === 'expire') return true;
        if (window.isUserExpired === true) return true;
        if (typeof window.isExpired === 'boolean' && window.isExpired) return true;
        
        var expiryBanner = document.getElementById('vocabWarningBanner') || document.querySelector('.vocab-warning-banner.tier-expired');
        if (expiryBanner) return true;

        if (currentUser) {
            if (currentUser.isExpiredOnly === true || currentUser.tier === 'expired' || currentUser.appTier === 'expired' || currentUser.tier === 'expire' || currentUser.appTier === 'expire') return true;
            if (currentUser.expiryDate) {
                var expTime = new Date(currentUser.expiryDate).getTime();
                if (!isNaN(expTime) && expTime < Date.now()) return true;
            }
        }
        return false;
    }

    function updateCooldownUI() {
        if (!tokenText || !tokenBadge) return;
        
        var now = Date.now();
        var timeSinceLastRefresh = now - lastTokenRefreshTime;
        
        if (lastTokenRefreshTime === 0 || timeSinceLastRefresh >= TOKEN_REFRESH_COOLDOWN) {
            tokenBadge.classList.remove('cooldown');
            tokenBadge.style.cursor = 'pointer';
            
            if (currentUser && !isTokenRefreshing) {
                var totalAvailable = myTokenQuota + myBonusTokens;
                var remain = totalAvailable - myTokensUsed;
                if (remain < 0) remain = 0;
                tokenText.textContent = remain.toLocaleString('vi-VN') + ' token';
            }
            
            if (cooldownTimerInterval) {
                clearInterval(cooldownTimerInterval);
                cooldownTimerInterval = null;
            }
            return;
        }
        
        var remainMs = TOKEN_REFRESH_COOLDOWN - timeSinceLastRefresh;
        var remainSec = Math.ceil(remainMs / 1000);
        
        tokenBadge.classList.add('cooldown');
        tokenBadge.style.cursor = 'not-allowed';
        
        if (!isTokenRefreshing) {
            tokenText.textContent = '⏳ Đợi ' + remainSec + 's';
        }
    }

    function startCooldownTimer() {
        if (cooldownTimerInterval) clearInterval(cooldownTimerInterval);
        updateCooldownUI();
        cooldownTimerInterval = setInterval(updateCooldownUI, 1000);
    }

    function initTokenState() {
        var user = null;
        try {
            for (var i = 0; i < localStorage.length; i++) {
                var key = localStorage.key(i);
                if (key && key.indexOf('user_cache_') === 0) {
                    var cached = JSON.parse(localStorage.getItem(key) || 'null');
                    if (cached && cached.data && cached.data.email) {
                        user = cached.data;
                        break;
                    }
                }
            }
        } catch(e) {}

        currentUser = user;
        if (!user) {
            tokenText.textContent = 'Chưa đăng nhập';
            tokenBadge.className = 'cp-token-badge warn';
            startBtn.disabled = true;
            return;
        }

        if (user.role === 'super_admin' || user.role === 'admin' || user.isPermanent) {
            if (user.role === 'admin' || user.role === 'super_admin') {
                myTokenQuota = 100000;
            } else {
                tokenText.textContent = 'Không giới hạn';
                tokenBadge.className = 'cp-token-badge';
                return;
            }
        } else {
            myTokenQuota = user.tokenQuota || 20000;
        }

        myBonusTokens = user.bonusTokens || 0;
        myTokensUsed = user.tokensUsed || 0;

        var isExpired = checkIsExpired();
        renderTokenUI(isExpired);

        refreshTokenFromFirestore().catch(function() {});

        try {
            var savedRefreshTime = parseInt(localStorage.getItem('cp_last_token_refresh') || '0');
            if (savedRefreshTime > 0) {
                lastTokenRefreshTime = savedRefreshTime;
                var timePassed = Date.now() - savedRefreshTime;
                
                if (timePassed < TOKEN_REFRESH_COOLDOWN) {
                    startCooldownTimer();
                } else {
                    lastTokenRefreshTime = 0;
                    try { localStorage.removeItem('cp_last_token_refresh'); } catch(e) {}
                }
            }
        } catch(e) {}
    }

    async function refreshTokenFromFirestore() {
        if (!currentUser || !currentUser.email || typeof db === 'undefined' || !db) {
            return false;
        }
        
        try {
            var doc = await db.collection('allowed_users').doc(currentUser.email).get({ source: 'server' });
            if (!doc.exists) return false;
            
            var freshData = doc.data();
            currentUser.bonusTokens = freshData.bonusTokens || 0;
            currentUser.tokensUsed = freshData.tokensUsed || 0;
            currentUser.tokenQuota = freshData.tokenQuota || 10000;
            currentUser.isPermanent = freshData.isPermanent || false;
            currentUser.role = freshData.role || currentUser.role;
            
            currentUser.isExpiredOnly = freshData.isExpiredOnly || false;
            currentUser.tier = freshData.tier || null;
            currentUser.appTier = freshData.appTier || null;
            currentUser.expiryDate = freshData.expiryDate || null;
            
            myTokenQuota = currentUser.tokenQuota;
            myBonusTokens = currentUser.bonusTokens;
            myTokensUsed = currentUser.tokensUsed;
            
            try {
                var cacheKey = 'user_cache_' + currentUser.email;
                var cached = JSON.parse(localStorage.getItem(cacheKey) || 'null');
                if (cached && cached.data) {
                    cached.data.bonusTokens = currentUser.bonusTokens;
                    cached.data.tokensUsed = currentUser.tokensUsed;
                    cached.data.tokenQuota = currentUser.tokenQuota;
                    cached.data.isPermanent = currentUser.isPermanent;
                    cached.data.isExpiredOnly = currentUser.isExpiredOnly;
                    cached.data.tier = currentUser.tier;
                    cached.data.appTier = currentUser.appTier;
                    cached.data.expiryDate = currentUser.expiryDate;
                    
                    localStorage.setItem(cacheKey, JSON.stringify(cached));
                }
            } catch(e) {}
            
            var isExpired = checkIsExpired();
            renderTokenUI(isExpired);
            return true;
        } catch(e) {
            return false;
        }
    }

    function renderTokenUI(isExpired) {
        // ⭐ CHẶN HIỂN THỊ TOKEN KHI CHƯA ĐĂNG NHẬP
        if (!currentUser) {
            tokenText.textContent = 'Chưa đăng nhập';
            tokenBadge.className = 'cp-token-badge warn';
            tokenBadge.style.pointerEvents = 'none'; 
            tokenBadge.style.opacity = '1';
            tokenBadge.title = 'Vui lòng đăng nhập';
            
            startBtn.classList.add('cp-hidden');
            buyTokenBtn.classList.remove('cp-hidden');
            buyTokenBtn.innerHTML = '<i class="fas fa-sign-in-alt"></i> Đăng nhập để sử dụng';
            
            inputArea.disabled = true;
            inputArea.placeholder = 'Vui lòng đăng nhập để sử dụng Trợ lý dịch thuật.';
            
            var historyBtnEl = document.getElementById('cpHistoryBtn');
            if (historyBtnEl) {
                historyBtnEl.disabled = true;
                historyBtnEl.style.opacity = '0.4';
                historyBtnEl.style.cursor = 'not-allowed';
                historyBtnEl.title = 'Vui lòng đăng nhập';
                historyBtnEl.innerHTML = '<i class="fas fa-lock"></i>';
            }
            return; // Dừng ngay, không chạy xuống phần tính toán token
        }

        // ⭐ XỬ LÝ CHO ADMIN / PREMIUM
        if (currentUser.role === 'super_admin' || currentUser.isPermanent) {
            tokenText.textContent = 'Không giới hạn';
            tokenBadge.className = 'cp-token-badge';
            tokenBadge.style.pointerEvents = 'auto';
            tokenBadge.style.opacity = '1';
            tokenBadge.title = 'Bấm để cập nhật số Token mới nhất';
            
            // Đảm bảo các nút mở khóa cho admin
            startBtn.classList.remove('cp-hidden');
            buyTokenBtn.classList.add('cp-hidden');
            inputArea.disabled = false;
            return;
        }

        // ⭐ TÍNH TOÁN TOKEN CHO USER THƯỜNG
        var totalAvailable = myTokenQuota + myBonusTokens;
        var remain = totalAvailable - myTokensUsed;
        if (remain < 0) remain = 0;

        tokenText.textContent = remain.toLocaleString('vi-VN') + ' token';
        tokenBadge.classList.remove('warn', 'danger');
        
        // ⭐ XỬ LÝ NÚT LỊCH SỬ
        var historyBtnEl = document.getElementById('cpHistoryBtn');
        if (historyBtnEl) {
            if (isExpired) {
                historyBtnEl.disabled = true;
                historyBtnEl.style.opacity = '0.4';
                historyBtnEl.style.cursor = 'not-allowed';
                historyBtnEl.title = 'Tài khoản đã hết hạn - Không thể xem lịch sử';
                historyBtnEl.innerHTML = '<i class="fas fa-lock"></i>';
            } else {
                historyBtnEl.disabled = false;
                historyBtnEl.style.opacity = '1';
                historyBtnEl.style.cursor = 'pointer';
                historyBtnEl.title = 'Xem lịch sử';
                historyBtnEl.innerHTML = '<i class="fas fa-clock-rotate-left"></i>';
            }
        }

        // ⭐ XỬ LÝ KHI HẾT HẠN
        if (isExpired) {
            tokenBadge.classList.add('danger');
            tokenBadge.style.pointerEvents = 'none';
            tokenBadge.style.opacity = '0.6';
            tokenBadge.title = 'Tài khoản đã hết hạn - Không thể làm mới Token';
            
            startBtn.classList.add('cp-hidden');
            buyTokenBtn.classList.remove('cp-hidden');
            buyTokenBtn.innerHTML = '<i class="fas fa-crown"></i> Gia hạn ngay (Giữ nguyên Token)';
            
            inputArea.disabled = true;
            inputArea.placeholder = 'Tài khoản đã hết hạn. Vui lòng gia hạn để tiếp tục sử dụng Luyện tập tự do.';
            return; 
        }

        // ⭐ XỬ LÝ KHI CÒN HẠN (Mở khóa nút Refresh)
        tokenBadge.style.pointerEvents = 'auto';
        tokenBadge.style.opacity = '1';
        tokenBadge.title = 'Bấm để cập nhật số Token mới nhất';

        if (remain <= 2000) tokenBadge.classList.add('danger');
        else if (remain <= 5000) tokenBadge.classList.add('warn');

        // ⭐ KIỂM TRA SỐ DƯ TOKEN
        if (remain <= 0 && currentUser.role !== 'admin') {
            startBtn.classList.add('cp-hidden');
            buyTokenBtn.classList.remove('cp-hidden');
            buyTokenBtn.innerHTML = '<i class="fas fa-shopping-cart"></i> Mua thêm Token';
            
            inputArea.disabled = true;
            inputArea.placeholder = 'Bạn đã hết Token. Vui lòng mua thêm để tiếp tục.';
        } else {
            startBtn.classList.remove('cp-hidden');
            buyTokenBtn.classList.add('cp-hidden');
            
            inputArea.disabled = false;
            inputArea.placeholder = currentMode === 'vi2zh' ? 'Nhập văn bản tiếng Việt vào đây...' : 'Dán văn bản tiếng Trung vào đây...';
        }
    }

    buyTokenBtn.addEventListener('click', function() {
        // ⭐ NẾU CHƯA ĐĂNG NHẬP -> MỞ MODAL ĐĂNG NHẬP
        if (!currentUser) {
            if (typeof openLoginModal === 'function') openLoginModal();
            else alert('Vui lòng đăng nhập để sử dụng tính năng này!');
            return;
        }
        
        // Nếu đã đăng nhập -> Mở modal gia hạn
        if (typeof openRenewalModal === 'function') openRenewalModal();
        else alert('Vui lòng liên hệ Admin để gia hạn tài khoản!');
    });
    function autoResizeTextarea() {
        inputArea.style.height = 'auto';
        var newHeight = inputArea.scrollHeight;
        var maxHeight = 400;
        if (newHeight > maxHeight) {
            inputArea.style.height = maxHeight + 'px';
            inputArea.style.overflowY = 'auto';
        } else {
            inputArea.style.height = newHeight + 'px';
            inputArea.style.overflowY = 'hidden';
        }
    }

    function findSuspiciousWords() {
        if (currentMode !== 'vi2zh') return [];
        var text = inputArea.value;
        var rawWords = text.split(/\s+/);
        var suspicious = [];
        var whitelist = ['tr', 'và', 'của', 'cho', 'với', 'để', 'là', 'có', 'không', 'những', 'các', 'được'];

        for (var i = 0; i < rawWords.length; i++) {
            var w = rawWords[i].replace(/^[.,!?;:"'()\[\]{}]+|[.,!?;:"'()\[\]{}]+$/g, '');
            if (!w || w.length < 3) continue;
            if (whitelist.includes(w.toLowerCase())) continue;

            var wLower = w.toLowerCase();
            var hasTripleChar = /(.)\1{2,}/.test(wLower);
            var vowelsRegex = /[aeiouyàáảãạâầấẩẫậăằắẳẵặèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵ]/i;
            var hasVowel = vowelsRegex.test(wLower);

            if (hasTripleChar || (!hasVowel && w.length >= 4)) {
                if (suspicious.indexOf(w) === -1) suspicious.push(w);
            }
        }
        return suspicious;
    }

    function checkSpellingSuggestions() {
        var suspiciousWords = findSuspiciousWords();
        if (suspiciousWords.length > 0) {
            spellChips.innerHTML = '';
            suspiciousWords.forEach(function(word) {
                var chip = document.createElement('div');
                chip.className = 'cp-spell-chip';
                chip.innerHTML = '<i class="fas fa-triangle-exclamation"></i> ' + word;
                spellChips.appendChild(chip);
            });
            spellContainer.classList.add('show');
        } else {
            spellContainer.classList.remove('show');
        }
    }

    function updateCharCount() {
        var len = inputArea.value.length;
        charCount.textContent = len + ' / ' + MAX_CHARS;
        if (len > MAX_CHARS) {
            charCount.classList.add('over');
            inputArea.value = inputArea.value.substring(0, MAX_CHARS);
            charCount.textContent = MAX_CHARS + ' / ' + MAX_CHARS + ' (Đã cắt)';
        } else {
            charCount.classList.remove('over');
        }
        autoResizeTextarea();
        checkSpellingSuggestions();
    }

    inputArea.addEventListener('input', updateCharCount);
    setTimeout(updateCharCount, 200);

    switchBtn.addEventListener('click', function() {
        if (currentMode === 'vi2zh') {
            currentMode = 'zh2vi';
            labelVi.classList.remove('active');
            labelZh.classList.add('active');
            spellContainer.classList.remove('show');
            if (!inputArea.disabled) inputArea.placeholder = '输入或粘贴中文文本，让翻译助手帮您搞定...';
        } else {
            currentMode = 'vi2zh';
            labelZh.classList.remove('active');
            labelVi.classList.add('active');
            if (!inputArea.disabled) inputArea.placeholder = 'Nhập hoặc dán văn bản để Trợ lý dịch giúp bạn...';
        }
        inputArea.value = '';
        updateCharCount();
    });

    resetBtn.addEventListener('click', function() {
        inputArea.value = '';
        spellContainer.classList.remove('show');
        updateCharCount();
        progressWrap.classList.remove('show');
        startBtn.disabled = false;
        startBtn.innerHTML = '<i class="fas fa-rocket"></i> Bắt đầu luyện tập';
        setTimeout(autoResizeTextarea, 50);
    });

    function showSpellModal(words) {
        return new Promise(function(resolve) {
            modalWordsList.textContent = words.join(', ');
            modalOverlay.classList.add('show');
            resolveModalAction = resolve;
        });
    }

    modalFixBtn.addEventListener('click', function() {
        modalOverlay.classList.remove('show');
        if (resolveModalAction) resolveModalAction(false);
    });

    modalProceedBtn.addEventListener('click', function() {
        modalOverlay.classList.remove('show');
        if (resolveModalAction) resolveModalAction(true);
    });

    function smartSplit(text, mode) {
        var protectedText = text.replace(/(\d)\.(\d)/g, '$1__DOT__$2');
        var rawParts = protectedText.split(/(?<=[.!?。！？\n])/g);
        var result = [];
        for (var i = 0; i < rawParts.length; i++) {
            var s = rawParts[i].replace(/__DOT__/g, '.').trim();
            if (s.length === 0) continue;
            if (mode === 'zh2vi') {
                if (!/[\u4e00-\u9fa5]/.test(s)) continue; 
            } else {
                if (!/[a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂưăạảấầẩẫậắằẳẵặẹẻẽềếểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪỬỮỰỲỴÝỶỸửữựỳỵỷỹ]/.test(s)) continue;
            }
            result.push(s);
        }
        return result;
    }

    startBtn.addEventListener('click', async function() {
        if (!currentUser) { alert('Vui lòng đăng nhập!'); return; }

        var isExpired = checkIsExpired();
        if (isExpired) {
            alert('Tài khoản của bạn đã hết hạn. Vui lòng gia hạn để tiếp tục sử dụng tính năng Luyện tập tự do.\n(Số dư Token của bạn vẫn được bảo lưu an toàn).');
            if (typeof openRenewalModal === 'function') openRenewalModal();
            return;
        }

        if (currentUser.role !== 'admin' && currentUser.role !== 'super_admin' && !currentUser.isPermanent && (myTokenQuota + myBonusTokens - myTokensUsed <= 0)) { 
            alert('Bạn đã hết token!'); 
            return; 
        }

        var rawText = inputArea.value.trim();
        if (!rawText) { alert('Vui lòng nhập văn bản!'); return; }

        var suspiciousWords = findSuspiciousWords();
        if (suspiciousWords.length > 0) {
            var proceed = await showSpellModal(suspiciousWords);
            if (!proceed) return;
        }

        startBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Đang dịch...';
        startBtn.disabled = true;
        switchBtn.style.pointerEvents = 'none';
        progressWrap.classList.add('show');
        progressBar.style.width = '0%';

        var sentences = smartSplit(rawText, currentMode);
        if (sentences.length === 0) {
            alert('Không tìm thấy câu hợp lệ!');
            finishProcess();
            return;
        }

        await loadPinyinPro();

        var total = sentences.length;
        var customData = [];
        var totalTokensThisSession = 0;
        var CHUNK_SIZE = 10;
        var processedCount = 0;

        try {
            for (var i = 0; i < total; i += CHUNK_SIZE) {
                var chunk = sentences.slice(i, i + CHUNK_SIZE);
                var combinedText = chunk.join('\n[---]\n');
                
                var data = await fetchTranslate(combinedText, currentMode);
                if (data.tokensUsed > 0) {
                    totalTokensThisSession += data.tokensUsed;
                }

                var translatedChunk = data.translated.split(/\n?\[\s*---\s*\]\n?/);

                for (var j = 0; j < chunk.length; j++) {
                    var originalSentence = chunk[j];
                    var transSentence = translatedChunk[j] ? translatedChunk[j].trim() : originalSentence;

                    var zhText = currentMode === 'vi2zh' ? transSentence : originalSentence;
                    var viText = currentMode === 'vi2zh' ? originalSentence : transSentence;
                    var pinyinStr = getSmartPinyin(zhText);

                    customData.push({
                        stt: String(i + j + 1),
                        zh: zhText,
                        vi: viText,
                        pinyin: pinyinStr,
                        hsk: 'HSK1',
                        topic: 'Văn bản tự do',
                        subject: 'Custom'
                    });

                    processedCount++;
                    var pct = Math.round((processedCount / total) * 100);
                    progressBar.style.width = pct + '%';
                    progressText.textContent = 'Đang xử lý: ' + processedCount + ' / ' + total + ' câu (' + pct + '%)';
                }
            }

            customData.sort(function(a, b) { return parseInt(a.stt) - parseInt(b.stt); });

            if (currentUser && currentUser.email && customData.length > 0) {
                fetch(SERVER_API_URL.replace('/translate', '/history'), {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        email: currentUser.email,
                        items: customData
                    })
                }).catch(function(e) {});
            }

            if (totalTokensThisSession > 0) {
                myTokensUsed += totalTokensThisSession;
                renderTokenUI(checkIsExpired());
                try {
                    var cacheKey = 'user_cache_' + currentUser.email;
                    var cached = JSON.parse(localStorage.getItem(cacheKey) || 'null');
                    if (cached && cached.data) { 
                        cached.data.tokensUsed = myTokensUsed; 
                        localStorage.setItem(cacheKey, JSON.stringify(cached)); 
                    }
                } catch(e) {}
            }

            loadDataToPracticeScreen(customData);
        } catch(e) {
            alert('Có lỗi xảy ra: ' + e.message);
        } finally {
            finishProcess();
        }
    });

    function loadDataToPracticeScreen(customData) {
        if (typeof window.activateCustomPracticeMode === 'function') {
            window.activateCustomPracticeMode(customData);
        } else {
            if (typeof RAW_DATA !== 'undefined') RAW_DATA = customData;
            if (typeof filtered !== 'undefined') filtered = customData;
            if (typeof buildFilters === 'function') buildFilters();
            if (typeof applyFilter === 'function') applyFilter();
            if (typeof updateResultCount === 'function') updateResultCount();
            if (typeof render === 'function') render(true);
        }
    }

    function finishProcess() {
        startBtn.innerHTML = '<i class="fas fa-rocket"></i> Bắt đầu luyện tập';
        startBtn.disabled = false;
        switchBtn.style.pointerEvents = 'auto';
        setTimeout(function() { progressWrap.classList.remove('show'); }, 1200);
        
        if (currentUser) {
            renderTokenUI(checkIsExpired());
        }
    }

    function loadPinyinPro() {
        if (window.pinyinPro) return Promise.resolve();
        return new Promise(function(resolve) {
            var script = document.createElement('script');
            script.src = 'https://unpkg.com/pinyin-pro@3.18.2/dist/index.js';
            script.onload = function() {
                if (!window.pinyinPro && window.pinyin) window.pinyinPro = window.pinyin;
                resolve();
            };
            script.onerror = function() {
                var script2 = document.createElement('script');
                script2.src = 'https://cdn.jsdelivr.net/npm/pinyin-pro@3.18.2/dist/index.min.js';
                script2.onload = resolve;
                script2.onerror = resolve;
                document.head.appendChild(script2);
            };
            document.head.appendChild(script);
        });
    }

    function getSmartPinyin(text) {
        if (!text) return '';
        if (!window.pinyinPro) return text;

        try {
            if (typeof Intl !== 'undefined' && Intl.Segmenter) {
                var segmenter = new Intl.Segmenter('zh', { granularity: 'word' });
                var result = [];
                for (var seg of segmenter.segment(text)) {
                    var word = seg.segment;
                    if (/[\u4e00-\u9fa5]/.test(word)) {
                        result.push(window.pinyinPro.pinyin(word, { toneType: 'symbol', separator: '' }));
                    } else {
                        result.push(word);
                    }
                }
                return result.join(' ');
            }
            return window.pinyinPro.pinyin(text, { toneType: 'symbol', separator: ' ' });
        } catch (e) {
            return window.pinyinPro.pinyin(text, { toneType: 'symbol', separator: ' ' });
        }
    }

    async function fetchTranslate(text, mode) {
        var translated = '';
        var tokensUsed = 0;

        try {
            var source = mode === 'zh2vi' ? 'zh-CN' : 'vi';
            var target = mode === 'zh2vi' ? 'vi' : 'zh-CN';
            
            var res = await fetch(SERVER_API_URL, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ 
                    text: text, 
                    source: source, 
                    target: target,
                    email: currentUser ? currentUser.email : ''
                })
            });
            
            if (!res.ok) throw new Error('HTTP ' + res.status);
            var json = await res.json();
            if (json.error) throw new Error(json.error);
            
            translated = json.translated;
            tokensUsed = json.tokensUsed || 0;
        } catch(e) {
            translated = text; 
        }
        
        return { translated: translated, tokensUsed: tokensUsed };
    }

    function updateCounterUI() {
        if (!historyCounter) return;
        if (isUserAdmin) {
            historyCounter.innerHTML = '<span style="color:#059669; font-weight:700;"><i class="fas fa-shield-halved"></i> Admin: Không giới hạn Read/Save</span>';
        } else {
            var saveRemain = 100 - currentTodayCount;
            if (saveRemain < 0) saveRemain = 0;
            var readRemainText = (typeof currentReadRemain !== 'undefined') ? currentReadRemain : 100;
            historyCounter.innerHTML = '📖 Lượt xem hôm nay: <b style="color:' + (readRemainText > 0 ? '#4f46e5' : '#dc2626') + ';">' + readRemainText + '</b>/100 | ⏳ Đã lưu: <b>' + currentTodayCount + '</b>/100';
        }
    }

    function renderHistoryUI() {
        updateCounterUI();
        if (cachedHistoryData.length === 0) {
            historyList.innerHTML = '<div style="text-align:center; color:#64748b; font-size:0.9rem;">Chưa có lịch sử dịch nào.</div>';
            return;
        }
        
        var html = '';
        cachedHistoryData.forEach(function(item, idx) {
            html += '<div class="cp-history-item" style="position:relative;" id="cp-hist-' + (item.id || idx) + '">' +
                '<div class="cp-history-vi">' + (item.text_vi || '') + '</div>' +
                '<div class="cp-history-zh">' + (item.text_zh || '') + '</div>' +
                (item.pinyin ? '<div class="cp-history-pinyin">' + item.pinyin + '</div>' : '') +
                '<div style="display:flex; justify-content:space-between; align-items:center; margin-top:8px;">' +
                    '<div class="cp-history-time">' + (item.createdAt || '') + '</div>' +
                    '<div style="display:flex; gap:6px;">' +
                        '<button class="cp-delete-single-history" data-id="' + (item.id || '') + '" data-index="' + idx + '" style="background:#fee2e2; color:#ef4444; border:none; padding:5px 10px; border-radius:8px; font-size:0.75rem; font-weight:700; cursor:pointer;" title="Xóa câu này">' +
                            '<i class="fas fa-trash-alt"></i> Xóa' +
                        '</button>' +
                        '<button class="cp-load-single-history" data-index="' + idx + '" style="background:linear-gradient(135deg,#6366f1,#a855f7); color:#fff; border:none; padding:5px 12px; border-radius:8px; font-size:0.75rem; font-weight:700; cursor:pointer;" type="button">' +
                            '<i class="fas fa-play"></i> Luyện tập' +
                        '</button>' +
                    '</div>' +
                '</div>' +
            '</div>';
        });
        historyList.innerHTML = html;
        
        var singleBtns = historyList.querySelectorAll('.cp-load-single-history');
        singleBtns.forEach(function(btn) {
            btn.addEventListener('click', function() {
                var idx = parseInt(this.getAttribute('data-index'));
                var targetItem = cachedHistoryData[idx];
                if (!targetItem) return;

                var singleData = [{
                    stt: '1',
                    zh: targetItem.text_zh || '',
                    vi: targetItem.text_vi || '',
                    pinyin: targetItem.pinyin || '',
                    hsk: 'HSK1',
                    topic: 'Lịch sử dịch',
                    subject: 'History'
                }];

                historyOverlay.classList.remove('show');
                loadDataToPracticeScreen(singleData);
            });
        });

        var deleteBtns = historyList.querySelectorAll('.cp-delete-single-history');
        deleteBtns.forEach(function(btn) {
            btn.addEventListener('click', async function() {
                var docId = this.getAttribute('data-id');
                var idx = parseInt(this.getAttribute('data-index'));
                if (!confirm('Bạn có chắc chắn muốn xóa câu này khỏi lịch sử?')) return;

                if (docId) {
                    try {
                        var res = await fetch(SERVER_API_URL.replace('/translate', '/history/delete'), {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ email: currentUser.email, id: docId })
                        });
                        var json = await res.json();
                        if (json.ok && typeof json.todayCount !== 'undefined') {
                            currentTodayCount = json.todayCount;
                        }
                    } catch(e) {}
                }

                cachedHistoryData.splice(idx, 1);
                renderHistoryUI();
            });
        });
    }

    if (historyBtn) {
        historyBtn.addEventListener('click', async function() {
            if (!currentUser || !currentUser.email) { alert('Vui lòng đăng nhập để xem lịch sử!'); return; }
            
            var isExpired = checkIsExpired();
            if (isExpired) {
                alert('Tài khoản của bạn đã hết hạn. Vui lòng gia hạn để xem lịch sử dịch.\n(Số dư Token và lịch sử của bạn vẫn được bảo lưu an toàn).');
                if (typeof openRenewalModal === 'function') openRenewalModal();
                return;
            }

            historyOverlay.classList.add('show');
            historyList.innerHTML = '<div style="text-align:center; color:#64748b; font-size:0.9rem;"><i class="fas fa-spinner fa-spin"></i> Đang tải...</div>';
            historyCounter.textContent = 'Đang tải bộ đếm...';
            
            try {
                var res = await fetch(SERVER_API_URL.replace('/translate', '/history'), {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ 
                        email: currentUser.email,
                        _method: 'GET'
                    })
                });
                
                var json = await res.json();
                if (!json.ok || !json.history) throw new Error(json.error || 'Không thể tải lịch sử');
                
                cachedHistoryData = json.history;
                currentTodayCount = json.todayCount || 0;
                currentReadRemain = (typeof json.readRemain !== 'undefined') ? json.readRemain : 100;
                isUserAdmin = json.isAdmin || false;

                renderHistoryUI();
                
            } catch (e) {
                historyList.innerHTML = '<div style="text-align:center; color:#ef4444; font-size:0.9rem;">Lỗi tải lịch sử: ' + e.message + '</div>';
                historyCounter.textContent = 'Không tải được bộ đếm';
            }
        });
    }

    if (selectAllHistoryBtn) {
        selectAllHistoryBtn.addEventListener('click', function() {
            if (!cachedHistoryData || cachedHistoryData.length === 0) {
                alert('Không có lịch sử nào để chọn!');
                return;
            }

            var allPracticeData = [];
            cachedHistoryData.forEach(function(item, idx) {
                allPracticeData.push({
                    stt: String(idx + 1),
                    zh: item.text_zh || '',
                    vi: item.text_vi || '',
                    pinyin: item.pinyin || '',
                    hsk: 'HSK1',
                    topic: 'Lịch sử dịch',
                    subject: 'History'
                });
            });

            historyOverlay.classList.remove('show');
            loadDataToPracticeScreen(allPracticeData);
        });
    }

    if (historyCloseBtn) {
        historyCloseBtn.addEventListener('click', function() {
            historyOverlay.classList.remove('show');
        });
    }
    if (historyOverlay) {
        historyOverlay.addEventListener('click', function(e) {
            if (e.target === this) this.classList.remove('show');
        });
    }

    if (tokenBadge) {
        tokenBadge.addEventListener('click', async function() {
            var now = Date.now();
            var timeSinceLastRefresh = now - lastTokenRefreshTime;
            
            if (isTokenRefreshing || this.classList.contains('refreshing')) return;
            
            if (timeSinceLastRefresh < TOKEN_REFRESH_COOLDOWN) {
                var waitSec = Math.ceil((TOKEN_REFRESH_COOLDOWN - timeSinceLastRefresh) / 1000);
                if (typeof showUserChangedToast === 'function') {
                    showUserChangedToast('⏳ Vui lòng đợi ' + waitSec + ' giây nữa', 'warn');
                }
                return;
            }
            
            isTokenRefreshing = true;
            lastTokenRefreshTime = now;
            try { localStorage.setItem('cp_last_token_refresh', String(now)); } catch(e) {}
            
            this.classList.add('refreshing');
            this.classList.remove('cooldown');
            var originalText = tokenText.textContent;
            tokenText.textContent = 'Đang cập nhật...';
            
            var ok = await refreshTokenFromFirestore();
            
            this.classList.remove('refreshing');
            isTokenRefreshing = false;
            
            if (!ok) {
                lastTokenRefreshTime = 0;
                try { localStorage.removeItem('cp_last_token_refresh'); } catch(e) {}
                tokenText.textContent = originalText;
                if (typeof showUserChangedToast === 'function') {
                    showUserChangedToast('⚠️ Không thể cập nhật, vui lòng thử lại', 'warn');
                }
            } else {
                if (typeof showUserChangedToast === 'function') {
                    showUserChangedToast('✅ Đã cập nhật số dư Token. Đợi 60s để bấm tiếp.', 'success');
                }
                startCooldownTimer();
            }
        });
    }

    setTimeout(initTokenState, 100);
    setTimeout(initTokenState, 1500);

})();
"""

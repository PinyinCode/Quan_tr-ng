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

/* ⭐ MODAL POPUP CẢNH BÁO TÙY CHỈNH (GLASSMORPHISM) */
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
"""

def build_custom_practice_html():
    return r"""
<div class="cp-card" id="cpSection">
    <div class="cp-header-row">
        <div class="cp-section-header">
            <div class="cp-icon-badge"><i class="fas fa-wand-magic-sparkles"></i></div>
            <div class="cp-title-group">
                <h3>Luyện Dịch Tự Do</h3>
                <p>Nhập văn bản bất kỳ để luyện tập</p>
            </div>
        </div>
        <div style="display:flex; gap:8px; align-items:center;">
            <div class="cp-token-badge" id="cpTokenBadge">
                <i class="fas fa-bolt"></i> <span id="cpTokenText">Đang tải...</span>
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
        <textarea class="cp-textarea" id="cpInputZh" rows="4" placeholder="Nhập văn bản tiếng Việt vào đây..."></textarea>
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
    var myTokenQuota = 20000;
    var myBonusTokens = 0;
    var currentUser = null;
    var resolveModalAction = null;
    var cachedHistoryData = [];
    var currentTodayCount = 0;
    var isUserAdmin = false;
    var currentReadRemain = 100;

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
        renderTokenUI();
    }

    function renderTokenUI() {
        if (currentUser && (currentUser.role === 'super_admin' || currentUser.isPermanent)) {
            tokenText.textContent = 'Không giới hạn';
            tokenBadge.className = 'cp-token-badge';
            return;
        }

        var totalAvailable = myTokenQuota + myBonusTokens;
        var remain = totalAvailable - myTokensUsed;
        if (remain < 0) remain = 0;

        tokenText.textContent = remain.toLocaleString('vi-VN') + ' token';
        tokenBadge.classList.remove('warn', 'danger');
        if (remain <= 2000) tokenBadge.classList.add('danger');
        else if (remain <= 5000) tokenBadge.classList.add('warn');

        if (remain <= 0 && currentUser.role !== 'admin') {
            startBtn.style.display = 'none';
            buyTokenBtn.style.display = 'flex';
            inputArea.disabled = true;
        } else {
            startBtn.style.display = 'flex';
            buyTokenBtn.style.display = 'none';
            inputArea.disabled = false;
        }
    }

    buyTokenBtn.addEventListener('click', function() {
        if (typeof openRenewalModal === 'function') openRenewalModal();
        else alert('Vui lòng liên hệ Admin để mua thêm Token!');
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
        var words = text.match(/\b[A-Za-zÀ-ỹ]+\b/g) || [];
        var suspicious = [];

        for (var i = 0; i < words.length; i++) {
            var w = words[i];
            var wLower = w.toLowerCase();
            if (w.length <= 1) continue;
            var hasInvalidDouble = /(hh|gg|kk|bb|dd|cc|vv|mm|pp|ss|ff|zz|jj|ww|qq|xx)/.test(wLower);
            var vowelsRegex = /[aeiouyàáảãạâầấẩẫậăằắẳẵặèéẻẽẹêềếểễệìíỉĩịòóỏõọôôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵ]/i;
            var hasVowel = vowelsRegex.test(wLower);

            if (hasInvalidDouble || !hasVowel) {
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
            if (!inputArea.disabled) inputArea.placeholder = 'Dán văn bản tiếng Trung vào đây...';
        } else {
            currentMode = 'vi2zh';
            labelZh.classList.remove('active');
            labelVi.classList.add('active');
            if (!inputArea.disabled) inputArea.placeholder = 'Nhập văn bản tiếng Việt vào đây...';
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
                totalTokensThisSession += (data.tokensUsed || 0);

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
                renderTokenUI();
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
            console.error('[CP] Batch processing error:', e);
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
    }

    function loadPinyinPro() {
        if (window.pinyinPro) return Promise.resolve();
        return new Promise(function(resolve) {
            var script = document.createElement('script');
            script.src = 'https://cdn.jsdelivr.net/npm/pinyin-pro@3.18.2/dist/index.min.js';
            script.onload = resolve;
            script.onerror = function() { resolve(); };
            document.head.appendChild(script);
        });
    }

        // ⭐ Hàm chuyển đổi Pinyin tự động nhận diện & gộp cụm từ ghép
        // ⭐ Hàm getSmartPinyin chuẩn hóa riêng cho chế độ Dịch Tự Do -> Màn hình Luyện Tập
    function getSmartPinyin(text) {
        if (!window.pinyinPro || !text) return '';
        try {
            // 1. Tách câu Tiếng Trung thành mảng các cụm từ ghép (Chữ Hán)
            var words = window.pinyinPro.pinyin(text, { type: 'array', segmentit: true });
            
            // 2. Chuyển từng cụm từ ghép sang Pinyin liền nhau (separator: '')
            var pinyinWords = words.map(function(word) {
                if (/[\u4e00-\u9fa5]/.test(word)) {
                    return window.pinyinPro.pinyin(word, { toneType: 'symbol', separator: '' });
                }
                return word;
            });
            
            // 3. Nối các cụm từ ghép bằng 1 khoảng trắng duy nhất
            return pinyinWords.join(' ');
        } catch (e) {
            return window.pinyinPro.pinyin(text, { toneType: 'symbol' });
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
                
                // ⭐ ĐOẠN ĐƯỢC CHÈN VÀO ĐÂY:
                cachedHistoryData = json.history;
                currentTodayCount = json.todayCount || 0;
                currentReadRemain = (typeof json.readRemain !== 'undefined') ? json.readRemain : 100;
                isUserAdmin = json.isAdmin || false;

                // Gọi vẽ lại giao diện lịch sử & bộ đếm
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

    setTimeout(initTokenState, 100);
    setTimeout(initTokenState, 1500);

})();
"""

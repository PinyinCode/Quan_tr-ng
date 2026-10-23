# -*- coding: utf-8 -*-
r"""
custom_practice_module.py - Khu vực Luyện tập Tự do (Tích hợp Gợi ý chính tả trực quan)
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

/* ⭐ GIAO DIỆN KHUNG GỢI Ý CHÍNH TẢ TRỰC QUAN */
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
    cursor: pointer;
    font-weight: 600;
    transition: all 0.2s;
    box-shadow: 0 2px 4px rgba(0,0,0,0.02);
}
.cp-spell-chip:hover {
    background: #f59e0b;
    color: #ffffff;
    transform: translateY(-1px);
}

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

@media (min-width: 768px) {
    .cp-btn-start, .cp-btn-buy-token { width: auto; min-width: 280px; align-self: flex-end; }
}
@media (max-width: 500px) {
    .cp-card { padding: 1.25rem; }
    .cp-title-group h3 { font-size: 1.05rem; }
    .cp-textarea { min-height: 100px; }
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
        <textarea class="cp-textarea" id="cpInputZh" rows="4" placeholder="Nhập văn bản tiếng Việt vào đây... (tối đa 5000 ký tự)"></textarea>
        
        <!-- ⭐ KHUNG GỢI Ý CHÍNH TẢ TRỰC QUAN -->
        <div class="cp-spell-container" id="cpSpellContainer">
            <div class="cp-spell-header">
                <i class="fas fa-triangle-exclamation"></i> Gợi ý chỉnh sửa chính tả/từ viết tắt:
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
"""

def build_custom_practice_js():
    return r"""
(function() {
    'use strict';
    var MAX_CHARS = 5000;
    var BATCH_SIZE = 10;
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

    var myTokensUsed = 0;
    var myTokenQuota = 20000;
    var myBonusTokens = 0;
    var currentUser = null;

    // ⭐ TỪ ĐIỂN TỪ VIẾT TẮT / LỖI CHÍNH TẢ PHỔ BIẾN (TIẾNG VIỆT)
    var commonTyposVi = {
        'ko': 'không', 'hok': 'không', 'kg': 'không', 'k': 'không',
        'dc': 'được', 'đc': 'được',
        'nhg': 'nhưng',
        'đg': 'đang',
        'j': 'gì',
        'rùi': 'rồi',
        'ik': 'đi',
        'bit': 'biết', 'bít': 'biết',
        'mng': 'mọi người', 'mn': 'mọi người',
        'tks': 'cảm ơn', 'thank': 'cảm ơn',
        'vs': 'với',
        'ntn': 'như thế nào',
        'kh': 'không', 'hok': 'không'
    };

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

        if (user.role === 'admin' || user.isPermanent) {
            tokenText.textContent = 'Không giới hạn';
            tokenBadge.className = 'cp-token-badge';
            return;
        }

        myTokenQuota = user.tokenQuota || 20000;
        myBonusTokens = user.bonusTokens || 0;
        myTokensUsed = user.tokensUsed || 0;
        
        renderTokenUI();
    }

    function renderTokenUI() {
        if (currentUser && (currentUser.role === 'admin' || currentUser.isPermanent)) return;

        var totalAvailable = myTokenQuota + myBonusTokens;
        var remain = totalAvailable - myTokensUsed;
        if (remain < 0) remain = 0;

        tokenText.textContent = remain.toLocaleString('vi-VN') + ' token';
        
        tokenBadge.classList.remove('warn', 'danger');
        if (remain <= 2000) tokenBadge.classList.add('danger');
        else if (remain <= 5000) tokenBadge.classList.add('warn');

        if (remain <= 0) {
            startBtn.style.display = 'none';
            buyTokenBtn.style.display = 'flex';
            inputArea.disabled = true;
            inputArea.placeholder = 'Bạn đã hết lượt dịch. Vui lòng mua thêm token.';
        } else {
            startBtn.style.display = 'flex';
            buyTokenBtn.style.display = 'none';
            inputArea.disabled = false;
            inputArea.placeholder = currentMode === 'vi2zh' ? 'Nhập văn bản tiếng Việt vào đây... (tối đa 5000 ký tự)' : 'Dán văn bản tiếng Trung vào đây... (tối đa 5000 ký tự)';
        }
    }

    buyTokenBtn.addEventListener('click', function() {
        if (typeof openRenewalModal === 'function') {
            openRenewalModal();
        } else {
            alert('Vui lòng liên hệ Admin để mua thêm Token!');
        }
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

    // ⭐ HÀM QUÉT VÀ HIỂN THỊ GỢI Ý CHÍNH TẢ TRỰC QUAN
    function checkSpellingSuggestions() {
        if (currentMode !== 'vi2zh') {
            spellContainer.classList.remove('show');
            return;
        }

        var text = inputArea.value;
        // Tách các từ đơn lẻ theo khoảng trắng và dấu câu
        var words = text.match(/\b[A-Za-zÀ-ỹ]+\b/g) || [];
        var foundTypos = {};

        for (var i = 0; i < words.length; i++) {
            var w = words[i].toLowerCase();
            if (commonTyposVi[w]) {
                foundTypos[w] = commonTyposVi[w];
            }
        }

        var keys = Object.keys(foundTypos);
        if (keys.length > 0) {
            spellChips.innerHTML = '';
            keys.forEach(function(wrongWord) {
                var correctWord = foundTypos[wrongWord];
                var chip = document.createElement('div');
                chip.className = 'cp-spell-chip';
                chip.innerHTML = '<i class="fas fa-magic"></i> "' + wrongWord + '" ➜ <b>' + correctWord + '</b>';
                
                // Khi bấm vào chip, tự động thay thế từ sai thành từ đúng trong textarea
                chip.addEventListener('click', function() {
                    var regex = new RegExp('\\b' + wrongWord + '\\b', 'gi');
                    inputArea.value = inputArea.value.replace(regex, correctWord);
                    updateCharCount();
                    checkSpellingSuggestions(); // Cập nhật lại danh sách gợi ý
                });
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
        checkSpellingSuggestions(); // Quét lỗi chính tả mỗi khi gõ
    }

    inputArea.addEventListener('input', updateCharCount);
    setTimeout(autoResizeTextarea, 100);

    switchBtn.addEventListener('click', function() {
        if (currentMode === 'vi2zh') {
            currentMode = 'zh2vi';
            labelVi.classList.remove('active');
            labelZh.classList.add('active');
            spellContainer.classList.remove('show');
            if (!inputArea.disabled) inputArea.placeholder = 'Dán văn bản tiếng Trung vào đây... (tối đa 5000 ký tự)';
        } else {
            currentMode = 'zh2vi';
            labelZh.classList.remove('active');
            labelVi.classList.add('active');
            if (!inputArea.disabled) inputArea.placeholder = 'Nhập văn bản tiếng Việt vào đây... (tối đa 5000 ký tự)';
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
        if (currentUser.role !== 'admin' && !currentUser.isPermanent && (myTokenQuota + myBonusTokens - myTokensUsed <= 0)) { 
            alert('Bạn đã hết token!'); 
            return; 
        }

        var rawText = inputArea.value.trim();
        if (!rawText) { alert('Vui lòng nhập văn bản!'); return; }

        startBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Đang xử lý...';
        startBtn.disabled = true;
        switchBtn.style.pointerEvents = 'none';
        progressWrap.classList.add('show');
        progressBar.style.width = '0%';

        var sentences = smartSplit(rawText, currentMode);
        if (sentences.length === 0) {
            alert('Không tìm thấy câu hợp lệ!');
            startBtn.innerHTML = '<i class="fas fa-rocket"></i> Bắt đầu luyện tập';
            startBtn.disabled = false;
            switchBtn.style.pointerEvents = 'auto';
            progressWrap.classList.remove('show');
            return;
        }

        await loadPinyinPro();

        var total = sentences.length;
        var translatedCount = 0;
        var customData = [];
        var totalTokensThisSession = 0;

        for (var b = 0; b < total; b += BATCH_SIZE) {
            var batchEnd = Math.min(b + BATCH_SIZE, total);
            var batchSentences = sentences.slice(b, batchEnd);

            var promises = batchSentences.map(function(sentence, idx) {
                return fetchTranslate(sentence, currentMode).then(function(data) {
                    totalTokensThisSession += (data.tokensUsed || 0);
                    customData.push({
                        stt: String(b + idx + 1),
                        zh: currentMode === 'vi2zh' ? data.translated : sentence,
                        vi: currentMode === 'vi2zh' ? sentence : data.translated,
                        pinyin: data.pinyin || '',
                        hsk: 'HSK1',
                        topic: 'Văn bản tự do',
                        subject: 'Custom'
                    });
                    translatedCount++;
                    var pct = Math.round((translatedCount / total) * 100);
                    progressBar.style.width = pct + '%';
                    progressText.textContent = 'Đang dịch: ' + translatedCount + ' / ' + total + ' câu (' + pct + '%)';
                }).catch(function(err) {
                    customData.push({
                        stt: String(b + idx + 1),
                        zh: currentMode === 'vi2zh' ? '[Lỗi]' : sentence,
                        vi: currentMode === 'vi2zh' ? sentence : '[Lỗi]',
                        pinyin: '',
                        hsk: 'HSK1',
                        topic: 'Văn bản tự do',
                        subject: 'Custom'
                    });
                    translatedCount++;
                });
            });

            await Promise.all(promises);
            if (batchEnd < total) await new Promise(function(r) { setTimeout(r, 500); });
        }

        customData.sort(function(a, b) { return parseInt(a.stt) - parseInt(b.stt); });

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

        startBtn.innerHTML = '<i class="fas fa-rocket"></i> Bắt đầu luyện tập';
        startBtn.disabled = false;
        switchBtn.style.pointerEvents = 'auto';
        setTimeout(function() { progressWrap.classList.remove('show'); }, 1500);
    });

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

    function getSmartPinyin(text) {
        if (!window.pinyinPro || !text) return '';
        if (typeof Intl !== 'undefined' && Intl.Segmenter) {
            try {
                var segmenter = new Intl.Segmenter('zh', { granularity: 'word' });
                var segs = segmenter.segment(text);
                var resultWords = [];
                for (var seg of segs) {
                    var segmentStr = seg.segment;
                    if (/[\u4e00-\u9fa5]/.test(segmentStr)) {
                        var pinyinWord = window.pinyinPro.pinyin(segmentStr, { toneType: 'symbol', separator: '' });
                        resultWords.push(pinyinWord);
                    } else {
                        resultWords.push(segmentStr);
                    }
                }
                return resultWords.join(' ');
            } catch (e) {
                console.warn('[Pinyin] Intl.Segmenter fallback:', e);
            }
        }
        return window.pinyinPro.pinyin(text, { toneType: 'symbol' });
    }

    async function fetchTranslate(text, mode) {
        var translated = '';
        var pinyin = '';
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

            var zhTextForPinyin = (mode === 'zh2vi') ? text : translated; 
            if (window.pinyinPro && zhTextForPinyin) {
                pinyin = getSmartPinyin(zhTextForPinyin);
            }
            
        } catch(e) {
            console.warn('[CP] Translate error:', e.message);
            translated = '[Lỗi: ' + e.message + ']'; 
        }
        
        return { translated: translated, pinyin: pinyin, tokensUsed: tokensUsed };
    }

    setTimeout(initTokenState, 100);
    setTimeout(initTokenState, 1500);

})();
"""

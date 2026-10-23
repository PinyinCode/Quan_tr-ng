# -*- coding: utf-8 -*-
r"""
custom_practice_module.py - Khu vực Luyện tập Tự do (Responsive tối ưu màn hình lớn/nhỏ)
Hỗ trợ: Dịch 2 chiều, nhận diện số chuẩn, từ ghép Pinyin, UI Glassmorphism hiện đại.
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
    transition: all 0.3s ease;
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
    letter-spacing: -0.3px;
}

.cp-title-group p {
    font-size: 0.8rem;
    color: var(--text-3, #64748b);
    margin: 2px 0 0 0;
}

.cp-btn-reset {
    padding: 0.45rem 0.9rem;
    border-radius: 50px;
    border: 1px solid var(--border, #e2e8f0);
    background: var(--surface, #ffffff);
    color: var(--text-3, #64748b);
    font-size: 0.75rem;
    font-weight: 700;
    font-family: inherit;
    cursor: pointer;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    box-shadow: 0 2px 6px rgba(0,0,0,0.02);
}

.cp-btn-reset:hover {
    background: #fee2e2;
    color: #ef4444;
    border-color: #fca5a5;
    transform: translateY(-1px);
}

/* Hàng chọn chế độ (Switch Pill) */
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
    transition: all 0.3s;
}

.cp-switch-container:hover {
    border-color: #a855f7;
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
    box-shadow: 0 4px 12px rgba(124,58,237,0.3);
    transition: transform 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    margin: 0 6px;
}

.cp-switch-container:hover .cp-switch-icon-box {
    transform: rotate(180deg);
}

/* Ô nhập liệu */
.cp-input-wrapper {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
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
    overflow-y: hidden;
    min-height: 120px;
    max-height: 400px;
    transition: all 0.25s ease;
    line-height: 1.6;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.02) inset;
}

.cp-textarea:focus {
    border-color: #a855f7;
    outline: none;
    box-shadow: 0 0 0 4px rgba(168, 85, 247, 0.15), 0 4px 20px rgba(0, 0, 0, 0.02) inset;
}

.cp-char-count {
    font-size: 0.75rem;
    color: var(--text-3, #64748b);
    text-align: right;
    font-weight: 600;
}

.cp-char-count.over {
    color: #ef4444;
    font-weight: 700;
}

/* Nút Bắt đầu - Responsive thông minh */
.cp-btn-start {
    width: 100%; /* Mặc định trên mobile chiếm hết chiều ngang */
    height: 52px;
    border-radius: 16px;
    border: none;
    background: linear-gradient(135deg, #4f46e5, #7c3aed, #ec4899);
    background-size: 200% auto;
    color: #fff;
    font-weight: 800;
    font-size: 1.05rem;
    cursor: pointer;
    transition: all 0.4s ease;
    font-family: inherit;
    box-shadow: 0 8px 25px rgba(124, 58, 237, 0.35);
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.6rem;
    padding: 0 2rem;
}

.cp-btn-start:hover:not(:disabled) {
    background-position: right center;
    transform: translateY(-2px);
    box-shadow: 0 12px 30px rgba(124, 58, 237, 0.5);
}

.cp-btn-start:disabled {
    opacity: 0.7;
    cursor: not-allowed;
    transform: none;
}

/* Tối ưu riêng cho màn hình lớn (Desktop từ 768px trở lên) */
@media (min-width: 768px) {
    .cp-btn-start {
        width: auto;           /* Không bị kéo dãn hết cỡ */
        min-width: 280px;      /* Giữ độ rộng tối thiểu vừa mắt */
        align-self: flex-end;  /* Căn lề sang phải cực kỳ sang trọng và cân đối */
    }
}

/* Thanh tiến trình */
.cp-progress-wrap {
    display: none;
    flex-direction: column;
    gap: 0.6rem;
    background: var(--surface-2, #f1f5f9);
    padding: 1rem;
    border-radius: 14px;
    border: 1px solid var(--border, #e2e8f0);
}

.cp-progress-wrap.show {
    display: flex;
    animation: fadeIn 0.3s ease;
}

.cp-progress-text {
    font-size: 0.8rem;
    color: var(--text, #1e1b4b);
    text-align: center;
    font-weight: 700;
}

.cp-progress-bar-bg {
    width: 100%;
    height: 10px;
    background: var(--surface, #ffffff);
    border-radius: 50px;
    overflow: hidden;
    border: 1px solid var(--border, #e2e8f0);
}

.cp-progress-bar {
    height: 100%;
    width: 0%;
    background: linear-gradient(90deg, #6366f1, #a855f7, #ec4899);
    transition: width 0.3s ease;
    border-radius: 50px;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(5px); }
    to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 500px) {
    .cp-card { padding: 1.25rem; border-radius: 20px; }
    .cp-title-group h3 { font-size: 1.05rem; }
    .cp-textarea { min-height: 100px; font-size: 0.95rem; }
    .cp-btn-start { height: 48px; font-size: 1rem; }
}
"""

def build_custom_practice_html():
    return r"""
<div class="cp-card" id="cpSection">
    <div class="cp-header-row">
        <div class="cp-section-header">
            <div class="cp-icon-badge">
                <i class="fas fa-wand-magic-sparkles"></i>
            </div>
            <div class="cp-title-group">
                <h3>Luyện Dịch Tự Do</h3>
                <p>Nhập văn bản bất kỳ để luyện tập</p>
            </div>
        </div>
        <button class="cp-btn-reset" id="cpResetBtn" type="button" title="Làm mới">
            <i class="fas fa-rotate-right"></i> Làm mới
        </button>
    </div>

    <!-- Hàng chuyển đổi chế độ kiểu Pill Switch -->
    <div class="cp-switch-container" id="cpSwitchBtn" title="Đảo chiều dịch">
        <span class="cp-switch-label active" id="cpLabelVi">Tiếng Việt</span>
        <div class="cp-switch-icon-box">
            <i class="fas fa-exchange-alt"></i>
        </div>
        <span class="cp-switch-label" id="cpLabelZh">Tiếng Trung</span>
    </div>

    <!-- Ô nhập liệu -->
    <div class="cp-input-wrapper">
        <textarea class="cp-textarea" id="cpInputZh" rows="4"
            placeholder="Nhập văn bản tiếng Việt vào đây... (tối đa 5000 ký tự)"></textarea>
        <div class="cp-char-count" id="cpCharCount">0 / 5000</div>
    </div>

    <!-- Nút Bắt đầu -->
    <button class="cp-btn-start" id="cpStartBtn" type="button">
        <i class="fas fa-rocket"></i> Bắt đầu luyện tập
    </button>

    <!-- Thanh tiến trình xử lý -->
    <div class="cp-progress-wrap" id="cpProgressWrap">
        <div class="cp-progress-text" id="cpProgressText">Đang xử lý...</div>
        <div class="cp-progress-bar-bg">
            <div class="cp-progress-bar" id="cpProgressBar"></div>
        </div>
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

    var WORKER_URL = 'https://tiny-fire-f000.hoanginvest199.workers.dev';

    var inputArea = document.getElementById('cpInputZh');
    var charCount = document.getElementById('cpCharCount');
    var startBtn = document.getElementById('cpStartBtn');
    var resetBtn = document.getElementById('cpResetBtn');
    
    var switchBtn = document.getElementById('cpSwitchBtn');
    var labelZh = document.getElementById('cpLabelZh');
    var labelVi = document.getElementById('cpLabelVi');
    
    var progressWrap = document.getElementById('cpProgressWrap');
    var progressBar = document.getElementById('cpProgressBar');
    var progressText = document.getElementById('cpProgressText');

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
    }
    inputArea.addEventListener('input', updateCharCount);
    setTimeout(autoResizeTextarea, 100);

    switchBtn.addEventListener('click', function() {
        if (currentMode === 'vi2zh') {
            currentMode = 'zh2vi';
            labelVi.classList.remove('active');
            labelZh.classList.add('active');
            inputArea.placeholder = 'Dán văn bản tiếng Trung vào đây... (tối đa 5000 ký tự)';
        } else {
            currentMode = 'vi2zh';
            labelZh.classList.remove('active');
            labelVi.classList.add('active');
            inputArea.placeholder = 'Nhập văn bản tiếng Việt vào đây... (tối đa 5000 ký tự)';
        }
        inputArea.value = '';
        updateCharCount();
    });

    resetBtn.addEventListener('click', function() {
        inputArea.value = '';
        updateCharCount();
        progressWrap.classList.remove('show');
        startBtn.disabled = false;
        startBtn.innerHTML = '<i class="fas fa-rocket"></i> Bắt đầu luyện tập';
        setTimeout(autoResizeTextarea, 50);
        
        if (window.__customPracticeActive) {
            window.__customPracticeActive = false;
            if (typeof DATASET_REGISTRY !== 'undefined' && DATASET_REGISTRY['tonghop']) {
                if (typeof window.__switchRawData === 'function') window.__switchRawData('tonghop');
                if (typeof buildFilters === 'function') buildFilters();
                if (typeof applyFilter === 'function') applyFilter();
                if (typeof updateResultCount === 'function') updateResultCount();
            }
        }
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
        var rawText = inputArea.value.trim();
        if (!rawText) {
            alert('Vui lòng nhập văn bản!');
            return;
        }

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

        for (var b = 0; b < total; b += BATCH_SIZE) {
            var batchEnd = Math.min(b + BATCH_SIZE, total);
            var batchSentences = sentences.slice(b, batchEnd);

            var promises = batchSentences.map(function(sentence, idx) {
                return fetchTranslate(sentence, currentMode).then(function(data) {
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

        if (typeof window.activateCustomPracticeMode === 'function') {
            window.activateCustomPracticeMode(customData);
        } else {
            if (typeof RAW_DATA !== 'undefined') RAW_DATA = customData;
            if (typeof filtered !== 'undefined') filtered = customData;
            window.__customPracticeActive = true;
            window.__onboardingOverride = null;
            if (typeof state !== 'undefined' && state) {
                state.search = ''; state.hsk = ''; state.subject = '';
            }
            if (typeof buildFilters === 'function') buildFilters();
            if (typeof applyFilter === 'function') applyFilter();
            if (typeof updateResultCount === 'function') updateResultCount();
            if (typeof render === 'function') render(true);
        }

        startBtn.innerHTML = '<i class="fas fa-rocket"></i> Bắt đầu luyện tập';
        startBtn.disabled = false;
        switchBtn.style.pointerEvents = 'auto';
        setTimeout(function() {
            progressWrap.classList.remove('show');
        }, 1500);
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

    async function fetchTranslate(text, mode) {
        var translated = '';
        var pinyin = '';
        var zhTextForPinyin = '';

        try {
            var source = mode === 'zh2vi' ? 'zh-CN' : 'vi';
            var target = mode === 'zh2vi' ? 'vi' : 'zh-CN';
            
            var controller = new AbortController();
            var timeoutId = setTimeout(function() { controller.abort(); }, 10000);

            var res = await fetch(WORKER_URL, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: text, source: source, target: target }),
                signal: controller.signal
            });
            
            clearTimeout(timeoutId);
            if (!res.ok) throw new Error('HTTP ' + res.status);
            
            var json = await res.json();
            if (json.error) throw new Error(json.error);
            
            translated = json.translated;

            if (mode === 'zh2vi') {
                zhTextForPinyin = text; 
            } else {
                zhTextForPinyin = translated; 
            }

            if (window.pinyinPro && zhTextForPinyin) {
                pinyin = window.pinyinPro.pinyin(zhTextForPinyin, { toneType: 'symbol' });
            }
            
        } catch(e) {
            console.warn('[CP] Translate Proxy error:', e.message);
            translated = '[Lỗi: ' + e.message + ']'; 
        }
        
        return { translated: translated, pinyin: pinyin };
    }
})();
"""

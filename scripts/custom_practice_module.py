# -*- coding: utf-8 -*-
r"""
custom_practice_module.py - Khu vực Luyện tập Tự do (Giao diện chủ lực)
Hỗ trợ: Dịch 2 chiều (gộp nút), nhận diện số chuẩn, từ ghép Pinyin, UI tinh gọn.
"""

def build_custom_practice_css():
    return r"""
/* ═══════════════════════════════════════════════════════════ */
/* KHU VỰC LUYỆN TẬP TỰ DO - TINH GỌN & TỐI ƯU               */
/* ═══════════════════════════════════════════════════════════ */
.cp-section {
    background: transparent;
    border: none;
    border-radius: 0;
    padding: 0;
    margin-bottom: 1.5rem;
    display: flex;
    flex-direction: column;
    gap: 1rem;
    position: relative;
}

.cp-header-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    margin-bottom: 0.5rem;
}

.cp-section-header {
    display: flex;
    align-items: center;
    gap: 8px; 
}
.cp-section-header i {
    color: #fff;
    font-size: 0.85rem;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 28px;
    height: 28px;
    border-radius: 50%;
    background: linear-gradient(135deg, #6366f1, #a855f7);
    box-shadow: 0 3px 8px rgba(168,85,247,0.3);
}
.cp-section-header span {
    font-size: 1.1rem;
    font-weight: 800;
    background: linear-gradient(90deg, #1e1b4b, #4c1d95);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -0.3px;
}

.cp-btn-reset {
    padding: .3rem .7rem;
    border-radius: 50px;
    border: 1px solid var(--border);
    background: var(--surface);
    color: var(--text-3);
    font-size: .75rem;
    font-weight: 700;
    font-family: inherit;
    cursor: pointer;
    transition: all .2s;
    display: inline-flex;
    align-items: center;
    gap: .3rem;
}
.cp-btn-reset:hover {
    background: #fee2e2;
    color: #ef4444;
    border-color: #fca5a5;
}

/* Ô nhập liệu */
.cp-input-wrapper {
    display: flex;
    flex-direction: column;
    gap: .4rem;
}
.cp-textarea {
    width: 100%;
    padding: 1.2rem 1rem; /* Tăng padding trên dưới cho thoáng */
    border-radius: 14px;
    border: 1.5px solid var(--border);
    background: var(--surface);
    color: var(--text);
    font-family: var(--font-zh);
    font-size: 1.05rem;
    resize: none;
    overflow-y: hidden;
    min-height: 120px; /* Tăng chiều cao mặc định lên 120px */
    max-height: 400px;
    transition: height 0.1s ease, border-color .2s, box-shadow .2s;
    line-height: 1.6;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.02);
}
.cp-textarea:focus {
    border-color: #a855f7;
    outline: none;
    box-shadow: 0 0 0 4px rgba(168,85,247,.15);
}
.cp-char-count {
    font-size: .75rem;
    color: var(--text-3);
    text-align: right;
    font-weight: 600;
}
.cp-char-count.over {
    color: var(--danger);
    font-weight: 700;
}

/* Hàng chứa Nút chuyển đổi và Nút Bắt đầu */
.cp-action-row {
    display: flex;
    align-items: center;
    gap: 12px;
    width: 100%;
}

/* Nút chuyển đổi thu nhỏ */
.cp-switch-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--surface-2);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 0 1rem;
    height: 48px; /* Bằng chiều cao nút Start */
    cursor: pointer;
    user-select: none;
    transition: all .2s;
    color: var(--primary);
    font-weight: 700;
    font-size: 0.9rem;
    gap: 8px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.02);
    flex-shrink: 0; /* Không bị co lại */
}
.cp-switch-btn:hover {
    background: var(--surface);
    border-color: var(--primary);
}
.cp-switch-btn i {
    transition: transform .4s ease;
}
.cp-switch-btn:hover i {
    transform: rotate(180deg);
}

/* Nút Bắt đầu chiếm phần còn lại */
.cp-btn-start {
    flex: 1; /* Tự động giãn hết phần còn lại */
    height: 48px;
    border-radius: 12px;
    border: none;
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    color: #fff;
    font-weight: 800;
    font-size: 1rem;
    cursor: pointer;
    transition: all .25s;
    font-family: inherit;
    box-shadow: 0 4px 15px rgba(124,58,237,.3);
    display: flex;
    align-items: center;
    justify-content: center;
    gap: .5rem;
}
.cp-btn-start:hover:not(:disabled) { 
    transform: translateY(-2px); 
    box-shadow: 0 6px 20px rgba(124,58,237,.5); 
}
.cp-btn-start:disabled { 
    opacity: 0.7; 
    cursor: not-allowed; 
    transform: none;
}

/* Thanh tiến trình */
.cp-progress-wrap {
    display: none;
    flex-direction: column;
    gap: .5rem;
    background: var(--surface-2);
    padding: .8rem 1rem;
    border-radius: 12px;
    border: 1px solid var(--border);
}
.cp-progress-wrap.show { display: flex; }
.cp-progress-text {
    font-size: .8rem;
    color: var(--text);
    text-align: center;
    font-weight: 700;
}
.cp-progress-bar-bg {
    width: 100%;
    height: 8px;
    background: var(--surface);
    border-radius: 50px;
    overflow: hidden;
    border: 1px solid var(--border);
}
.cp-progress-bar {
    height: 100%;
    width: 0%;
    background: linear-gradient(90deg, #6366f1, #a855f7, #ec4899);
    transition: width .3s ease;
    border-radius: 50px;
}

@media (max-width: 500px) {
    .cp-switch-btn { padding: 0 0.6rem; font-size: 0.8rem; }
    .cp-btn-start { font-size: .9rem; }
    .cp-textarea { min-height: 100px; }
}
"""

def build_custom_practice_html():
    return r"""
<div class="cp-section" id="cpSection">
    <div class="cp-header-row">
        <div class="cp-section-header">
            <i class="fas fa-pen-fancy"></i>
            <span>Luyện Dịch Tự Do</span>
        </div>
        <button class="cp-btn-reset" id="cpResetBtn" type="button" title="Làm mới">
            <i class="fas fa-trash-alt"></i> Xóa
        </button>
    </div>

    <div class="cp-input-wrapper">
        <textarea class="cp-textarea" id="cpInputZh" rows="4"
            placeholder="Dán văn bản tiếng Trung vào đây... (tối đa 5000 ký tự)"></textarea>
        <div class="cp-char-count" id="cpCharCount">0 / 5000</div>
    </div>

    <!-- Hàng chứa Nút đổi chiều và Nút Bắt đầu -->
    <div class="cp-action-row">
        <div class="cp-switch-btn" id="cpSwitchBtn" title="Đảo chiều dịch">
            <span id="cpLabelZh" style="color: var(--text);">Trung</span>
            <i class="fas fa-exchange-alt"></i>
            <span id="cpLabelVi">Việt</span>
        </div>
        <button class="cp-btn-start" id="cpStartBtn" type="button">
            <i class="fas fa-rocket"></i> Bắt đầu
        </button>
    </div>

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
    var currentMode = 'zh2vi';

    // ĐƯỜNG LINK CLOUDFLARE WORKER
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

    // Đổi chiều dịch
    switchBtn.addEventListener('click', function() {
        if (currentMode === 'zh2vi') {
            currentMode = 'vi2zh';
            labelZh.style.color = 'var(--text-3)';
            labelVi.style.color = 'var(--text)';
            inputArea.placeholder = 'Nhập văn bản tiếng Việt vào đây... (tối đa 5000 ký tự)';
        } else {
            currentMode = 'zh2vi';
            labelVi.style.color = 'var(--text-3)';
            labelZh.style.color = 'var(--text)';
            inputArea.placeholder = 'Dán văn bản tiếng Trung vào đây... (tối đa 5000 ký tự)';
        }
        inputArea.value = '';
        updateCharCount();
    });

    resetBtn.addEventListener('click', function() {
        inputArea.value = '';
        updateCharCount();
        progressWrap.classList.remove('show');
        startBtn.disabled = false;
        startBtn.innerHTML = '<i class="fas fa-rocket"></i> Bắt đầu';
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
        // Bảo vệ dấu chấm trong số (1.400)
        var protectedText = text.replace(/(\d)\.(\d)/g, '$1__DOT__$2');
        
        // Tách câu dựa trên dấu kết thúc
        var rawParts = protectedText.split(/(?<=[.!?。！？\n])/g);
        var result = [];
        
        for (var i = 0; i < rawParts.length; i++) {
            var s = rawParts[i].replace(/__DOT__/g, '.').trim();
            if (s.length === 0) continue;
            
            if (mode === 'zh2vi') {
                if (!/[\u4e00-\u9fa5]/.test(s)) continue; 
            } else {
                // Chỉ dịch câu có chứa chữ cái tiếng Việt, bỏ qua câu chỉ có số/ký tự
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
            startBtn.innerHTML = '<i class="fas fa-rocket"></i> Bắt đầu';
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
 Promise                state.search = ''; state.hsk = ''; state.subject = '';
            }
            if (typeof buildFilters === 'function') buildFilters();
            if (typeof applyFilter === 'function') applyFilter();
            if (typeof updateResultCount === 'function') updateResultCount();
            if (typeof render === 'function') render(true);
        }

        startBtn.innerHTML = '<i class="fas fa-rocket"></i> Bắt đầu';
        startBtn.disabled = false;
        switchBtn.style.pointerEvents = 'auto';
        setTimeout(function() {
            progressWrap.classList.remove('show');
        }, 1500);
    });

    function loadPinyinPro() {
        if (window.pinyinPro) return Promise.resolve();
        return new(function(resolve) {
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

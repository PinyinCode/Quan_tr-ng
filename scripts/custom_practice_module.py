# -*- coding: utf-8 -*-
r"""
custom_practice_module.py - Khu vực Luyện tập Tự do (Hiển thị sẵn)
Hỗ trợ: Dịch 2 chiều, tự động giãn chiều cao, tự động chia nhỏ để dịch.
"""

def build_custom_practice_css():
    return r"""
/* ═══════════════════════════════════════════════════════════ */
/* HERO SECTION: KHU VỰC LUYỆN TẬP TỰ DO (NỔI BẬT)            */
/* ═══════════════════════════════════════════════════════════ */
.cp-section {
    position: relative;
    background: linear-gradient(145deg, var(--surface) 0%, #f8faff 100%);
    border: 2px solid transparent;
    background-clip: padding-box;
    border-radius: 24px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    box-shadow: 
        0 10px 40px -10px rgba(99, 102, 241, 0.15),
        0 4px 12px rgba(15, 23, 42, 0.03),
        inset 0 1px 0 rgba(255,255,255,0.8);
    display: flex;
    flex-direction: column;
    gap: 1rem;
    overflow: hidden;
}
[data-theme="dark"] .cp-section {
    background: linear-gradient(145deg, var(--surface) 0%, rgba(30, 41, 59, 0.8) 100%);
    box-shadow: 
        0 10px 40px -10px rgba(0, 0, 0, 0.4),
        inset 0 1px 0 rgba(255,255,255,0.05);
}

/* Hiệu ứng viền phát sáng (Glow) */
.cp-section::before {
    content: '';
    position: absolute;
    inset: -2px;
    border-radius: 24px;
    padding: 2px;
    background: linear-gradient(135deg, #6366f1, #a855f7, #ec4899, #6366f1);
    background-size: 300% 300%;
    -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
    -webkit-mask-composite: xor;
    mask-composite: exclude;
    z-index: -1;
    animation: borderGlow 6s linear infinite;
    opacity: 0.7;
}
@keyframes borderGlow {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Họa tiết nền chìm */
.cp-section::after {
    content: '';
    position: absolute;
    top: -50%; right: -20%;
    width: 300px; height: 300px;
    background: radial-gradient(circle, rgba(168,85,247,0.08) 0%, transparent 70%);
    border-radius: 50%;
    pointer-events: none;
    z-index: 0;
}

/* Header */
.cp-section-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: .5rem;
    position: relative;
    z-index: 1;
}
.cp-title-wrap {
    display: flex;
    align-items: center;
    gap: .6rem;
    font-size: 1.15rem;
    font-weight: 900;
    color: var(--text);
    letter-spacing: -0.02em;
}
.cp-title-wrap i {
    color: #fff;
    font-size: 1.1rem;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 38px;
    height: 38px;
    border-radius: 12px;
    background: linear-gradient(135deg, #6366f1, #a855f7);
    box-shadow: 0 4px 12px rgba(139, 92, 246, 0.4);
    flex-shrink: 0;
}

/* Nút đổi chiều */
.cp-switch-toggle {
    display: inline-flex;
    align-items: center;
    gap: .4rem;
    padding: .45rem 1rem;
    border-radius: 50px;
    border: 1.5px solid rgba(139, 92, 246, 0.2);
    background: rgba(139, 92, 246, 0.05);
    color: #7c3aed;
    font-size: .78rem;
    font-weight: 800;
    font-family: inherit;
    cursor: pointer;
    transition: all .25s cubic-bezier(.34,1.56,.64,1);
    position: relative;
    z-index: 1;
}
.cp-switch-toggle:hover {
    background: rgba(139, 92, 246, 0.15);
    border-color: rgba(139, 92, 246, 0.4);
    transform: scale(1.03);
}
.cp-switch-toggle i { font-size: .8rem; transition: transform .3s; }
.cp-switch-toggle.mode-vi2zh i { transform: rotate(180deg); }
[data-theme="dark"] .cp-switch-toggle { color: #c4b5fd; border-color: rgba(196,181,253,.3); }

/* Ô nhập liệu */
.cp-input-wrapper {
    display: flex;
    flex-direction: column;
    gap: .4rem;
    position: relative;
    z-index: 1;
}
.cp-textarea {
    width: 100%;
    padding: 1rem 1.15rem;
    border-radius: 16px;
    border: 2px solid rgba(139, 92, 246, 0.15);
    background: var(--surface);
    color: var(--text);
    font-family: var(--font-zh);
    font-size: 1.05rem;
    resize: none;
    overflow-y: hidden;
    min-height: 54px;
    max-height: 350px;
    transition: all 0.2s ease;
    line-height: 1.6;
    box-shadow: 0 2px 8px rgba(0,0,0,0.02);
}
.cp-textarea:focus {
    border-color: #8b5cf6;
    outline: none;
    box-shadow: 0 0 0 4px rgba(139, 92, 246, 0.15), 0 4px 12px rgba(139, 92, 246, 0.1);
    background: var(--surface);
}
.cp-textarea::placeholder {
    color: var(--text-3);
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    font-size: .95rem;
}
.cp-char-count {
    font-size: .72rem;
    color: var(--text-3);
    text-align: right;
    padding-right: .5rem;
    font-weight: 600;
}
.cp-char-count.over {
    color: var(--danger);
    font-weight: 800;
}

/* Nút Bắt đầu */
.cp-btn-start {
    padding: 1rem;
    border-radius: 16px;
    border: none;
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 50%, #c026d3 100%);
    background-size: 200% auto;
    color: #fff;
    font-weight: 900;
    font-size: 1.05rem;
    cursor: pointer;
    transition: all 0.3s cubic-bezier(.34,1.56,.64,1);
    font-family: inherit;
    box-shadow: 0 8px 24px -6px rgba(124, 58, 237, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    gap: .6rem;
    position: relative;
    z-index: 1;
    overflow: hidden;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}
.cp-btn-start::before {
    content: '';
    position: absolute;
    top: 0; left: -100%;
    width: 100%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.25), transparent);
    transition: left 0.6s ease;
}
.cp-btn-start:hover:not(:disabled) { 
    background-position: right center;
    transform: translateY(-3px);
    box-shadow: 0 12px 28px -6px rgba(124, 58, 237, 0.7);
}
.cp-btn-start:hover:not(:disabled)::before { left: 100%; }
.cp-btn-start:active:not(:disabled) { transform: translateY(1px) scale(0.98); }
.cp-btn-start:disabled { 
    opacity: 0.7; 
    cursor: not-allowed; 
    background: var(--text-3);
    box-shadow: none;
    transform: none;
}

/* Thanh tiến trình */
.cp-progress-wrap {
    display: none;
    flex-direction: column;
    gap: .4rem;
    position: relative;
    z-index: 1;
    background: var(--surface-2);
    padding: .75rem;
    border-radius: 12px;
    border: 1px solid var(--border);
}
.cp-progress-wrap.show { display: flex; }
.cp-progress-text {
    font-size: .8rem;
    color: var(--primary);
    text-align: center;
    font-weight: 800;
    letter-spacing: 0.02em;
}
.cp-progress-bar-bg {
    width: 100%;
    height: 8px;
    background: rgba(139, 92, 246, 0.15);
    border-radius: 50px;
    overflow: hidden;
}
.cp-progress-bar {
    height: 100%;
    width: 0%;
    background: linear-gradient(90deg, #6366f1, #a855f7);
    transition: width .3s ease;
    border-radius: 50px;
    box-shadow: 0 0 10px rgba(168,85,247,0.5);
}

/* Responsive */
@media (max-width: 500px) {
    .cp-section { padding: 1.15rem; border-radius: 20px; margin-bottom: 1rem; }
    .cp-title-wrap { font-size: 1.05rem; }
    .cp-title-wrap i { width: 32px; height: 32px; font-size: .95rem; }
    .cp-switch-toggle { font-size: .7rem; padding: .35rem .75rem; }
    .cp-textarea { font-size: .95rem; padding: .85rem; }
    .cp-btn-start { font-size: .95rem; padding: .85rem; }
}
"""

def build_custom_practice_html():
    return r"""
<div class="cp-section" id="cpSection">
    <div class="cp-section-header">
        <div class="cp-title-wrap">
            <i class="fas fa-pen-fancy"></i>
            <span>Luyện tập văn bản tự do</span>
        </div>
        <button class="cp-switch-toggle" id="cpSwitchBtn" type="button" title="Đổi chiều dịch">
            <i class="fas fa-arrow-right"></i>
            <span id="cpSwitchLabel">Trung → Việt</span>
        </button>
    </div>

    <div class="cp-input-wrapper">
        <textarea class="cp-textarea" id="cpInputZh" rows="1"
            placeholder="Dán văn bản tiếng Trung hoặc nhập tiếng Việt (mỗi câu kết thúc bằng dấu chấm)..."></textarea>
        <div class="cp-char-count" id="cpCharCount">0 / 5000</div>
    </div>

    <button class="cp-btn-start" id="cpStartBtn" type="button">
        <i class="fas fa-play"></i> Bắt đầu luyện tập
    </button>

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

    var inputArea = document.getElementById('cpInputZh');
    var charCount = document.getElementById('cpCharCount');
    var startBtn = document.getElementById('cpStartBtn');
    var switchBtn = document.getElementById('cpSwitchBtn');
    var switchLabel = document.getElementById('cpSwitchLabel');
    var progressWrap = document.getElementById('cpProgressWrap');
    var progressBar = document.getElementById('cpProgressBar');
    var progressText = document.getElementById('cpProgressText');

    // ⭐ 1. TỰ ĐỘNG GIÃN CHIỀU CAO
    function autoResizeTextarea() {
        inputArea.style.height = 'auto';
        var newHeight = inputArea.scrollHeight;
        var maxHeight = 350;
        if (newHeight > maxHeight) {
            inputArea.style.height = maxHeight + 'px';
            inputArea.style.overflowY = 'auto';
        } else {
            inputArea.style.height = newHeight + 'px';
            inputArea.style.overflowY = 'hidden';
        }
    }

    // ⭐ 2. ĐẾM KÝ TỰ
    function updateCharCount() {
        var len = inputArea.value.length;
        charCount.textContent = len + ' / ' + MAX_CHARS;
        
        if (len > MAX_CHARS) {
            charCount.classList.add('over');
            inputArea.value = inputArea.value.substring(0, MAX_CHARS);
            charCount.textContent = MAX_CHARS + ' / ' + MAX_CHARS + ' (Đã cắt bớt)';
        } else {
            charCount.classList.remove('over');
        }
        autoResizeTextarea();
    }
    inputArea.addEventListener('input', updateCharCount);
    setTimeout(autoResizeTextarea, 100);

    // ⭐ 3. CHUYỂN ĐỔI CHIỀU DỊCH
    switchBtn.addEventListener('click', function() {
        if (currentMode === 'zh2vi') {
            currentMode = 'vi2zh';
            switchLabel.textContent = 'Việt → Trung';
            switchBtn.classList.add('mode-vi2zh');
            inputArea.placeholder = 'Nhập văn bản tiếng Việt (mỗi câu kết thúc bằng dấu chấm)...';
        } else {
            currentMode = 'zh2vi';
            switchLabel.textContent = 'Trung → Việt';
            switchBtn.classList.remove('mode-vi2zh');
            inputArea.placeholder = 'Dán văn bản tiếng Trung hoặc nhập tiếng Việt (mỗi câu kết thúc bằng dấu chấm)...';
        }
        inputArea.value = '';
        updateCharCount();
    });

    // ⭐ 4. HÀM TÁCH CÂU THÔNG MINH (ĐÃ CẬP NHẬT THEO YÊU CẦU)
    function splitIntoSentences(text, mode) {
        var sentences = [];
        var hasChinese = /[\u4e00-\u9fa5]/.test(text);
        var actualMode = mode;
        if (mode === 'zh2vi' && !hasChinese) actualMode = 'vi2zh';
        if (mode === 'vi2zh' && hasChinese) actualMode = 'zh2vi';

        if (actualMode === 'zh2vi') {
            // Tách tiếng Trung
            var rawSentences = text.split(/(?<=[。！？!?\n])/g);
            rawSentences.forEach(function(s) {
                s = s.trim();
                if (s && /[\u4e00-\u9fa5]/.test(s)) sentences.push(s);
            });
        } else {
            // Tách tiếng Việt (Bảo vệ số thập phân, dấu chấm lửng, chữ viết tắt)
            var textForSplit = text;
            textForSplit = textForSplit.replace(/(\d)\.(\d)/g, '$1___DOT___$2');  // 0.2
            textForSplit = textForSplit.replace(/\.\.\./g, '___ELLIPSIS___');      // ...
            textForSplit = textForSplit.replace(/([A-Z])\.([A-Z])/g, '$1___DOT___$2'); // TP.HCM
            
            // Tách SAU dấu chấm câu và dấu xuống dòng
            var rawSentences = textForSplit.split(/(?<=[.!?\n])\s*/g);
            rawSentences.forEach(function(s) {
                s = s.trim();
                if (s) {
                    s = s.replace(/___DOT___/g, '.').replace(/___ELLIPSIS___/g, '...');
                    sentences.push(s);
                }
            });
        }

        // Chia nhỏ câu quá dài (> 5000 ký tự)
        var finalSentences = [];
        sentences.forEach(function(s) {
            if (s.length > MAX_SENTENCE_LENGTH) {
                var remaining = s;
                while (remaining.length > MAX_SENTENCE_LENGTH) {
                    var chunk = remaining.substring(0, MAX_SENTENCE_LENGTH);
                    var lastSpace = chunk.lastIndexOf(' ');
                    if (lastSpace === -1 || lastSpace < MAX_SENTENCE_LENGTH * 0.8) lastSpace = MAX_SENTENCE_LENGTH;
                    finalSentences.push(remaining.substring(0, lastSpace).trim());
                    remaining = remaining.substring(lastSpace).trim();
                }
                if (remaining.length > 0) finalSentences.push(remaining);
            } else {
                finalSentences.push(s);
            }
        });
        return finalSentences;
    }

    // ⭐ 5. NÚT BẮT ĐẦU
    startBtn.addEventListener('click', async function() {
        var rawText = inputArea.value.trim();
        if (!rawText) { alert('Vui lòng nhập văn bản!'); return; }

        var hasChinese = /[\u4e00-\u9fa5]/.test(rawText);
        if (currentMode === 'zh2vi' && !hasChinese) {
            currentMode = 'vi2zh';
            switchLabel.textContent = 'Việt → Trung';
            switchBtn.classList.add('mode-vi2zh');
        } else if (currentMode === 'vi2zh' && hasChinese) {
            currentMode = 'zh2vi';
            switchLabel.textContent = 'Trung → Việt';
            switchBtn.classList.remove('mode-vi2zh');
        }

        startBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Đang xử lý...';
        startBtn.disabled = true;
        progressWrap.classList.add('show');
        progressBar.style.width = '0%';

        var sentences = splitIntoSentences(rawText, currentMode);
        if (sentences.length === 0) {
            alert('Không tìm thấy câu hợp lệ!');
            startBtn.innerHTML = '<i class="fas fa-play"></i> Bắt đầu luyện tập';
            startBtn.disabled = false;
            progressWrap.classList.remove('show');
            return;
        }

        progressText.textContent = 'Tìm thấy ' + sentences.length + ' câu. Đang dịch...';
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
                        zh: currentMode === 'vi2zh' ? '[Lỗi dịch]' : sentence,
                        vi: currentMode === 'vi2zh' ? sentence : '[Lỗi dịch]',
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
            RAW_DATA = customData;
            filtered = customData;
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

        startBtn.innerHTML = '<i class="fas fa-play"></i> Bắt đầu luyện tập';
        startBtn.disabled = false;
        setTimeout(function() {
            progressWrap.classList.remove('show');
        }, 1500);
    });

    function loadPinyinPro() {
        if (window.pinyinPro) return Promise.resolve();
        return new Promise(function(resolve, reject) {
            var script = document.createElement('script');
            script.src = 'https://cdn.jsdelivr.net/npm/pinyin-pro@3.18.2/dist/index.min.js';
            script.onload = resolve;
            script.onerror = reject;
            document.head.appendChild(script);
        });
    }

    async function fetchTranslate(text, mode) {
        var translated = '';
        var pinyin = '';
        try {
            if (mode === 'zh2vi') {
                var gtRes = await fetch('https://translate.googleapis.com/translate_a/single?client=gtx&sl=zh-CN&tl=vi&dt=t&q=' + encodeURIComponent(text));
                var gtJson = await gtRes.json();
                translated = gtJson[0].map(function(item) { return item[0]; }).join('');
                if (window.pinyinPro) {
                    pinyin = window.pinyinPro.pinyin(text, { toneType: 'symbol' });
                }
            } else {
                var gtRes2 = await fetch('https://translate.googleapis.com/translate_a/single?client=gtx&sl=vi&tl=zh-CN&dt=t&q=' + encodeURIComponent(text));
                var gtJson2 = await gtRes2.json();
                translated = gtJson2[0].map(function(item) { return item[0]; }).join('');
                if (window.pinyinPro) {
                    pinyin = window.pinyinPro.pinyin(translated, { toneType: 'symbol' });
                }
            }
        } catch(e) {
            console.warn('[CP] Google Translate error:', e);
        }
        return { translated: translated, pinyin: pinyin };
    }
})();
"""

# -*- coding: utf-8 -*-
r"""
custom_practice_module.py - Khu vực Luyện tập Tự do (Hiển thị sẵn)
Tính năng:
- Dịch 2 chiều (Trung <-> Việt) qua Google Translate.
- Tự động tách câu thông minh, chia nhỏ câu quá dài.
- Tự động giãn chiều cao ô nhập liệu.
- Không giới hạn tổng ký tự (chỉ giới hạn mỗi câu 5000 ký tự).
- Tự động lấy Pinyin (từ ghép) qua pinyin-pro.
"""

def build_custom_practice_css():
    return r"""
/* ═══════════════════════════════════════════════════════════ */
/* KHU VỰC LUYỆN TẬP TỰ DO - GIAO DIỆN TINH TẾ                */
/* ═══════════════════════════════════════════════════════════ */
.cp-section {
    background: var(--surface);
    border: 1.5px solid var(--border);
    border-radius: 16px;
    padding: 1.25rem;
    margin-bottom: 1.25rem;
    box-shadow: var(--shadow-sm);
    display: flex;
    flex-direction: column;
    gap: 1rem;
    position: relative;
}

/* Header */
.cp-section-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: .5rem;
}
.cp-title-wrap {
    display: flex;
    align-items: center;
    gap: .5rem;
    font-size: 1rem;
    font-weight: 800;
    color: var(--text);
}
.cp-title-wrap i {
    color: var(--primary);
    font-size: 1.1rem;
}

/* Nút đổi chiều (Gộp 1 nút) */
.cp-switch-toggle {
    display: inline-flex;
    align-items: center;
    gap: .4rem;
    padding: .35rem .8rem;
    border-radius: 50px;
    border: 1.5px solid rgba(99, 102, 241, 0.2);
    background: rgba(99, 102, 241, 0.05);
    color: var(--primary);
    font-size: .75rem;
    font-weight: 800;
    font-family: inherit;
    cursor: pointer;
    transition: all .25s cubic-bezier(.34,1.56,.64,1);
}
.cp-switch-toggle:hover {
    background: rgba(99, 102, 241, 0.12);
    border-color: rgba(99, 102, 241, 0.4);
    transform: scale(1.03);
}
.cp-switch-toggle i {
    font-size: .8rem;
    transition: transform .3s;
}
.cp-switch-toggle.mode-vi2zh i {
    transform: rotate(180deg);
}

/* Ô nhập liệu */
.cp-input-wrapper {
    display: flex;
    flex-direction: column;
    gap: .4rem;
}
.cp-textarea {
    width: 100%;
    padding: .85rem 1rem;
    border-radius: 12px;
    border: 1.5px solid var(--border);
    background: var(--surface-2);
    color: var(--text);
    font-family: var(--font-zh);
    font-size: 1rem;
    resize: none;
    overflow-y: hidden;
    min-height: 52px;
    max-height: 350px;
    transition: all 0.2s ease;
    line-height: 1.5;
}
.cp-textarea:focus {
    border-color: var(--primary);
    outline: none;
    box-shadow: 0 0 0 3px rgba(37,99,235,.12);
    background: var(--surface);
}
.cp-char-count {
    font-size: .72rem;
    color: var(--text-3);
    text-align: right;
    padding-right: .2rem;
}

/* Nút Bắt đầu */
.cp-btn-start {
    padding: .75rem;
    border-radius: 12px;
    border: none;
    background: var(--primary);
    color: #fff;
    font-weight: 800;
    font-size: .9rem;
    cursor: pointer;
    transition: all .2s;
    font-family: inherit;
    box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25);
    display: flex;
    align-items: center;
    justify-content: center;
    gap: .5rem;
}
.cp-btn-start:hover:not(:disabled) { 
    background: var(--primary-dark);
    transform: translateY(-1px);
    box-shadow: 0 6px 16px rgba(37, 99, 235, 0.35);
}
.cp-btn-start:disabled { 
    opacity: 0.6; 
    cursor: not-allowed; 
    box-shadow: none;
    transform: none;
}

/* Thanh tiến trình */
.cp-progress-wrap {
    display: none;
    flex-direction: column;
    gap: .4rem;
    margin-top: .5rem;
}
.cp-progress-wrap.show { display: flex; }
.cp-progress-text {
    font-size: .75rem;
    color: var(--text-3);
    text-align: center;
}
.cp-progress-bar-bg {
    width: 100%;
    height: 6px;
    background: var(--surface-2);
    border-radius: 50px;
    overflow: hidden;
}
.cp-progress-bar {
    height: 100%;
    width: 0%;
    background: var(--primary);
    transition: width .3s ease;
    border-radius: 50px;
}

@media (max-width: 500px) {
    .cp-section { padding: 1rem; border-radius: 14px; }
    .cp-title-wrap { font-size: .92rem; }
    .cp-switch-toggle { font-size: .7rem; padding: .3rem .6rem; }
    .cp-textarea { font-size: .92rem; padding: .75rem .85rem; max-height: 250px; }
    .cp-btn-start { font-size: .85rem; padding: .65rem; }
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
            placeholder="Dán văn bản tiếng Trung vào đây..."></textarea>
        <div class="cp-char-count" id="cpCharCount">0 ký tự</div>
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
    var MAX_SENTENCE_LENGTH = 5000; // Giới hạn cho MỖI CÂU
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
        charCount.textContent = len.toLocaleString('vi-VN') + ' ký tự';
        autoResizeTextarea();
    }
    inputArea.addEventListener('input', updateCharCount);
    setTimeout(autoResizeTextarea, 100);

    // ⭐ 3. NÚT CHUYỂN ĐỔI CHIỀU DỊCH
    switchBtn.addEventListener('click', function() {
        if (currentMode === 'zh2vi') {
            currentMode = 'vi2zh';
            switchLabel.textContent = 'Việt → Trung';
            switchBtn.classList.add('mode-vi2zh');
            inputArea.placeholder = 'Nhập văn bản tiếng Việt vào đây... (hệ thống sẽ dịch sang tiếng Trung)';
        } else {
            currentMode = 'zh2vi';
            switchLabel.textContent = 'Trung → Việt';
            switchBtn.classList.remove('mode-vi2zh');
            inputArea.placeholder = 'Dán văn bản tiếng Trung vào đây...';
        }
        inputArea.value = '';
        updateCharCount();
    });

    // ⭐ 4. HÀM TÁCH CÂU THÔNG MINH
    function splitIntoSentences(text, mode) {
        var sentences = [];
        
        if (mode === 'zh2vi') {
            var rawSentences = text.split(/(?<=[。！？!?\n])/g);
            rawSentences.forEach(function(s) {
                s = s.trim();
                if (s && /[\u4e00-\u9fa5]/.test(s)) {
                    sentences.push(s);
                }
            });
        } else {
            var textForSplit = text.replace(/\.\.\./g, '___ELLIPSIS___');
            textForSplit = textForSplit.replace(/(\d)\.(\d)/g, '$1___DOT___$2');
            
            var rawSentences = textForSplit.split(/(?<=[.!?\n])/g);
            rawSentences.forEach(function(s) {
                s = s.trim();
                if (s) {
                    s = s.replace(/___ELLIPSIS___/g, '...').replace(/___DOT___/g, '.');
                    sentences.push(s);
                }
            });
        }

        // Chia nhỏ câu quá dài
        var finalSentences = [];
        sentences.forEach(function(s) {
            if (s.length > MAX_SENTENCE_LENGTH) {
                var remaining = s;
                while (remaining.length > MAX_SENTENCE_LENGTH) {
                    var chunk = remaining.substring(0, MAX_SENTENCE_LENGTH);
                    var lastSpace = chunk.lastIndexOf(' ');
                    if (lastSpace === -1 || lastSpace < MAX_SENTENCE_LENGTH * 0.8) {
                        lastSpace = MAX_SENTENCE_LENGTH;
                    }
                    finalSentences.push(remaining.substring(0, lastSpace).trim());
                    remaining = remaining.substring(lastSpace).trim();
                }
                if (remaining.length > 0) {
                    finalSentences.push(remaining);
                }
            } else {
                finalSentences.push(s);
            }
        });

        return finalSentences;
    }

    // ⭐ 5. NÚT BẮT ĐẦU
    startBtn.addEventListener('click', async function() {
        var rawText = inputArea.value.trim();
        if (!rawText) {
            alert('Vui lòng nhập văn bản!');
            return;
        }

        startBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Đang xử lý...';
        startBtn.disabled = true;
        progressWrap.classList.add('show');
        progressBar.style.width = '0%';

        // Tách câu
        var sentences = splitIntoSentences(rawText, currentMode);

        if (sentences.length === 0) {
            alert('Không tìm thấy câu hợp lệ!');
            startBtn.innerHTML = '<i class="fas fa-play"></i> Bắt đầu luyện tập';
            startBtn.disabled = false;
            progressWrap.classList.remove('show');
            return;
        }

        progressText.textContent = 'Tìm thấy ' + sentences.length + ' câu. Đang dịch...';

        // Nạp pinyin-pro
        await loadPinyinPro();

        // Dịch
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

        // Kích hoạt hệ thống luyện tập
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

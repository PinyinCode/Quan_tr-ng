# -*- coding: utf-8 -*-
r"""
custom_practice_module.py - Khu vực Luyện tập Tự do (Hiển thị sẵn)
Hỗ trợ: Dịch 2 chiều, tự động giãn chiều cao, tự động chia nhỏ để dịch.
"""

def build_custom_practice_css():
    return r"""
/* ═══════════════════════════════════════════════════════════ */
/* KHU VỰC LUYỆN TẬP TỰ DO - HIỂN THỊ SẴN TRÊN TRANG CHỦ      */
/* ═══════════════════════════════════════════════════════════ */
.cp-section {
    background: var(--surface);
    border: 1.5px solid var(--border);
    border-radius: 16px;
    padding: 1.25rem;
    margin-bottom: 1rem;
    box-shadow: var(--shadow-sm);
    display: flex;
    flex-direction: column;
    gap: .85rem;
    position: relative;
    overflow: hidden;
}
.cp-section::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, #6366f1, #a855f7, #ec4899);
}

.cp-section-header {
    display: flex;
    align-items: center;
    gap: .6rem;
    font-size: 1rem;
    font-weight: 800;
    color: var(--text);
}
.cp-section-header i {
    color: var(--primary);
    font-size: 1.1rem;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 32px;
    height: 32px;
    border-radius: 8px;
    background: linear-gradient(135deg, rgba(99,102,241,.15), rgba(168,85,247,.15));
}
.cp-btn-reset {
    padding: .35rem .8rem;
    border-radius: 50px;
    border: 1.5px solid var(--border);
    background: var(--surface);
    color: var(--text-2);
    font-size: .75rem;
    font-weight: 700;
    font-family: inherit;
    cursor: pointer;
    transition: .15s;
    margin-left: auto;
    display: inline-flex;
    align-items: center;
    gap: .3rem;
}
.cp-btn-reset:hover {
    background: var(--surface-2);
    color: var(--primary);
    border-color: var(--primary);
}

/* Nút chuyển đổi chiều dịch */
.cp-switch-row {
    display: flex;
    gap: .5rem;
    background: var(--surface-2);
    padding: .35rem;
    border-radius: 50px;
    width: fit-content;
    max-width: 100%;
}
.cp-switch-btn {
    padding: .4rem 1rem;
    border-radius: 50px;
    border: none;
    background: transparent;
    color: var(--text-3);
    font-weight: 700;
    font-size: .82rem;
    cursor: pointer;
    transition: .2s;
    font-family: inherit;
    white-space: nowrap;
    display: inline-flex;
    align-items: center;
    gap: .35rem;
}
.cp-switch-btn.active {
    background: var(--primary);
    color: #fff;
    box-shadow: 0 2px 6px rgba(37,99,235,.3);
}
.cp-switch-btn:hover:not(.active) {
    color: var(--primary);
}

/* Ô nhập liệu tự giãn */
.cp-input-wrapper {
    display: flex;
    flex-direction: column;
    gap: .3rem;
}
.cp-textarea {
    width: 100%;
    padding: .85rem;
    border-radius: 12px;
    border: 1.5px solid var(--border);
    background: var(--surface-2);
    color: var(--text);
    font-family: var(--font-zh);
    font-size: 1rem;
    resize: none;
    overflow-y: hidden;
    min-height: 46px;
    max-height: 250px;
    transition: height 0.1s ease, border-color .15s, box-shadow .15s;
    line-height: 1.5;
}
.cp-textarea:focus {
    border-color: var(--primary);
    outline: none;
    box-shadow: 0 0 0 3px rgba(37,99,235,.15);
    background: var(--surface);
}
.cp-char-count {
    font-size: .72rem;
    color: var(--text-3);
    text-align: right;
}
.cp-char-count.over {
    color: var(--danger);
    font-weight: 700;
}

/* Nút bắt đầu */
.cp-btn-start {
    padding: .75rem;
    border-radius: 12px;
    border: none;
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    color: #fff;
    font-weight: 800;
    font-size: .9rem;
    cursor: pointer;
    transition: .2s;
    font-family: inherit;
    box-shadow: 0 4px 12px rgba(124,58,237,.35);
    display: flex;
    align-items: center;
    justify-content: center;
    gap: .5rem;
}
.cp-btn-start:hover:not(:disabled) { 
    transform: translateY(-1px); 
    box-shadow: 0 6px 18px rgba(124,58,237,.5); 
}
.cp-btn-start:disabled { 
    opacity: 0.7; 
    cursor: not-allowed; 
}

/* Thanh tiến trình */
.cp-progress-wrap {
    display: none;
    flex-direction: column;
    gap: .4rem;
}
.cp-progress-wrap.show { display: flex; }
.cp-progress-text {
    font-size: .78rem;
    color: var(--text-3);
    text-align: center;
    font-weight: 600;
}
.cp-progress-bar-bg {
    width: 100%;
    height: 8px;
    background: var(--surface-2);
    border-radius: 50px;
    overflow: hidden;
}
.cp-progress-bar {
    height: 100%;
    width: 0%;
    background: linear-gradient(90deg, #6366f1, #a855f7);
    transition: width .3s ease;
    border-radius: 50px;
}

@media (max-width: 500px) {
    .cp-section { padding: 1rem; border-radius: 14px; }
    .cp-section-header { font-size: .92rem; }
    .cp-btn-reset { font-size: .7rem; padding: .3rem .65rem; }
    .cp-switch-btn { padding: .35rem .75rem; font-size: .75rem; }
    .cp-textarea { font-size: .92rem; padding: .7rem; }
    .cp-btn-start { font-size: .85rem; padding: .65rem; }
}
"""

def build_custom_practice_html():
    return r"""
<div class="cp-section" id="cpSection">
    <div class="cp-section-header">
        <i class="fas fa-pen-fancy"></i>
        <span>Luyện tập văn bản tự do</span>
        <button class="cp-btn-reset" id="cpResetBtn" type="button" title="Làm mới">
            <i class="fas fa-redo"></i> Làm mới
        </button>
    </div>

    <div class="cp-switch-row">
        <button class="cp-switch-btn active" data-mode="zh2vi" type="button">
            <i class="fas fa-arrow-right"></i> Trung → Việt
        </button>
        <button class="cp-switch-btn" data-mode="vi2zh" type="button">
            <i class="fas fa-arrow-left"></i> Việt → Trung
        </button>
    </div>

    <div class="cp-input-wrapper">
        <textarea class="cp-textarea" id="cpInputZh" rows="1"
            placeholder="Dán văn bản tiếng Trung vào đây... (tối đa 5000 ký tự)"></textarea>
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
    var resetBtn = document.getElementById('cpResetBtn');
    var switchBtns = document.querySelectorAll('.cp-switch-btn');
    var progressWrap = document.getElementById('cpProgressWrap');
    var progressBar = document.getElementById('cpProgressBar');
    var progressText = document.getElementById('cpProgressText');

    // ⭐ 1. TỰ ĐỘNG GIÃN CHIỀU CAO Ô NHẬP LIỆU
    function autoResizeTextarea() {
        inputArea.style.height = 'auto';
        var newHeight = inputArea.scrollHeight;
        var maxHeight = 250; // Khớp với max-height trong CSS
        if (newHeight > maxHeight) {
            inputArea.style.height = maxHeight + 'px';
            inputArea.style.overflowY = 'auto';
        } else {
            inputArea.style.height = newHeight + 'px';
            inputArea.style.overflowY = 'hidden';
        }
    }

    // ⭐ 2. ĐẾM KÝ TỰ + CẮT BỚT NẾU VƯỢT QUÁ
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
    setTimeout(autoResizeTextarea, 100); // Chạy lần đầu

    // ⭐ 3. CHUYỂN ĐỔI CHIỀU DỊCH (Trung -> Việt / Việt -> Trung)
    switchBtns.forEach(function(btn) {
        btn.addEventListener('click', function() {
            var mode = this.dataset.mode;
            if (mode === currentMode) return;
            
            currentMode = mode;
            switchBtns.forEach(function(b) { b.classList.remove('active'); });
            this.classList.add('active');
            
            if (currentMode === 'zh2vi') {
                inputArea.placeholder = 'Dán văn bản tiếng Trung vào đây... (tối đa 5000 ký tự)';
            } else {
                inputArea.placeholder = 'Nhập văn bản tiếng Việt vào đây... (hệ thống sẽ dịch sang tiếng Trung)';
            }
            inputArea.value = '';
            updateCharCount();
        });
    });

    // ⭐ 4. NÚT "LÀM MỚI"
    resetBtn.addEventListener('click', function() {
        inputArea.value = '';
        updateCharCount();
        progressWrap.classList.remove('show');
        startBtn.disabled = false;
        startBtn.innerHTML = '<i class="fas fa-play"></i> Bắt đầu luyện tập';
        setTimeout(autoResizeTextarea, 50);
        
        // Reset về tab tổng hợp nếu đang ở custom
        if (window.__customPracticeActive) {
            window.__customPracticeActive = false;
            if (typeof DATASET_REGISTRY !== 'undefined' && DATASET_REGISTRY['tonghop']) {
                if (typeof window.__switchRawData === 'function') {
                    window.__switchRawData('tonghop');
                }
                if (typeof buildFilters === 'function') buildFilters();
                if (typeof applyFilter === 'function') applyFilter();
                if (typeof updateResultCount === 'function') updateResultCount();
            }
        }
    });

    // ⭐ 5. NÚT "BẮT ĐẦU LUYỆN TẬP"
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

        // Tách câu theo chế độ
        var sentences = [];
        if (currentMode === 'zh2vi') {
            sentences = rawText.split(/(?<=[。！？!?\n])/g)
                .map(function(s) { return s.trim(); })
                .filter(function(s) { return s.length > 0 && /[\u4e00-\u9fa5]/.test(s); });
        } else {
            sentences = rawText.split(/(?<=[.!?\n])/g)
                .map(function(s) { return s.trim(); })
                .filter(function(s) { return s.length > 0; });
        }

        if (sentences.length === 0) {
            alert('Không tìm thấy câu hợp lệ!');
            startBtn.innerHTML = '<i class="fas fa-play"></i> Bắt đầu luyện tập';
            startBtn.disabled = false;
            progressWrap.classList.remove('show');
            return;
        }

        // Nạp pinyin-pro
        await loadPinyinPro();

        // Dịch từng đợt
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

        // Sắp xếp lại
        customData.sort(function(a, b) { return parseInt(a.stt) - parseInt(b.stt); });

        // Đưa vào hệ thống luyện tập
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

    // ⭐ HÀM NẠP THƯ VIỆN PINYIN
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

    // ⭐ HÀM GỌI GOOGLE TRANSLATE
    async function fetchTranslate(text, mode) {
        var translated = '';
        var pinyin = '';
        try {
            if (mode === 'zh2vi') {
                var gtRes = await fetch('https://translate.googleapis.com/translate_a/single?client=gtx&sl=zh-CN&tl=vi&dt=t&q=' + encodeURIComponent(text));
                var gtJson = await gtRes.json();
                translated = gtJson[0].map(function(item) { return item[0]; }).join('');
                if (window.pinyinPro) {
                    pinyin = window.pinyinPro.pinyin(text, { toneType: 'symbol', type: 'array' }).join(' ');
                }
            } else {
                var gtRes2 = await fetch('https://translate.googleapis.com/translate_a/single?client=gtx&sl=vi&tl=zh-CN&dt=t&q=' + encodeURIComponent(text));
                var gtJson2 = await gtRes2.json();
                translated = gtJson2[0].map(function(item) { return item[0]; }).join('');
                if (window.pinyinPro) {
                    pinyin = window.pinyinPro.pinyin(translated, { toneType: 'symbol', type: 'array' }).join(' ');
                }
            }
        } catch(e) {
            console.warn('[CP] Google Translate error:', e);
        }
        return { translated: translated, pinyin: pinyin };
    }
})();
"""

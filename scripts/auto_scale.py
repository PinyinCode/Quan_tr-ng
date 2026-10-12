# -*- coding: utf-8 -*-
"""
Auto-scale module — Chia tỉ lệ không gian bằng FLEX cho cả Desktop + Mobile.

Nguyên tắc:
- Practice Full modal dùng flex-direction: column
- Header/filters/nav: flex 0 0 auto (không co giãn)
- Body: flex 1 1 auto (chiếm phần còn lại)
- Trong body: nội dung dùng flex phân bố theo tỉ lệ
- Font-size: dùng clamp() có kèm vmin (min của vw, vh) — tự scale cả 2 chiều

Cách dùng trong build.py:
    from auto_scale import build_auto_scale_css, build_auto_scale_js

    full_css = (
        ...
        + build_auto_scale_css()  # chèn CUỐI CSS
    )

    full_js = (
        ...
        + build_auto_scale_js()   # chèn sau $ helper
    )
"""


def build_scale_css():
    return r"""
/* ═══════════════════════════════════════════════════════════════ */
/* AUTO-SCALE — Chia tỉ lệ bằng FLEX cho cả Desktop + Mobile     */
/* ═══════════════════════════════════════════════════════════════ */

:root {
    --pf-scale: 1;
    --ui-scale: 1;
}

/* ═══════════════════════════════════════════════════════════════ */
/* 1. PRACTICE FULL MODAL — phân bố theo FLEX TỈ LỆ              */
/* ═══════════════════════════════════════════════════════════════ */

/* Body: chiếm hết không gian còn lại */
.practice-full-body {
    flex: 1 1 auto !important;
    min-height: 0 !important;
    overflow-y: auto;
    display: flex !important;
    flex-direction: column;
    justify-content: center;      /* ⭐ căn giữa theo chiều dọc */
    align-items: center;
    padding: clamp(.5rem, 2vh, 1.5rem) clamp(.5rem, 2vw, 1.25rem)
             calc(60px + env(safe-area-inset-bottom)) !important;
}

/* Content: chiếm hết chiều rộng + dùng flex phân bố */
.practice-full-content {
    width: 100%;
    max-width: var(--pf-content-max, 95vw);
    height: 100%;                 /* ⭐ chiếm hết chiều cao body */
    max-height: 100%;
    display: flex;
    flex-direction: column;
    gap: 0;                       /* ⭐ bỏ gap cố định — dùng flex */
    justify-content: space-between;  /* ⭐ phân bố đều 3 khối */
    margin: 0 !important;
    transition: max-width .3s cubic-bezier(.34,1.56,.64,1);
}

/* Khối 1: Câu hỏi VI — không co giãn */
.practice-full-vi {
    flex: 0 0 auto;
    font-size: clamp(1.15rem, 2.2vmin, 2.4rem) !important;
    padding: clamp(.6rem, 1.5vh, 1.4rem) clamp(.6rem, 1.5vw, 1.2rem);
    line-height: 1.45;
    margin-bottom: clamp(.5rem, 1.5vh, 1.2rem);
}

/* Khối 2: Vùng input — chiếm không gian còn thừa */
.practice-full-input-wrap {
    flex: 1 1 auto;
    min-height: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;      /* ⭐ input ở giữa vùng này */
    gap: clamp(.4rem, 1vh, .8rem);
    padding: clamp(.5rem, 1.5vh, 1rem) 0;
}

/* Khối 3: Nút Chấm điểm / Xem đáp án — không co giãn */
.reveal-actions {
    flex: 0 0 auto;
    margin-top: clamp(.5rem, 1.5vh, 1.2rem);
}

.answer-reveal {
    flex: 0 0 auto;
    margin-top: clamp(.4rem, 1vh, .8rem);
}

/* ─── Input ô nhập: tự scale theo vmin (min vw, vh) ─── */
.practice-input-row {
    display: flex;
    align-items: stretch;
    gap: clamp(.4rem, .8vw, .6rem);
}

.practice-full-input {
    font-size: clamp(1.15rem, 2.4vmin, 2rem) !important;
    padding: clamp(.7rem, 1.6vh, 1.2rem) clamp(.85rem, 1.5vw, 1.3rem) !important;
    min-height: clamp(48px, 7vh, 72px) !important;
    max-height: 30vh !important;
}

.practice-speak-btn {
    min-width: clamp(42px, 6vmin, 64px) !important;
    font-size: clamp(.9rem, 1.6vmin, 1.4rem) !important;
    border-radius: clamp(10px, 1.5vmin, 16px) !important;
}

/* ─── Preview ký tự ─── */
.char-preview {
    min-height: clamp(28px, 4vh, 50px);
    padding: clamp(.3rem, .8vh, .7rem);
    gap: clamp(.25rem, .5vmin, .5rem);
}

.char-slot {
    font-size: clamp(1rem, 2vmin, 1.8rem) !important;
    min-width: clamp(1.2rem, 2vmin, 2rem) !important;
    height: clamp(1.6rem, 3vh, 2.8rem) !important;
}

/* ─── Nút Chấm điểm / Xem đáp án — tự to theo vmin ─── */
.reveal-actions button {
    padding: clamp(.55rem, 1.4vh, 1rem) clamp(.7rem, 1.5vw, 1.3rem) !important;
    font-size: clamp(.8rem, 1.5vmin, 1.1rem) !important;
    border-radius: clamp(10px, 1.5vmin, 16px) !important;
}

/* ─── Đáp án ─── */
.answer-phrase-btn {
    font-size: clamp(1.1rem, 2.2vmin, 2rem) !important;
    padding: clamp(.35rem, .9vh, .8rem) clamp(.65rem, 1.2vw, 1.1rem) !important;
}

.answer-pinyin {
    font-size: clamp(.8rem, 1.4vmin, 1.1rem) !important;
}

/* ═══════════════════════════════════════════════════════════════ */
/* 2. HEADER + FILTER + DATASET — scale theo --ui-scale + vmin   */
/* ═══════════════════════════════════════════════════════════════ */

.header-inner {
    margin-bottom: calc(.4rem * var(--ui-scale, 1));
}

.logo-icon {
    width: calc(clamp(40px, 5vmin, 64px) * var(--ui-scale, 1)) !important;
    height: calc(clamp(40px, 5vmin, 64px) * var(--ui-scale, 1)) !important;
    font-size: calc(clamp(1.1rem, 2.5vmin, 1.9rem) * var(--ui-scale, 1)) !important;
}

.logo-text .title {
    font-size: calc(clamp(1.1rem, 2.4vmin, 1.9rem) * var(--ui-scale, 1)) !important;
}

.logo-text .subtitle {
    font-size: calc(clamp(.6rem, 1.2vmin, .9rem) * var(--ui-scale, 1)) !important;
    padding: calc(.25rem * var(--ui-scale, 1))
             calc(.7rem * var(--ui-scale, 1)) !important;
}

.header-actions .icon-btn {
    width: calc(clamp(30px, 4vmin, 46px) * var(--ui-scale, 1)) !important;
    height: calc(clamp(30px, 4vmin, 46px) * var(--ui-scale, 1)) !important;
    font-size: calc(clamp(.75rem, 1.5vmin, 1.1rem) * var(--ui-scale, 1)) !important;
}

/* ─── Dataset selector ─── */
.dataset-selector {
    padding: calc(.6rem, 1.2vmin, 1rem) !important;
    padding: clamp(.6rem, 1.2vmin, 1rem) clamp(.75rem, 1.5vmin, 1.2rem) !important;
    margin-bottom: clamp(.5rem, 1vmin, .9rem) !important;
}

.ds-label {
    font-size: clamp(.62rem, 1.1vmin, .85rem) !important;
    margin-bottom: clamp(.35rem, .8vmin, .6rem) !important;
}

.ds-btn {
    padding: clamp(.5rem, 1.2vmin, .9rem) clamp(.7rem, 1.4vmin, 1.1rem) !important;
    font-size: clamp(.75rem, 1.4vmin, 1rem) !important;
}

.ds-sub-btn {
    padding: clamp(.45rem, 1vmin, .85rem) clamp(.8rem, 1.6vmin, 1.2rem) !important;
    font-size: clamp(.7rem, 1.3vmin, .95rem) !important;
}

/* ─── Search bar ─── */
.search-bar input {
    padding: clamp(.4rem, 1vmin, .8rem)
             clamp(2rem, 4vmin, 3rem)
             clamp(.4rem, 1vmin, .8rem)
             clamp(2rem, 4vmin, 3rem) !important;
    font-size: clamp(.78rem, 1.5vmin, 1rem) !important;
}

/* ─── Filters HSK + Chủ đề (trang chính) ─── */
.filters .chip {
    padding: clamp(.35rem, .9vmin, .7rem) clamp(.55rem, 1.2vmin, 1rem) !important;
    font-size: clamp(.7rem, 1.3vmin, .95rem) !important;
}

.chip-label {
    font-size: clamp(.55rem, 1vmin, .75rem) !important;
}

/* ─── Result count ─── */
.result-count {
    font-size: clamp(.65rem, 1.2vmin, .85rem) !important;
    padding: clamp(.3rem, .7vmin, .5rem) clamp(.55rem, 1.1vmin, .9rem) !important;
}

/* ─── Card chính ─── */
.card-zh {
    font-size: clamp(1.1rem, 2.2vmin, 1.6rem) !important;
}
.card-vi {
    font-size: clamp(.78rem, 1.4vmin, 1rem) !important;
}
.card-pinyin {
    font-size: clamp(.72rem, 1.3vmin, .95rem) !important;
}

.card.focused .card-zh {
    font-size: clamp(1.5rem, 3vmin, 2.4rem) !important;
}

/* ═══════════════════════════════════════════════════════════════ */
/* 3. PRACTICE FULL — Header / Filters / Nav scale theo vmin     */
/* ═══════════════════════════════════════════════════════════════ */

.practice-full-header {
    min-height: clamp(44px, 7vh, 72px) !important;
    padding: clamp(.4rem, 1.2vh, .9rem) clamp(.8rem, 2vw, 1.4rem) !important;
}

.pf-brand-icon {
    width: clamp(28px, 4vmin, 46px) !important;
    height: clamp(28px, 4vmin, 46px) !important;
    font-size: clamp(.75rem, 1.8vmin, 1.2rem) !important;
}

.pf-brand-title {
    font-size: clamp(.75rem, 1.6vmin, 1.1rem) !important;
}

.pf-brand-sub {
    font-size: clamp(.55rem, 1.2vmin, .8rem) !important;
}

.pf-counter {
    font-size: clamp(.65rem, 1.4vmin, .95rem) !important;
    padding: clamp(.3rem, .8vmin, .5rem) clamp(.6rem, 1.4vmin, 1rem) !important;
}

.pf-close {
    width: clamp(28px, 4vmin, 44px) !important;
    height: clamp(28px, 4vmin, 44px) !important;
    font-size: clamp(.8rem, 1.6vmin, 1.1rem) !important;
}

/* ─── Filters trong modal ─── */
.pf-filters {
    padding: clamp(.4rem, 1.2vh, .7rem) clamp(.8rem, 2vw, 1.4rem) !important;
}

.pf-chip {
    padding: clamp(.25rem, .7vmin, .55rem) clamp(.5rem, 1.1vmin, .9rem) !important;
    font-size: clamp(.65rem, 1.3vmin, .9rem) !important;
}

.pf-chip-label {
    font-size: clamp(.52rem, 1vmin, .7rem) !important;
}

/* ─── Dataset row trong modal ─── */
.pf-dataset-row {
    padding: clamp(.4rem, 1vmin, .7rem) clamp(.5rem, 1.2vmin, .9rem) !important;
    gap: clamp(.35rem, .8vmin, .6rem) !important;
}

.pf-dataset-select,
.pf-dataset-search input,
.pf-quick-nav-select {
    padding: clamp(.3rem, .8vmin, .6rem) clamp(1.8rem, 3.5vmin, 2.4rem) !important;
    font-size: clamp(.68rem, 1.4vmin, .95rem) !important;
}

.pf-dataset-label,
.pf-quick-nav-label {
    font-size: clamp(.55rem, 1.1vmin, .8rem) !important;
}

/* ─── Nav bottom của modal ─── */
.practice-full-nav {
    min-height: clamp(58px, 9vh, 96px) !important;
    padding: clamp(.5rem, 1.5vh, 1.1rem) clamp(.7rem, 2vw, 1.5rem) !important;
    gap: clamp(.4rem, 1.2vmin, .9rem) !important;
}

.pf-nav-icon.main-nav {
    width: clamp(46px, 8vmin, 88px) !important;
    height: clamp(46px, 8vmin, 88px) !important;
    font-size: clamp(1rem, 2.4vmin, 1.9rem) !important;
}

.pf-nav-icon.mini-nav {
    width: clamp(38px, 6.5vmin, 68px) !important;
    height: clamp(38px, 6.5vmin, 68px) !important;
    font-size: clamp(.8rem, 1.8vmin, 1.4rem) !important;
}

.pf-nav-icon.mini-nav.assemble-toggle.with-label {
    height: clamp(34px, 5.5vmin, 54px) !important;
    padding: 0 clamp(.5rem, 1.2vmin, .9rem) !important;
}

.pf-nav-icon.mini-nav.assemble-toggle.with-label .assemble-toggle-label {
    font-size: clamp(.62rem, 1.3vmin, .85rem) !important;
}

/* ═══════════════════════════════════════════════════════════════ */
/* 4. DESKTOP-ONLY — override lại một số chỗ cần to hơn          */
/* ═══════════════════════════════════════════════════════════════ */
@media (min-width: 769px) {
    /* Content giới hạn chiều rộng hợp lý, không kéo full 100% */
    .practice-full-content {
        max-width: min(90vw, 900px);
    }

    /* Trên desktop, không cần giãn input full chiều cao */
    .practice-full-input-wrap {
        flex: 1 1 auto;
        min-height: 120px;
    }

    /* VI + input + reveal cách đều hơn trên desktop */
    .practice-full-vi {
        margin-bottom: clamp(1rem, 2vh, 2rem);
    }
    .reveal-actions {
        margin-top: clamp(1rem, 2vh, 2rem);
    }

    /* Font to hơn trên desktop */
    .practice-full-vi {
        font-size: clamp(1.5rem, 2.6vmin, 2.4rem) !important;
    }
    .practice-full-input {
        font-size: clamp(1.5rem, 2.8vmin, 2.2rem) !important;
    }
    .reveal-actions button {
        font-size: clamp(.9rem, 1.6vmin, 1.15rem) !important;
    }
}

/* Desktop cực cao (>1100px): cho nội dung to hơn nữa */
@media (min-width: 769px) and (min-height: 1100px) {
    .practice-full-content {
        max-width: min(88vw, 1100px);
        gap: 0;
    }
    .practice-full-vi {
        font-size: clamp(1.8rem, 2.8vmin, 2.6rem) !important;
        padding: clamp(1rem, 2vh, 1.8rem) clamp(.8rem, 2vw, 1.5rem);
    }
    .practice-full-input {
        font-size: clamp(1.8rem, 3vmin, 2.6rem) !important;
        min-height: clamp(72px, 9vh, 100px) !important;
    }
    .char-slot {
        font-size: clamp(1.6rem, 2.4vmin, 2.4rem) !important;
        min-width: clamp(2rem, 2.4vmin, 3rem) !important;
        height: clamp(2.4rem, 3.5vh, 3.6rem) !important;
    }
    .reveal-actions button {
        padding: clamp(.9rem, 1.8vh, 1.3rem) clamp(1rem, 2vw, 1.6rem) !important;
        font-size: clamp(1rem, 1.8vmin, 1.3rem) !important;
    }
    .pf-nav-icon.main-nav {
        width: clamp(68px, 8vmin, 96px) !important;
        height: clamp(68px, 8vmin, 96px) !important;
    }
}

/* Mobile: giữ nguyên flex, font nhỏ gọn */
@media (max-width: 768px) {
    .practice-full-content {
        max-width: 100%;
    }
    .practice-full-vi {
        font-size: clamp(1.1rem, 2.6vmin, 1.5rem) !important;
    }
    .practice-full-input {
        font-size: clamp(1.1rem, 2.8vmin, 1.5rem) !important;
    }
}
"""


def build_auto_scale_js():
    """
    JS: chỉ cần tính --ui-scale (cho header/filter trang chính).
    --pf-scale không cần nữa vì Practice Full đã dùng flex + vmin.
    """
    return r"""
/* ═══════════════════════════════════════════════════════════════ */
/* AUTO-SCALE — tính --ui-scale cho header/filter trang chính     */
/* (Practice Full dùng flex + vmin, không cần JS)                */
/* ═══════════════════════════════════════════════════════════════ */
(function setupUiScale() {
    'use strict';

    var UI_BASE_HEIGHT = 900;
    var UI_MIN_SCALE   = 0.9;
    var UI_MAX_SCALE   = 1.35;

    function computeUiScale() {
        if (window.innerWidth < 769) {
            document.documentElement.style.removeProperty('--ui-scale');
            return;
        }
        var vh = window.innerHeight;
        var uiScale = Math.max(UI_MIN_SCALE, Math.min(UI_MAX_SCALE, vh / UI_BASE_HEIGHT));
        document.documentElement.style.setProperty('--ui-scale', uiScale.toFixed(3));
    }

    computeUiScale();

    var resizeTimer = null;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(computeUiScale, 150);
    });
    window.addEventListener('orientationchange', function() {
        setTimeout(computeUiScale, 300);
    });

    console.log('[AutoScale] UI scale module loaded');
})();
"""


if __name__ == "__main__":
    css = build_auto_scale_css()
    js  = build_auto_scale_js()
    print("=" * 60)
    print("AUTO-SCALE — kiểm tra")
    print("=" * 60)
    print(f"CSS: {len(css):,} ký tự ({len(css.splitlines())} dòng)")
    print(f"JS:  {len(js):,} ký tự ({len(js.splitlines())} dòng)")
    print("✅ OK")

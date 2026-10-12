# -*- coding: utf-8 -*-

def build_auto_scale_css():
    return r"""
:root {
    --ui-scale: 1;
}

body .practice-full-body {
    flex: 1 1 auto !important;
    min-height: 0 !important;
    overflow-y: auto !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: flex-start !important;
    align-items: center !important;
    padding: 1rem 1rem 80px 1rem !important;
    padding-bottom: calc(80px + env(safe-area-inset-bottom)) !important;
}

body .practice-full-content {
    width: 100% !important;
    max-width: min(92vw, 900px) !important;
    display: flex !important;
    flex-direction: column !important;
    gap: clamp(0.75rem, 1.8vh, 1.5rem) !important;
    justify-content: flex-start !important;
    margin: 0 !important;
    padding: 0 !important;
}

body .practice-full-vi {
    flex: 0 0 auto !important;
    font-size: clamp(1.5rem, 3.2vmin, 3rem) !important;
    padding: clamp(0.9rem, 2vh, 1.6rem) clamp(0.9rem, 2vw, 1.5rem) !important;
    line-height: 1.45 !important;
    margin: 0 !important;
}

body .practice-full-input-wrap {
    flex: 0 0 auto !important;
    display: flex !important;
    flex-direction: column !important;
    gap: clamp(0.5rem, 1.2vh, 1rem) !important;
    padding: 0 !important;
}

body .reveal-actions {
    flex: 0 0 auto !important;
    margin-top: 0 !important;
}

body .answer-reveal {
    flex: 0 0 auto !important;
    margin-top: 0 !important;
}

body .practice-input-row {
    display: flex !important;
    align-items: stretch !important;
    gap: clamp(0.5rem, 1vw, 0.75rem) !important;
}

body .practice-full-input {
    font-size: clamp(1.5rem, 3.2vmin, 2.8rem) !important;
    padding: clamp(0.9rem, 2vh, 1.4rem) clamp(1rem, 2vw, 1.6rem) !important;
    min-height: clamp(60px, 9vh, 90px) !important;
    max-height: 30vh !important;
    line-height: 1.4 !important;
}

body .practice-speak-btn {
    min-width: clamp(50px, 7vmin, 78px) !important;
    font-size: clamp(1.1rem, 2.2vmin, 1.8rem) !important;
    border-radius: clamp(12px, 1.8vmin, 18px) !important;
}

body .char-preview {
    min-height: clamp(34px, 5vh, 60px) !important;
    padding: clamp(0.4rem, 1vh, 0.85rem) !important;
    gap: clamp(0.3rem, 0.6vmin, 0.6rem) !important;
}

body .char-slot {
    font-size: clamp(1.3rem, 2.6vmin, 2.2rem) !important;
    min-width: clamp(1.5rem, 2.6vmin, 2.5rem) !important;
    height: clamp(2rem, 4vh, 3.2rem) !important;
}

body .reveal-actions button {
    padding: clamp(0.75rem, 1.8vh, 1.3rem) clamp(0.9rem, 2vw, 1.6rem) !important;
    font-size: clamp(1rem, 1.9vmin, 1.4rem) !important;
    border-radius: clamp(12px, 1.8vmin, 18px) !important;
}

body .practice-full-status {
    font-size: clamp(1rem, 1.9vmin, 1.4rem) !important;
    min-height: 1.6rem !important;
}

body .answer-phrase-btn {
    font-size: clamp(1.3rem, 2.6vmin, 2.4rem) !important;
    padding: clamp(0.5rem, 1.2vh, 1rem) clamp(0.8rem, 1.5vw, 1.4rem) !important;
}

body .answer-pinyin {
    font-size: clamp(0.95rem, 1.7vmin, 1.4rem) !important;
}

body .header-inner {
    margin-bottom: calc(0.4rem * var(--ui-scale, 1)) !important;
}

body .logo-icon {
    width: calc(clamp(44px, 5.5vmin, 72px) * var(--ui-scale, 1)) !important;
    height: calc(clamp(44px, 5.5vmin, 72px) * var(--ui-scale, 1)) !important;
    font-size: calc(clamp(1.2rem, 2.7vmin, 2.1rem) * var(--ui-scale, 1)) !important;
}

body .logo-text .title {
    font-size: calc(clamp(-bar1.2rem, 2.6vmin, 2.1rem) * var(--ui-scale, 1)) !important;
}

body .logo-text .subtitle {
    font-size: calc(clamp(0.68rem, 1.3vmin, 1rem) * var(--ui-scale, 1)) !important;
}

body .header-actions .icon-btn {
    width: calc(clamp(34px, 4.5vmin, 52px) * var(--ui-scale, 1)) !important;
    height: calc(clamp(34px, 4.5vmin, 52px) * var(--ui-scale, 1)) !important;
    font-size: calc(clamp(0.85rem, 1.7vmin, 1.25rem) * var(--ui-scale, 1)) !important;
}

body .dataset-selector {
    padding: clamp(0.7rem, 1.4vmin, 1.2rem) clamp(0.85rem, 1.7vmin, 1.4rem) !important;
    margin-bottom: clamp(0.6rem, 1.2vmin, 1.1rem) !important;
}

body .ds-label {
    font-size: clamp(0.7rem, 1.25vmin, 1rem) !important;
    margin-bottom: clamp(0.4rem, 0.9vmin, 0.7rem) !important;
}

body .ds-btn {
    padding: clamp(0.6rem, 1.4vmin, 1.1rem) clamp(0.8rem, 1.6vmin, 1.3rem) !important;
    font-size: clamp(0.85rem, 1.6vmin, 1.15rem) !important;
}

body .ds-sub-btn {
    padding: clamp(0.55rem, 1.2vmin, 1rem) clamp(0.9rem, 1.8vmin, 1.4rem) !important;
    font-size: clamp(0.8rem, 1.5vmin, 1.1rem) !important;
}

body .search input {
    padding: clamp(0.5rem, 1.2vmin, 1rem) clamp(2.2rem, 4.5vmin, 3.4rem) clamp(0.5rem, 1.2vmin, 1rem) clamp(2.2rem, 4.5vmin, 3.4rem) !important;
    font-size: clamp(0.88rem, 1.7vmin, 1.15rem) !important;
}

body .filters .chip {
    padding: clamp(0.45rem, 1.1vmin, 0.9rem) clamp(0.7rem, 1.4vmin, 1.2rem) !important;
    font-size: clamp(0.8rem, 1.5vmin, 1.1rem) !important;
}

body .chip-label {
    font-size: clamp(0.62rem, 1.15vmin, 0.85rem) !important;
}

body .result-count {
    font-size: clamp(0.75rem, 1.4vmin, 1rem) !important;
    padding: clamp(0.35rem, 0.8vmin, 0.6rem) clamp(0.65rem, 1.3vmin, 1.05rem) !important;
}

body .card-zh {
    font-size: clamp(1.3rem, 2.6vmin, 1.9rem) !important;
}

body .card-vi {
    font-size: clamp(0.9rem, 1.6vmin, 1.15rem) !important;
}

body .card-pinyin {
    font-size: clamp(0.85rem, 1.5vmin, 1.1rem) !important;
}

body .card.focused .card-zh {
    font-size: clamp(1.7rem, 3.4vmin, 2.8rem) !important;
}

body .practice-full-header {
    min-height: clamp(52px, 8vh, 84px) !important;
    padding: clamp(0.5rem, 1.4vh, 1rem) clamp(1rem, 2.2vw, 1.6rem) !important;
}

body .pf-brand-icon {
    width: clamp(34px, 4.5vmin, 54px) !important;
    height: clamp(34px, 4.5vmin, 54px) !important;
    font-size: clamp(0.85rem, 2vmin, 1.4rem) !important;
}

body .pf-brand-title {
    font-size: clamp(0.9rem, 1.8vmin, 1.3rem) !important;
}

body .pf-brand-sub {
    font-size: clamp(0.65rem, 1.4vmin, 0.95rem) !important;
}

body .pf-counter {
    font-size: clamp(0.78rem, 1.6vmin, 1.1rem) !important;
    padding: clamp(0.38rem, 0.9vmin, 0.6rem) clamp(0.7rem, 1.5vmin, 1.15rem) !important;
}

body .pf-close {
    width: clamp(34px, 4.5vmin, 52px) !important;
    height: clamp(34px, 4.5vmin, 52px) !important;
    font-size: clamp(0.95rem, 1.8vmin, 1.3rem) !important;
}

body .pf-filters {
    padding: clamp(0.5rem, 1.4vh, 0.85rem) clamp(1rem, 2.2vw, 1.6rem) !important;
}

body .pf-chip {
    padding: clamp(0.35rem, 0.9vmin, 0.7rem) clamp(0.65rem, 1.3vmin, 1.1rem) !important;
    font-size: clamp(0.78rem, 1.5vmin, 1.05rem) !important;
}

body .pf-chip-label {
    font-size: clamp(0.62rem, 1.15vmin, 0.85rem) !important;
}

body .pf-dataset-row {
    padding: clamp(0.5rem, 1.2vmin, 0.9rem) clamp(0.6rem, 1.4vmin, 1.1rem) !important;
    gap: clamp(0.45rem, 1vmin, 0.75rem) !important;
}

body .pf-dataset-select,
body .pf-dataset-search input,
body .pf-quick-nav-select {
    padding: clamp(0.4rem, 1vmin, 0.75rem) clamp(2rem, 4vmin, 2.8rem) !important;
    font-size: clamp(0.8rem, 1.55vmin, 1.1rem) !important;
}

body .pf-dataset-label,
body .pf-quick-nav-label {
    font-size: clamp(0.65rem, 1.25vmin, 0.92rem) !important;
}

body .practice-full-nav {
    min-height: clamp(66px, 10vh, 108px) !important;
    padding: clamp(0.6rem, 1.7vh, 1.25rem) clamp(0.85rem, 2.2vw, 1.7rem) !important;
    gap: clamp(0.5rem, 1.4vmin, 1.05rem) !important;
}

body .pf-nav-icon.main-nav {
    width: clamp(54px, 9vmin, 100px) !important;
    height: clamp(54px, 9vmin, 100px) !important;
    font-size: clamp(1.15rem, 2.7vmin, 2.1rem) !important;
}

body .pf-nav-icon.mini-nav {
    width: clamp(44px, 7.5vmin, 80px) !important;
    height: clamp(44px, 7.5vmin, 80px) !important;
    font-size: clamp(0.9rem, 2vmin, 1.6rem) !important;
}

body .pf-nav-icon.mini-nav.assemble-toggle.with-label {
    height: clamp(40px, 6.5vmin, 64px) !important;
    padding: 0 clamp(0.6rem, 1.4vmin, 1.05rem) !important;
}

body .pf-nav-icon.mini-nav.assemble-toggle.with-label .assemble-toggle-label {
    font-size: clamp(0.72rem, 1.5vmin, 1rem) !important;
}

@media (max-width: 768px) {
    body .practice-full-content {
        max-width: 100% !important;
        gap: clamp(0.6rem, 1.5vh, 1rem) !important;
    }
    body .practice-full-vi {
        font-size: clamp(1.15rem, 3vmin, 1.6rem) !important;
        padding: 0.75rem 0.7rem !important;
    }
    body .practice-full-input {
        font-size: clamp(1.15rem, 3.2vmin, 1.6rem) !important;
        min-height: 52px !important;
    }
    body .reveal-actions button {
        font-size: clamp(0.8rem, 2vmin, 1rem) !important;
        padding: 0.65rem 0.7rem !important;
    }
    body .pf-nav-icon.main-nav {
        width: 54px !important;
        height: 54px !important;
        font-size: 1.2rem !important;
    }
    body .pf-nav-icon.mini-nav {
        width: 44px !important;
        height: 44px !important;
        font-size: 0.9rem !important;
    }
}
"""


def build_auto_scale_js():
    return r"""
(function setupUiScale() {
    'use strict';
    var UI_BASE_HEIGHT = 900;
    var UI_MIN_SCALE = 0.9;
    var UI_MAX_SCALE = 1.35;
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
})();
"""

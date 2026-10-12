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
    justify-content: center !important;
    align-items: center !important;
    padding: 0.5rem 0.5rem 60px 0.5rem !important;
    padding-bottom: calc(60px + env(safe-area-inset-bottom)) !important;
}

body .practice-full-content {
    width: 100% !important;
    max-width: min(92vw, 900px) !important;
    height: 100% !important;
    max-height: 100% !important;
    display: flex !important;
    flex-direction: column !important;
    gap: 0 !important;
    justify-content: space-between !important;
    margin: 0 !important;
    padding: 0 !important;
}

body .practice-full-vi {
    flex: 0 0 auto !important;
    font-size: clamp(1.1rem, 2.4vmin, 2.4rem) !important;
    padding: clamp(0.6rem, 1.6vh, 1.4rem) clamp(0.6rem, 1.5vw, 1.2rem) !important;
    line-height: 1.45 !important;
    margin: 0 0 clamp(0.5rem, 1.5vh, 1.2rem) 0 !important;
}

body .practice-full-input-wrap {
    flex: 1 1 auto !important;
    min-height: 0 !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
    gap: clamp(0.4rem, 1vh, 0.8rem) !important;
    padding: clamp(0.5rem, 1.5vh, 1rem) 0 !important;
}

body .reveal-actions {
    flex: 0 0 auto !important;
    margin-top: clamp(0.5rem, 1.5vh, 1.2rem) !important;
}

body .answer-reveal {
    flex: 0 0 auto !important;
    margin-top: clamp(0.4rem, 1vh, 0.8rem) !important;
}

body .practice-input-row {
    display: flex !important;
    align-items: stretch !important;
    gap: clamp(0.4rem, 0.8vw, 0.6rem) !important;
}

body .practice-full-input {
    font-size: clamp(1.1rem, 2.4vmin, 2rem) !important;
    padding: clamp(0.7rem, 1.6vh, 1.2rem) clamp(0.85rem, 1.5vw, 1.3rem) !important;
    min-height: clamp(48px, 7vh, 72px) !important;
    max-height: 30vh !important;
}

body .practice-speak-btn {
    min-width: clamp(42px, 6vmin, 64px) !important;
    font-size: clamp(0.9rem, 1.6vmin, 1.4rem) !important;
    border-radius: clamp(10px, 1.5vmin, 16px) !important;
}

body .char-preview {
    min-height: clamp(28px, 4vh, 50px) !important;
    padding: clamp(0.3rem, 0.8vh, 0.7rem) !important;
    gap: clamp(0.25rem, 0.5vmin, 0.5rem) !important;
}

body .char-slot {
    font-size: clamp(1rem, 2vmin, 1.8rem) !important;
    min-width: clamp(1.2rem, 2vmin, 2rem) !important;
    height: clamp(1.6rem, 3vh, 2.8rem) !important;
}

body .reveal-actions button {
    padding: clamp(0.55rem, 1.4vh, 1rem) clamp(0.7rem, 1.5vw, 1.3rem) !important;
    font-size: clamp(0.8rem, 1.5vmin, 1.1rem) !important;
    border-radius: clamp(10px, 1.5vmin, 16px) !important;
}

body .answer-phrase-btn {
    font-size: clamp(1.1rem, 2.2vmin, 2rem) !important;
    padding: clamp(0.35rem, 0.9vh, 0.8rem) clamp(0.65rem, 1.2vw, 1.1rem) !important;
}

body .answer-pinyin {
    font-size: clamp(0.8rem, 1.4vmin, 1.1rem) !important;
}

body .header-inner {
    margin-bottom: calc(0.4rem * var(--ui-scale, 1)) !important;
}

body .logo-icon {
    width: calc(clamp(40px, 5vmin, 64px) * var(--ui-scale, 1)) !important;
    height: calc(clamp(40px, 5vmin, 64px) * var(--ui-scale, 1)) !important;
    font-size: calc(clamp(1.1rem, 2.5vmin, 1.9rem) * var(--ui-scale, 1)) !important;
}

body .logo-text .title {
    font-size: calc(clamp(1.1rem, 2.4vmin, 1.9rem) * var(--ui-scale, 1)) !important;
}

body .logo-text .subtitle {
    font-size: calc(clamp(0.6rem, 1.2vmin, 0.9rem) * var(--ui-scale, 1)) !important;
}

body .header-actions .icon-btn {
    width: calc(clamp(30px, 4vmin, 46px) * var(--ui-scale, 1)) !important;
    height: calc(clamp(30px, 4vmin, 46px) * var(--ui-scale, 1)) !important;
    font-size: calc(clamp(0.75rem, 1.5vmin, 1.1rem) * var(--ui-scale, 1)) !important;
}

body .dataset-selector {
    padding: clamp(0.6rem, 1.2vmin, 1rem) clamp(0.75rem, 1.5vmin, 1.2rem) !important;
    margin-bottom: clamp(0.5rem, 1vmin, 0.9rem) !important;
}

body .ds-label {
    font-size: clamp(0.62rem, 1.1vmin, 0.85rem) !important;
    margin-bottom: clamp(0.35rem, 0.8vmin, 0.6rem) !important;
}

body .ds-btn {
    padding: clamp(0.5rem, 1.2vmin, 0.9rem) clamp(0.7rem, 1.4vmin, 1.1rem) !important;
    font-size: clamp(0.75rem, 1.4vmin, 1rem) !important;
}

body .ds-sub-btn {
    padding: clamp(0.45rem, 1vmin, 0.85rem) clamp(0.8rem, 1.6vmin, 1.2rem) !important;
    font-size: clamp(0.7rem, 1.3vmin, 0.95rem) !important;
}

body .search-bar input {
    padding: clamp(0.4rem, 1vmin, 0.8rem) clamp(2rem, 4vmin, 3rem) clamp(0.4rem, 1vmin, 0.8rem) clamp(2rem, 4vmin, 3rem) !important;
    font-size: clamp(0.78rem, 1.5vmin, 1rem) !important;
}

body .filters .chip {
    padding: clamp(0.35rem, 0.9vmin, 0.7rem) clamp(0.55rem, 1.2vmin, 1rem) !important;
    font-size: clamp(0.7rem, 1.3vmin, 0.95rem) !important;
}

body .chip-label {
    font-size: clamp(0.55rem, 1vmin, 0.75rem) !important;
}

body .result-count {
    font-size: clamp(0.65rem, 1.2vmin, 0.85rem) !important;
    padding: clamp(0.3rem, 0.7vmin, 0.5rem) clamp(0.55rem, 1.1vmin, 0.9rem) !important;
}

body .card-zh {
    font-size: clamp(1.1rem, 2.2vmin, 1.6rem) !important;
}

body .card-vi {
    font-size: clamp(0.78rem, 1.4vmin, 1rem) !important;
}

body .card-pinyin {
    font-size: clamp(0.72rem, 1.3vmin, 0.95rem) !important;
}

body .card.focused .card-zh {
    font-size: clamp(1.5rem, 3vmin, 2.4rem) !important;
}

body .practice-full-header {
    min-height: clamp(44px, 7vh, 72px) !important;
    padding: clamp(0.4rem, 1.2vh, 0.9rem) clamp(0.8rem, 2vw, 1.4rem) !important;
}

body .pf-brand-icon {
    width: clamp(28px, 4vmin, 46px) !important;
    height: clamp(28px, 4vmin, 46px) !important;
    font-size: clamp(0.75rem, 1.8vmin, 1.2rem) !important;
}

body .pf-brand-title {
    font-size: clamp(0.75rem, 1.6vmin, 1.1rem) !important;
}

body .pf-brand-sub {
    font-size: clamp(0.55rem, 1.2vmin, 0.8rem) !important;
}

body .pf-counter {
    font-size: clamp(0.65rem, 1.4vmin, 0.95rem) !important;
    padding: clamp(0.3rem, 0.8vmin, 0.5rem) clamp(0.6rem, 1.4vmin, 1rem) !important;
}

body .pf-close {
    width: clamp(28px, 4vmin, 44px) !important;
    height: clamp(28px, 4vmin, 44px) !important;
    font-size: clamp(0.8rem, 1.6vmin, 1.1rem) !important;
}

body .pf-filters {
    padding: clamp(0.4rem, 1.2vh, 0.7rem) clamp(0.8rem, 2vw, 1.4rem) !important;
}

body .pf-chip {
    padding: clamp(0.25rem, 0.7vmin, 0.55rem) clamp(0.5rem, 1.1vmin, 0.9rem) !important;
    font-size: clamp(0.65rem, 1.3vmin, 0.9rem) !important;
}

body .pf-chip-label {
    font-size: clamp(0.52rem, 1vmin, 0.7rem) !important;
}

body .pf-dataset-row {
    padding: clamp(0.4rem, 1vmin, 0.7rem) clamp(0.5rem, 1.2vmin, 0.9rem) !important;
    gap: clamp(0.35rem, 0.8vmin, 0.6rem) !important;
}

body .pf-dataset-select,
body .pf-dataset-search input,
body .pf-quick-nav-select {
    padding: clamp(0.3rem, 0.8vmin, 0.6rem) clamp(1.8rem, 3.5vmin, 2.4rem) !important;
    font-size: clamp(0.68rem, 1.4vmin, 0.95rem) !important;
}

body .pf-dataset-label,
body .pf-quick-nav-label {
    font-size: clamp(0.55rem, 1.1vmin, 0.8rem) !important;
}

body .practice-full-nav {
    min-height: clamp(58px, 9vh, 96px) !important;
    padding: clamp(0.5rem, 1.5vh, 1.1rem) clamp(0.7rem, 2vw, 1.5rem) !important;
    gap: clamp(0.4rem, 1.2vmin, 0.9rem) !important;
}

body .pf-nav-icon.main-nav {
    width: clamp(46px, 8vmin, 88px) !important;
    height: clamp(46px, 8vmin, 88px) !important;
    font-size: clamp(1rem, 2.4vmin, 1.9rem) !important;
}

body .pf-nav-icon.mini-nav {
    width: clamp(38px, 6.5vmin, 68px) !important;
    height: clamp(38px, 6.5vmin, 68px) !important;
    font-size: clamp(0.8rem, 1.8vmin, 1.4rem) !important;
}

body .pf-nav-icon.mini-nav.assemble-toggle.with-label {
    height: clamp(34px, 5.5vmin, 54px) !important;
    padding: 0 clamp(0.5rem, 1.2vmin, 0.9rem) !important;
}

body .pf-nav-icon.mini-nav.assemble-toggle.with-label .assemble-toggle-label {
    font-size: clamp(0.62rem, 1.3vmin, 0.85rem) !important;
}

@media (min-width: 769px) {
    body .practice-full-content {
        max-width: min(90vw, 900px) !important;
    }
    body .practice-full-input-wrap {
        min-height: 120px !important;
    }
    body .practice-full-vi {
        font-size: clamp(1.5rem, 2.6vmin, 2.4rem) !important;
        margin-bottom: clamp(1rem, 2vh, 2rem) !important;
    }
    body .reveal-actions {
        margin-top: clamp(1rem, 2vh, 2rem) !important;
    }
    body .practice-full-input {
        font-size: clamp(1.5rem, 2.8vmin, 2.2rem) !important;
    }
    body .reveal-actions button {
        font-size: clamp(0.9rem, 1.6vmin, 1.15rem) !important;
    }
}

@media (min-width: 769px) and (min-height: 1100px) {
    body .practice-full-content {
        max-width: min(88vw, 1100px) !important;
    }
    body .practice-full-vi {
        font-size: clamp(1.8rem, 2.8vmin, 2.6rem) !important;
        padding: clamp(1rem, 2vh, 1.8rem) clamp(0.8rem, 2vw, 1.5rem) !important;
    }
    body .practice-full-input {
        font-size: clamp(1.8rem, 3vmin, 2.6rem) !important;
        min-height: clamp(72px, 9vh, 100px) !important;
    }
    body .char-slot {
        font-size: clamp(1.6rem, 2.4vmin, 2.4rem) !important;
        min-width: clamp(2rem, 2.4vmin, 3rem) !important;
        height: clamp(2.4rem, 3.5vh, 3.6rem) !important;
    }
    body .reveal-actions button {
        padding: clamp(0.9rem, 1.8vh, 1.3rem) clamp(1rem, 2vw, 1.6rem) !important;
        font-size: clamp(1rem, 1.8vmin, 1.3rem) !important;
    }
    body .pf-nav-icon.main-nav {
        width: clamp(68px, 8vmin, 96px) !important;
        height: clamp(68px, 8vmin, 96px) !important;
    }
}

@media (max-width: 768px) {
    body .practice-full-content {
        max-width: 100% !important;
    }
    body .practice-full-vi {
        font-size: clamp(1.1rem, 2.6vmin, 1.5rem) !important;
    }
    body .practice-full-input {
        font-size: clamp(1.1rem, 2.8vmin, 1.5rem) !important;
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

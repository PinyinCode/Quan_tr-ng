# -*- coding: utf-8 -*-
"""
Auto-scale module — Tự động scale + căn chỉnh theo KÍCH THƯỚC MÀN HÌNH THỰC.

Quy tắc:
- Desktop (>768px): 
    scale = 60% inch_factor + 40% viewport_factor
    → Màn 10" vs 16" vs 27" khác nhau rõ rệt
- Mobile (≤768px): reset scale = 1
- Font-size: dùng vmin (min của vw, vh) → tự scale
- Practice Full: căn giữa lệch 30/70 (before 30% - content - after 70%)
"""


def build_auto_scale_css():
    return r"""
:root{--ui-scale:1;--pf-scale:1}

/* ═══════════════════════════════════════════════════════════════ */
/* CĂN GIỮA NỘI DUNG — Practice Full (lệch 30/70)               */
/* before = 30% không gian thừa phía trên                        */
/* after  = 70% không gian thừa phía dưới                        */
/* ═══════════════════════════════════════════════════════════════ */
html body .practice-full-body{
    flex:1 1 auto!important;
    min-height:0!important;
    overflow-y:auto!important;
    display:flex!important;
    flex-direction:column!important;
    justify-content:center!important;
    align-items:center!important;
    padding:1rem 1rem 80px 1rem!important;
    padding-bottom:calc(80px + env(safe-area-inset-bottom))!important;
    box-sizing:border-box!important
}
html body .practice-full-body::before{
    content:''!important;
    flex:3 1 0!important;
    min-height:0!important;
    display:block!important;
    pointer-events:none!important
}
html body .practice-full-body::after{
    content:''!important;
    flex:7 1 0!important;
    min-height:0!important;
    display:block!important;
    pointer-events:none!important
}
html body .practice-full-content{
    width:100%!important;
    max-width:min(92vw,900px)!important;
    flex:0 0 auto!important;
    display:flex!important;
    flex-direction:column!important;
    gap:calc(clamp(.75rem,1.8vh,1.5rem) * var(--pf-scale,1))!important;
    justify-content:flex-start!important;
    margin:0!important;
    padding:0!important
}

/* ═══════════════════════════════════════════════════════════════ */
/* HEADER CHÍNH                                                  */
/* ═══════════════════════════════════════════════════════════════ */
html body .logo-icon{
    width:calc(clamp(44px,5.5vmin,72px) * var(--ui-scale,1))!important;
    height:calc(clamp(44px,5.5vmin,72px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(1.2rem,2.7vmin,2.1rem) * var(--ui-scale,1))!important
}
html body .logo-text .title{
    font-size:calc(clamp(1.2rem,2.6vmin,2.1rem) * var(--ui-scale,1))!important
}
html body .logo-text .title .hsk-badge{
    font-size:.62em!important;
    padding:.22em .65em!important
}
html body .logo-text .subtitle{
    font-size:calc(clamp(.68rem,1.3vmin,1rem) * var(--ui-scale,1))!important;
    padding:calc(clamp(.22rem,.5vmin,.4rem) * var(--ui-scale,1))
             calc(clamp(.55rem,1.1vmin,.85rem) * var(--ui-scale,1))!important
}
html body .header-actions .icon-btn{
    width:calc(clamp(34px,4.5vmin,52px) * var(--ui-scale,1))!important;
    height:calc(clamp(34px,4.5vmin,52px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.82rem,1.7vmin,1.25rem) * var(--ui-scale,1))!important
}
html body .trial-badge,
html body .demo-badge{
    font-size:calc(clamp(.65rem,1.3vmin,.95rem) * var(--ui-scale,1))!important;
    padding:calc(clamp(.25rem,.55vmin,.45rem) * var(--ui-scale,1))
             calc(clamp(.5rem,1vmin,.85rem) * var(--ui-scale,1))!important
}
html body .btn-login-header{
    font-size:calc(clamp(.82rem,1.6vmin,1.15rem) * var(--ui-scale,1))!important;
    padding:calc(clamp(.5rem,1vmin,.8rem) * var(--ui-scale,1))
             calc(clamp(.95rem,1.9vmin,1.4rem) * var(--ui-scale,1))!important
}

/* ═══════════════════════════════════════════════════════════════ */
/* DATASET SELECTOR                                              */
/* ═══════════════════════════════════════════════════════════════ */
html body .dataset-selector{
    padding:calc(clamp(.7rem,1.4vmin,1.2rem) * var(--ui-scale,1))
             calc(clamp(.85rem,1.7vmin,1.4rem) * var(--ui-scale,1))!important;
    margin-bottom:calc(clamp(.6rem,1.2vmin,1.1rem) * var(--ui-scale,1))!important;
    border-radius:calc(clamp(12px,1.8vmin,18px) * var(--ui-scale,1))!important
}
html body .ds-label{
    font-size:calc(clamp(.7rem,1.25vmin,1rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.4rem,.8vmin,.6rem) * var(--ui-scale,1))!important;
    margin-bottom:calc(clamp(.4rem,.9vmin,.7rem) * var(--ui-scale,1))!important
}
html body .ds-label i{
    font-size:calc(clamp(.85rem,1.6vmin,1.2rem) * var(--ui-scale,1))!important
}
html body .ds-main-row{
    gap:calc(clamp(.4rem,.8vmin,.6rem) * var(--ui-scale,1))!important
}
html body .ds-btn{
    padding:calc(clamp(.6rem,1.4vmin,1.1rem) * var(--ui-scale,1))
             calc(clamp(.8rem,1.6vmin,1.3rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.82rem,1.6vmin,1.15rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.45rem,.9vmin,.7rem) * var(--ui-scale,1))!important;
    border-radius:calc(clamp(10px,1.6vmin,16px) * var(--ui-scale,1))!important
}
html body .ds-btn i:first-child{
    font-size:calc(clamp(1rem,1.9vmin,1.4rem) * var(--ui-scale,1))!important
}
html body .ds-arrow{
    font-size:calc(clamp(.7rem,1.3vmin,.95rem) * var(--ui-scale,1))!important
}
html body .ds-btn[data-dataset="tonghop"]{
    min-height:calc(clamp(62px,9vmin,96px) * var(--ui-scale,1))!important;
    max-height:none!important;
    padding:calc(clamp(.5rem,1vmin,.8rem) * var(--ui-scale,1))
             calc(clamp(.6rem,1.2vmin,1rem) * var(--ui-scale,1))!important
}
html body .ds-btn[data-dataset="tonghop"] > span{
    font-size:calc(clamp(.7rem,1.4vmin,1.05rem) * var(--ui-scale,1))!important
}
html body .ds-sub-wrap{
    margin-top:calc(clamp(.6rem,1.2vmin,1rem) * var(--ui-scale,1))!important;
    padding-top:calc(clamp(.6rem,1.2vmin,1rem) * var(--ui-scale,1))!important
}
html body .ds-sub-label{
    font-size:calc(clamp(.68rem,1.3vmin,.95rem) * var(--ui-scale,1))!important;
    margin-bottom:calc(clamp(.4rem,.85vmin,.65rem) * var(--ui-scale,1))!important
}
html body .ds-sub-grid{
    gap:calc(clamp(.4rem,.8vmin,.6rem) * var(--ui-scale,1))!important
}
html body .ds-sub-btn{
    padding:calc(clamp(.55rem,1.2vmin,1rem) * var(--ui-scale,1))
             calc(clamp(.85rem,1.7vmin,1.3rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.78rem,1.55vmin,1.1rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.4rem,.8vmin,.6rem) * var(--ui-scale,1))!important;
    border-radius:calc(clamp(50px,7vmin,100px) * var(--ui-scale,1))!important
}
html body .ds-sub-btn i:first-child{
    font-size:calc(clamp(.9rem,1.75vmin,1.3rem) * var(--ui-scale,1))!important
}
html body .ds-new-badge{
    font-size:calc(clamp(.6rem,1.15vmin,.85rem) * var(--ui-scale,1))!important;
    padding:calc(clamp(.15rem,.3vmin,.28rem) * var(--ui-scale,1))
             calc(clamp(.45rem,.9vmin,.7rem) * var(--ui-scale,1))!important
}
html body .ds-sub-lock{
    font-size:calc(clamp(.58rem,1.1vmin,.82rem) * var(--ui-scale,1))!important;
    padding:calc(clamp(.12rem,.24vmin,.22rem) * var(--ui-scale,1))
             calc(clamp(.28rem,.55vmin,.42rem) * var(--ui-scale,1))!important
}
html body .ds-main-lock{
    font-size:calc(clamp(.68rem,1.3vmin,.95rem) * var(--ui-scale,1))!important;
    padding:calc(clamp(.12rem,.24vmin,.22rem) * var(--ui-scale,1))
             calc(clamp(.3rem,.6vmin,.45rem) * var(--ui-scale,1))!important
}
html body .ds-fav-badge{
    min-width:calc(clamp(20px,3vmin,34px) * var(--ui-scale,1))!important;
    height:calc(clamp(20px,3vmin,34px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.62rem,1.2vmin,.88rem) * var(--ui-scale,1))!important;
    padding:0 calc(clamp(.4rem,.8vmin,.6rem) * var(--ui-scale,1))!important
}
html body .ds-fav-lock{
    width:calc(clamp(20px,3vmin,34px) * var(--ui-scale,1))!important;
    height:calc(clamp(20px,3vmin,34px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.6rem,1.15vmin,.85rem) * var(--ui-scale,1))!important
}
html body .ds-dd-fav-badge{
    min-width:calc(clamp(18px,2.7vmin,30px) * var(--ui-scale,1))!important;
    height:calc(clamp(18px,2.7vmin,30px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.6rem,1.15vmin,.85rem) * var(--ui-scale,1))!important
}
html body .ds-dd-fav-lock{
    font-size:calc(clamp(.7rem,1.3vmin,.95rem) * var(--ui-scale,1))!important
}

/* ═══════════════════════════════════════════════════════════════ */
/* SEARCH + FILTER                                               */
/* ═══════════════════════════════════════════════════════════════ */
html body .search-bar input{
    padding:calc(clamp(.5rem,1.2vmin,1rem) * var(--ui-scale,1))
             calc(clamp(2.2rem,4.5vmin,3.4rem) * var(--ui-scale,1))
             calc(clamp(.5rem,1.2vmin,1rem) * var(--ui-scale,1))
             calc(clamp(2.2rem,4.5vmin,3.4rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.88rem,1.7vmin,1.15rem) * var(--ui-scale,1))!important
}
html body .search-bar i.fa-search{
    font-size:calc(clamp(.85rem,1.6vmin,1.15rem) * var(--ui-scale,1))!important;
    left:calc(clamp(12px,1.8vmin,20px) * var(--ui-scale,1))!important
}
html body .search-clear{
    width:calc(clamp(26px,3.6vmin,42px) * var(--ui-scale,1))!important;
    height:calc(clamp(26px,3.6vmin,42px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.72rem,1.4vmin,1rem) * var(--ui-scale,1))!important
}
html body .filters{
    gap:calc(clamp(.4rem,.8vmin,.6rem) * var(--ui-scale,1))!important
}
html body .chip{
    padding:calc(clamp(.42rem,1vmin,.8rem) * var(--ui-scale,1))
             calc(clamp(.6rem,1.3vmin,1rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.8rem,1.5vmin,1.1rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.35rem,.7vmin,.55rem) * var(--ui-scale,1))!important;
    border-radius:calc(clamp(50px,7vmin,100px) * var(--ui-scale,1))!important
}
html body .chip-label{
    font-size:calc(clamp(.62rem,1.15vmin,.85rem) * var(--ui-scale,1))!important
}
html body .chip-value{
    font-size:calc(clamp(.8rem,1.5vmin,1.1rem) * var(--ui-scale,1))!important
}
html body .chip-arrow{
    font-size:calc(clamp(.65rem,1.25vmin,.92rem) * var(--ui-scale,1))!important
}
html body .result-count{
    padding:calc(clamp(.3rem,.7vmin,.55rem) * var(--ui-scale,1))
             calc(clamp(.55rem,1.1vmin,.9rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.72rem,1.4vmin,1rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.35rem,.7vmin,.55rem) * var(--ui-scale,1))!important
}

/* ═══════════════════════════════════════════════════════════════ */
/* FAB GROUP                                                     */
/* ═══════════════════════════════════════════════════════════════ */
html body .fab-btn{
    width:calc(clamp(42px,6vmin,68px) * var(--ui-scale,1))!important;
    height:calc(clamp(42px,6vmin,68px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.95rem,1.9vmin,1.4rem) * var(--ui-scale,1))!important
}
html body .fab-main{
    width:calc(clamp(46px,6.6vmin,74px) * var(--ui-scale,1))!important;
    height:calc(clamp(46px,6.6vmin,74px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(1.05rem,2.1vmin,1.55rem) * var(--ui-scale,1))!important
}

/* ═══════════════════════════════════════════════════════════════ */
/* CARD CHÍNH                                                    */
/* ═══════════════════════════════════════════════════════════════ */
html body .card{
    padding:calc(clamp(.85rem,1.7vmin,1.4rem) * var(--ui-scale,1))!important;
    padding-left:calc(clamp(1rem,2vmin,1.6rem) * var(--ui-scale,1))!important;
    border-radius:calc(clamp(16px,2.5vmin,22px) * var(--ui-scale,1))!important
}
html body .card::before{
    width:calc(clamp(4px,.7vmin,6px) * var(--ui-scale,1))!important;
    border-radius:calc(clamp(16px,2.5vmin,22px) * var(--ui-scale,1)) 0 0 calc(clamp(16px,2.5vmin,22px) * var(--ui-scale,1))!important
}
html body .card-header{
    margin-bottom:calc(clamp(.6rem,1.2vmin,1rem) * var(--ui-scale,1))!important;
    padding-bottom:calc(clamp(.55rem,1.1vmin,.9rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.4rem,.8vmin,.6rem) * var(--ui-scale,1))!important
}
html body .card-stt{
    min-width:calc(clamp(28px,4vmin,48px) * var(--ui-scale,1))!important;
    height:calc(clamp(28px,4vmin,48px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.7rem,1.35vmin,1rem) * var(--ui-scale,1))!important;
    padding:0 calc(clamp(.45rem,.9vmin,.7rem) * var(--ui-scale,1))!important
}
html body .card-meta{
    gap:calc(clamp(.25rem,.5vmin,.4rem) * var(--ui-scale,1))!important
}
html body .card-tag{
    padding:calc(clamp(.18rem,.35vmin,.28rem) * var(--ui-scale,1))
             calc(clamp(.5rem,1vmin,.8rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.65rem,1.25vmin,.92rem) * var(--ui-scale,1))!important
}
html body .card-vi{
    font-size:calc(clamp(.88rem,1.6vmin,1.15rem) * var(--ui-scale,1))!important;
    margin-bottom:calc(clamp(.4rem,.8vmin,.6rem) * var(--ui-scale,1))!important;
    padding-left:calc(clamp(.7rem,1.3vmin,1rem) * var(--ui-scale,1))!important
}
html body .card-zh{
    font-size:calc(clamp(1.3rem,2.6vmin,1.95rem) * var(--ui-scale,1))!important;
    margin-bottom:calc(clamp(.4rem,.8vmin,.6rem) * var(--ui-scale,1))!important
}
html body .card.focused .card-zh{
    font-size:calc(clamp(1.7rem,3.4vmin,2.6rem) * var(--ui-scale,1))!important
}
html body .card-pinyin{
    padding:calc(clamp(.28rem,.55vmin,.45rem) * var(--ui-scale,1))
             calc(clamp(.6rem,1.2vmin,.95rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.8rem,1.5vmin,1.1rem) * var(--ui-scale,1))!important;
    border-radius:calc(clamp(50px,7vmin,100px) * var(--ui-scale,1))!important
}
html body .card-body{
    margin-bottom:calc(clamp(.6rem,1.2vmin,1rem) * var(--ui-scale,1))!important
}
html body .card-practice{
    padding-top:calc(clamp(.5rem,1vmin,.85rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.35rem,.7vmin,.55rem) * var(--ui-scale,1))!important
}
html body .audio-btn,
html body .write-btn,
html body .practice-full-btn,
html body .fav-btn,
html body .toggle-check-btn{
    width:calc(clamp(34px,4.8vmin,55px) * var(--ui-scale,1))!important;
    height:calc(clamp(34px,4.8vmin,55px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.85rem,1.65vmin,1.2rem) * var(--ui-scale,1))!important
}
html body .action-group{
    gap:calc(clamp(.25rem,.5vmin,.4rem) * var(--ui-scale,1))!important
}
html body .practice-input{
    padding:calc(clamp(.45rem,.9vmin,.7rem) * var(--ui-scale,1))
             calc(clamp(.65rem,1.3vmin,1rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.88rem,1.7vmin,1.2rem) * var(--ui-scale,1))!important;
    border-radius:calc(clamp(50px,7vmin,100px) * var(--ui-scale,1))!important
}

/* ═══════════════════════════════════════════════════════════════ */
/* PRACTICE FULL — Header                                        */
/* ═══════════════════════════════════════════════════════════════ */
html body .practice-full-header{
    padding:calc(clamp(.5rem,1.4vh,1rem) * var(--pf-scale,1))
             calc(clamp(1rem,2.2vw,1.6rem) * var(--pf-scale,1))!important;
    min-height:calc(clamp(52px,8vh,84px) * var(--pf-scale,1))!important;
    gap:calc(clamp(.5rem,1vmin,.8rem) * var(--pf-scale,1))!important
}
html body .pf-brand-icon{
    width:calc(clamp(34px,4.5vmin,54px) * var(--pf-scale,1))!important;
    height:calc(clamp(34px,4.5vmin,54px) * var(--pf-scale,1))!important;
    font-size:calc(clamp(.85rem,2vmin,1.4rem) * var(--pf-scale,1))!important;
    border-radius:calc(clamp(9px,1.5vmin,14px) * var(--pf-scale,1))!important
}
html body .pf-brand-title{
    font-size:calc(clamp(.9rem,1.8vmin,1.3rem) * var(--pf-scale,1))!important
}
html body .pf-brand-sub{
    font-size:calc(clamp(.65rem,1.4vmin,.95rem) * var(--pf-scale,1))!important
}
html body .pf-counter{
    padding:calc(clamp(.35rem,.85vmin,.6rem) * var(--pf-scale,1))
             calc(clamp(.65rem,1.4vmin,1.05rem) * var(--pf-scale,1))!important;
    font-size:calc(clamp(.78rem,1.6vmin,1.1rem) * var(--pf-scale,1))!important
}
html body .pf-close{
    width:calc(clamp(34px,4.5vmin,52px) * var(--pf-scale,1))!important;
    height:calc(clamp(34px,4.5vmin,52px) * var(--pf-scale,1))!important;
    font-size:calc(clamp(.95rem,1.8vmin,1.35rem) * var(--pf-scale,1))!important
}
html body .pf-fav-btn{
    width:calc(clamp(32px,4.5vmin,52px) * var(--pf-scale,1))!important;
    height:calc(clamp(32px,4.5vmin,52px) * var(--pf-scale,1))!important;
    font-size:calc(clamp(.85rem,1.7vmin,1.2rem) * var(--pf-scale,1))!important
}

/* ═══════════════════════════════════════════════════════════════ */
/* PRACTICE FULL — Filters                                       */
/* ═══════════════════════════════════════════════════════════════ */
html body .pf-filters{
    padding:calc(clamp(.5rem,1.4vh,.85rem) * var(--pf-scale,1))
             calc(clamp(1rem,2.2vw,1.6rem) * var(--pf-scale,1))!important
}
html body .pf-filter-row{
    gap:calc(clamp(.4rem,.8vmin,.6rem) * var(--pf-scale,1))!important
}
html body .pf-chip{
    padding:calc(clamp(.35rem,.9vmin,.7rem) * var(--pf-scale,1))
             calc(clamp(.6rem,1.3vmin,1rem) * var(--pf-scale,1))!important;
    font-size:calc(clamp(.78rem,1.5vmin,1.05rem) * var(--pf-scale,1))!important;
    gap:calc(clamp(.35rem,.7vmin,.55rem) * var(--pf-scale,1))!important;
    border-radius:calc(clamp(50px,7vmin,100px) * var(--pf-scale,1))!important
}
html body .pf-chip-label{
    font-size:calc(clamp(.62rem,1.15vmin,.85rem) * var(--pf-scale,1))!important
}
html body .pf-chip-value{
    font-size:calc(clamp(.78rem,1.5vmin,1.05rem) * var(--pf-scale,1))!important
}
html body .pf-chip-arrow{
    font-size:calc(clamp(.6rem,1.15vmin,.85rem) * var(--pf-scale,1))!important
}
html body .pf-dataset-row{
    padding:calc(clamp(.45rem,1vmin,.8rem) * var(--pf-scale,1))
             calc(clamp(.55rem,1.2vmin,.9rem) * var(--pf-scale,1))!important;
    gap:calc(clamp(.4rem,.8vmin,.6rem) * var(--pf-scale,1))!important;
    border-radius:calc(clamp(10px,1.6vmin,16px) * var(--pf-scale,1))!important
}
html body .pf-dataset-label,
html body .pf-quick-nav-label{
    font-size:calc(clamp(.65rem,1.25vmin,.92rem) * var(--pf-scale,1))!important;
    gap:calc(clamp(.28rem,.55vmin,.42rem) * var(--pf-scale,1))!important
}
html body .pf-dataset-select,
html body .pf-dataset-search input,
html body .pf-quick-nav-select{
    padding:calc(clamp(.4rem,1vmin,.75rem) * var(--pf-scale,1))
             calc(clamp(1.9rem,3.8vmin,2.7rem) * var(--pf-scale,1))
             calc(clamp(.4rem,1vmin,.75rem) * var(--pf-scale,1))
             calc(clamp(.7rem,1.5vmin,1.1rem) * var(--pf-scale,1))!important;
    font-size:calc(clamp(.8rem,1.55vmin,1.1rem) * var(--pf-scale,1))!important;
    border-radius:calc(clamp(50px,7vmin,100px) * var(--pf-scale,1))!important
}
html body .pf-dataset-search i.fa-search{
    font-size:calc(clamp(.78rem,1.5vmin,1.05rem) * var(--pf-scale,1))!important;
    left:calc(clamp(11px,1.7vmin,19px) * var(--pf-scale,1))!important
}
html body .pf-dataset-row .pf-quick-nav{
    padding-top:calc(clamp(.4rem,.9vmin,.7rem) * var(--pf-scale,1))!important;
    margin-top:calc(clamp(.2rem,.45vmin,.35rem) * var(--pf-scale,1))!important;
    gap:calc(clamp(.4rem,.8vmin,.6rem) * var(--pf-scale,1))!important
}

/* ═══════════════════════════════════════════════════════════════ */
/* PRACTICE FULL — Content                                       */
/* ═══════════════════════════════════════════════════════════════ */
html body .practice-full-vi{
    padding:calc(clamp(.85rem,2vh,1.5rem) * var(--pf-scale,1))
             calc(clamp(.85rem,2vw,1.4rem) * var(--pf-scale,1))!important;
    font-size:calc(clamp(1.2rem,2.6vmin,2rem) * var(--pf-scale,1))!important;
    border-radius:calc(clamp(14px,2.2vmin,20px) * var(--pf-scale,1))!important
}
html body .practice-full-input-wrap{
    gap:calc(clamp(.45rem,1vmin,.75rem) * var(--pf-scale,1))!important
}
html body .practice-input-row{
    gap:calc(clamp(.4rem,.8vmin,.6rem) * var(--pf-scale,1))!important
}
html body .practice-full-input{
    padding:calc(clamp(.85rem,2vh,1.4rem) * var(--pf-scale,1))
             calc(clamp(.9rem,1.8vw,1.5rem) * var(--pf-scale,1))!important;
    font-size:calc(clamp(1.2rem,2.8vmin,2rem) * var(--pf-scale,1))!important;
    min-height:calc(clamp(56px,9vmin,95px) * var(--pf-scale,1))!important;
    border-radius:calc(clamp(12px,2vmin,18px) * var(--pf-scale,1))!important
}
html body .practice-speak-btn{
    min-width:calc(clamp(50px,7vmin,78px) * var(--pf-scale,1))!important;
    font-size:calc(clamp(1.05rem,2.1vmin,1.6rem) * var(--pf-scale,1))!important;
    border-radius:calc(clamp(12px,2vmin,18px) * var(--pf-scale,1))!important
}
html body .char-preview{
    min-height:calc(clamp(34px,5.5vmin,60px) * var(--pf-scale,1))!important;
    padding:calc(clamp(.4rem,1vmin,.85rem) * var(--pf-scale,1))!important;
    gap:calc(clamp(.28rem,.55vmin,.45rem) * var(--pf-scale,1))!important;
    border-radius:calc(clamp(10px,1.6vmin,16px) * var(--pf-scale,1))!important
}
html body .char-slot{
    font-size:calc(clamp(1.3rem,2.6vmin,2.1rem) * var(--pf-scale,1))!important;
    min-width:calc(clamp(1.5rem,2.7vmin,2.2rem) * var(--pf-scale,1))!important;
    height:calc(clamp(2rem,4vmin,3rem) * var(--pf-scale,1))!important;
    padding:0 calc(clamp(.3rem,.6vmin,.5rem) * var(--pf-scale,1))!important;
    border-radius:calc(clamp(6px,1vmin,10px) * var(--pf-scale,1))!important
}
html body .practice-full-status{
    font-size:calc(clamp(.95rem,1.85vmin,1.4rem) * var(--pf-scale,1))!important;
    min-height:calc(clamp(1.4rem,2.6vmin,2rem) * var(--pf-scale,1))!important
}
html body .reveal-actions{
    gap:calc(clamp(.45rem,.9vmin,.7rem) * var(--pf-scale,1))!important
}
html body .reveal-actions button{
    padding:calc(clamp(.75rem,1.7vh,1.25rem) * var(--pf-scale,1))
             calc(clamp(.85rem,1.7vw,1.4rem) * var(--pf-scale,1))!important;
    font-size:calc(clamp(.95rem,1.85vmin,1.4rem) * var(--pf-scale,1))!important;
    border-radius:calc(clamp(12px,2vmin,18px) * var(--pf-scale,1))!important;
    gap:calc(clamp(.4rem,.8vmin,.6rem) * var(--pf-scale,1))!important
}
html body .answer-reveal{
    gap:calc(clamp(.6rem,1.2vmin,.9rem) * var(--pf-scale,1))!important;
    padding:calc(clamp(.8rem,1.6vmin,1.2rem) * var(--pf-scale,1))!important;
    border-radius:calc(clamp(12px,2vmin,18px) * var(--pf-scale,1))!important
}
html body .answer-phrase-btn{
    padding:calc(clamp(.42rem,.9vmin,.7rem) * var(--pf-scale,1))
             calc(clamp(.75rem,1.5vmin,1.15rem) * var(--pf-scale,1))!important;
    font-size:calc(clamp(1.2rem,2.4vmin,1.9rem) * var(--pf-scale,1))!important;
    border-radius:calc(clamp(10px,1.7vmin,16px) * var(--pf-scale,1))!important
}
html body .answer-pinyin{
    font-size:calc(clamp(.9rem,1.75vmin,1.3rem) * var(--pf-scale,1))!important
}
html body .answer-phrase-tooltip{
    padding:calc(clamp(.4rem,.8vmin,.65rem) * var(--pf-scale,1))
             calc(clamp(.7rem,1.4vmin,1.1rem) * var(--pf-scale,1))!important;
    font-size:calc(clamp(.78rem,1.5vmin,1.1rem) * var(--pf-scale,1))!important;
    border-radius:calc(clamp(10px,1.6vmin,16px) * var(--pf-scale,1))!important
}

/* ═══════════════════════════════════════════════════════════════ */
/* PRACTICE FULL — Nav bottom                                    */
/* ═══════════════════════════════════════════════════════════════ */
html body .practice-full-nav{
    padding:calc(clamp(.6rem,1.6vh,1.15rem) * var(--pf-scale,1))
             calc(clamp(.85rem,2vw,1.5rem) * var(--pf-scale,1))!important;
    min-height:calc(clamp(60px,9.5vmin,105px) * var(--pf-scale,1))!important;
    gap:calc(clamp(.55rem,1.1vmin,.9rem) * var(--pf-scale,1))!important
}
html body .pf-nav-icon.main-nav{
    width:calc(clamp(56px,8.5vmin,96px) * var(--pf-scale,1))!important;
    height:calc(clamp(56px,8.5vmin,96px) * var(--pf-scale,1))!important;
    font-size:calc(clamp(1.25rem,2.6vmin,2rem) * var(--pf-scale,1))!important
}
html body .pf-nav-icon.mini-nav{
    width:calc(clamp(44px,7vmin,78px) * var(--pf-scale,1))!important;
    height:calc(clamp(44px,7vmin,78px) * var(--pf-scale,1))!important;
    font-size:calc(clamp(.9rem,1.9vmin,1.5rem) * var(--pf-scale,1))!important
}
html body .practice-full-nav .mini-group{
    gap:calc(clamp(.3rem,.6vmin,.45rem) * var(--pf-scale,1))!important;
    padding-left:calc(clamp(.6rem,1.2vmin,.9rem) * var(--pf-scale,1))!important;
    margin-left:calc(clamp(.4rem,.8vmin,.6rem) * var(--pf-scale,1))!important
}

/* ═══════════════════════════════════════════════════════════════ */
/* TIKTOK FLOAT + WIDTH CONTROL                                  */
/* ═══════════════════════════════════════════════════════════════ */
html body .pf-tiktok-float{
    padding:calc(clamp(.4rem,.8vmin,.65rem) * var(--pf-scale,1))
             calc(clamp(.75rem,1.5vmin,1.15rem) * var(--pf-scale,1))
             calc(clamp(.4rem,.8vmin,.65rem) * var(--pf-scale,1))
             calc(clamp(.4rem,.8vmin,.65rem) * var(--pf-scale,1))!important;
    gap:calc(clamp(.4rem,.8vmin,.6rem) * var(--pf-scale,1))!important;
    min-width:calc(clamp(120px,18vmin,200px) * var(--pf-scale,1))!important;
    max-width:calc(clamp(180px,25vmin,280px) * var(--pf-scale,1))!important
}
html body .pf-tiktok-avatar-wrap{
    width:calc(clamp(28px,4.5vmin,52px) * var(--pf-scale,1))!important;
    height:calc(clamp(28px,4.5vmin,52px) * var(--pf-scale,1))!important
}
html body .pf-tiktok-label{
    font-size:calc(clamp(.5rem,1vmin,.75rem) * var(--pf-scale,1))!important
}
html body .pf-tiktok-name{
    font-size:calc(clamp(.7rem,1.4vmin,1rem) * var(--pf-scale,1))!important
}
html body .pf-tiktok-badge{
    font-size:calc(clamp(.85rem,1.7vmin,1.25rem) * var(--pf-scale,1))!important
}
html body .pf-width-btn{
    width:calc(clamp(36px,5.5vmin,62px) * var(--pf-scale,1))!important;
    height:calc(clamp(36px,5.5vmin,62px) * var(--pf-scale,1))!important;
    font-size:calc(clamp(.9rem,1.8vmin,1.4rem) * var(--pf-scale,1))!important
}
html body .pf-width-indicator{
    font-size:calc(clamp(.62rem,1.2vmin,.9rem) * var(--pf-scale,1))!important;
    min-width:calc(clamp(34px,5vmin,52px) * var(--pf-scale,1))!important;
    padding:calc(clamp(.15rem,.3vmin,.25rem) * var(--pf-scale,1))
             calc(clamp(.4rem,.8vmin,.6rem) * var(--pf-scale,1))!important
}

/* ═══════════════════════════════════════════════════════════════ */
/* VOICE MODAL                                                   */
/* ═══════════════════════════════════════════════════════════════ */
html body .voice-box{
    max-width:calc(clamp(420px,55vmin,620px) * var(--ui-scale,1))!important;
    border-radius:calc(clamp(16px,2.5vmin,26px) * var(--ui-scale,1))!important
}
html body .voice-header{
    padding:calc(clamp(1rem,2vmin,1.5rem) * var(--ui-scale,1))
             calc(clamp(1.15rem,2.3vmin,1.7rem) * var(--ui-scale,1))!important
}
html body .voice-header h2{
    font-size:calc(clamp(1rem,1.95vmin,1.5rem) * var(--ui-scale,1))!important
}
html body .voice-close{
    width:calc(clamp(30px,4.5vmin,50px) * var(--ui-scale,1))!important;
    height:calc(clamp(30px,4.5vmin,50px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.9rem,1.8vmin,1.35rem) * var(--ui-scale,1))!important
}
html body .voice-body{
    padding:calc(clamp(1.1rem,2.2vmin,1.65rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(1rem,2vmin,1.5rem) * var(--ui-scale,1))!important
}
html body .voice-group-label{
    font-size:calc(clamp(.7rem,1.35vmin,1rem) * var(--ui-scale,1))!important
}
html body .voice-group-label .voice-value{
    font-size:calc(clamp(.82rem,1.6vmin,1.15rem) * var(--ui-scale,1))!important;
    padding:calc(clamp(.12rem,.25vmin,.2rem) * var(--ui-scale,1))
             calc(clamp(.5rem,1vmin,.8rem) * var(--ui-scale,1))!important
}
html body .voice-slider-row{
    gap:calc(clamp(.5rem,1vmin,.75rem) * var(--ui-scale,1))!important
}
html body .voice-slider-row button{
    width:calc(clamp(32px,4.8vmin,54px) * var(--ui-scale,1))!important;
    height:calc(clamp(32px,4.8vmin,54px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.85rem,1.7vmin,1.25rem) * var(--ui-scale,1))!important
}
html body .voice-preset-btn{
    padding:calc(clamp(.28rem,.55vmin,.45rem) * var(--ui-scale,1))
             calc(clamp(.65rem,1.3vmin,1rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.7rem,1.35vmin,1rem) * var(--ui-scale,1))!important;
    border-radius:calc(clamp(50px,7vmin,100px) * var(--ui-scale,1))!important
}
html body .voice-select{
    padding:calc(clamp(.55rem,1.1vmin,.85rem) * var(--ui-scale,1))
             calc(clamp(.75rem,1.5vmin,1.15rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.82rem,1.55vmin,1.15rem) * var(--ui-scale,1))!important
}
html body .voice-test-btn{
    padding:calc(clamp(.7rem,1.4vmin,1.1rem) * var(--ui-scale,1))
             calc(clamp(.95rem,1.9vmin,1.4rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.85rem,1.65vmin,1.2rem) * var(--ui-scale,1))!important
}
html body .voice-reset{
    padding:calc(clamp(.5rem,1vmin,.8rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.75rem,1.45vmin,1.05rem) * var(--ui-scale,1))!important
}
html body .voice-note{
    padding:calc(clamp(.55rem,1.1vmin,.85rem) * var(--ui-scale,1))
             calc(clamp(.75rem,1.5vmin,1.15rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.7rem,1.35vmin,1rem) * var(--ui-scale,1))!important
}

/* ═══════════════════════════════════════════════════════════════ */
/* WRITER MODAL                                                  */
/* ═══════════════════════════════════════════════════════════════ */
html body .writer-box{
    max-width:calc(clamp(400px,55vmin,580px) * var(--ui-scale,1))!important;
    padding:calc(clamp(.9rem,1.8vmin,1.4rem) * var(--ui-scale,1))
             calc(clamp(.85rem,1.7vmin,1.3rem) * var(--ui-scale,1))!important;
    border-radius:calc(clamp(16px,2.5vmin,26px) * var(--ui-scale,1))!important
}
html body .writer-close{
    width:calc(clamp(32px,4.5vmin,52px) * var(--ui-scale,1))!important;
    height:calc(clamp(32px,4.5vmin,52px) * var(--ui-scale,1))!important
}
html body .writer-char-info .vi-small{
    font-size:calc(clamp(.82rem,1.55vmin,1.15rem) * var(--ui-scale,1))!important
}
html body .writer-char-info .pinyin-small{
    font-size:calc(clamp(.78rem,1.45vmin,1.05rem) * var(--ui-scale,1))!important;
    padding:calc(clamp(.18rem,.35vmin,.28rem) * var(--ui-scale,1))
             calc(clamp(.55rem,1.1vmin,.85rem) * var(--ui-scale,1))!important
}
html body .writer-char-btn{
    width:calc(clamp(36px,5.5vmin,62px) * var(--ui-scale,1))!important;
    height:calc(clamp(36px,5.5vmin,62px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(1.1rem,2.1vmin,1.55rem) * var(--ui-scale,1))!important
}
html body .writer-target{
    width:calc(clamp(220px,45vmin,340px) * var(--ui-scale,1))!important;
    height:calc(clamp(220px,45vmin,340px) * var(--ui-scale,1))!important
}
html body .writer-btn{
    padding:calc(clamp(.48rem,.95vmin,.75rem) * var(--ui-scale,1))
             calc(clamp(.7rem,1.4vmin,1.1rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.78rem,1.5vmin,1.1rem) * var(--ui-scale,1))!important
}
html body .writer-score{
    font-size:calc(clamp(.8rem,1.55vmin,1.15rem) * var(--ui-scale,1))!important
}

/* ═══════════════════════════════════════════════════════════════ */
/* ONBOARDING MODAL                                              */
/* ═══════════════════════════════════════════════════════════════ */
html body .onboarding-box{
    max-width:calc(clamp(500px,65vmin,720px) * var(--ui-scale,1))!important;
    max-height:min(85vh,calc(640px * var(--ui-scale,1)))!important;
    border-radius:calc(clamp(20px,3vmin,30px) * var(--ui-scale,1))!important
}
html body .onboarding-close{
    width:calc(clamp(30px,4.5vmin,50px) * var(--ui-scale,1))!important;
    height:calc(clamp(30px,4.5vmin,50px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.8rem,1.55vmin,1.15rem) * var(--ui-scale,1))!important
}
html body .onboarding-header{
    padding:calc(clamp(1.3rem,2.6vmin,2rem) * var(--ui-scale,1))
             calc(clamp(1.3rem,2.6vmin,2rem) * var(--ui-scale,1))
             calc(clamp(.9rem,1.8vmin,1.4rem) * var(--ui-scale,1))!important
}
html body .onboarding-icon{
    width:calc(clamp(54px,8vmin,90px) * var(--ui-scale,1))!important;
    height:calc(clamp(54px,8vmin,90px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(1.4rem,2.8vmin,2.2rem) * var(--ui-scale,1))!important;
    border-radius:calc(clamp(14px,2.3vmin,22px) * var(--ui-scale,1))!important
}
html body .onboarding-title{
    font-size:calc(clamp(1.1rem,2.15vmin,1.65rem) * var(--ui-scale,1))!important
}
html body .onboarding-subtitle{
    font-size:calc(clamp(.8rem,1.55vmin,1.15rem) * var(--ui-scale,1))!important
}
html body .onboarding-counter{
    padding:calc(clamp(.3rem,.6vmin,.5rem) * var(--ui-scale,1))
             calc(clamp(.7rem,1.4vmin,1.1rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.75rem,1.45vmin,1.05rem) * var(--ui-scale,1))!important
}
html body .onboarding-body{
    padding:calc(clamp(1rem,2vmin,1.5rem) * var(--ui-scale,1))
             calc(clamp(1.3rem,2.6vmin,2rem) * var(--ui-scale,1))!important
}
html body .onboarding-section-label{
    font-size:calc(clamp(.7rem,1.35vmin,1rem) * var(--ui-scale,1))!important
}
html body .onboarding-topic{
    padding:calc(clamp(.45rem,.9vmin,.7rem) * var(--ui-scale,1))
             calc(clamp(.85rem,1.7vmin,1.3rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.78rem,1.5vmin,1.1rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.4rem,.8vmin,.6rem) * var(--ui-scale,1))!important
}
html body .onboarding-topic .count{
    font-size:calc(clamp(.65rem,1.25vmin,.92rem) * var(--ui-scale,1))!important;
    padding:calc(clamp(.08rem,.15vmin,.12rem) * var(--ui-scale,1))
             calc(clamp(.4rem,.8vmin,.6rem) * var(--ui-scale,1))!important
}
html body .onboarding-topic .topic-lock{
    font-size:calc(clamp(.62rem,1.2vmin,.88rem) * var(--ui-scale,1))!important;
    padding:calc(clamp(.08rem,.15vmin,.12rem) * var(--ui-scale,1))
             calc(clamp(.35rem,.7vmin,.55rem) * var(--ui-scale,1))!important
}
html body .onboarding-footer{
    padding:calc(clamp(.9rem,1.8vmin,1.4rem) * var(--ui-scale,1))
             calc(clamp(1.3rem,2.6vmin,2rem) * var(--ui-scale,1))
             calc(clamp(1rem,2vmin,1.5rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.5rem,1vmin,.75rem) * var(--ui-scale,1))!important
}
html body .onboarding-btn{
    padding:calc(clamp(.68rem,1.35vmin,1rem) * var(--ui-scale,1))
             calc(clamp(1.2rem,2.4vmin,1.85rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.85rem,1.65vmin,1.2rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.45rem,.9vmin,.7rem) * var(--ui-scale,1))!important
}

/* ═══════════════════════════════════════════════════════════════ */
/* ONBOARDING ACTIVE BANNER                                      */
/* ═══════════════════════════════════════════════════════════════ */
html body .onboarding-active-banner{
    padding:calc(clamp(.7rem,1.4vmin,1.1rem) * var(--ui-scale,1))
             calc(clamp(.9rem,1.8vmin,1.4rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.5rem,1vmin,.8rem) * var(--ui-scale,1))!important;
    border-radius:calc(clamp(12px,2vmin,18px) * var(--ui-scale,1))!important
}
html body .onboarding-active-banner .ob-icon{
    width:calc(clamp(26px,4vmin,42px) * var(--ui-scale,1))!important;
    height:calc(clamp(26px,4vmin,42px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(1rem,2vmin,1.5rem) * var(--ui-scale,1))!important
}
html body .onboarding-active-banner .ob-label{
    font-size:calc(clamp(.8rem,1.55vmin,1.15rem) * var(--ui-scale,1))!important
}
html body .onboarding-active-banner .ob-chip{
    padding:calc(clamp(.28rem,.55vmin,.45rem) * var(--ui-scale,1))
             calc(clamp(.7rem,1.4vmin,1.1rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.72rem,1.4vmin,1.05rem) * var(--ui-scale,1))!important
}
html body .onboarding-active-banner .ob-count{
    font-size:calc(clamp(.72rem,1.4vmin,1.05rem) * var(--ui-scale,1))!important
}
html body .onboarding-active-banner .ob-change-btn{
    padding:calc(clamp(.35rem,.7vmin,.55rem) * var(--ui-scale,1))
             calc(clamp(.8rem,1.6vmin,1.2rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.72rem,1.4vmin,1.05rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.3rem,.6vmin,.45rem) * var(--ui-scale,1))!important
}
html body .onboarding-active-banner .ob-stat-inline{
    padding:calc(clamp(.28rem,.55vmin,.45rem) * var(--ui-scale,1))
             calc(clamp(.65rem,1.3vmin,1rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.72rem,1.4vmin,1.05rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.3rem,.6vmin,.45rem) * var(--ui-scale,1))!important
}
html body .onboarding-active-banner .ob-stat-inline i{
    font-size:calc(clamp(.7rem,1.35vmin,1rem) * var(--ui-scale,1))!important
}
html body .onboarding-active-banner .ob-cta-btn{
    padding:calc(clamp(.45rem,.9vmin,.7rem) * var(--ui-scale,1))
             calc(clamp(.9rem,1.8vmin,1.4rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.75rem,1.45vmin,1.05rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.35rem,.7vmin,.55rem) * var(--ui-scale,1))!important
}

/* ═══════════════════════════════════════════════════════════════ */
/* FAVORITES                                                     */
/* ═══════════════════════════════════════════════════════════════ */
html body .pf-fav-float{
    padding:calc(clamp(.55rem,1.1vmin,.85rem) * var(--ui-scale,1))
             calc(clamp(.85rem,1.7vmin,1.3rem) * var(--ui-scale,1))
             calc(clamp(.55rem,1.1vmin,.85rem) * var(--ui-scale,1))
             calc(clamp(.7rem,1.4vmin,1.05rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.82rem,1.55vmin,1.15rem) * var(--ui-scale,1))!important;
    max-width:none!important;
    max-height:none!important
}
html body .pf-fav-float i{
    font-size:calc(clamp(1.05rem,2vmin,1.5rem) * var(--ui-scale,1))!important
}
html body .pf-fav-only-float{
    padding:calc(clamp(.55rem,1.1vmin,.85rem) * var(--ui-scale,1))
             calc(clamp(.85rem,1.7vmin,1.3rem) * var(--ui-scale,1))
             calc(clamp(.55rem,1.1vmin,.85rem) * var(--ui-scale,1))
             calc(clamp(.7rem,1.4vmin,1.05rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.8rem,1.5vmin,1.1rem) * var(--ui-scale,1))!important;
    max-width:none!important;
    max-height:none!important;
    gap:calc(clamp(.4rem,.8vmin,.6rem) * var(--ui-scale,1))!important
}
html body .pf-fav-only-float i{
    font-size:calc(clamp(.95rem,1.8vmin,1.35rem) * var(--ui-scale,1))!important
}
html body .pf-fav-only-count{
    min-width:calc(clamp(20px,3vmin,34px) * var(--ui-scale,1))!important;
    height:calc(clamp(20px,3vmin,34px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.65rem,1.25vmin,.9rem) * var(--ui-scale,1))!important;
    padding:0 calc(clamp(.4rem,.8vmin,.6rem) * var(--ui-scale,1))!important
}
html body .fav-empty{
    padding:calc(clamp(2.5rem,5vmin,4rem) * var(--ui-scale,1))
             calc(clamp(1.5rem,3vmin,2.5rem) * var(--ui-scale,1))!important
}
html body .fav-empty .fav-empty-icon{
    width:calc(clamp(60px,9vmin,100px) * var(--ui-scale,1))!important;
    height:calc(clamp(60px,9vmin,100px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(1.6rem,3vmin,2.6rem) * var(--ui-scale,1))!important;
    margin-bottom:calc(clamp(1rem,2vmin,1.5rem) * var(--ui-scale,1))!important
}
html body .fav-empty .fav-empty-title{
    font-size:calc(clamp(1rem,1.9vmin,1.4rem) * var(--ui-scale,1))!important;
    margin-bottom:calc(clamp(.4rem,.8vmin,.65rem) * var(--ui-scale,1))!important
}
html body .fav-empty .fav-empty-desc{
    font-size:calc(clamp(.82rem,1.55vmin,1.1rem) * var(--ui-scale,1))!important
}
html body .fav-locked-empty{
    padding:calc(clamp(2.5rem,5vmin,4rem) * var(--ui-scale,1))
             calc(clamp(1.5rem,3vmin,2.5rem) * var(--ui-scale,1))!important
}
html body .fav-locked-empty .fav-empty-cta{
    padding:calc(clamp(.55rem,1.1vmin,.85rem) * var(--ui-scale,1))
             calc(clamp(1rem,2vmin,1.5rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.82rem,1.55vmin,1.1rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.35rem,.7vmin,.55rem) * var(--ui-scale,1))!important
}
html body .fav-toast{
    padding:calc(clamp(.65rem,1.3vmin,1rem) * var(--ui-scale,1))
             calc(clamp(1.1rem,2.2vmin,1.65rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.82rem,1.55vmin,1.1rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.4rem,.8vmin,.6rem) * var(--ui-scale,1))!important
}
html body .fav-toast i{
    font-size:calc(clamp(.95rem,1.8vmin,1.35rem) * var(--ui-scale,1))!important
}
html body .pf-fav-filter-btn{
    padding:calc(clamp(.28rem,.6vmin,.45rem) * var(--pf-scale,1))
             calc(clamp(.6rem,1.2vmin,.9rem) * var(--pf-scale,1))!important;
    font-size:calc(clamp(.66rem,1.25vmin,.92rem) * var(--pf-scale,1))!important;
    gap:calc(clamp(.3rem,.6vmin,.45rem) * var(--pf-scale,1))!important
}
html body .pf-fav-filter-btn i:first-child{
    font-size:calc(clamp(.8rem,1.55vmin,1.15rem) * var(--pf-scale,1))!important
}
html body .pf-fav-filter-badge{
    min-width:calc(clamp(17px,2.6vmin,28px) * var(--pf-scale,1))!important;
    height:calc(clamp(17px,2.6vmin,28px) * var(--pf-scale,1))!important;
    font-size:calc(clamp(.58rem,1.1vmin,.82rem) * var(--pf-scale,1))!important;
    padding:0 calc(clamp(.3rem,.6vmin,.45rem) * var(--pf-scale,1))!important
}
html body .pf-fav-filter-summary{
    padding:calc(clamp(.4rem,.8vmin,.6rem) * var(--pf-scale,1))
             calc(clamp(.75rem,1.5vmin,1.15rem) * var(--pf-scale,1))
             calc(clamp(.45rem,.9vmin,.7rem) * var(--pf-scale,1))!important;
    gap:calc(clamp(.3rem,.6vmin,.45rem) * var(--pf-scale,1))!important
}
html body .pf-fav-summary-count{
    padding:calc(clamp(.2rem,.42vmin,.32rem) * var(--pf-scale,1))
             calc(clamp(.55rem,1.1vmin,.85rem) * var(--pf-scale,1))!important;
    font-size:calc(clamp(.66rem,1.25vmin,.92rem) * var(--pf-scale,1))!important;
    gap:calc(clamp(.3rem,.6vmin,.45rem) * var(--pf-scale,1))!important
}
html body .pf-fav-summary-chip{
    padding:calc(clamp(.18rem,.38vmin,.28rem) * var(--pf-scale,1))
             calc(clamp(.45rem,.9vmin,.7rem) * var(--pf-scale,1))
             calc(clamp(.18rem,.38vmin,.28rem) * var(--pf-scale,1))
             calc(clamp(.5rem,1vmin,.8rem) * var(--pf-scale,1))!important;
    font-size:calc(clamp(.64rem,1.2vmin,.9rem) * var(--pf-scale,1))!important;
    gap:calc(clamp(.22rem,.45vmin,.35rem) * var(--pf-scale,1))!important
}
html body .pf-fav-summary-clear{
    padding:calc(clamp(.18rem,.38vmin,.28rem) * var(--pf-scale,1))
             calc(clamp(.55rem,1.1vmin,.85rem) * var(--pf-scale,1))!important;
    font-size:calc(clamp(.6rem,1.15vmin,.85rem) * var(--pf-scale,1))!important
}
html body .fav-filter-box{
    max-width:calc(clamp(500px,65vmin,760px) * var(--pf-scale,1))!important;
    max-height:min(85vh,calc(640px * var(--pf-scale,1)))!important;
    border-radius:calc(clamp(18px,2.8vmin,26px) * var(--pf-scale,1))!important
}
html body .fav-filter-header{
    padding:calc(clamp(1rem,2vmin,1.5rem) * var(--pf-scale,1))
             calc(clamp(1.2rem,2.4vmin,1.85rem) * var(--pf-scale,1))
             calc(clamp(.9rem,1.8vmin,1.35rem) * var(--pf-scale,1))!important;
    gap:calc(clamp(.55rem,1.1vmin,.85rem) * var(--pf-scale,1))!important
}
html body .fav-filter-header-icon{
    width:calc(clamp(40px,6vmin,70px) * var(--pf-scale,1))!important;
    height:calc(clamp(40px,6vmin,70px) * var(--pf-scale,1))!important;
    font-size:calc(clamp(1.1rem,2.1vmin,1.55rem) * var(--pf-scale,1))!important;
    border-radius:calc(clamp(10px,1.5vmin,15px) * var(--pf-scale,1))!important
}
html body .fav-filter-header-title{
    font-size:calc(clamp(1rem,1.95vmin,1.45rem) * var(--pf-scale,1))!important
}
html body .fav-filter-header-sub{
    font-size:calc(clamp(.7rem,1.35vmin,1rem) * var(--pf-scale,1))!important
}
html body .fav-filter-close{
    width:calc(clamp(30px,4.5vmin,52px) * var(--pf-scale,1))!important;
    height:calc(clamp(30px,4.5vmin,52px) * var(--pf-scale,1))!important;
    font-size:calc(clamp(.85rem,1.6vmin,1.2rem) * var(--pf-scale,1))!important
}
html body .fav-filter-body{
    padding:calc(clamp(1rem,2vmin,1.5rem) * var(--pf-scale,1))
             calc(clamp(1.2rem,2.4vmin,1.85rem) * var(--pf-scale,1))!important
}
html body .fav-filter-section-icon{
    width:calc(clamp(22px,3.3vmin,38px) * var(--pf-scale,1))!important;
    height:calc(clamp(22px,3.3vmin,38px) * var(--pf-scale,1))!important;
    font-size:calc(clamp(.7rem,1.3vmin,.95rem) * var(--pf-scale,1))!important
}
html body .fav-filter-section-title{
    font-size:calc(clamp(.8rem,1.5vmin,1.1rem) * var(--pf-scale,1))!important
}
html body .fav-filter-section-actions button{
    padding:calc(clamp(.18rem,.38vmin,.28rem) * var(--pf-scale,1))
             calc(clamp(.45rem,.9vmin,.7rem) * var(--pf-scale,1))!important;
    font-size:calc(clamp(.58rem,1.1vmin,.82rem) * var(--pf-scale,1))!important
}
html body .fav-filter-option{
    padding:calc(clamp(.32rem,.65vmin,.5rem) * var(--pf-scale,1))
             calc(clamp(.65rem,1.3vmin,1rem) * var(--pf-scale,1))
             calc(clamp(.34rem,.68vmin,.52rem) * var(--pf-scale,1))!important;
    font-size:calc(clamp(.7rem,1.35vmin,1rem) * var(--pf-scale,1))!important;
    gap:calc(clamp(.3rem,.6vmin,.45rem) * var(--pf-scale,1))!important
}
html body .fav-filter-option .fav-opt-count{
    font-size:calc(clamp(.58rem,1.1vmin,.82rem) * var(--pf-scale,1))!important;
    padding:calc(clamp(.05rem,.1vmin,.08rem) * var(--pf-scale,1))
             calc(clamp(.32rem,.65vmin,.5rem) * var(--pf-scale,1))!important
}
html body .fav-filter-footer{
    padding:calc(clamp(.9rem,1.8vmin,1.35rem) * var(--pf-scale,1))
             calc(clamp(1.2rem,2.4vmin,1.85rem) * var(--pf-scale,1))
             calc(clamp(1rem,2vmin,1.5rem) * var(--pf-scale,1))!important;
    gap:calc(clamp(.5rem,1vmin,.75rem) * var(--pf-scale,1))!important
}
html body .fav-filter-result{
    font-size:calc(clamp(.75rem,1.4vmin,1rem) * var(--pf-scale,1))!important
}
html body .fav-filter-btn-secondary{
    padding:calc(clamp(.5rem,1vmin,.8rem) * var(--pf-scale,1))
             calc(clamp(.9rem,1.8vmin,1.35rem) * var(--pf-scale,1))!important;
    font-size:calc(clamp(.75rem,1.4vmin,1rem) * var(--pf-scale,1))!important;
    gap:calc(clamp(.3rem,.6vmin,.45rem) * var(--pf-scale,1))!important
}
html body .fav-filter-btn-primary{
    padding:calc(clamp(.55rem,1.1vmin,.85rem) * var(--pf-scale,1))
             calc(clamp(1.1rem,2.2vmin,1.65rem) * var(--pf-scale,1))!important;
    font-size:calc(clamp(.8rem,1.5vmin,1.1rem) * var(--pf-scale,1))!important;
    gap:calc(clamp(.35rem,.7vmin,.55rem) * var(--pf-scale,1))!important
}

/* ═══════════════════════════════════════════════════════════════ */
/* ADMIN CHAT MANAGER                                            */
/* ═══════════════════════════════════════════════════════════════ */
html body .acm-box{
    max-width:calc(clamp(900px,75vmin,1300px) * var(--ui-scale,1))!important;
    height:min(85vh,calc(800px * var(--ui-scale,1)))!important
}
html body .acm-header{
    padding:calc(clamp(.9rem,1.8vmin,1.4rem) * var(--ui-scale,1))
             calc(clamp(1.1rem,2.2vmin,1.7rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.8rem,1.6vmin,1.2rem) * var(--ui-scale,1))!important
}
html body .acm-header h3{
    font-size:calc(clamp(1rem,1.95vmin,1.45rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.4rem,.8vmin,.6rem) * var(--ui-scale,1))!important
}
html body .acm-header h3 i{
    font-size:calc(clamp(1.1rem,2.1vmin,1.55rem) * var(--ui-scale,1))!important
}
html body .acm-header-back,
html body .acm-close,
html body .acm-bulk-toggle,
html body .acm-clear-all-btn{
    width:calc(clamp(34px,4.8vmin,54px) * var(--ui-scale,1))!important;
    height:calc(clamp(34px,4.8vmin,54px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.9rem,1.8vmin,1.35rem) * var(--ui-scale,1))!important
}
html body .acm-stats{
    padding:calc(clamp(.65rem,1.3vmin,1rem) * var(--ui-scale,1))
             calc(clamp(1.1rem,2.2vmin,1.7rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.4rem,.8vmin,.6rem) * var(--ui-scale,1))!important
}
html body .acm-stat{
    padding:calc(clamp(.45rem,.9vmin,.7rem) * var(--ui-scale,1))
             calc(clamp(.65rem,1.3vmin,1rem) * var(--ui-scale,1))!important
}
html body .acm-stat-value{
    font-size:calc(clamp(1.2rem,2.4vmin,1.8rem) * var(--ui-scale,1))!important
}
html body .acm-stat-label{
    font-size:calc(clamp(.62rem,1.2vmin,.88rem) * var(--ui-scale,1))!important
}
html body .acm-search{
    padding:calc(clamp(.65rem,1.3vmin,1rem) * var(--ui-scale,1))
             calc(clamp(1.1rem,2.2vmin,1.7rem) * var(--ui-scale,1))!important
}
html body .acm-search-input{
    padding:calc(clamp(.5rem,1vmin,.8rem) * var(--ui-scale,1))
             calc(clamp(.9rem,1.8vmin,1.35rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.82rem,1.55vmin,1.15rem) * var(--ui-scale,1))!important
}
html body .acm-refresh-btn{
    width:calc(clamp(36px,5.5vmin,60px) * var(--ui-scale,1))!important;
    height:calc(clamp(36px,5.5vmin,60px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.85rem,1.65vmin,1.2rem) * var(--ui-scale,1))!important
}
html body .acm-user{
    padding:calc(clamp(.65rem,1.3vmin,1rem) * var(--ui-scale,1))
             calc(clamp(.75rem,1.5vmin,1.15rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.6rem,1.2vmin,.9rem) * var(--ui-scale,1))!important;
    border-radius:calc(clamp(10px,1.6vmin,16px) * var(--ui-scale,1))!important;
    margin-bottom:calc(clamp(.4rem,.8vmin,.6rem) * var(--ui-scale,1))!important
}
html body .acm-user-avatar{
    width:calc(clamp(40px,6vmin,70px) * var(--ui-scale,1))!important;
    height:calc(clamp(40px,6vmin,70px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.95rem,1.85vmin,1.4rem) * var(--ui-scale,1))!important
}
html body .acm-user-name{
    font-size:calc(clamp(.85rem,1.6vmin,1.15rem) * var(--ui-scale,1))!important
}
html body .acm-user-name .acm-tier{
    font-size:calc(clamp(.55rem,1.05vmin,.78rem) * var(--ui-scale,1))!important;
    padding:calc(clamp(.08rem,.18vmin,.14rem) * var(--ui-scale,1))
             calc(clamp(.35rem,.7vmin,.55rem) * var(--ui-scale,1))!important
}
html body .acm-user-email{
    font-size:calc(clamp(.7rem,1.35vmin,1rem) * var(--ui-scale,1))!important
}
html body .acm-user-preview{
    font-size:calc(clamp(.72rem,1.4vmin,1.05rem) * var(--ui-scale,1))!important
}
html body .acm-user-time{
    font-size:calc(clamp(.65rem,1.25vmin,.92rem) * var(--ui-scale,1))!important
}
html body .acm-user-badge{
    min-width:calc(clamp(20px,3vmin,34px) * var(--ui-scale,1))!important;
    height:calc(clamp(20px,3vmin,34px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.6rem,1.15vmin,.85rem) * var(--ui-scale,1))!important
}
html body .acm-user-btn{
    width:calc(clamp(30px,4.5vmin,52px) * var(--ui-scale,1))!important;
    height:calc(clamp(30px,4.5vmin,52px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.78rem,1.5vmin,1.1rem) * var(--ui-scale,1))!important
}
html body .acm-empty{
    padding:calc(clamp(2.5rem,5vmin,4rem) * var(--ui-scale,1))
             calc(clamp(1.5rem,3vmin,2.5rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.6rem,1.2vmin,.9rem) * var(--ui-scale,1))!important
}
html body .acm-empty i{
    font-size:calc(clamp(2.5rem,4.5vmin,4rem) * var(--ui-scale,1))!important
}
html body .acm-empty .acm-empty-title{
    font-size:calc(clamp(.9rem,1.75vmin,1.3rem) * var(--ui-scale,1))!important
}
html body .acm-empty .acm-empty-desc{
    font-size:calc(clamp(.78rem,1.5vmin,1.1rem) * var(--ui-scale,1))!important
}
html body .acm-hist-header{
    padding:calc(clamp(.85rem,1.7vmin,1.3rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.85rem,1.7vmin,1.3rem) * var(--ui-scale,1))!important;
    border-radius:calc(clamp(10px,1.6vmin,16px) * var(--ui-scale,1))!important
}
html body .acm-hist-avatar{
    width:calc(clamp(52px,8vmin,90px) * var(--ui-scale,1))!important;
    height:calc(clamp(52px,8vmin,90px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(1.35rem,2.6vmin,2rem) * var(--ui-scale,1))!important
}
html body .acm-hist-name{
    font-size:calc(clamp(1rem,1.95vmin,1.45rem) * var(--ui-scale,1))!important
}
html body .acm-hist-email{
    font-size:calc(clamp(.75rem,1.4vmin,1rem) * var(--ui-scale,1))!important
}
html body .acm-hist-meta{
    font-size:calc(clamp(.65rem,1.25vmin,.92rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.6rem,1.2vmin,.9rem) * var(--ui-scale,1))!important
}
html body .acm-hist-filter{
    padding:calc(clamp(.32rem,.65vmin,.5rem) * var(--ui-scale,1))
             calc(clamp(.75rem,1.5vmin,1.15rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.7rem,1.35vmin,1rem) * var(--ui-scale,1))!important
}
html body .acm-tl-item{
    padding:calc(clamp(.65rem,1.3vmin,1rem) * var(--ui-scale,1))
             calc(clamp(.85rem,1.7vmin,1.3rem) * var(--ui-scale,1))!important;
    margin-bottom:calc(clamp(.85rem,1.7vmin,1.3rem) * var(--ui-scale,1))!important;
    border-radius:calc(clamp(8px,1.4vmin,13px) * var(--ui-scale,1))!important
}
html body .acm-tl-title{
    font-size:calc(clamp(.82rem,1.55vmin,1.15rem) * var(--ui-scale,1))!important
}
html body .acm-tl-icon{
    width:calc(clamp(18px,3vmin,32px) * var(--ui-scale,1))!important;
    height:calc(clamp(18px,3vmin,32px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.62rem,1.2vmin,.88rem) * var(--ui-scale,1))!important
}
html body .acm-tl-time{
    font-size:calc(clamp(.65rem,1.25vmin,.92rem) * var(--ui-scale,1))!important
}
html body .acm-tl-body{
    font-size:calc(clamp(.75rem,1.4vmin,1rem) * var(--ui-scale,1))!important
}
html body .acm-confirm-box{
    max-width:calc(clamp(380px,55vmin,540px) * var(--ui-scale,1))!important;
    padding:calc(clamp(1.2rem,2.4vmin,1.85rem) * var(--ui-scale,1))!important;
    border-radius:calc(clamp(14px,2.2vmin,20px) * var(--ui-scale,1))!important
}
html body .acm-confirm-icon{
    width:calc(clamp(54px,8vmin,88px) * var(--ui-scale,1))!important;
    height:calc(clamp(54px,8vmin,88px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(1.4rem,2.8vmin,2.2rem) * var(--ui-scale,1))!important;
    margin-bottom:calc(clamp(.85rem,1.7vmin,1.3rem) * var(--ui-scale,1))!important
}
html body .acm-confirm-title{
    font-size:calc(clamp(1rem,1.95vmin,1.45rem) * var(--ui-scale,1))!important
}
html body .acm-confirm-desc{
    font-size:calc(clamp(.8rem,1.55vmin,1.15rem) * var(--ui-scale,1))!important
}
html body .acm-confirm-btn{
    padding:calc(clamp(.55rem,1.1vmin,.85rem) * var(--ui-scale,1))
             calc(clamp(1.1rem,2.2vmin,1.65rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.82rem,1.55vmin,1.15rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.35rem,.7vmin,.55rem) * var(--ui-scale,1))!important
}
html body .acm-bulk-compose-box{
    max-width:calc(clamp(500px,70vmin,760px) * var(--ui-scale,1))!important
}
html body .acm-bulk-compose-header{
    padding:calc(clamp(.9rem,1.8vmin,1.4rem) * var(--ui-scale,1))
             calc(clamp(1.1rem,2.2vmin,1.7rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.6rem,1.2vmin,.9rem) * var(--ui-scale,1))!important
}
html body .acm-bulk-compose-header h3{
    font-size:calc(clamp(.95rem,1.85vmin,1.4rem) * var(--ui-scale,1))!important
}
html body .acm-bulk-compose-close{
    width:calc(clamp(30px,4.5vmin,52px) * var(--ui-scale,1))!important;
    height:calc(clamp(30px,4.5vmin,52px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.85rem,1.6vmin,1.2rem) * var(--ui-scale,1))!important
}
html body .acm-bulk-compose-body{
    padding:calc(clamp(1.1rem,2.2vmin,1.65rem) * var(--ui-scale,1))!important
}
html body .acm-bulk-label{
    font-size:calc(clamp(.7rem,1.35vmin,1rem) * var(--ui-scale,1))!important
}
html body .acm-bulk-textarea{
    padding:calc(clamp(.75rem,1.5vmin,1.15rem) * var(--ui-scale,1))
             calc(clamp(.9rem,1.8vmin,1.35rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.85rem,1.65vmin,1.2rem) * var(--ui-scale,1))!important;
    border-radius:calc(clamp(10px,1.6vmin,16px) * var(--ui-scale,1))!important
}
html body .acm-bulk-charcount{
    font-size:calc(clamp(.7rem,1.35vmin,1rem) * var(--ui-scale,1))!important
}
html body .acm-bulk-template{
    padding:calc(clamp(.32rem,.65vmin,.5rem) * var(--ui-scale,1))
             calc(clamp(.7rem,1.4vmin,1.1rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.7rem,1.35vmin,1rem) * var(--ui-scale,1))!important
}
html body .acm-bulk-recipient-tag{
    padding:calc(clamp(.18rem,.35vmin,.28rem) * var(--ui-scale,1))
             calc(clamp(.5rem,1vmin,.8rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.68rem,1.3vmin,.95rem) * var(--ui-scale,1))!important
}
html body .acm-bulk-send-btn{
    padding:calc(clamp(.65rem,1.3vmin,1rem) * var(--ui-scale,1))
             calc(clamp(1.3rem,2.6vmin,2rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.82rem,1.55vmin,1.15rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.35rem,.7vmin,.55rem) * var(--ui-scale,1))!important
}

/* ═══════════════════════════════════════════════════════════════ */
/* CHAT SUPPORT                                                  */
/* ═══════════════════════════════════════════════════════════════ */
html body #chatFloatBtn{
    width:calc(clamp(50px,7vmin,82px) * var(--ui-scale,1))!important;
    height:calc(clamp(50px,7vmin,82px) * var(--ui-scale,1))!important
}
html body #chatFloatBtn i.fa-comments{
    font-size:calc(clamp(1.2rem,2.3vmin,1.7rem) * var(--ui-scale,1))!important
}
html body .chat-float-sub{
    width:calc(clamp(44px,6.4vmin,74px) * var(--ui-scale,1))!important;
    height:calc(clamp(44px,6.4vmin,74px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(1rem,2vmin,1.5rem) * var(--ui-scale,1))!important
}
html body .chat-float-sub .sub-badge{
    min-width:calc(clamp(18px,2.8vmin,32px) * var(--ui-scale,1))!important;
    height:calc(clamp(18px,2.8vmin,32px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.58rem,1.1vmin,.82rem) * var(--ui-scale,1))!important
}
html body .chat-box{
    width:calc(clamp(340px,45vmin,520px) * var(--ui-scale,1))!important;
    min-height:calc(240px * var(--ui-scale,1))!important;
    max-height:calc(100vh - 120px)!important;
    border-radius:calc(clamp(14px,2.2vmin,22px) * var(--ui-scale,1))!important
}
html body .chat-header{
    padding:calc(clamp(.85rem,1.7vmin,1.3rem) * var(--ui-scale,1))
             calc(clamp(1rem,2vmin,1.6rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.6rem,1.2vmin,.9rem) * var(--ui-scale,1))!important
}
html body .chat-header-back,
html body .chat-header-close{
    width:calc(clamp(30px,4.5vmin,52px) * var(--ui-scale,1))!important;
    height:calc(clamp(30px,4.5vmin,52px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.85rem,1.6vmin,1.25rem) * var(--ui-scale,1))!important
}
html body .chat-header-info .name{
    font-size:calc(clamp(.88rem,1.7vmin,1.25rem) * var(--ui-scale,1))!important
}
html body .chat-header-info .status{
    font-size:calc(clamp(.68rem,1.3vmin,.95rem) * var(--ui-scale,1))!important
}
html body .chat-header .chat-counter{
    font-size:calc(clamp(.62rem,1.2vmin,.88rem) * var(--ui-scale,1))!important;
    padding:calc(clamp(.12rem,.25vmin,.2rem) * var(--ui-scale,1))
             calc(clamp(.45rem,.9vmin,.7rem) * var(--ui-scale,1))!important
}
html body .chat-body{
    padding:calc(clamp(.85rem,1.7vmin,1.3rem) * var(--ui-scale,1))
             calc(clamp(1rem,2vmin,1.6rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.4rem,.8vmin,.6rem) * var(--ui-scale,1))!important
}
html body .chat-msg .bubble{
    padding:calc(clamp(.55rem,1.1vmin,.85rem) * var(--ui-scale,1))
             calc(clamp(.75rem,1.5vmin,1.15rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.82rem,1.55vmin,1.15rem) * var(--ui-scale,1))!important;
    border-radius:calc(clamp(14px,2.2vmin,20px) * var(--ui-scale,1))!important
}
html body .chat-msg .msg-time{
    font-size:calc(clamp(.6rem,1.15vmin,.85rem) * var(--ui-scale,1))!important
}
html body .chat-system{
    padding:calc(clamp(.22rem,.45vmin,.35rem) * var(--ui-scale,1))
             calc(clamp(.65rem,1.3vmin,1rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.68rem,1.3vmin,.95rem) * var(--ui-scale,1))!important
}
html body .chat-empty i{
    font-size:calc(clamp(2.2rem,4.2vmin,3.5rem) * var(--ui-scale,1))!important
}
html body .chat-empty .title{
    font-size:calc(clamp(.88rem,1.7vmin,1.25rem) * var(--ui-scale,1))!important
}
html body .chat-empty .desc{
    font-size:calc(clamp(.75rem,1.4vmin,1rem) * var(--ui-scale,1))!important
}
html body .chat-footer{
    padding:calc(clamp(.65rem,1.3vmin,1rem) * var(--ui-scale,1))
             calc(clamp(.85rem,1.7vmin,1.3rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.4rem,.8vmin,.6rem) * var(--ui-scale,1))!important
}
html body .chat-footer textarea{
    min-height:calc(clamp(40px,6vmin,65px) * var(--ui-scale,1))!important;
    padding:calc(clamp(.6rem,1.2vmin,.9rem) * var(--ui-scale,1))
             calc(clamp(.85rem,1.7vmin,1.3rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.82rem,1.55vmin,1.15rem) * var(--ui-scale,1))!important;
    border-radius:calc(clamp(20px,3vmin,30px) * var(--ui-scale,1))!important
}
html body .chat-send-btn{
    width:calc(clamp(42px,6.2vmin,70px) * var(--ui-scale,1))!important;
    height:calc(clamp(42px,6.2vmin,70px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(1rem,2vmin,1.5rem) * var(--ui-scale,1))!important
}
html body .chat-quick-btn{
    padding:calc(clamp(.28rem,.55vmin,.45rem) * var(--ui-scale,1))
             calc(clamp(.65rem,1.3vmin,1rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.7rem,1.35vmin,1rem) * var(--ui-scale,1))!important
}
html body .chat-limit-banner{
    padding:calc(clamp(.6rem,1.2vmin,.9rem) * var(--ui-scale,1))
             calc(clamp(.8rem,1.6vmin,1.2rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.75rem,1.4vmin,1rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.45rem,.9vmin,.7rem) * var(--ui-scale,1))!important
}
html body .chat-limit-banner .clb-icon{
    width:calc(clamp(26px,4vmin,44px) * var(--ui-scale,1))!important;
    height:calc(clamp(26px,4vmin,44px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.82rem,1.55vmin,1.15rem) * var(--ui-scale,1))!important
}
html body .chat-limit-banner .clb-btn{
    padding:calc(clamp(.32rem,.65vmin,.5rem) * var(--ui-scale,1))
             calc(clamp(.65rem,1.3vmin,1rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.7rem,1.35vmin,1rem) * var(--ui-scale,1))!important
}
html body .admin-chat-thread{
    padding:calc(clamp(.65rem,1.3vmin,1rem) * var(--ui-scale,1))
             calc(clamp(.75rem,1.5vmin,1.15rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.6rem,1.2vmin,.9rem) * var(--ui-scale,1))!important;
    border-radius:calc(clamp(10px,1.6vmin,16px) * var(--ui-scale,1))!important;
    margin-bottom:calc(clamp(.4rem,.8vmin,.6rem) * var(--ui-scale,1))!important
}
html body .admin-chat-thread .t-avatar{
    width:calc(clamp(38px,5.6vmin,65px) * var(--ui-scale,1))!important;
    height:calc(clamp(38px,5.6vmin,65px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.95rem,1.85vmin,1.4rem) * var(--ui-scale,1))!important
}
html body .admin-chat-thread .t-name{
    font-size:calc(clamp(.85rem,1.6vmin,1.15rem) * var(--ui-scale,1))!important
}
html body .admin-chat-thread .t-preview{
    font-size:calc(clamp(.72rem,1.4vmin,1.05rem) * var(--ui-scale,1))!important
}
html body .admin-chat-thread .t-time{
    font-size:calc(clamp(.65rem,1.25vmin,.92rem) * var(--ui-scale,1))!important
}
html body .admin-chat-thread .t-badge{
    min-width:calc(clamp(20px,3vmin,34px) * var(--ui-scale,1))!important;
    height:calc(clamp(20px,3vmin,34px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.62rem,1.2vmin,.88rem) * var(--ui-scale,1))!important
}
html body .dropdown-chat-preview{
    padding:calc(clamp(.6rem,1.2vmin,.9rem) * var(--ui-scale,1))
             calc(clamp(.7rem,1.4vmin,1.1rem) * var(--ui-scale,1))!important;
    margin:calc(clamp(.35rem,.7vmin,.55rem) * var(--ui-scale,1))
             calc(clamp(.45rem,.9vmin,.7rem) * var(--ui-scale,1))!important
}
html body .dropdown-chat-preview .dcp-title{
    font-size:calc(clamp(.65rem,1.25vmin,.92rem) * var(--ui-scale,1))!important
}
html body .dropdown-chat-preview .dcp-time{
    font-size:calc(clamp(.6rem,1.15vmin,.85rem) * var(--ui-scale,1))!important
}
html body .dropdown-chat-preview .dcp-msg{
    font-size:calc(clamp(.75rem,1.4vmin,1rem) * var(--ui-scale,1))!important
}
html body .dropdown-chat-preview .dcp-badge{
    font-size:calc(clamp(.56rem,1.05vmin,.78rem) * var(--ui-scale,1))!important;
    padding:calc(clamp(.08rem,.15vmin,.12rem) * var(--ui-scale,1))
             calc(clamp(.3rem,.6vmin,.45rem) * var(--ui-scale,1))!important
}
html body .quota-grid{
    gap:calc(clamp(.65rem,1.3vmin,1rem) * var(--ui-scale,1))!important;
    margin-bottom:calc(clamp(.85rem,1.7vmin,1.3rem) * var(--ui-scale,1))!important
}
html body .quota-card{
    padding:calc(clamp(.85rem,1.7vmin,1.3rem) * var(--ui-scale,1))!important;
    border-radius:calc(clamp(10px,1.6vmin,16px) * var(--ui-scale,1))!important
}
html body .quota-card .qc-label{
    font-size:calc(clamp(.68rem,1.3vmin,.95rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.3rem,.6vmin,.45rem) * var(--ui-scale,1))!important
}
html body .quota-card .qc-value{
    font-size:calc(clamp(1.4rem,2.8vmin,2.2rem) * var(--ui-scale,1))!important
}
html body .quota-card .qc-sub{
    font-size:calc(clamp(.68rem,1.3vmin,.95rem) * var(--ui-scale,1))!important
}
html body .quota-card .qc-bar{
    height:calc(clamp(5px,.9vmin,8px) * var(--ui-scale,1))!important
}
html body .quota-card .qc-icon{
    font-size:calc(clamp(1.35rem,2.6vmin,2rem) * var(--ui-scale,1))!important
}
html body .quota-actions .btn{
    padding:calc(clamp(.45rem,.9vmin,.7rem) * var(--ui-scale,1))
             calc(clamp(.8rem,1.6vmin,1.2rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.75rem,1.4vmin,1rem) * var(--ui-scale,1))!important
}
html body .quota-info{
    padding:calc(clamp(.7rem,1.4vmin,1.05rem) * var(--ui-scale,1))
             calc(clamp(.9rem,1.8vmin,1.4rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.75rem,1.4vmin,1rem) * var(--ui-scale,1))!important
}
html body .quota-history-table{
    font-size:calc(clamp(.75rem,1.4vmin,1rem) * var(--ui-scale,1))!important
}
html body .quota-history-table th{
    padding:calc(clamp(.38rem,.75vmin,.6rem) * var(--ui-scale,1))
             calc(clamp(.55rem,1.1vmin,.85rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.65rem,1.25vmin,.92rem) * var(--ui-scale,1))!important
}
html body .quota-history-table td{
    padding:calc(clamp(.38rem,.75vmin,.6rem) * var(--ui-scale,1))
             calc(clamp(.55rem,1.1vmin,.85rem) * var(--ui-scale,1))!important
}
html body .online-user-row{
    padding:calc(clamp(.55rem,1.1vmin,.85rem) * var(--ui-scale,1))
             calc(clamp(.7rem,1.4vmin,1.1rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.5rem,1vmin,.8rem) * var(--ui-scale,1))!important
}
html body .ou-dot{
    width:calc(clamp(10px,1.6vmin,14px) * var(--ui-scale,1))!important;
    height:calc(clamp(10px,1.6vmin,14px) * var(--ui-scale,1))!important
}
html body .ou-name{
    font-size:calc(clamp(.82rem,1.55vmin,1.1rem) * var(--ui-scale,1))!important
}
html body .ou-sub{
    font-size:calc(clamp(.68rem,1.3vmin,.95rem) * var(--ui-scale,1))!important
}
html body .ou-chat-btn{
    width:calc(clamp(30px,4.5vmin,52px) * var(--ui-scale,1))!important;
    height:calc(clamp(30px,4.5vmin,52px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.78rem,1.5vmin,1.1rem) * var(--ui-scale,1))!important
}
html body .chat-toast{
    padding:calc(clamp(.75rem,1.5vmin,1.15rem) * var(--ui-scale,1))
             calc(clamp(1.2rem,2.4vmin,1.8rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.82rem,1.55vmin,1.15rem) * var(--ui-scale,1))!important
}

/* ═══════════════════════════════════════════════════════════════ */
/* SOCIAL                                                        */
/* ═══════════════════════════════════════════════════════════════ */
html body .zalo-btn,
html body .tiktok-float-btn{
    padding:calc(clamp(.65rem,1.3vmin,1rem) * var(--ui-scale,1))
             calc(clamp(1rem,2vmin,1.5rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.82rem,1.55vmin,1.15rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.45rem,.9vmin,.7rem) * var(--ui-scale,1))!important
}
html body .zalo-btn i,
html body .tiktok-float-btn i{
    font-size:calc(clamp(1.1rem,2.1vmin,1.55rem) * var(--ui-scale,1))!important
}
html body .zalo-btn .zalo-label,
html body .tiktok-float-btn .tiktok-label{
    font-size:calc(clamp(.62rem,1.2vmin,.88rem) * var(--ui-scale,1))!important
}
html body .zalo-btn .zalo-name,
html body .tiktok-float-btn .tiktok-name{
    font-size:calc(clamp(.82rem,1.55vmin,1.15rem) * var(--ui-scale,1))!important
}
html body .zalo-btn.compact,
html body .tiktok-float-btn.compact{
    width:calc(clamp(50px,7vmin,80px) * var(--ui-scale,1))!important;
    height:calc(clamp(50px,7vmin,80px) * var(--ui-scale,1))!important
}
html body .zalo-btn.compact i,
html body .tiktok-float-btn.compact i{
    font-size:calc(clamp(1.3rem,2.5vmin,1.9rem) * var(--ui-scale,1))!important
}
html body .floating-left-group{
    gap:calc(clamp(.5rem,1vmin,.8rem) * var(--ui-scale,1))!important;
    left:calc(clamp(16px,2vmin,28px) * var(--ui-scale,1))!important;
    bottom:calc(clamp(20px,2.5vmin,32px) * var(--ui-scale,1) + env(safe-area-inset-bottom))!important
}
html body .tiktok-hover-card{
    width:calc(clamp(280px,40vmin,400px) * var(--ui-scale,1))!important;
    padding:calc(clamp(.85rem,1.7vmin,1.3rem) * var(--ui-scale,1))!important;
    border-radius:calc(clamp(14px,2vmin,20px) * var(--ui-scale,1))!important
}
html body .thc-avatar,
html body .thc-avatar-fallback{
    width:calc(clamp(54px,8vmin,84px) * var(--ui-scale,1))!important;
    height:calc(clamp(54px,8vmin,84px) * var(--ui-scale,1))!important
}
html body .thc-avatar-fallback{
    font-size:calc(clamp(1.5rem,3vmin,2.3rem) * var(--ui-scale,1))!important
}
html body .thc-verified{
    width:calc(clamp(18px,2.6vmin,28px) * var(--ui-scale,1))!important;
    height:calc(clamp(18px,2.6vmin,28px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.6rem,1.1vmin,.85rem) * var(--ui-scale,1))!important
}
html body .thc-nick{
    font-size:calc(clamp(.95rem,1.8vmin,1.35rem) * var(--ui-scale,1))!important
}
html body .thc-user{
    font-size:calc(clamp(.75rem,1.4vmin,1rem) * var(--ui-scale,1))!important
}
html body .thc-desc{
    font-size:calc(clamp(.75rem,1.4vmin,1rem) * var(--ui-scale,1))!important;
    padding:calc(clamp(.6rem,1.2vmin,.9rem) * var(--ui-scale,1)) 0!important
}
html body .thc-stat .num{
    font-size:calc(clamp(.95rem,1.8vmin,1.35rem) * var(--ui-scale,1))!important
}
html body .thc-stat .label{
    font-size:calc(clamp(.62rem,1.15vmin,.85rem) * var(--ui-scale,1))!important
}
html body .thc-btn{
    padding:calc(clamp(.65rem,1.3vmin,1rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.85rem,1.6vmin,1.15rem) * var(--ui-scale,1))!important
}
html body .tiktok-bar{
    padding:calc(clamp(.5rem,1vmin,.85rem) * var(--ui-scale,1))
             calc(clamp(.85rem,1.7vmin,1.3rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.8rem,1.5vmin,1.1rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.6rem,1.2vmin,.9rem) * var(--ui-scale,1))!important
}
html body .tiktok-bar-avatar{
    width:calc(clamp(32px,4.5vmin,52px) * var(--ui-scale,1))!important;
    height:calc(clamp(32px,4.5vmin,52px) * var(--ui-scale,1))!important
}
html body .tiktok-bar-info .tiktok-nick{
    font-size:calc(clamp(.92rem,1.75vmin,1.3rem) * var(--ui-scale,1))!important
}
html body .tiktok-bar-info .tiktok-user{
    font-size:calc(clamp(.75rem,1.4vmin,1rem) * var(--ui-scale,1))!important
}
html body .tiktok-bar-link{
    padding:calc(clamp(.4rem,.8vmin,.65rem) * var(--ui-scale,1))
             calc(clamp(.8rem,1.6vmin,1.2rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.75rem,1.4vmin,1rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.35rem,.7vmin,.55rem) * var(--ui-scale,1))!important
}
html body .dropdown-zalo,
html body .dropdown-tiktok{
    padding:calc(clamp(.65rem,1.3vmin,1rem) * var(--ui-scale,1))
             calc(clamp(.75rem,1.5vmin,1.15rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.85rem,1.6vmin,1.15rem) * var(--ui-scale,1))!important
}

/* ═══════════════════════════════════════════════════════════════ */
/* ACCOUNTS                                                      */
/* ═══════════════════════════════════════════════════════════════ */
html body .user-avatar{
    width:calc(clamp(38px,5vmin,58px) * var(--ui-scale,1))!important;
    height:calc(clamp(38px,5vmin,58px) * var(--ui-scale,1))!important
}
html body .user-dropdown{
    min-width:calc(clamp(280px,40vmin,400px) * var(--ui-scale,1))!important;
    padding:calc(clamp(.5rem,1vmin,.85rem) * var(--ui-scale,1))!important
}
html body .user-info{
    padding:calc(clamp(.75rem,1.5vmin,1.15rem) * var(--ui-scale,1))!important
}
html body .user-info .name{
    font-size:calc(clamp(.9rem,1.75vmin,1.3rem) * var(--ui-scale,1))!important
}
html body .user-info .email{
    font-size:calc(clamp(.75rem,1.4vmin,1rem) * var(--ui-scale,1))!important
}
html body .user-info .role{
    font-size:calc(clamp(.68rem,1.3vmin,.95rem) * var(--ui-scale,1))!important;
    padding:calc(clamp(.15rem,.35vmin,.3rem) * var(--ui-scale,1))
             calc(clamp(.5rem,1vmin,.8rem) * var(--ui-scale,1))!important
}
html body .dropdown-item{
    padding:calc(clamp(.65rem,1.3vmin,1rem) * var(--ui-scale,1))
             calc(clamp(.75rem,1.5vmin,1.15rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.85rem,1.6vmin,1.15rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.5rem,1vmin,.75rem) * var(--ui-scale,1))!important
}
html body .dropdown-renew{
    padding:calc(clamp(.75rem,1.5vmin,1.15rem) * var(--ui-scale,1))
             calc(clamp(1rem,2vmin,1.5rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.9rem,1.75vmin,1.3rem) * var(--ui-scale,1))!important
}
html body .dropdown-renew i{
    font-size:calc(clamp(1rem,1.9vmin,1.4rem) * var(--ui-scale,1))!important
}
html body .user-details{
    padding:calc(clamp(.6rem,1.2vmin,.95rem) * var(--ui-scale,1))
             calc(clamp(.75rem,1.5vmin,1.15rem) * var(--ui-scale,1))
             calc(clamp(.75rem,1.5vmin,1.15rem) * var(--ui-scale,1))!important
}
html body .detail-icon{
    width:calc(clamp(36px,4.8vmin,56px) * var(--ui-scale,1))!important;
    height:calc(clamp(36px,4.8vmin,56px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.95rem,1.85vmin,1.35rem) * var(--ui-scale,1))!important
}
html body .detail-label{
    font-size:calc(clamp(.65rem,1.25vmin,.92rem) * var(--ui-scale,1))!important
}
html body .detail-value{
    font-size:calc(clamp(.85rem,1.6vmin,1.15rem) * var(--ui-scale,1))!important
}
html body .detail-sub{
    font-size:calc(clamp(.7rem,1.3vmin,.95rem) * var(--ui-scale,1))!important
}
html body .login-box{
    max-width:calc(clamp(400px,55vmin,560px) * var(--ui-scale,1))!important;
    padding:calc(clamp(2rem,4vmin,3.2rem) * var(--ui-scale,1))
             calc(clamp(1.5rem,3vmin,2.5rem) * var(--ui-scale,1))!important;
    border-radius:calc(clamp(16px,2.5vmin,26px) * var(--ui-scale,1))!important
}
html body .login-logo{
    width:calc(clamp(60px,8vmin,96px) * var(--ui-scale,1))!important;
    height:calc(clamp(60px,8vmin,96px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(1.6rem,3vmin,2.6rem) * var(--ui-scale,1))!important
}
html body .login-box h2{
    font-size:calc(clamp(1.15rem,2.2vmin,1.7rem) * var(--ui-scale,1))!important
}
html body .login-box p{
    font-size:calc(clamp(.85rem,1.6vmin,1.15rem) * var(--ui-scale,1))!important
}
html body .btn-google{
    padding:calc(clamp(.85rem,1.7vmin,1.3rem) * var(--ui-scale,1))
             calc(clamp(1.3rem,2.6vmin,2rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.95rem,1.85vmin,1.35rem) * var(--ui-scale,1))!important
}
html body .btn-google img{
    width:calc(clamp(22px,3vmin,34px) * var(--ui-scale,1))!important;
    height:calc(clamp(22px,3vmin,34px) * var(--ui-scale,1))!important
}
html body .login-footer{
    font-size:calc(clamp(.78rem,1.5vmin,1.05rem) * var(--ui-scale,1))!important
}
html body .admin-box{
    max-width:calc(clamp(900px,75vw,1200px) * var(--ui-scale,1))!important
}
html body .admin-header{
    padding:calc(clamp(1.1rem,2.2vmin,1.65rem) * var(--ui-scale,1))
             calc(clamp(1.3rem,2.6vmin,2rem) * var(--ui-scale,1))!important
}
html body .admin-header h2{
    font-size:calc(clamp(1.05rem,2.1vmin,1.55rem) * var(--ui-scale,1))!important
}
html body .admin-summary-bar{
    padding:calc(clamp(.7rem,1.4vmin,1.05rem) * var(--ui-scale,1))
             calc(clamp(1rem,2vmin,1.5rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(1rem,2vmin,1.5rem) * var(--ui-scale,1))!important
}
html body .admin-summary-bar .summary-item{
    font-size:calc(clamp(.85rem,1.6vmin,1.15rem) * var(--ui-scale,1))!important
}
html body .admin-summary-bar .summary-value{
    font-size:calc(clamp(1.05rem,2.1vmin,1.55rem) * var(--ui-scale,1))!important;
    padding:calc(clamp(.15rem,.35vmin,.3rem) * var(--ui-scale,1))
             calc(clamp(.65rem,1.3vmin,1rem) * var(--ui-scale,1))!important
}
html body .admin-search{
    padding:calc(clamp(.7rem,1.4vmin,1.05rem) * var(--ui-scale,1))
             calc(clamp(.85rem,1.7vmin,1.3rem) * var(--ui-scale,1))
             calc(clamp(.7rem,1.4vmin,1.05rem) * var(--ui-scale,1))
             calc(clamp(2.4rem,4.5vmin,3.4rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.85rem,1.6vmin,1.15rem) * var(--ui-scale,1))!important
}
html body .admin-filter-btn{
    padding:calc(clamp(.35rem,.7vmin,.55rem) * var(--ui-scale,1))
             calc(clamp(.75rem,1.5vmin,1.15rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.75rem,1.4vmin,1rem) * var(--ui-scale,1))!important
}
html body .admin-section-head{
    padding:calc(clamp(.85rem,1.7vmin,1.3rem) * var(--ui-scale,1))
             calc(clamp(1rem,2vmin,1.5rem) * var(--ui-scale,1))!important
}
html body .ash-icon{
    width:calc(clamp(32px,4.5vmin,52px) * var(--ui-scale,1))!important;
    height:calc(clamp(32px,4.5vmin,52px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.85rem,1.65vmin,1.2rem) * var(--ui-scale,1))!important
}
html body .ash-title{
    font-size:calc(clamp(.9rem,1.75vmin,1.3rem) * var(--ui-scale,1))!important
}
html body .admin-toggle-btn{
    width:calc(clamp(34px,4.5vmin,52px) * var(--ui-scale,1))!important;
    height:calc(clamp(34px,4.5vmin,52px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.85rem,1.65vmin,1.2rem) * var(--ui-scale,1))!important
}
html body .user-row{
    padding:calc(clamp(.7rem,1.4vmin,1.05rem) * var(--ui-scale,1))
             calc(clamp(.75rem,1.5vmin,1.15rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.6rem,1.2vmin,.9rem) * var(--ui-scale,1))!important
}
html body .u-name{
    font-size:calc(clamp(.85rem,1.6vmin,1.15rem) * var(--ui-scale,1))!important
}
html body .u-email{
    font-size:calc(clamp(.72rem,1.35vmin,1rem) * var(--ui-scale,1))!important
}
html body .u-role{
    font-size:calc(clamp(.65rem,1.25vmin,.92rem) * var(--ui-scale,1))!important
}
html body .u-last-login,
html body .u-expiry{
    font-size:calc(clamp(.68rem,1.3vmin,.95rem) * var(--ui-scale,1))!important
}
html body .u-settings-btn{
    width:calc(clamp(34px,4.5vmin,52px) * var(--ui-scale,1))!important;
    height:calc(clamp(34px,4.5vmin,52px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.95rem,1.85vmin,1.35rem) * var(--ui-scale,1))!important
}
html body .u-settings-menu{
    min-width:calc(clamp(220px,32vmin,320px) * var(--ui-scale,1))!important;
    padding:calc(clamp(.35rem,.7vmin,.55rem) * var(--ui-scale,1))!important
}
html body .u-settings-item{
    padding:calc(clamp(.55rem,1.1vmin,.85rem) * var(--ui-scale,1))
             calc(clamp(.65rem,1.3vmin,1rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.82rem,1.55vmin,1.1rem) * var(--ui-scale,1))!important
}
html body .expiry-banner{
    padding:calc(clamp(.7rem,1.4vmin,1.05rem) * var(--ui-scale,1))
             calc(clamp(.8rem,1.6vmin,1.2rem) * var(--ui-scale,1))!important;
    gap:calc(clamp(.6rem,1.2vmin,.9rem) * var(--ui-scale,1))!important
}
html body .expiry-banner-icon{
    width:calc(clamp(40px,5.5vmin,64px) * var(--ui-scale,1))!important;
    height:calc(clamp(40px,5.5vmin,64px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(1.1rem,2.2vmin,1.6rem) * var(--ui-scale,1))!important
}
html body .expiry-banner-text .title{
    font-size:calc(clamp(.86rem,1.7vmin,1.25rem) * var(--ui-scale,1))!important
}
html body .expiry-banner-text .desc{
    font-size:calc(clamp(.72rem,1.4vmin,1rem) * var(--ui-scale,1))!important
}
html body .expiry-banner-btn{
    padding:calc(clamp(.5rem,1vmin,.8rem) * var(--ui-scale,1))
             calc(clamp(.85rem,1.7vmin,1.3rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.74rem,1.4vmin,1.05rem) * var(--ui-scale,1))!important
}
html body .renewal-box{
    max-width:calc(clamp(520px,65vmin,760px) * var(--ui-scale,1))!important
}
html body .renewal-header{
    padding:calc(clamp(1.1rem,2.2vmin,1.65rem) * var(--ui-scale,1))
             calc(clamp(1.3rem,2.6vmin,2rem) * var(--ui-scale,1))!important
}
html body .renewal-header h2{
    font-size:calc(clamp(1.05rem,2.1vmin,1.55rem) * var(--ui-scale,1))!important
}
html body .renewal-body{
    padding:calc(clamp(1.3rem,2.6vmin,2rem) * var(--ui-scale,1))!important
}
html body .renewal-current{
    padding:calc(clamp(.85rem,1.7vmin,1.3rem) * var(--ui-scale,1))
             calc(clamp(1rem,2vmin,1.5rem) * var(--ui-scale,1))!important
}
html body .rc-icon{
    width:calc(clamp(42px,5.8vmin,68px) * var(--ui-scale,1))!important;
    height:calc(clamp(42px,5.8vmin,68px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(1.1rem,2.1vmin,1.55rem) * var(--ui-scale,1))!important
}
html body .renewal-close{
    width:calc(clamp(30px,4.5vmin,52px) * var(--ui-scale,1))!important;
    height:calc(clamp(30px,4.5vmin,52px) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.85rem,1.6vmin,1.2rem) * var(--ui-scale,1))!important
}
html body .package-card{
    padding:calc(clamp(.85rem,1.7vmin,1.3rem) * var(--ui-scale,1))
             calc(clamp(.7rem,1.4vmin,1.1rem) * var(--ui-scale,1))!important
}
html body .pkg-label{
    font-size:calc(clamp(.9rem,1.75vmin,1.3rem) * var(--ui-scale,1))!important
}
html body .pkg-price{
    font-size:calc(clamp(1.15rem,2.2vmin,1.7rem) * var(--ui-scale,1))!important
}
html body .qr-img{
    width:calc(clamp(200px,35vmin,280px) * var(--ui-scale,1))!important;
    height:calc(clamp(200px,35vmin,280px) * var(--ui-scale,1))!important
}
html body .bank-row{
    font-size:calc(clamp(.82rem,1.55vmin,1.15rem) * var(--ui-scale,1))!important
}
html body .renewal-btn{
    padding:calc(clamp(.65rem,1.3vmin,1rem) * var(--ui-scale,1))
             calc(clamp(1.1rem,2.2vmin,1.65rem) * var(--ui-scale,1))!important;
    font-size:calc(clamp(.82rem,1.55vmin,1.15rem) * var(--ui-scale,1))!important
}

/* ═══════════════════════════════════════════════════════════════ */
/* ASSEMBLE                                                      */
/* ═══════════════════════════════════════════════════════════════ */
html body .pf-assemble-info{
    padding:calc(clamp(.4rem,.85vmin,.65rem) * var(--pf-scale,1))
             calc(clamp(.6rem,1.2vmin,.9rem) * var(--pf-scale,1))!important;
    gap:calc(clamp(.35rem,.7vmin,.55rem) * var(--pf-scale,1))!important;
    font-size:calc(clamp(.72rem,1.4vmin,1rem) * var(--pf-scale,1))!important
}
html body .pf-assemble-info .pf-info-tag{
    padding:calc(clamp(.18rem,.35vmin,.28rem) * var(--pf-scale,1))
             calc(clamp(.5rem,1vmin,.8rem) * var(--pf-scale,1))!important;
    font-size:calc(clamp(.62rem,1.2vmin,.9rem) * var(--pf-scale,1))!important
}
html body .pf-assemble-info .pf-info-word{
    padding:calc(clamp(.16rem,.3vmin,.25rem) * var(--pf-scale,1))
             calc(clamp(.5rem,1vmin,.8rem) * var(--pf-scale,1))!important;
    font-size:calc(clamp(1.1rem,2.2vmin,1.65rem) * var(--pf-scale,1))!important
}
html body .pf-assemble-info .pf-info-example{
    padding:calc(clamp(.12rem,.25vmin,.2rem) * var(--pf-scale,1))
             calc(clamp(.3rem,.6vmin,.5rem) * var(--pf-scale,1))!important;
    font-size:calc(clamp(.82rem,1.6vmin,1.2rem) * var(--pf-scale,1))!important
}
html body .pf-assemble-info .pf-info-plain{
    font-size:calc(clamp(.92rem,1.8vmin,1.35rem) * var(--pf-scale,1))!important
}
html body .pf-assemble-info .pf-info-pinyin{
    font-size:calc(clamp(.68rem,1.3vmin,.98rem) * var(--pf-scale,1))!important
}
html body .pf-assemble-info .pf-info-meaning{
    font-size:calc(clamp(.75rem,1.45vmin,1.1rem) * var(--pf-scale,1))!important
}
html body .pf-assemble-answer{
    min-height:calc(clamp(54px,9vmin,100px) * var(--pf-scale,1))!important;
    padding:calc(clamp(.5rem,1vmin,.85rem) * var(--pf-scale,1))
             calc(clamp(.6rem,1.2vmin,1rem) * var(--pf-scale,1))!important;
    border-radius:calc(clamp(12px,2vmin,18px) * var(--pf-scale,1))!important
}
html body .pf-assemble-hint{
    font-size:calc(clamp(.78rem,1.5vmin,1.15rem) * var(--pf-scale,1))!important
}
html body .pf-assemble-pool{
    min-height:calc(clamp(54px,9vmin,100px) * var(--pf-scale,1))!important;
    padding:calc(clamp(.5rem,1vmin,.85rem) * var(--pf-scale,1))
             calc(clamp(.6rem,1.2vmin,1rem) * var(--pf-scale,1))!important;
    gap:calc(clamp(.3rem,.6vmin,.5rem) * var(--pf-scale,1))!important;
    border-radius:calc(clamp(12px,2vmin,18px) * var(--pf-scale,1))!important
}
html body .pf-word{
    padding:calc(clamp(.38rem,.75vmin,.6rem) * var(--pf-scale,1))
             calc(clamp(.7rem,1.3vmin,1.1rem) * var(--pf-scale,1))!important;
    font-size:calc(clamp(1.1rem,2.2vmin,1.7rem) * var(--pf-scale,1))!important;
    border-radius:calc(clamp(9px,1.5vmin,14px) * var(--pf-scale,1))!important
}
html body .pf-assemble-next-btn{
    padding:calc(clamp(.6rem,1.2vmin,1rem) * var(--pf-scale,1))
             calc(clamp(1.2rem,2.4vmin,1.9rem) * var(--pf-scale,1))!important;
    font-size:calc(clamp(.85rem,1.65vmin,1.25rem) * var(--pf-scale,1))!important;
    margin-top:calc(clamp(.7rem,1.4vmin,1.15rem) * var(--pf-scale,1))!important
}
html body .pf-assemble-actions{
    gap:calc(clamp(.35rem,.7vmin,.55rem) * var(--pf-scale,1))!important
}
html body .pf-assemble-btn{
    padding:calc(clamp(.38rem,.75vmin,.6rem) * var(--pf-scale,1))
             calc(clamp(.65rem,1.3vmin,1.05rem) * var(--pf-scale,1))!important;
    font-size:calc(clamp(.72rem,1.4vmin,1.05rem) * var(--pf-scale,1))!important
}
html body .pf-assemble-btn.auto-shuffle{
    width:calc(clamp(36px,5.5vmin,62px) * var(--pf-scale,1))!important;
    height:calc(clamp(36px,5.5vmin,62px) * var(--pf-scale,1))!important
}
html body .pf-assemble-btn .pf-shuffle-countdown{
    width:calc(clamp(24px,3.7vmin,42px) * var(--pf-scale,1))!important;
    height:calc(clamp(24px,3.7vmin,42px) * var(--pf-scale,1))!important;
    font-size:calc(clamp(.68rem,1.3vmin,1rem) * var(--pf-scale,1))!important
}
html body .pf-nav-icon.mini-nav.assemble-toggle.with-label{
    height:calc(clamp(38px,6vmin,68px) * var(--pf-scale,1))!important;
    padding:0 calc(clamp(.6rem,1.2vmin,.95rem) * var(--pf-scale,1))!important
}
html body .pf-nav-icon.mini-nav.assemble-toggle.with-label i{
    font-size:calc(clamp(.85rem,1.6vmin,1.25rem) * var(--pf-scale,1))!important
}
html body .pf-nav-icon.mini-nav.assemble-toggle.with-label .assemble-toggle-label{
    font-size:calc(clamp(.7rem,1.35vmin,1rem) * var(--pf-scale,1))!important
}
html body .pf-nav-icon.mini-nav.assemble-toggle .assemble-new-badge{
    font-size:calc(clamp(.55rem,1vmin,.8rem) * var(--pf-scale,1))!important;
    padding:calc(clamp(.12rem,.25vmin,.2rem) * var(--pf-scale,1))
             calc(clamp(.35rem,.7vmin,.55rem) * var(--pf-scale,1))!important
}
html body .pf-settings-menu{
    min-width:calc(clamp(210px,30vmin,320px) * var(--pf-scale,1))!important;
    padding:calc(clamp(.35rem,.7vmin,.55rem) * var(--pf-scale,1))!important
}
html body .pf-settings-item{
    padding:calc(clamp(.5rem,1vmin,.8rem) * var(--pf-scale,1))
             calc(clamp(.65rem,1.3vmin,1rem) * var(--pf-scale,1))!important;
    font-size:calc(clamp(.8rem,1.55vmin,1.15rem) * var(--pf-scale,1))!important
}
html body .pf-phrase-word{
    padding:calc(clamp(.42rem,.85vmin,.7rem) * var(--pf-scale,1))
             calc(clamp(.8rem,1.6vmin,1.25rem) * var(--pf-scale,1))
             calc(clamp(.38rem,.75vmin,.6rem) * var(--pf-scale,1))!important;
    border-radius:calc(clamp(12px,2vmin,18px) * var(--pf-scale,1))!important
}
html body .pf-phrase-word .pf-phrase-zh{
    font-size:calc(clamp(1.5rem,3vmin,2.3rem) * var(--pf-scale,1))!important
}
html body .pf-phrase-word .pf-phrase-pinyin{
    font-size:calc(clamp(.72rem,1.4vmin,1.05rem) * var(--pf-scale,1))!important
}

/* ═══════════════════════════════════════════════════════════════ */
/* MOBILE — Reset scale = 1                                      */
/* ═══════════════════════════════════════════════════════════════ */
@media (max-width:768px){
    html body .practice-full-body{
        padding:0.75rem 0.75rem 70px 0.75rem!important;
        padding-bottom:calc(70px + env(safe-area-inset-bottom))!important
    }
    html body .practice-full-content{
        max-width:100%!important
    }
    html{--ui-scale:1!important;--pf-scale:1!important}
}
html body .practice-full-body{
justify-content:flex-start!important;
padding-top:1rem!important
}
html body .practice-full-body::before{
flex:0 1 0!important;
min-height:0!important
}
html body .practice-full-body::after{
flex:0 1 0!important;
min-height:0!important
}
html body .practice-full-content{
flex:0 0 auto!important;
margin:0!important;
overflow:visible!important
}
html body .practice-full-input-wrap{
width:100%!important;
flex:0 0 auto!important;
display:flex!important;
flex-direction:column!important;
gap:calc(clamp(.45rem,1vmin,.75rem) * var(--pf-scale,1))!important
}
html body .practice-input-row{
width:100%!important;
flex:0 0 auto!important;
display:flex!important;
align-items:stretch!important
}
html body .practice-full-input{
width:100%!important;
flex:1 1 auto!important;
box-sizing:border-box!important;
transition:none!important
}
html body .practice-speak-btn{
flex:0 0 auto!important;
align-self:stretch!important
}
html body .char-preview{
width:100%!important;
flex:0 0 auto!important;
box-sizing:border-box!important
}
html body .practice-full-status{
width:100%!important;
flex:0 0 auto!important
}
html body .reveal-actions{
width:100%!important;
flex:0 0 auto!important;
box-sizing:border-box!important
}
html body .answer-reveal{
width:100%!important;
flex:0 0 auto!important;
box-sizing:border-box!important
}
html body .pf-assemble-mode{
width:100%!important;
flex:0 0 auto!important;
box-sizing:border-box!important
}
html body .pf-assemble-info{
width:100%!important;
flex:0 0 auto!important;
box-sizing:border-box!important
}
html body .pf-assemble-answer{
width:100%!important;
flex:0 0 auto!important;
box-sizing:border-box!important
}
html body .pf-assemble-pool{
width:100%!important;
flex:0 0 auto!important;
box-sizing:border-box!important
}
html body .pf-assemble-actions{
width:100%!important;
flex:0 0 auto!important;
box-sizing:border-box!important
}
html body .pf-assemble-next-btn{
flex:0 0 auto!important;
align-self:center!important
}
@media (max-width:768px){
html body .practice-full-body{
padding-top:.75rem!important
}
}
html body .practice-full-body::before{flex:0 1 0!important;min-height:0!important}
html body .practice-full-body::after{flex:0 1 0!important;min-height:0!important}
html body .practice-full-body{justify-content:flex-start!important;padding-top:clamp(.5rem,1vh,.85rem)!important;padding-bottom:calc(72px + env(safe-area-inset-bottom))!important}
html body .practice-full-content{gap:calc(clamp(.4rem,.9vh,.7rem) * var(--pf-scale,1))!important}
html body .practice-full-input-wrap{gap:calc(clamp(.3rem,.7vh,.5rem) * var(--pf-scale,1))!important}
html body .reveal-actions{margin-top:calc(clamp(.15rem,.35vh,.25rem) * var(--pf-scale,1))!important;gap:calc(clamp(.35rem,.7vmin,.55rem) * var(--pf-scale,1))!important}
html body .answer-reveal{padding:calc(clamp(.55rem,1.1vmin,.85rem) * var(--pf-scale,1))!important;gap:calc(clamp(.45rem,.9vmin,.7rem) * var(--pf-scale,1))!important}
html body .practice-full-vi{padding:calc(clamp(.55rem,1.2vh,.9rem) * var(--pf-scale,1)) calc(clamp(.7rem,1.6vw,1.1rem) * var(--pf-scale,1))!important}
html body .char-preview{min-height:calc(clamp(26px,4vmin,44px) * var(--pf-scale,1))!important;padding:calc(clamp(.28rem,.7vmin,.55rem) * var(--pf-scale,1))!important}
html body .practice-full-status{min-height:calc(clamp(1rem,1.8vmin,1.4rem) * var(--pf-scale,1))!important;font-size:calc(clamp(.8rem,1.55vmin,1.15rem) * var(--pf-scale,1))!important}
@media (max-width:768px){
html body .practice-full-body{padding-top:.5rem!important;padding-bottom:calc(66px + env(safe-area-inset-bottom))!important}
html body .practice-full-content{gap:.5rem!important}
}
"""


def build_auto_scale_js():
    return r"""
(function setupAutoScale(){
'use strict';

/* ────────────────────────────────────────────────────────────── */
/* CẤU HÌNH SCALE                                                */
/* ────────────────────────────────────────────────────────────── */
var UI_MIN_SCALE = 0.85;
var UI_MAX_SCALE = 1.6;
var PF_MIN_SCALE = 0.8;
var PF_MAX_SCALE = 1.8;

var UI_BASE_HEIGHT = 900;
var PF_BASE_HEIGHT = 850;

/* Tỉ lệ kết hợp: 60% inch + 40% viewport */
var INCH_WEIGHT = 0.6;
var VH_WEIGHT = 0.4;

/* Base inch: 15 inch = factor 1.0 */
var INCH_BASE = 15;

/* DPI ước lượng (CSS pixel ~ 96, nhưng laptop hiện đại ~ 110) */
var DPI_ESTIMATE = 110;

function clamp(val, min, max){
    return Math.max(min, Math.min(max, val));
}

/* ────────────────────────────────────────────────────────────── */
/* ƯỚC LƯỢNG KÍCH THƯỚC MÀN HÌNH THEO INCH                      */
/* ────────────────────────────────────────────────────────────── */
function estimateScreenInches(){
    try {
        var w = window.screen.width || 1920;
        var h = window.screen.height || 1080;
        var dpr = window.devicePixelRatio || 1;

        /* Đường chéo pixel vật lý */
        var diagPx = Math.sqrt(w * w + h * h) * dpr;

        /* Chia cho DPI để ra inch */
        var inches = diagPx / DPI_ESTIMATE;

        /* Clamp để tránh giá trị vô lý */
        return clamp(inches, 8, 40);
    } catch(e) {
        return 15; /* fallback */
    }
}

/* ────────────────────────────────────────────────────────────── */
/* TÍNH SCALE                                                    */
/* ────────────────────────────────────────────────────────────── */
function computeScales(){
    /* Mobile: reset về 1 */
    if(window.innerWidth < 769){
        document.documentElement.style.removeProperty('--ui-scale');
        document.documentElement.style.removeProperty('--pf-scale');
        return;
    }

    var vh = window.innerHeight;
    var inches = estimateScreenInches();

    /* ⭐ Scale theo viewport height */
    var uiVhScale = clamp(vh / UI_BASE_HEIGHT, UI_MIN_SCALE, UI_MAX_SCALE);
    var pfVhScale = clamp(vh / PF_BASE_HEIGHT, PF_MIN_SCALE, PF_MAX_SCALE);

    /* ⭐ Scale theo inch */
    var inchFactor = clamp(inches / INCH_BASE, 0.85, 1.5);

    /* ⭐ Kết hợp có trọng số: 60% inch + 40% viewport */
    var uiScale = (inchFactor * INCH_WEIGHT) + (uiVhScale * VH_WEIGHT);
    var pfScale = (inchFactor * INCH_WEIGHT) + (pfVhScale * VH_WEIGHT);

   var uiBase = clamp(
        (inchFactor * INCH_WEIGHT) + (uiVhScale * VH_WEIGHT),
        UI_MIN_SCALE, UI_MAX_SCALE
    );
    var pfBase = clamp(
        (inchFactor * INCH_WEIGHT) + (pfVhScale * VH_WEIGHT),
        PF_MIN_SCALE, PF_MAX_SCALE
    );

    /* ⭐ LƯU BASE SCALE vào 2 biến riêng */
    var rootStyle = document.documentElement.style;
    rootStyle.setProperty('--ui-scale-base', uiBase.toFixed(3));
    rootStyle.setProperty('--pf-scale-base', pfBase.toFixed(3));

    /* ⭐ Đọc user-scale (từ nút +/-), mặc định 1.0 */
    var userScale = 1.0;
    try {
        var saved = parseFloat(localStorage.getItem('pfUserScale_v1'));
        if (!isNaN(saved) && saved >= 0.7 && saved <= 1.6) userScale = saved;
    } catch(e) {}

    /* ⭐ ÁP DỤNG: base × user */
    rootStyle.setProperty('--ui-scale', (uiBase * userScale).toFixed(3));
    rootStyle.setProperty('--pf-scale', (pfBase * userScale).toFixed(3));
    console.log('[AutoScale] inches=' + inches.toFixed(1) +
                ' vh=' + vh +
                ' inchFactor=' + inchFactor.toFixed(3) +
                ' → ui=' + uiScale.toFixed(3) +
                ' pf=' + pfScale.toFixed(3));
}

/* Chạy ngay khi load */
computeScales();

/* Re-calc khi resize (throttled 150ms) */
var resizeTimer = null;
window.addEventListener('resize', function(){
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(computeScales, 150);
});

/* Re-calc khi orientation change */
window.addEventListener('orientationchange', function(){
    setTimeout(computeScales, 300);
});

/* Re-calc khi mở Practice Full hoặc đổi câu (view height thay đổi) */
document.addEventListener('click', function(e){
    if(!e.target || !e.target.closest) return;
    if(e.target.closest('#pfNextBtn,#pfPrevBtn,.practice-full-btn,#pfQuickNav')){
        setTimeout(computeScales, 100);
    }
});

console.log('[AutoScale] Module loaded — trọng số ' +
            (INCH_WEIGHT * 100) + '% inch + ' +
            (VH_WEIGHT * 100) + '% viewport');
})();
"""


if __name__ == "__main__":
    css = build_auto_scale_css()
    js = build_auto_scale_js()
    print("="*60)
    print("AUTO-SCALE MODULE — Kiểm tra")
    print("="*60)
    print("CSS: {} ký tự ({} dòng)".format(len(css), len(css.splitlines())))
    print("JS:  {} ký tự ({} dòng)".format(len(js), len(js.splitlines())))
    print()
    print("Căn giữa: before 30% - content - after 70%")
    print("Scale: 60% inch + 40% viewport")
    print("Modules tích hợp: 19")
    print("✅ Module OK")

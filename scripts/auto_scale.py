# -*- coding: utf-8 -*-


def build_auto_scale_css():
    return r"""
:root{--ui-scale:1;--pf-scale:1}
html body .practice-full-body{
flex:1 1 auto!important;min-height:0!important;overflow-y:auto!important;
display:flex!important;flex-direction:column!important;
justify-content:flex-start!important;align-items:center!important;
padding:clamp(.5rem,1vh,.85rem) 1rem calc(72px + env(safe-area-inset-bottom)) 1rem!important;
box-sizing:border-box!important
}
html body .practice-full-content{
width:100%!important;max-width:min(92vw,900px)!important;flex:0 0 auto!important;
display:flex!important;flex-direction:column!important;
gap:calc(clamp(.15rem,.35vh,.3rem) * var(--pf-scale,1))!important;
justify-content:flex-start!important;margin:0!important;padding:0!important;overflow:visible!important
}
html body .practice-full-input-wrap{
width:100%!important;flex:0 0 auto!important;display:flex!important;
flex-direction:column!important;gap:calc(clamp(.1rem,.25vh,.2rem) * var(--pf-scale,1))!important
}
html body .practice-input-row{
width:100%!important;flex:0 0 auto!important;display:flex!important;
align-items:stretch!important;gap:calc(clamp(.4rem,.8vmin,.6rem) * var(--pf-scale,1))!important
}
html body .practice-full-input{
width:100%!important;flex:1 1 auto!important;box-sizing:border-box!important;transition:none!important;
padding:calc(clamp(.85rem,2vh,1.4rem) * var(--pf-scale,1)) calc(clamp(.9rem,1.8vw,1.5rem) * var(--pf-scale,1))!important;
font-size:calc(clamp(1.2rem,2.8vmin,2rem) * var(--pf-scale,1))!important;
min-height:calc(clamp(56px,9vmin,95px) * var(--pf-scale,1))!important;
border-radius:calc(clamp(12px,2vmin,18px) * var(--pf-scale,1))!important
}
html body .practice-speak-btn{
flex:0 0 auto!important;align-self:stretch!important;
min-width:calc(clamp(50px,7vmin,78px) * var(--pf-scale,1))!important;
font-size:calc(clamp(1.05rem,2.1vmin,1.6rem) * var(--pf-scale,1))!important;
border-radius:calc(clamp(12px,2vmin,18px) * var(--pf-scale,1))!important
}
html body .char-preview{
width:100%!important;flex:0 0 auto!important;box-sizing:border-box!important;
min-height:calc(clamp(26px,4vmin,44px) * var(--pf-scale,1))!important;
padding:calc(clamp(.28rem,.7vmin,.55rem) * var(--pf-scale,1))!important;
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
width:100%!important;flex:0 0 auto!important;
min-height:calc(clamp(1rem,1.8vmin,1.4rem) * var(--pf-scale,1))!important;
font-size:calc(clamp(.8rem,1.55vmin,1.15rem) * var(--pf-scale,1))!important
}
html body .reveal-actions{
width:100%!important;flex:0 0 auto!important;box-sizing:border-box!important;
margin-top:0!important;
gap:calc(clamp(.35rem,.7vmin,.55rem) * var(--pf-scale,1))!important
}
html body .reveal-actions button{
padding:calc(clamp(.75rem,1.7vh,1.25rem) * var(--pf-scale,1)) calc(clamp(.85rem,1.7vw,1.4rem) * var(--pf-scale,1))!important;
font-size:calc(clamp(.95rem,1.85vmin,1.4rem) * var(--pf-scale,1))!important;
border-radius:calc(clamp(12px,2vmin,18px) * var(--pf-scale,1))!important;
gap:calc(clamp(.4rem,.8vmin,.6rem) * var(--pf-scale,1))!important
}
html body .answer-reveal{
width:100%!important;flex:0 0 auto!important;box-sizing:border-box!important;
gap:calc(clamp(.45rem,.9vmin,.7rem) * var(--pf-scale,1))!important;
padding:calc(clamp(.55rem,1.1vmin,.85rem) * var(--pf-scale,1))!important;
border-radius:calc(clamp(12px,2vmin,18px) * var(--pf-scale,1))!important
}
html body .answer-phrase-btn{
padding:calc(clamp(.42rem,.9vmin,.7rem) * var(--pf-scale,1)) calc(clamp(.75rem,1.5vmin,1.15rem) * var(--pf-scale,1))!important;
font-size:calc(clamp(1.2rem,2.4vmin,1.9rem) * var(--pf-scale,1))!important;
border-radius:calc(clamp(10px,1.7vmin,16px) * var(--pf-scale,1))!important
}
html body .answer-pinyin{
font-size:calc(clamp(.9rem,1.75vmin,1.3rem) * var(--pf-scale,1))!important
}
html body .answer-phrase-tooltip{
padding:calc(clamp(.4rem,.8vmin,.65rem) * var(--pf-scale,1)) calc(clamp(.7rem,1.4vmin,1.1rem) * var(--pf-scale,1))!important;
font-size:calc(clamp(.78rem,1.5vmin,1.1rem) * var(--pf-scale,1))!important;
border-radius:calc(clamp(10px,1.6vmin,16px) * var(--pf-scale,1))!important
}
html body .practice-full-vi{
padding:calc(clamp(.55rem,1.2vh,.9rem) * var(--pf-scale,1)) calc(clamp(.7rem,1.6vw,1.1rem) * var(--pf-scale,1))!important;
font-size:calc(clamp(1.2rem,2.6vmin,2rem) * var(--pf-scale,1))!important;
border-radius:calc(clamp(14px,2.2vmin,20px) * var(--pf-scale,1))!important
}
html body .pf-assemble-mode{
width:100%!important;flex:0 0 auto!important;box-sizing:border-box!important
}
html body .pf-assemble-info{
width:100%!important;flex:0 0 auto!important;box-sizing:border-box!important;
padding:calc(clamp(.4rem,.85vmin,.65rem) * var(--pf-scale,1)) calc(clamp(.6rem,1.2vmin,.9rem) * var(--pf-scale,1))!important;
gap:calc(clamp(.35rem,.7vmin,.55rem) * var(--pf-scale,1))!important;
font-size:calc(clamp(.72rem,1.4vmin,1rem) * var(--pf-scale,1))!important
}
html body .pf-assemble-info .pf-info-tag{
padding:calc(clamp(.18rem,.35vmin,.28rem) * var(--pf-scale,1)) calc(clamp(.5rem,1vmin,.8rem) * var(--pf-scale,1))!important;
font-size:calc(clamp(.62rem,1.2vmin,.9rem) * var(--pf-scale,1))!important
}
html body .pf-assemble-info .pf-info-word{
padding:calc(clamp(.16rem,.3vmin,.25rem) * var(--pf-scale,1)) calc(clamp(.5rem,1vmin,.8rem) * var(--pf-scale,1))!important;
font-size:calc(clamp(1.1rem,2.2vmin,1.65rem) * var(--pf-scale,1))!important
}
html body .pf-assemble-info .pf-info-example{
padding:calc(clamp(.12rem,.25vmin,.2rem) * var(--pf-scale,1)) calc(clamp(.3rem,.6vmin,.5rem) * var(--pf-scale,1))!important;
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
width:100%!important;flex:0 0 auto!important;box-sizing:border-box!important;
min-height:calc(clamp(54px,9vmin,100px) * var(--pf-scale,1))!important;
padding:calc(clamp(.5rem,1vmin,.85rem) * var(--pf-scale,1)) calc(clamp(.6rem,1.2vmin,1rem) * var(--pf-scale,1))!important;
border-radius:calc(clamp(12px,2vmin,18px) * var(--pf-scale,1))!important
}
html body .pf-assemble-hint{
font-size:calc(clamp(.78rem,1.5vmin,1.15rem) * var(--pf-scale,1))!important
}
html body .pf-assemble-pool{
width:100%!important;flex:0 0 auto!important;box-sizing:border-box!important;
min-height:calc(clamp(54px,9vmin,100px) * var(--pf-scale,1))!important;
padding:calc(clamp(.5rem,1vmin,.85rem) * var(--pf-scale,1)) calc(clamp(.6rem,1.2vmin,1rem) * var(--pf-scale,1))!important;
gap:calc(clamp(.3rem,.6vmin,.5rem) * var(--pf-scale,1))!important;
border-radius:calc(clamp(12px,2vmin,18px) * var(--pf-scale,1))!important
}
html body .pf-word{
padding:calc(clamp(.38rem,.75vmin,.6rem) * var(--pf-scale,1)) calc(clamp(.7rem,1.3vmin,1.1rem) * var(--pf-scale,1))!important;
font-size:calc(clamp(1.1rem,2.2vmin,1.7rem) * var(--pf-scale,1))!important;
border-radius:calc(clamp(9px,1.5vmin,14px) * var(--pf-scale,1))!important
}
html body .pf-assemble-next-btn{
padding:calc(clamp(.6rem,1.2vmin,1rem) * var(--pf-scale,1)) calc(clamp(1.2rem,2.4vmin,1.9rem) * var(--pf-scale,1))!important;
font-size:calc(clamp(.85rem,1.65vmin,1.25rem) * var(--pf-scale,1))!important;
margin-top:calc(clamp(.7rem,1.4vmin,1.15rem) * var(--pf-scale,1))!important;
flex:0 0 auto!important;align-self:center!important
}
html body .pf-assemble-actions{
width:100%!important;flex:0 0 auto!important;box-sizing:border-box!important;
gap:calc(clamp(.35rem,.7vmin,.55rem) * var(--pf-scale,1))!important
}
html body .pf-assemble-btn{
padding:calc(clamp(.38rem,.75vmin,.6rem) * var(--pf-scale,1)) calc(clamp(.65rem,1.3vmin,1.05rem) * var(--pf-scale,1))!important;
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
padding:calc(clamp(.12rem,.25vmin,.2rem) * var(--pf-scale,1)) calc(clamp(.35rem,.7vmin,.55rem) * var(--pf-scale,1))!important
}
html body .pf-settings-menu{
min-width:calc(clamp(210px,30vmin,320px) * var(--pf-scale,1))!important;
padding:calc(clamp(.35rem,.7vmin,.55rem) * var(--pf-scale,1))!important
}
html body .pf-settings-item{
padding:calc(clamp(.5rem,1vmin,.8rem) * var(--pf-scale,1)) calc(clamp(.65rem,1.3vmin,1rem) * var(--pf-scale,1))!important;
font-size:calc(clamp(.8rem,1.55vmin,1.15rem) * var(--pf-scale,1))!important
}
html body .pf-phrase-word{
padding:calc(clamp(.42rem,.85vmin,.7rem) * var(--pf-scale,1)) calc(clamp(.8rem,1.6vmin,1.25rem) * var(--pf-scale,1)) calc(clamp(.38rem,.75vmin,.6rem) * var(--pf-scale,1))!important;
border-radius:calc(clamp(12px,2vmin,18px) * var(--pf-scale,1))!important
}
html body .pf-phrase-word .pf-phrase-zh{
font-size:calc(clamp(1.5rem,3vmin,2.3rem) * var(--pf-scale,1))!important
}
html body .pf-phrase-word .pf-phrase-pinyin{
font-size:calc(clamp(.72rem,1.4vmin,1.05rem) * var(--pf-scale,1))!important
}
#quickSearchRoot{
position:fixed;left:20px;bottom:calc(90px + env(safe-area-inset-bottom));
z-index:9997;display:flex;flex-direction:column;align-items:flex-start;gap:.5rem;
pointer-events:none;transition:bottom .35s cubic-bezier(.34,1.56,.64,1)
}
#quickSearchRoot>*{pointer-events:auto}
#quickSearchRoot.hidden{opacity:0;pointer-events:none}
body.has-floating-group #quickSearchRoot{bottom:calc(260px + env(safe-area-inset-bottom))}
.quick-search-toggle{
width:44px;height:44px;border-radius:50%;border:2px solid #fff;
background:linear-gradient(135deg,#0891b2,#0e7490,#155e75);color:#fff;cursor:pointer;
display:flex;align-items:center;justify-content:center;font-size:1.05rem;
box-shadow:0 8px 24px rgba(14,116,144,.55);
transition:all .3s cubic-bezier(.34,1.56,.64,1);flex-shrink:0;font-family:inherit;padding:0
}
.quick-search-toggle:hover{transform:scale(1.08);box-shadow:0 12px 32px rgba(14,116,144,.75)}
.quick-search-toggle.active{
background:linear-gradient(135deg,#dc2626,#991b1b);
box-shadow:0 8px 24px rgba(220,38,38,.65)
}
.quick-search-toggle i{transition:transform .3s}
.quick-search-toggle.active i{transform:rotate(90deg)}
.quick-search-panel{
display:flex;align-items:center;gap:.35rem;padding:0;border-radius:999px;
background:#fff;border:2px solid #e2e8f0;box-shadow:0 8px 24px rgba(15,23,42,.25);
overflow:hidden;max-width:0;opacity:0;transform:translateX(-8px);
transition:max-width .35s cubic-bezier(.34,1.56,.64,1),opacity .25s ease,transform .3s ease,padding .25s ease;
pointer-events:none;position:relative
}
.quick-search-panel.open{
max-width:calc(100vw - 90px);opacity:1;transform:translateX(0);
padding:.3rem .35rem .3rem .6rem;pointer-events:auto
}
[data-theme="dark"] .quick-search-panel{background:#1e293b;border-color:#334155}
.quick-search-panel input{
flex:1;min-width:0;border:none;outline:none;background:transparent;color:#0f172a;
font-size:.85rem;font-family:inherit;padding:.4rem 0;min-width:150px;height:30px;line-height:30px
}
[data-theme="dark"] .quick-search-panel input{color:#f1f5f9}
.quick-search-panel input::placeholder{color:#94a3b8;font-size:.78rem}
.quick-search-clear,.quick-search-go{
width:30px;height:30px;min-width:30px;min-height:30px;border-radius:50%;border:none;cursor:pointer;
display:none;align-items:center;justify-content:center;flex-shrink:0;transition:.15s;
font-family:inherit;padding:0;margin:0;line-height:1;box-sizing:border-box
}
.quick-search-clear i,.quick-search-go i{
display:flex;align-items:center;justify-content:center;line-height:1;margin:0;padding:0;
pointer-events:none;font-size:.75rem
}
.quick-search-clear{background:#f1f5f9;color:#475569}
.quick-search-clear:hover{background:#fee2e2;color:#dc2626}
.quick-search-go{background:linear-gradient(135deg,#0891b2,#0e7490);color:#fff}
.quick-search-go:hover{transform:scale(1.08);box-shadow:0 4px 12px rgba(14,116,144,.5)}
.quick-search-panel.has-value .quick-search-clear,
.quick-search-panel.has-value .quick-search-go{display:flex}
.quick-search-toast{
position:fixed;top:80px;left:50%;transform:translateX(-50%) translateY(-20px);
padding:.7rem 1.2rem;border-radius:50px;font-size:.85rem;font-weight:700;color:#fff;
background:linear-gradient(135deg,#0891b2,#155e75);
box-shadow:0 8px 24px rgba(14,116,144,.45);z-index:99999;opacity:0;
transition:opacity .25s,transform .3s cubic-bezier(.34,1.56,.64,1);
pointer-events:none;max-width:90vw;overflow:hidden;text-overflow:ellipsis;white-space:nowrap
}
.quick-search-toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.quick-search-toast.error{
background:linear-gradient(135deg,#dc2626,#991b1b);
box-shadow:0 8px 24px rgba(220,38,38,.5)
}
@media (max-width:768px){
#quickSearchRoot{left:12px;bottom:calc(80px + env(safe-area-inset-bottom))}
body.has-floating-group #quickSearchRoot{bottom:calc(240px + env(safe-area-inset-bottom))}
.quick-search-toggle{width:42px;height:42px;font-size:1rem}
.practice-full-body{padding-top:.5rem!important;padding-bottom:calc(66px + env(safe-area-inset-bottom))!important}
.practice-full-content{gap:.35rem!important}
.practice-full-input-wrap{gap:.2rem!important}
}
@media (max-width:400px){
#quickSearchRoot{left:10px}
.quick-search-toggle{width:40px;height:40px}
}
@media (max-width:768px){
html body .practice-full-body{
padding:0.75rem 0.75rem 70px 0.75rem!important;
padding-bottom:calc(70px + env(safe-area-inset-bottom))!important
}
html body .practice-full-content{max-width:100%!important}
html{--ui-scale:1!important;--pf-scale:1!important}
}
"""


def build_auto_scale_js():
    return r"""
(function setupAutoScale(){
'use strict';
var UI_MIN_SCALE=0.85;
var UI_MAX_SCALE=1.6;
var PF_MIN_SCALE=0.8;
var PF_MAX_SCALE=1.8;
var UI_BASE_HEIGHT=900;
var PF_BASE_HEIGHT=850;
var INCH_WEIGHT=0.6;
var VH_WEIGHT=0.4;
var INCH_BASE=15;
var DPI_ESTIMATE=110;
function clamp(val,min,max){return Math.max(min,Math.min(max,val))}
function estimateScreenInches(){
try{
var w=window.screen.width||1920;
var h=window.screen.height||1080;
var dpr=window.devicePixelRatio||1;
var diagPx=Math.sqrt(w*w+h*h)*dpr;
var inches=diagPx/DPI_ESTIMATE;
return clamp(inches,8,40)
}catch(e){return 15}
}
function computeScales(){
if(window.innerWidth<769){
document.documentElement.style.removeProperty('--ui-scale');
document.documentElement.style.removeProperty('--pf-scale');
return
}
var vh=window.innerHeight;
var inches=estimateScreenInches();
var uiVhScale=clamp(vh/UI_BASE_HEIGHT,UI_MIN_SCALE,UI_MAX_SCALE);
var pfVhScale=clamp(vh/PF_BASE_HEIGHT,PF_MIN_SCALE,PF_MAX_SCALE);
var inchFactor=clamp(inches/INCH_BASE,0.85,1.5);
var uiBase=clamp((inchFactor*INCH_WEIGHT)+(uiVhScale*VH_WEIGHT),UI_MIN_SCALE,UI_MAX_SCALE);
var pfBase=clamp((inchFactor*INCH_WEIGHT)+(pfVhScale*VH_WEIGHT),PF_MIN_SCALE,PF_MAX_SCALE);
var rootStyle=document.documentElement.style;
rootStyle.setProperty('--ui-scale-base',uiBase.toFixed(3));
rootStyle.setProperty('--pf-scale-base',pfBase.toFixed(3));
var userScale=1.0;
try{
var saved=parseFloat(localStorage.getItem('pfUserScale_v1'));
if(!isNaN(saved)&&saved>=0.7&&saved<=1.6)userScale=saved
}catch(e){}
rootStyle.setProperty('--ui-scale',(uiBase*userScale).toFixed(3));
rootStyle.setProperty('--pf-scale',(pfBase*userScale).toFixed(3));
console.log('[AutoScale] inches='+inches.toFixed(1)+' vh='+vh+' inchFactor='+inchFactor.toFixed(3)+' → ui='+uiBase.toFixed(3)+' pf='+pfBase.toFixed(3))
}
computeScales();
var resizeTimer=null;
window.addEventListener('resize',function(){
clearTimeout(resizeTimer);
resizeTimer=setTimeout(computeScales,150)
});
window.addEventListener('orientationchange',function(){setTimeout(computeScales,300)});
document.addEventListener('click',function(e){
if(!e.target||!e.target.closest)return;
if(e.target.closest('#pfNextBtn,#pfPrevBtn,.practice-full-btn,#pfQuickNav')){setTimeout(computeScales,100)}
});
console.log('[AutoScale] Module loaded — trọng số '+(INCH_WEIGHT*100)+'% inch + '+(VH_WEIGHT*100)+'% viewport')
})();
(function quickSearchModule(){
'use strict';
var QS={open:false,inited:false,retries:0,MOUNT_ID:'quickSearchRoot'};
function $id(id){return document.getElementById(id)}
function buildDOM(){
var root=document.createElement('div');
root.id=QS.MOUNT_ID;
root.innerHTML=
'<div class="quick-search-panel" id="quickSearchPanel">'+
'<input type="text" id="quickSearchInput" placeholder="hsk1 5 - hsk2 10 20" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false">'+
'<button class="quick-search-clear" id="quickSearchClear" type="button" title="Xoa"><i class="fas fa-times"></i></button>'+
'<button class="quick-search-go" id="quickSearchGo" type="button" title="Tim"><i class="fas fa-arrow-right"></i></button>'+
'</div>'+
'<button class="quick-search-toggle" id="quickSearchToggle" type="button" title="Tim kiem nhanh"><i class="fas fa-search"></i></button>';
return root
}
function mount(){
if($id(QS.MOUNT_ID))return true;
if(!document.body){
QS.retries++;
if(QS.retries>60)return false;
setTimeout(mount,300);
return false
}
var root=buildDOM();
document.body.appendChild(root);
console.log('[quick-search] Mount OK');
return true
}
function showToast(msg,isError){
var old=$id('quickSearchToast');
if(old)old.remove();
var t=document.createElement('div');
t.id='quickSearchToast';
t.className='quick-search-toast'+(isError?' error':'');
t.textContent=msg;
document.body.appendChild(t);
requestAnimationFrame(function(){t.classList.add('show')});
setTimeout(function(){
t.classList.remove('show');
setTimeout(function(){if(t.parentNode)t.remove()},300)
},2400)
}
function doSearch(){
var input=$id('quickSearchInput');
if(!input)return;
var raw=input.value.trim();
if(!raw){showToast('Nhap gi do de tim...',true);input.focus();return}
var pfModal=$id('practiceFullModal');
var isPFOpen=pfModal&&pfModal.classList.contains('show');
if(isPFOpen){
var pfsi=$id('pfSearchInput');
if(!pfsi){showToast('Khong co o search Full',true);return}
pfsi.value=raw;
try{pfsi.dispatchEvent(new Event('input',{bubbles:true}))}
catch(e){
var ev2=document.createEvent('Event');
ev2.initEvent('input',true,true);
pfsi.dispatchEvent(ev2)
}
var pfcb=$id('pfClearSearchBtn');
if(pfcb)pfcb.classList.add('show')
}else{
var si=$id('searchInput');
if(!si){showToast('Khong co o search chinh',true);return}
si.value=raw;
try{si.dispatchEvent(new Event('input',{bubbles:true}))}
catch(e){
var ev=document.createEvent('Event');
ev.initEvent('input',true,true);
si.dispatchEvent(ev)
}
var cb=$id('clearSearchBtn');
if(cb)cb.classList.add('show')
}
closePanel();
setTimeout(function(){
var mainEl=$id('mainContent');
if(mainEl){
var y=mainEl.getBoundingClientRect().top+window.scrollY-100;
window.scrollTo({top:y,behavior:'smooth'})
}
},100);
showToast('Da tim: '+raw)
}
function openPanel(){
QS.open=true;
var p=$id('quickSearchPanel');
var t=$id('quickSearchToggle');
if(p)p.classList.add('open');
if(t)t.classList.add('active');
setTimeout(function(){var i=$id('quickSearchInput');if(i)i.focus()},200)
}
function closePanel(){
QS.open=false;
var p=$id('quickSearchPanel');
var t=$id('quickSearchToggle');
if(p)p.classList.remove('open');
if(t)t.classList.remove('active')
}
function clearPanel(){
var p=$id('quickSearchPanel');
var i=$id('quickSearchInput');
if(p)p.classList.remove('has-value');
if(i){i.value='';i.focus()}
}
function bind(){
if(QS.inited)return;
var toggle=$id('quickSearchToggle');
var panel=$id('quickSearchPanel');
var input=$id('quickSearchInput');
var clearB=$id('quickSearchClear');
var goB=$id('quickSearchGo');
if(!toggle||!panel||!input||!clearB||!goB){setTimeout(bind,300);return}
QS.inited=true;
goB.addEventListener('click',function(e){
if(e){e.stopPropagation();e.preventDefault()}
doSearch()
});
clearB.addEventListener('click',function(e){
if(e){e.stopPropagation();e.preventDefault()}
clearPanel()
});
toggle.addEventListener('click',function(e){
if(e){e.stopPropagation();e.preventDefault()}
if(QS.open)closePanel();else openPanel()
});
input.addEventListener('input',function(){panel.classList.toggle('has-value',!!this.value.trim())});
input.addEventListener('keydown',function(e){
if(e.key==='Enter'||e.keyCode===13){
e.preventDefault();
e.stopPropagation();
var g=$id('quickSearchGo');
if(g){g.click()}else{doSearch()}
return false
}
if(e.key==='Escape'||e.keyCode===27){
e.preventDefault();
if(this.value.trim()){
this.value='';
panel.classList.remove('has-value')
}else{closePanel()}
return false
}
});
document.addEventListener('click',function(e){
if(!QS.open)return;
if(e.target.closest('#'+QS.MOUNT_ID))return;
var i=$id('quickSearchInput');
if(i&&i.value.trim())return;
closePanel()
});
console.log('[quick-search] Bind OK')
}
function init(){
if(mount()){bind()}
else{
setTimeout(function(){if($id(QS.MOUNT_ID))bind()},600)
}
}
if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',init)}else{init()}
window.__quickSearch={
open:openPanel,
close:closePanel,
clear:clearPanel,
do:doSearch,
mount:mount,
reinit:function(){QS.inited=false;QS.retries=0;init()}
}
})();
"""


if __name__ == "__main__":
    css = build_auto_scale_css()
    js = build_auto_scale_js()
    print("CSS: {} ký tự ({} dòng)".format(len(css), len(css.splitlines())))
    print("JS:  {} ký tự ({} dòng)".format(len(js), len(js.splitlines())))

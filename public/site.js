(function(){
  var c=document.getElementById('cookie'),k='ar-consent';
  try{if(!localStorage.getItem(k))c.hidden=false}catch(e){c.hidden=false}
  c.addEventListener('click',function(e){var v=e.target.getAttribute('data-v');if(!v)return;try{localStorage.setItem(k,v)}catch(x){}c.hidden=true});
})();

(function(){
  var bs=document.querySelectorAll('.case-trigger');
  bs.forEach(function(b){
    var m=(b.getAttribute('onclick')||'').match(/'(case\d+)'/); if(!m) return;
    b.setAttribute('aria-expanded','false'); b.setAttribute('aria-controls',m[1]);
    b.addEventListener('click',function(){setTimeout(function(){var p=document.getElementById(m[1]); if(p) b.setAttribute('aria-expanded', p.style.maxHeight && p.style.maxHeight!=='0px' ? 'true':'false');},60);});
  });
})();

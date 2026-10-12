(function(){
  var c=document.getElementById('cookie'),k='ar-consent';
  try{if(!localStorage.getItem(k))c.hidden=false}catch(e){c.hidden=false}
  c.addEventListener('click',function(e){var v=e.target.getAttribute('data-v');if(!v)return;try{localStorage.setItem(k,v)}catch(x){}c.hidden=true});
})();

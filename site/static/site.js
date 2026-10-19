// World of SWOS: the mobile menu and the remembered language (a per-viewer convenience only).
(function () {
  var top = document.querySelector('.top'), btn = document.querySelector('.menu-btn');
  if (btn && top) btn.addEventListener('click', function () {
    var open = top.classList.toggle('open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  var lang = document.documentElement.lang;
  try { localStorage.setItem('lang', lang); } catch (e) {}
  document.querySelectorAll('.lang a').forEach(function (a) {
    a.addEventListener('click', function () { try { localStorage.setItem('lang', a.getAttribute('hreflang')); } catch (e) {} });
  });
})();

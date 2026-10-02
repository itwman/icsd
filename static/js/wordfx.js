/* کلمات ذره‌ای هیرو — هر کلمه از ذره ساخته می‌شود، به کلمه‌ی بعد تبدیل می‌شود و در پایان لوگو.
   ماوس/لمس ذره‌ها را کنار می‌زند؛ کلیک = انفجار و ساخت دوباره. رنگ‌ها از --sabz و --firoozeh (روز/شب).
   داده‌ها از data-words (جداشده با |)، data-logo و data-interval روی #wordfx. Canvas خالص، بدون کتابخانه. */
(function () {
  'use strict';
  var box = document.getElementById('wordfx'); if (!box) return;
  var cv = box.querySelector('canvas'); if (!cv || !cv.getContext) return;
  var ctx = cv.getContext('2d');
  var words = (box.dataset.words || '').split('|').map(function (w) { return w.trim(); }).filter(Boolean);
  var logoUrl = box.dataset.logo || '';
  var interval = Math.max(1200, parseInt(box.dataset.interval, 10) || 3200);
  var root = document.documentElement;
  var reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var FONT = "'Vazirmatn', Tahoma, sans-serif";

  var W = 0, H = 0, GAP = 4, DOT = 2.4, R = 90;
  var shapes = [], parts = [], N = 0, cur = 0, t = 0;
  var mx = -1e4, my = -1e4, visible = true, ready = false, logoImg = null, lastW = 0;
  var c1 = '#1E9E7B', c2 = '#16A9C7', hot1 = '#F05C7E', hot2 = '#F2A83B';
  var OFF = document.createElement('canvas');
  var octx = OFF.getContext('2d', { willReadFrequently: true });

  function readColors() {
    var s = getComputedStyle(root);
    c1 = s.getPropertyValue('--sabz').trim() || c1;
    c2 = s.getPropertyValue('--firoozeh').trim() || c2;
    hot1 = s.getPropertyValue('--golab').trim() || hot1;
    hot2 = s.getPropertyValue('--zaferan').trim() || hot2;
  }

  function fit() {
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    W = box.clientWidth; H = box.clientHeight;
    cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    GAP = W < 520 ? 2 : 3;
    DOT = W < 520 ? 1.5 : 2.1;
    R = Math.max(60, Math.min(110, W / 6));
    OFF.width = W; OFF.height = H;
  }

  function collect(test) {
    var d = octx.getImageData(0, 0, W, H).data, pts = [];
    for (var y = 0; y < H; y += GAP) for (var x = 0; x < W; x += GAP) {
      var i = (y * W + x) * 4;
      if (test(d, i)) pts.push({ x: x, y: y });
    }
    return pts;
  }

  /* کلمه: اندازه‌ی جدا برای هر کلمه تا هم کلمه‌ی کوتاه درشت باشد هم کلمه‌ی بلند جا شود */
  function sampleWord(word) {
    octx.clearRect(0, 0, W, H);
    octx.direction = 'rtl'; octx.textAlign = 'center'; octx.textBaseline = 'alphabetic';
    octx.font = '800 100px ' + FONT;
    var m = octx.measureText(word), w = m.width || 1;
    var size = Math.min(100 * (W * 0.94) / w, H * 0.66);
    octx.font = '800 ' + size + 'px ' + FONT;
    m = octx.measureText(word);
    var asc = m.actualBoundingBoxAscent || size * 0.7, desc = m.actualBoundingBoxDescent || size * 0.25;
    octx.fillStyle = '#fff';
    octx.fillText(word, W / 2, H / 2 + (asc - desc) / 2);
    return collect(function (d, i) { return d[i + 3] > 130; });
  }

  /* لوگو: SVG شفاف با آلفا؛ برای PNG/JPG با پس‌زمینه، پیکسل‌های هم‌رنگ گوشه حذف می‌شوند */
  function sampleLogo(img) {
    octx.clearRect(0, 0, W, H);
    var r = (img.naturalWidth || 1) / (img.naturalHeight || 1);
    var h = H * 0.92, w = h * r;
    if (w > W * 0.9) { w = W * 0.9; h = w / r; }
    var x0 = (W - w) / 2, y0 = (H - h) / 2;
    octx.drawImage(img, x0, y0, w, h);
    var c = octx.getImageData(Math.round(x0) + 1, Math.round(y0) + 1, 1, 1).data;
    var opaqueBg = c[3] > 200;
    return collect(function (d, i) {
      if (d[i + 3] < 130) return false;
      if (!opaqueBg) return true;
      return Math.abs(d[i] - c[0]) + Math.abs(d[i + 1] - c[1]) + Math.abs(d[i + 2] - c[2]) > 70;
    });
  }

  function build() {
    fit(); readColors();
    shapes = words.map(sampleWord).filter(function (p) { return p.length; });
    if (logoImg) {
      /* لوگو از دامنه‌ی دیگر (CDN/مدیا) بدون CORS بوم را «آلوده» می‌کند؛ در آن صورت فقط کلمه‌ها */
      try { var lp = sampleLogo(logoImg); if (lp.length) shapes.push(lp); } catch (e) { logoImg = null; }
    }
    if (!shapes.length) return;
    N = 0; shapes.forEach(function (s) { if (s.length > N) N = s.length; });
    var old = parts; parts = [];
    for (var i = 0; i < N; i++) {
      var o = old[i];
      parts.push(o ? o : { x: Math.random() * W, y: Math.random() * H, vx: 0, vy: 0, ph: Math.random() * 6.283 });
    }
    if (cur >= shapes.length) cur = 0;
    ready = true;
  }

  function kick(power) {
    for (var i = 0; i < N; i++) {
      var a = Math.random() * 6.283, s = Math.random() * power;
      parts[i].vx += Math.cos(a) * s; parts[i].vy += Math.sin(a) * s;
    }
  }

  function paint(staticOnly) {
    ctx.clearRect(0, 0, W, H);
    var pts = shapes[cur], len = pts.length, hot = [];
    var breathe = 1 + 0.018 * Math.sin(t * 0.45), cx = W / 2, cy = H / 2;
    ctx.globalCompositeOperation = 'source-over';
    ctx.fillStyle = '#000';
    for (var i = 0; i < N; i++) {
      var p = parts[i], q = pts[i % len];
      if (staticOnly) { ctx.fillRect(q.x, q.y, DOT, DOT); continue; }
      var tx = cx + (q.x - cx) * breathe + Math.sin(t + p.ph) * 0.7;
      var ty = cy + (q.y - cy) * breathe + Math.cos(t * 0.8 + p.ph) * 0.7;
      p.vx = p.vx * 0.8 + (tx - p.x) * 0.06;
      p.vy = p.vy * 0.8 + (ty - p.y) * 0.06;
      var ex = p.x - mx, ey = p.y - my, d = Math.sqrt(ex * ex + ey * ey) || 1;
      var k = d < R ? 1 - d / R : 0;
      if (k) { p.vx += ex / d * k * 5; p.vy += ey / d * k * 5; }
      p.x += p.vx; p.y += p.vy;
      if (k > 0.3) hot.push(p, k); else ctx.fillRect(p.x, p.y, DOT, DOT);
    }
    /* رنگ‌آمیزی یک‌جا: همه‌ی ذره‌ها گرادیان سبز → فیروزه‌ای (راست به چپ) می‌گیرند */
    ctx.globalCompositeOperation = 'source-in';
    var g = ctx.createLinearGradient(W, 0, 0, H);
    g.addColorStop(0, c1); g.addColorStop(1, c2);
    ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
    ctx.globalCompositeOperation = 'source-over';
    for (var j = 0; j < hot.length; j += 2) {
      var hp = hot[j], hk = hot[j + 1], sz = DOT + 1.6 * hk;
      ctx.fillStyle = hk > 0.62 ? hot1 : hot2;
      ctx.fillRect(hp.x, hp.y, sz, sz);
    }
  }

  function loop() {
    if (ready && visible && !document.hidden) { t += 0.05; paint(false); }
    requestAnimationFrame(loop);
  }

  var timer = null;
  function schedule() {
    clearTimeout(timer);
    var isLogo = logoImg && cur === shapes.length - 1;
    timer = setTimeout(function () {
      if (ready && visible && !document.hidden && shapes.length > 1) {
        cur = (cur + 1) % shapes.length; kick(2.2);
      }
      schedule();
    }, isLogo ? interval * 1.5 : interval);
  }

  /* ورودی: Pointer Events برای ماوس و لمس؛ بعد از برداشتن انگشت، ذره‌ها برمی‌گردند */
  function setPtr(e) { var r = box.getBoundingClientRect(); mx = e.clientX - r.left; my = e.clientY - r.top; }
  function clearPtr() { mx = -1e4; my = -1e4; }
  box.addEventListener('pointermove', setPtr, { passive: true });
  box.addEventListener('pointerdown', setPtr, { passive: true });
  box.addEventListener('pointerleave', clearPtr, { passive: true });
  box.addEventListener('pointerup', function (e) { if (e.pointerType !== 'mouse') clearPtr(); }, { passive: true });
  box.addEventListener('pointercancel', clearPtr, { passive: true });
  box.addEventListener('click', function () { if (ready && !reduced) kick(14); });

  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (es) { es.forEach(function (e) { visible = e.isIntersecting; }); },
      { rootMargin: '80px' }).observe(box);
  }
  /* تغییر حالت شب/روز یا رنگ برند → رنگ‌ها دوباره خوانده شوند */
  new MutationObserver(function () { readColors(); if (reduced && ready) paint(true); })
    .observe(root, { attributes: true, attributeFilter: ['data-mode', 'style', 'class'] });

  /* فقط تغییر عرض بازسازی می‌کند (در مرورگرهای داخل‌برنامه‌ای، اسکرول ارتفاع را عوض می‌کند) */
  var rz;
  addEventListener('resize', function () {
    if (box.clientWidth === lastW) return;
    clearTimeout(rz); rz = setTimeout(function () { lastW = box.clientWidth; build(); if (reduced) paint(true); }, 160);
  }, { passive: true });

  function start() {
    lastW = box.clientWidth;
    build();
    if (!ready) return;
    box.classList.add('is-on');
    if (reduced) { cur = 0; paint(true); return; }
    loop(); schedule();
  }

  function whenFont(cb) {
    var done = false, go = function () { if (!done) { done = true; cb(); } };
    if (document.fonts && document.fonts.load) document.fonts.load("800 80px 'Vazirmatn'").then(go, go);
    setTimeout(go, 1800);
  }

  whenFont(function () {
    if (!logoUrl) return start();
    var img = new Image();
    try { if (new URL(logoUrl, location.href).origin !== location.origin) img.crossOrigin = 'anonymous'; } catch (e) {}
    img.onload = function () { logoImg = img; start(); };
    img.onerror = function () { start(); };
    img.src = logoUrl;
  });
})();

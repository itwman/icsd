/* تپه سیلک — منظره‌ی تمام‌عرض: تپه‌ی جنوبی (بزرگ) و شمالی (کوچک)، لایه‌های فرسایش‌یافته،
   ترانشه‌ی کاوش، و شبکه‌ی عصبی که از عمق به سطح پالس می‌فرستد. Canvas خالص. */
(function () {
  'use strict';
  var cv = document.getElementById('sialk'); if (!cv) return;
  var ctx = cv.getContext('2d'), W = 0, H = 0, dpr = Math.min(devicePixelRatio || 1, 2);
  var reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var root = document.documentElement;
  var css = function (v) { return getComputedStyle(root).getPropertyValue(v).trim(); };

  function noise(x, s) { return Math.sin(x * 1.7 + s) * .5 + Math.sin(x * 4.3 + s * 2.1) * .25 + Math.sin(x * 9.1 + s * .7) * .125; }
  function bump(u, w, p) { var t = 1 - Math.pow(Math.abs(u) / w, 2); return t > 0 ? Math.pow(t, p) : 0; } // u: فاصله از مرکز (نسبت به W)

  /* شکل زمین: دو تپه‌ی واقعی سیلک — جنوبی بلندتر و پهن‌تر، شمالی کوتاه‌تر؛ قله‌ها پهن و فرسوده */
  function terrain(x) {
    var u = x / W;
    var south = bump(u - .60, .36, .55) * 1.00;   // تپه‌ی جنوبی
    var north = bump(u - .18, .19, .6) * .58;     // تپه‌ی شمالی
    var saddle = bump(u - .39, .12, 1) * .18;     // زین بین دو تپه
    return Math.max(south, north, saddle) + .04;  // دشت پایه
  }

  var strata = [], nodes = [], edges = [], pulses = [], t0 = performance.now();
  var LAYERS = [
    { f: 1.00, c: ['#B4533A', '#9E4A34'] }, { f: .86, c: ['#C0603F', '#AD5539'] }, { f: .73, c: ['#CF7249', '#BE6440'] },
    { f: .60, c: ['#DC8658', '#CC7650'] }, { f: .47, c: ['#E89E70', '#D98A5F'] }, { f: .34, c: ['#F0B58C', '#E4A276'] }
  ];

  function build() {
    strata = []; nodes = []; edges = []; pulses = [];
    var maxH = H * .86;
    LAYERS.forEach(function (L, i) {
      var pts = [], seed = i * 9.3;
      for (var x = -12; x <= W + 12; x += 5) {
        var h = terrain(x) * maxH * L.f;
        var erosion = noise(x / 55, seed) * (6 + i * 3.2) * Math.min(1, h / 40);
        pts.push([x, Math.min(H - h + erosion, H)]);
      }
      strata.push({ pts: pts, c: L.c });
    });
    /* گره‌ها: روی لایه‌ها، بیشتر داخل تپه‌ها */
    var id = 0;
    strata.forEach(function (S, li) {
      var step = 4 + li;
      for (var k = step; k < S.pts.length - step; k += step) {
        var p = S.pts[k]; if (H - p[1] < 14) continue;
        if (Math.random() < .55) continue;
        nodes.push({ id: id++, x: p[0] + (Math.random() - .5) * 8, y: p[1] + 6 + Math.random() * 10, layer: li, r: 1.8 + Math.random() * 1.5, phase: Math.random() * 6.28 });
      }
    });
    var maxD = Math.max(70, W * .075);
    nodes.forEach(function (a) { nodes.forEach(function (b) {
      if (b.id <= a.id) return;
      var d = Math.hypot(a.x - b.x, a.y - b.y);
      if (d < maxD && Math.abs(a.layer - b.layer) <= 1 && Math.random() < .5) edges.push({ a: a, b: b });
    }); });
  }

  function drawTrench() {
    /* ترانشه‌ی کاوش روی دامنه‌ی تپه‌ی جنوبی: برش پله‌ای که لایه‌ها را نشان می‌دهد */
    var x0 = W * .66, top = H - terrain(x0) * H * .86 + 6, w = Math.max(40, W * .05);
    ctx.save();
    ctx.fillStyle = 'rgba(60,25,12,.28)';
    for (var s = 0; s < 4; s++) { ctx.fillRect(x0 + s * 3, top + s * 9, w - s * 6, 9); }
    ctx.strokeStyle = 'rgba(255,240,220,.35)'; ctx.lineWidth = 1;
    for (var k = 0; k < 4; k++) { ctx.beginPath(); ctx.moveTo(x0 + k * 3, top + k * 9); ctx.lineTo(x0 + w - k * 3, top + k * 9); ctx.stroke(); }
    ctx.restore();
  }

  function draw(now) {
    var t = (now - t0) / 1000, dark = root.getAttribute('data-mode') === 'shab';
    ctx.clearRect(0, 0, W, H);
    /* خورشید کم‌رنگ پشت تپه‌ی شمالی */
    var g = ctx.createRadialGradient(W * .3, H * .35, 0, W * .3, H * .35, H * .9);
    g.addColorStop(0, dark ? 'rgba(242,168,59,.10)' : 'rgba(242,168,59,.22)'); g.addColorStop(1, 'rgba(242,168,59,0)');
    ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);

    strata.forEach(function (S) {
      var lg = ctx.createLinearGradient(0, H * .2, 0, H);
      lg.addColorStop(0, S.c[0]); lg.addColorStop(1, S.c[1]);
      ctx.beginPath(); ctx.moveTo(S.pts[0][0], H);
      S.pts.forEach(function (p) { ctx.lineTo(p[0], p[1]); });
      ctx.lineTo(S.pts[S.pts.length - 1][0], H); ctx.closePath();
      ctx.fillStyle = lg; ctx.globalAlpha = dark ? .8 : .96; ctx.fill(); ctx.globalAlpha = 1;
      /* آبراهه‌های فرسایش */
      ctx.strokeStyle = 'rgba(0,0,0,.08)'; ctx.lineWidth = 1; ctx.beginPath();
      S.pts.forEach(function (p, k) { if (k % 3 === 0 && H - p[1] > 10) { ctx.moveTo(p[0], p[1] + 3); ctx.lineTo(p[0] + 2, Math.min(p[1] + 14, H)); } });
      ctx.stroke();
    });
    drawTrench();

    var sabz = css('--sabz') || '#1E9E7B';
    ctx.lineWidth = 1;
    edges.forEach(function (e) {
      var a = .10 + .10 * (Math.sin(t * .8 + e.a.phase) * .5 + .5);
      ctx.strokeStyle = 'rgba(255,255,255,' + (dark ? a * .7 : a) + ')';
      ctx.beginPath(); ctx.moveTo(e.a.x, e.a.y); ctx.lineTo(e.b.x, e.b.y); ctx.stroke();
    });
    if (!reduced && Math.random() < .08 && edges.length) pulses.push({ e: edges[Math.floor(Math.random() * edges.length)], p: 0, sp: .008 + Math.random() * .012 });
    pulses = pulses.filter(function (P) { P.p += P.sp; return P.p <= 1; });
    pulses.forEach(function (P) {
      var x = P.e.a.x + (P.e.b.x - P.e.a.x) * P.p, y = P.e.a.y + (P.e.b.y - P.e.a.y) * P.p;
      ctx.beginPath(); ctx.arc(x, y, 6, 0, 6.28); ctx.fillStyle = 'rgba(30,158,123,.18)'; ctx.fill();
      ctx.beginPath(); ctx.arc(x, y, 2.2, 0, 6.28); ctx.fillStyle = sabz; ctx.fill();
    });
    nodes.forEach(function (n) {
      var glow = .45 + .55 * (Math.sin(t * 1.3 + n.phase) * .5 + .5);
      ctx.beginPath(); ctx.arc(n.x, n.y, n.r + 3, 0, 6.28); ctx.fillStyle = 'rgba(30,158,123,' + (glow * .16) + ')'; ctx.fill();
      ctx.beginPath(); ctx.arc(n.x, n.y, n.r, 0, 6.28); ctx.fillStyle = sabz; ctx.globalAlpha = .5 + glow * .5; ctx.fill(); ctx.globalAlpha = 1;
    });
    if (!reduced) requestAnimationFrame(draw);
  }

  function resize() { var r = cv.getBoundingClientRect(); W = r.width; H = r.height; cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0); build(); }
  resize(); addEventListener('resize', resize);
  requestAnimationFrame(draw);
  if (reduced) setTimeout(function () { draw(performance.now()); }, 0);
})();

/* ICSD — رفتار مشترک سایت. بدون jQuery، بدون CDN. */
(function () {
  'use strict';
  var FA = '۰۱۲۳۴۵۶۷۸۹', AR = '٠١٢٣٤٥٦٧٨٩';
  var toEn = function (s) { return String(s).replace(/[۰-۹]/g, function (d) { return FA.indexOf(d); }).replace(/[٠-٩]/g, function (d) { return AR.indexOf(d); }); };
  var toFa = function (s) { return String(s).replace(/\d/g, function (d) { return FA[+d]; }); };
  window.icsd = { toEn: toEn, toFa: toFa };

  /* ── شب / روز ── */
  var root = document.documentElement, modeBtn = document.getElementById('mode');
  function setMode(m) {
    root.setAttribute('data-mode', m);
    if (modeBtn) { modeBtn.textContent = m === 'rooz' ? 'شب' : 'روز'; }
    try { localStorage.setItem('icsd-mode', m); } catch (e) {}
  }
  setMode(root.getAttribute('data-mode') || 'rooz');
  if (modeBtn) modeBtn.addEventListener('click', function () { setMode(root.getAttribute('data-mode') === 'rooz' ? 'shab' : 'rooz'); });

  /* ── سربرگ ── */
  var nav = document.getElementById('nav');
  if (nav) { var onS = function () { nav.classList.toggle('stuck', scrollY > 8); }; onS(); addEventListener('scroll', onS, { passive: true }); }
  var burger = document.getElementById('burger'), mnav = document.getElementById('mobile-nav');
  if (burger && mnav) burger.addEventListener('click', function () { var o = mnav.classList.toggle('is-open'); burger.setAttribute('aria-expanded', String(o)); });

  /* ── تقویم شمسی ── */
  if (window.jalaliDatepicker) {
    jalaliDatepicker.startWatch({ persianDigits: true, autoShow: true, autoHide: true, hideAfterChange: true,
      showTodayBtn: true, showEmptyBtn: true, time: false, separatorChar: '/', zIndex: 2000 });
  }

  /* ── انتخابگر آژاکسی (Tom Select) ── */
  function csrf() { var m = document.cookie.match(/(?:^|;\s*)csrftoken=([^;]*)/); return m ? decodeURIComponent(m[1]) : ''; }
  function autocomplete(el) {
    if (!window.TomSelect || el.tomselect) return;
    var url = el.dataset.autocompleteUrl, allowCreate = el.dataset.allowCreate !== 'false';
    var dep = el.dataset.dependsOn ? document.getElementById(el.dataset.dependsOn) : null;
    var extra = function () { return dep && dep.value ? '&province=' + encodeURIComponent(dep.value) : ''; };
    var ts = new TomSelect(el, {
      valueField: 'value', labelField: 'text', searchField: 'text', maxOptions: 20, loadThrottle: 250, persist: false,
      createOnBlur: false, closeAfterSelect: !el.multiple, plugins: el.multiple ? ['remove_button'] : [],
      placeholder: el.getAttribute('placeholder') || 'تایپ کنید…',
      preload: 'focus',
      load: function (q, cb) {
        fetch(url + '?q=' + encodeURIComponent(q) + extra(), { headers: { 'X-Requested-With': 'XMLHttpRequest' } })
          .then(function (r) { return r.ok ? r.json() : { results: [] }; }).then(function (j) { cb(j.results || []); }).catch(function () { cb(); });
      },
      create: allowCreate ? function (input, cb) {
        var body = { text: input }; if (dep) body.province = dep.value;
        fetch(url, { method: 'POST', headers: { 'Content-Type': 'application/json', 'X-CSRFToken': csrf(), 'X-Requested-With': 'XMLHttpRequest' }, body: JSON.stringify(body) })
          .then(function (r) { return r.json(); }).then(function (j) { cb(j && j.value !== undefined ? j : false); if (j && j.error) alert(j.error); }).catch(function () { cb(false); });
      } : false,
      render: {
        option_create: function (d, esc) { return '<div class="create">افزودن «<strong>' + esc(d.input) + '</strong>»</div>'; },
        no_results: function () { return '<div class="no-results">موردی یافت نشد' + (allowCreate ? ' — تایپ کنید تا ساخته شود' : '') + '</div>'; },
        loading: function () { return '<div class="spinner-row">در حال جستجو…</div>'; }
      }
    });
    if (dep) dep.addEventListener('change', function () { ts.clear(); ts.clearOptions(); ts.load(''); });
  }
  document.querySelectorAll('[data-autocomplete-url]').forEach(autocomplete);

  /* ── نرمال‌سازی اعداد هنگام ارسال ── */
  document.querySelectorAll('form').forEach(function (f) {
    f.addEventListener('submit', function () {
      f.querySelectorAll('input[data-jdp], input[inputmode="numeric"]').forEach(function (i) { i.value = toEn(i.value); });
    });
  });

  /* ── نوار نقش سفال سیلک ── */
  var band = document.getElementById('band');
  if (band) {
    var zig = '<svg viewBox="0 0 60 26" fill="none"><path d="M2 22h56M2 4h56" stroke="currentColor" stroke-width="1.4"/><path d="M4 18l5-9 5 9M18 18l5-9 5 9M32 18l5-9 5 9M46 18l5-9 5 9" stroke="currentColor" stroke-width="1.2" stroke-linejoin="round"/></svg>';
    var boz = '<svg viewBox="0 0 34 26" fill="none"><path d="M17 21l-4-8h8z" fill="currentColor"/><path d="M13.5 12C6 8 5 2.5 11 1M20.5 12C28 8 29 2.5 23 1" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>';
    var unit = (zig + boz).repeat(10); band.innerHTML = unit + unit;
  }

  /* ── ساعت ── */
  var clock = document.getElementById('clock');
  if (clock) {
    var NS = 'http://www.w3.org/2000/svg';
    var fr = document.getElementById('frieze'); for (var i = 0; i < 12; i++) { var u = document.createElementNS(NS, 'use'); u.setAttribute('href', '#boz'); u.setAttribute('transform', 'rotate(' + (i * 30) + ' 100 100) translate(100 25)'); fr.appendChild(u); }
    var tk = document.getElementById('ticks'); for (var j = 0; j < 60; j++) { var big = j % 5 === 0, l = document.createElementNS(NS, 'line'); l.setAttribute('x1', 100); l.setAttribute('y1', big ? 36 : 39); l.setAttribute('x2', 100); l.setAttribute('y2', 43); l.setAttribute('stroke-width', big ? 2 : .9); l.setAttribute('opacity', big ? .85 : .4); l.setAttribute('stroke-linecap', 'round'); l.setAttribute('transform', 'rotate(' + (j * 6) + ' 100 100)'); tk.appendChild(l); }
    var nm = document.getElementById('nums'); for (var h = 1; h <= 12; h++) { var a = ((h / 12) * 360 - 90) * Math.PI / 180, t = document.createElementNS(NS, 'text'); t.setAttribute('x', (100 + Math.cos(a) * 55).toFixed(1)); t.setAttribute('y', (100 + Math.sin(a) * 55 + 5.4).toFixed(1)); t.textContent = toFa(h); nm.appendChild(t); }
    var hH = document.getElementById('h-hour'), hM = document.getElementById('h-min'), hS = document.getElementById('h-sec');
    var eH = document.getElementById('t-h'), eM = document.getElementById('t-m'), eS = document.getElementById('t-s'), eMs = document.getElementById('t-ms'), eD = document.getElementById('t-date');
    var pad = function (n, w) { return String(n).padStart(w, '0'); };
    function digits(el, str) { if (!el || el.dataset.v === str) return; el.dataset.v = str; el.textContent = ''; toFa(str).split('').forEach(function (ch) { var s = document.createElement('span'); s.className = 'dg'; s.textContent = ch; el.appendChild(s); }); }
    var fmt = null; try { fmt = new Intl.DateTimeFormat('fa-IR', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' }); } catch (e) {}
    var lastDay = '';
    (function frame() {
      var now = new Date(), ms = now.getMilliseconds(), s = now.getSeconds() + ms / 1000, m = now.getMinutes() + s / 60, hh = (now.getHours() % 12) + m / 60;
      hH.setAttribute('transform', 'rotate(' + (hh * 30) + ' 100 100)'); hM.setAttribute('transform', 'rotate(' + (m * 6) + ' 100 100)'); hS.setAttribute('transform', 'rotate(' + (s * 6) + ' 100 100)');
      digits(eH, pad(now.getHours(), 2)); digits(eM, pad(now.getMinutes(), 2)); digits(eS, pad(now.getSeconds(), 2)); digits(eMs, '٫' + pad(ms, 3));
      var dk = now.toDateString(); if (fmt && eD && dk !== lastDay) { lastDay = dk; eD.textContent = fmt.format(now); }
      requestAnimationFrame(frame);
    })();
  }

  /* ── تکمیل درس با آژاکس (بدون رفرش) ── */
  var doneForm = document.getElementById('done-form');
  if (doneForm) doneForm.addEventListener('submit', function (e) {
    var nxt = doneForm.querySelector('[name=next]');
    e.preventDefault();
    fetch(doneForm.action, { method: 'POST', headers: { 'X-CSRFToken': csrf(), 'X-Requested-With': 'XMLHttpRequest' }, body: new FormData(doneForm) })
      .then(function (r) { return r.json(); }).then(function (j) {
        var pb = document.getElementById('pbar'), pt = document.getElementById('ptext');
        if (pb) pb.style.width = j.percent + '%'; if (pt) pt.textContent = toFa(j.percent) + '٪';
        location.href = nxt ? nxt.value : location.href;
      }).catch(function () { doneForm.submit(); });
  });
})();

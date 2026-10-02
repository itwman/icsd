/* پنل سئوی زنده در ادمین — پیش‌نمایش گوگل، شمارنده‌ها و امتیاز (همان قواعد apps/seo/analysis.py) */
(function () {
  'use strict';
  function ready(fn) { document.readyState !== 'loading' ? fn() : document.addEventListener('DOMContentLoaded', fn); }
  ready(function () {
    var panel = document.getElementById('seo-panel'); if (!panel) return;
    var $ = function (id) { return document.getElementById(id); };
    var site = panel.dataset.site || '', base = panel.dataset.url || location.origin, prefix = panel.dataset.prefix || '/';
    var f = { title: $('id_' + panel.dataset.title) || $('id_title') || $('id_name'), seo: $('id_seo_title'), desc: $('id_meta_description'),
              kw: $('id_focus_keyword'), slug: $('id_slug'), body: $('id_' + panel.dataset.body) };
    var FA = { 'ي': 'ی', 'ك': 'ک', '‌': ' ', 'ة': 'ه', 'أ': 'ا', 'إ': 'ا', 'ۀ': 'ه' };
    var norm = function (s) { return (s || '').replace(/[يكة‌أإۀ]/g, function (c) { return FA[c]; }).replace(/\s+/g, ' ').trim().toLowerCase(); };
    var text = function (h) { var d = document.createElement('div'); d.innerHTML = h || ''; return (d.textContent || '').replace(/\s+/g, ' ').trim(); };
    var count = function (hay, needle) { if (!needle) return 0; var n = 0, i = 0; while ((i = hay.indexOf(needle, i)) !== -1) { n++; i += needle.length; } return n; };
    function bodyHtml() {
      var ed = window.editors && f.body && window.editors[f.body.id];
      return ed ? ed.getData() : (f.body ? f.body.value : '');
    }

    panel.innerHTML =
      '<div class="seo-grid">' +
      '<div class="seo-snip"><small>پیش‌نمایش در گوگل</small><div class="seo-snip__card">' +
      '<div class="seo-snip__url"></div><div class="seo-snip__t"></div><div class="seo-snip__d"></div></div></div>' +
      '<div class="seo-score"><div class="seo-ring"><b>0</b><span>امتیاز سئو</span></div></div></div>' +
      '<ul class="seo-checks"></ul>';
    var el = { url: panel.querySelector('.seo-snip__url'), t: panel.querySelector('.seo-snip__t'), d: panel.querySelector('.seo-snip__d'),
               ring: panel.querySelector('.seo-ring'), score: panel.querySelector('.seo-ring b'), list: panel.querySelector('.seo-checks') };

    function counter(input, lo, hi) {
      if (!input) return;
      var c = document.createElement('div'); c.className = 'seo-counter'; c.innerHTML = '<i></i><span></span>';
      input.insertAdjacentElement('afterend', c);
      input._counter = function () {
        var n = input.value.length, pct = Math.min(100, n / hi * 100);
        c.querySelector('i').style.width = pct + '%';
        c.className = 'seo-counter ' + (n >= lo && n <= hi ? 'is-ok' : n === 0 ? '' : 'is-warn');
        c.querySelector('span').textContent = n + ' / ' + lo + '–' + hi + ' کاراکتر';
      };
    }
    counter(f.seo, 30, 60); counter(f.desc, 120, 160);

    function run() {
      var title = f.title ? f.title.value : '', seo = f.seo ? f.seo.value : '', desc = f.desc ? f.desc.value : '';
      var kw = norm(f.kw ? f.kw.value : ''), slug = f.slug ? f.slug.value : '', html = bodyHtml(), t = seo || title;
      var plain = text(html), words = plain ? plain.split(' ').length : 0;
      var shownTitle = seo ? seo : (title + (site ? ' | ' + site : ''));
      el.url.textContent = base.replace(/^https?:\/\//, '') + ' › ' + (prefix.replace(/^\/|\/$/g, '').split('/').filter(Boolean).concat([slug]).join(' › '));
      el.t.textContent = shownTitle.length > 62 ? shownTitle.slice(0, 60) + '…' : shownTitle || 'عنوان صفحه';
      el.d.textContent = (desc || plain.slice(0, 155) || 'توضیح متا را بنویسید…').slice(0, 160);

      var checks = [], add = function (st, msg, w) { checks.push([st, msg, w || 1]); };
      var fullLen = t.length + (seo ? 0 : (site.length + 3));
      if (!kw) add('bad', 'کلیدواژه‌ی کانونی تعیین نشده است.', 2);
      add(fullLen >= 30 && fullLen <= 62 ? 'ok' : 'warn', 'طول عنوان: ' + fullLen + ' کاراکتر (۳۰ تا ۶۰).');
      add(desc.length >= 110 && desc.length <= 165 ? 'ok' : desc.length ? 'warn' : 'bad', 'طول توضیح متا: ' + desc.length + ' کاراکتر (۱۲۰ تا ۱۶۰).', desc.length ? 1 : 2);
      if (kw) {
        var nt = norm(t), np = norm(plain);
        add(nt.indexOf(kw) > -1 ? 'ok' : 'bad', 'کلیدواژه در عنوان' + (nt.indexOf(kw) > -1 ? ' آمده.' : ' نیامده.'), 2);
        add(nt.indexOf(kw) === 0 ? 'ok' : 'warn', nt.indexOf(kw) === 0 ? 'کلیدواژه در ابتدای عنوان است.' : 'بهتر است کلیدواژه در ابتدای عنوان بیاید.');
        add(norm(desc).indexOf(kw) > -1 ? 'ok' : 'bad', 'کلیدواژه در توضیح متا' + (norm(desc).indexOf(kw) > -1 ? ' آمده.' : ' نیامده.'));
        var first = norm(plain.split(' ').slice(0, 80).join(' '));
        add(first.indexOf(kw) > -1 ? 'ok' : 'warn', 'کلیدواژه در پاراگراف اول' + (first.indexOf(kw) > -1 ? ' آمده.' : ' نیامده.'));
        var heads = norm((html.match(/<h[23][^>]*>[\s\S]*?<\/h[23]>/g) || []).map(text).join(' '));
        add(heads.indexOf(kw) > -1 ? 'ok' : 'warn', 'کلیدواژه در تیترهای H2/H3' + (heads.indexOf(kw) > -1 ? ' آمده.' : ' نیامده.'));
        var n = count(np, kw), dens = words ? n * kw.split(' ').length / words * 100 : 0;
        add(dens >= 0.5 && dens <= 2.5 ? 'ok' : 'warn', 'تراکم کلیدواژه: ' + dens.toFixed(1) + '٪ (' + n + ' بار) — بین ۰٫۵ تا ۲٫۵٪.');
        if (/[؀-ۿ]/.test(slug)) add(norm(slug.replace(/-/g, ' ')).indexOf(kw) > -1 ? 'ok' : 'warn', 'نامک ' + (norm(slug.replace(/-/g, ' ')).indexOf(kw) > -1 ? 'کلیدواژه را دارد.' : 'کلیدواژه را ندارد.'));
      }
      if (f.body && words) {
        add(words >= 600 ? 'ok' : words >= 300 ? 'warn' : 'bad', 'طول متن: ' + words + ' کلمه' + (words < 600 ? ' (۶۰۰+ بهتر است).' : '.'), words < 300 ? 2 : 1);
        if (/<h1/i.test(html)) add('bad', 'داخل متن H1 هست؛ از H2 استفاده کنید.');
        add(/<h2/i.test(html) ? 'ok' : (words >= 300 ? 'warn' : 'ok'), /<h2/i.test(html) ? 'متن تیتر H2 دارد.' : 'متن تیتر فرعی H2 ندارد.');
        var imgs = html.match(/<img\b[^>]*>/g) || [], noAlt = imgs.filter(function (i) { return !/alt="[^"]+/.test(i); });
        if (imgs.length) add(noAlt.length ? 'warn' : 'ok', noAlt.length ? noAlt.length + ' تصویر بدون متن جایگزین (alt). روی تصویر کلیک و «متن جایگزین» را پر کنید.' : 'همه‌ی تصاویر alt دارند.');
        var links = (html.match(/<a\b[^>]*href="([^"]+)"/g) || []).filter(function (a) { return /href="\//.test(a); });
        add(links.length ? 'ok' : 'warn', links.length ? 'پیوند داخلی دارد.' : 'پیوند داخلی ندارد؛ به یک صفحه‌ی مرتبط در سایت لینک دهید.');
      }
      var tot = 0, got = 0;
      checks.forEach(function (c) { tot += c[2]; got += c[0] === 'ok' ? c[2] : c[0] === 'warn' ? c[2] / 2 : 0; });
      var sc = Math.round(got / (tot || 1) * 100);
      el.score.textContent = sc;
      el.ring.style.setProperty('--p', sc);
      el.ring.className = 'seo-ring ' + (sc >= 75 ? 'is-ok' : sc >= 50 ? 'is-warn' : 'is-bad');
      el.list.innerHTML = checks.sort(function (a, b) { return 'bwo'.indexOf(a[0][0]) - 'bwo'.indexOf(b[0][0]); })
        .map(function (c) { return '<li class="is-' + c[0] + '">' + c[1] + '</li>'; }).join('');
      [f.seo, f.desc].forEach(function (i) { if (i && i._counter) i._counter(); });
    }
    var tmr; function later() { clearTimeout(tmr); tmr = setTimeout(run, 250); }
    [f.title, f.seo, f.desc, f.kw, f.slug].forEach(function (i) { if (i) i.addEventListener('input', later); });
    var tries = 0; (function hook() {
      var ed = window.editors && f.body && window.editors[f.body.id];
      if (ed) { ed.model.document.on('change:data', later); run(); }
      else if (tries++ < 40) setTimeout(hook, 250); else run();
    })();
    run();
  });
})();

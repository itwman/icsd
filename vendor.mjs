/**
 * vendor.mjs — کپی دارایی‌های npm به assets/vendor
 *
 *   npm install
 *   node vendor.mjs
 *
 * بعد از این، پروژه هیچ وابستگی به اینترنت ندارد.
 * node_modules را می‌توانید پاک کنید؛ assets/vendor خودکفاست.
 */
import { readdirSync, statSync, mkdirSync, copyFileSync, existsSync } from 'node:fs';
import { join, dirname, basename } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = dirname(fileURLToPath(import.meta.url));
const NM = join(ROOT, 'node_modules');
const OUT = join(ROOT, 'static', 'vendor');

/** جستجوی بازگشتی برای اولین فایلی که با الگو بخواند */
function findFile(dir, matcher, depth = 8) {
  if (depth < 0 || !existsSync(dir)) return null;
  let entries;
  try { entries = readdirSync(dir); } catch { return null; }
  const dirs = [];
  for (const name of entries) {
    const full = join(dir, name);
    let st;
    try { st = statSync(full); } catch { continue; }
    if (st.isDirectory()) { dirs.push(full); continue; }
    if (matcher(name, full)) return full;
  }
  for (const d of dirs) {
    const hit = findFile(d, matcher, depth - 1);
    if (hit) return hit;
  }
  return null;
}

/** target: مسیر مقصد نسبت به assets/vendor  ·  pkg: نام بسته  ·  match: تابع تطبیق نام فایل */
const TASKS = [
  { target: 'bootstrap/bootstrap.rtl.min.css',       pkg: 'bootstrap',  match: (n) => n === 'bootstrap.rtl.min.css' },
  { target: 'bootstrap/bootstrap.rtl.min.css.map',   pkg: 'bootstrap',  match: (n) => n === 'bootstrap.rtl.min.css.map', optional: true },
  { target: 'bootstrap/bootstrap.bundle.min.js',     pkg: 'bootstrap',  match: (n) => n === 'bootstrap.bundle.min.js' },

  { target: 'tom-select/tom-select.css',             pkg: 'tom-select', match: (n) => n === 'tom-select.css' },
  { target: 'tom-select/tom-select.complete.min.js', pkg: 'tom-select', match: (n) => n === 'tom-select.complete.min.js' },

  { target: 'jalali-datepicker/jalalidatepicker.min.css', pkg: '@majidh1/jalalidatepicker', match: (n) => /^jalalidatepicker(\.min)?\.css$/.test(n) },
  { target: 'jalali-datepicker/jalalidatepicker.min.js',  pkg: '@majidh1/jalalidatepicker', match: (n) => /^jalalidatepicker(\.min)?\.js$/.test(n) },

  // فونت متغیر وزیرمتن — نام فایل در بسته متفاوت است، اولین woff2 متغیر را برمی‌داریم
  { target: 'vazirmatn/Vazirmatn[wght].woff2', pkg: 'vazirmatn',
    match: (n) => /\.woff2$/i.test(n) && /(\[wght\]|wght|variable)/i.test(n) },
  { target: 'vazirmatn/Vazirmatn-Regular.woff2', pkg: 'vazirmatn',
    match: (n) => /vazirmatn-regular\.woff2$/i.test(n), optional: true },

  // مونواسپیس — اختیاری
  { target: 'jetbrains-mono/JetBrainsMono[wght].woff2', pkg: '@fontsource-variable/jetbrains-mono',
    match: (n) => /\.woff2$/i.test(n) && /latin/i.test(n), optional: true },
];

let ok = 0, missing = [];

for (const t of TASKS) {
  const pkgDir = join(NM, ...t.pkg.split('/'));
  const src = findFile(pkgDir, t.match);
  if (!src) {
    if (!t.optional) missing.push(`${t.pkg} → ${t.target}`);
    continue;
  }
  const dest = join(OUT, t.target);
  mkdirSync(dirname(dest), { recursive: true });
  copyFileSync(src, dest);
  console.log(`  ✓ ${t.target}  ←  ${basename(src)}`);
  ok++;
}

console.log(`\n${ok} فایل کپی شد → static/vendor/`);

if (missing.length) {
  console.error('\n✗ پیدا نشد:');
  missing.forEach((m) => console.error('   ' + m));
  console.error('\nاول `npm install` را اجرا کنید.');
  process.exit(1);
}

console.log('آماده است. حالا: python manage.py runserver\n');

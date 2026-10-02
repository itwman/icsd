# ICSD — وب‌سایت جنگو

سایت جدید **توسعه هوشمند فرش ایرانیان**: محصولات، آکادمی (۱۷ دوره‌ی آماده)، وبلاگ، فرم شروع پروژه،
پرداخت زرین‌پال، پنل مدیریت فارسی، آمار بازدید داخلی و سئو. همه‌ی دارایی‌ها محلی، بدون CDN.

## راه‌اندازی لوکال (PowerShell — هر خط جدا)

```powershell
cd $HOME\Documents\icsd-django
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
npm install
node vendor.mjs
Copy-Item .env.example .env
python manage.py makemigrations
python manage.py migrate
python manage.py seed_site
python manage.py seed_geo
python manage.py seed_courses
python manage.py seed_quizzes
python manage.py setup_roles
python manage.py createsuperuser
python manage.py runserver
```

سپس: سایت `http://127.0.0.1:8000` — پنل `http://127.0.0.1:8000/admin/`

- `createsuperuser` شماره موبایل می‌پرسد (مثل `09123456789`) و رمز.
- در لوکال کد پیامکی در **ترمینال** چاپ می‌شود (`SMS_PROVIDER=console`).
- اگر `Activate.ps1` خطای اجرای اسکریپت داد: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

## ساختار

```
config/            settings · urls · unfold (پنل)
apps/
  common/          تاریخ شمسی، ارقام فارسی، آیکن‌ها، AutocompleteView، دکمه‌ی ویرایش
  core/            تنظیمات سایت (برند، لوگو، دامنه، رنگ، تماس)، بخش‌های صفحه اصلی، خط زمان، صفحات، منو
  accounts/        کاربر با موبایل، ورود OTP + رمز، نقش‌ها (setup_roles)
  academy/         دوره › فصل › درس (ویدیو: آروان / آپارات / آپلود)، ثبت‌نام، پیشرفت، seed_courses
  products/        محصول، قابلیت‌ها، گالری، آموزش‌های محصول، کاتالوگ چاپی
  blog/            نوشته، دسته، برچسب
  leads/           فرم شروع پروژه با آدرس کامل، استان/شهر (seed_geo)
  payments/        زرین‌پال (لایه‌ی قابل تعویض)
  analytics/       ثبت بازدید + داشبورد پنل
  seo/             متادیتا، ریدایرکت وردپرس، sitemap، robots
templates/         قالب‌ها (base.html + هر اپ)
static/            css · js · vendor (با node vendor.mjs پر می‌شود)
```

## چیزهایی که از پنل قابل تغییر است

| کجا | چه چیزی |
|---|---|
| تنظیمات سایت | نام برند، لوگو (روز/شب)، فاوآیکن، **آدرس سایت**، رنگ‌ها، متن هیرو، آمار، تماس، شبکه‌ها، فوتر، کد سرچ‌کنسول، اینماد، مرچنت زرین‌پال، کلید پیامک |
| بخش‌های صفحه اصلی | ترتیب، روشن/خاموش، تیتر و زیرتیتر هر بخش + بخش سفارشی با متن آزاد |
| خط زمان کاشان | رویدادها، رنگ نقطه |
| صفحات | درباره ما، قوانین، حریم خصوصی و هر صفحه‌ی جدید |
| منو | آیتم‌ها و ترتیب |
| دوره‌ها | همه‌چیز؛ فصل و درس به‌صورت inline، متن با ویرایشگر فارسی، ویدیو از سه منبع. مطالعه‌ی دوره‌ها آزاد و بدون ثبت‌نام است |
| آزمون‌ها | هر دوره یک آزمون؛ سؤال و گزینه، حد نصاب، مهلت، تعداد سؤال هر نوبت (بانک سؤال تصادفی)، تعداد نوبت. نوبت‌ها و **گواهینامه‌ها** (با شماره، کد استعلام و ابطال) |
| محصولات | شرح کامل، قابلیت‌ها، گالری، آموزش‌ها، کاتالوگ PDF یا خودکار، دوره‌های مرتبط |
| کاربران و نقش‌ها | گروه‌ها: مدیر محتوا، مدرس، پشتیبانی (برای ورود به پنل `is_staff` را روشن کنید) |
| سئو | title/description هر مسیر، noindex، JSON-LD، ریدایرکت‌ها |
| آمار | بازدیدها + داشبورد |

وقتی مدیر وارد سایت است، کنار هر بخش دکمه‌ی زرد **«ویرایش»** ظاهر می‌شود (با هاور).

## به‌روزرسانی محتوای دوره‌ها

متن دوره‌ها در `apps/academy/seed/courses/*.py` و آزمون‌ها در `apps/academy/seed/quizzes/*.py` است. بعد از هر تغییر:

```powershell
python manage.py seed_courses --overwrite
python manage.py seed_quizzes --overwrite
```

`--overwrite` فصل‌ها و درس‌های همان دوره را از نو می‌سازد (ثبت‌نام‌ها و گواهینامه‌ها دست نمی‌خورند). محتوایی که از پنل ویرایش کرده‌اید با این دستور جایگزین می‌شود؛ اگر دوره‌ای را از پنل شخصی‌سازی کرده‌اید، فایل seed آن را هم به‌روز کنید.

## لوگو

لوگوی رسمی در `static/img/logo.svg` است و تا وقتی در تنظیمات سایت لوگویی آپلود نشده، در منو، فوتر، گواهینامه و کاتالوگ به‌طور خودکار استفاده می‌شود (رنگ از `--sabz` می‌آید و با هاور می‌چرخد). آپلود لوگو در پنل آن را جایگزین می‌کند.

## انتقال به گیت‌هاب

```powershell
git init
git add .
git commit -m "ICSD Django site"
git branch -M main
git remote add origin https://github.com/USER/icsd-django.git
git push -u origin main
```

`.env`، `db.sqlite3`، `media/` و `static/vendor/` در `.gitignore` هستند — روی سرور دوباره ساخته می‌شوند.

## استقرار روی سرور (اوبونتو)

```bash
sudo apt install python3-venv python3-pip nginx postgresql nodejs npm
git clone https://github.com/USER/icsd-django.git /srv/icsd
cd /srv/icsd
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
npm install
node vendor.mjs
cp .env.example .env      # DEBUG=False، SECRET_KEY، ALLOWED_HOSTS، POSTGRES_*، CSRF_TRUSTED_ORIGINS
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py seed_site
python manage.py seed_geo
python manage.py seed_courses
python manage.py seed_quizzes
python manage.py setup_roles
python manage.py createsuperuser
gunicorn config.wsgi -b 127.0.0.1:8001 -w 3
```

nginx: `location /media/ { alias /srv/icsd/media/; }` و بقیه به `127.0.0.1:8001` پراکسی شود. استاتیک را WhiteNoise سرو می‌کند.

## بعد از انتقال دامنه

۱. در تنظیمات سایت، **آدرس سایت** را به دامنه‌ی واقعی تغییر دهید (sitemap و لینک‌های مطلق از همین می‌خوانند).
۲. `sitemap.xml` را در سرچ‌کنسول ثبت کنید.
۳. ریدایرکت‌های وردپرس با `seed_site` ساخته شده‌اند؛ در پنل ← سئو ← ریدایرکت‌ها قابل ویرایش‌اند.

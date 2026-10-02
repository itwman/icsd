# -*- coding: utf-8 -*-
# دوره‌ی جامع جنگو (Django 5.x / Python 3.12) — ۸ فصل، ۴۰ درس. متن‌ها r""" هستند تا بک‌اسلش‌های کد (\d، \n، مسیرهای ویندوز) دست‌نخورده بمانند.

COURSE = {
    "slug": "django",
    "title": "آموزش جامع جنگو (Django)",
    "category": "برنامه‌نویسی",
    "level": "intermediate",
    "summary": "از معماری MTV و Custom User تا ORM حرفه‌ای، فرم فارسی، ادمین، DRF، Celery و استقرار واقعی روی اوبونتو — با یک پروژه‌ی کامل ثبت سفارش فرش.",
    "description": (
        "<p>بیشتر آموزش‌های جنگو در همان «وبلاگ ساده» متوقف می‌شوند: یک مدل Post، یک ListView و تمام. اما در پروژه‌ی واقعی "
        "با مسئله‌هایی روبه‌رو می‌شوید که هیچ‌کدام از آن آموزش‌ها نگفته‌اند: صفحه‌ای که با ۲۰۰ کوئری باز می‌شود، کاربری که "
        "باید با موبایل وارد شود، ارقام فارسی که فرم را خراب می‌کنند، ۴۰۳ مرموز CSRF پشت nginx، و استاتیک‌هایی که با "
        "DEBUG=False ناپدید می‌شوند. این دوره برای برنامه‌نویسی نوشته شده که می‌خواهد جنگو را «درست» یاد بگیرد.</p>"
        "<p>از معماری MTV و چرخه‌ی درخواست شروع می‌کنیم، از روز اول <strong>Custom User</strong> با موبایل می‌سازیم، "
        "بعد به عمق <strong>ORM</strong> می‌رویم (N+1، Subquery، تراکنش و قفل)، View و Template و فیلتر تاریخ شمسی، "
        "فرم‌های فارسی و formset، ادمین حرفه‌ای، مجوزها و ورود با <strong>OTP پیامکی</strong>، "
        "<strong>Django REST Framework</strong>، کش با Redis، کارهای پس‌زمینه با <strong>Celery</strong>، تست با pytest "
        "و در پایان استقرار کامل روی اوبونتو با PostgreSQL، gunicorn، nginx و HTTPS. پروژه‌ی پایانی یک سامانه‌ی ثبت "
        "سفارش فرش است که همه‌ی این‌ها را کنار هم می‌گذارد.</p>"
        "<p>پیش‌نیاز: دوره‌ی مبانی پایتون (تابع، کلاس، ماژول، virtualenv). همه‌ی مثال‌ها برای Django 5.x و Python 3.12 "
        "نوشته شده‌اند و دستورهای ویندوز به‌صورت PowerShell آمده‌اند. هر درس با بخش «نکته‌هایی که کمتر کسی می‌داند» "
        "تمام می‌شود: دام‌ها و ترفندهایی که معمولاً فقط بعد از چند پروژه‌ی واقعی و چند شب بی‌خوابی یاد گرفته می‌شوند.</p>"
    ),
    "price": 0,
    "duration_minutes": 873,
    "tags": ["جنگو", "پایتون", "توسعه وب", "Django", "DRF", "ORM"],
    "modules": [
        # ───────────────────────────── فصل ۱ ─────────────────────────────
        {
            "title": "فصل ۱: شروع درست — معماری، ساختار پروژه و Custom User",
            "lessons": [
                {
                    "title": "جنگو چیست؛ معماری MTV و چرخه‌ی درخواست/پاسخ",
                    "kind": "text",
                    "minutes": 16,
                    "is_preview": True,
                    "body": r"""<h2>جنگو دقیقاً چه کاری برای ما می‌کند؟</h2>
<p>جنگو یک فریمورک وب «باتری‌دار» پایتون است: ORM برای کار با پایگاه داده، سیستم مسیریابی URL، موتور قالب، فرم و اعتبارسنجی، احراز هویت، پنل ادمین آماده، migration، کش، ارسال ایمیل و ده‌ها محافظ امنیتی پیش‌فرض (CSRF، XSS، SQL Injection، Clickjacking) همه در خود فریمورک هستند. به همین دلیل یک تیم کوچک می‌تواند در چند هفته سامانه‌ای بسازد که با فریمورک‌های مینیمال چند ماه طول می‌کشد. اینستاگرام، Disqus و بسیاری از سامانه‌های اداری و فروشگاهی ایرانی روی جنگو ساخته شده‌اند.</p>
<h3>MTV در برابر MVC</h3>
<p>جنگو اسم لایه‌ها را کمی متفاوت گذاشته است و همین برای تازه‌کارها گیج‌کننده است:</p>
<table><thead><tr><th>جنگو (MTV)</th><th>معادل در MVC</th><th>مسئولیت</th></tr></thead><tbody>
<tr><td>Model</td><td>Model</td><td>ساختار داده و منطق کسب‌وکار؛ هر کلاس یک جدول</td></tr>
<tr><td>Template</td><td>View</td><td>نمایش؛ HTML با زبان قالب جنگو</td></tr>
<tr><td>View</td><td>Controller</td><td>گرفتن درخواست، خواندن/نوشتن داده، انتخاب پاسخ</td></tr>
<tr><td>URLconf</td><td>Router</td><td>نگاشت آدرس به View</td></tr>
</tbody></table>
<h3>سفر یک درخواست</h3>
<p>وقتی کاربر آدرس <code>/orders/42/</code> را باز می‌کند، این اتفاق‌ها به ترتیب می‌افتد:</p>
<ol>
<li>وب‌سرور (nginx) درخواست را به سرور برنامه (gunicorn برای WSGI یا uvicorn برای ASGI) می‌دهد.</li>
<li>جنگو یک شیء <code>HttpRequest</code> می‌سازد و آن را از لایه‌های <strong>Middleware</strong> به ترتیب تعریف‌شده در settings عبور می‌دهد (Session، Authentication، CSRF و…).</li>
<li><strong>URL Resolver</strong> فهرست urlpatterns را از بالا به پایین می‌گردد و اولین الگوی منطبق را پیدا می‌کند.</li>
<li>View اجرا می‌شود؛ معمولاً از ORM داده می‌خواند و با یک Template پاسخ HTML می‌سازد.</li>
<li><code>HttpResponse</code> دوباره از Middlewareها — این بار به ترتیب <em>برعکس</em> — برمی‌گردد و به کاربر فرستاده می‌شود.</li>
</ol>
<pre><code class="language-python"># apps/orders/views.py
from django.shortcuts import get_object_or_404, render
from .models import Order

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)          # Model
    return render(request, "orders/detail.html",      # Template
                  {"order": order})                   # View = هماهنگ‌کننده

# apps/orders/urls.py
from django.urls import path
from . import views

app_name = "orders"
urlpatterns = [
    path("&lt;int:pk&gt;/", views.order_detail, name="detail"),
]</code></pre>
<h3>کدام نسخه؟</h3>
<p>در این دوره Django 5.x را هدف گرفته‌ایم و برای پروژه‌ی تازه نسخه‌ی <strong>5.2 LTS</strong> را پیشنهاد می‌کنیم؛ نسخه‌های LTS حدود سه سال وصله‌ی امنیتی می‌گیرند. Django 5.x به Python 3.10 به بالا نیاز دارد و ما با Python 3.12 کار می‌کنیم.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>داخل هر View می‌توانید <code>request.resolver_match</code> را بخوانید؛ نام url، namespace و آرگومان‌های گرفته‌شده را دارد و برای لاگ و منوی فعال عالی است.</li>
<li>ترتیب MIDDLEWARE مهم است: <code>SecurityMiddleware</code> باید اول باشد و <code>AuthenticationMiddleware</code> حتماً بعد از <code>SessionMiddleware</code>، چون کاربر را از Session می‌خواند.</li>
<li>اگر یک Middleware در مرحله‌ی درخواست خودش پاسخ برگرداند (مثلاً صفحه‌ی تعمیرات)، View و Middlewareهای بعدی اصلاً اجرا نمی‌شوند.</li>
<li><code>python -m django --version</code> نسخه‌ی دقیق نصب‌شده در همان venv فعال را نشان می‌دهد؛ اولین قدم در عیب‌یابی خطاهای «این ویژگی وجود ندارد».</li>
<li>جنگو هم WSGI و هم ASGI را پشتیبانی می‌کند؛ فایل‌های <code>wsgi.py</code> و <code>asgi.py</code> هر دو در پروژه ساخته می‌شوند و View همگام شما در هر دو کار می‌کند.</li>
</ul>""",
                },
                {
                    "title": "نصب در venv و ساخت پروژه با ساختار config/ و apps/",
                    "kind": "text",
                    "minutes": 18,
                    "is_preview": False,
                    "body": r"""<h2>یک شروع تمیز که بعداً پشیمان نشوید</h2>
<p>ساختار پیش‌فرض <code>startproject</code> پوشه‌ی تنظیمات را هم‌نام پروژه می‌سازد (<code>mysite/mysite/settings.py</code>) و اپ‌ها را کنار آن پراکنده می‌کند. در پروژه‌های واقعی دو قرارداد ساده خیلی کمک می‌کند: پوشه‌ی تنظیمات را <strong>config</strong> بنامید و همه‌ی اپ‌ها را داخل پوشه‌ی <strong>apps</strong> بگذارید.</p>
<h3>ساخت محیط مجازی روی ویندوز (PowerShell)</h3>
<pre><code class="language-powershell">mkdir carpet-orders
cd carpet-orders
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install "django&gt;=5.2,&lt;6.0" python-dotenv
django-admin startproject config .
mkdir apps
New-Item apps\__init__.py -ItemType File
mkdir apps\orders
python manage.py startapp orders apps\orders</code></pre>
<p>نقطه‌ی آخر <code>startproject config .</code> یعنی «همین پوشه»؛ بدون آن یک لایه پوشه‌ی اضافه ساخته می‌شود. روی لینوکس به‌جای Activate.ps1 از <code>source .venv/bin/activate</code> استفاده کنید.</p>
<h3>ساختار نهایی</h3>
<pre><code class="language-text">carpet-orders/
├── .venv/
├── .env                 # رمزها؛ هرگز در git نه
├── manage.py
├── requirements.txt
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── apps/
│   ├── accounts/        # Custom User
│   ├── catalog/         # طرح‌های فرش
│   └── orders/
├── templates/
└── static/</code></pre>
<h3>یک اصلاح ضروری در apps.py</h3>
<p>وقتی اپ داخل پوشه‌ی apps است، مسیر پایتونی آن <code>apps.orders</code> است؛ پس باید <code>name</code> را در <code>apps.py</code> اصلاح و همان را در INSTALLED_APPS ثبت کنید:</p>
<pre><code class="language-python"># apps/orders/apps.py
from django.apps import AppConfig

class OrdersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.orders"          # مسیر ایمپورت
    verbose_name = "سفارش‌ها"     # عنوان فارسی در ادمین

# config/settings.py
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "apps.accounts",
    "apps.catalog",
    "apps.orders",
]</code></pre>
<p>برچسب اپ (app label) همچنان <code>orders</code> است؛ یعنی در migrationها، <code>"orders.Order"</code> و مجوزها همان نام کوتاه به کار می‌رود.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>اگر PowerShell با خطای «running scripts is disabled» جلوی Activate.ps1 را گرفت، یک بار <code>Set-ExecutionPolicy -Scope CurrentUser RemoteSigned</code> را اجرا کنید؛ نیازی به دسترسی ادمین نیست.</li>
<li><code>py -0</code> فهرست همه‌ی نسخه‌های پایتون نصب‌شده روی ویندوز را نشان می‌دهد؛ با <code>py -3.12</code> دقیقاً همان نسخه را برای venv انتخاب کنید.</li>
<li>بعد از فعال‌سازی venv همیشه <code>python -m pip</code> بنویسید نه فقط <code>pip</code>؛ این‌طور مطمئنید pip همان پایتون venv را نصب می‌کند.</li>
<li>در ایران اگر pip کند است یا خطای 403 می‌دهد، می‌توانید با <code>pip config set global.index-url</code> یک میرور داخلی PyPI را برای همیشه تنظیم کنید؛ دیگر لازم نیست هر بار <code>-i</code> بنویسید.</li>
<li><code>startapp</code> پوشه‌ی مقصد را نمی‌سازد؛ اگر <code>apps\orders</code> وجود نداشته باشد خطای «Destination directory does not exist» می‌گیرید.</li>
</ul>""",
                },
                {
                    "title": "settings حرفه‌ای: .env، DEBUG، ALLOWED_HOSTS، زبان فارسی و منطقه‌ی زمانی",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>تنظیماتی که نباید در کد باشد</h2>
<p>فایل <code>settings.py</code> در git می‌رود؛ پس <strong>SECRET_KEY</strong>، رمز پایگاه داده و کلید API پیامک نباید در آن نوشته شوند. قاعده‌ی ساده: هرچه بین لوکال و سرور فرق می‌کند یا محرمانه است، از متغیر محیطی خوانده شود. ساده‌ترین راه، فایل <code>.env</code> و کتابخانه‌ی <code>python-dotenv</code> است.</p>
<pre><code class="language-ini"># .env  (در .gitignore)
DJANGO_SECRET_KEY=change-me-to-a-long-random-string
DJANGO_DEBUG=1
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
DB_NAME=carpet
DB_PASSWORD=
SMS_API_KEY=</code></pre>
<pre><code class="language-python"># config/settings.py
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

def env_bool(name, default="0"):
    return os.getenv(name, default).strip().lower() in {"1", "true", "yes", "on"}

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]      # نبودش = خطای فوری، نه کلید پیش‌فرض ناامن
DEBUG = env_bool("DJANGO_DEBUG")
ALLOWED_HOSTS = [h.strip() for h in os.getenv("DJANGO_ALLOWED_HOSTS", "").split(",") if h.strip()]

LANGUAGE_CODE = "fa"
TIME_ZONE = "Asia/Tehran"
USE_I18N = True
USE_TZ = True

AUTH_USER_MODEL = "accounts.User"   # درس ۵</code></pre>
<p>برای ساختن یک کلید تصادفی امن:</p>
<pre><code class="language-powershell">python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"</code></pre>
<h3>معنای چند تنظیم کلیدی</h3>
<table><thead><tr><th>تنظیم</th><th>کار</th><th>مقدار درست در سرور</th></tr></thead><tbody>
<tr><td>DEBUG</td><td>صفحه‌ی خطای کامل با متغیرها و تنظیمات؛ سرو خودکار static</td><td>همیشه False</td></tr>
<tr><td>ALLOWED_HOSTS</td><td>دامنه‌هایی که هدر Host آن‌ها پذیرفته می‌شود</td><td><code>["example.ir", "www.example.ir"]</code></td></tr>
<tr><td>LANGUAGE_CODE</td><td>زبان پیام‌های جنگو، ادمین و راست‌به‌چپ بودن آن</td><td><code>"fa"</code></td></tr>
<tr><td>TIME_ZONE</td><td>منطقه‌ی زمانی نمایش و ورودی فرم‌ها</td><td><code>"Asia/Tehran"</code></td></tr>
<tr><td>USE_TZ</td><td>ذخیره‌ی زمان‌ها به UTC و aware بودن datetimeها</td><td>True</td></tr>
</tbody></table>
<h3>USE_TZ را خاموش نکنید</h3>
<p>با <code>USE_TZ = True</code> جنگو همه‌ی زمان‌ها را در پایگاه داده به UTC ذخیره می‌کند و هنگام نمایش به وقت تهران برمی‌گرداند. برای «الان» همیشه <code>django.utils.timezone.now()</code> را به کار ببرید، نه <code>datetime.now()</code>؛ دومی زمان naive می‌دهد و هشدار «received a naive datetime» تولید می‌کند. برای «امروزِ تهران» هم <code>timezone.localdate()</code> درست است، نه <code>date.today()</code> که به ساعت سرور وابسته است.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>bool(os.getenv("DJANGO_DEBUG"))</code> برای رشته‌ی <code>"False"</code> هم True می‌دهد؛ هر رشته‌ی غیرخالی True است. همیشه مثل تابع <code>env_bool</code> بالا مقایسه کنید.</li>
<li>ایران از سال ۱۴۰۱ ساعت تابستانی ندارد. اگر روی ویندوز ساعت‌ها یک ساعت جابه‌جاست، بسته‌ی <code>tzdata</code> را در venv نصب یا به‌روز کنید؛ پایتون روی ویندوز پایگاه منطقه‌ی زمانی سیستمی ندارد.</li>
<li>برای عوض کردن SECRET_KEY بدون خارج شدن همه‌ی کاربران، کلید قدیمی را در <code>SECRET_KEY_FALLBACKS</code> بگذارید و بعد از چند هفته حذفش کنید.</li>
<li>با <code>python manage.py diffsettings</code> فقط تنظیماتی را می‌بینید که با پیش‌فرض جنگو فرق دارند؛ بهترین راه برای فهمیدن این‌که پروژه‌ی تحویل‌گرفته چه چیزی را عوض کرده است.</li>
<li>وقتی DEBUG=True و ALLOWED_HOSTS خالی است، جنگو خودش localhost و 127.0.0.1 را مجاز می‌داند؛ به همین دلیل خطای DisallowedHost معمولاً اولین بار روی سرور دیده می‌شود.</li>
</ul>""",
                },
                {
                    "title": "manage.py و دستورات مهم؛ ساخت دستور مدیریتی اختصاصی",
                    "kind": "text",
                    "minutes": 17,
                    "is_preview": False,
                    "body": r"""<h2>manage.py؛ کنترل پنل خط فرمان پروژه</h2>
<p><code>manage.py</code> همان <code>django-admin</code> است که از قبل <code>DJANGO_SETTINGS_MODULE</code> را روی تنظیمات پروژه‌ی شما گذاشته. هر کاری که «یک بار» یا «زمان‌بندی‌شده» انجام می‌شود — ساخت ادمین، پاک‌سازی داده، ورود اکسل — جایش یک دستور مدیریتی است، نه یک View مخفی.</p>
<h3>دستورهایی که هر روز لازم دارید</h3>
<table><thead><tr><th>دستور</th><th>کاربرد</th></tr></thead><tbody>
<tr><td><code>runserver 0.0.0.0:8000</code></td><td>سرور توسعه؛ با 0.0.0.0 از گوشی در همان شبکه هم باز می‌شود</td></tr>
<tr><td><code>makemigrations</code> / <code>migrate</code></td><td>ساخت و اجرای migration (فصل ۲)</td></tr>
<tr><td><code>createsuperuser</code></td><td>ساخت کاربر مدیر</td></tr>
<tr><td><code>shell</code></td><td>پایتون تعاملی با تنظیمات پروژه</td></tr>
<tr><td><code>dbshell</code></td><td>کلاینت خط فرمان همان پایگاه داده (psql، sqlite3)</td></tr>
<tr><td><code>check</code> / <code>check --deploy</code></td><td>بررسی خطاهای پیکربندی و امنیتی</td></tr>
<tr><td><code>dumpdata</code> / <code>loaddata</code></td><td>خروجی و ورودی JSON داده‌ها</td></tr>
<tr><td><code>collectstatic</code></td><td>جمع‌کردن فایل‌های static برای سرور</td></tr>
<tr><td><code>changepassword 09121234567</code></td><td>عوض کردن رمز یک کاربر</td></tr>
<tr><td><code>sendtestemail you@example.ir</code></td><td>آزمون سریع تنظیمات ایمیل</td></tr>
</tbody></table>
<h3>یک دستور اختصاصی: لغو سفارش‌های رهاشده</h3>
<p>فایل باید در مسیر <code>apps/orders/management/commands/</code> باشد (هر دو پوشه با <code>__init__.py</code>) و نام فایل، نام دستور می‌شود:</p>
<pre><code class="language-python"># apps/orders/management/commands/cancel_stale_orders.py
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from apps.orders.models import Order


class Command(BaseCommand):
    help = "سفارش‌های پرداخت‌نشده‌ی قدیمی‌تر از N روز را لغو می‌کند"

    def add_arguments(self, parser):
        parser.add_argument("--days", type=int, default=3)
        parser.add_argument("--dry-run", action="store_true")

    def handle(self, *args, **opts):
        limit = timezone.now() - timedelta(days=opts["days"])
        qs = Order.objects.filter(status="pending", created_at__lt=limit)
        count = qs.count()
        if opts["dry_run"]:
            self.stdout.write(f"{count} سفارش لغو خواهد شد (آزمایشی).")
            return
        qs.update(status="cancelled")
        self.stdout.write(self.style.SUCCESS(f"{count} سفارش لغو شد."))</code></pre>
<pre><code class="language-powershell">python manage.py cancel_stale_orders --days 5 --dry-run
python manage.py cancel_stale_orders --days 5</code></pre>
<p>روی سرور همین دستور را با cron یا systemd timer زمان‌بندی می‌کنید؛ در کد هم با <code>django.core.management.call_command("cancel_stale_orders", days=5)</code> قابل صدا زدن است (مثلاً داخل تست).</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>در Django 5.2 دستور <code>shell</code> همه‌ی مدل‌های اپ‌های نصب‌شده را خودکار import می‌کند؛ دیگر لازم نیست هر بار <code>from apps.orders.models import Order</code> بنویسید.</li>
<li><code>python manage.py shell -c "..."</code> یک خط کد را بدون ورود به محیط تعاملی اجرا می‌کند؛ برای اسکریپت‌های سریع روی سرور عالی است.</li>
<li>در PowerShell خروجی <code>dumpdata &gt; data.json</code> را با UTF-16 می‌نویسد و loaddata بعداً خطا می‌دهد؛ به‌جایش از گزینه‌ی <code>-o data.json</code> خود دستور استفاده کنید.</li>
<li>برای dumpdata قابل‌انتقال از <code>--natural-foreign -e contenttypes -e auth.permission</code> استفاده کنید؛ وگرنه روی پایگاه داده‌ی تازه به خطای تکراری بودن کلید برمی‌خورید.</li>
<li>نام گزینه‌ی <code>--dry-run</code> در <code>opts</code> با زیرخط (<code>dry_run</code>) می‌آید؛ این رفتار argparse است و منشأ یک KeyError رایج.</li>
</ul>""",
                },
                {
                    "title": "Custom User از روز اول: ورود با شماره‌ی موبایل",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>مهم‌ترین تصمیم قبل از اولین migrate</h2>
<p>مستندات رسمی جنگو صریحاً توصیه می‌کند در هر پروژه‌ی تازه، حتی اگر فعلاً به فیلد اضافه‌ای نیاز ندارید، یک مدل کاربر اختصاصی بسازید. دلیلش ساده است: وقتی چند جدول با ForeignKey به <code>auth.User</code> اشاره کردند و داده‌ی واقعی وارد شد، عوض کردن مدل کاربر یکی از دردناک‌ترین مهاجرت‌هاست. در ایران هم تقریباً همه‌ی سامانه‌ها ورود با موبایل می‌خواهند؛ پس از همان روز اول <code>mobile</code> را شناسه‌ی کاربر می‌کنیم.</p>
<h3>AbstractUser یا AbstractBaseUser؟</h3>
<table><thead><tr><th>پایه</th><th>چه می‌دهد</th><th>کِی</th></tr></thead><tbody>
<tr><td>AbstractUser</td><td>همه‌ی فیلدهای User استاندارد (نام، ایمیل، is_staff، گروه‌ها)</td><td>بیشتر پروژه‌ها؛ فقط شناسه را عوض می‌کنیم</td></tr>
<tr><td>AbstractBaseUser + PermissionsMixin</td><td>فقط رمز و last_login؛ بقیه را خودتان تعریف می‌کنید</td><td>وقتی ساختار کاملاً متفاوت می‌خواهید</td></tr>
</tbody></table>
<h3>پیاده‌سازی با AbstractUser</h3>
<pre><code class="language-python"># apps/accounts/models.py
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models

mobile_validator = RegexValidator(r"^09\d{9}$", "شماره‌ی موبایل باید ۱۱ رقم و با 09 شروع شود.")


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, mobile, password, **extra):
        if not mobile:
            raise ValueError("شماره‌ی موبایل الزامی است.")
        user = self.model(mobile=mobile, **extra)
        user.set_password(password)      # password=None یعنی رمز غیرقابل‌استفاده (ورود فقط با OTP)
        user.save(using=self._db)
        return user

    def create_user(self, mobile, password=None, **extra):
        extra.setdefault("is_staff", False)
        extra.setdefault("is_superuser", False)
        return self._create_user(mobile, password, **extra)

    def create_superuser(self, mobile, password, **extra):
        extra.update(is_staff=True, is_superuser=True)
        return self._create_user(mobile, password, **extra)


class User(AbstractUser):
    username = None                      # فیلد username حذف می‌شود
    mobile = models.CharField("موبایل", max_length=11, unique=True, validators=[mobile_validator])

    USERNAME_FIELD = "mobile"
    REQUIRED_FIELDS = []                 # createsuperuser جز موبایل و رمز چیزی نمی‌پرسد

    objects = UserManager()

    def __str__(self):
        return self.get_full_name() or self.mobile</code></pre>
<p>در settings: <code>AUTH_USER_MODEL = "accounts.User"</code>، سپس <code>makemigrations accounts</code> و بعد <code>migrate</code>. ترتیب مهم است: این باید <em>قبل از اولین migrate</em> پروژه انجام شود.</p>
<h3>ارجاع درست به مدل کاربر</h3>
<pre><code class="language-python"># در models.py: رشته از settings
from django.conf import settings
owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

# در view، فرم و سرویس: خود کلاس
from django.contrib.auth import get_user_model
User = get_user_model()</code></pre>
<p>برای ادمین هم باید از <code>UserAdmin</code> ارث ببرید و <code>ordering</code>، <code>fieldsets</code> و <code>add_fieldsets</code> را بازنویسی کنید، چون نسخه‌ی پیش‌فرض آن‌ها به <code>username</code> اشاره می‌کند و ادمین با خطای «unknown field» بالا نمی‌آید.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>username = None</code> در زیرکلاس AbstractUser فیلد را واقعاً از مدل حذف می‌کند؛ ترفندی کوتاه که نیاز به نوشتن کل مدل از صفر را برطرف می‌کند.</li>
<li><code>set_password(None)</code> رمز «غیرقابل‌استفاده» ثبت می‌کند و <code>has_usable_password()</code> برایش False است؛ مناسب کاربرانی که فقط با پیامک وارد می‌شوند.</li>
<li>موبایل را قبل از ذخیره نرمال کنید (ارقام فارسی، +98، فاصله)؛ وگرنه «۰۹۱۲…» و «0912…» دو کاربر جدا می‌شوند و unique هم جلویش را نمی‌گیرد.</li>
<li>در فایل models هرگز <code>get_user_model()</code> را در سطح ماژول صدا نزنید؛ ممکن است قبل از بارگذاری اپ‌ها اجرا شود. در ForeignKey همیشه <code>settings.AUTH_USER_MODEL</code>.</li>
<li>اگر پروژه قبلاً با auth.User migrate شده و هنوز داده‌ی مهمی ندارد، ساده‌ترین راه پاک کردن پایگاه داده و migrationها و شروع دوباره است؛ مهاجرت درجا ممکن است اما چند مرحله‌ی دستی و پرخطر دارد.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۲ ─────────────────────────────
        {
            "title": "فصل ۲: مدل‌ها و ORM — طراحی داده‌ی درست",
            "lessons": [
                {
                    "title": "فیلدها و گزینه‌ها: null در برابر blank، TextChoices، unique و db_index",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>مدل، قرارداد شما با پایگاه داده است</h2>
<p>هر کلاس مدل یک جدول و هر فیلد یک ستون است. انتخاب نوع فیلد و گزینه‌هایش فقط سلیقه نیست: روی درستی داده، سرعت کوئری و اعتبارسنجی فرم‌ها و ادمین اثر مستقیم دارد. مدل طرح فرش یک کارخانه‌ی کاشانی را ببینید:</p>
<pre><code class="language-python"># apps/catalog/models.py
from django.db import models
from django.db.models.functions import Now


class Carpet(models.Model):
    class Density(models.IntegerChoices):
        D700 = 700, "۷۰۰ شانه"
        D1000 = 1000, "۱۰۰۰ شانه"
        D1200 = 1200, "۱۲۰۰ شانه"

    class Status(models.TextChoices):
        DRAFT = "draft", "پیش‌نویس"
        ACTIVE = "active", "فعال"
        ARCHIVED = "archived", "بایگانی"

    code = models.CharField("کد طرح", max_length=20, unique=True)
    name = models.CharField("نام طرح", max_length=100, db_index=True)
    density = models.PositiveSmallIntegerField("تراکم", choices=Density)
    status = models.CharField("وضعیت", max_length=10, choices=Status, default=Status.DRAFT)
    price = models.PositiveBigIntegerField("قیمت هر متر (ریال)")
    stock = models.PositiveIntegerField("موجودی", default=0)
    weight_kg = models.DecimalField("وزن", max_digits=6, decimal_places=2, null=True, blank=True)
    description = models.TextField("توضیحات", blank=True)
    created_at = models.DateTimeField(db_default=Now())
    updated_at = models.DateTimeField(auto_now=True)</code></pre>
<p>از Django 5.0 می‌توانید خود کلاس TextChoices را مستقیم به <code>choices</code> بدهید و دیگر لازم نیست <code>.choices</code> بنویسید. <code>db_default</code> هم (باز از 5.0) مقدار پیش‌فرض را در خود پایگاه داده تعریف می‌کند؛ حتی INSERTهای خارج از جنگو هم آن را می‌گیرند.</p>
<h3>null در برابر blank</h3>
<table><thead><tr><th>گزینه</th><th>سطح</th><th>معنی</th></tr></thead><tbody>
<tr><td><code>null=True</code></td><td>پایگاه داده</td><td>ستون می‌تواند NULL باشد</td></tr>
<tr><td><code>blank=True</code></td><td>اعتبارسنجی (فرم/ادمین)</td><td>فیلد در فرم می‌تواند خالی بماند</td></tr>
</tbody></table>
<p>قاعده‌ی عملی: برای فیلدهای متنی (CharField، TextField) فقط <code>blank=True</code> بگذارید و «خالی» را با رشته‌ی خالی نشان دهید. برای عدد، تاریخ و ForeignKey اختیاری، هر دو را با هم بگذارید؛ چون عدد «خالی» معنایی جز NULL ندارد.</p>
<h3>پول را چطور ذخیره کنیم؟</h3>
<p>هرگز با <code>FloatField</code>. ریال را به‌صورت عدد صحیح (<code>PositiveBigIntegerField</code>) نگه دارید و تبدیل به تومان را فقط در نمایش انجام دهید. اگر اعشار واقعی دارید (نرخ ارز، وزن) از <code>DecimalField</code> استفاده کنید.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>CharField با <code>null=True</code> دو نوع «خالی» می‌سازد (NULL و رشته‌ی خالی) و کوئری‌ها را پیچیده می‌کند؛ تنها استثنا وقتی است که <code>unique=True</code> دارید و چند رکورد خالی مجاز است.</li>
<li><code>unique=True</code> خودش ایندکس می‌سازد؛ اضافه کردن <code>db_index=True</code> کنارش فقط یک ایندکس تکراری بی‌فایده است.</li>
<li>برای هر فیلد choices، متد <code>get_status_display()</code> خودکار ساخته می‌شود و برچسب فارسی را برمی‌گرداند؛ در قالب بدون پرانتز: <code>{{ carpet.get_status_display }}</code>.</li>
<li><code>auto_now</code> فقط در <code>save()</code> به‌روز می‌شود؛ <code>QuerySet.update()</code> آن را دست نمی‌زند و باید خودتان <code>updated_at=timezone.now()</code> را بفرستید.</li>
<li><code>choices</code> فقط در اعتبارسنجی اعمال می‌شود، نه در پایگاه داده؛ برای ضمانت واقعی یک CheckConstraint اضافه کنید (درس ۸).</li>
</ul>""",
                },
                {
                    "title": "روابط: ForeignKey و on_delete، OneToOne، ManyToMany و through",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>داده‌ها تنها زندگی نمی‌کنند</h2>
<p>یک مشتری چند سفارش دارد (یک‌به‌چند)، هر کاربر یک پروفایل مشتری دارد (یک‌به‌یک) و هر سفارش چند طرح فرش با تعداد و قیمت مشخص دارد (چندبه‌چند با اطلاعات اضافه). جنگو برای هر کدام فیلد مخصوص دارد.</p>
<pre><code class="language-python"># apps/orders/models.py
from django.conf import settings
from django.db import models


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                related_name="customer")
    full_name = models.CharField("نام کامل", max_length=120)
    city = models.CharField("شهر", max_length=50, default="کاشان")


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name="orders")
    carpets = models.ManyToManyField("catalog.Carpet", through="OrderItem", related_name="orders")
    tracking_code = models.CharField(max_length=12, unique=True, blank=True)
    status = models.CharField(max_length=10, default="pending")
    total = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    carpet = models.ForeignKey("catalog.Carpet", on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField(default=1)
    unit_price = models.PositiveBigIntegerField()   # قیمت لحظه‌ی خرید؛ نه قیمت فعلی طرح</code></pre>
<h3>on_delete: وقتی والد حذف می‌شود</h3>
<table><thead><tr><th>گزینه</th><th>رفتار</th><th>مثال مناسب</th></tr></thead><tbody>
<tr><td>CASCADE</td><td>فرزندان هم حذف می‌شوند</td><td>اقلام یک سفارش</td></tr>
<tr><td>PROTECT</td><td>حذف والد با ProtectedError متوقف می‌شود</td><td>مشتری‌ای که سفارش دارد</td></tr>
<tr><td>RESTRICT</td><td>مثل PROTECT، اما اگر والد از مسیر CASCADE دیگری حذف شود اجازه می‌دهد</td><td>ساختارهای تودرتو</td></tr>
<tr><td>SET_NULL</td><td>ستون NULL می‌شود (نیاز به null=True)</td><td>نویسنده‌ی یک مقاله</td></tr>
<tr><td>SET_DEFAULT / SET(...)</td><td>مقدار پیش‌فرض یا حاصل یک تابع</td><td>انتقال به «کاربر حذف‌شده»</td></tr>
<tr><td>DO_NOTHING</td><td>جنگو کاری نمی‌کند؛ پایگاه داده تصمیم می‌گیرد</td><td>تقریباً هیچ‌وقت</td></tr>
</tbody></table>
<h3>کار با روابط</h3>
<pre><code class="language-python">customer = request.user.customer             # OneToOne معکوس
customer.orders.filter(status="pending")      # related_name
order.items.select_related("carpet")          # اقلام با طرح‌ها
order.carpets.add(carpet, through_defaults={"quantity": 2, "unit_price": carpet.price})
Order.objects.filter(customer__city="کاشان", items__carpet__density=1200).distinct()</code></pre>
<p>جدول واسط <code>OrderItem</code> دلیل مهمی دارد: قیمت فرش فردا عوض می‌شود، اما فاکتور دیروز نباید عوض شود. هر رابطه‌ی چندبه‌چندی که «اطلاعات خودش» را دارد باید through داشته باشد.</p>
<h3>OneToOne یا ForeignKey با unique؟</h3>
<p>از نظر پایگاه داده هر دو یک ستون یکتا می‌سازند، اما رفتار پایتونی فرق دارد: در OneToOne دسترسی معکوس (<code>user.customer</code>) یک شیء برمی‌گرداند و اگر وجود نداشته باشد استثنای <code>RelatedObjectDoesNotExist</code> می‌دهد؛ در ForeignKey یک Manager برمی‌گردد. برای «پروفایل» و «اطلاعات تکمیلی» همیشه OneToOne را انتخاب کنید و در View با <code>hasattr(request.user, "customer")</code> یا <code>getattr</code> نبودنش را مدیریت کنید، نه با try بی‌انتها.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>اشاره با رشته (<code>"catalog.Carpet"</code>) مشکل import حلقوی بین اپ‌ها را حل می‌کند؛ برای اشاره به خود مدل هم <code>"self"</code> بنویسید.</li>
<li><code>related_name="+"</code> رابطه‌ی معکوس را کاملاً غیرفعال می‌کند؛ برای فیلدهایی مثل <code>created_by</code> که هرگز از سمت کاربر پیمایش نمی‌شوند.</li>
<li>ForeignKey به‌صورت خودکار ایندکس دارد؛ ایندکس دستی روی آن لازم نیست مگر ایندکس ترکیبی بخواهید.</li>
<li>فیلتر روی رابطه‌ی چندتایی (<code>items__carpet__...</code>) ممکن است ردیف تکراری بدهد؛ <code>.distinct()</code> را فراموش نکنید.</li>
<li><code>limit_choices_to={"status": "active"}</code> روی ForeignKey، گزینه‌های فرم و ادمین را محدود می‌کند؛ بدون نوشتن حتی یک خط کد در فرم.</li>
</ul>""",
                },
                {
                    "title": "کلاس Meta: ordering، indexes، constraints و نام‌های فارسی",
                    "kind": "text",
                    "minutes": 18,
                    "is_preview": False,
                    "body": r"""<h2>Meta؛ جایی که مدل درباره‌ی خودش حرف می‌زند</h2>
<p>کلاس درونی <code>Meta</code> رفتار کلی مدل را تعیین می‌کند: نام فارسی در ادمین، ترتیب پیش‌فرض، ایندکس‌های ترکیبی و قیدهای پایگاه داده. قیدها (constraints) مهم‌ترین بخش‌اند؛ چون ضمانتی می‌دهند که هیچ باگی در کد پایتون نمی‌تواند دورش بزند.</p>
<pre><code class="language-python">from django.db import models
from django.db.models import Q


class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "در انتظار پرداخت"
        PAID = "paid", "پرداخت‌شده"
        SHIPPED = "shipped", "ارسال‌شده"
        CANCELLED = "cancelled", "لغوشده"

    customer = models.ForeignKey("orders.Customer", on_delete=models.PROTECT, related_name="orders")
    status = models.CharField(max_length=10, choices=Status, default=Status.PENDING)
    total = models.BigIntegerField(default=0)
    discount = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural = "سفارش‌ها"
        ordering = ["-created_at"]
        get_latest_by = "created_at"
        indexes = [
            models.Index(fields=["status", "-created_at"], name="order_status_created_idx"),
        ]
        constraints = [
            models.CheckConstraint(condition=Q(total__gte=0), name="order_total_gte_0"),
            models.CheckConstraint(condition=Q(discount__lte=models.F("total")),
                                   name="order_discount_lte_total",
                                   violation_error_message="تخفیف نمی‌تواند از مبلغ سفارش بیشتر باشد."),
            models.CheckConstraint(condition=Q(status__in=["pending", "paid", "shipped", "cancelled"]),
                                   name="order_status_valid"),
            # هر مشتری فقط یک سفارش «در انتظار» داشته باشد (سبد خرید باز)
            models.UniqueConstraint(fields=["customer"], condition=Q(status="pending"),
                                    name="one_pending_order_per_customer"),
        ]</code></pre>
<h3>ordering؛ راحت اما نه رایگان</h3>
<p><code>ordering</code> روی <em>همه‌ی</em> کوئری‌ها اعمال می‌شود، حتی جایی که ترتیب مهم نیست. روی جدول‌های بزرگ این یعنی مرتب‌سازی اضافه در هر کوئری. اگر ترتیب پیش‌فرض دارید، ایندکس متناسب با آن هم بسازید (مثل ایندکس بالا روی <code>-created_at</code>) یا ordering را حذف کنید و فقط در جای لازم <code>order_by()</code> بنویسید.</p>
<h3>ایندکس درست</h3>
<p>ایندکس ترکیبی <code>["status", "-created_at"]</code> دقیقاً برای کوئری‌ای مثل «سفارش‌های در انتظار، جدیدترین اول» ساخته شده است. ترتیب ستون‌ها مهم است: ایندکس از چپ استفاده می‌شود؛ پس کوئری فقط روی <code>created_at</code> از آن سود نمی‌برد.</p>
<h3>چرا قید، وقتی اعتبارسنجی فرم داریم؟</h3>
<p>فرم فقط یکی از درهای ورود داده است. API، دستور مدیریتی، اسکریپت واردکردن اکسل، <code>QuerySet.update()</code> و حتی یک همکار که مستقیم با psql کار می‌کند، همه فرم را دور می‌زنند. قید پایگاه داده آخرین خط دفاع است و هزینه‌ی تقریباً صفری دارد. قید <code>one_pending_order_per_customer</code> بالا مثلاً مشکل کلاسیک «دو سبد خرید هم‌زمان» را که از دو تب مرورگر ساخته می‌شود، بدون هیچ قفل و منطق پایتونی حل می‌کند.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>از Django 5.1 پارامتر CheckConstraint نامش <code>condition</code> است؛ <code>check</code> قدیمی منسوخ شده. اگر روی 5.0 هستید همان <code>check=</code> را بنویسید.</li>
<li>قیدها از Django 4.1 در <code>full_clean()</code> هم بررسی می‌شوند؛ یعنی ModelForm و ادمین پیام خطای <code>violation_error_message</code> را به‌جای IntegrityError نشان می‌دهند.</li>
<li>UniqueConstraint شرطی (با <code>condition</code>) روی PostgreSQL و SQLite کار می‌کند اما MySQL آن را نادیده می‌گیرد؛ اگر پایگاه داده‌تان MySQL است به این قید تکیه نکنید.</li>
<li>بدون <code>verbose_name_plural</code> ادمین جنگو فقط یک «s» لاتین به نام فارسی می‌چسباند و «سفارشs» می‌بینید.</li>
<li>نام ایندکس و قید حداکثر ۳۰ کاراکتر (برای سازگاری با Oracle) و در کل پروژه یکتاست؛ از الگوی <code>app_model_field_idx</code> استفاده کنید تا تداخل پیش نیاید.</li>
</ul>""",
                },
                {
                    "title": "Migrations حرفه‌ای: data migration، squash و حل تداخل",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>Migration؛ تاریخچه‌ی نسخه‌دار پایگاه داده</h2>
<p>هر بار مدل را تغییر می‌دهید، <code>makemigrations</code> یک فایل پایتونی می‌سازد که فقط «تفاوت» را توصیف می‌کند و <code>migrate</code> آن را روی پایگاه داده اجرا می‌کند. این فایل‌ها بخشی از کد پروژه‌اند و باید در git کامیت شوند؛ سرور هرگز نباید خودش makemigrations بزند.</p>
<table><thead><tr><th>دستور</th><th>کاربرد</th></tr></thead><tbody>
<tr><td><code>makemigrations orders</code></td><td>ساخت migration برای یک اپ</td></tr>
<tr><td><code>migrate</code></td><td>اجرای همه‌ی migrationهای اجرانشده</td></tr>
<tr><td><code>showmigrations orders</code></td><td>فهرست با علامت [X] برای اجراشده‌ها</td></tr>
<tr><td><code>sqlmigrate orders 0005</code></td><td>SQL دقیقی که اجرا خواهد شد</td></tr>
<tr><td><code>migrate orders 0004</code></td><td>برگشت به یک نقطه‌ی قبلی</td></tr>
<tr><td><code>migrate --plan</code></td><td>نمایش ترتیب اجرا بدون اجرا</td></tr>
<tr><td><code>makemigrations --merge</code></td><td>حل تداخل دو شاخه</td></tr>
<tr><td><code>squashmigrations orders 0001 0040</code></td><td>ادغام چند migration در یکی</td></tr>
</tbody></table>
<h3>Data migration با RunPython</h3>
<p>فرض کنید فیلد <code>tracking_code</code> را اضافه کرده‌اید و باید برای هزاران سفارش قدیمی مقدار بسازید. یک migration خالی بسازید و منطق را در آن بنویسید:</p>
<pre><code class="language-powershell">python manage.py makemigrations orders --empty --name fill_tracking_codes</code></pre>
<pre><code class="language-python">from django.db import migrations


def fill_codes(apps, schema_editor):
    Order = apps.get_model("orders", "Order")       # نسخه‌ی تاریخی مدل، نه import مستقیم
    batch = []
    for order in Order.objects.filter(tracking_code="").only("pk").iterator(chunk_size=2000):
        order.tracking_code = f"KSH{order.pk:07d}"
        batch.append(order)
        if len(batch) &gt;= 2000:
            Order.objects.bulk_update(batch, ["tracking_code"])
            batch.clear()
    Order.objects.bulk_update(batch, ["tracking_code"])


class Migration(migrations.Migration):
    dependencies = [("orders", "0006_order_tracking_code")]
    operations = [
        migrations.RunPython(fill_codes, migrations.RunPython.noop),
    ]</code></pre>
<p>آرگومان دوم (<code>noop</code>) اجازه می‌دهد migration برگشت‌پذیر بماند؛ بدون آن <code>migrate orders 0005</code> با خطای «irreversible» متوقف می‌شود.</p>
<h3>تداخل migration در کار تیمی</h3>
<p>اگر شما و همکارتان هر دو روی شاخه‌ی خودتان <code>0007_...</code> ساخته باشید، بعد از merge پیام «Conflicting migrations detected» می‌گیرید. راه‌حل: <code>python manage.py makemigrations --merge</code> که یک migration ادغام با دو وابستگی می‌سازد. اگر هر دو migration یک فیلد را تغییر داده‌اند، قبل از merge یکی را حذف و دوباره بسازید.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>در RunPython هرگز مدل را مستقیم import نکنید؛ مدل امروز ممکن است فیلدهایی داشته باشد که در آن نقطه از تاریخ هنوز وجود ندارند. همیشه <code>apps.get_model</code>.</li>
<li>متدهای سفارشی مدل و متد <code>save()</code> بازنویسی‌شده در مدل تاریخی وجود ندارند؛ فقط فیلدها و Managerهایی که <code>use_in_migrations = True</code> دارند.</li>
<li><code>makemigrations --check --dry-run</code> در CI اگر مدلی تغییر کرده اما migration ساخته نشده باشد با کد خطا خارج می‌شود؛ جلوی «فراموش کردم migration بسازم» را می‌گیرد.</li>
<li>افزودن فیلد NOT NULL به جدول بزرگ را سه‌مرحله‌ای انجام دهید: اول فیلد nullable، بعد data migration، بعد NOT NULL کردن؛ تا جدول مدت طولانی قفل نماند.</li>
<li>روی PostgreSQL هر migration در یک تراکنش اجرا می‌شود؛ برای ساختن ایندکس بدون قفل از <code>AddIndexConcurrently</code> با <code>atomic = False</code> استفاده کنید.</li>
</ul>""",
                },
                {
                    "title": "متدهای مدل، save و سیگنال‌ها: هر منطق کجا بنشیند؟",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>مدل‌های چاق، Viewهای لاغر — با احتیاط</h2>
<p>منطقی که به «خود داده» مربوط است (کد رهگیری، محاسبه‌ی جمع، قابل‌پرداخت بودن) جایش در مدل است، نه در ده View مختلف. جنگو چند نقطه‌ی استاندارد برای این کار دارد:</p>
<pre><code class="language-python">import secrets

from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Order(models.Model):
    # ... فیلدهای درس قبل ...
    delivery_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"سفارش {self.tracking_code or self.pk}"

    def get_absolute_url(self):
        return reverse("orders:detail", kwargs={"pk": self.pk})

    @property
    def is_payable(self):
        return self.status == self.Status.PENDING and self.total &gt; 0

    def clean(self):
        if self.delivery_date and self.delivery_date &lt; timezone.localdate():
            raise ValidationError({"delivery_date": "تاریخ تحویل نمی‌تواند در گذشته باشد."})

    def save(self, *args, **kwargs):
        if not self.tracking_code:
            self.tracking_code = "KSH" + secrets.token_hex(4).upper()
            update_fields = kwargs.get("update_fields")
            if update_fields is not None:
                kwargs["update_fields"] = {"tracking_code", *update_fields}
        super().save(*args, **kwargs)</code></pre>
<table><thead><tr><th>نقطه</th><th>کِی اجرا می‌شود</th><th>مناسب برای</th></tr></thead><tbody>
<tr><td><code>__str__</code></td><td>نمایش در ادمین، shell، قالب</td><td>متن خوانا و کوتاه</td></tr>
<tr><td><code>get_absolute_url</code></td><td>redirect(obj)، دکمه‌ی «View on site» ادمین</td><td>آدرس صفحه‌ی جزئیات</td></tr>
<tr><td><code>clean()</code></td><td>فقط در <code>full_clean()</code>؛ یعنی ModelForm و ادمین</td><td>اعتبارسنجی بین چند فیلد</td></tr>
<tr><td><code>save()</code></td><td>هر ذخیره‌ی تکی</td><td>مقداردهی خودکار فیلدها</td></tr>
<tr><td>سیگنال</td><td>قبل/بعد از save و delete</td><td>واکنش اپ «دیگر» به یک رویداد</td></tr>
</tbody></table>
<h3>سیگنال‌ها و وقتی نباید سراغشان رفت</h3>
<pre><code class="language-python"># apps/notifications/signals.py
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.orders.models import Order
from .tasks import send_order_sms

@receiver(post_save, sender=Order, dispatch_uid="order_created_sms")
def order_created(sender, instance, created, **kwargs):
    if created:
        transaction.on_commit(lambda: send_order_sms.delay(instance.pk))

# apps/notifications/apps.py
class NotificationsConfig(AppConfig):
    name = "apps.notifications"
    def ready(self):
        from . import signals  # noqa: F401  ثبت گیرنده‌ها</code></pre>
<p>سیگنال منطق را «پنهان» می‌کند: کسی که <code>order.save()</code> را می‌خواند نمی‌فهمد پیامکی هم فرستاده می‌شود. قاعده: اگر منطق در همان اپ است، یک تابع سرویس صریح (مثل <code>place_order()</code>) بنویسید. سیگنال را برای جداسازی اپ‌ها نگه دارید؛ مثلاً اپ اعلان‌ها که نباید اپ سفارش از وجودش باخبر باشد.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>save()</code> به‌طور خودکار <code>full_clean()</code> را صدا نمی‌زند؛ پس <code>clean()</code> شما در shell، API و اسکریپت‌ها اجرا نمی‌شود مگر خودتان صدایش کنید.</li>
<li><code>QuerySet.update()</code> و <code>bulk_create()</code> نه <code>save()</code> را صدا می‌زنند نه سیگنال‌های pre_save/post_save را؛ اما <code>QuerySet.delete()</code> سیگنال‌های حذف را برای تک‌تک اشیا می‌فرستد.</li>
<li>اگر در save فیلدی را خودکار مقدار می‌دهید، حتماً آن را به <code>update_fields</code> اضافه کنید (مثل کد بالا)؛ وگرنه فراخوانی <code>save(update_fields=[...])</code> مقدار جدید را ذخیره نمی‌کند.</li>
<li>بدون <code>dispatch_uid</code>، اگر ماژول سیگنال دو بار import شود گیرنده دو بار ثبت می‌شود و مشتری دو پیامک می‌گیرد.</li>
<li>کار خارجی (پیامک، ایمیل، وب‌هوک) را همیشه در <code>transaction.on_commit</code> بگذارید؛ وگرنه ممکن است پیامک برود و تراکنش rollback شود.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۳ ─────────────────────────────
        {
            "title": "فصل ۳: QuerySet حرفه‌ای — سریع، درست و بدون N+1",
            "lessons": [
                {
                    "title": "QuerySet تنبل است: ارزیابی، کش، filter/exclude و lookupها",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>تا وقتی لازم نباشد، هیچ کوئری‌ای اجرا نمی‌شود</h2>
<p>وقتی می‌نویسید <code>qs = Order.objects.filter(status="paid")</code> هیچ SQLی اجرا نمی‌شود؛ فقط یک «توصیف» از کوئری ساخته می‌شود. می‌توانید ده بار filter و order_by و exclude را زنجیر کنید و باز هم هیچ اتفاقی در پایگاه داده نمی‌افتد. کوئری فقط در این لحظه‌ها اجرا می‌شود (ارزیابی):</p>
<ul>
<li>پیمایش با <code>for</code> یا در قالب با <code>{% for %}</code></li>
<li><code>list(qs)</code>، <code>len(qs)</code>، <code>bool(qs)</code> و <code>if qs:</code></li>
<li>برش با گام (<code>qs[::2]</code>) یا ایندکس تکی (<code>qs[0]</code>)</li>
<li><code>repr(qs)</code> — مثلاً وقتی در shell فقط نامش را می‌نویسید</li>
</ul>
<h3>کش نتیجه</h3>
<p>بعد از اولین ارزیابی، نتیجه روی همان شیء QuerySet کش می‌شود. این رفتار هم کمک است هم دام:</p>
<pre><code class="language-python">orders = Order.objects.filter(status="paid")
for o in orders: ...          # کوئری ۱
for o in orders: ...          # از کش؛ بدون کوئری

Order.objects.filter(status="paid")[0]   # کوئری
Order.objects.filter(status="paid")[0]   # باز کوئری؛ هر بار QuerySet تازه

# خوب: وقتی فقط وجود/تعداد مهم است
if orders.exists(): ...       # SELECT 1 ... LIMIT 1
total = orders.count()        # SELECT COUNT(*)

# اما اگر قرار است بعداً پیمایش کنید، همان len() بهتر است
orders = list(orders)
if orders:
    print(len(orders))</code></pre>
<h3>filter، exclude و lookupها</h3>
<p>شکل کلی یک شرط <code>field__lookup=value</code> است و با <code>__</code> می‌توانید روی روابط هم جلو بروید:</p>
<table><thead><tr><th>lookup</th><th>مثال</th><th>SQL تقریبی</th></tr></thead><tbody>
<tr><td>exact / iexact</td><td><code>code__iexact="ksh-12"</code></td><td>= / ILIKE</td></tr>
<tr><td>contains / icontains</td><td><code>name__icontains="افشان"</code></td><td>LIKE '%…%'</td></tr>
<tr><td>in</td><td><code>status__in=["paid", "shipped"]</code></td><td>IN (…)</td></tr>
<tr><td>gt, gte, lt, lte</td><td><code>total__gte=50_000_000</code></td><td>&gt;=</td></tr>
<tr><td>range</td><td><code>created_at__date__range=(d1, d2)</code></td><td>BETWEEN</td></tr>
<tr><td>isnull</td><td><code>delivery_date__isnull=True</code></td><td>IS NULL</td></tr>
<tr><td>startswith</td><td><code>customer__user__mobile__startswith="0912"</code></td><td>LIKE '0912%'</td></tr>
<tr><td>date / year / month</td><td><code>created_at__year=2025</code></td><td>استخراج بخش تاریخ</td></tr>
</tbody></table>
<pre><code class="language-python">qs = (Order.objects
      .filter(customer__city="کاشان", total__gte=100_000_000)
      .exclude(status="cancelled")
      .order_by("-created_at"))
print(qs.query)     # SQL تولیدشده برای دیباگ</code></pre>
<h3>جست‌وجوی فارسی</h3>
<p>متن فارسی دو «ی» و دو «ک» دارد: فارسی (ی، ک) و عربی (ي، ك). اگر داده از منابع مختلف (اکسل قدیمی، کیبورد عربی) آمده باشد، <code>icontains="کاشی"</code> رکوردی را که با «كاشي» ذخیره شده پیدا نمی‌کند. راه درست: هم هنگام ذخیره و هم روی عبارت جست‌وجو، این حروف را یکسان کنید (فصل ۵).</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>.first()</code> اگر ترتیبی تعریف نشده باشد خودش <code>ORDER BY pk</code> اضافه می‌کند؛ روی جدول بزرگ بدون ایندکس مناسب ممکن است کند باشد.</li>
<li>زنجیر کردن دو <code>filter()</code> روی رابطه‌ی چندتایی با یک <code>filter()</code> با دو شرط فرق دارد: اولی ممکن است دو قلم <em>متفاوت</em> را مطابق کند، دومی شرط هر دو را روی <em>یک</em> قلم می‌خواهد.</li>
<li>دادن یک QuerySet به <code>__in</code> (<code>filter(customer__in=Customer.objects.filter(...))</code>) یک زیرکوئری SQL می‌سازد، نه دو کوئری جدا؛ نیازی به <code>values_list</code> و list کردن نیست.</li>
<li><code>created_at__date=...</code> تاریخ را در منطقه‌ی زمانی فعال (تهران) حساب می‌کند نه UTC؛ سفارش ساعت ۱ بامداد تهران در همان روز تهران شمرده می‌شود.</li>
<li>روی SQLite جست‌وجوی <code>iexact</code> و <code>icontains</code> فقط برای حروف ASCII غیرحساس به بزرگی است؛ برای فارسی مهم نیست، اما در متن‌های لاتین نتیجه با PostgreSQL فرق می‌کند.</li>
</ul>""",
                },
                {
                    "title": "Q و F، annotate و aggregate، values و values_list",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>منطق را به پایگاه داده بسپارید</h2>
<p>یک خطای رایج این است که همه‌ی ردیف‌ها را به پایتون بیاوریم و آن‌جا جمع، شمارش یا مقایسه کنیم. پایگاه داده برای همین کارها ساخته شده و ده‌ها برابر سریع‌تر است. ابزارهای اصلی ORM برای این کار Q، F، annotate و aggregate هستند.</p>
<h3>Q: شرط‌های «یا» و «نقیض»</h3>
<pre><code class="language-python">from django.db.models import Q

# سفارش‌های پرداخت‌شده یا ارسال‌شده که مشتری‌شان تهرانی نیست
Order.objects.filter(Q(status="paid") | Q(status="shipped"), ~Q(customer__city="تهران"))

# ساخت پویا از فرم جست‌وجو
cond = Q()
if q := request.GET.get("q"):
    cond &amp;= Q(tracking_code__icontains=q) | Q(customer__full_name__icontains=q)
if city := request.GET.get("city"):
    cond &amp;= Q(customer__city=city)
orders = Order.objects.filter(cond)</code></pre>
<h3>F: ارجاع به مقدار ستون</h3>
<pre><code class="language-python">from django.db.models import F

Carpet.objects.filter(stock__lt=F("min_stock"))                 # مقایسه‌ی دو ستون
Carpet.objects.filter(pk=7).update(stock=F("stock") - 1)        # کم کردن اتمیک در SQL
Carpet.objects.update(price=F("price") * 110 / 100)             # افزایش ۱۰٪ همه‌ی قیمت‌ها</code></pre>
<p><code>stock=F("stock") - 1</code> در خود پایگاه داده اجرا می‌شود؛ پس اگر دو درخواست هم‌زمان برسند، هیچ‌کدام تغییر دیگری را بازنویسی نمی‌کند (race condition کلاسیک «خواندن، کم کردن، ذخیره» پیش نمی‌آید).</p>
<h3>aggregate و annotate</h3>
<p><code>aggregate</code> یک دیکشنری برای <em>کل</em> QuerySet برمی‌گرداند؛ <code>annotate</code> به <em>هر ردیف</em> یک ستون محاسبه‌شده اضافه می‌کند.</p>
<pre><code class="language-python">from django.db.models import Avg, Count, Sum, BigIntegerField
from django.db.models.functions import Coalesce

Order.objects.filter(status="paid").aggregate(total=Sum("total"), avg=Avg("total"), n=Count("id"))
# {'total': 8450000000, 'avg': 70416666.6, 'n': 120}

vip = (Customer.objects
       .annotate(order_count=Count("orders", distinct=True),
                 spent=Coalesce(Sum("orders__total"), 0, output_field=BigIntegerField()))
       .filter(order_count__gte=3)
       .order_by("-spent"))</code></pre>
<h3>values و values_list: فقط همان ستون‌ها</h3>
<pre><code class="language-python">Order.objects.values("status").annotate(n=Count("id"))           # گروه‌بندی بر اساس status
Carpet.objects.values_list("code", flat=True)                      # ['KSH-1200-17', ...]
Carpet.objects.values_list("code", "price", named=True)           # namedtuple</code></pre>
<p>ترتیب مهم است: <code>values()</code> قبل از <code>annotate()</code> یعنی GROUP BY؛ بعد از آن یعنی فقط انتخاب ستون‌ها.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>دو <code>Count</code> یا <code>Sum</code> روی دو رابطه‌ی چندتایی مختلف در یک annotate، به دلیل JOIN نتیجه را ضرب می‌کنند؛ برای Count از <code>distinct=True</code> و برای Sum از Subquery (درس ۱۴) استفاده کنید.</li>
<li>بعد از <code>obj.stock = F("stock") - 1; obj.save()</code> مقدار <code>obj.stock</code> در پایتون یک عبارت F است، نه عدد؛ قبل از استفاده <code>obj.refresh_from_db(fields=["stock"])</code> بزنید.</li>
<li><code>Sum</code> روی مجموعه‌ی خالی <code>None</code> برمی‌گرداند نه صفر؛ Coalesce یا در Django 4.0 به بعد پارامتر <code>default=0</code> خود aggregate را به کار ببرید: <code>Sum("total", default=0)</code>.</li>
<li><code>TruncMonth</code> ماه میلادی را برمی‌گرداند؛ برای گزارش ماهانه‌ی شمسی باید بازه‌ی هر ماه شمسی را با jdatetime حساب کنید و با <code>created_at__range</code> فیلتر کنید (پروژه‌ی پایانی).</li>
<li>ordering پیش‌فرض Meta روی GROUP BY اثر ندارد (از Django 3.1)، اما <code>order_by()</code> صریح شما وارد GROUP BY می‌شود و ممکن است گروه‌ها را بشکند؛ اگر گروه‌بندی عجیب شد، <code>order_by()</code> خالی بزنید.</li>
</ul>""",
                },
                {
                    "title": "مسئله‌ی N+1: select_related، prefetch_related و django-debug-toolbar",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>صفحه‌ای که با ۲۰۱ کوئری باز می‌شود</h2>
<p>مهم‌ترین مشکل کارایی در پروژه‌های جنگو N+1 است: یک کوئری برای فهرست و سپس برای <em>هر</em> ردیف یک کوئری دیگر برای رابطه‌اش. این کد بی‌گناه به نظر می‌رسد:</p>
<pre><code class="language-html">{% for order in orders %}
  &lt;tr&gt;
    &lt;td&gt;{{ order.tracking_code }}&lt;/td&gt;
    &lt;td&gt;{{ order.customer.full_name }}&lt;/td&gt;       {# هر بار یک کوئری #}
    &lt;td&gt;{{ order.items.count }}&lt;/td&gt;               {# باز یک کوئری #}
  &lt;/tr&gt;
{% endfor %}</code></pre>
<p>با ۱۰۰ سفارش: ۱ + ۱۰۰ + ۱۰۰ = ۲۰۱ کوئری. روی لوکال با SQLite سریع به نظر می‌رسد؛ روی سرور با پایگاه داده‌ی شبکه‌ای، صفحه چند ثانیه طول می‌کشد.</p>
<h3>راه‌حل‌ها</h3>
<table><thead><tr><th>ابزار</th><th>برای</th><th>روش</th></tr></thead><tbody>
<tr><td><code>select_related</code></td><td>ForeignKey و OneToOne (رو به جلو)</td><td>JOIN در همان کوئری</td></tr>
<tr><td><code>prefetch_related</code></td><td>ManyToMany و رابطه‌ی معکوس</td><td>یک کوئری جدا با IN و اتصال در پایتون</td></tr>
<tr><td><code>annotate(Count)</code></td><td>وقتی فقط تعداد یا جمع لازم است</td><td>GROUP BY در همان کوئری</td></tr>
</tbody></table>
<pre><code class="language-python">from django.db.models import Count, Prefetch

orders = (Order.objects
          .select_related("customer", "customer__user")
          .annotate(item_count=Count("items"))
          .prefetch_related(
              Prefetch("items",
                       queryset=OrderItem.objects.select_related("carpet").order_by("id"),
                       to_attr="item_list"))
          )[:50]
# در قالب: order.customer.full_name، order.item_count، و حلقه روی order.item_list
# مجموع: ۲ کوئری، مستقل از تعداد سفارش‌ها</code></pre>
<h3>django-debug-toolbar: اول ببینید، بعد بهینه کنید</h3>
<pre><code class="language-powershell">pip install django-debug-toolbar</code></pre>
<pre><code class="language-python"># settings (فقط توسعه)
if DEBUG:
    INSTALLED_APPS += ["debug_toolbar"]
    MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
    INTERNAL_IPS = ["127.0.0.1"]

# config/urls.py
from django.conf import settings
if settings.DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]</code></pre>
<p>پنل SQL نوار ابزار تعداد کوئری‌ها، زمان هر کدام و مهم‌تر از همه «similar» و «duplicate» را نشان می‌دهد؛ ده کوئری مشابه یعنی یک N+1.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>اگر روی رابطه‌ی prefetch‌شده دوباره <code>.filter()</code> یا <code>.order_by()</code> بزنید (<code>order.items.filter(...)</code>)، کش prefetch دور ریخته می‌شود و کوئری تازه می‌رود؛ فیلتر را داخل <code>Prefetch(queryset=...)</code> بگذارید.</li>
<li>وقتی در <code>Prefetch</code> از <code>to_attr</code> استفاده می‌کنید، نتیجه فقط در همان ویژگی (<code>item_list</code>) است؛ <code>order.items.all</code> و <code>order.items.count</code> در قالب دوباره برای هر سفارش کوئری می‌زنند. در قالب فقط از <code>item_list</code> استفاده کنید.</li>
<li>در تست‌ها با <code>self.assertNumQueries(2)</code> تعداد کوئری را قفل کنید تا کسی بعداً بی‌صدا N+1 را برنگرداند.</li>
<li>debug-toolbar روی پاسخ‌های JSON و API ظاهر نمی‌شود؛ برای آن‌ها <code>connection.queries</code> (فقط با DEBUG=True) یا لاگر <code>django.db.backends</code> را در سطح DEBUG روشن کنید.</li>
<li><code>.iterator()</code> از Django 4.1 با prefetch_related کار می‌کند به شرطی که <code>chunk_size</code> بدهید؛ برای خروجی اکسل از صدها هزار ردیف بدون پر شدن حافظه.</li>
</ul>""",
                },
                {
                    "title": "Subquery، Exists، عملیات دسته‌ای، only/defer و SQL خام",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>ابزارهای سطح بالاتر ORM</h2>
<p>وقتی annotate ساده کافی نیست — مثلاً «تاریخ آخرین سفارش هر مشتری» یا «آیا سفارش در انتظار دارد؟» — به زیرکوئری‌های همبسته نیاز داریم. جنگو این‌ها را با <code>Subquery</code>، <code>OuterRef</code> و <code>Exists</code> می‌سازد.</p>
<pre><code class="language-python">from django.db.models import Exists, OuterRef, Subquery

last_order = (Order.objects
              .filter(customer=OuterRef("pk"))
              .order_by("-created_at"))

customers = Customer.objects.annotate(
    last_order_at=Subquery(last_order.values("created_at")[:1]),
    last_total=Subquery(last_order.values("total")[:1]),
    has_pending=Exists(Order.objects.filter(customer=OuterRef("pk"), status="pending")),
).filter(has_pending=False)</code></pre>
<p><code>OuterRef("pk")</code> یعنی «pk ردیف کوئری بیرونی». <code>Exists</code> از <code>Count() &gt; 0</code> بسیار سریع‌تر است چون پایگاه داده با اولین تطابق متوقف می‌شود.</p>
<h3>عملیات دسته‌ای</h3>
<pre><code class="language-python"># ساخت هزار طرح با چند کوئری، نه هزار کوئری
Carpet.objects.bulk_create(
    [Carpet(code=f"KSH-{i}", name=f"طرح {i}", density=1200, price=45_000_000) for i in range(1000)],
    batch_size=500,
)

# به‌روزرسانی دسته‌ای فیلدهای مشخص
for c in carpets:
    c.price = int(round(c.price * 1.15, -4))       # گرد کردن به ده‌هزار ریال
Carpet.objects.bulk_update(carpets, ["price"], batch_size=500)

# upsert: اگر بود به‌روز کن، نبود بساز
carpet, created = Carpet.objects.update_or_create(
    code="KSH-1200-17",
    defaults={"price": 52_000_000},                    # فقط هنگام به‌روزرسانی (و ساخت)
    create_defaults={"price": 52_000_000, "name": "افشان", "density": 1200},  # Django 5.0+
)</code></pre>
<h3>only و defer</h3>
<p><code>only("id", "code", "price")</code> فقط همین ستون‌ها را می‌خواند و <code>defer("description")</code> همه جز این‌ها را. برای جدول‌هایی با فیلد متنی حجیم (توضیحات، JSON) در صفحه‌ی فهرست تفاوت چشمگیری دارد.</p>
<h3>SQL خام؛ آخرین گزینه</h3>
<pre><code class="language-python">rows = Carpet.objects.raw(
    "SELECT * FROM catalog_carpet WHERE density = %s AND price &lt; %s",
    [1200, 60_000_000],
)

from django.db import connection
with connection.cursor() as cur:
    cur.execute("SELECT city, COUNT(*) FROM orders_customer GROUP BY city")
    stats = cur.fetchall()</code></pre>
<p>وقتش وقتی است که ORM واقعاً نمی‌تواند (توابع پنجره‌ای خاص، CTE بازگشتی، hint پایگاه داده) یا کوئری گزارشی پیچیده‌ای دارید که SQL خوانا از ORM نامفهوم بهتر است. پارامترها را <em>همیشه</em> جدا بفرستید.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>هرگز SQL را با f-string نسازید (<code>f"... WHERE code = '{code}'"</code>)؛ این دقیقاً SQL Injection است. <code>%s</code> و لیست پارامتر را به درایور بسپارید؛ حتی برای عدد.</li>
<li><code>bulk_create</code> متد <code>save()</code> و سیگنال‌ها را اجرا نمی‌کند؛ فیلدهایی که در save خودکار پر می‌شوند (مثل کد رهگیری) خالی می‌مانند.</li>
<li><code>bulk_create(..., update_conflicts=True, unique_fields=["code"], update_fields=["price"])</code> یک upsert واقعی در یک کوئری است؛ برای همگام‌سازی لیست قیمت از اکسل عالی است.</li>
<li><code>get_or_create</code> بدون قید unique روی فیلدهای جست‌وجو در شرایط هم‌زمانی ممکن است دو رکورد بسازد؛ قید unique آن را امن می‌کند چون جنگو IntegrityError را گرفته و دوباره get می‌زند.</li>
<li>دسترسی به فیلدی که با <code>only</code> کنار گذاشته شده، برای <em>هر</em> شیء یک کوئری جدا می‌زند؛ only بد می‌تواند N+1 تازه بسازد.</li>
</ul>""",
                },
                {
                    "title": "تراکنش، select_for_update و Manager/QuerySet سفارشی",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>یا همه، یا هیچ</h2>
<p>ثبت یک سفارش چند مرحله دارد: ساخت سفارش، ساخت اقلام، کم کردن موجودی انبار. اگر مرحله‌ی سوم خطا بدهد، نباید سفارشی نیمه‌کاره باقی بماند. <code>transaction.atomic</code> همه‌ی این مراحل را یک واحد می‌کند: یا همه commit می‌شوند یا همه rollback.</p>
<h3>کم کردن موجودی بدون فروش بیش از انبار</h3>
<p>دو مشتری هم‌زمان آخرین فرش یک طرح را سفارش می‌دهند. هر دو موجودی را «۱» می‌خوانند و هر دو ثبت می‌کنند. <code>select_for_update</code> ردیف‌ها را تا پایان تراکنش قفل می‌کند تا درخواست دوم منتظر بماند و موجودی به‌روز را ببیند:</p>
<pre><code class="language-python"># apps/orders/services.py
from django.db import transaction
from django.db.models import F

from apps.catalog.models import Carpet
from .models import Order, OrderItem
from .tasks import send_order_sms


class OutOfStock(Exception):
    pass


def place_order(customer, items):
    # items: [{"carpet_id": 3, "quantity": 2}, ...]
    ids = [i["carpet_id"] for i in items]
    with transaction.atomic():
        carpets = Carpet.objects.select_for_update().in_bulk(ids)
        order = Order.objects.create(customer=customer)
        total = 0
        for item in items:
            carpet = carpets[item["carpet_id"]]
            if carpet.stock &lt; item["quantity"]:
                raise OutOfStock(f"موجودی طرح {carpet.name} کافی نیست.")
            OrderItem.objects.create(order=order, carpet=carpet,
                                     quantity=item["quantity"], unit_price=carpet.price)
            Carpet.objects.filter(pk=carpet.pk).update(stock=F("stock") - item["quantity"])
            total += carpet.price * item["quantity"]
        order.total = total
        order.save(update_fields=["total"])
        transaction.on_commit(lambda: send_order_sms.delay(order.pk))
    return order</code></pre>
<p>اگر <code>OutOfStock</code> بالا برود، همه‌چیز rollback می‌شود و پیامکی هم نمی‌رود، چون <code>on_commit</code> فقط بعد از commit موفق اجرا می‌شود.</p>
<h3>QuerySet و Manager سفارشی</h3>
<p>فیلترهای تکراری را یک بار و با نام معنادار تعریف کنید تا در View، ادمین، API و تست یکسان باشند:</p>
<pre><code class="language-python">class OrderQuerySet(models.QuerySet):
    def pending(self):
        return self.filter(status=self.model.Status.PENDING)

    def for_user(self, user):
        return self.filter(customer__user=user)

    def with_details(self):
        return self.select_related("customer").prefetch_related("items__carpet")


class Order(models.Model):
    ...
    objects = OrderQuerySet.as_manager()

# استفاده: زنجیرپذیر
Order.objects.for_user(request.user).pending().with_details()</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>select_for_update()</code> بیرون از <code>atomic</code> خطای <code>TransactionManagementError</code> می‌دهد؛ و روی SQLite هیچ قفلی نمی‌گذارد، پس رفتار هم‌زمانی را فقط روی PostgreSQL یا MySQL آزمایش کنید.</li>
<li>اگر داخل <code>atomic</code> یک <code>IntegrityError</code> را با try بگیرید و ادامه دهید، تراکنش خراب است و کوئری بعدی خطا می‌دهد؛ بخش پرخطر را در یک <code>atomic</code> تودرتو (savepoint) بپیچید.</li>
<li><code>select_for_update(skip_locked=True)</code> ردیف‌های قفل‌شده را رد می‌کند؛ پایه‌ی ساخت یک صف کار ساده روی PostgreSQL بدون Redis.</li>
<li><code>ATOMIC_REQUESTS = True</code> در تنظیمات DATABASES هر درخواست را یک تراکنش می‌کند؛ ساده است اما تراکنش را در طول رندر قالب هم باز نگه می‌دارد و قفل‌ها طولانی می‌شوند.</li>
<li>Manager پیش‌فرض (اولین Manager تعریف‌شده) را هرگز فیلتر نکنید (مثلاً فقط فعال‌ها)؛ ادمین، روابط معکوس و dumpdata از آن استفاده می‌کنند و رکوردها «ناپدید» می‌شوند. یک Manager دوم مثل <code>active = ActiveManager()</code> بسازید.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۴ ─────────────────────────────
        {
            "title": "فصل ۴: View، URL و Template",
            "lessons": [
                {
                    "title": "URLها: path و converterها، include، namespace و reverse",
                    "kind": "text",
                    "minutes": 18,
                    "is_preview": False,
                    "body": r"""<h2>آدرس‌ها را اسم‌گذاری کنید، نه هاردکد</h2>
<p>URLconf جنگو فهرستی از الگوهاست که از بالا به پایین بررسی می‌شوند و اولین تطابق برنده است. در پروژه‌ی تمیز، <code>config/urls.py</code> فقط مسیرهای اصلی را به اپ‌ها «include» می‌کند و هر اپ فایل urls خودش را دارد.</p>
<pre><code class="language-python"># config/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("manage-7f3a/", admin.site.urls),               # آدرس ادمین را حدس‌زدنی نگذارید
    path("orders/", include("apps.orders.urls")),
    path("api/", include("apps.api.urls")),
    path("", include("apps.pages.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# apps/orders/urls.py
from django.urls import path, register_converter
from . import converters, views

register_converter(converters.TrackingCodeConverter, "tcode")

app_name = "orders"                                       # namespace
urlpatterns = [
    path("", views.OrderListView.as_view(), name="list"),
    path("new/", views.OrderCreateView.as_view(), name="create"),
    path("&lt;int:pk&gt;/", views.order_detail, name="detail"),
    path("&lt;int:pk&gt;/cancel/", views.cancel_order, name="cancel"),
    path("track/&lt;tcode:code&gt;/", views.track, name="track"),
]</code></pre>
<h3>converterها</h3>
<table><thead><tr><th>converter</th><th>تطبیق</th><th>نوع در View</th></tr></thead><tbody>
<tr><td>int</td><td>ارقام 0 تا 9</td><td>int</td></tr>
<tr><td>str</td><td>هر چیزی جز / (پیش‌فرض)</td><td>str</td></tr>
<tr><td>slug</td><td>حروف و ارقام لاتین، - و _</td><td>str</td></tr>
<tr><td>uuid</td><td>UUID با خط تیره</td><td>UUID</td></tr>
<tr><td>path</td><td>هر چیزی حتی /</td><td>str</td></tr>
</tbody></table>
<p>converter اختصاصی فقط یک کلاس با <code>regex</code>، <code>to_python</code> و <code>to_url</code> است:</p>
<pre><code class="language-python"># apps/orders/converters.py
class TrackingCodeConverter:
    regex = r"KSH[0-9A-F]{8}"

    def to_python(self, value):
        return value.upper()

    def to_url(self, value):
        return value</code></pre>
<h3>reverse: ساخت آدرس از روی نام</h3>
<pre><code class="language-python">from django.urls import reverse, reverse_lazy

reverse("orders:detail", kwargs={"pk": 42})       # '/orders/42/'
reverse("orders:track", args=["KSH1A2B3C4D"])

class OrderCreateView(CreateView):
    success_url = reverse_lazy("orders:list")      # در سطح کلاس، lazy لازم است</code></pre>
<p>در قالب: <code>{% url 'orders:detail' pk=order.pk %}</code>. اگر فردا آدرس را از <code>orders/</code> به <code>sefaresh/</code> تغییر دهید، هیچ لینکی نمی‌شکند.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>اگر <code>to_python</code> یک converter استثنای <code>ValueError</code> بدهد، جنگو آن را «عدم تطابق» حساب می‌کند و سراغ الگوی بعدی می‌رود؛ راهی تمیز برای رد کردن مقادیر نامعتبر پیش از رسیدن به View.</li>
<li>با <code>APPEND_SLASH</code> (پیش‌فرض True) درخواست GET به <code>/orders/42</code> به <code>/orders/42/</code> ریدایرکت می‌شود؛ اما برای POST در DEBUG خطای RuntimeError می‌گیرید، چون داده‌ی POST در ریدایرکت از دست می‌رود.</li>
<li>در سطح کلاس و ماژول (success_url، تنظیمات LOGIN_URL) از <code>reverse_lazy</code> استفاده کنید؛ <code>reverse</code> در زمان import، قبل از بارگذاری URLconf، خطا می‌دهد.</li>
<li><code>python manage.py show_urls</code> جزو جنگو نیست (از django-extensions است)؛ بدون آن هم می‌توانید در shell با <code>get_resolver().reverse_dict</code> الگوها را ببینید، یا <code>resolve("/orders/42/")</code> بزنید تا بفهمید آدرس به کدام View می‌رسد.</li>
<li>ثبت دوباره‌ی یک converter با همان نام در Django 5.1 به بعد منسوخ و خطاساز است؛ <code>register_converter</code> را فقط یک بار و در یک ماژول انجام دهید.</li>
</ul>""",
                },
                {
                    "title": "View تابعی: request، render، redirect، JsonResponse و get_object_or_404",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>ساده‌ترین شکل View: یک تابع</h2>
<p>View تابعی (FBV) یک <code>HttpRequest</code> می‌گیرد و یک <code>HttpResponse</code> برمی‌گرداند. همین. هر چیز دیگری — قالب، ریدایرکت، JSON — فقط انواع مختلف پاسخ است. FBV صریح و خواناست و برای منطق‌های غیرمعمول اغلب از CBV بهتر است.</p>
<h3>آنچه در request دارید</h3>
<table><thead><tr><th>ویژگی</th><th>محتوا</th></tr></thead><tbody>
<tr><td><code>request.method</code></td><td>"GET"، "POST" و…</td></tr>
<tr><td><code>request.GET</code> / <code>request.POST</code></td><td>QueryDict پارامترها؛ <code>getlist()</code> برای چندمقداری</td></tr>
<tr><td><code>request.FILES</code></td><td>فایل‌های آپلودی</td></tr>
<tr><td><code>request.user</code></td><td>کاربر فعلی یا AnonymousUser</td></tr>
<tr><td><code>request.headers</code></td><td>هدرها؛ غیرحساس به بزرگی حروف</td></tr>
<tr><td><code>request.session</code></td><td>دیکشنری Session</td></tr>
<tr><td><code>request.META["REMOTE_ADDR"]</code></td><td>IP (پشت پراکسی: IP خود پراکسی!)</td></tr>
</tbody></table>
<pre><code class="language-python"># apps/orders/views.py
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from apps.catalog.models import Carpet
from .models import Order


@login_required
def order_detail(request, pk):
    order = get_object_or_404(
        Order.objects.select_related("customer").prefetch_related("items__carpet"),
        pk=pk,
        customer__user=request.user,          # جلوگیری از دیدن سفارش دیگران
    )
    return render(request, "orders/detail.html", {"order": order})


@login_required
@require_POST
def cancel_order(request, pk):
    order = get_object_or_404(Order, pk=pk, customer__user=request.user)
    if order.status != Order.Status.PENDING:
        messages.error(request, "فقط سفارش در انتظار پرداخت قابل لغو است.")
    else:
        order.status = Order.Status.CANCELLED
        order.save(update_fields=["status"])
        messages.success(request, f"سفارش {order.tracking_code} لغو شد.")
    return redirect(order)                    # از get_absolute_url استفاده می‌کند


def carpet_price(request, code):
    carpet = get_object_or_404(Carpet, code=code, status="active")
    return JsonResponse({"code": carpet.code, "name": carpet.name, "price": carpet.price},
                        json_dumps_params={"ensure_ascii": False})</code></pre>
<h3>الگوی POST/Redirect/GET</h3>
<p>بعد از هر POST موفق همیشه redirect کنید، نه render. اگر render کنید و کاربر صفحه را رفرش کند، مرورگر فرم را دوباره می‌فرستد و سفارش دو بار ثبت یا لغو می‌شود. پیام موفقیت را هم با <code>messages</code> به صفحه‌ی بعد منتقل کنید.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>شرط <code>customer__user=request.user</code> در get_object_or_404 جلوی آسیب‌پذیری IDOR را می‌گیرد: کاربری که عدد آدرس را عوض کند به‌جای سفارش دیگران 404 می‌بیند، نه 403 که وجود سفارش را لو بدهد.</li>
<li>بدون <code>ensure_ascii=False</code> متن فارسی در JsonResponse به‌صورت <code>ک...</code> می‌رود؛ از نظر فنی درست است اما در دیباگ و لاگ خوانا نیست.</li>
<li><code>JsonResponse</code> به‌طور پیش‌فرض فقط dict می‌پذیرد؛ برای برگرداندن لیست باید <code>safe=False</code> بدهید.</li>
<li>ترتیب دکوراتورها مهم است: <code>login_required</code> بیرونی باشد تا کاربر مهمان به صفحه‌ی ورود برود، نه این‌که اول خطای 405 بگیرد.</li>
<li><code>redirect()</code> هم شیء مدل، هم نام url با آرگومان (<code>redirect("orders:detail", pk=5)</code>) و هم آدرس خام را می‌پذیرد؛ برای ریدایرکت دائمی <code>permanent=True</code> بدهید.</li>
</ul>""",
                },
                {
                    "title": "View کلاسی و generic viewها: ListView، DetailView، CreateView و mixinها",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>الگوهای تکراری را دوباره ننویسید</h2>
<p>فهرست با صفحه‌بندی، صفحه‌ی جزئیات، فرم ساخت و ویرایش، تأیید حذف: این پنج الگو در هر پروژه ده‌ها بار تکرار می‌شوند. Generic viewهای جنگو این‌ها را آماده دارند و شما فقط تفاوت‌ها را بازنویسی می‌کنید.</p>
<table><thead><tr><th>View</th><th>کار</th><th>قالب پیش‌فرض</th></tr></thead><tbody>
<tr><td>ListView</td><td>فهرست + صفحه‌بندی</td><td><code>orders/order_list.html</code></td></tr>
<tr><td>DetailView</td><td>یک شیء با pk یا slug</td><td><code>orders/order_detail.html</code></td></tr>
<tr><td>CreateView</td><td>فرم ساخت</td><td><code>orders/order_form.html</code></td></tr>
<tr><td>UpdateView</td><td>فرم ویرایش</td><td><code>orders/order_form.html</code></td></tr>
<tr><td>DeleteView</td><td>تأیید و حذف با POST</td><td><code>orders/order_confirm_delete.html</code></td></tr>
<tr><td>TemplateView / RedirectView</td><td>صفحه‌ی ثابت / ریدایرکت</td><td>—</td></tr>
</tbody></table>
<pre><code class="language-python">from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, ListView

from .forms import OrderForm
from .models import Order


class OrderListView(LoginRequiredMixin, ListView):
    template_name = "orders/list.html"
    context_object_name = "orders"
    paginate_by = 20
    paginate_orphans = 3                     # صفحه‌ی آخرِ ۲ آیتمی ساخته نشود

    def get_queryset(self):
        qs = Order.objects.for_user(self.request.user).select_related("customer")
        if q := self.request.GET.get("q", "").strip():
            qs = qs.filter(tracking_code__icontains=q)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["q"] = self.request.GET.get("q", "")
        return ctx


class OrderDetailView(LoginRequiredMixin, DetailView):
    template_name = "orders/detail.html"

    def get_queryset(self):
        return Order.objects.for_user(self.request.user).with_details()


class OrderCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = OrderForm
    template_name = "orders/form.html"
    def get_success_message(self, cleaned_data):
        # tracking_code فیلد فرم نیست؛ پس از self.object می‌خوانیم
        return f"سفارش {self.object.tracking_code} با موفقیت ثبت شد."

    def form_valid(self, form):
        form.instance.customer = self.request.user.customer
        return super().form_valid(form)     # ذخیره + redirect به get_absolute_url</code></pre>
<h3>صفحه‌بندی در قالب</h3>
<pre><code class="language-html">{% if page_obj.has_next %}
  &lt;a href="?{% querystring page=page_obj.next_page_number %}"&gt;صفحه‌ی بعد&lt;/a&gt;
{% endif %}
&lt;span&gt;صفحه‌ی {{ page_obj.number }} از {{ page_obj.paginator.num_pages }}&lt;/span&gt;</code></pre>
<p>تگ <code>{% querystring %}</code> (Django 5.1 به بعد) پارامترهای فعلی مثل <code>q</code> را حفظ می‌کند و فقط page را عوض می‌کند؛ قبلاً باید دستی می‌نوشتید و جست‌وجو با رفتن به صفحه‌ی ۲ گم می‌شد.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>mixinهای دسترسی (LoginRequiredMixin، PermissionRequiredMixin) باید <em>سمت چپ</em> کلاس پایه باشند؛ به خاطر MRO پایتون، اگر راست باشند ممکن است View قبل از بررسی دسترسی اجرا شود.</li>
<li>فیلتر امنیتی را در <code>get_queryset</code> بگذارید نه <code>get_object</code>؛ این‌طور DetailView، UpdateView و DeleteView همه خودکار 404 می‌دهند.</li>
<li>اگر <code>success_url</code> تعریف نکنید، CreateView و UpdateView به <code>get_absolute_url</code> شیء ریدایرکت می‌کنند؛ نبود هر دو خطای ImproperlyConfigured می‌دهد.</li>
<li>در urls می‌توانید ویژگی‌ها را بدون زیرکلاس عوض کنید: <code>TemplateView.as_view(template_name="pages/about.html")</code>.</li>
<li>DeleteView از Django 4.0 از <code>FormMixin</code> استفاده می‌کند؛ منطق قبل از حذف را در <code>form_valid</code> بنویسید، نه در <code>delete()</code> که دیگر برای POST صدا زده نمی‌شود.</li>
</ul>""",
                },
                {
                    "title": "قالب‌ها: وراثت، include، context processor، static و media، messages",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>یک base.html، صدها صفحه</h2>
<p>زبان قالب جنگو عمداً محدود است: منطق کسب‌وکار جایش در View و مدل است و قالب فقط نمایش می‌دهد. قدرت اصلی آن <strong>وراثت</strong> است: یک اسکلت پایه با بلوک‌های قابل‌بازنویسی و صفحه‌هایی که فقط بلوک‌های لازم را پر می‌کنند.</p>
<pre><code class="language-html">{# templates/base.html #}
{% load static %}
&lt;!DOCTYPE html&gt;
&lt;html lang="fa" dir="rtl"&gt;
&lt;head&gt;
  &lt;meta charset="utf-8"&gt;
  &lt;meta name="viewport" content="width=device-width, initial-scale=1"&gt;
  &lt;title&gt;{% block title %}{{ site_name }}{% endblock %}&lt;/title&gt;
  &lt;link rel="stylesheet" href="{% static 'css/vazirmatn.css' %}"&gt;
  &lt;link rel="stylesheet" href="{% static 'css/main.css' %}"&gt;
&lt;/head&gt;
&lt;body&gt;
  {% include "partials/navbar.html" %}
  {% for message in messages %}
    &lt;div class="alert alert-{{ message.tags }}"&gt;{{ message }}&lt;/div&gt;
  {% endfor %}
  &lt;main&gt;{% block content %}{% endblock %}&lt;/main&gt;
  {% block scripts %}{% endblock %}
&lt;/body&gt;
&lt;/html&gt;

{# templates/orders/detail.html #}
{% extends "base.html" %}
{% block title %}سفارش {{ order.tracking_code }} | {{ block.super }}{% endblock %}
{% block content %}
  &lt;h1&gt;سفارش {{ order.tracking_code }}&lt;/h1&gt;
  &lt;p&gt;وضعیت: {{ order.get_status_display }}&lt;/p&gt;
  {% include "orders/_items_table.html" with items=order.items.all only %}
{% endblock %}</code></pre>
<h3>context processor: داده‌ای که همه‌ی صفحه‌ها لازم دارند</h3>
<p>نام سایت، تعداد اقلام سبد یا شماره‌ی پشتیبانی را نباید در هر View به context اضافه کرد. یک تابع ساده بنویسید و در <code>TEMPLATES["OPTIONS"]["context_processors"]</code> ثبت کنید:</p>
<pre><code class="language-python"># apps/core/context_processors.py
from django.conf import settings

def site(request):
    return {
        "site_name": "فرش کاشان",
        "support_phone": settings.SUPPORT_PHONE,
    }</code></pre>
<h3>static در برابر media</h3>
<table><thead><tr><th></th><th>static</th><th>media</th></tr></thead><tbody>
<tr><td>منبع</td><td>توسعه‌دهنده (CSS، JS، فونت، لوگو)</td><td>کاربر (عکس محصول، فایل آپلودی)</td></tr>
<tr><td>تنظیمات</td><td><code>STATIC_URL</code>، <code>STATIC_ROOT</code>، <code>STATICFILES_DIRS</code></td><td><code>MEDIA_URL</code>، <code>MEDIA_ROOT</code></td></tr>
<tr><td>در git</td><td>بله</td><td>هرگز</td></tr>
<tr><td>در سرور</td><td>collectstatic + WhiteNoise یا nginx</td><td>nginx مستقیم</td></tr>
<tr><td>در قالب</td><td><code>{% static 'css/main.css' %}</code></td><td><code>{{ carpet.image.url }}</code></td></tr>
</tbody></table>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>{% include ... with x=1 only %}</code> قالب فرعی را فقط با همان متغیرها رندر می‌کند؛ هم سریع‌تر است هم جلوی وابستگی پنهان به متغیرهای صفحه‌ی مادر را می‌گیرد.</li>
<li>جنگو همه‌ی متغیرها را خودکار escape می‌کند؛ فیلتر <code>|safe</code> روی داده‌ی کاربر یعنی باز کردن در XSS. اگر HTML کاربر لازم است، قبل از ذخیره با یک sanitizer مثل nh3 پاکش کنید.</li>
<li>context processorها برای <em>هر</em> رندر اجرا می‌شوند؛ کوئری سنگین در آن‌ها همه‌ی صفحات را کند می‌کند. یا کش کنید یا یک تابع lazy برگردانید که فقط در صورت استفاده اجرا شود.</li>
<li>با گذاشتن <code>"string_if_invalid": "!!%s!!"</code> در OPTIONS قالب (فقط در توسعه) متغیرهای غلط‌املایی به‌جای رشته‌ی خالی با علامت دیده می‌شوند.</li>
<li>تگ <code>{% url 'orders:list' as list_url %}</code> اگر url پیدا نشود خطا نمی‌دهد و فقط متغیر را خالی می‌گذارد؛ برای لینک‌های اختیاری مفید است.</li>
</ul>""",
                },
                {
                    "title": "تگ و فیلتر سفارشی: تاریخ شمسی، ارقام فارسی و قیمت تومانی",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>قالب فارسی بدون تکرار کد</h2>
<p>در هر سایت ایرانی سه نیاز نمایشی همیشگی داریم: تاریخ شمسی، ارقام فارسی و مبلغ به تومان با جداکننده‌ی هزارگان. جای این منطق نه در مدل است نه در View؛ جایش <strong>فیلتر قالب</strong> است. فیلترها و تگ‌های سفارشی در پوشه‌ی <code>templatetags</code> یک اپ قرار می‌گیرند (با <code>__init__.py</code>) و نام فایل، نام کتابخانه برای <code>{% load %}</code> است.</p>
<pre><code class="language-python"># apps/core/templatetags/persian.py
import datetime

import jdatetime
from django import template
from django.utils import timezone

register = template.Library()

FA_DIGITS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
MONTHS = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور",
          "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]


@register.filter
def fa_digits(value):
    return str(value).translate(FA_DIGITS)


@register.filter
def jdate(value, fmt="%Y/%m/%d"):
    if not value:
        return ""
    if isinstance(value, datetime.datetime):
        if timezone.is_aware(value):
            value = timezone.localtime(value)          # UTC به وقت تهران
        j = jdatetime.datetime.fromgregorian(datetime=value)
    else:
        j = jdatetime.date.fromgregorian(date=value)
    return j.strftime(fmt).translate(FA_DIGITS)


@register.filter
def jdate_long(value):
    if not value:
        return ""
    if isinstance(value, datetime.datetime):
        value = timezone.localtime(value).date()
    j = jdatetime.date.fromgregorian(date=value)
    return f"{j.day} {MONTHS[j.month - 1]} {j.year}".translate(FA_DIGITS)


@register.filter
def toman(rial):
    try:
        return f"{int(rial) // 10:,}".replace(",", "٬").translate(FA_DIGITS) + " تومان"
    except (TypeError, ValueError):
        return ""


@register.simple_tag(takes_context=True)
def active(context, url_name):
    match = context["request"].resolver_match
    return "active" if match and match.view_name == url_name else ""</code></pre>
<pre><code class="language-html">{% load persian %}
&lt;p&gt;تاریخ ثبت: {{ order.created_at|jdate:"%Y/%m/%d %H:%M" }}&lt;/p&gt;
&lt;p&gt;تحویل: {{ order.delivery_date|jdate_long }}&lt;/p&gt;       {# ۱۵ بهمن ۱۴۰۴ #}
&lt;p&gt;مبلغ: {{ order.total|toman }}&lt;/p&gt;                      {# ۱۲٬۵۰۰٬۰۰۰ تومان #}
&lt;a class="{% active 'orders:list' %}" href="{% url 'orders:list' %}"&gt;سفارش‌ها&lt;/a&gt;</code></pre>
<h3>inclusion_tag: یک تکه‌ی قالب قابل‌استفاده‌ی مجدد</h3>
<pre><code class="language-python">@register.inclusion_tag("orders/_status_badge.html")
def status_badge(order):
    colors = {"pending": "warning", "paid": "info", "shipped": "success", "cancelled": "secondary"}
    return {"label": order.get_status_display(), "color": colors.get(order.status, "light")}</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>بعد از ساختن پوشه‌ی templatetags باید runserver را از نو اجرا کنید؛ کتابخانه‌های قالب فقط هنگام شروع ثبت می‌شوند و تا آن موقع خطای «is not a registered tag library» می‌گیرید.</li>
<li>اگر کتابخانه‌ای را در همه‌ی قالب‌ها لازم دارید، آن را در <code>TEMPLATES["OPTIONS"]["builtins"] = ["apps.core.templatetags.persian"]</code> بگذارید تا دیگر <code>{% load %}</code> لازم نباشد.</li>
<li>تبدیل تاریخ aware به شمسی بدون <code>timezone.localtime</code> زمان UTC را نشان می‌دهد؛ سفارش ساعت ۲ بامداد تهران در روز «قبل» نمایش داده می‌شود.</li>
<li>جداکننده‌ی هزارگان فارسی کاراکتر «٬» (U+066C) است نه ویرگول لاتین؛ در متن راست‌به‌چپ ویرگول لاتین گاهی جای عدد را به‌هم می‌ریزد.</li>
<li>فیلترها را برای ورودی نامعتبر مقاوم بنویسید (مثل try در toman)؛ خطای یک فیلتر کل صفحه را با 500 از کار می‌اندازد.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۵ ─────────────────────────────
        {
            "title": "فصل ۵: فرم‌ها و اعتبارسنجی — ورودی امن و فارسی",
            "lessons": [
                {
                    "title": "Form و ModelForm: چرخه‌ی اعتبارسنجی، cleaned_data و widgetها",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>فرم جنگو فقط HTML نیست</h2>
<p>فرم جنگو سه کار را با هم انجام می‌دهد: HTML فیلدها را می‌سازد، داده‌ی ورودی را از رشته به نوع درست پایتون تبدیل می‌کند (رشته‌ی «1200» به عدد 1200، رشته‌ی تاریخ به <code>date</code>) و آن را اعتبارسنجی می‌کند. هرگز مستقیماً از <code>request.POST</code> داده برندارید و ذخیره نکنید؛ همیشه از <code>form.cleaned_data</code> بخوانید.</p>
<h3>فرم ساده و ModelForm</h3>
<pre><code class="language-python"># apps/orders/forms.py
from django import forms
from .models import Order


class ContactForm(forms.Form):
    name = forms.CharField(label="نام و نام خانوادگی", max_length=80)
    mobile = forms.CharField(label="موبایل", max_length=15)
    message = forms.CharField(label="پیام", widget=forms.Textarea(attrs={"rows": 4}))


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["delivery_date", "address", "note"]        # فهرست صریح؛ هرگز "__all__"
        labels = {"note": "توضیحات برای کارگاه"}
        help_texts = {"delivery_date": "حداقل ۱۰ روز کاری بعد از ثبت"}
        widgets = {
            "note": forms.Textarea(attrs={"rows": 3}),
            "address": forms.TextInput(attrs={"autocomplete": "street-address"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault("class", "form-control")</code></pre>
<h3>الگوی استاندارد View</h3>
<pre><code class="language-python">def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)          # فرم «bound»
        if form.is_valid():
            send_contact_email(**form.cleaned_data)
            messages.success(request, "پیام شما دریافت شد.")
            return redirect("pages:contact")
    else:
        form = ContactForm()                      # فرم «unbound»
    return render(request, "pages/contact.html", {"form": form})</code></pre>
<h3>ترتیب اعتبارسنجی</h3>
<p>وقتی <code>is_valid()</code> را صدا می‌زنید، این مراحل اجرا می‌شود:</p>
<ol>
<li>برای هر فیلد: <code>to_python()</code> (تبدیل نوع)، <code>validate()</code> (الزامی بودن و…)، <code>run_validators()</code> (max_length و validatorهای اضافه).</li>
<li>برای هر فیلد: متد <code>clean_&lt;field&gt;()</code> فرم، اگر تعریف شده باشد.</li>
<li>متد <code>clean()</code> کل فرم، برای قواعدی که به چند فیلد وابسته‌اند.</li>
<li>در ModelForm: ساختن instance و اجرای <code>full_clean()</code> مدل، یعنی <code>clean()</code> مدل و قیدهای unique و constraints.</li>
</ol>
<p>در قالب ساده‌ترین حالت <code>{{ form }}</code> است که از Django 5.0 خروجی مبتنی بر div تولید می‌کند. برای کنترل بیشتر هر فیلد را جدا رندر کنید: <code>{{ form.mobile.as_field_group }}</code> برچسب، ویجت، راهنما و خطا را با هم می‌آورد.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>fields = "__all__"</code> یا <code>exclude</code> در ModelForm یعنی اگر فردا فیلد <code>is_approved</code> یا <code>discount</code> به مدل اضافه شود، کاربر می‌تواند با دستکاری HTML آن را هم بفرستد (mass assignment). همیشه فهرست صریح بنویسید.</li>
<li><code>form.save(commit=False)</code> شیء را بدون ذخیره برمی‌گرداند تا فیلدهای سمت سرور (مثل customer) را پر کنید؛ اگر فرم فیلد ManyToMany دارد، بعد از save خودتان <code>form.save_m2m()</code> را صدا بزنید.</li>
<li><code>initial</code> فقط مقدار نمایشی فرم unbound است؛ اگر فرم را با داده‌ی POST بسازید، initial نادیده گرفته می‌شود و فیلدی که ارسال نشده خالی حساب می‌شود.</li>
<li><code>form.has_changed()</code> و <code>form.changed_data</code> می‌گویند کاربر دقیقاً کدام فیلدها را عوض کرده است؛ برای ثبت تاریخچه‌ی تغییرات یا ارسال اعلان عالی است.</li>
<li>ویجت <code>DateInput(attrs={"type": "date"})</code> تقویم میلادی مرورگر را نشان می‌دهد؛ برای کاربر ایرانی یک datepicker شمسی محلی (بدون CDN) بگذارید و مقدار را قبل از اعتبارسنجی به میلادی برگردانید.</li>
</ul>""",
                },
                {
                    "title": "اعتبارسنجی سفارشی و فرم فارسی: ارقام فارسی، موبایل و کد ملی",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>کاربر ایرانی «۰۹۱۲» تایپ می‌کند</h2>
<p>بیشتر کاربران گوشی با کیبورد فارسی عدد وارد می‌کنند. رقم «۵» فارسی (U+06F5) با «5» لاتین فرق دارد و RegexValidator با <code>\d</code> در پایتون آن را قبول می‌کند اما پایگاه داده آن را همان‌طور ذخیره می‌کند؛ نتیجه: دو کاربر با یک موبایل، جست‌وجوهایی که پیدا نمی‌کنند و پیامکی که نمی‌رسد. راه درست این است که ورودی را <em>قبل از هر اعتبارسنجی</em> نرمال کنیم؛ یعنی در <code>to_python</code> یک فیلد فرم اختصاصی.</p>
<pre><code class="language-python"># apps/core/forms_fa.py
import re

from django import forms
from django.core.exceptions import ValidationError

DIGITS = str.maketrans("۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩", "01234567890123456789")
ARABIC_LETTERS = str.maketrans({"ي": "ی", "ك": "ک", "ى": "ی"})


def normalize_digits(value):
    return (value or "").translate(DIGITS).strip()


def normalize_text(value):
    return re.sub(r"\s+", " ", (value or "").translate(ARABIC_LETTERS)).strip()


class MobileField(forms.CharField):
    default_error_messages = {"invalid": "شماره‌ی موبایل معتبر نیست؛ مثال: 09121234567"}

    def to_python(self, value):
        value = re.sub(r"[\s\-()]", "", normalize_digits(super().to_python(value)))
        if value.startswith("+98"):
            value = "0" + value[3:]
        elif value.startswith("0098"):
            value = "0" + value[4:]
        elif value.startswith("9") and len(value) == 10:
            value = "0" + value
        return value

    def validate(self, value):
        super().validate(value)
        if value and not re.fullmatch(r"09\d{9}", value):
            raise ValidationError(self.error_messages["invalid"], code="invalid")


def validate_national_code(value):
    code = normalize_digits(value)
    if not re.fullmatch(r"\d{10}", code) or len(set(code)) == 1:
        raise ValidationError("کد ملی باید ۱۰ رقم معتبر باشد.", code="invalid")
    check = int(code[9])
    s = sum(int(code[i]) * (10 - i) for i in range(9)) % 11
    if (s &lt; 2 and check != s) or (s &gt;= 2 and check != 11 - s):
        raise ValidationError("کد ملی نامعتبر است.", code="checksum")</code></pre>
<h3>استفاده در ModelForm با clean_ و clean</h3>
<pre><code class="language-python">class CustomerForm(forms.ModelForm):
    mobile = MobileField(label="موبایل")
    national_code = forms.CharField(label="کد ملی", required=False)

    class Meta:
        model = Customer
        fields = ["full_name", "mobile", "national_code", "city"]

    def clean_full_name(self):
        return normalize_text(self.cleaned_data["full_name"])

    def clean_national_code(self):
        code = normalize_digits(self.cleaned_data.get("national_code"))
        if code:
            validate_national_code(code)
        return code

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("city") == "خارج از کشور" and not cleaned.get("national_code"):
            self.add_error("national_code", "برای ارسال خارجی کد ملی الزامی است.")
        return cleaned</code></pre>
<p>الگوریتم کد ملی: ۹ رقم اول را به‌ترتیب در ۱۰ تا ۲ ضرب و جمع کنید، باقیمانده بر ۱۱ را حساب کنید؛ اگر کمتر از ۲ بود رقم کنترل باید خودش باشد، وگرنه ۱۱ منهای آن. کدهایی مثل «۱۱۱۱۱۱۱۱۱۱» از نظر ریاضی درست‌اند اما نامعتبرند؛ برای همین <code>len(set(code)) == 1</code> را رد می‌کنیم.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>اگر نرمال‌سازی را در <code>clean_mobile</code> بگذارید دیر است: <code>max_length=11</code> قبل از آن اجرا شده و «+989121234567» را با خطای طول رد کرده است. جای نرمال‌سازی <code>to_python</code> است.</li>
<li><code>\d</code> در regex پایتون ارقام فارسی و عربی را هم تطبیق می‌دهد (یونیکد)؛ اگر فقط لاتین می‌خواهید <code>[0-9]</code> بنویسید یا پرچم <code>re.ASCII</code> بدهید.</li>
<li><code>clean()</code> حتی وقتی فیلدها خطا دارند اجرا می‌شود؛ پس همیشه با <code>cleaned.get()</code> بخوانید نه <code>cleaned[...]</code>، وگرنه KeyError می‌گیرید.</li>
<li><code>add_error(None, "...")</code> خطای کلی فرم (non_field_errors) می‌سازد و در قالب با <code>{{ form.non_field_errors }}</code> نمایش داده می‌شود.</li>
<li>نرمال‌سازی «ي» و «ك» عربی را هم در ذخیره و هم در عبارت جست‌وجو انجام دهید؛ اگر فقط یکی را درست کنید، جست‌وجو همچنان رکوردهای قدیمی را پیدا نمی‌کند.</li>
</ul>""",
                },
                {
                    "title": "Formset و Inline Formset: سفارش با چند قلم در یک صفحه",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>یک فرم، چند ردیف</h2>
<p>فاکتور سفارش فرش یک سربرگ دارد (مشتری، تاریخ تحویل) و چند ردیف قلم (طرح، ابعاد، تعداد). ساختن این صفحه با فرم‌های جدا و نام‌گذاری دستی فیلدها کابوس است. <strong>Formset</strong> مجموعه‌ای از فرم‌های هم‌شکل را مدیریت می‌کند و <strong>Inline Formset</strong> همین کار را برای اشیای وابسته به یک والد (ForeignKey) انجام می‌دهد: ساخت، ویرایش و حذف ردیف‌ها با یک فرم.</p>
<pre><code class="language-python"># apps/orders/forms.py
from django import forms
from django.forms import BaseInlineFormSet, inlineformset_factory
from .models import Order, OrderItem


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ["carpet", "quantity"]           # unit_price عمداً نیست؛ سرور تعیین می‌کند


class BaseItemFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        seen = set()
        for form in self.forms:
            if not form.cleaned_data or form.cleaned_data.get("DELETE"):
                continue
            carpet = form.cleaned_data["carpet"]
            if carpet in seen:
                raise forms.ValidationError("هر طرح فقط یک بار در سفارش بیاید؛ تعداد را زیاد کنید.")
            seen.add(carpet)


OrderItemFormSet = inlineformset_factory(
    Order, OrderItem, form=OrderItemForm, formset=BaseItemFormSet,
    extra=1, can_delete=True, min_num=1, validate_min=True, max_num=20,
)</code></pre>
<h3>View</h3>
<pre><code class="language-python">@login_required
def order_edit(request, pk):
    order = get_object_or_404(Order, pk=pk, customer__user=request.user, status="pending")
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        formset = OrderItemFormSet(request.POST, instance=order, prefix="items")
        if form.is_valid() and formset.is_valid():
            with transaction.atomic():
                form.save()
                items = formset.save(commit=False)
                for obj in formset.deleted_objects:
                    obj.delete()
                for item in items:
                    item.unit_price = item.carpet.price          # قیمت از سرور
                    item.save()
                order.recalculate_total()
            return redirect(order)
    else:
        form = OrderForm(instance=order)
        formset = OrderItemFormSet(instance=order, prefix="items")
    return render(request, "orders/edit.html", {"form": form, "formset": formset})</code></pre>
<h3>قالب</h3>
<pre><code class="language-html">&lt;form method="post"&gt;
  {% csrf_token %}
  {{ form.as_div }}
  {{ formset.management_form }}
  {{ formset.non_form_errors }}
  &lt;table id="items"&gt;
    {% for f in formset %}
      &lt;tr&gt;{{ f.id }}&lt;td&gt;{{ f.carpet }}&lt;/td&gt;&lt;td&gt;{{ f.quantity }}&lt;/td&gt;&lt;td&gt;{{ f.DELETE }}&lt;/td&gt;&lt;/tr&gt;
    {% endfor %}
  &lt;/table&gt;
  &lt;template id="empty-row"&gt;&lt;tr&gt;{{ formset.empty_form.id }}&lt;td&gt;{{ formset.empty_form.carpet }}&lt;/td&gt;&lt;td&gt;{{ formset.empty_form.quantity }}&lt;/td&gt;&lt;/tr&gt;&lt;/template&gt;
  &lt;button type="submit"&gt;ذخیره&lt;/button&gt;
&lt;/form&gt;</code></pre>
<p>برای دکمه‌ی «افزودن ردیف» با جاوااسکریپت، محتوای <code>empty_form</code> را کپی کنید، رشته‌ی <code>__prefix__</code> را با شماره‌ی ردیف جایگزین کنید و مقدار فیلد مخفی <code>items-TOTAL_FORMS</code> را یکی زیاد کنید.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>فراموش کردن <code>{{ formset.management_form }}</code> خطای «ManagementForm data is missing or has been tampered with» می‌دهد؛ پرتکرارترین باگ formset.</li>
<li>فیلد مخفی <code>{{ f.id }}</code> را در هر ردیف رندر کنید؛ بدونش جنگو ردیف‌های موجود را «جدید» می‌بیند و در هر ذخیره اقلام تکراری ساخته می‌شود.</li>
<li>الگوی رایج <code>Form(request.POST or None)</code> یک دام دارد: POST بدون هیچ فیلد (مثلاً فقط یک دکمه) یک QueryDict خالی و falsy است و فرم unbound می‌ماند؛ در formsetها صریحاً <code>request.method</code> را بررسی کنید.</li>
<li><code>max_num</code> فقط تعداد ردیف‌های نمایشی را محدود می‌کند؛ سقف امنیتی واقعی <code>absolute_max</code> است (پیش‌فرض max_num + 1000) که جلوی ارسال هزاران فرم جعلی را می‌گیرد.</li>
<li>اگر دو formset در یک صفحه دارید، <code>prefix</code> متفاوت الزامی است؛ وگرنه نام فیلدها تداخل می‌کند و داده‌ی یکی در دیگری می‌نشیند.</li>
</ul>""",
                },
                {
                    "title": "آپلود فایل: ImageField، upload_to، محدودیت حجم و نوع",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>فایل کاربر را هرگز باور نکنید</h2>
<p>آپلود فایل یکی از پرخطرترین بخش‌های هر سامانه است: فایل حجیمی که دیسک را پر می‌کند، «عکسی» که در واقع اسکریپت است، نام فایلی با <code>../</code> یا حروف فارسی که روی سرور مشکل می‌سازد. جنگو ابزار کافی دارد، به شرط این‌که درست کنار هم گذاشته شوند.</p>
<h3>تنظیمات پایه</h3>
<pre><code class="language-python"># settings.py
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
DATA_UPLOAD_MAX_MEMORY_SIZE = 5 * 1024 * 1024      # سقف بدنه‌ی درخواست بدون احتساب فایل‌ها
FILE_UPLOAD_MAX_MEMORY_SIZE = 2 * 1024 * 1024      # بزرگ‌تر از این روی دیسک موقت می‌رود
FILE_UPLOAD_PERMISSIONS = 0o644</code></pre>
<h3>مدل با اعتبارسنجی حجم و نوع</h3>
<pre><code class="language-python"># apps/catalog/models.py
from pathlib import Path
from uuid import uuid4

from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models

MAX_IMAGE_MB = 3


def carpet_image_path(instance, filename):
    ext = Path(filename).suffix.lower()
    return f"carpets/{instance.carpet.code}/{uuid4().hex}{ext}"   # نام تصادفی لاتین


def validate_image_size(f):
    if f.size &gt; MAX_IMAGE_MB * 1024 * 1024:
        raise ValidationError(f"حجم تصویر حداکثر {MAX_IMAGE_MB} مگابایت است.")


class CarpetImage(models.Model):
    carpet = models.ForeignKey("catalog.Carpet", on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(
        "تصویر",
        upload_to=carpet_image_path,
        validators=[FileExtensionValidator(["jpg", "jpeg", "png", "webp"]), validate_image_size],
    )
    alt = models.CharField(max_length=150, blank=True)</code></pre>
<p><code>ImageField</code> به کتابخانه‌ی Pillow نیاز دارد و فایل را واقعاً به‌عنوان تصویر باز می‌کند؛ فایل متنی که پسوند jpg گرفته رد می‌شود. پسوند را هم جدا بررسی می‌کنیم چون Pillow فرمت‌هایی را هم می‌شناسد که نمی‌خواهید (مثل TIFF و فرمت‌های کمتر امن).</p>
<h3>فرم و View</h3>
<pre><code class="language-html">&lt;form method="post" enctype="multipart/form-data"&gt;
  {% csrf_token %}
  {{ form.as_div }}
  &lt;button&gt;بارگذاری&lt;/button&gt;
&lt;/form&gt;</code></pre>
<pre><code class="language-python">form = CarpetImageForm(request.POST, request.FILES)   # FILES را فراموش نکنید</code></pre>
<p>در توسعه، سرو فایل‌های media با <code>static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)</code> در urls انجام می‌شود (درس ۱۶)؛ در سرور nginx مستقیم آن‌ها را سرو می‌کند و در nginx هم باید <code>client_max_body_size</code> را متناسب تنظیم کنید.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>FILE_UPLOAD_MAX_MEMORY_SIZE</code> حجم فایل را محدود <em>نمی‌کند</em>؛ فقط آستانه‌ی رفتن از حافظه به فایل موقت است. سقف واقعی را validator و <code>client_max_body_size</code> در nginx تعیین می‌کنند.</li>
<li>بدون <code>enctype="multipart/form-data"</code> مرورگر فقط نام فایل را می‌فرستد و فرم با خطای «این فیلد لازم است» برمی‌گردد؛ گیج‌کننده‌ترین باگ آپلود.</li>
<li>حذف رکورد مدل فایل را از دیسک پاک نمی‌کند (عمداً، به‌خاطر تراکنش‌ها)؛ برای پاک‌سازی از <code>transaction.on_commit</code> در سیگنال post_delete یا یک دستور مدیریتی دوره‌ای استفاده کنید.</li>
<li><code>content_type</code> فایل آپلودی را مرورگر اعلام می‌کند و قابل جعل است؛ هرگز به آن برای امنیت تکیه نکنید.</li>
<li>فایل‌های خصوصی (فاکتور، قرارداد) را در MEDIA عمومی نگذارید؛ آن‌ها را بیرون از ریشه‌ی وب ذخیره و از طریق یک View با بررسی دسترسی و هدر <code>X-Accel-Redirect</code> nginx تحویل دهید.</li>
</ul>""",
                },
                {
                    "title": "CSRF و فرم‌های AJAX: چرا هرگز csrf_exempt",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>حمله‌ای که از سایت دیگری می‌آید</h2>
<p>فرض کنید کاربر در سایت شما لاگین است و در تب دیگری یک صفحه‌ی مخرب را باز می‌کند. آن صفحه می‌تواند یک فرم مخفی بسازد که به <code>/orders/42/cancel/</code> شما POST شود؛ مرورگر کوکی Session را هم خودکار می‌فرستد و از دید سرور، خود کاربر درخواست را داده است. این <strong>CSRF</strong> است. جنگو با <code>CsrfViewMiddleware</code> از همه‌ی درخواست‌های «ناامن» (POST، PUT، PATCH، DELETE) یک توکن می‌خواهد که سایت مهاجم نمی‌تواند بخواند؛ روی HTTPS هم هدر Origin یا Referer را با دامنه‌ی شما مقایسه می‌کند.</p>
<h3>چرا csrf_exempt راه‌حل نیست</h3>
<p>وقتی AJAX با خطای 403 برمی‌گردد، ساده‌ترین «راه‌حل» گذاشتن <code>@csrf_exempt</code> است؛ یعنی دقیقاً همان در را برای مهاجم باز کردن. تنها جای مشروع آن وب‌هوک‌هایی است که از سرور دیگری (مثلاً درگاه پرداخت) می‌آیند و با امضا یا توکن دیگری احراز می‌شوند.</p>
<h3>AJAX درست با fetch</h3>
<pre><code class="language-html">&lt;form id="quote-form" method="post" action="{% url 'orders:quote' %}"&gt;
  {% csrf_token %}
  {{ form.as_div }}
  &lt;button type="submit"&gt;محاسبه‌ی قیمت&lt;/button&gt;
  &lt;div id="result"&gt;&lt;/div&gt;
&lt;/form&gt;</code></pre>
<pre><code class="language-javascript">const form = document.getElementById("quote-form");
form.addEventListener("submit", async (e) =&gt; {
  e.preventDefault();
  const token = form.querySelector("[name=csrfmiddlewaretoken]").value;
  const resp = await fetch(form.action, {
    method: "POST",
    headers: { "X-CSRFToken": token, "X-Requested-With": "fetch" },
    body: new FormData(form),
  });
  const data = await resp.json();
  const box = document.getElementById("result");
  box.textContent = data.ok ? `مبلغ: ${data.price_toman} تومان` : "لطفاً خطاهای فرم را اصلاح کنید.";
});</code></pre>
<pre><code class="language-python">@require_POST
def quote(request):
    form = QuoteForm(request.POST)
    if form.is_valid():
        price = calculate_price(**form.cleaned_data)
        return JsonResponse({"ok": True, "price_toman": f"{price // 10:,}"})
    return JsonResponse({"ok": False, "errors": form.errors.get_json_data()}, status=400)</code></pre>
<p><code>form.errors.get_json_data()</code> خطاها را به شکل ساختاریافته (پیام و کد برای هر فیلد) برمی‌گرداند تا جاوااسکریپت بتواند هر خطا را کنار فیلد خودش نشان دهد.</p>
<h3>CSRF پشت nginx و HTTPS</h3>
<pre><code class="language-python">CSRF_TRUSTED_ORIGINS = ["https://example.ir", "https://www.example.ir"]   # با scheme
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>از Django 4.0 مقادیر <code>CSRF_TRUSTED_ORIGINS</code> باید با scheme باشند (<code>https://</code>)؛ نوشتن فقط دامنه همان 403 معروف «Origin checking failed» را پشت پراکسی می‌سازد.</li>
<li>اگر صفحه هیچ <code>{% csrf_token %}</code> ندارد اما جاوااسکریپت آن POST می‌زند، دکوراتور <code>@ensure_csrf_cookie</code> روی View صفحه کوکی توکن را حتماً ست می‌کند.</li>
<li>با <code>CSRF_FAILURE_VIEW</code> می‌توانید به‌جای صفحه‌ی انگلیسی پیش‌فرض، یک صفحه‌ی فارسی بسازید که توضیح دهد «صفحه را رفرش کنید»؛ کاربرانی که فرم را ساعت‌ها باز گذاشته‌اند سپاس‌گزار می‌شوند.</li>
<li>هر درخواست GET باید بی‌اثر باشد؛ CSRF فقط از متدهای ناامن محافظت می‌کند، پس لینک GET که سفارش را لغو کند با هیچ توکنی امن نمی‌شود.</li>
<li>در DRF، <code>SessionAuthentication</code> فقط برای کاربران لاگین‌شده CSRF را اجبار می‌کند؛ پس فرم AJAX مهمان بدون توکن کار می‌کند اما پس از لاگین ناگهان 403 می‌دهد.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۶ ─────────────────────────────
        {
            "title": "فصل ۶: ادمین، احراز هویت و دسترسی",
            "lessons": [
                {
                    "title": "شخصی‌سازی ModelAdmin: list_display، list_filter، search_fields و کارایی",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>ادمین جنگو؛ پنل اداری رایگان</h2>
<p>ادمین جنگو برای کارمندان داخلی ساخته شده، نه مشتریان. با چند خط تنظیم، واحد فروش می‌تواند سفارش‌ها را جست‌وجو، فیلتر و ویرایش کند و شما هفته‌ها زمان ساخت پنل را ذخیره می‌کنید. اما ادمین پیش‌فرض روی جدول‌های بزرگ کند و بی‌استفاده است؛ شخصی‌سازی درست تفاوت را می‌سازد.</p>
<pre><code class="language-python"># apps/orders/admin.py
from django.contrib import admin
from django.db.models import Count

from apps.core.templatetags.persian import jdate, toman
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("tracking_code", "customer", "status", "total_display", "items_count", "created_jalali")
    list_display_links = ("tracking_code",)
    list_filter = ("status", "customer__city", ("created_at", admin.DateFieldListFilter))
    search_fields = ("=tracking_code", "customer__full_name", "^customer__user__mobile")
    list_select_related = ("customer",)
    list_per_page = 50
    readonly_fields = ("tracking_code", "total", "created_at")
    ordering = ("-created_at",)
    show_facets = admin.ShowFacets.ALWAYS          # تعداد کنار هر فیلتر (Django 5.0+)
    fieldsets = (
        ("اطلاعات سفارش", {"fields": ("tracking_code", "customer", "status")}),
        ("مالی", {"fields": ("total", "discount")}),
        ("زمان‌ها", {"fields": ("delivery_date", "created_at"), "classes": ("collapse",)}),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(_items=Count("items"))

    @admin.display(description="مبلغ", ordering="total")
    def total_display(self, obj):
        return toman(obj.total)

    @admin.display(description="تعداد اقلام", ordering="_items")
    def items_count(self, obj):
        return obj._items

    @admin.display(description="تاریخ ثبت", ordering="created_at")
    def created_jalali(self, obj):
        return jdate(obj.created_at, "%Y/%m/%d %H:%M")</code></pre>
<h3>چه چیزی چه می‌کند</h3>
<table><thead><tr><th>گزینه</th><th>اثر</th></tr></thead><tbody>
<tr><td>list_display</td><td>ستون‌های فهرست؛ فیلد، متد یا تابع</td></tr>
<tr><td>list_filter</td><td>فیلترهای کناری؛ روی رابطه‌ها هم با <code>__</code></td></tr>
<tr><td>search_fields</td><td>کادر جست‌وجو؛ پیشوند <code>=</code> تطابق دقیق، <code>^</code> شروع‌شدن</td></tr>
<tr><td>list_select_related</td><td>جلوگیری از N+1 برای ستون‌های ForeignKey</td></tr>
<tr><td>readonly_fields</td><td>نمایش بدون امکان ویرایش؛ متدها را هم می‌پذیرد</td></tr>
<tr><td>fieldsets</td><td>گروه‌بندی فرم ویرایش؛ <code>collapse</code> برای بخش جمع‌شونده</td></tr>
</tbody></table>
<h3>ستون محاسبه‌شده بدون N+1</h3>
<p>اگر در <code>items_count</code> بنویسید <code>obj.items.count()</code>، برای هر ردیف یک کوئری می‌زند: پنجاه ردیف یعنی پنجاه کوئری. با annotate در <code>get_queryset</code> همه در یک کوئری حساب می‌شود و <code>ordering="_items"</code> ستون را قابل مرتب‌سازی هم می‌کند.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>search_fields</code> بدون پیشوند از <code>icontains</code> روی همه‌ی فیلدها با OR استفاده می‌کند؛ روی جدول میلیونی کند است. برای کد و موبایل <code>=</code> یا <code>^</code> بگذارید تا ایندکس استفاده شود.</li>
<li>برای جدول‌های خیلی بزرگ، <code>show_full_result_count = False</code> کوئری COUNT کامل «از ۳٬۲۰۰٬۰۰۰» را حذف می‌کند و صفحه‌ی جست‌وجو چند برابر سریع‌تر می‌شود.</li>
<li><code>date_hierarchy</code> ادمین بر اساس ماه‌های میلادی کار می‌کند؛ برای کاربر ایرانی یک <code>SimpleListFilter</code> سفارشی با بازه‌های «امروز، این هفته، این ماه شمسی» مفیدتر است.</li>
<li><code>list_editable</code> ویرایش درجا در فهرست را ممکن می‌کند، اما هر فیلد list_editable باید در list_display باشد و نمی‌تواند اولین ستون (لینک) باشد.</li>
<li>عنوان‌های ادمین را با <code>admin.site.site_header</code>، <code>site_title</code> و <code>index_title</code> فارسی کنید؛ یک خط در admin.py هر اپ یا در urls.</li>
</ul>""",
                },
                {
                    "title": "ادمین پیشرفته: inlines، actions، autocomplete و ادمین فارسی",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>از فهرست ساده تا ابزار کار روزانه</h2>
<p>کارمند فروش باید اقلام سفارش را همان‌جا ببیند، ده سفارش را با یک کلیک «ارسال‌شده» کند و بین دو هزار طرح فرش با تایپ چند حرف انتخاب کند. سه ابزار این‌ها را ممکن می‌کنند: <strong>inline</strong>، <strong>action</strong> و <strong>autocomplete</strong>.</p>
<pre><code class="language-python">from django.contrib import admin, messages
from django.db import transaction

from apps.catalog.models import Carpet
from .models import Order, OrderItem


@admin.register(Carpet)
class CarpetAdmin(admin.ModelAdmin):
    search_fields = ("code", "name")          # برای autocomplete الزامی است
    list_display = ("code", "name", "density", "price", "stock")


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    autocomplete_fields = ("carpet",)
    readonly_fields = ("unit_price",)


@admin.action(description="علامت‌گذاری به‌عنوان ارسال‌شده", permissions=["change"])
def mark_shipped(modeladmin, request, queryset):
    with transaction.atomic():
        n = queryset.filter(status="paid").update(status="shipped")
    skipped = queryset.count() - n
    modeladmin.message_user(request, f"{n} سفارش ارسال‌شده شد.", messages.SUCCESS)
    if skipped:
        modeladmin.message_user(request, f"{skipped} سفارش پرداخت‌نشده نادیده گرفته شد.", messages.WARNING)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    actions = [mark_shipped]
    autocomplete_fields = ("customer",)

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.status in ("shipped", "cancelled"):
            return [f.name for f in self.model._meta.fields]     # سفارش بسته قفل است
        return ("tracking_code", "total")

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.instance.recalculate_total()                        # بعد از ذخیره‌ی اقلام</code></pre>
<h3>ادمین فارسی و راست‌به‌چپ</h3>
<p>با <code>LANGUAGE_CODE = "fa"</code> ادمین خودکار راست‌به‌چپ و فارسی می‌شود؛ جنگو ترجمه‌ی فارسی رسمی دارد. دو چیز باقی می‌ماند: فونت (با override کردن قالب <code>admin/base_site.html</code> و افزودن یک فایل CSS محلی با فونت Vazirmatn) و تاریخ شمسی (با ستون‌های نمایشی مثل درس قبل یا بسته‌هایی مثل django-jalali). اگر ظاهر مدرن‌تر می‌خواهید، تم‌هایی مثل django-unfold ادمین را بازطراحی می‌کنند و از RTL پشتیبانی دارند؛ همین سایت آموزشی هم با آن ساخته شده است.</p>
<pre><code class="language-html">{# templates/admin/base_site.html #}
{% extends "admin/base_site.html" %}
{% load static %}
{% block extrastyle %}{{ block.super }}
&lt;link rel="stylesheet" href="{% static 'admin/fa.css' %}"&gt;
{% endblock %}</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>autocomplete_fields فقط وقتی کار می‌کند که ModelAdmin مدل مقصد <code>search_fields</code> داشته باشد؛ وگرنه در <code>check</code> خطای admin.E040 می‌گیرید.</li>
<li>action با <code>queryset.update()</code> نه <code>save()</code> مدل را صدا می‌زند نه سیگنال‌ها را؛ اگر ارسال به پیامک یا لاگ تغییرات لازم است، روی اشیا حلقه بزنید یا کار را صریحاً انجام دهید.</li>
<li><code>admin.site.disable_action("delete_selected")</code> حذف گروهی را در کل ادمین غیرفعال می‌کند؛ یکی از رایج‌ترین منشأهای فاجعه‌ی «همه‌ی سفارش‌ها پاک شد».</li>
<li>ادمین با <code>extends "admin/base_site.html"</code> در قالبی با همان نام کار می‌کند چون جنگو قالب‌های پروژه را قبل از قالب‌های اپ admin پیدا می‌کند؛ اپ‌های شما باید در <code>DIRS</code> یا قبل از admin در INSTALLED_APPS باشند.</li>
<li><code>formfield_for_foreignkey</code> اجازه می‌دهد گزینه‌های یک ForeignKey را بر اساس کاربر محدود کنید؛ مثلاً هر نماینده‌ی فروش فقط مشتریان شهر خودش را ببیند.</li>
</ul>""",
                },
                {
                    "title": "احراز هویت: login، logout، تغییر و بازیابی رمز",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>احراز هویت آماده، فقط قالب لازم دارد</h2>
<p>اپ <code>django.contrib.auth</code> همه‌ی Viewهای ورود و خروج و مدیریت رمز را آماده دارد. کافی است urlهای آن را include کنید و قالب‌هایش را بسازید. به لطف Custom User فصل اول، فرم ورود خودش برچسب «موبایل» را به‌جای «نام کاربری» نشان می‌دهد، چون از <code>USERNAME_FIELD</code> می‌خواند.</p>
<pre><code class="language-python"># config/urls.py
urlpatterns += [path("accounts/", include("django.contrib.auth.urls"))]

# settings.py
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "orders:list"
LOGOUT_REDIRECT_URL = "pages:home"
SESSION_COOKIE_AGE = 60 * 60 * 24 * 14        # دو هفته
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",   # pip install argon2-cffi
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
]</code></pre>
<table><thead><tr><th>نام url</th><th>آدرس</th><th>قالب</th></tr></thead><tbody>
<tr><td>login</td><td>accounts/login/</td><td>registration/login.html</td></tr>
<tr><td>logout</td><td>accounts/logout/ (فقط POST)</td><td>registration/logged_out.html</td></tr>
<tr><td>password_change</td><td>accounts/password_change/</td><td>registration/password_change_form.html</td></tr>
<tr><td>password_reset</td><td>accounts/password_reset/</td><td>registration/password_reset_form.html</td></tr>
<tr><td>password_reset_confirm</td><td>accounts/reset/&lt;uidb64&gt;/&lt;token&gt;/</td><td>registration/password_reset_confirm.html</td></tr>
</tbody></table>
<h3>قالب ورود و دکمه‌ی خروج</h3>
<pre><code class="language-html">{# templates/registration/login.html #}
{% extends "base.html" %}
{% block content %}
&lt;form method="post"&gt;
  {% csrf_token %}
  {{ form.as_div }}
  &lt;input type="hidden" name="next" value="{{ next }}"&gt;
  &lt;button type="submit"&gt;ورود&lt;/button&gt;
&lt;/form&gt;
{% endblock %}

{# در navbar: خروج از Django 5.0 فقط با POST #}
&lt;form method="post" action="{% url 'logout' %}"&gt;
  {% csrf_token %}
  &lt;button type="submit"&gt;خروج&lt;/button&gt;
&lt;/form&gt;</code></pre>
<h3>ورود و خروج دستی در کد</h3>
<pre><code class="language-python">from django.contrib.auth import authenticate, login, update_session_auth_hash

user = authenticate(request, mobile="09121234567", password="...")   # یا username=
if user is not None:
    login(request, user)

# بعد از تغییر رمز توسط خود کاربر، تا از Session خارج نشود:
update_session_auth_hash(request, user)</code></pre>
<p>بازیابی رمز پیش‌فرض جنگو با ایمیل کار می‌کند. اگر کاربران شما فقط موبایل دارند، بازیابی را با کد پیامکی (درس ۳۰) بسازید.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>از Django 5.0 خروج با GET حذف شده است؛ لینک ساده‌ی <code>&lt;a href="/accounts/logout/"&gt;</code> خطای 405 می‌دهد و باید فرم POST با توکن CSRF باشد.</li>
<li>Django 5.1 میدل‌ور <code>LoginRequiredMiddleware</code> را آورد: همه‌ی صفحات به‌طور پیش‌فرض لاگین می‌خواهند و صفحات عمومی را با دکوراتور <code>@login_not_required</code> باز می‌کنید؛ برای پنل‌های داخلی امن‌ترین پیش‌فرض است.</li>
<li>LoginView پارامتر <code>next</code> را با <code>url_has_allowed_host_and_scheme</code> بررسی می‌کند تا ریدایرکت به سایت مهاجم (open redirect) ممکن نباشد؛ اگر ورود دستی می‌نویسید، همین تابع را خودتان صدا بزنید.</li>
<li><code>login()</code> شناسه‌ی Session را عوض می‌کند (جلوگیری از session fixation) اما داده‌های Session مهمان مثل سبد خرید را نگه می‌دارد.</li>
<li>فهرست <code>PASSWORD_HASHERS</code> را که عوض کنید، رمز کاربران قدیمی در اولین ورود موفق خودکار با الگوریتم جدید دوباره هش می‌شود؛ مهاجرت بی‌دردسر به Argon2.</li>
</ul>""",
                },
                {
                    "title": "Permission و Group: has_perm، مجوز سفارشی و دسترسی سطح شیء",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>چه کسی اجازه‌ی چه کاری را دارد؟</h2>
<p>احراز هویت می‌گوید «تو کیستی»؛ مجوز می‌گوید «اجازه‌ی چه کاری داری». جنگو برای هر مدل چهار مجوز خودکار می‌سازد: <code>add</code>، <code>change</code>، <code>delete</code> و <code>view</code>. نام کامل هر مجوز به شکل <code>app_label.codename</code> است؛ مثلاً <code>orders.change_order</code>. مجوزها به کاربر یا به <strong>Group</strong> داده می‌شوند و کاربر مجوزهای همه‌ی گروه‌هایش را به ارث می‌برد.</p>
<h3>مجوز سفارشی</h3>
<pre><code class="language-python">class Order(models.Model):
    ...
    class Meta:
        permissions = [
            ("approve_order", "می‌تواند سفارش را تأیید کند"),
            ("export_orders", "می‌تواند خروجی اکسل سفارش‌ها را بگیرد"),
        ]</code></pre>
<p>بعد از makemigrations و migrate، این مجوزها در ادمین قابل تخصیص‌اند.</p>
<h3>ساخت گروه‌ها با کد، نه با کلیک</h3>
<pre><code class="language-python"># apps/accounts/management/commands/setup_roles.py
from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

ROLES = {
    "فروش": ["orders.view_order", "orders.change_order", "orders.approve_order"],
    "انبار": ["catalog.view_carpet", "catalog.change_carpet"],
    "حسابداری": ["orders.view_order", "orders.export_orders"],
}


class Command(BaseCommand):
    def handle(self, *args, **opts):
        for name, perms in ROLES.items():
            group, _ = Group.objects.get_or_create(name=name)
            objs = []
            for p in perms:
                app_label, codename = p.split(".")
                objs.append(Permission.objects.get(content_type__app_label=app_label, codename=codename))
            group.permissions.set(objs)
            self.stdout.write(f"گروه {name}: {len(objs)} مجوز")</code></pre>
<h3>بررسی مجوز در View و قالب</h3>
<pre><code class="language-python">from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

@permission_required("orders.approve_order", raise_exception=True)
def approve(request, pk): ...

class ExportView(PermissionRequiredMixin, View):
    permission_required = "orders.export_orders"

if request.user.has_perm("orders.approve_order"): ...</code></pre>
<pre><code class="language-html">{% if perms.orders.approve_order %}
  &lt;button&gt;تأیید سفارش&lt;/button&gt;
{% endif %}</code></pre>
<h3>دسترسی سطح شیء</h3>
<p>مجوزهای جنگو «سطح مدل» هستند: یا می‌توانید <em>همه‌ی</em> سفارش‌ها را تأیید کنید یا هیچ‌کدام را. برای «نماینده‌ی فروش فقط سفارش‌های شهر خودش را» دو راه دارید: ساده و رایج، محدود کردن queryset در <code>get_queryset</code>؛ یا نوشتن یک authentication backend که <code>has_perm(user_obj, perm, obj=None)</code> را با منطق شیء پیاده کند (یا کتابخانه‌هایی مثل django-rules و django-guardian).</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>مجوزها روی شیء user کش می‌شوند؛ اگر در همان درخواست مجوزی اضافه کنید، <code>has_perm</code> هنوز False می‌دهد تا کاربر را دوباره از پایگاه داده بخوانید.</li>
<li><code>is_superuser</code> همه‌ی بررسی‌های <code>has_perm</code> را دور می‌زند، اما <code>is_active=False</code> حتی برای سوپریوزر همه را False می‌کند.</li>
<li>مجوزها در سیگنال <code>post_migrate</code> ساخته می‌شوند؛ در data migration ممکن است هنوز وجود نداشته باشند. به همین دلیل ساخت گروه‌ها با دستور مدیریتی بعد از migrate امن‌تر است.</li>
<li><code>raise_exception=True</code> برای کاربر لاگین‌شده‌ی بدون مجوز 403 برمی‌گرداند؛ بدون آن به صفحه‌ی ورود ریدایرکت می‌شود و کاربر در حلقه‌ی «وارد شدم ولی باز صفحه‌ی ورود» گیر می‌کند.</li>
<li><code>is_staff</code> فقط اجازه‌ی ورود به ادمین است، نه هیچ مجوز دیگری؛ کاربر staff بدون مجوز در ادمین صفحه‌ای خالی می‌بیند.</li>
</ul>""",
                },
                {
                    "title": "ورود با OTP پیامکی: طراحی امن، انقضا و محدودیت نرخ",
                    "kind": "text",
                    "minutes": 26,
                    "is_preview": False,
                    "body": r"""<h2>رمز یک‌بارمصرف؛ ساده برای کاربر، حساس برای شما</h2>
<p>کاربر ایرانی به ورود با پیامک عادت دارد: شماره را وارد می‌کند، کد پنج‌رقمی می‌گیرد و وارد می‌شود. پیاده‌سازی ساده‌ی آن در ده دقیقه تمام می‌شود؛ پیاده‌سازی <em>امن</em>ش چند نکته دارد که اگر رعایت نشود، مهاجم می‌تواند کد را حدس بزند، هزینه‌ی پیامک شما را بالا ببرد یا وجود کاربران را کشف کند.</p>
<h3>قواعد طراحی</h3>
<ul>
<li>کد با <code>secrets</code> ساخته شود نه <code>random</code>، و فقط <em>هش</em> آن ذخیره شود.</li>
<li>انقضای کوتاه (۲ دقیقه) و حداکثر ۵ تلاش برای هر کد؛ بعد از آن کد باطل شود.</li>
<li>فاصله‌ی زمانی بین دو ارسال برای یک شماره (۶۰ ثانیه) و سقف ارسال برای هر IP در ساعت.</li>
<li>پاسخ برای شماره‌ی ثبت‌شده و ثبت‌نشده یکسان باشد.</li>
<li>ارسال پیامک در پس‌زمینه (Celery) و بعد از commit.</li>
</ul>
<pre><code class="language-python"># apps/accounts/otp.py
import hashlib
import hmac
import secrets
import time

from django.conf import settings
from django.core.cache import cache

from .tasks import send_otp_sms

OTP_TTL, COOLDOWN, MAX_TRIES, IP_LIMIT = 120, 60, 5, 10


class OTPError(Exception):
    pass


def _digest(mobile, code):
    msg = f"{mobile}:{code}".encode()
    return hmac.new(settings.SECRET_KEY.encode(), msg, hashlib.sha256).hexdigest()


def request_otp(mobile, ip):
    if not cache.add(f"otp:cd:{mobile}", 1, timeout=COOLDOWN):
        raise OTPError("کد قبلاً ارسال شده؛ یک دقیقه صبر کنید.")
    ip_key = f"otp:ip:{ip}"
    cache.add(ip_key, 0, timeout=3600)
    if cache.incr(ip_key) &gt; IP_LIMIT:
        raise OTPError("تعداد درخواست‌ها بیش از حد مجاز است.")
    code = f"{secrets.randbelow(100000):05d}"
    cache.set(f"otp:{mobile}", {"h": _digest(mobile, code), "tries": 0,
                                "exp": time.time() + OTP_TTL}, timeout=OTP_TTL)
    send_otp_sms.delay(mobile, code)


def verify_otp(mobile, code):
    key = f"otp:{mobile}"
    data = cache.get(key)
    if not data or data["tries"] &gt;= MAX_TRIES:
        cache.delete(key)
        return False
    if hmac.compare_digest(data["h"], _digest(mobile, code)):
        cache.delete(key)                       # یک‌بارمصرف
        return True
    data["tries"] += 1
    remaining = int(data["exp"] - time.time())
    if remaining &gt; 0:
        cache.set(key, data, timeout=remaining)  # TTL تمدید نشود
    return False</code></pre>
<pre><code class="language-python"># apps/accounts/views.py (بخش تأیید)
if verify_otp(mobile, code):
    user, created = User.objects.get_or_create(mobile=mobile)
    login(request, user, backend="django.contrib.auth.backends.ModelBackend")
    return redirect(request.GET.get("next") or "orders:list")   # next را با url_has_allowed_host_and_scheme بررسی کنید</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>کش پیش‌فرض (LocMemCache) برای هر پروسه‌ی gunicorn جداست؛ با چهار worker کد ممکن است در یکی ذخیره و در دیگری جست‌وجو شود. OTP و rate limit حتماً Redis می‌خواهند.</li>
<li>شمارش تلاش‌ها با get/set در شرایط هم‌زمانی قابل دور زدن است (چند درخواست موازی)؛ در مقیاس جدی از <code>incr</code> اتمیک Redis برای شمارنده‌ی تلاش استفاده کنید.</li>
<li>بیشتر سرویس‌های پیامک ایرانی متد «ارسال با الگو» (verify/lookup) دارند که از خط خدماتی و بدون فیلتر بلک‌لیست مخابرات می‌رود و بسیار سریع‌تر از ارسال متن آزاد می‌رسد.</li>
<li><code>autocomplete="one-time-code"</code> و <code>inputmode="numeric"</code> روی input کد باعث می‌شود گوشی کد پیامک را خودش پیشنهاد دهد و کیبورد عددی باز شود.</li>
<li>هنگام لاگین دستی کاربری که با authenticate احراز نشده، پارامتر <code>backend</code> در <code>login()</code> الزامی است وقتی بیش از یک backend در <code>AUTHENTICATION_BACKENDS</code> دارید.</li>
<li>کد OTP را هرگز در لاگ ننویسید، حتی در DEBUG؛ لاگ‌ها معمولاً دسترسی گسترده‌تری از پایگاه داده دارند.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۷ ─────────────────────────────
        {
            "title": "فصل ۷: API و امکانات حرفه‌ای — DRF، کش، Celery و امنیت",
            "lessons": [
                {
                    "title": "Django REST Framework: Serializer، ModelViewSet و Router",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>وقتی مشتری شما یک اپ موبایل است</h2>
<p>اپ اندرویدی فروشندگان، داشبورد React یا نرم‌افزار حسابداری که باید سفارش‌ها را بخواند، HTML نمی‌خواهند؛ JSON می‌خواهند. <strong>Django REST Framework</strong> (DRF) استاندارد عملی ساخت API در جنگوست: سریال‌سازی، اعتبارسنجی، احراز هویت، مجوز، صفحه‌بندی و مستندات قابل‌مرور، همه آماده.</p>
<pre><code class="language-powershell">pip install djangorestframework</code></pre>
<pre><code class="language-python"># settings.py
INSTALLED_APPS += ["rest_framework"]</code></pre>
<h3>Serializer: پل بین مدل و JSON</h3>
<p>Serializer همان نقشی را در API دارد که Form در HTML: داده‌ی ورودی را اعتبارسنجی و به شیء تبدیل می‌کند و شیء را برای خروجی به dict تبدیل می‌کند.</p>
<pre><code class="language-python"># apps/api/serializers.py
from rest_framework import serializers
from apps.catalog.models import Carpet
from apps.orders.models import Order, OrderItem


class CarpetSerializer(serializers.ModelSerializer):
    price_toman = serializers.SerializerMethodField()
    density_label = serializers.CharField(source="get_density_display", read_only=True)

    class Meta:
        model = Carpet
        fields = ["id", "code", "name", "density", "density_label", "price", "price_toman", "stock"]
        read_only_fields = ["stock"]

    def get_price_toman(self, obj):
        return obj.price // 10

    def validate_price(self, value):
        if value % 10_000:
            raise serializers.ValidationError("قیمت باید مضرب ده هزار ریال باشد.")
        return value


class OrderItemSerializer(serializers.ModelSerializer):
    carpet = CarpetSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ["carpet", "quantity", "unit_price"]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    customer_name = serializers.CharField(source="customer.full_name", read_only=True)

    class Meta:
        model = Order
        fields = ["id", "tracking_code", "status", "total", "customer_name", "items", "created_at"]</code></pre>
<h3>ViewSet و Router</h3>
<pre><code class="language-python"># apps/api/views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class CarpetViewSet(viewsets.ModelViewSet):
    queryset = Carpet.objects.filter(status="active").order_by("code")
    serializer_class = CarpetSerializer
    lookup_field = "code"

    @action(detail=True, methods=["get"])
    def stock(self, request, code=None):
        carpet = self.get_object()
        return Response({"code": carpet.code, "stock": carpet.stock})


class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return (Order.objects.for_user(self.request.user)
                .select_related("customer").prefetch_related("items__carpet"))

# apps/api/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("carpets", CarpetViewSet)
router.register("orders", OrderViewSet, basename="order")
urlpatterns = [path("v1/", include(router.urls))]</code></pre>
<p>همین چند خط این endpointها را می‌سازد: <code>GET/POST /api/v1/carpets/</code>، <code>GET/PUT/PATCH/DELETE /api/v1/carpets/{code}/</code>، <code>GET /api/v1/carpets/{code}/stock/</code> و فهرست و جزئیات سفارش‌های خود کاربر.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>وقتی ViewSet به‌جای ویژگی <code>queryset</code> متد <code>get_queryset</code> دارد، <code>basename</code> در router الزامی است؛ وگرنه خطای «basename argument not specified» می‌گیرید.</li>
<li>ModelSerializer متد <code>clean()</code> مدل را صدا نمی‌زند؛ قواعد مدل را در <code>validate()</code> سریالایزر تکرار کنید یا در آن‌جا <code>instance.full_clean()</code> را صدا بزنید.</li>
<li>Serializerهای تودرتو N+1 می‌سازند؛ همیشه در <code>get_queryset</code> ViewSet، select_related و prefetch_related متناسب با فیلدهای سریالایزر بگذارید.</li>
<li><code>SerializerMethodField</code> فقط‌خواندنی است؛ برای فیلد محاسبه‌شده‌ی قابل‌نوشتن از <code>source</code> یا بازنویسی <code>to_internal_value</code> استفاده کنید.</li>
<li>در سرور می‌توانید Browsable API را با حذف <code>BrowsableAPIRenderer</code> از <code>DEFAULT_RENDERER_CLASSES</code> خاموش کنید؛ هم سطح حمله کمتر می‌شود هم ساختار داخلی لو نمی‌رود.</li>
</ul>""",
                },
                {
                    "title": "DRF حرفه‌ای: permissions، pagination، throttling و JWT",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>API عمومی بدون محافظ، دعوت‌نامه است</h2>
<p>API برخلاف صفحه‌ی HTML با اسکریپت فراخوانده می‌شود؛ یعنی مهاجم می‌تواند در یک دقیقه هزاران درخواست بفرستد. چهار لایه‌ی پیش‌فرض را همیشه در تنظیمات سراسری DRF مشخص کنید تا هیچ endpointی به‌طور تصادفی باز نماند.</p>
<pre><code class="language-python"># settings.py
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",   # اپ موبایل
        "rest_framework.authentication.SessionAuthentication",         # فرانت هم‌دامنه
    ],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 20,
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
        "rest_framework.throttling.ScopedRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {"anon": "30/min", "user": "300/min", "otp": "5/hour"},
    "NUM_PROXIES": 1,                     # پشت nginx: IP واقعی از X-Forwarded-For
}</code></pre>
<h3>permission سفارشی</h3>
<pre><code class="language-python"># apps/api/permissions.py
from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsOwnerOrStaffReadOnly(BasePermission):
    message = "شما به این سفارش دسترسی ندارید."

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return request.method in SAFE_METHODS
        return obj.customer.user_id == request.user.id</code></pre>
<pre><code class="language-python">class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrStaffReadOnly]

class OTPRequestView(APIView):
    permission_classes = [AllowAny]
    throttle_scope = "otp"               # فقط ۵ درخواست در ساعت</code></pre>
<h3>صفحه‌بندی</h3>
<table><thead><tr><th>کلاس</th><th>پارامتر</th><th>مناسب برای</th></tr></thead><tbody>
<tr><td>PageNumberPagination</td><td><code>?page=3</code></td><td>پنل‌ها و فهرست‌های معمولی</td></tr>
<tr><td>LimitOffsetPagination</td><td><code>?limit=50&amp;offset=100</code></td><td>جدول‌های با اندازه‌ی صفحه‌ی متغیر</td></tr>
<tr><td>CursorPagination</td><td><code>?cursor=…</code></td><td>جدول‌های بسیار بزرگ و اسکرول بی‌نهایت اپ</td></tr>
</tbody></table>
<h3>JWT برای اپ موبایل</h3>
<pre><code class="language-python"># pip install djangorestframework-simplejwt
from datetime import timedelta
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=14),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,     # نیاز به اپ token_blacklist
}

urlpatterns += [
    path("auth/token/", TokenObtainPairView.as_view()),
    path("auth/token/refresh/", TokenRefreshView.as_view()),
]</code></pre>
<p>برای ورود با OTP، به‌جای TokenObtainPairView یک View بنویسید که کد را با <code>verify_otp</code> درس ۳۰ بررسی کند و با <code>RefreshToken.for_user(user)</code> توکن بسازد.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>has_object_permission</code> فقط وقتی اجرا می‌شود که View متد <code>get_object()</code> را صدا بزند؛ در list هرگز اجرا نمی‌شود. محدودیت فهرست را حتماً در <code>get_queryset</code> بگذارید.</li>
<li>throttling از کش استفاده می‌کند؛ با LocMemCache و چند worker هر worker شمارنده‌ی جدا دارد و محدودیت واقعی چند برابر می‌شود. Redis لازم است.</li>
<li>بدون <code>NUM_PROXIES</code> پشت nginx همه‌ی کاربران IP یکسان (127.0.0.1) دارند و یک کاربر پرکار سهمیه‌ی anon همه را تمام می‌کند.</li>
<li>JWT پس از صدور قابل باطل‌کردن نیست تا منقضی شود؛ برای همین access کوتاه (۵ تا ۱۵ دقیقه) و refresh با rotation و blacklist انتخاب امن است.</li>
<li>PageNumberPagination در صفحات دور (<code>?page=5000</code>) کند می‌شود چون OFFSET بزرگ می‌سازد؛ CursorPagination زمان ثابت دارد اما به یک ترتیب یکتا و ثابت (مثلاً <code>-created_at</code>) نیاز دارد.</li>
</ul>""",
                },
                {
                    "title": "کش: per-view، fragment، low-level و Redis",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>سریع‌ترین کوئری، کوئری‌ای است که اجرا نشود</h2>
<p>صفحه‌ی اصلی فروشگاه که پرفروش‌ترین طرح‌ها را با چند annotate سنگین نشان می‌دهد، در هر بازدید همان نتیجه را دوباره حساب می‌کند. کش یعنی نتیجه را یک بار حساب کنیم و برای مدتی نگه داریم. جنگو چهار سطح کش دارد و از نسخه‌ی 4.0 backend رسمی Redis هم دارد.</p>
<pre><code class="language-python"># settings.py  (pip install redis)
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": os.getenv("REDIS_URL", "redis://127.0.0.1:6379/1"),
        "KEY_PREFIX": "carpet",
        "TIMEOUT": 300,
    }
}</code></pre>
<h3>سطح ۱: کش کل View</h3>
<pre><code class="language-python">from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

@cache_page(60 * 10)                 # ۱۰ دقیقه
def price_list(request): ...

# برای CBV در urls:
path("catalog/", cache_page(600)(CatalogView.as_view()), name="catalog")</code></pre>
<h3>سطح ۲: کش تکه‌ای از قالب</h3>
<pre><code class="language-html">{% load cache %}
{% cache 900 bestsellers %}
  {% for carpet in bestsellers %}&lt;li&gt;{{ carpet.name }}&lt;/li&gt;{% endfor %}
{% endcache %}

{% cache 300 user_sidebar request.user.pk %}...{% endcache %}   {# کلید جدا برای هر کاربر #}</code></pre>
<h3>سطح ۳: کش سطح پایین</h3>
<pre><code class="language-python">from django.core.cache import cache

def get_bestsellers():
    return cache.get_or_set(
        "bestsellers:v1",
        lambda: list(Carpet.objects.filter(status="active")
                     .annotate(sold=Sum("orderitem__quantity"))
                     .order_by("-sold")[:10]),
        timeout=900,
    )

# باطل کردن هنگام تغییر
def on_carpet_changed(**kwargs):
    cache.delete("bestsellers:v1")</code></pre>
<p>نکته‌ی مهم <code>list(...)</code> است: اگر خود QuerySet را کش کنید، چون تنبل است ممکن است چیزی که ذخیره می‌شود فقط «توصیف کوئری» باشد و در هر استفاده دوباره اجرا شود.</p>
<table><thead><tr><th>سطح</th><th>ابزار</th><th>مناسب برای</th></tr></thead><tbody>
<tr><td>کل سایت</td><td>UpdateCacheMiddleware / FetchFromCacheMiddleware</td><td>سایت‌های تقریباً ایستا و بدون لاگین</td></tr>
<tr><td>View</td><td><code>cache_page</code></td><td>صفحات عمومی مثل لیست قیمت</td></tr>
<tr><td>قالب</td><td><code>{% cache %}</code></td><td>بخش‌های سنگین یک صفحه‌ی پویا</td></tr>
<tr><td>داده</td><td><code>cache.get_or_set</code></td><td>نتیجه‌ی محاسبات و فراخوانی API بیرونی</td></tr>
</tbody></table>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>cache_page</code> را روی صفحه‌ای که نام کاربر یا توکن CSRF دارد نگذارید؛ کاربر دوم صفحه‌ی کاربر اول را می‌بیند. اگر لازم است، با <code>vary_on_cookie</code> کلید را به کوکی وابسته کنید.</li>
<li><code>KEY_PREFIX</code> اجازه می‌دهد چند پروژه یک Redis مشترک داشته باشند بدون تداخل کلیدها؛ روی سرورهای کوچک ایرانی که یک Redis برای همه دارند، ضروری است.</li>
<li>به‌جای پاک کردن تک‌تک کلیدها، یک عدد نسخه در نام کلید بگذارید (<code>bestsellers:v2</code>)؛ عوض کردن نسخه همه‌ی کش قدیمی را بی‌اثر می‌کند.</li>
<li><code>cache.add()</code> فقط اگر کلید وجود نداشته باشد می‌نویسد و اتمیک است؛ پایه‌ی یک قفل ساده برای جلوگیری از اجرای هم‌زمان یک کار سنگین.</li>
<li>در تست‌ها از <code>DummyCache</code> یا <code>LocMemCache</code> استفاده کنید و بین تست‌ها <code>cache.clear()</code> بزنید؛ وگرنه نتیجه‌ی یک تست به تست بعدی نشت می‌کند.</li>
</ul>""",
                },
                {
                    "title": "کارهای پس‌زمینه با Celery و Redis؛ ارسال ایمیل",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>کاربر نباید منتظر سرویس پیامک بماند</h2>
<p>ارسال پیامک، ایمیل فاکتور، ساخت PDF، ورود اکسل هزارخطی: هر کاری که بیش از چند صد میلی‌ثانیه طول می‌کشد یا به سرویس بیرونی وابسته است، نباید در چرخه‌ی درخواست انجام شود. اگر سرویس پیامک ده ثانیه جواب ندهد، worker gunicorn ده ثانیه قفل است. <strong>Celery</strong> این کارها را در صف (Redis) می‌گذارد و پروسه‌های جداگانه (worker) آن‌ها را اجرا می‌کنند.</p>
<pre><code class="language-powershell">pip install "celery[redis]"</code></pre>
<pre><code class="language-python"># config/celery.py
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

# config/__init__.py
from .celery import app as celery_app
__all__ = ("celery_app",)

# settings.py
CELERY_BROKER_URL = os.getenv("REDIS_URL", "redis://127.0.0.1:6379/0")
CELERY_TIMEZONE = TIME_ZONE
CELERY_TASK_ACKS_LATE = True
CELERY_TASK_TIME_LIMIT = 120</code></pre>
<h3>تعریف task</h3>
<pre><code class="language-python"># apps/notifications/tasks.py
import requests
from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from apps.orders.models import Order


@shared_task(bind=True, autoretry_for=(requests.RequestException,),
             retry_backoff=True, retry_kwargs={"max_retries": 5})
def send_order_sms(self, order_id):
    order = Order.objects.select_related("customer__user").get(pk=order_id)
    sms_client.send_pattern(order.customer.user.mobile, "order-created",
                            {"code": order.tracking_code})


@shared_task
def send_invoice_email(order_id):
    order = Order.objects.get(pk=order_id)
    ctx = {"order": order}
    msg = EmailMultiAlternatives(
        subject=f"فاکتور سفارش {order.tracking_code}",
        body=render_to_string("emails/invoice.txt", ctx),
        to=[order.customer.user.email],
    )
    msg.attach_alternative(render_to_string("emails/invoice.html", ctx), "text/html")
    msg.send()</code></pre>
<p>فراخوانی: <code>transaction.on_commit(lambda: send_order_sms.delay(order.pk))</code>. اجرای worker و زمان‌بند:</p>
<pre><code class="language-bash">celery -A config worker -l info
celery -A config beat -l info          # کارهای دوره‌ای (CELERY_BEAT_SCHEDULE)
# روی ویندوز برای توسعه:
celery -A config worker -l info --pool=solo</code></pre>
<h3>تنظیمات ایمیل</h3>
<pre><code class="language-python">EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "mail.example.ir"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_PASSWORD")
DEFAULT_FROM_EMAIL = "فرش کاشان &lt;noreply@example.ir&gt;"
# در توسعه: "django.core.mail.backends.console.EmailBackend"</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>به task همیشه شناسه بدهید نه شیء مدل؛ شیء سریال‌سازی می‌شود و وقتی worker آن را اجرا می‌کند ممکن است داده‌اش کهنه باشد.</li>
<li>بدون <code>on_commit</code>، worker ممکن است قبل از commit تراکنش task را بگیرد و با <code>DoesNotExist</code> روبه‌رو شود؛ باگی که فقط زیر بار واقعی دیده می‌شود. از Celery 5.4 می‌توانید مستقیم <code>task.delay_on_commit(...)</code> را صدا بزنید.</li>
<li>Celery 4 به بعد روی ویندوز رسماً پشتیبانی نمی‌شود؛ pool پیش‌فرض prefork آن‌جا کار نمی‌کند و <code>--pool=solo</code> فقط برای توسعه است.</li>
<li>با <code>acks_late</code> اگر worker وسط کار از کار بیفتد، task دوباره اجرا می‌شود؛ پس taskها را idempotent بنویسید (اجرای دوباره نباید پیامک دوم بفرستد؛ مثلاً پرچم <code>sms_sent</code>).</li>
<li>برای پروژه‌های کوچک که Redis و Celery سربار زیادی است، Django 6.0 چارچوب داخلی Tasks را آورده؛ روی 5.x، کتابخانه‌هایی مثل django-q2 یا huey با پیکربندی کمتر همین کار را می‌کنند.</li>
</ul>""",
                },
                {
                    "title": "Middleware سفارشی، لاگ‌گیری و فارسی‌سازی (i18n)",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>کدی که دور همه‌ی درخواست‌ها می‌پیچد</h2>
<p>Middleware یک لایه‌ی سراسری است: هر درخواست قبل از رسیدن به View از آن عبور می‌کند و هر پاسخ در بازگشت. کارهایی که به همه‌ی صفحه‌ها مربوط‌اند جایشان این‌جاست: اندازه‌گیری زمان پاسخ، گرفتن IP واقعی، حالت تعمیرات، افزودن هدرهای امنیتی.</p>
<pre><code class="language-python"># apps/core/middleware.py
import logging
import time

logger = logging.getLogger("apps.requests")


class RequestTimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response          # یک بار، هنگام شروع سرور

    def __call__(self, request):
        start = time.perf_counter()
        response = self.get_response(request)     # بقیه‌ی زنجیره و View
        ms = (time.perf_counter() - start) * 1000
        response["Server-Timing"] = f"app;dur={ms:.0f}"
        if ms &gt; 1000:
            logger.warning("slow request %s %s %.0fms user=%s",
                           request.method, request.path, ms, getattr(request.user, "pk", None))
        return response


class MaintenanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        from django.conf import settings
        from django.shortcuts import render
        if settings.MAINTENANCE_MODE and not request.path.startswith("/manage-7f3a/"):
            return render(request, "503.html", status=503)
        return self.get_response(request)</code></pre>
<p>ثبت در <code>MIDDLEWARE</code>: بعد از <code>AuthenticationMiddleware</code> تا <code>request.user</code> در دسترس باشد.</p>
<h3>لاگ‌گیری که روی سرور به کار بیاید</h3>
<pre><code class="language-python">LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {"std": {"format": "{asctime} {levelname} {name} {message}", "style": "{"}},
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "std"},
        "file": {"class": "logging.handlers.RotatingFileHandler",
                 "filename": BASE_DIR / "logs" / "app.log",
                 "maxBytes": 10 * 1024 * 1024, "backupCount": 5,
                 "formatter": "std", "encoding": "utf-8"},
    },
    "loggers": {
        "django": {"handlers": ["console", "file"], "level": "WARNING"},
        "apps": {"handlers": ["console", "file"], "level": "INFO"},
    },
}</code></pre>
<p>با systemd، خروجی console خودکار در journal ذخیره می‌شود و با <code>journalctl -u carpet -f</code> دیده می‌شود.</p>
<h3>فارسی‌سازی: i18n</h3>
<p>حتی اگر سایت فقط فارسی است، متن‌های ثابت کد را با <code>gettext_lazy</code> علامت بزنید تا روزی که نسخه‌ی انگلیسی برای مشتری خارجی لازم شد، فقط فایل ترجمه بسازید:</p>
<pre><code class="language-python">from django.utils.translation import gettext_lazy as _

class Carpet(models.Model):
    name = models.CharField(_("نام طرح"), max_length=100)

# settings.py
LANGUAGES = [("fa", "فارسی"), ("en", "English")]
LOCALE_PATHS = [BASE_DIR / "locale"]
# MIDDLEWARE: "django.middleware.locale.LocaleMiddleware" بعد از SessionMiddleware</code></pre>
<pre><code class="language-bash">python manage.py makemessages -l en
python manage.py compilemessages</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>__init__</code> middleware فقط یک بار اجرا می‌شود؛ اگر در آن <code>MiddlewareNotUsed</code> بالا ببرید، جنگو آن middleware را کاملاً از زنجیره حذف می‌کند (مثلاً وقتی تنظیمی خاموش است).</li>
<li>هدر <code>Server-Timing</code> مستقیم در تب Network ابزار توسعه‌ی مرورگر نمایش داده می‌شود؛ بدون هیچ ابزار مانیتورینگی زمان سمت سرور را می‌بینید.</li>
<li>در سطح ماژول و فیلدهای مدل حتماً <code>gettext_lazy</code> بنویسید نه <code>gettext</code>؛ نسخه‌ی غیر lazy در زمان import، قبل از فعال شدن زبان، ترجمه می‌شود.</li>
<li>makemessages روی ویندوز به ابزار GNU gettext نیاز دارد که همراه پایتون نیست؛ یا نصبش کنید یا این مرحله را روی WSL یا سرور لینوکس انجام دهید.</li>
<li><code>encoding="utf-8"</code> در handler فایل روی ویندوز ضروری است؛ بدون آن اولین پیام لاگ فارسی با UnicodeEncodeError کل لاگ‌گیری را خراب می‌کند.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۸ ─────────────────────────────
        {
            "title": "فصل ۸: تست، استقرار و پروژه‌ی پایانی",
            "lessons": [
                {
                    "title": "تست: TestCase، Client، pytest-django و factory_boy",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>تست یعنی جرئت تغییر دادن</h2>
<p>پروژه‌ای که تست ندارد بعد از شش ماه «دست‌نزدنی» می‌شود: هر تغییر ممکن است جای دیگری را بشکند و کسی جرئت نمی‌کند نسخه‌ی جنگو را به‌روز کند. تست‌های جنگو روی یک پایگاه داده‌ی موقت اجرا می‌شوند و هر تست داخل یک تراکنش است که در پایان rollback می‌شود؛ پس تست‌ها روی هم اثر نمی‌گذارند.</p>
<h3>TestCase و Client داخلی جنگو</h3>
<pre><code class="language-python"># apps/orders/tests/test_views.py
from django.test import TestCase
from django.urls import reverse

from apps.accounts.models import User
from apps.orders.models import Customer, Order


class OrderViewsTests(TestCase):
    @classmethod
    def setUpTestData(cls):                       # یک بار برای کل کلاس
        cls.user = User.objects.create_user(mobile="09120000001", password="pass-12345")
        cls.other = User.objects.create_user(mobile="09120000002", password="pass-12345")
        cls.customer = Customer.objects.create(user=cls.user, full_name="علی رضایی")
        cls.order = Order.objects.create(customer=cls.customer, total=120_000_000)

    def test_login_required(self):
        resp = self.client.get(reverse("orders:list"))
        self.assertRedirects(resp, f"{reverse('login')}?next={reverse('orders:list')}")

    def test_owner_sees_order(self):
        self.client.force_login(self.user)
        resp = self.client.get(self.order.get_absolute_url())
        self.assertContains(resp, self.order.tracking_code)

    def test_other_user_gets_404(self):
        self.client.force_login(self.other)
        resp = self.client.get(self.order.get_absolute_url())
        self.assertEqual(resp.status_code, 404)

    def test_list_query_count(self):
        self.client.force_login(self.user)
        with self.assertNumQueries(4):            # session، user، count، list
            self.client.get(reverse("orders:list"))</code></pre>
<pre><code class="language-powershell">python manage.py test apps.orders --parallel</code></pre>
<h3>pytest-django و factory_boy</h3>
<p>pytest خواناتر است، fixture دارد و خروجی خطایش بهتر است. factory_boy هم ساخت داده‌ی آزمایشی را از تکرار نجات می‌دهد:</p>
<pre><code class="language-ini"># pytest.ini
[pytest]
DJANGO_SETTINGS_MODULE = config.settings
python_files = tests.py test_*.py
addopts = --reuse-db -q</code></pre>
<pre><code class="language-python"># apps/orders/tests/factories.py
import factory
from apps.accounts.models import User
from apps.orders.models import Customer, Order


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    mobile = factory.Sequence(lambda n: f"0912{n:07d}")


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer
    user = factory.SubFactory(UserFactory)
    full_name = factory.Faker("name", locale="fa_IR")


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order
    customer = factory.SubFactory(CustomerFactory)
    total = 50_000_000

# apps/orders/tests/test_services.py
import pytest
from apps.orders.services import OutOfStock, place_order

@pytest.mark.django_db
def test_out_of_stock_rolls_back(carpet_factory):
    carpet = carpet_factory(stock=1)
    customer = CustomerFactory()
    with pytest.raises(OutOfStock):
        place_order(customer, [{"carpet_id": carpet.pk, "quantity": 2}])
    assert customer.orders.count() == 0</code></pre>
<p>(<code>carpet_factory</code> با ثبت factory در <code>conftest.py</code> از طریق پلاگین pytest-factoryboy یا یک fixture ساده ساخته می‌شود.)</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>setUpTestData</code> داده را یک بار برای کل کلاس می‌سازد و از Django 3.2 هر تست یک کپی ایزوله از اشیا می‌گیرد؛ چند برابر سریع‌تر از <code>setUp</code>.</li>
<li><code>force_login</code> مراحل هش رمز را رد می‌کند و تست‌ها را محسوس سریع‌تر می‌کند؛ برای سرعت بیشتر در تنظیمات تست <code>MD5PasswordHasher</code> بگذارید.</li>
<li><code>TestCase</code> معمولی <code>on_commit</code> را اجرا نمی‌کند چون تراکنش هرگز commit نمی‌شود؛ با <code>self.captureOnCommitCallbacks(execute=True)</code> آن‌ها را اجرا و بررسی کنید.</li>
<li>در pytest-django فیکسچر <code>django_assert_num_queries</code> همان assertNumQueries است و <code>settings</code> فیکسچری است که تنظیمات را فقط برای یک تست تغییر می‌دهد.</li>
<li>برای تست Celery، <code>CELERY_TASK_ALWAYS_EAGER = True</code> در تنظیمات تست taskها را هم‌زمان اجرا می‌کند؛ بدون نیاز به Redis در CI.</li>
</ul>""",
                },
                {
                    "title": "استقرار روی اوبونتو (۱): PostgreSQL، gunicorn و systemd",
                    "kind": "text",
                    "minutes": 26,
                    "is_preview": False,
                    "body": r"""<h2>از runserver تا سرور واقعی</h2>
<p><code>runserver</code> فقط برای توسعه است: تک‌پروسه، بدون امنیت و کارایی لازم. معماری استاندارد استقرار جنگو روی لینوکس این است: <strong>nginx</strong> جلوی همه (HTTPS، فایل‌های static و media، محدودیت حجم)، <strong>gunicorn</strong> با چند worker برای اجرای کد پایتون، <strong>PostgreSQL</strong> به‌عنوان پایگاه داده و <strong>systemd</strong> برای روشن نگه داشتن همه‌چیز. در این درس سه لایه‌ی اول پشتی را می‌سازیم؛ درس بعد nginx و HTTPS.</p>
<h3>۱. آماده‌سازی سرور</h3>
<pre><code class="language-bash">sudo apt update
sudo apt install -y python3.12-venv python3-dev build-essential libpq-dev \
    postgresql nginx redis-server git
sudo adduser --system --group --home /srv/carpet carpet</code></pre>
<p>برنامه با یک کاربر سیستمی بدون دسترسی root اجرا می‌شود؛ اگر روزی آسیب‌پذیری در کد باشد، مهاجم به کل سرور دسترسی ندارد.</p>
<h3>۲. PostgreSQL</h3>
<pre><code class="language-bash">sudo -u postgres psql &lt;&lt;'SQL'
CREATE USER carpet WITH PASSWORD 'a-long-random-password';
CREATE DATABASE carpet OWNER carpet ENCODING 'UTF8';
ALTER ROLE carpet SET timezone TO 'UTC';
SQL</code></pre>
<pre><code class="language-python"># settings.py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME", "carpet"),
        "USER": os.getenv("DB_USER", "carpet"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST", "127.0.0.1"),
        "PORT": "5432",
        "CONN_MAX_AGE": 60,                 # استفاده‌ی مجدد از اتصال
        "CONN_HEALTH_CHECKS": True,
    }
}</code></pre>
<h3>۳. کد، venv و مهاجرت</h3>
<pre><code class="language-bash">sudo -u carpet -H bash
cd /srv/carpet
git clone https://git.example.ir/team/carpet.git app
cd app
python3.12 -m venv .venv
.venv/bin/pip install -r requirements.txt gunicorn "psycopg[binary]"
nano .env                                  # DJANGO_DEBUG=0 و بقیه
.venv/bin/python manage.py migrate
.venv/bin/python manage.py collectstatic --noinput
.venv/bin/python manage.py check --deploy</code></pre>
<h3>۴. gunicorn با systemd</h3>
<pre><code class="language-ini"># /etc/systemd/system/carpet.socket
[Unit]
Description=carpet gunicorn socket

[Socket]
ListenStream=/run/carpet.sock
SocketUser=www-data

[Install]
WantedBy=sockets.target

# /etc/systemd/system/carpet.service
[Unit]
Description=carpet gunicorn
Requires=carpet.socket
After=network.target postgresql.service

[Service]
User=carpet
Group=carpet
WorkingDirectory=/srv/carpet/app
EnvironmentFile=/srv/carpet/app/.env
ExecStart=/srv/carpet/app/.venv/bin/gunicorn config.wsgi:application \
    --workers 3 --timeout 60 --max-requests 1000 --max-requests-jitter 100 \
    --access-logfile -
ExecReload=/bin/kill -s HUP $MAINPID
Restart=on-failure

[Install]
WantedBy=multi-user.target</code></pre>
<pre><code class="language-bash">sudo systemctl daemon-reload
sudo systemctl enable --now carpet.socket carpet.service
sudo systemctl status carpet
journalctl -u carpet -n 50 --no-pager</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>تعداد worker معمول <code>2 × هسته + 1</code> است، اما روی VPSهای کم‌حافظه‌ی ایرانی حافظه محدودکننده است نه CPU؛ هر worker جنگو ۸۰ تا ۱۵۰ مگابایت می‌گیرد.</li>
<li><code>--max-requests</code> هر worker را پس از چند صد درخواست بازسازی می‌کند؛ درمان ساده و مؤثر نشت حافظه‌ی تدریجی کتابخانه‌ها.</li>
<li><code>systemctl reload carpet</code> (سیگنال HUP) workerها را بدون قطع درخواست‌های در جریان عوض می‌کند؛ برای استقرار نسخه‌ی جدید به‌جای restart از آن استفاده کنید.</li>
<li>با socket activation، systemd سوکت را نگه می‌دارد و در لحظه‌ی restart درخواست‌ها در صف می‌مانند و 502 نمی‌گیرند.</li>
<li>در ایران برای pip روی سرور، میرور داخلی را در <code>/etc/pip.conf</code> تنظیم کنید و برای apt هم از مخزن‌های آینه‌ی داخلی استفاده کنید؛ نصب‌ها از ده دقیقه به چند ثانیه می‌رسند.</li>
</ul>""",
                },
                {
                    "title": "استقرار (۲): nginx، static با WhiteNoise، media، HTTPS و check --deploy",
                    "kind": "text",
                    "minutes": 26,
                    "is_preview": False,
                    "body": r"""<h2>لایه‌ی جلویی و امنیت نهایی</h2>
<p>nginx درخواست‌ها را از اینترنت می‌گیرد، HTTPS را مدیریت می‌کند، فایل‌های media را مستقیم از دیسک سرو می‌کند و بقیه را از طریق سوکت به gunicorn می‌دهد. برای static دو راه داریم: nginx مستقیم، یا <strong>WhiteNoise</strong> که فایل‌ها را فشرده و با نام هش‌دار از خود جنگو سرو می‌کند و در پشت CDN یا nginx بهترین هدرهای کش را می‌گذارد.</p>
<h3>WhiteNoise</h3>
<pre><code class="language-python"># pip install whitenoise
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",        # بلافاصله بعد از Security
    # ...
]
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"},
}</code></pre>
<h3>nginx</h3>
<pre><code class="language-nginx"># /etc/nginx/sites-available/carpet
upstream carpet_app { server unix:/run/carpet.sock fail_timeout=0; }

server {
    listen 80;
    server_name example.ir www.example.ir;
    client_max_body_size 10M;

    location /media/ {
        alias /srv/carpet/app/media/;
        expires 30d;
    }
    location /protected/ {
        internal;                                   # فقط با X-Accel-Redirect
        alias /srv/carpet/private/;
    }
    location / {
        proxy_pass http://carpet_app;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_read_timeout 60s;
    }
}</code></pre>
<pre><code class="language-bash">sudo ln -s /etc/nginx/sites-available/carpet /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
sudo apt install -y certbot python3-certbot-nginx
sudo certbot --nginx -d example.ir -d www.example.ir</code></pre>
<p>certbot گواهی Let's Encrypt را می‌گیرد، بلوک <code>listen 443 ssl</code> را به کانفیگ اضافه می‌کند و تمدید خودکار را با یک systemd timer تنظیم می‌کند.</p>
<h3>تنظیمات امنیتی production</h3>
<table><thead><tr><th>تنظیم</th><th>مقدار</th><th>اثر</th></tr></thead><tbody>
<tr><td>DEBUG</td><td>False</td><td>عدم نمایش جزئیات خطا</td></tr>
<tr><td>SECURE_PROXY_SSL_HEADER</td><td><code>("HTTP_X_FORWARDED_PROTO", "https")</code></td><td>جنگو بفهمد درخواست HTTPS بوده</td></tr>
<tr><td>SECURE_SSL_REDIRECT</td><td>True</td><td>ریدایرکت HTTP به HTTPS</td></tr>
<tr><td>SESSION_COOKIE_SECURE / CSRF_COOKIE_SECURE</td><td>True</td><td>کوکی‌ها فقط روی HTTPS</td></tr>
<tr><td>SECURE_HSTS_SECONDS</td><td>ابتدا 3600، بعد 31536000</td><td>مرورگر فقط HTTPS بزند</td></tr>
<tr><td>SECURE_HSTS_INCLUDE_SUBDOMAINS</td><td>True (با احتیاط)</td><td>HSTS برای همه‌ی زیردامنه‌ها</td></tr>
<tr><td>CSRF_TRUSTED_ORIGINS</td><td><code>["https://example.ir"]</code></td><td>عبور CSRF پشت پراکسی</td></tr>
<tr><td>X_FRAME_OPTIONS</td><td>"DENY" (پیش‌فرض)</td><td>جلوگیری از clickjacking</td></tr>
</tbody></table>
<p>در پایان <code>python manage.py check --deploy</code> را اجرا کنید؛ هر تنظیم جاافتاده را با کد هشدار (مثل security.W004 برای HSTS) گزارش می‌دهد.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>با <code>CompressedManifestStaticFilesStorage</code> اگر در قالب به فایلی اشاره کنید که وجود ندارد، با DEBUG=False خطای 500 «Missing staticfiles manifest entry» می‌گیرید؛ قبل از استقرار یک بار محلی با DEBUG=False تست کنید.</li>
<li>HSTS را اول با مقدار کوچک روشن کنید؛ اگر یک زیردامنه هنوز HTTPS ندارد و HSTS یک‌ساله با includeSubDomains فرستاده باشید، تا یک سال برای کاربرانی که سایت را دیده‌اند باز نمی‌شود.</li>
<li>بدون <code>SECURE_PROXY_SSL_HEADER</code>، <code>SECURE_SSL_REDIRECT=True</code> پشت nginx حلقه‌ی بی‌نهایت ریدایرکت می‌سازد، چون جنگو هر درخواست را HTTP می‌بیند.</li>
<li>عبارت <code>alias</code> در nginx حتماً با <code>/</code> تمام شود وقتی location هم با <code>/</code> تمام شده؛ عدم تطابق این دو منشأ خطاهای 404 مرموز media و حتی آسیب‌پذیری path traversal است.</li>
<li>Django 5.1 به بعد برای PostgreSQL گزینه‌ی <code>"OPTIONS": {"pool": True}</code> (با psycopg 3 و psycopg-pool) را دارد؛ روی سرورهای پرترافیک جایگزین سبک‌تری برای pgbouncer است.</li>
</ul>""",
                },
                {
                    "title": "پروژه‌ی پایانی: سامانه‌ی ثبت سفارش فرش",
                    "kind": "text",
                    "minutes": 30,
                    "is_preview": False,
                    "body": r"""<h2>همه‌چیز کنار هم</h2>
<p>یک کارخانه‌ی فرش ماشینی در کاشان می‌خواهد سفارش فروشگاه‌های سراسر کشور را آنلاین بگیرد. نیازها: فروشگاه‌ها با موبایل و OTP وارد شوند، طرح‌ها را با قیمت و موجودی ببینند، سفارش چندقلمی ثبت کنند و وضعیتش را پیگیری کنند؛ کارمندان فروش در ادمین سفارش‌ها را تأیید کنند؛ اپ اندرویدی بازاریاب‌ها از API استفاده کند؛ و مدیر هر ماه گزارش فروش ماه‌های شمسی را ببیند. این درس نقشه‌ی اجرای پروژه است؛ هر گام به درس‌های قبلی ارجاع دارد.</p>
<h3>گام ۱: ساختار و مدل‌ها</h3>
<table><thead><tr><th>اپ</th><th>مدل‌ها</th><th>درس مرجع</th></tr></thead><tbody>
<tr><td>accounts</td><td>User (موبایل)، OTP در Redis</td><td>۵ و ۳۰</td></tr>
<tr><td>catalog</td><td>Carpet، CarpetImage</td><td>۶ و ۲۴</td></tr>
<tr><td>orders</td><td>Customer، Order، OrderItem</td><td>۷، ۸ و ۱۰</td></tr>
<tr><td>api</td><td>Serializerها و ViewSetها</td><td>۳۱ و ۳۲</td></tr>
<tr><td>reports</td><td>بدون مدل؛ فقط کوئری و View</td><td>همین درس</td></tr>
</tbody></table>
<pre><code class="language-python"># apps/orders/models.py (بخش کلیدی)
class Order(models.Model):
    ...
    objects = OrderQuerySet.as_manager()

    def recalculate_total(self):
        agg = self.items.aggregate(s=Sum(F("quantity") * F("unit_price"), default=0))
        self.total = agg["s"] - self.discount
        self.save(update_fields=["total"])</code></pre>
<h3>گام ۲: ثبت سفارش</h3>
<p>فرم سربرگ + inline formset اقلام (درس ۲۳)، و ذخیره از طریق سرویس <code>place_order</code> با <code>atomic</code> و <code>select_for_update</code> (درس ۱۵). قیمت واحد همیشه از سرور خوانده می‌شود. بعد از commit، پیامک تأیید با Celery (درس ۳۴).</p>
<h3>گام ۳: ادمین کارمندان</h3>
<p>OrderAdmin با inline اقلام، action «تأیید» که فقط گروه «فروش» با مجوز <code>approve_order</code> می‌بیند، ستون مبلغ تومانی و تاریخ شمسی، و فیلتر سفارشی «این ماه شمسی» (درس‌های ۲۶ تا ۲۹).</p>
<h3>گام ۴: API اپ بازاریاب‌ها</h3>
<p>endpointهای <code>/api/v1/carpets/</code> (فقط‌خواندنی برای بازاریاب) و <code>/api/v1/orders/</code> (فقط سفارش‌های خودش)، با JWT و throttle جدا برای درخواست OTP.</p>
<h3>گام ۵: گزارش ماهانه‌ی شمسی</h3>
<p>TruncMonth ماه میلادی می‌دهد؛ پس بازه‌ی هر ماه شمسی را با jdatetime می‌سازیم و با یک کوئری aggregate برای هر ماه جمع می‌زنیم:</p>
<pre><code class="language-python"># apps/reports/services.py
import datetime

import jdatetime
from django.db.models import Count, Sum
from django.utils import timezone

from apps.orders.models import Order

MONTHS = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور",
          "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]


def jalali_month_range(jy, jm):
    start = jdatetime.date(jy, jm, 1).togregorian()
    ny, nm = (jy + 1, 1) if jm == 12 else (jy, jm + 1)
    end = jdatetime.date(ny, nm, 1).togregorian()
    tz = timezone.get_current_timezone()
    return (timezone.make_aware(datetime.datetime.combine(start, datetime.time.min), tz),
            timezone.make_aware(datetime.datetime.combine(end, datetime.time.min), tz))


def yearly_report(jy):
    rows = []
    paid = Order.objects.filter(status__in=["paid", "shipped"])
    for jm in range(1, 13):
        start, end = jalali_month_range(jy, jm)
        agg = paid.filter(created_at__gte=start, created_at__lt=end).aggregate(
            n=Count("id"), total=Sum("total", default=0))
        rows.append({"month": MONTHS[jm - 1], **agg})
    return rows</code></pre>
<p>View گزارش با <code>PermissionRequiredMixin</code> و <code>cache_page</code> یک‌ساعته، و قالب با فیلتر <code>toman</code> (درس ۲۰). برای خروجی اکسل می‌توانید همین rows را با openpyxl بنویسید.</p>
<h3>گام ۶: تست و استقرار</h3>
<p>دست‌کم این تست‌ها: دسترسی نداشتن کاربر به سفارش دیگران، rollback در کمبود موجودی، تعداد کوئری فهرست سفارش‌ها و اعتبارسنجی کد ملی. سپس استقرار طبق درس‌های ۳۷ و ۳۸ و اجرای <code>check --deploy</code> بدون هشدار.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>ماه‌های اسفند ۲۹ یا ۳۰ روزه‌اند؛ با گرفتن «اول ماه بعد» به‌عنوان مرز انتهایی (مثل کد بالا) هرگز لازم نیست طول ماه را حساب کنید.</li>
<li>دوازده کوئری aggregate برای گزارش سالانه کاملاً قابل‌قبول است؛ اگر ماهانه صدها گزارش می‌خواهید، به‌جای آن ستونی با کد ماه شمسی (مثلاً ۱۴۰۴۰۸) هنگام ذخیره‌ی سفارش بسازید و روی آن GROUP BY کنید.</li>
<li><code>Sum(F("quantity") * F("unit_price"))</code> ضرب را در SQL انجام می‌دهد؛ برای جلوگیری از سرریز روی جمع‌های بزرگ، هر دو ستون را BigInteger نگه دارید.</li>
<li>پیش از راه‌اندازی، داده‌ی آزمایشی واقع‌گرایانه (چند هزار سفارش با factory) بسازید و صفحات را با debug-toolbar بسنجید؛ مشکلات N+1 با ده رکورد دیده نمی‌شوند.</li>
<li>تاریخچه‌ی تغییر وضعیت سفارش را در یک مدل جدا (OrderEvent با کاربر و زمان) ثبت کنید؛ اولین سؤال مدیر بعد از هر مشکل «چه کسی و کی؟» است.</li>
</ul>""",
                },
                {
                    "title": "کلینیک خطاهای رایج جنگو: علت و درمان",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>خطا را بخوانید، نه این‌که فقط گوگل کنید</h2>
<p>بیشتر خطاهای جنگو پیام دقیقی دارند؛ مشکل این است که ما پیام را کامل نمی‌خوانیم. این درس پرتکرارترین خطاهایی را جمع کرده که در پروژه‌های واقعی، به‌خصوص هنگام اولین استقرار، دیده می‌شوند.</p>
<table><thead><tr><th>خطا</th><th>علت رایج</th><th>درمان</th></tr></thead><tbody>
<tr><td>TemplateDoesNotExist</td><td>قالب در مسیر مورد انتظار نیست یا <code>DIRS</code> تنظیم نشده</td><td>پیام «Template-loader postmortem» را بخوانید؛ مسیرهای بررسی‌شده را نشان می‌دهد. <code>TEMPLATES["DIRS"] = [BASE_DIR / "templates"]</code> و پوشه‌ی <code>templates/&lt;app&gt;/</code> داخل اپ</td></tr>
<tr><td>NoReverseMatch</td><td>نام url یا namespace اشتباه، یا آرگومان جاافتاده/خالی</td><td>متغیر خالی مثل <code>pk=""</code> را بررسی کنید؛ namespace را با <code>app_name</code> تطبیق دهید</td></tr>
<tr><td>static در DEBUG=False کار نمی‌کند</td><td>runserver فقط با DEBUG=True static سرو می‌کند</td><td>collectstatic + WhiteNoise یا location در nginx</td></tr>
<tr><td>403 CSRF verification failed پشت پراکسی</td><td>CSRF_TRUSTED_ORIGINS بدون scheme، یا نبود X-Forwarded-Proto</td><td><code>https://</code> در CSRF_TRUSTED_ORIGINS و SECURE_PROXY_SSL_HEADER</td></tr>
<tr><td>Conflicting migrations detected</td><td>دو migration هم‌شماره از دو شاخه</td><td><code>makemigrations --merge</code></td></tr>
<tr><td>no such table / relation does not exist</td><td>migrate اجرا نشده، یا migration اپ ساخته نشده</td><td><code>showmigrations</code>؛ بعد makemigrations همان اپ و migrate</td></tr>
<tr><td>DisallowedHost</td><td>دامنه یا IP در ALLOWED_HOSTS نیست</td><td>افزودن دامنه (بدون http و پورت)</td></tr>
<tr><td>RuntimeWarning: naive datetime</td><td><code>datetime.now()</code> با USE_TZ=True</td><td><code>timezone.now()</code> یا <code>make_aware</code></td></tr>
<tr><td>ImproperlyConfigured: SECRET_KEY</td><td>.env خوانده نشده؛ معمولاً مسیر اشتباه در systemd</td><td><code>EnvironmentFile</code> و <code>load_dotenv(BASE_DIR / ".env")</code></td></tr>
<tr><td>502 Bad Gateway</td><td>gunicorn بالا نیامده یا سوکت در دسترس nginx نیست</td><td><code>journalctl -u carpet</code> و دسترسی www-data به سوکت</td></tr>
<tr><td>pip timeout / 403 در ایران</td><td>تحریم یا اختلال شبکه</td><td>میرور داخلی PyPI با <code>pip config set global.index-url</code></td></tr>
</tbody></table>
<h3>روش عیب‌یابی گام‌به‌گام</h3>
<pre><code class="language-bash"># ۱. پیکربندی سالم است؟
python manage.py check
python manage.py check --deploy
# ۲. وضعیت migrationها
python manage.py showmigrations | grep "\[ \]"
# ۳. آدرس به کدام View می‌رسد؟
python manage.py shell -c "from django.urls import resolve; print(resolve('/orders/42/'))"
# ۴. لاگ سرویس‌ها روی سرور
journalctl -u carpet -n 100 --no-pager
sudo tail -n 50 /var/log/nginx/error.log</code></pre>
<h3>وقتی DEBUG=False است و خطا را نمی‌بینید</h3>
<p>هرگز برای دیدن خطا DEBUG را روی سرور روشن نکنید. به‌جایش <code>ADMINS</code> را تنظیم کنید تا خطاهای 500 ایمیل شوند، لاگر <code>django.request</code> را در سطح ERROR به فایل بفرستید، یا یک سرویس گزارش خطا مثل Sentry (نسخه‌ی self-hosted برای شرایط تحریم) نصب کنید.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>اگر TemplateDoesNotExist برای قالبی می‌آید که مطمئنید وجود دارد، به نام قالب داخل پیام دقت کنید: ListView بدون template_name دنبال <code>orders/order_list.html</code> می‌گردد، نه list.html.</li>
<li>NoReverseMatch با پیام «with arguments ('',)» یعنی url درست است اما مقدار ارسالی خالی بوده؛ معمولاً شیء هنوز ذخیره نشده و pk ندارد.</li>
<li>«no such table: django_session» در اولین اجرا یعنی حتی migrationهای خود جنگو اجرا نشده‌اند؛ یک <code>migrate</code> ساده کافی است.</li>
<li>خطای «Apps aren't loaded yet» معمولاً یعنی در یک اسکریپت مستقل قبل از <code>django.setup()</code> مدل import کرده‌اید، یا در models.py یک import حلقوی دارید.</li>
<li>تغییرات کد روی سرور بدون <code>systemctl reload carpet</code> اعمال نمی‌شوند؛ gunicorn کد را فقط هنگام شروع worker بارگذاری می‌کند و «کد را عوض کردم ولی فرقی نکرد» از همین است.</li>
</ul>""",
                },
            ],
        },
    ],
}

# -*- coding: utf-8 -*-
# دوره‌ی جامع پایتون از صفر — ۸ فصل، ۴۰ درس. متن‌ها r""" هستند تا بک‌اسلش‌های کد (\n، \d، مسیرهای ویندوز) دست‌نخورده بمانند.

COURSE = {
    "slug": "python-basics",
    "title": "آموزش جامع پایتون (از صفر)",
    "category": "برنامه‌نویسی",
    "level": "beginner",
    "summary": "از نصب درست روی ویندوز و venv تا داده‌ها، توابع، فایل‌های فارسی، شیءگرایی، تست و یک پروژه‌ی واقعی مدیریت سفارش فرش — پایتون ۳.۱۲ به زبان ساده اما دقیق.",
    "description": (
        "<p>این دوره برای کسی نوشته شده که می‌خواهد پایتون را <strong>درست</strong> یاد بگیرد، نه فقط «کار راه‌انداز»: "
        "دانشجویی که اولین زبانش را شروع می‌کند، کارمندی که می‌خواهد کارهای تکراری اکسل و فایل را خودکار کند، یا "
        "برنامه‌نویسی که از زبان دیگری می‌آید و می‌خواهد پایتونیک فکر کند. از صفر شروع می‌کنیم و فرض نمی‌کنیم چیزی "
        "از قبل می‌دانید.</p>"
        "<p>مسیر دوره: نصب اصولی روی ویندوز (PATH، py launcher، <strong>venv</strong> در PowerShell و میرورهای ایرانی pip)، "
        "انواع داده با تمرکز روی دام‌های واقعی (0.1+0.2، پول با <strong>Decimal</strong>، یونیکد فارسی، نیم‌فاصله و ارقام فارسی)، "
        "کنترل جریان و match/case، ساختارهای داده و collections، توابع و scope، فایل‌های UTF-8 و CSV مخصوص اکسل فارسی، "
        "مدیریت خطا و logging، ماژول‌ها، تاریخ شمسی با jdatetime، کلاس و dataclass، و در پایان یک پروژه‌ی خط فرمان "
        "«مدیریت سفارش فرش» همراه با requests، pytest، دیباگر و کلینیک خطاهای رایج.</p>"
        "<p>پیش‌نیاز: فقط کار با کامپیوتر. همه‌ی مثال‌ها روی Python 3.12 به بالا و ویندوز با PowerShell نوشته شده‌اند "
        "(تفاوت‌های لینوکس و مک هرجا مهم باشد گفته می‌شود). هر درس با بخش «نکته‌هایی که کمتر کسی می‌داند» تمام می‌شود؛ "
        "همان چیزهایی که معمولاً بعد از چند سال و چند باگ عجیب یاد گرفته می‌شوند.</p>"
    ),
    "price": 0,
    "duration_minutes": 862,
    "tags": ["پایتون", "برنامه‌نویسی", "مقدماتی"],
    "modules": [
        # ───────────────────────────── فصل ۱ ─────────────────────────────
        {
            "title": "فصل ۱: شروع درست — نصب، ابزارها و محیط مجازی",
            "lessons": [
                {
                    "title": "پایتون چیست، کجا به کار می‌رود و این دوره چطور پیش می‌رود",
                    "kind": "text",
                    "minutes": 16,
                    "is_preview": True,
                    "body": r"""<h2>زبانی که برای خوانده شدن طراحی شد</h2>
<p>پایتون را خیدو فان روسوم در اوایل دهه‌ی ۱۹۹۰ ساخت و از همان روز اول یک اصل داشت: <strong>کد بیشتر خوانده می‌شود تا نوشته</strong>. به همین دلیل پایتون به‌جای آکولاد از تورفتگی (indentation) برای مشخص کردن بلوک‌ها استفاده می‌کند، کلمات کلیدی‌اش به انگلیسی ساده نزدیک‌اند و معمولاً «یک راه واضح» برای انجام هر کار وجود دارد. اگر در ترمینال پایتون بنویسید <code>import this</code>، متنی به نام «ذن پایتون» ظاهر می‌شود که همین فلسفه را در ۱۹ جمله خلاصه کرده است.</p>
<p>پایتون یک زبان <strong>تفسیری</strong> (دقیق‌تر: کامپایل به بایت‌کد و اجرا روی ماشین مجازی CPython) و <strong>پویا</strong> (dynamic typing) است: لازم نیست نوع متغیر را اعلام کنید و برنامه را خط‌به‌خط می‌توانید امتحان کنید. بهای این راحتی، سرعت اجرای کمتر از C یا Go در حلقه‌های سنگین است؛ اما در عمل بیشتر کارهای سنگین پایتون (NumPy، pandas، کتابخانه‌های هوش مصنوعی) در لایه‌ی زیرین با C نوشته شده‌اند و پایتون نقش «چسب» هوشمند را دارد.</p>
<h3>پایتون کجا به کار می‌رود؟</h3>
<table><thead><tr><th>حوزه</th><th>ابزارهای رایج</th><th>مثال واقعی</th></tr></thead><tbody>
<tr><td>وب و API</td><td>Django، FastAPI، Flask</td><td>سامانه‌ی ثبت سفارش یک کارگاه فرش</td></tr>
<tr><td>تحلیل داده</td><td>pandas، matplotlib، Jupyter</td><td>گزارش فروش ماهانه از فایل اکسل</td></tr>
<tr><td>هوش مصنوعی و بینایی ماشین</td><td>PyTorch، OpenCV، scikit-learn</td><td>تشخیص خرابی بافت در تصویر فرش ماشینی</td></tr>
<tr><td>اتوماسیون</td><td>pathlib، openpyxl، requests</td><td>تغییر نام هزار فایل، ارسال گزارش روزانه</td></tr>
<tr><td>ابزارهای سیستمی و DevOps</td><td>Ansible، اسکریپت‌های CLI</td><td>پشتیبان‌گیری خودکار از دیتابیس</td></tr>
</tbody></table>
<h3>اولین نگاه به کد</h3>
<p>این چند خط را فعلاً فقط بخوانید؛ تا پایان فصل دوم همه‌ی اجزایش را کامل می‌فهمید:</p>
<pre><code class="language-python">orders = {"کاشان": 12, "تبریز": 7, "مشهد": 9}

for city, count in orders.items():
    print(f"{city}: {count} سفارش")

total = sum(orders.values())
print(f"جمع کل: {total:,} سفارش")</code></pre>
<p>نه نقطه‌ویرگولی، نه آکولادی، نه اعلان نوعی. همین خوانایی است که پایتون را به محبوب‌ترین زبان آموزشی و یکی از پراستفاده‌ترین زبان‌های صنعتی تبدیل کرده است.</p>
<h3>این دوره چطور پیش می‌رود</h3>
<ul>
<li><strong>فصل ۱</strong>: محیط کار را درست می‌سازیم؛ نصب، VS Code، venv و pip با میرور ایرانی. نصب اشتباه منشأ نیمی از مشکلات بعدی است.</li>
<li><strong>فصل ۲ تا ۵</strong>: زبان را از داده تا تابع یاد می‌گیریم، با تأکید روی دام‌هایی که حتی برنامه‌نویسان باتجربه در آن‌ها می‌افتند.</li>
<li><strong>فصل ۶ و ۷</strong>: فایل، خطا، ماژول، تاریخ شمسی و شیءگرایی؛ یعنی ابزارهای نوشتن برنامه‌ی واقعی.</li>
<li><strong>فصل ۸</strong>: یک پروژه‌ی کامل خط فرمان، کار با API، تست، دیباگ و کلینیک خطاها.</li>
</ul>
<p>توصیه‌ی جدی: هر کد را خودتان تایپ کنید، نه کپی. انگشت‌ها چیزهایی را یاد می‌گیرند که چشم از رویشان رد می‌شود.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>نام پایتون از مار نیامده، از گروه کمدی «Monty Python» آمده است؛ به همین دلیل در مستندات رسمی به‌جای foo و bar اغلب spam و eggs می‌بینید.</li>
<li>«پایتون» در واقع یک مشخصات زبان است و CPython فقط رایج‌ترین پیاده‌سازی آن. PyPy (با کامپایلر JIT) گاهی حلقه‌های خالص پایتونی را چند برابر سریع‌تر اجرا می‌کند.</li>
<li>Python 2 از سال ۲۰۲۰ رسماً مرده است. اگر آموزشی دیدید که <code>print "hello"</code> بدون پرانتز نوشته، آن را کنار بگذارید.</li>
<li>هر نسخه‌ی پایتون حدود پنج سال پشتیبانی امنیتی دارد و هر سال در ماه اکتبر یک نسخه‌ی جدید منتشر می‌شود؛ برای پروژه‌ی تازه همیشه یکی از دو نسخه‌ی آخر را انتخاب کنید.</li>
<li>نوشتن <code>import antigravity</code> در پایتون یک کمیک مشهور را در مرورگر باز می‌کند؛ نشانه‌ای از فرهنگ شوخ‌طبع جامعه‌ی پایتون.</li>
</ul>""",
                },
                {
                    "title": "نصب پایتون روی ویندوز: Add to PATH، py launcher و تفاوت python و py",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>نصبی که بعداً دردسر نسازد</h2>
<p>بیشترِ «پایتونم کار نمی‌کند»ها در ویندوز به همان سی ثانیه‌ی نصب برمی‌گردد. نصاب رسمی را (نسخه‌ی 64-bit، Python 3.12 یا جدیدتر) از سایت رسمی پایتون بگیرید و در <strong>اولین صفحه</strong> دقت کنید:</p>
<ol>
<li>تیک <strong>Add python.exe to PATH</strong> را بزنید. بدون آن، دستور <code>python</code> در ترمینال شناخته نمی‌شود.</li>
<li>تیک <strong>Use admin privileges when installing py.exe</strong> را نگه دارید تا py launcher برای همه‌ی کاربران نصب شود.</li>
<li>اگر نام کاربری ویندوزتان فارسی است یا فاصله دارد، از <strong>Customize installation</strong> مسیر را به چیزی مثل <code>C:\Python312</code> تغییر دهید؛ بعضی ابزارها هنوز با مسیرهای یونیکد مشکل دارند.</li>
<li>در پایان، گزینه‌ی <strong>Disable path length limit</strong> را بزنید تا محدودیت ۲۶۰ کاراکتری مسیر در ویندوز برداشته شود.</li>
</ol>
<h3>PATH دقیقاً چیست؟</h3>
<p>PATH فهرستی از پوشه‌هاست که ویندوز وقتی دستوری مثل <code>python</code> را تایپ می‌کنید، به ترتیب در آن‌ها دنبال فایل اجرایی می‌گردد. اولین موردی که پیدا شود اجرا می‌شود. پس اگر دو پایتون نصب دارید، ترتیب PATH تعیین می‌کند کدام اجرا شود. برای دیدن این‌که واقعاً کدام فایل اجرا می‌شود:</p>
<pre><code class="language-powershell">python --version
Get-Command python
where.exe python
py --list</code></pre>
<h3>python در برابر py</h3>
<table><thead><tr><th>دستور</th><th>چیست</th><th>کی استفاده کنیم</th></tr></thead><tbody>
<tr><td><code>python</code></td><td>اولین python.exe در PATH</td><td>داخل venv فعال (فصل بعد) یا وقتی فقط یک نسخه دارید</td></tr>
<tr><td><code>py</code></td><td>Python Launcher ویندوز؛ خودش نسخه را انتخاب می‌کند</td><td>بیرون از venv، مخصوصاً با چند نسخه‌ی نصب‌شده</td></tr>
<tr><td><code>py -3.12</code></td><td>اجرای دقیق نسخه‌ی 3.12</td><td>ساخت venv با نسخه‌ی مشخص</td></tr>
<tr><td><code>py --list</code></td><td>فهرست همه‌ی نسخه‌های نصب‌شده</td><td>عیب‌یابی</td></tr>
</tbody></table>
<p>py launcher مستقل از PATH کار می‌کند و به همین دلیل حتی اگر تیک PATH را فراموش کرده باشید، <code>py</code> معمولاً کار می‌کند. قاعده‌ی عملی: <strong>بیرون از venv از <code>py</code> و داخل venv از <code>python</code> استفاده کنید.</strong></p>
<h3>دام Microsoft Store</h3>
<p>اگر <code>python</code> را تایپ کنید و به‌جای پایتون، Microsoft Store باز شود یا هیچ خروجی‌ای نبینید، ویندوز یک «میان‌بر جعلی» به نام App execution alias دارد که جلوتر از پایتون واقعی در PATH نشسته است. راه‌حل: Settings ← Apps ← Advanced app settings ← <strong>App execution aliases</strong> و خاموش کردن دو مورد python.exe و python3.exe. بعد ترمینال را ببندید و دوباره باز کنید.</p>
<p>برای اطمینان نهایی، این را اجرا کنید تا مسیر دقیق مفسر را ببینید:</p>
<pre><code class="language-powershell">py -c "import sys; print(sys.version); print(sys.executable)"</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>تغییر PATH فقط روی ترمینال‌هایی اثر دارد که <em>بعد از</em> تغییر باز شده‌اند؛ VS Code را هم باید کامل ببندید و باز کنید، نه فقط تب ترمینالش را.</li>
<li>اگر اولین خط اسکریپت <code>#!/usr/bin/env python3.12</code> باشد، py launcher (وقتی با <code>py script.py</code> اجرا کنید) آن را می‌خواند و همان نسخه را انتخاب می‌کند؛ یعنی shebang لینوکسی در ویندوز هم بی‌اثر نیست.</li>
<li>نصب مجدد با همان نصاب، گزینه‌ی <strong>Modify</strong> و <strong>Repair</strong> دارد؛ اگر PATH را فراموش کرده‌اید، لازم نیست پایتون را حذف کنید.</li>
<li>در ویندوز فایل <code>python3.exe</code> معمولاً وجود ندارد (جز همان alias استور)؛ دستورهای آموزش‌های لینوکسی را با <code>py</code> جایگزین کنید.</li>
<li>متغیر محیطی <code>PY_PYTHON=3.12</code> نسخه‌ی پیش‌فرض py launcher را تعیین می‌کند، بدون این‌که به PATH دست بزنید.</li>
</ul>""",
                },
                {
                    "title": "VS Code، افزونه‌ها، REPL و اولین برنامه",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>ابزاری که هر روز با آن کار می‌کنید</h2>
<p>برای پایتون چند ویرایشگر خوب هست (PyCharm، VS Code، حتی IDLE که همراه پایتون نصب می‌شود). در این دوره از <strong>VS Code</strong> استفاده می‌کنیم: رایگان، سبک و با بهترین پشتیبانی از venv و دیباگ. بعد از نصب، این افزونه‌ها را از بخش Extensions (Ctrl+Shift+X) نصب کنید:</p>
<table><thead><tr><th>افزونه</th><th>کاربرد</th></tr></thead><tbody>
<tr><td>Python (ناشر Microsoft)</td><td>اجرای کد، انتخاب مفسر، دیباگ؛ Pylance و Python Debugger را هم خودکار نصب می‌کند</td></tr>
<tr><td>Pylance</td><td>تکمیل خودکار، نمایش خطای نوع و پرش به تعریف توابع</td></tr>
<tr><td>Ruff</td><td>linter و formatter بسیار سریع؛ کد را طبق PEP 8 مرتب می‌کند</td></tr>
<tr><td>Error Lens (اختیاری)</td><td>پیام خطا را همان کنار خط نشان می‌دهد</td></tr>
</tbody></table>
<p>مهم‌ترین تنظیم: با Ctrl+Shift+P دستور <strong>Python: Select Interpreter</strong> را اجرا کنید و مفسر درست را انتخاب کنید. نام مفسر انتخاب‌شده در نوار وضعیت پایین پنجره دیده می‌شود. اگر کتابخانه‌ای نصب کرده‌اید ولی VS Code می‌گوید پیدا نمی‌شود، تقریباً همیشه مفسر اشتباه انتخاب شده است.</p>
<h3>REPL: آزمایشگاه جیبی</h3>
<p>در ترمینال <code>py</code> را بدون آرگومان بزنید تا علامت <code>&gt;&gt;&gt;</code> ظاهر شود. این همان <strong>REPL</strong> (Read-Eval-Print Loop) است: هر عبارت را می‌خواند، اجرا می‌کند و نتیجه را چاپ می‌کند. برای امتحان سریع یک ایده بهترین جاست:</p>
<pre><code class="language-python">&gt;&gt;&gt; 12 * 3.5
42.0
&gt;&gt;&gt; "کاشان".upper()
'کاشان'
&gt;&gt;&gt; _ + " — شهر فرش"
'کاشان — شهر فرش'
&gt;&gt;&gt; help(str.split)
&gt;&gt;&gt; exit()</code></pre>
<p>از Python 3.13 به بعد REPL جدید رنگی است، ورودی چندخطی را درست ویرایش می‌کند و <code>exit</code> را بدون پرانتز هم می‌فهمد.</p>
<h3>اولین برنامه‌ی واقعی</h3>
<p>یک پوشه بسازید (مثلاً <code>D:\projects\hello</code>)، آن را با File ← Open Folder در VS Code باز کنید و فایلی به نام <code>hello.py</code> بسازید:</p>
<pre><code class="language-python">name = input("نام شما: ")
rugs = int(input("چند تخته فرش سفارش می‌دهید؟ "))
print(f"سلام {name}! سفارش {rugs} تخته فرش ثبت شد.")</code></pre>
<p>اجرا از ترمینال یکپارچه‌ی VS Code (Ctrl+`):</p>
<pre><code class="language-powershell">py hello.py</code></pre>
<p>یا با دکمه‌ی مثلث Run در بالای ویرایشگر. اگر در ترمینال ویندوز حروف فارسی به‌صورت علامت سؤال یا مربع دیده شد، مشکل از فونت ترمینال است نه از پایتون؛ در تنظیمات Windows Terminal فونتی مثل Cascadia Code یا Vazir Code را انتخاب کنید.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>در REPL متغیر <code>_</code> همیشه نتیجه‌ی آخرین عبارت را نگه می‌دارد؛ برای ماشین‌حساب بازی عالی است (فقط در REPL، نه در فایل).</li>
<li><code>py -i hello.py</code> فایل را اجرا می‌کند و بعد در REPL می‌ماند تا متغیرهای برنامه را بررسی کنید؛ یک دیباگر ساده‌ی رایگان.</li>
<li>در VS Code با انتخاب چند خط و زدن Shift+Enter همان خط‌ها در REPL پایتون اجرا می‌شوند؛ لازم نیست کل فایل را اجرا کنید.</li>
<li>فایل را هرگز با نام کتابخانه‌ها (مثل <code>random.py</code>، <code>json.py</code> یا <code>requests.py</code>) ذخیره نکنید؛ پایتون فایل شما را به‌جای کتابخانه‌ی واقعی import می‌کند و خطاهای عجیب می‌دهد.</li>
<li>تنظیم <code>"editor.formatOnSave": true</code> همراه با Ruff باعث می‌شود هر بار ذخیره، کد خودکار مرتب شود؛ دعوای تیمی سر فاصله‌ها برای همیشه تمام می‌شود.</li>
</ul>""",
                },
                {
                    "title": "محیط مجازی venv در PowerShell: چرا، چطور و دام ExecutionPolicy",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>هر پروژه، جعبه‌ی خودش</h2>
<p>فرض کنید پروژه‌ی A به Django 4.2 نیاز دارد و پروژه‌ی B به Django 5.1. اگر هر دو کتابخانه را در پایتون اصلی سیستم نصب کنید، فقط یکی می‌تواند وجود داشته باشد. <strong>محیط مجازی</strong> (virtual environment) یک پوشه است که یک کپی سبک از مفسر و پوشه‌ی مخصوص کتابخانه‌ها را در خود دارد؛ هر پروژه کتابخانه‌های خودش را دارد و به بقیه دست نمی‌زند. قاعده‌ی حرفه‌ای ساده است: <strong>برای هر پروژه یک venv، و هیچ‌وقت نصب در پایتون سراسری.</strong></p>
<h3>ساخت و فعال‌سازی در PowerShell</h3>
<pre><code class="language-powershell">cd D:\projects\carpet-orders
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python --version
python -c "import sys; print(sys.prefix)"</code></pre>
<p>بعد از فعال‌سازی، ابتدای خط فرمان <code>(.venv)</code> ظاهر می‌شود و دستور <code>python</code> به مفسر داخل پوشه‌ی <code>.venv</code> اشاره می‌کند. برای خروج کافی است <code>deactivate</code> را بزنید. نام <code>.venv</code> یک قرارداد رایج است و VS Code آن را خودکار تشخیص می‌دهد.</p>
<h3>خطای «running scripts is disabled on this system»</h3>
<p>ویندوز به‌طور پیش‌فرض اجرای اسکریپت‌های PowerShell (از جمله <code>Activate.ps1</code>) را ممنوع می‌کند. راه‌حل امن این است که فقط برای کاربر خودتان اجازه‌ی اسکریپت‌های محلی را بدهید:</p>
<pre><code class="language-powershell">Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
Get-ExecutionPolicy -List</code></pre>
<p><code>RemoteSigned</code> یعنی اسکریپت‌هایی که روی سیستم خودتان ساخته شده‌اند اجرا می‌شوند، ولی اسکریپت دانلودشده از اینترنت باید امضا داشته باشد. این دستور نیاز به Administrator ندارد و فقط یک بار لازم است. اگر سازمانتان با Group Policy این تنظیم را قفل کرده، می‌توانید برای یک جلسه‌ی موقت از <code>Set-ExecutionPolicy -Scope Process Bypass</code> استفاده کنید.</p>
<h3>ساختار پوشه‌ی venv</h3>
<table><thead><tr><th>مسیر</th><th>محتوا</th></tr></thead><tbody>
<tr><td><code>.venv\Scripts\python.exe</code></td><td>مفسر محیط (در لینوکس و مک: <code>.venv/bin/python</code>)</td></tr>
<tr><td><code>.venv\Scripts\Activate.ps1</code></td><td>اسکریپت فعال‌سازی PowerShell (برای cmd: <code>activate.bat</code>)</td></tr>
<tr><td><code>.venv\Lib\site-packages</code></td><td>کتابخانه‌های نصب‌شده‌ی همین پروژه</td></tr>
<tr><td><code>.venv\pyvenv.cfg</code></td><td>مسیر پایتون پایه و نسخه‌ی آن</td></tr>
</tbody></table>
<h3>venv را جزو پروژه حساب نکنید</h3>
<p>پوشه‌ی <code>.venv</code> قابل‌انتقال نیست: مسیرهای مطلق داخلش نوشته شده است. آن را در <code>.gitignore</code> بگذارید، کپی نکنید و در زیپ پروژه نفرستید. آنچه باید منتقل شود فهرست کتابخانه‌هاست (<code>requirements.txt</code>، درس بعد)؛ هرکس با آن می‌تواند در یک دقیقه محیط را از نو بسازد. اگر venv خراب شد یا نسخه‌ی پایتون را عوض کردید، ساده‌ترین راه حذف پوشه و ساخت دوباره است.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>فعال‌سازی اجباری نیست: <code>.\.venv\Scripts\python.exe script.py</code> همان کار را می‌کند. در Task Scheduler و سرویس‌های ویندوز همیشه همین مسیر کامل را بدهید، چون آن‌جا کسی Activate نمی‌کند.</li>
<li>اگر پوشه‌ی پروژه را جابه‌جا یا تغییر نام دهید، venv نیمه‌خراب می‌شود (pip به مسیر قدیمی اشاره می‌کند)؛ به‌جای تعمیر، آن را دوباره بسازید.</li>
<li><code>py -m venv .venv --upgrade-deps</code> هنگام ساخت، pip داخل محیط را هم به آخرین نسخه ارتقا می‌دهد.</li>
<li>VS Code وقتی پوشه‌ی <code>.venv</code> را در ریشه‌ی پروژه ببیند، ترمینال‌های جدید را خودکار فعال می‌کند؛ اگر نکرد، یک‌بار Select Interpreter را روی همان venv بزنید.</li>
<li>در cmd قدیمی به‌جای Activate.ps1 باید <code>.venv\Scripts\activate.bat</code> اجرا شود و ExecutionPolicy آن‌جا اصلاً مطرح نیست.</li>
</ul>""",
                },
                {
                    "title": "pip، میرورهای ایرانی و requirements.txt",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>نصب کتابخانه بدون درد تحریم</h2>
<p><strong>pip</strong> مدیر بسته‌ی رسمی پایتون است و کتابخانه‌ها را از مخزن PyPI دانلود می‌کند. همیشه آن را به شکل <code>python -m pip</code> صدا بزنید، نه فقط <code>pip</code>؛ این‌طوری مطمئن هستید بسته دقیقاً برای همان پایتونی نصب می‌شود که <code>python</code> به آن اشاره دارد.</p>
<pre><code class="language-powershell">python -m pip install requests
python -m pip install "django&gt;=5.0,&lt;5.2"
python -m pip list
python -m pip show requests
python -m pip uninstall requests</code></pre>
<h3>میرور ایرانی</h3>
<p>دسترسی مستقیم به PyPI از ایران گاهی کند است، قطع می‌شود یا به‌خاطر تحریم خطای 403 می‌دهد. چند سرویس ابری ایرانی (مثل رانفلر، لیارا و آروان) آینه‌ی PyPI دارند. می‌توانید برای یک دستور یا برای همیشه از میرور استفاده کنید:</p>
<pre><code class="language-powershell">python -m pip install jdatetime -i https://mirror-pypi.runflare.com/simple
python -m pip config set global.index-url https://mirror-pypi.runflare.com/simple
python -m pip config set global.timeout 60
python -m pip config list
python -m pip config debug</code></pre>
<p>تنظیم دائمی در فایل <code>%APPDATA%\pip\pip.ini</code> ذخیره می‌شود. آدرس دقیق هر میرور ممکن است تغییر کند؛ آن را از مستندات همان سرویس بگیرید و اگر یک میرور از کار افتاد، دیگری را امتحان کنید. اگر میرور با گواهی SSL مشکل داشت، راه درست <code>global.trusted-host</code> برای همان دامنه است، نه خاموش کردن کامل بررسی امنیتی.</p>
<h3>requirements.txt: فهرست خرید پروژه</h3>
<p>این فایل می‌گوید پروژه به چه کتابخانه‌هایی با چه نسخه‌ای نیاز دارد. دو روش رایج:</p>
<table><thead><tr><th>روش</th><th>دستور</th><th>مزیت / عیب</th></tr></thead><tbody>
<tr><td>freeze کامل</td><td><code>python -m pip freeze</code></td><td>همه‌ی بسته‌ها با نسخه‌ی دقیق؛ تکرارپذیر اما شلوغ</td></tr>
<tr><td>دستی</td><td>نوشتن فقط بسته‌های اصلی</td><td>خوانا؛ اما نسخه‌ی وابستگی‌ها ثابت نیست</td></tr>
</tbody></table>
<p>یک requirements دستی خوب چنین شکلی دارد:</p>
<pre><code class="language-python"># requirements.txt
requests&gt;=2.32,&lt;3
jdatetime&gt;=4.1
pytest&gt;=8        # فقط برای توسعه</code></pre>
<p>و در سیستم جدید یا روی سرور:</p>
<pre><code class="language-powershell">py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>در Windows PowerShell 5.1، دستور <code>pip freeze &gt; requirements.txt</code> فایل را با کدگذاری UTF-16 می‌سازد؛ pip آن را می‌خواند ولی git و ابزارهای دیگر آن را باینری می‌بینند. بنویسید <code>python -m pip freeze | Out-File -Encoding utf8 requirements.txt</code> (در PowerShell 7 مشکلی نیست).</li>
<li><code>pip install --user</code> را داخل venv هرگز نزنید؛ بسته به پوشه‌ی کاربر می‌رود و venv آن را نمی‌بیند.</li>
<li>متغیر محیطی <code>PIP_INDEX_URL</code> بر pip.ini اولویت دارد؛ اگر میرورتان «عوض نمی‌شود»، <code>pip config debug</code> نشان می‌دهد تنظیم از کجا می‌آید.</li>
<li><code>python -m pip download -r requirements.txt -d wheels</code> همه‌ی بسته‌ها را دانلود می‌کند؛ روی سرور بدون اینترنت با <code>pip install --no-index --find-links wheels -r requirements.txt</code> نصب کنید.</li>
<li>برای سرعت، ابزار جدید <code>uv</code> همان کار pip و venv را ده‌ها برابر سریع‌تر انجام می‌دهد و با <code>UV_INDEX_URL</code> با میرور ایرانی هم کار می‌کند؛ بعد از مسلط شدن به pip امتحانش کنید.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۲ ─────────────────────────────
        {
            "title": "فصل ۲: داده‌ها — متغیر، عدد، پول، متن فارسی و ورودی",
            "lessons": [
                {
                    "title": "متغیر، نام‌گذاری و PEP 8: متغیر برچسب است، نه جعبه",
                    "kind": "text",
                    "minutes": 18,
                    "is_preview": False,
                    "body": r"""<h2>مدل ذهنی درست از همین ابتدا</h2>
<p>در بسیاری از کتاب‌ها متغیر را «جعبه‌ای که مقدار در آن ریخته می‌شود» معرفی می‌کنند. برای پایتون این تصویر گمراه‌کننده است. در پایتون هر مقدار یک <strong>شیء</strong> (object) در حافظه است و متغیر فقط یک <strong>نام یا برچسب</strong> است که به آن شیء چسبانده می‌شود. عبارت <code>price = 1200000</code> یعنی «یک شیء عدد صحیح بساز و برچسب price را به آن بزن».</p>
<pre><code class="language-python">price = 1_200_000        # زیرخط فقط برای خوانایی است
discount = price         # برچسب دوم روی همان شیء
price = price - 200_000  # شیء جدید ساخته شد؛ price به آن اشاره می‌کند

print(price, discount)   # 1000000 1200000
print(type(price))       # &lt;class 'int'&gt;
print(id(price) == id(discount))  # False</code></pre>
<p>برای اعداد و رشته‌ها این تفاوت به چشم نمی‌آید چون این اشیا <strong>تغییرناپذیر</strong> (immutable) هستند. اما در فصل ۴ می‌بینید که وقتی دو برچسب به یک لیست اشاره کنند، تغییر از طریق یکی در دیگری هم دیده می‌شود؛ منشأ یکی از رایج‌ترین باگ‌های تازه‌کارها.</p>
<h3>تایپ پویا</h3>
<p>پایتون نوع را به <em>شیء</em> نسبت می‌دهد، نه به <em>نام</em>. پس یک نام می‌تواند اول به عدد و بعد به متن اشاره کند. این آزادی است، نه دعوت: اگر متغیری را برای دو نوع مختلف استفاده کنید، خواننده‌ی کد (یعنی خود شما در سه ماه بعد) گیج می‌شود.</p>
<h3>قواعد و قراردادهای نام‌گذاری (PEP 8)</h3>
<p>PEP 8 راهنمای رسمی سبک کد پایتون است. قواعد اجباری زبان: نام با حرف یا <code>_</code> شروع شود، فقط حرف و رقم و <code>_</code> داشته باشد و کلمه‌ی کلیدی نباشد (<code>class</code>، <code>for</code>، <code>if</code> و…). قراردادها:</p>
<table><thead><tr><th>چه چیزی</th><th>سبک</th><th>مثال</th></tr></thead><tbody>
<tr><td>متغیر و تابع</td><td>snake_case</td><td><code>order_count</code>، <code>calc_area()</code></td></tr>
<tr><td>ثابت</td><td>UPPER_CASE</td><td><code>TAX_RATE = 0.10</code></td></tr>
<tr><td>کلاس</td><td>PascalCase</td><td><code>CarpetOrder</code></td></tr>
<tr><td>«خصوصی» (قرارداد)</td><td>با _ شروع</td><td><code>_cache</code></td></tr>
<tr><td>متغیر دورریختنی</td><td>فقط _</td><td><code>for _ in range(3):</code></td></tr>
</tbody></table>
<p>نام خوب، توضیح می‌دهد <em>چه</em> چیزی نگه داشته شده، نه <em>چه نوعی</em>: <code>width_cm</code> بهتر از <code>w</code> و بهتر از <code>int_value</code> است. واحد را در نام بیاورید (<code>_cm</code>، <code>_rial</code>)؛ باگ‌های تبدیل ریال و تومان را با همین کار ساده کم می‌کنید. تورفتگی استاندارد ۴ فاصله است و طول خط حداکثر ۷۹ تا ۱۰۰ کاراکتر.</p>
<h3>انتساب چندگانه</h3>
<pre><code class="language-python">width, length = 250, 350     # دو متغیر در یک خط
width, length = length, width   # جابه‌جایی بدون متغیر کمکی
a = b = 0                       # هر دو به همان شیء 0</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>نام متغیر فارسی در پایتون ۳ مجاز است (<code>قیمت = 1000</code> کار می‌کند)، اما به‌خاطر جابه‌جایی جهت متن و کیبورد، در کد واقعی استفاده نکنید.</li>
<li>نام‌هایی مثل <code>list</code>، <code>str</code>، <code>id</code>، <code>type</code> و <code>sum</code> کلمه‌ی کلیدی نیستند و پایتون جلوی استفاده را نمی‌گیرد؛ اما با <code>list = [1, 2]</code> تابع list را تا پایان برنامه از دست می‌دهید.</li>
<li>پایتون اعداد صحیح ‎-5 تا 256 را از قبل می‌سازد و بازاستفاده می‌کند؛ به همین دلیل <code>is</code> روی اعداد کوچک «کار می‌کند» و روی اعداد بزرگ نه. برای مقایسه‌ی مقدار همیشه <code>==</code> بنویسید.</li>
<li><code>match</code>، <code>case</code> و <code>type</code> «کلمه‌ی کلیدی نرم» هستند؛ می‌توانید متغیری به نام <code>match</code> داشته باشید و در عین حال از <code>match/case</code> استفاده کنید.</li>
<li><code>del x</code> شیء را پاک نمی‌کند، فقط برچسب را برمی‌دارد؛ شیء وقتی از حافظه آزاد می‌شود که هیچ برچسبی به آن اشاره نکند.</li>
</ul>""",
                },
                {
                    "title": "اعداد و پول: int، float، دام 0.1+0.2 و Decimal برای ریال و تومان",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>ماشین‌حسابی که همیشه راست نمی‌گوید</h2>
<p>پایتون دو نوع عددی اصلی دارد: <strong>int</strong> (عدد صحیح) و <strong>float</strong> (عدد اعشاری). int در پایتون اندازه‌ی نامحدود دارد؛ <code>2 ** 200</code> بدون سرریز محاسبه می‌شود. float اما همان استاندارد IEEE 754 است که در همه‌ی زبان‌ها وجود دارد و دقتی حدود ۱۵ تا ۱۷ رقم دارد.</p>
<h3>عملگرها</h3>
<table><thead><tr><th>عملگر</th><th>معنی</th><th>مثال</th><th>نتیجه</th></tr></thead><tbody>
<tr><td><code>/</code></td><td>تقسیم؛ همیشه float</td><td><code>7 / 2</code></td><td>3.5</td></tr>
<tr><td><code>//</code></td><td>تقسیم صحیح (رو به پایین)</td><td><code>7 // 2</code></td><td>3</td></tr>
<tr><td><code>%</code></td><td>باقی‌مانده</td><td><code>7 % 2</code></td><td>1</td></tr>
<tr><td><code>**</code></td><td>توان</td><td><code>2 ** 10</code></td><td>1024</td></tr>
<tr><td><code>divmod</code></td><td>خارج‌قسمت و باقی‌مانده با هم</td><td><code>divmod(125, 60)</code></td><td>(2, 5)</td></tr>
</tbody></table>
<p>دقت کنید <code>//</code> رو به پایین گرد می‌کند، نه رو به صفر: <code>-7 // 2</code> برابر ‎-4 است. <code>divmod</code> برای تبدیل دقیقه به ساعت و دقیقه یا سانتی‌متر به متر و سانتی‌متر بسیار کاربردی است.</p>
<h3>دام معروف 0.1 + 0.2</h3>
<pre><code class="language-python">&gt;&gt;&gt; 0.1 + 0.2
0.30000000000000004
&gt;&gt;&gt; 0.1 + 0.2 == 0.3
False
&gt;&gt;&gt; import math
&gt;&gt;&gt; math.isclose(0.1 + 0.2, 0.3)
True</code></pre>
<p>این باگ پایتون نیست. کامپیوتر اعداد را در مبنای ۲ ذخیره می‌کند و 0.1 در مبنای ۲ یک کسر متناوب است، همان‌طور که 1/3 در مبنای ۱۰ برابر 0.333… است. نتیجه: هیچ‌وقت دو float را با <code>==</code> مقایسه نکنید و هیچ‌وقت پول را با float حساب نکنید.</p>
<h3>پول: دو راه درست</h3>
<p><strong>راه اول، int به ریال:</strong> ریال واحد خرد ندارد، پس همه‌ی مبالغ را به‌صورت عدد صحیح ریالی نگه دارید و فقط هنگام نمایش به تومان تبدیل کنید. ساده، سریع و بدون خطای گرد کردن.</p>
<p><strong>راه دوم، Decimal:</strong> وقتی درصد، نرخ ارز یا اعشار دارید، از ماژول <code>decimal</code> استفاده کنید که محاسبه را در مبنای ۱۰ و دقیق انجام می‌دهد:</p>
<pre><code class="language-python">from decimal import Decimal, ROUND_HALF_UP

price_rial = Decimal("12500000")        # قیمت یک تخته فرش
vat = Decimal("0.10")                    # مالیات بر ارزش افزوده
total = price_rial * (1 + vat)
print(total)                             # 13750000.00

rate = Decimal("2.675")
print(rate.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))  # 2.68

toman = int(total) // 10
print(f"{toman:,} تومان")                # 1,375,000 تومان</code></pre>
<p>Decimal را <strong>همیشه از رشته</strong> بسازید. <code>Decimal(0.1)</code> همان خطای float را با خودش می‌آورد و عددی با ۵۵ رقم اعشار تحویل می‌دهد.</p>
<h3>گرد کردن بانکی</h3>
<p>تابع <code>round</code> در پایتون از «گرد کردن بانکی» استفاده می‌کند: عدد دقیقاً وسط را به نزدیک‌ترین عدد <em>زوج</em> گرد می‌کند. پس <code>round(2.5)</code> برابر 2 و <code>round(3.5)</code> برابر 4 است. برای فاکتور که انتظار «نیم به بالا» دارد، از <code>quantize</code> با <code>ROUND_HALF_UP</code> استفاده کنید.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>round(2.675, 2)</code> برابر 2.67 است نه 2.68؛ چون 2.675 در حافظه در واقع کمی کمتر از 2.675 ذخیره شده است. این یکی گرد کردن بانکی نیست، خطای float است.</li>
<li><code>float("nan") == float("nan")</code> برابر False است؛ NaN تنها مقداری است که با خودش برابر نیست. برای بررسی از <code>math.isnan</code> استفاده کنید.</li>
<li>زیرخط در اعداد (<code>12_500_000</code>) فقط برای چشم است؛ <code>int("12_500")</code> هم کار می‌کند، ولی <code>int("12,500")</code> خطا می‌دهد.</li>
<li><code>10 / 2</code> برابر <code>5.0</code> است نه <code>5</code>؛ اگر نتیجه را برای اندیس لیست یا <code>range</code> لازم دارید، از <code>//</code> استفاده کنید.</li>
<li>عدد صحیحی با بیش از ۴۳۰۰ رقم را پایتون به‌طور پیش‌فرض به رشته تبدیل نمی‌کند (محافظت در برابر حمله‌ی DoS)؛ اگر واقعاً لازم شد، <code>sys.set_int_max_str_digits</code> را تغییر دهید.</li>
</ul>""",
                },
                {
                    "title": "bool، truthiness، None و عملگرهای منطقی",
                    "kind": "text",
                    "minutes": 16,
                    "is_preview": False,
                    "body": r"""<h2>درست، نادرست و «هیچ»</h2>
<p>نوع <strong>bool</strong> فقط دو مقدار دارد: <code>True</code> و <code>False</code> (با حرف بزرگ). نتیجه‌ی هر مقایسه یک bool است: <code>5 &gt; 3</code> برابر True و <code>"فرش" == "گلیم"</code> برابر False. اما نکته‌ی مهم‌تر این است که در پایتون <strong>هر شیئی</strong> را می‌توان در شرط گذاشت؛ به این ویژگی truthiness می‌گویند.</p>
<h3>چه چیزهایی «نادرست» حساب می‌شوند؟</h3>
<table><thead><tr><th>نوع</th><th>مقدار falsy</th><th>هر چیز دیگر</th></tr></thead><tbody>
<tr><td>عدد</td><td><code>0</code>، <code>0.0</code>، <code>Decimal("0")</code></td><td>truthy</td></tr>
<tr><td>رشته</td><td><code>""</code> (رشته‌ی خالی)</td><td>حتی <code>"0"</code> و <code>"False"</code> truthy هستند</td></tr>
<tr><td>مجموعه‌ها</td><td><code>[]</code>، <code>()</code>، <code>{}</code>، <code>set()</code></td><td>truthy اگر حداقل یک عضو داشته باشند</td></tr>
<tr><td>ویژه</td><td><code>None</code>، <code>False</code></td><td>—</td></tr>
</tbody></table>
<p>بنابراین به‌جای <code>if len(orders) &gt; 0:</code> بنویسید <code>if orders:</code>. این سبک پایتونیک است و روی هر نوع مجموعه‌ای کار می‌کند.</p>
<h3>and، or، not: فقط True/False برنمی‌گردانند</h3>
<p><code>and</code> و <code>or</code> «میان‌بری» (short-circuit) هستند و <strong>یکی از خود عملوندها</strong> را برمی‌گردانند، نه لزوماً True یا False:</p>
<pre><code class="language-python">name = input("نام مشتری: ") or "مشتری ناشناس"
print(name)          # اگر Enter خالی بزنید: مشتری ناشناس

print(0 or 5)        # 5
print(3 and 7)       # 7
print([] and 10)     # []

orders = []
if orders and orders[0] &gt; 10:   # اگر لیست خالی باشد، بخش دوم اجرا نمی‌شود
    print("سفارش بزرگ")</code></pre>
<p>در مثال آخر، اگر لیست خالی باشد <code>orders[0]</code> خطای IndexError می‌داد؛ اما چون <code>and</code> با دیدن اولین مقدار falsy متوقف می‌شود، بخش دوم هرگز اجرا نمی‌شود. از این رفتار آگاهانه برای «نگهبان» استفاده کنید.</p>
<h3>None: «هنوز مقداری ندارد»</h3>
<p><code>None</code> تنها شیء از نوع <code>NoneType</code> است و معنی «نبودِ مقدار» را دارد: تخفیفی که هنوز تعیین نشده، مشتری‌ای که پیدا نشد، تابعی که چیزی برنمی‌گرداند. برای بررسی آن <strong>همیشه</strong> از <code>is</code> استفاده کنید:</p>
<pre><code class="language-python">discount = None

if discount is None:
    print("تخفیف تعیین نشده")

# خطرناک: اگر تخفیف 0 باشد هم وارد این شرط می‌شود
if not discount:
    print("تخفیف ندارد یا صفر است")</code></pre>
<p>تفاوت ظریف ولی مهم: <code>not discount</code> صفر را هم «خالی» می‌داند. اگر صفر یک مقدار معتبر است (تخفیف صفر درصد)، فقط <code>is None</code> درست است.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>bool</code> زیرکلاس <code>int</code> است: <code>True + True</code> برابر 2 است. پس <code>sum(x &gt; 10 for x in sizes)</code> تعداد اعضای بزرگ‌تر از ۱۰ را می‌شمارد.</li>
<li><code>bool("False")</code> برابر True است؛ هر رشته‌ی غیرخالی truthy است. مقادیر «بله/خیر» ورودی کاربر یا فایل را خودتان با مقایسه‌ی رشته تبدیل کنید.</li>
<li><code>if x == 1 or 2:</code> همیشه درست است، چون به‌صورت <code>(x == 1) or 2</code> خوانده می‌شود و 2 truthy است. درستش <code>if x in (1, 2):</code> است.</li>
<li><code>x or default</code> برای مقادیری که صفر یا رشته‌ی خالی‌شان معتبر است خطرناک است؛ آنجا بنویسید <code>default if x is None else x</code>.</li>
<li><code>not</code> اولویت پایین‌تری از مقایسه دارد: <code>not a == b</code> یعنی <code>not (a == b)</code>. برای وضوح بنویسید <code>a != b</code>.</li>
</ul>""",
                },
                {
                    "title": "رشته‌ها و یونیکد فارسی: len، نیم‌فاصله، ی و ک عربی، متدها و slicing",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>متن فارسی از نگاه پایتون</h2>
<p>در پایتون ۳ هر رشته (<code>str</code>) دنباله‌ای از <strong>کاراکترهای یونیکد</strong> است؛ بنابراین فارسی، عربی و ایموجی همان‌قدر «طبیعی» هستند که حروف لاتین. رشته را می‌توان با <code>'…'</code> یا <code>"…"</code> ساخت و برای چندخطی از سه کوتیشن استفاده کرد. رشته‌ها <strong>تغییرناپذیرند</strong>: هر متدی مثل <code>replace</code> یک رشته‌ی جدید برمی‌گرداند و رشته‌ی اصلی دست‌نخورده می‌ماند.</p>
<h3>len و کاراکترهای نامرئی</h3>
<pre><code class="language-python">print(len("سلام"))          # 4
print(len("می‌روم"))        # 6 — نیم‌فاصله هم یک کاراکتر است
print("‌" in "می‌روم")  # True: U+200C همان نیم‌فاصله (ZWNJ) است
print(ord("ی"), ord("ي"))   # 1740 1610
print("علی" == "علي")       # False!</code></pre>
<p>دو نکته‌ی حیاتی برای هر برنامه‌ی فارسی: اول، <strong>نیم‌فاصله</strong> کاراکتر واقعی است و در طول رشته، جست‌وجو و مقایسه حساب می‌شود. دوم، «ی» و «ک» فارسی (U+06CC و U+06A9) با «ي» و «ك» عربی (U+064A و U+0643) کدهای متفاوتی دارند. متنی که از کیبورد عربی، سیستم‌های قدیمی یا بعضی سایت‌ها می‌آید، ظاهراً یکسان است ولی در جست‌وجو پیدا نمی‌شود. راه‌حل، <strong>یکسان‌سازی</strong> پیش از ذخیره یا مقایسه است:</p>
<pre><code class="language-python">FA_FIX = str.maketrans({"ي": "ی", "ك": "ک", "ى": "ی"})

def normalize_fa(text: str) -&gt; str:
    return " ".join(text.translate(FA_FIX).split())   # اصلاح حروف و فاصله‌های اضافی

print(normalize_fa("  فرش   كاشان  علي ") == "فرش کاشان علی")   # True</code></pre>
<h3>اندیس و برش (slicing)</h3>
<p>هر کاراکتر یک شماره (اندیس) دارد که از صفر شروع می‌شود؛ اندیس منفی از انتها می‌شمارد. برش با <code>[start:stop:step]</code> زیررشته می‌سازد و <code>stop</code> جزو نتیجه نیست:</p>
<pre><code class="language-python">code = "KSH-1403-0587"
print(code[0])       # K
print(code[-4:])     # 0587   — چهار کاراکتر آخر
print(code[4:8])     # 1403
print(code[::-1])    # معکوس رشته
print(code[20:])     # '' — برش هیچ‌وقت IndexError نمی‌دهد</code></pre>
<h3>متدهای پرکاربرد</h3>
<table><thead><tr><th>متد</th><th>کار</th><th>مثال</th></tr></thead><tbody>
<tr><td><code>strip()</code></td><td>حذف فاصله‌ی ابتدا و انتها</td><td><code>" کاشان ".strip()</code></td></tr>
<tr><td><code>split(sep)</code></td><td>شکستن به لیست</td><td><code>"۳×۴,کاشان".split(",")</code></td></tr>
<tr><td><code>sep.join(list)</code></td><td>چسباندن لیست رشته‌ها</td><td><code>"، ".join(cities)</code></td></tr>
<tr><td><code>replace(a, b)</code></td><td>جایگزینی</td><td><code>s.replace("ك", "ک")</code></td></tr>
<tr><td><code>startswith</code> / <code>endswith</code></td><td>بررسی ابتدا/انتها؛ تاپل هم می‌گیرد</td><td><code>f.endswith((".csv", ".xlsx"))</code></td></tr>
<tr><td><code>find</code> / <code>index</code></td><td>جای زیررشته؛ find در نبود ‎-1 می‌دهد، index خطا</td><td><code>s.find("فرش")</code></td></tr>
<tr><td><code>zfill(n)</code></td><td>صفر در ابتدا</td><td><code>"87".zfill(4)</code> ← 0087</td></tr>
</tbody></table>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>strip()</code> نیم‌فاصله را حذف نمی‌کند، چون ZWNJ از نظر یونیکد «فاصله» نیست؛ برای حذفش بنویسید <code>s.strip(" ‌")</code>.</li>
<li><code>split()</code> بدون آرگومان با <code>split(" ")</code> فرق دارد: اولی هر تعداد فاصله، Tab و خط جدید را یکی حساب می‌کند و رشته‌ی خالی تولید نمی‌کند.</li>
<li><code>unicodedata.name("ی")</code> نام رسمی کاراکتر را می‌دهد (ARABIC LETTER FARSI YEH)؛ بهترین ابزار برای کشف کاراکترهای مشکوک در داده.</li>
<li>برعکس کردن رشته‌ی فارسی با <code>[::-1]</code> حروف را معکوس می‌کند اما چون نمایش فارسی راست‌به‌چپ است، نتیجه در ترمینال ممکن است غیرمنتظره به نظر برسد؛ منطق درست است، نمایش گول‌زننده است.</li>
<li>رشته‌سازی با <code>+=</code> در حلقه‌ی بزرگ کند است؛ تکه‌ها را در لیست جمع کنید و در پایان یک‌بار <code>"".join(parts)</code> بزنید.</li>
</ul>""",
                },
                {
                    "title": "f-string، input، تبدیل نوع و ارقام فارسی با str.translate",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>گرفتن ورودی و نمایش زیبای خروجی</h2>
<p>تابع <code>input</code> متنی را از کاربر می‌گیرد و <strong>همیشه یک رشته</strong> برمی‌گرداند، حتی اگر کاربر عدد تایپ کند. پس برای محاسبه باید نوع را تبدیل کنید: <code>int()</code>، <code>float()</code> یا <code>Decimal()</code>. اگر تبدیل ممکن نباشد، خطای <code>ValueError</code> رخ می‌دهد (مدیریت آن را در فصل ۶ کامل یاد می‌گیریم).</p>
<pre><code class="language-python">width = int(input("عرض فرش (سانتی‌متر): "))
length = int(input("طول فرش (سانتی‌متر): "))
area = width * length / 10_000
print(f"مساحت: {area:.2f} متر مربع")</code></pre>
<h3>ارقام فارسی در ورودی</h3>
<p>کاربر ایرانی اغلب با کیبورد فارسی «۲۵۰» تایپ می‌کند. خبر خوب: <code>int("۲۵۰")</code> در پایتون کار می‌کند، چون int هر رقم یونیکد را می‌شناسد. خبر بد: <code>float("۱۲٫۵")</code> با ممیز فارسی خطا می‌دهد، رشته‌ای مثل «۱۴۰۳/۰۵/۲۰» باید برای ذخیره یا مقایسه لاتین شود، و ارقام عربی (٤ ٥ ٦) هم از بعضی کیبوردها می‌آیند. راه‌حل تمیز، یک جدول تبدیل با <code>str.maketrans</code> و <code>str.translate</code> است:</p>
<pre><code class="language-python">FA_DIGITS = "۰۱۲۳۴۵۶۷۸۹"
AR_DIGITS = "٠١٢٣٤٥٦٧٨٩"
TO_LATIN = str.maketrans(FA_DIGITS + AR_DIGITS + "٫٬", "0123456789" * 2 + ".,")
TO_PERSIAN = str.maketrans("0123456789", FA_DIGITS)

def to_latin(text: str) -&gt; str:
    return text.translate(TO_LATIN)

def to_persian(text: str) -&gt; str:
    return text.translate(TO_PERSIAN)

print(float(to_latin("۱۲٫۵")))          # 12.5
print(to_latin("۱۴۰۳/۰۵/٢٠"))           # 1403/05/20
print(to_persian(f"{12500000:,}"))       # ۱۲,۵۰۰,۰۰۰</code></pre>
<p><code>translate</code> در یک عبور کل رشته را تبدیل می‌کند و از ده بار <code>replace</code> بسیار سریع‌تر و خواناتر است.</p>
<h3>f-string: زبان کوچک قالب‌بندی</h3>
<p>f-string (رشته‌ای که با <code>f</code> شروع می‌شود) هر عبارت داخل <code>{}</code> را ارزیابی می‌کند. بعد از دونقطه می‌توانید قالب را مشخص کنید:</p>
<table><thead><tr><th>قالب</th><th>نتیجه</th><th>کاربرد</th></tr></thead><tbody>
<tr><td><code>f"{12500000:,}"</code></td><td>12,500,000</td><td>جداکننده‌ی هزارگان</td></tr>
<tr><td><code>f"{3.14159:.2f}"</code></td><td>3.14</td><td>دو رقم اعشار</td></tr>
<tr><td><code>f"{0.075:.1%}"</code></td><td>7.5%</td><td>درصد</td></tr>
<tr><td><code>f"{87:05}"</code></td><td>00087</td><td>شماره‌ی سفارش با صفر</td></tr>
<tr><td><code>f"{'کاشان':&gt;10}"</code></td><td>تراز راست در ۱۰ خانه</td><td>جدول متنی</td></tr>
<tr><td><code>f"{total=}"</code></td><td>total=13750000</td><td>دیباگ سریع</td></tr>
</tbody></table>
<p>برای جداکننده‌ی فارسی «٬» (U+066C) کافی است خروجی را جایگزین کنید: <code>f"{price:,}".replace(",", "٬")</code>.</p>
<h3>تبدیل نوع در یک نگاه</h3>
<pre><code class="language-python">int("  42 ")        # 42 — فاصله‌های اطراف مشکلی ندارند
int(3.99)           # 3 — قطع می‌کند، گرد نمی‌کند
int(float("12.5"))  # 12
str(1403)           # '1403'
float("1e3")        # 1000.0</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>از Python 3.12 می‌توانید داخل f-string همان نوع کوتیشن بیرونی را به کار ببرید: <code>f"{order["city"]}"</code> دیگر خطا نیست.</li>
<li><code>"۲۵۰".isdigit()</code> برابر True است؛ پس isdigit فقط ارقام لاتین را تأیید نمی‌کند. اگر فقط لاتین می‌خواهید، <code>s.isascii() and s.isdigit()</code> بنویسید.</li>
<li><code>int("12.0")</code> خطا می‌دهد، در حالی که <code>int(12.0)</code> کار می‌کند؛ رشته‌ی اعشاری را اول با float تبدیل کنید.</li>
<li><code>f"{x!r}"</code> نسخه‌ی repr را نشان می‌دهد و فاصله‌ها و کاراکترهای نامرئی (مثل <code>‌</code>) را آشکار می‌کند؛ عالی برای پیدا کردن «چرا این دو رشته برابر نیستند».</li>
<li>برای جدا کردن ورودی چندتایی در یک خط: <code>w, l = map(int, input("عرض و طول: ").split())</code>.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۳ ─────────────────────────────
        {
            "title": "فصل ۳: کنترل جریان — تصمیم‌گیری و تکرار",
            "lessons": [
                {
                    "title": "if/elif/else، عملگرهای مقایسه، مقایسه‌ی زنجیره‌ای و عبارت شرطی",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>برنامه‌ای که تصمیم می‌گیرد</h2>
<p>تا این‌جا برنامه‌ها خط‌به‌خط از بالا به پایین اجرا می‌شدند. دستور <code>if</code> اجازه می‌دهد بخشی از کد فقط در صورت درست بودن یک شرط اجرا شود. در پایتون، بلوک هر شرط با <strong>دونقطه</strong> شروع می‌شود و با <strong>تورفتگی</strong> (۴ فاصله) مشخص می‌شود؛ خبری از آکولاد نیست و تورفتگی جزو نحو زبان است، نه سلیقه.</p>
<pre><code class="language-python">area = 12            # متر مربع
city = "تهران"

if area &gt;= 12:
    shipping = 0
elif area &gt;= 6:
    shipping = 350_000
else:
    shipping = 600_000

if city in ("کاشان", "آران و بیدگل"):
    shipping = 0         # ارسال درون‌شهری رایگان

print(f"هزینه‌ی ارسال: {shipping:,} ریال")</code></pre>
<p>پایتون شرط‌ها را به ترتیب بررسی می‌کند و <strong>اولین</strong> شاخه‌ی درست را اجرا می‌کند؛ بقیه نادیده گرفته می‌شوند. پس ترتیب elif ها مهم است: شرط خاص‌تر را بالاتر بگذارید. اگر <code>area &gt;= 6</code> را اول می‌نوشتید، فرش ۱۲ متری هم هزینه‌ی ۳۵۰ هزار ریالی می‌گرفت.</p>
<h3>عملگرهای مقایسه</h3>
<table><thead><tr><th>عملگر</th><th>معنی</th><th>نکته</th></tr></thead><tbody>
<tr><td><code>==</code> و <code>!=</code></td><td>برابر / نابرابر</td><td>مقایسه‌ی مقدار</td></tr>
<tr><td><code>&lt;</code> <code>&lt;=</code> <code>&gt;</code> <code>&gt;=</code></td><td>کوچک‌تر/بزرگ‌تر</td><td>روی رشته‌ها الفبایی (بر اساس کد یونیکد)</td></tr>
<tr><td><code>in</code> و <code>not in</code></td><td>عضویت</td><td>روی رشته، لیست، دیکشنری (کلیدها)، set</td></tr>
<tr><td><code>is</code> و <code>is not</code></td><td>هویت (همان شیء)</td><td>فقط برای None، True، False</td></tr>
</tbody></table>
<h3>مقایسه‌ی زنجیره‌ای</h3>
<p>پایتون، برخلاف بیشتر زبان‌ها، مقایسه‌ها را مثل ریاضی زنجیر می‌کند: <code>100 &lt;= width &lt;= 400</code> یعنی «عرض بین ۱۰۰ و ۴۰۰»، و معادل <code>100 &lt;= width and width &lt;= 400</code> است با این تفاوت که <code>width</code> فقط یک‌بار ارزیابی می‌شود.</p>
<h3>عبارت شرطی (ternary)</h3>
<p>وقتی فقط می‌خواهید بین دو مقدار یکی را انتخاب کنید، یک خط کافی است:</p>
<pre><code class="language-python">label = "عمده" if quantity &gt;= 10 else "خرده"
unit = "تخته" if quantity == 1 else "تخته‌ها"</code></pre>
<p>عبارت شرطی را تودرتو نکنید؛ دو سطح ternary در یک خط خوانایی را نابود می‌کند و آن‌جا if/elif معمولی بهتر است.</p>
<h3>کاهش تودرتویی</h3>
<p>کد با پنج سطح if تودرتو خواندنی نیست. دو ترفند: شرط‌های مرتبط را با <code>and</code> ترکیب کنید و حالت‌های خطا را زودتر رد کنید (در توابع با <code>return</code> زودهنگام، که در فصل ۵ می‌بینید). قاعده‌ی سرانگشتی: اگر به سطح سوم تورفتگی رسیدید، مکث کنید و ساختار را بازبینی کنید.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>"10" &lt; "9"</code> برابر True است، چون رشته‌ها کاراکتربه‌کاراکتر مقایسه می‌شوند و «۱» قبل از «۹» است. عددهایی را که از فایل یا input آمده‌اند، اول تبدیل کنید.</li>
<li>مقایسه‌ی ترتیبی دو نوع ناهمخوان مثل <code>5 &lt; "5"</code> در پایتون ۳ خطای TypeError می‌دهد، اما <code>5 == "5"</code> بی‌صدا False برمی‌گرداند؛ دومی خطرناک‌تر است.</li>
<li>زنجیره‌ی <code>a &lt; b &gt; c</code> هم مجاز است و یعنی «b از هر دو بزرگ‌تر است»؛ مجاز بودن دلیل خوانا بودن نیست.</li>
<li>بلوک خالی مجاز نیست؛ اگر جای کدی را فعلاً خالی می‌گذارید، از <code>pass</code> یا <code>...</code> (Ellipsis) استفاده کنید.</li>
<li>مخلوط کردن Tab و فاصله در تورفتگی خطای TabError می‌دهد؛ در VS Code پایین پنجره «Spaces: 4» را چک کنید و Convert Indentation to Spaces را بزنید.</li>
</ul>""",
                },
                {
                    "title": "match/case: تطبیق الگوی ساختاری",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>فراتر از switch</h2>
<p>از Python 3.10 دستور <code>match/case</code> به زبان اضافه شد. در نگاه اول شبیه switch در زبان‌های دیگر است، اما در واقع یک ابزار <strong>تطبیق الگوی ساختاری</strong> است: نه فقط مقدار، که <em>شکل</em> داده را هم بررسی می‌کند و اجزای آن را در متغیرها می‌ریزد.</p>
<h3>ساده‌ترین شکل: تطبیق مقدار</h3>
<pre><code class="language-python">status = "shipped"

match status:
    case "new":
        text = "ثبت شده"
    case "weaving" | "finishing":        # چند مقدار با |
        text = "در حال تولید"
    case "shipped":
        text = "ارسال شد"
    case _:                              # حالت پیش‌فرض
        text = "نامشخص"</code></pre>
<p>برخلاف C، هیچ «سقوط» (fall-through) به case بعدی وجود ندارد و نیازی به break نیست. <code>case _</code> مثل else عمل می‌کند و همیشه آخر می‌آید.</p>
<h3>قدرت واقعی: تطبیق ساختار</h3>
<p>فرض کنید برنامه‌ای خط فرمان دارید و کاربر دستورهایی مثل <code>add رضایی 3</code> تایپ می‌کند. با تطبیق روی لیست کلمات، هم دستور و هم آرگومان‌ها را در یک قدم جدا می‌کنید:</p>
<pre><code class="language-python">def handle(command: str) -&gt; str:
    match command.split():
        case ["add", name, qty] if qty.isdigit():
            return f"ثبت {qty} تخته برای {name}"
        case ["add", *_]:
            return "فرمت: add نام تعداد"
        case ["list"] | ["ls"]:
            return "فهرست سفارش‌ها"
        case ["quit" | "exit"]:
            return "خداحافظ"
        case []:
            return "چیزی ننوشتید"
        case _:
            return f"دستور ناشناخته: {command}"

print(handle("add رضایی 3"))   # ثبت 3 تخته برای رضایی
print(handle("add x"))         # فرمت: add نام تعداد</code></pre>
<p>اجزای این مثال: <code>name</code> و <code>qty</code> <strong>متغیر گیرنده</strong> (capture) هستند و هر مقداری را می‌گیرند؛ <code>if qty.isdigit()</code> یک <strong>guard</strong> است که شرط اضافه می‌گذارد؛ <code>*_</code> «هر تعداد عضو باقی‌مانده» را می‌پذیرد؛ و الگوی لیست فقط وقتی تطبیق می‌خورد که <em>تعداد</em> اعضا هم جور باشد.</p>
<h3>تطبیق دیکشنری (مثلاً داده‌ی JSON)</h3>
<pre><code class="language-python">def describe(event: dict) -&gt; str:
    match event:
        case {"type": "order", "qty": int(q)} if q &gt; 10:
            return f"سفارش عمده: {q} تخته"
        case {"type": "order", "qty": q}:
            return f"سفارش: {q}"
        case {"type": "cancel", "id": order_id}:
            return f"لغو سفارش {order_id}"
        case _:
            return "رویداد ناشناخته"</code></pre>
<p>الگوی دیکشنری فقط کلیدهای ذکرشده را بررسی می‌کند و کلیدهای اضافه را نادیده می‌گیرد. <code>int(q)</code> یعنی «مقدار باید از نوع int باشد و در q قرار گیرد».</p>
<h3>کی از match استفاده نکنیم؟</h3>
<p>اگر فقط دو سه مقدار ساده را مقایسه می‌کنید، if/elif کوتاه‌تر و آشناتر است. match وقتی می‌درخشد که داده ساختار دارد: دستورهای چندکلمه‌ای، پیام‌های JSON، تاپل مختصات یا درخت‌ها.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>دام بزرگ: <code>case QUIT:</code> که QUIT یک متغیر ساده باشد، مقایسه نمی‌کند بلکه <em>هر چیزی</em> را می‌گیرد و در QUIT می‌ریزد! ثابت‌ها باید «نقطه‌دار» باشند، مثل <code>case Status.QUIT:</code> یا <code>case config.QUIT:</code>.</li>
<li>الگوی رشته‌ای <code>"abc"</code> با لیست <code>["a","b","c"]</code> تطبیق نمی‌خورد؛ match عمداً رشته را «دنباله» حساب نمی‌کند تا غافلگیری پیش نیاید.</li>
<li>با <code>as</code> می‌توانید کل زیرالگو را هم نگه دارید: <code>case ["add" | "new" as cmd, name]:</code>.</li>
<li>برای گرفتن کلیدهای اضافه‌ی دیکشنری از <code>**rest</code> استفاده کنید: <code>case {"type": "order", **rest}:</code>.</li>
<li>متغیرهای capture بعد از match هم باقی می‌مانند؛ حتی در caseی که در نهایت به‌خاطر guard رد شده، ممکن است مقدار گرفته باشند.</li>
</ul>""",
                },
                {
                    "title": "حلقه‌ها: while، for، range و break/continue/else",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>تکرار، قلب اتوماسیون</h2>
<p>پایتون دو حلقه دارد: <code>while</code> که «تا وقتی شرط درست است» تکرار می‌کند، و <code>for</code> که «روی اعضای یک مجموعه» می‌چرخد. قاعده‌ی انتخاب ساده است: اگر تعداد یا مجموعه‌ی اعضا را می‌دانید، <strong>for</strong>؛ اگر پایان به رویدادی بستگی دارد (ورودی درست کاربر، رسیدن به هدف)، <strong>while</strong>.</p>
<h3>while و اعتبارسنجی ورودی</h3>
<pre><code class="language-python">while True:
    text = input("تعداد تخته (۱ تا ۱۰۰): ")
    if text.isdigit() and 1 &lt;= int(text) &lt;= 100:
        qty = int(text)
        break                     # خروج از حلقه
    print("عدد معتبر وارد کنید.")

print(f"{qty} تخته ثبت شد")</code></pre>
<p>الگوی <code>while True</code> + <code>break</code> رایج‌ترین راه برای «تا ورودی درست نیامده، دوباره بپرس» است. اگر حلقه‌ای بی‌پایان شد، در ترمینال <strong>Ctrl+C</strong> آن را متوقف می‌کند.</p>
<h3>عملگر walrus</h3>
<p>از Python 3.8 عملگر <code>:=</code> اجازه می‌دهد وسط یک عبارت، مقداری را به متغیر نسبت دهید. برای حلقه‌هایی که ورودی می‌خوانند بسیار تمیز است:</p>
<pre><code class="language-python">while (cmd := input("&gt; ").strip()) != "q":
    print(f"دستور: {cmd}")</code></pre>
<h3>for و range</h3>
<p><code>for</code> روی هر چیز «پیمایش‌پذیر» (iterable) کار می‌کند: لیست، رشته، دیکشنری، فایل و… . برای تکرار عددی از <code>range</code> استفاده می‌شود که عدد پایانی را شامل <strong>نمی‌شود</strong>:</p>
<table><thead><tr><th>عبارت</th><th>اعداد تولیدشده</th></tr></thead><tbody>
<tr><td><code>range(5)</code></td><td>0, 1, 2, 3, 4</td></tr>
<tr><td><code>range(1, 6)</code></td><td>1, 2, 3, 4, 5</td></tr>
<tr><td><code>range(0, 20, 5)</code></td><td>0, 5, 10, 15</td></tr>
<tr><td><code>range(10, 0, -3)</code></td><td>10, 7, 4, 1</td></tr>
</tbody></table>
<pre><code class="language-python">prices = [8_500_000, 12_000_000, 4_200_000]
total = 0
for p in prices:
    if p &lt; 5_000_000:
        continue              # این یکی را رد کن و برو سراغ بعدی
    total += p
print(f"{total:,}")           # 20,500,000</code></pre>
<h3>else روی حلقه: کمترشناخته‌شده اما مفید</h3>
<p>حلقه‌های for و while می‌توانند بخش <code>else</code> داشته باشند که <strong>فقط اگر حلقه بدون break تمام شود</strong> اجرا می‌شود. کاربرد کلاسیک: جست‌وجو.</p>
<pre><code class="language-python">codes = ["KSH-101", "TBZ-220", "MSH-310"]
target = "ISF-500"

for code in codes:
    if code == target:
        print("پیدا شد")
        break
else:
    print("سفارشی با این کد وجود ندارد")</code></pre>
<p>بدون else باید یک متغیر پرچم (<code>found = False</code>) تعریف می‌کردید. نام else این‌جا کمی گمراه‌کننده است؛ آن را در ذهن «nobreak» بخوانید.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>متغیر حلقه‌ی for بعد از حلقه باقی می‌ماند و آخرین مقدار را دارد؛ اما اگر حلقه اصلاً اجرا نشود (لیست خالی)، تعریف نشده است و NameError می‌گیرید.</li>
<li>حذف عضو از لیستی که روی آن for می‌زنید، عضوها را جا می‌اندازد. روی یک کپی بچرخید (<code>for x in items[:]:</code>) یا لیست جدید بسازید.</li>
<li><code>range</code> لیست نمی‌سازد و حافظه‌ی ثابتی دارد؛ <code>range(10**12)</code> فوری ساخته می‌شود و <code>10**11 in range(10**12)</code> هم بدون پیمایش جواب می‌دهد.</li>
<li><code>break</code> فقط از درونی‌ترین حلقه خارج می‌شود؛ برای خروج از دو حلقه‌ی تودرتو، آن‌ها را در یک تابع بگذارید و <code>return</code> کنید.</li>
<li>برای شمارش معکوس، <code>reversed(range(5))</code> خواناتر از <code>range(4, -1, -1)</code> است و خطای یکی‌کم‌یکی‌زیاد ندارد.</li>
</ul>""",
                },
                {
                    "title": "enumerate، zip، any/all و الگوریتم‌های کوچک",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>حلقه‌ی پایتونیک</h2>
<p>کسانی که از زبان‌های دیگر می‌آیند معمولاً می‌نویسند <code>for i in range(len(names)):</code> و بعد <code>names[i]</code>. در پایتون تقریباً هیچ‌وقت به این نیاز ندارید؛ ابزارهای بهتری هست.</p>
<h3>enumerate: شماره و عضو با هم</h3>
<pre><code class="language-python">customers = ["رضا احمدی", "مریم کاشانی", "سارا نراقی"]

for i, name in enumerate(customers, start=1):
    print(f"{i}. {name}")</code></pre>
<p><code>enumerate</code> در هر دور یک جفت (شماره، عضو) تحویل می‌دهد و با <code>start=1</code> شماره‌گذاری برای انسان‌ها طبیعی‌تر می‌شود.</p>
<h3>zip: پیمایش موازی</h3>
<p>وقتی چند لیست هم‌طول دارید که عضوهای متناظرشان به هم مربوط‌اند، <code>zip</code> آن‌ها را جفت می‌کند:</p>
<pre><code class="language-python">names = ["رضا", "مریم", "سارا"]
sizes = [6, 12, 9]          # متر مربع
prices = [7_800_000, 9_500_000, 8_200_000]   # ریال برای هر متر

for name, size, price in zip(names, sizes, prices, strict=True):
    print(f"{name}: {size * price:,} ریال")</code></pre>
<p>zip به‌طور پیش‌فرض با رسیدن به انتهای <em>کوتاه‌ترین</em> لیست بی‌صدا متوقف می‌شود؛ اگر یکی از لیست‌ها به‌اشتباه کوتاه‌تر باشد، داده گم می‌شود و هیچ خطایی نمی‌بینید. آرگومان <code>strict=True</code> (از 3.10) در این حالت ValueError می‌دهد؛ عادت کنید آن را بنویسید.</p>
<h3>any و all</h3>
<pre><code class="language-python">if any(s &gt; 10 for s in sizes):
    print("دست‌کم یک فرش بزرگ داریم")
if all(p &gt; 0 for p in prices):
    print("همه‌ی قیمت‌ها معتبرند")</code></pre>
<h3>الگوریتم‌های کوچک، دست‌ساز</h3>
<p>پایتون برای بیشتر کارها تابع آماده دارد (<code>sum</code>، <code>max</code>، <code>min</code>، <code>sorted</code>)، اما یک‌بار دستی نوشتنشان منطق حلقه را در ذهن می‌نشاند:</p>
<pre><code class="language-python">def biggest(values):
    best = values[0]
    for v in values[1:]:
        if v &gt; best:
            best = v
    return best

def knots_per_sqm(raj: int) -&gt; int:
    # «رج» تعداد گره در ۷ سانتی‌متر است؛ تراکم در یک متر مربع
    per_meter = raj * 100 / 7
    return round(per_meter ** 2)

print(biggest([12, 6, 30, 9]))        # 30
print(f"{knots_per_sqm(50):,}")        # 510,204 گره در متر مربع</code></pre>
<p>و با ابزار آماده: <code>max(sizes)</code>، <code>sum(prices) / len(prices)</code> برای میانگین، و <code>max(names, key=len)</code> برای طولانی‌ترین نام. پارامتر <code>key</code> را در فصل بعد عمیق‌تر می‌بینیم.</p>
<h3>تمرین پیشنهادی</h3>
<ol>
<li>برنامه‌ای بنویسید که تا کاربر «پایان» نزده، قیمت بگیرد و در پایان تعداد، جمع، میانگین، بیشینه و کمینه را چاپ کند.</li>
<li>فهرستی از کدهای سفارش بگیرید و کدهای تکراری را با یک حلقه و یک لیست کمکی پیدا کنید.</li>
<li>جدول ضرب ۱ تا ۹ را با دو حلقه‌ی تودرتو و f-string تراز شده چاپ کنید.</li>
</ol>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>zip(*rows)</code> جدول را ترانهاده می‌کند: سطرها ستون می‌شوند. <code>list(zip(*[[1, 2, 3], [4, 5, 6]]))</code> می‌دهد <code>[(1, 4), (2, 5), (3, 6)]</code>.</li>
<li><code>any</code> و <code>all</code> میان‌بری هستند: any با اولین True و all با اولین False متوقف می‌شود. <code>all([])</code> برابر True است (هیچ مثال نقضی نیست!).</li>
<li><code>max</code> و <code>min</code> روی لیست خالی خطا می‌دهند؛ پارامتر <code>default</code> نجاتتان می‌دهد: <code>max(prices, default=0)</code>.</li>
<li>zip و enumerate خودشان «تکرارکننده» (iterator) هستند و یک‌بار مصرف‌اند؛ اگر نتیجه را دو بار لازم دارید، با <code>list()</code> ذخیره کنید.</li>
<li>برای جفت‌های پشت‌سرهم (مثلاً اختلاف قیمت روزها) از <code>itertools.pairwise(prices)</code> استفاده کنید، نه اندیس‌بازی.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۴ ─────────────────────────────
        {
            "title": "فصل ۴: ساختارهای داده — list، tuple، dict، set و collections",
            "lessons": [
                {
                    "title": "list: متدها، دام a = b و کپی سطحی در برابر عمیق",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>پرکاربردترین ساختار داده</h2>
<p><strong>list</strong> دنباله‌ای مرتب و <strong>تغییرپذیر</strong> (mutable) از اشیاست که با کروشه ساخته می‌شود: <code>sizes = [6, 12, 9]</code>. اعضا می‌توانند از هر نوعی باشند، اما در عمل بهتر است یک لیست از اشیای هم‌جنس باشد (همه قیمت، همه نام). اندیس‌گذاری و برش دقیقاً مثل رشته است، با این تفاوت که می‌توانید عضوها را تغییر دهید: <code>sizes[0] = 8</code>.</p>
<h3>متدهای اصلی</h3>
<table><thead><tr><th>متد</th><th>کار</th><th>بازگشتی</th></tr></thead><tbody>
<tr><td><code>append(x)</code></td><td>افزودن یک عضو به انتها</td><td>None</td></tr>
<tr><td><code>extend(iterable)</code></td><td>افزودن همه‌ی اعضای یک مجموعه</td><td>None</td></tr>
<tr><td><code>insert(i, x)</code></td><td>درج در جایگاه i</td><td>None</td></tr>
<tr><td><code>pop(i=-1)</code></td><td>برداشتن و برگرداندن عضو</td><td>عضو حذف‌شده</td></tr>
<tr><td><code>remove(x)</code></td><td>حذف اولین x (نبودش ValueError)</td><td>None</td></tr>
<tr><td><code>sort()</code> / <code>reverse()</code></td><td>مرتب/معکوس کردن <em>درجا</em></td><td>None</td></tr>
<tr><td><code>index(x)</code> / <code>count(x)</code></td><td>جایگاه / تعداد تکرار</td><td>عدد</td></tr>
</tbody></table>
<p>به ستون آخر دقت کنید: متدهایی که لیست را تغییر می‌دهند <strong>None برمی‌گردانند</strong>. خطای کلاسیک <code>sizes = sizes.sort()</code> لیست شما را به None تبدیل می‌کند. اگر نسخه‌ی مرتب‌شده‌ی جدید می‌خواهید، از <code>sorted(sizes)</code> استفاده کنید.</p>
<h3>دام a = b</h3>
<p>یادتان هست متغیر فقط برچسب است؟ این‌جا اهمیتش آشکار می‌شود:</p>
<pre><code class="language-python">today = ["KSH-101", "TBZ-220"]
backup = today              # کپی نیست! دو برچسب روی یک لیست
today.append("MSH-310")
print(backup)               # ['KSH-101', 'TBZ-220', 'MSH-310']
print(backup is today)      # True</code></pre>
<p>برای کپی واقعی یکی از این‌ها را بنویسید: <code>today.copy()</code>، <code>list(today)</code> یا <code>today[:]</code>.</p>
<h3>کپی سطحی در برابر عمیق</h3>
<p>همه‌ی روش‌های بالا <strong>کپی سطحی</strong> (shallow) می‌سازند: خود لیست جدید است، اما اگر اعضا خودشان لیست یا دیکشنری باشند، همان اشیای قبلی به اشتراک گذاشته می‌شوند.</p>
<pre><code class="language-python">import copy

orders = [["KSH-101", 6], ["TBZ-220", 12]]
shallow = orders.copy()
shallow[0][1] = 99          # زیرلیست مشترک است
print(orders[0])            # ['KSH-101', 99]  — اصل هم عوض شد!

deep = copy.deepcopy(orders)
deep[1][1] = 0
print(orders[1])            # ['TBZ-220', 12]  — دست‌نخورده</code></pre>
<h3>دام ضرب لیست تودرتو</h3>
<pre><code class="language-python">grid = [[0] * 3] * 3        # سه برچسب روی یک زیرلیست!
grid[0][0] = 1
print(grid)                 # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

grid = [[0] * 3 for _ in range(3)]   # درست: سه زیرلیست مستقل</code></pre>
<p>ضرب لیست اعداد مشکلی ندارد (<code>[0] * 5</code>)، چون اعداد تغییرناپذیرند. مشکل فقط وقتی است که عضو تکرارشونده خودش تغییرپذیر باشد.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>items.append([1, 2])</code> یک عضو (یک لیست) اضافه می‌کند، اما <code>items += "ab"</code> دو عضو <code>'a'</code> و <code>'b'</code>؛ چون <code>+=</code> روی لیست همان extend است و رشته را حرف‌به‌حرف باز می‌کند.</li>
<li><code>pop(0)</code> و <code>insert(0, x)</code> روی لیست بزرگ کندند (همه‌ی اعضا جابه‌جا می‌شوند)؛ برای صف از <code>collections.deque</code> استفاده کنید.</li>
<li><code>del items[1:3]</code> یک بازه را حذف می‌کند و <code>items[1:3] = ["x"]</code> بازه را با تعداد متفاوتی عضو جایگزین می‌کند.</li>
<li><code>x in big_list</code> همه‌ی اعضا را یکی‌یکی بررسی می‌کند؛ اگر زیاد عضویت می‌پرسید، یک set بسازید که تقریباً فوری جواب می‌دهد.</li>
<li><code>list.sort()</code> «پایدار» است: عضوهای با کلید برابر ترتیب قبلی‌شان را حفظ می‌کنند؛ پس می‌توانید در دو مرحله، اول بر اساس معیار فرعی و بعد اصلی مرتب کنید.</li>
</ul>""",
                },
                {
                    "title": "tuple، unpacking و set",
                    "kind": "text",
                    "minutes": 18,
                    "is_preview": False,
                    "body": r"""<h2>داده‌ی ثابت و مجموعه‌ی بی‌تکرار</h2>
<p><strong>tuple</strong> مثل list است اما <strong>تغییرناپذیر</strong>. با پرانتز یا فقط با ویرگول ساخته می‌شود: <code>size = (200, 300)</code> یا <code>size = 200, 300</code>. چرا باید چیزی را بخواهیم که نمی‌شود تغییرش داد؟ چون تغییرناپذیری یک <em>قول</em> است: tuple می‌گوید «این رکورد ثابت است»؛ مختصات، ابعاد فرش، تاریخ به شکل (سال، ماه، روز). به‌علاوه tuple می‌تواند کلید دیکشنری و عضو set باشد، ولی list نه.</p>
<p>قاعده‌ی عملی: <strong>list برای مجموعه‌ای از چیزهای هم‌جنس با تعداد متغیر، tuple برای یک رکورد با ساختار ثابت</strong> که هر جایگاهش معنای خاصی دارد.</p>
<h3>unpacking: باز کردن در یک خط</h3>
<pre><code class="language-python">rug = ("KSH-101", 200, 300, "ابریشم")
code, width, length, material = rug

first, *middle, last = [3, 8, 1, 9, 4]
print(first, middle, last)      # 3 [8, 1, 9] 4

*_, latest = ["1403/01/05", "1403/02/11", "1403/03/20"]
print(latest)                   # 1403/03/20

for name, (w, l) in [("قالیچه", (100, 150)), ("پادری", (60, 90))]:
    print(name, w * l)</code></pre>
<p>ستاره (<code>*</code>) «هر چند عضو باقی‌مانده» را در یک لیست جمع می‌کند و در هر unpacking فقط یک بار می‌تواند بیاید. unpacking روی هر iterableی کار می‌کند؛ اگر تعداد جور نباشد، ValueError می‌گیرید که در واقع یک بررسی رایگان است.</p>
<h3>set: عضویت سریع و حذف تکرار</h3>
<p><strong>set</strong> مجموعه‌ای <em>بی‌ترتیب</em> از اعضای <em>یکتا</em> است. دو کاربرد اصلی دارد: حذف تکراری‌ها و پاسخ فوری به سؤال «آیا x عضو است؟».</p>
<pre><code class="language-python">codes = ["K1", "T1", "K1", "M2", "T1"]
unique = set(codes)                 # {'K1', 'T1', 'M2'}
ordered_unique = list(dict.fromkeys(codes))   # ['K1', 'T1', 'M2'] با حفظ ترتیب

kashan = {"ابریشم", "پشم", "نخ"}
tabriz = {"پشم", "نخ", "اکریلیک"}
print(kashan &amp; tabriz)    # اشتراک: {'پشم', 'نخ'}
print(kashan | tabriz)    # اجتماع
print(tabriz - kashan)    # تفاضل: {'اکریلیک'}
print(kashan ^ tabriz)    # تفاضل متقارن: فقط در یکی</code></pre>
<table><thead><tr><th>ویژگی</th><th>list</th><th>tuple</th><th>set</th></tr></thead><tbody>
<tr><td>ترتیب</td><td>دارد</td><td>دارد</td><td>ندارد</td></tr>
<tr><td>تکرار</td><td>مجاز</td><td>مجاز</td><td>خیر</td></tr>
<tr><td>تغییرپذیر</td><td>بله</td><td>خیر</td><td>بله (frozenset: خیر)</td></tr>
<tr><td>سرعت <code>in</code></td><td>کند (خطی)</td><td>کند (خطی)</td><td>تقریباً فوری</td></tr>
<tr><td>اندیس</td><td>بله</td><td>بله</td><td>خیر</td></tr>
</tbody></table>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>(5)</code> تاپل نیست، فقط عدد 5 در پرانتز است؛ تاپل تک‌عضوی ویرگول می‌خواهد: <code>(5,)</code>. همین ویرگول جاافتاده در انتهای یک خط، <code>x = 5,</code> را بی‌صدا به تاپل تبدیل می‌کند.</li>
<li><code>{}</code> دیکشنری خالی است، نه set خالی؛ set خالی را فقط با <code>set()</code> می‌سازید.</li>
<li>tuple تغییرناپذیر است، اما اگر عضوی تغییرپذیر (مثل لیست) داشته باشد، آن عضو هنوز قابل تغییر است؛ و چنین tupleی دیگر نمی‌تواند کلید دیکشنری باشد.</li>
<li><code>list(dict.fromkeys(items))</code> سریع‌ترین راه حذف تکرار با <em>حفظ ترتیب</em> است؛ <code>set</code> ترتیب را به هم می‌ریزد.</li>
<li>ترتیب چاپ اعضای یک set از رشته‌ها ممکن است در هر اجرای برنامه فرق کند (hash تصادفی رشته‌ها)؛ هرگز به ترتیب set تکیه نکنید.</li>
</ul>""",
                },
                {
                    "title": "dict: get، setdefault، items و مرتب‌سازی بر اساس مقدار",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>نگاشت کلید به مقدار</h2>
<p><strong>dict</strong> مهم‌ترین ساختار داده‌ی پایتون است؛ حتی خود زبان در درون از آن برای متغیرها و ویژگی‌های اشیا استفاده می‌کند. هر عضو یک جفت <strong>کلید: مقدار</strong> است و جست‌وجو با کلید تقریباً فوری انجام می‌شود، مهم نیست دیکشنری ده عضو داشته باشد یا ده میلیون. کلید باید تغییرناپذیر (hashable) باشد: رشته، عدد، tuple.</p>
<pre><code class="language-python">order = {
    "code": "KSH-101",
    "customer": "مریم کاشانی",
    "size": (200, 300),
    "price": 185_000_000,
}
print(order["customer"])
order["status"] = "weaving"      # افزودن یا تغییر
del order["size"]                # حذف
print("price" in order)          # بررسی وجود کلید (نه مقدار)</code></pre>
<p>از Python 3.7 به بعد، دیکشنری <strong>ترتیب درج</strong> را حفظ می‌کند؛ این بخشی از مشخصات رسمی زبان است، نه جزئیات پیاده‌سازی.</p>
<h3>خواندن امن: get</h3>
<p>دسترسی با <code>d[key]</code> اگر کلید نباشد <code>KeyError</code> می‌دهد. وقتی نبودن کلید طبیعی است، از <code>get</code> استفاده کنید:</p>
<pre><code class="language-python">stock = {"کاشان": 12, "تبریز": 7}
print(stock.get("مشهد"))         # None
print(stock.get("مشهد", 0))      # 0

for city in ["کاشان", "مشهد", "کاشان"]:
    stock[city] = stock.get(city, 0) + 1</code></pre>
<h3>setdefault: گروه‌بندی</h3>
<pre><code class="language-python">by_city = {}
for city, code in [("کاشان", "K1"), ("تبریز", "T1"), ("کاشان", "K2")]:
    by_city.setdefault(city, []).append(code)
print(by_city)     # {'کاشان': ['K1', 'K2'], 'تبریز': ['T1']}</code></pre>
<p><code>setdefault</code> اگر کلید نباشد، آن را با مقدار پیش‌فرض می‌سازد و در هر حال مقدار فعلی را برمی‌گرداند. (در درس collections راه تمیزتر defaultdict را می‌بینید.)</p>
<h3>پیمایش و مرتب‌سازی</h3>
<pre><code class="language-python">sales = {"کاشان": 42, "تبریز": 17, "مشهد": 29}

for city, count in sales.items():          # جفت کلید و مقدار
    print(f"{city:&lt;8}{count:&gt;5}")

top = sorted(sales.items(), key=lambda kv: kv[1], reverse=True)
print(top)                                 # [('کاشان', 42), ('مشهد', 29), ('تبریز', 17)]
print(max(sales, key=sales.get))           # کاشان

merged = sales | {"اصفهان": 11}            # ادغام (3.9+)
sales |= {"تبریز": 20}                     # به‌روزرسانی درجا</code></pre>
<table><thead><tr><th>متد</th><th>خروجی</th></tr></thead><tbody>
<tr><td><code>keys()</code></td><td>نمای کلیدها</td></tr>
<tr><td><code>values()</code></td><td>نمای مقادیر</td></tr>
<tr><td><code>items()</code></td><td>نمای جفت‌ها</td></tr>
<tr><td><code>pop(k, default)</code></td><td>حذف و برگرداندن مقدار</td></tr>
<tr><td><code>update(other)</code></td><td>ادغام درجا</td></tr>
</tbody></table>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>افزودن یا حذف کلید حین پیمایش دیکشنری خطای <code>RuntimeError: dictionary changed size during iteration</code> می‌دهد؛ روی <code>list(d)</code> پیمایش کنید.</li>
<li><code>1</code>، <code>1.0</code> و <code>True</code> به‌عنوان کلید یکی حساب می‌شوند! <code>{1: "a", True: "b"}</code> فقط یک عضو دارد: <code>{1: 'b'}</code>.</li>
<li><code>keys()</code> و <code>items()</code> «نما» (view) هستند و زنده‌اند؛ روی keys می‌توانید عملیات مجموعه بزنید: <code>d1.keys() &amp; d2.keys()</code> کلیدهای مشترک را می‌دهد.</li>
<li><code>dict(zip(names, prices))</code> دو لیست را در یک خط به دیکشنری تبدیل می‌کند؛ <code>{v: k for k, v in d.items()}</code> کلید و مقدار را جابه‌جا می‌کند.</li>
<li><code>d.get(k) or default</code> برای مقادیر صفر یا رشته‌ی خالی اشتباه است؛ همیشه <code>d.get(k, default)</code> بنویسید.</li>
</ul>""",
                },
                {
                    "title": "comprehension ها و sorted با key و lambda (و مرتب‌سازی الفبای فارسی)",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>ساختن مجموعه در یک خط خوانا</h2>
<p><strong>comprehension</strong> روشی فشرده برای ساختن list، dict یا set از روی یک iterable است. الگوی کلی: «عبارت برای هر عضو در مجموعه، اگر شرط». مقایسه کنید:</p>
<pre><code class="language-python">prices = [8_500_000, 12_000_000, 4_200_000, 15_700_000]

# روش حلقه‌ای
expensive = []
for p in prices:
    if p &gt; 10_000_000:
        expensive.append(p // 10)

# comprehension: همان کار، یک خط
expensive = [p // 10 for p in prices if p &gt; 10_000_000]</code></pre>
<table><thead><tr><th>نوع</th><th>نحو</th><th>نمونه</th></tr></thead><tbody>
<tr><td>list</td><td><code>[expr for x in it if cond]</code></td><td><code>[s * 2 for s in sizes]</code></td></tr>
<tr><td>dict</td><td><code>{k: v for x in it}</code></td><td><code>{c: len(c) for c in cities}</code></td></tr>
<tr><td>set</td><td><code>{expr for x in it}</code></td><td><code>{w.strip() for w in words}</code></td></tr>
<tr><td>generator</td><td><code>(expr for x in it)</code></td><td><code>sum(p for p in prices)</code></td></tr>
</tbody></table>
<p>دقت کنید «if در انتها» <em>فیلتر</em> می‌کند، اما «if/else در ابتدا» <em>تبدیل</em> است: <code>[p if p &gt; 0 else 0 for p in values]</code> هیچ عضوی را حذف نمی‌کند، فقط منفی‌ها را صفر می‌کند.</p>
<p>قاعده‌ی خوانایی: اگر comprehension از یک خط بیشتر شد یا دو حلقه‌ی تودرتو و چند شرط داشت، به حلقه‌ی معمولی برگردید. هدف کد کوتاه‌تر نیست، کد روشن‌تر است.</p>
<h3>sorted و پارامتر key</h3>
<p><code>sorted(iterable)</code> همیشه یک <strong>لیست جدید</strong> برمی‌گرداند و روی هر iterableی کار می‌کند. پارامتر <code>key</code> تابعی است که برای هر عضو «کلید مقایسه» تولید می‌کند. <strong>lambda</strong> تابع کوچک بی‌نامی است که فقط یک عبارت برمی‌گرداند و برای همین موقعیت‌ها ساخته شده است:</p>
<pre><code class="language-python">orders = [("رضا", 12, 9_500_000), ("مریم", 6, 7_800_000), ("سارا", 12, 8_200_000)]

by_price = sorted(orders, key=lambda o: o[2])
by_size_desc_then_price = sorted(orders, key=lambda o: (-o[1], o[2]))
names_ci = sorted(["b", "A", "c"], key=str.casefold)   # بدون حساسیت به حروف بزرگ</code></pre>
<p>ترفند تاپل در key: مرتب‌سازی چندسطحی را در یک خط انجام می‌دهد؛ اول بر اساس عضو اول تاپل، در صورت تساوی بر اساس دومی. منفی کردن عدد، ترتیب همان سطح را نزولی می‌کند.</p>
<h3>مرتب‌سازی درست فارسی</h3>
<p>پایتون رشته‌ها را بر اساس <strong>کد یونیکد</strong> مرتب می‌کند و در یونیکد، حروف «پ چ ژ ک گ ی» بعد از «و» و «ه» آمده‌اند (چون به الفبای عربی اضافه شده‌اند). نتیجه: «پارسا» بعد از «وحید» می‌آید! راه‌حل، کلید سفارشی بر اساس الفبای فارسی است:</p>
<pre><code class="language-python">FA_ALPHABET = "آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی"
ORDER = {ch: i for i, ch in enumerate(FA_ALPHABET)}

def fa_key(word: str) -&gt; list[int]:
    return [ORDER.get(ch, 100 + ord(ch)) for ch in word]

names = ["یاسمن", "پارسا", "وحید", "چنگیز", "علی", "گلناز", "آرش"]
print(sorted(names))              # ['آرش', 'علی', 'وحید', 'پارسا', ...]  غلط
print(sorted(names, key=fa_key))  # ['آرش', 'پارسا', 'چنگیز', 'علی', 'گلناز', 'وحید', 'یاسمن']</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>متغیر حلقه‌ی comprehension به بیرون نشت نمی‌کند (برخلاف حلقه‌ی for معمولی)؛ <code>x</code> داخل <code>[x for x in ...]</code> بعد از آن تعریف نشده است.</li>
<li><code>sum([x * x for x in data])</code> اول کل لیست را می‌سازد؛ <code>sum(x * x for x in data)</code> بدون کروشه، عضوبه‌عضو و با حافظه‌ی ثابت کار می‌کند.</li>
<li><code>operator.itemgetter(2)</code> معادل سریع‌تر و خواناتر <code>lambda o: o[2]</code> است و با چند اندیس هم کار می‌کند: <code>itemgetter(1, 2)</code>.</li>
<li>در comprehension تودرتو ترتیب حلقه‌ها مثل حلقه‌های تودرتوی معمولی است: <code>[(r, c) for r in rows for c in cols]</code>؛ حلقه‌ی بیرونی اول می‌آید.</li>
<li>برای مرتب‌سازی حرفه‌ای‌تر فارسی (نادیده گرفتن نیم‌فاصله، اعراب و «ي» عربی)، قبل از fa_key متن را یکسان‌سازی کنید؛ کتابخانه‌ی PyICU هم collation کامل فارسی دارد.</li>
</ul>""",
                },
                {
                    "title": "collections: Counter، defaultdict، namedtuple و deque",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>ابزارهای آماده برای کارهای تکراری</h2>
<p>ماژول <code>collections</code> در کتابخانه‌ی استاندارد، نسخه‌های تخصصی dict، tuple و list را دارد که کدهای رایج را کوتاه‌تر، سریع‌تر و کم‌خطاتر می‌کنند. هر برنامه‌نویس پایتون باید این چهار ابزار را بشناسد.</p>
<h3>Counter: شمارش در یک خط</h3>
<pre><code class="language-python">from collections import Counter

sold = ["کاشان", "تبریز", "کاشان", "مشهد", "کاشان", "تبریز"]
c = Counter(sold)
print(c)                     # Counter({'کاشان': 3, 'تبریز': 2, 'مشهد': 1})
print(c.most_common(2))      # [('کاشان', 3), ('تبریز', 2)]
print(c["اصفهان"])           # 0 — کلید نبود، KeyError نمی‌دهد

c.update(["مشهد", "مشهد"])   # افزودن شمارش
words = Counter("فرش دستباف کاشان فرش ماشینی".split())
print(sum(c.values()))       # جمع کل</code></pre>
<p>Counter از جمع و تفریق هم پشتیبانی می‌کند: <code>farvardin + ordibehesht</code> فروش دو ماه را جمع می‌کند و <code>stock - sold</code> موجودی باقی‌مانده را می‌دهد (نتیجه‌های صفر و منفی حذف می‌شوند).</p>
<h3>defaultdict: دیکشنری با مقدار پیش‌فرض خودکار</h3>
<pre><code class="language-python">from collections import defaultdict

by_city = defaultdict(list)
for city, code in [("کاشان", "K1"), ("تبریز", "T1"), ("کاشان", "K2")]:
    by_city[city].append(code)       # بدون get و setdefault

totals = defaultdict(int)            # int() یعنی 0
for city, amount in [("کاشان", 5), ("کاشان", 3)]:
    totals[city] += amount</code></pre>
<p>آرگومان defaultdict یک <em>تابع سازنده</em> است (<code>list</code>، <code>int</code>، <code>set</code>)، نه یک مقدار. هر بار کلید ناموجودی خوانده شود، آن تابع صدا زده می‌شود.</p>
<h3>namedtuple: tuple با نام فیلد</h3>
<pre><code class="language-python">from collections import namedtuple

Rug = namedtuple("Rug", "code width length material")
r = Rug("KSH-101", 200, 300, "ابریشم")
print(r.width * r.length)            # 60000 — به‌جای r[1] * r[2]
print(r._asdict())                   # تبدیل به dict
r2 = r._replace(width=250)           # نسخه‌ی جدید؛ اصلی تغییرناپذیر است</code></pre>
<p>namedtuple برای رکوردهای سبک و تغییرناپذیر عالی است. اگر به مقدار پیش‌فرض، متد یا تغییرپذیری نیاز داشتید، سراغ <code>dataclass</code> بروید (فصل ۷).</p>
<h3>deque: صف دوطرفه</h3>
<pre><code class="language-python">from collections import deque

recent = deque(maxlen=3)             # فقط سه عضو آخر نگه داشته می‌شود
for code in ["K1", "K2", "K3", "K4"]:
    recent.append(code)
print(recent)                        # deque(['K2', 'K3', 'K4'], maxlen=3)

queue = deque(["سفارش ۱", "سفارش ۲"])
queue.append("سفارش ۳")              # ورود از انتها
first = queue.popleft()              # خروج از ابتدا — سریع</code></pre>
<table><thead><tr><th>ابزار</th><th>جایگزین چه کدی</th></tr></thead><tbody>
<tr><td>Counter</td><td><code>d[k] = d.get(k, 0) + 1</code> در حلقه</td></tr>
<tr><td>defaultdict</td><td><code>d.setdefault(k, []).append(v)</code></td></tr>
<tr><td>namedtuple</td><td>tuple با اندیس‌های جادویی <code>r[2]</code></td></tr>
<tr><td>deque</td><td><code>list.pop(0)</code> و <code>list.insert(0, x)</code></td></tr>
</tbody></table>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>خواندن کلید ناموجود از defaultdict آن کلید را <em>می‌سازد</em>؛ حتی یک <code>print(d["x"])</code> ساده دیکشنری را بزرگ می‌کند. برای بررسی، از <code>"x" in d</code> استفاده کنید.</li>
<li><code>Counter("کاشان")</code> حروف را می‌شمارد، نه کلمه را؛ برای کلمه اول <code>split()</code> بزنید.</li>
<li><code>deque(maxlen=n)</code> ساده‌ترین راه ساختن «n رکورد آخر» یا تاریخچه‌ی محدود است؛ عضوهای قدیمی خودکار بیرون می‌افتند.</li>
<li><code>Counter.total()</code> (3.10+) جمع همه‌ی شمارش‌ها را می‌دهد و از <code>sum(c.values())</code> خواناتر است.</li>
<li>قبل از json.dump کردن defaultdict، آن را با <code>dict(d)</code> تبدیل کنید تا خروجی و repr تمیز باشد.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۵ ─────────────────────────────
        {
            "title": "فصل ۵: توابع — از تعریف ساده تا scope و بازگشت",
            "lessons": [
                {
                    "title": "تعریف تابع، return، پارامتر پیش‌فرض و دام پیش‌فرض mutable",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>کد را یک بار بنویسید، بارها استفاده کنید</h2>
<p><strong>تابع</strong> یک تکه کد نام‌دار است که ورودی (پارامتر) می‌گیرد و خروجی برمی‌گرداند. هر وقت دیدید یک منطق را دو بار کپی کرده‌اید، وقت ساختن تابع است. تابع سه مزیت دارد: تکرار را حذف می‌کند، به منطق یک <em>نام</em> می‌دهد (که خودش مستندسازی است) و آزمودن را ممکن می‌کند.</p>
<pre><code class="language-python">def rug_price(width_cm, length_cm, price_per_sqm):
    area = width_cm * length_cm / 10_000
    return round(area * price_per_sqm)

p = rug_price(200, 300, 9_500_000)
print(f"{p:,} ریال")          # 57,000,000 ریال</code></pre>
<p>اجزا: کلمه‌ی <code>def</code>، نام تابع (snake_case)، پارامترها در پرانتز، دونقطه و بدنه‌ی تورفته. <code>return</code> اجرای تابع را <strong>همان لحظه</strong> تمام می‌کند و مقدار را به فراخواننده برمی‌گرداند. تابعی که return ندارد (یا return خالی دارد) در واقع <code>None</code> برمی‌گرداند.</p>
<h3>print در برابر return</h3>
<p>اشتباه رایج تازه‌کارها این است که به‌جای return، نتیجه را داخل تابع print می‌کنند. print فقط روی صفحه نشان می‌دهد و مقدار را به برنامه برنمی‌گرداند؛ نمی‌توانید نتیجه را جمع بزنید، ذخیره کنید یا تست کنید. قاعده: <strong>توابع محاسبه return می‌کنند؛ فقط لایه‌ی نمایش print می‌کند.</strong></p>
<h3>return زودهنگام و چند مقدار</h3>
<pre><code class="language-python">def shipping_cost(area, city):
    if city == "کاشان":
        return 0                      # حالت خاص را زود رد کن
    if area &gt;= 12:
        return 0
    return 350_000 if area &gt;= 6 else 600_000

def min_max(values):
    return min(values), max(values)   # در واقع یک tuple

low, high = min_max([12, 6, 30])</code></pre>
<p>الگوی «نگهبان» (guard clause) با return زودهنگام، کد را از if های تودرتو نجات می‌دهد.</p>
<h3>پارامتر پیش‌فرض</h3>
<pre><code class="language-python">def price_with_tax(amount, rate=0.10):
    return round(amount * (1 + rate))

price_with_tax(1_000_000)             # با نرخ پیش‌فرض
price_with_tax(1_000_000, rate=0.09)  # با نام، خواناتر</code></pre>
<h3>دام معروف: پیش‌فرض تغییرپذیر</h3>
<pre><code class="language-python">def add_item(item, basket=[]):        # اشتباه!
    basket.append(item)
    return basket

print(add_item("K1"))   # ['K1']
print(add_item("K2"))   # ['K1', 'K2']  — سبد قبلی هنوز آن‌جاست!</code></pre>
<p>مقدار پیش‌فرض <strong>فقط یک بار</strong>، هنگام تعریف تابع ساخته می‌شود، نه در هر فراخوانی. پس همه‌ی فراخوانی‌ها یک لیست مشترک دارند. الگوی درست استفاده از None است:</p>
<pre><code class="language-python">def add_item(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>همین «یک‌بار ساخته شدن» برای <code>def log(msg, when=datetime.now())</code> هم صدق می‌کند: همه‌ی لاگ‌ها زمان بارگذاری ماژول را می‌گیرند. زمان را داخل تابع حساب کنید.</li>
<li>در Ruff و Pylint قاعده‌ای به نام B006 یا dangerous-default-value همین دام را خودکار پیدا می‌کند؛ روشنش کنید.</li>
<li>تابع هم یک شیء است: <code>rug_price.__name__</code> نامش را می‌دهد و می‌توانید آن را در متغیر، لیست یا دیکشنری بگذارید (درس آخر همین فصل).</li>
<li>بدنه‌ی تابعی را که هنوز ننوشته‌اید با <code>...</code> پر کنید؛ کد اجرا می‌شود و یادتان می‌ماند که جای خالی دارد.</li>
<li>پایتون overloading ندارد: اگر دو تابع هم‌نام تعریف کنید، دومی بی‌صدا اولی را جایگزین می‌کند. Ruff این را هم با قاعده‌ی F811 تشخیص می‌دهد.</li>
</ul>""",
                },
                {
                    "title": "*args، **kwargs، آرگومان keyword-only و positional-only",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>امضای تابع، قرارداد با فراخواننده</h2>
<p>آرگومان‌ها را می‌توان به دو شکل فرستاد: <strong>موقعیتی</strong> (positional) که بر اساس ترتیب به پارامترها می‌رسند، و <strong>با نام</strong> (keyword) که بر اساس نام. <code>rug_price(200, 300, 9_500_000)</code> موقعیتی است و <code>rug_price(width_cm=200, length_cm=300, price_per_sqm=9_500_000)</code> با نام. در یک فراخوانی می‌توانید ترکیب کنید، به شرط این‌که موقعیتی‌ها اول بیایند.</p>
<h3>*args: تعداد دلخواه آرگومان موقعیتی</h3>
<pre><code class="language-python">def total(*prices, discount=0):
    # prices یک tuple است
    return sum(prices) * (100 - discount) // 100

print(total(8_500_000, 12_000_000))                 # 20500000
print(total(8_500_000, 12_000_000, discount=10))    # 18450000</code></pre>
<p>ستاره در تعریف یعنی «همه‌ی آرگومان‌های موقعیتی باقی‌مانده را در یک tuple جمع کن». نام <code>args</code> فقط قرارداد است؛ <code>*prices</code> گویاتر است.</p>
<h3>**kwargs: تعداد دلخواه آرگومان با نام</h3>
<pre><code class="language-python">def make_label(code, **details):
    # details یک dict است
    parts = [f"{k}={v}" for k, v in details.items()]
    return f"{code} ({', '.join(parts)})"

print(make_label("KSH-101", color="لاکی", raj=50))
# KSH-101 (color=لاکی, raj=50)</code></pre>
<h3>keyword-only و positional-only</h3>
<p>هر پارامتری که بعد از <code>*</code> (یا بعد از <code>*args</code>) بیاید، <strong>فقط با نام</strong> قابل ارسال است. هر پارامتری که قبل از <code>/</code> بیاید، <strong>فقط موقعیتی</strong>:</p>
<pre><code class="language-python">def make_order(code, /, qty, *, express=False):
    return code, qty, express

make_order("K1", 2)                    # درست
make_order("K1", qty=2, express=True)  # درست
make_order("K1", 2, True)              # TypeError: express باید با نام بیاید</code></pre>
<p>چرا این محدودیت‌ها مفیدند؟ فراخوانی <code>send_sms("0912...", "سلام", True, False)</code> را در نظر بگیرید؛ True و False چه معنایی دارند؟ با keyword-only، فراخواننده مجبور است بنویسد <code>urgent=True</code> و کد خودش را توضیح می‌دهد. positional-only هم اجازه می‌دهد بعداً نام پارامتر را بدون شکستن کد دیگران عوض کنید.</p>
<table><thead><tr><th>نماد در تعریف</th><th>معنی</th></tr></thead><tbody>
<tr><td><code>a, b</code></td><td>معمولی: موقعیتی یا با نام</td></tr>
<tr><td><code>a, /</code></td><td>a فقط موقعیتی</td></tr>
<tr><td><code>*, a</code></td><td>a فقط با نام</td></tr>
<tr><td><code>*args</code></td><td>بقیه‌ی موقعیتی‌ها در tuple</td></tr>
<tr><td><code>**kwargs</code></td><td>بقیه‌ی با نام‌ها در dict؛ همیشه آخر</td></tr>
</tbody></table>
<h3>باز کردن هنگام فراخوانی</h3>
<p>ستاره در <em>فراخوانی</em> برعکس عمل می‌کند و مجموعه را باز می‌کند:</p>
<pre><code class="language-python">size = (200, 300)
options = {"price_per_sqm": 9_500_000}
rug_price(*size, **options)   # معادل rug_price(200, 300, price_per_sqm=9_500_000)</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>ترتیب مجاز در تعریف همیشه این است: موقعیتی‌فقط، <code>/</code>، معمولی، <code>*args</code> یا <code>*</code>، keyword-only، <code>**kwargs</code>.</li>
<li>خود <code>print</code> امضایی شبیه <code>print(*objects, sep=" ", end="\n")</code> دارد؛ برای همین <code>print(*items, sep=" | ")</code> لیست را با جداکننده چاپ می‌کند.</li>
<li><code>**kwargs</code> راحت است ولی غلط‌های تایپی را می‌بلعد: <code>make_label("K1", colour="قرمز")</code> خطا نمی‌دهد. جایی که پارامترها مشخص‌اند، صریح نامشان را بنویسید.</li>
<li>برای ادغام دو دیکشنری هنگام فراخوانی: <code>f(**defaults, **overrides)</code>؛ اما اگر کلید تکراری باشد، TypeError می‌گیرید (برخلاف عملگر <code>|</code>).</li>
<li>آرگومان‌های با نام را در فراخوانی به هر ترتیبی می‌توانید بنویسید؛ پس در توابع با چند پارامتر، نام‌دار فرستادن جلوی جابه‌جا شدن عرض و طول را می‌گیرد.</li>
</ul>""",
                },
                {
                    "title": "scope و قاعده‌ی LEGB، global و nonlocal",
                    "kind": "text",
                    "minutes": 18,
                    "is_preview": False,
                    "body": r"""<h2>هر نام کجا زندگی می‌کند؟</h2>
<p>وقتی در کد نامی مثل <code>rate</code> را می‌خوانید، پایتون باید بفهمد این نام به کدام شیء اشاره دارد. پاسخ از قاعده‌ی <strong>LEGB</strong> می‌آید؛ پایتون به این ترتیب جست‌وجو می‌کند و اولین مورد را برمی‌دارد:</p>
<table><thead><tr><th>حرف</th><th>دامنه</th><th>مثال</th></tr></thead><tbody>
<tr><td>L — Local</td><td>داخل همین تابع</td><td>پارامترها و متغیرهای تعریف‌شده در تابع</td></tr>
<tr><td>E — Enclosing</td><td>تابع بیرونی (در توابع تودرتو)</td><td>متغیرهای تابعی که این تابع را در خود دارد</td></tr>
<tr><td>G — Global</td><td>سطح ماژول (فایل)</td><td>ثابت‌ها و توابع تعریف‌شده در بالای فایل</td></tr>
<tr><td>B — Built-in</td><td>نام‌های داخلی پایتون</td><td><code>len</code>، <code>print</code>، <code>sum</code></td></tr>
</tbody></table>
<pre><code class="language-python">TAX_RATE = 0.10                  # Global

def invoice(amount):
    discount = 0.05              # Local
    def apply():
        return amount * (1 - discount) * (1 + TAX_RATE)   # E و G
    return round(apply())

print(invoice(10_000_000))       # 10450000
print(discount)                  # NameError — discount بیرون تابع وجود ندارد</code></pre>
<p>متغیرهای محلی با پایان تابع از بین می‌روند و هر فراخوانی، مجموعه‌ی محلی تازه‌ی خودش را دارد. این جداسازی چیز خوبی است: تابع با دنیای بیرون فقط از راه پارامتر و return حرف می‌زند.</p>
<h3>دام UnboundLocalError</h3>
<pre><code class="language-python">count = 0

def register():
    count += 1          # UnboundLocalError!
    return count</code></pre>
<p>چرا خواندن متغیر global مجاز است ولی این کد خطا می‌دهد؟ چون پایتون <strong>در زمان کامپایل</strong> تصمیم می‌گیرد: هر نامی که داخل تابع به آن <em>انتساب</em> شود (از جمله با <code>+=</code>)، در کل آن تابع محلی است. پس <code>count</code> محلی حساب می‌شود و هنوز مقدار نگرفته است.</p>
<h3>global و nonlocal</h3>
<pre><code class="language-python">count = 0

def register():
    global count        # «منظورم همان count سطح ماژول است»
    count += 1

def make_counter():
    n = 0
    def step():
        nonlocal n      # «منظورم n تابع بیرونی است»
        n += 1
        return n
    return step

next_id = make_counter()
next_id(); next_id()
print(next_id())        # 3</code></pre>
<p>مثال دوم یک <strong>closure</strong> است: تابع داخلی متغیر تابع بیرونی را حتی پس از پایان آن «به خاطر می‌سپارد». این پایه‌ی decorator هاست که در پایان دوره به آن اشاره می‌کنیم.</p>
<h3>چرا global بد نام است</h3>
<p>متغیر global را هر تابعی می‌تواند عوض کند؛ پس وقتی مقدارش غلط است، نمی‌دانید مقصر کیست. تست کردن توابعی که به global وابسته‌اند هم سخت است. قاعده: <strong>ثابت‌های global (با حروف بزرگ) خوب‌اند؛ حالت (state) global بد است.</strong> حالت را از راه پارامتر بدهید و از راه return بگیرید، یا در یک کلاس (فصل ۷) بسته‌بندی کنید.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>برای تغییر <em>محتوای</em> یک لیست یا دیکشنری global به global نیاز ندارید (<code>orders.append(x)</code> کار می‌کند)؛ global فقط برای <em>انتساب دوباره‌ی نام</em> لازم است.</li>
<li>حلقه‌ی for و بلوک if در پایتون scope جدید نمی‌سازند؛ متغیر تعریف‌شده داخل if بعد از آن هم در دسترس است.</li>
<li><code>globals()</code> و <code>locals()</code> دیکشنری نام‌ها را برمی‌گردانند؛ برای دیباگ مفید، برای کد اصلی ممنوع.</li>
<li>closure ها متغیر را «زنده» نگه می‌دارند، نه مقدارش را؛ به همین دلیل lambda های ساخته‌شده در حلقه همه آخرین مقدار را می‌بینند (درس آخر همین فصل).</li>
<li>اگر نام یک built-in را در سطح ماژول بازتعریف کنید (مثلاً <code>input = ...</code>)، طبق LEGB همه‌ی توابع آن فایل نسخه‌ی شما را می‌بینند.</li>
</ul>""",
                },
                {
                    "title": "docstring و type hints مقدماتی",
                    "kind": "text",
                    "minutes": 18,
                    "is_preview": False,
                    "body": r"""<h2>کدی که خودش را توضیح می‌دهد</h2>
<p>دو ابزار کد را برای انسان‌ها و ابزارها خواناتر می‌کنند: <strong>docstring</strong> که می‌گوید تابع <em>چه</em> می‌کند، و <strong>type hint</strong> که می‌گوید <em>چه نوعی</em> می‌گیرد و برمی‌گرداند.</p>
<h3>docstring</h3>
<p>اولین رشته‌ی داخل بدنه‌ی تابع، کلاس یا ماژول، docstring آن است. طبق قرارداد با سه دابل‌کوتیشن نوشته می‌شود:</p>
<pre><code class="language-python">def rug_price(width_cm: int, length_cm: int, price_per_sqm: int) -&gt; int:
    &quot;&quot;&quot;قیمت فرش را بر اساس ابعاد و قیمت هر متر مربع حساب می‌کند.

    width_cm و length_cm بر حسب سانتی‌متر و قیمت بر حسب ریال است.
    نتیجه به نزدیک‌ترین ریال گرد می‌شود.
    &quot;&quot;&quot;
    area = width_cm * length_cm / 10_000
    return round(area * price_per_sqm)

help(rug_price)            # docstring را نشان می‌دهد
print(rug_price.__doc__)</code></pre>
<p>خط اول یک جمله‌ی خلاصه است؛ سپس یک خط خالی و جزئیات. VS Code با نگه داشتن ماوس روی نام تابع همین متن را نمایش می‌دهد. docstring بگوید «چه» و «چرا»؛ «چطور» را خود کد نشان می‌دهد.</p>
<h3>type hints</h3>
<p>از پایتون ۳.۵ می‌توانید نوع پارامترها و خروجی را اعلام کنید. نکته‌ی بسیار مهم: <strong>پایتون در زمان اجرا این نوع‌ها را بررسی نمی‌کند</strong>. <code>rug_price("200", 300, 1)</code> با وجود hint اجرا می‌شود (و البته جای دیگری خطا می‌دهد). ارزش hint ها در ابزارهاست: Pylance در VS Code، mypy و Ruff اشتباه را قبل از اجرا زیر کد خط قرمز می‌کشند و تکمیل خودکار دقیق‌تر می‌شود.</p>
<table><thead><tr><th>hint</th><th>معنی</th></tr></thead><tbody>
<tr><td><code>int</code>، <code>str</code>، <code>float</code>، <code>bool</code></td><td>انواع ساده</td></tr>
<tr><td><code>list[str]</code></td><td>لیستی از رشته‌ها (از 3.9 بدون import)</td></tr>
<tr><td><code>dict[str, int]</code></td><td>دیکشنری با کلید رشته و مقدار عدد</td></tr>
<tr><td><code>tuple[int, int]</code></td><td>تاپل دقیقاً دوتایی</td></tr>
<tr><td><code>int | None</code></td><td>عدد یا None (از 3.10)</td></tr>
<tr><td><code>-&gt; None</code></td><td>تابع چیزی برنمی‌گرداند</td></tr>
</tbody></table>
<pre><code class="language-python">def find_order(orders: list[dict], code: str) -&gt; dict | None:
    for order in orders:
        if order["code"] == code:
            return order
    return None

def city_totals(rows: list[tuple[str, int]]) -&gt; dict[str, int]:
    totals: dict[str, int] = {}
    for city, amount in rows:
        totals[city] = totals.get(city, 0) + amount
    return totals</code></pre>
<p>با <code>dict | None</code> در خروجی، Pylance اگر بدون بررسی None بنویسید <code>find_order(...)["price"]</code> هشدار می‌دهد؛ یعنی یک باگ واقعی قبل از اجرا گرفته شده است.</p>
<p>در این دوره‌ی مقدماتی hint را در حد همین جدول نگه می‌داریم. مباحثی مثل Protocol، TypeVar و generic ها در دوره‌ی پایتون پیشرفته آمده‌اند.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>در VS Code تنظیم <code>python.analysis.typeCheckingMode</code> را روی <code>basic</code> یا <code>standard</code> بگذارید تا Pylance خطاهای نوع را واقعاً گزارش کند؛ پیش‌فرض آن off است.</li>
<li>اگر اولین عبارت تابع یک f-string باشد، docstring حساب نمی‌شود و <code>__doc__</code> برابر None است؛ docstring باید رشته‌ی ثابت باشد.</li>
<li><code>list[int]</code> در زمان اجرا چیزی را محدود نمی‌کند؛ <code>isinstance(x, list[int])</code> حتی خطا می‌دهد. hint برای ابزارهاست، نه اعتبارسنجی.</li>
<li>برای مستندسازی واحد، hint جای خوبی نیست؛ واحد را در نام پارامتر بیاورید (<code>width_cm</code>) که هم در کد و هم در فراخوانی دیده می‌شود.</li>
<li>متغیر را هم می‌توان annotate کرد (<code>totals: dict[str, int] = {}</code>)؛ برای ظرف‌های خالی که ابزار نمی‌تواند نوعشان را حدس بزند بسیار مفید است.</li>
</ul>""",
                },
                {
                    "title": "توابع به‌عنوان مقدار، lambda، بازگشت (recursion) و محدودیتش",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>تابع هم یک شیء است</h2>
<p>در پایتون تابع «شهروند درجه یک» است: می‌توانید آن را در متغیر بگذارید، به تابع دیگر بفرستید، از تابع برگردانید و در لیست یا دیکشنری نگه دارید. همین ویژگی است که <code>sorted(..., key=len)</code> را ممکن می‌کند؛ ما خود تابع <code>len</code> را (بدون پرانتز) می‌فرستیم تا sorted هر وقت لازم داشت صدایش بزند.</p>
<pre><code class="language-python">def to_toman(rial: int) -&gt; int:
    return rial // 10

convert = to_toman              # بدون پرانتز: خود تابع، نه نتیجه‌اش
print(convert(125_000_000))     # 12500000

def apply_all(fn, values):
    return [fn(v) for v in values]

print(apply_all(to_toman, [10_000, 250_000]))   # [1000, 25000]</code></pre>
<h3>دیکشنری از توابع: جایگزین if های طولانی</h3>
<pre><code class="language-python">def report_daily(): return "گزارش روزانه"
def report_monthly(): return "گزارش ماهانه"

REPORTS = {"daily": report_daily, "monthly": report_monthly}

choice = "monthly"
action = REPORTS.get(choice)
print(action() if action else "گزارش ناشناخته")</code></pre>
<h3>lambda</h3>
<p><code>lambda</code> تابعی بی‌نام با <strong>یک عبارت</strong> است: <code>lambda a, b: a + b</code>. جای درستش آرگومان کوتاه برای توابعی مثل sorted، max و min است. اگر lambda را در متغیر ذخیره می‌کنید (<code>f = lambda x: ...</code>)، همان‌جا با def بنویسیدش؛ نام دارد، docstring می‌گیرد و در پیام خطا شناخته می‌شود.</p>
<h3>بازگشت (recursion)</h3>
<p>تابع بازگشتی خودش را صدا می‌زند. هر تابع بازگشتی دو جزء دارد: <strong>حالت پایه</strong> که بدون بازگشت جواب می‌دهد، و <strong>گام بازگشتی</strong> که مسئله را کوچک‌تر می‌کند. برای ساختارهای درختی (پوشه‌ها، دسته‌بندی‌های تودرتوی محصول) طبیعی‌ترین راه‌حل است:</p>
<pre><code class="language-python">catalog = {
    "فرش دستباف": {"کاشان": 42, "تبریز": 17},
    "فرش ماشینی": {"۷۰۰ شانه": {"کاشان": 120, "آران": 35}, "۱۲۰۰ شانه": 64},
}

def count_items(tree) -&gt; int:
    total = 0
    for value in tree.values():
        if isinstance(value, dict):
            total += count_items(value)   # گام بازگشتی
        else:
            total += value                # حالت پایه
    return total

print(count_items(catalog))              # 278</code></pre>
<h3>محدودیت بازگشت در پایتون</h3>
<p>پایتون عمق بازگشت را به‌طور پیش‌فرض به حدود ۱۰۰۰ محدود می‌کند (<code>sys.getrecursionlimit()</code>) و پس از آن <code>RecursionError</code> می‌دهد. پایتون «بهینه‌سازی فراخوانی انتهایی» هم ندارد. پس برای مسائلی که عمقشان به اندازه‌ی داده است (مثل پیمایش یک لیست صدهزارتایی) از حلقه استفاده کنید و بازگشت را برای ساختارهای درختی با عمق محدود نگه دارید.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>دام lambda در حلقه: <code>[lambda: i for i in range(3)]</code> سه تابع می‌سازد که همه 2 برمی‌گردانند، چون i را هنگام <em>اجرا</em> می‌خوانند. راه‌حل: <code>lambda i=i: i</code>.</li>
<li><code>functools.lru_cache</code> نتیجه‌ی توابع بازگشتی مثل فیبوناچی را کش می‌کند و زمان را از نمایی به خطی می‌رساند؛ فقط یک خط بالای تابع (<code>@lru_cache</code>).</li>
<li><code>sys.setrecursionlimit</code> را بی‌گدار بالا نبرید؛ پشته‌ی واقعی سیستم‌عامل محدود است و برنامه ممکن است بدون پیام خطا کرش کند.</li>
<li>بسیاری از توابع آماده مثل <code>str.upper</code> و <code>int</code> را مستقیم به‌عنوان key یا در map بفرستید: <code>list(map(int, ["1", "2"]))</code>؛ lambda اضافه لازم نیست.</li>
<li><code>filter(None, items)</code> همه‌ی اعضای falsy (صفر، رشته‌ی خالی، None) را حذف می‌کند؛ کوتاه‌ترین راه تمیز کردن لیست.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۶ ─────────────────────────────
        {
            "title": "فصل ۶: فایل‌ها و خطاها — pathlib، UTF-8، CSV، JSON و logging",
            "lessons": [
                {
                    "title": "pathlib: کار با مسیرها بدون دردسر بک‌اسلش ویندوز",
                    "kind": "text",
                    "minutes": 18,
                    "is_preview": False,
                    "body": r"""<h2>مسیر، یک شیء است نه یک رشته</h2>
<p>در کدهای قدیمی مسیرها را با رشته و <code>os.path.join</code> می‌ساختند. روش مدرن ماژول <strong>pathlib</strong> است که مسیر را یک شیء با متدهای مفید می‌کند و تفاوت ویندوز (<code>\</code>) و لینوکس (<code>/</code>) را خودش مدیریت می‌کند.</p>
<pre><code class="language-python">from pathlib import Path

base = Path(__file__).resolve().parent     # پوشه‌ی همین اسکریپت
data = base / "data"                        # عملگر / مسیر را می‌چسباند
report = data / "orders-1403.csv"

print(report.name)      # orders-1403.csv
print(report.stem)      # orders-1403
print(report.suffix)    # .csv
print(report.parent)    # ...\data
print(report.with_suffix(".json").name)   # orders-1403.json
print(report.exists(), report.is_file())</code></pre>
<h3>دام بک‌اسلش در ویندوز</h3>
<p>در رشته‌های پایتون، بک‌اسلش شروع «کاراکتر ویژه» است: <code>\n</code> یعنی خط جدید و <code>\t</code> یعنی Tab. پس مسیر <code>"C:\new\test.txt"</code> در واقع شامل یک خط جدید و یک Tab است! سه راه‌حل:</p>
<table><thead><tr><th>روش</th><th>نمونه</th><th>توصیه</th></tr></thead><tbody>
<tr><td>رشته‌ی خام (raw)</td><td><code>r"C:\new\test.txt"</code></td><td>برای کپی مسیر از Explorer</td></tr>
<tr><td>اسلش رو به جلو</td><td><code>"C:/new/test.txt"</code></td><td>ویندوز هم می‌پذیرد</td></tr>
<tr><td>pathlib</td><td><code>Path("C:/") / "new" / "test.txt"</code></td><td>بهترین؛ قابل‌حمل</td></tr>
</tbody></table>
<h3>ساخت، پیدا کردن و پیمایش</h3>
<pre><code class="language-python">out = Path("output") / "reports" / "1403"
out.mkdir(parents=True, exist_ok=True)    # ساخت همه‌ی پوشه‌های میانی، بدون خطا اگر وجود داشت

for csv_file in sorted(Path("data").glob("*.csv")):
    print(csv_file.name, csv_file.stat().st_size, "بایت")

all_json = list(Path("data").rglob("*.json"))   # جست‌وجوی بازگشتی در زیرپوشه‌ها

home = Path.home()                 # C:\Users\نام‌کاربری
desktop = home / "Desktop"</code></pre>
<h3>خواندن و نوشتن سریع</h3>
<p>برای فایل‌های کوچک، pathlib متدهای یک‌خطی دارد: <code>path.read_text(encoding="utf-8")</code> و <code>path.write_text(text, encoding="utf-8")</code>. برای فایل‌های بزرگ یا خط‌به‌خط، از <code>open</code> در درس بعد استفاده کنید.</p>
<h3>مسیر نسبی نسبت به چه؟</h3>
<p>مسیر نسبی مثل <code>Path("data")</code> نسبت به <strong>پوشه‌ی جاری</strong> (current working directory) حل می‌شود، نه نسبت به محل فایل اسکریپت. اگر اسکریپت را از پوشه‌ی دیگری اجرا کنید یا از Task Scheduler، «فایل پیدا نشد» می‌گیرید. برای فایل‌هایی که کنار اسکریپت هستند، همیشه از <code>Path(__file__).resolve().parent</code> شروع کنید.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>رشته‌ی خام نمی‌تواند به یک بک‌اسلش تک ختم شود: <code>r"C:\data\"</code> خطای نحوی است. یکی از دلایل خوب برای استفاده از pathlib.</li>
<li><code>Path.cwd()</code> پوشه‌ی جاری را نشان می‌دهد؛ اولین چیزی که هنگام «فایل پیدا نمی‌شود» باید چاپ کنید.</li>
<li><code>path.unlink(missing_ok=True)</code> فایل را حذف می‌کند و اگر نبود خطا نمی‌دهد؛ برای پوشه‌ی پر از <code>shutil.rmtree</code> استفاده کنید (با احتیاط!).</li>
<li><code>glob</code> در ویندوز به بزرگی و کوچکی حروف حساس نیست ولی در لینوکس حساس است؛ <code>*.CSV</code> روی سرور لینوکسی فایل <code>a.csv</code> را پیدا نمی‌کند.</li>
<li><code>os.startfile(path)</code> (فقط ویندوز) فایل را با برنامه‌ی پیش‌فرضش باز می‌کند؛ برای باز کردن خودکار گزارش اکسل بعد از ساخت عالی است.</li>
</ul>""",
                },
                {
                    "title": "open، encoding=\"utf-8\" و with: فایل متنی فارسی بدون خرابی",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>مهم‌ترین آرگومانی که همه فراموش می‌کنند</h2>
<p>فایل روی دیسک فقط بایت است. برای تبدیل بایت به متن (و برعکس) باید <strong>کدگذاری</strong> (encoding) مشخص شود. اگر آن را ننویسید، پایتون از کدگذاری پیش‌فرض سیستم‌عامل استفاده می‌کند؛ در لینوکس و مک UTF-8 است، اما در ویندوز با تنظیمات منطقه‌ای فارسی معمولاً <strong>cp1256</strong> (کدگذاری قدیمی عربی ویندوز). نتیجه: کدی که روی لپ‌تاپ شما درست کار می‌کند روی سرور لینوکسی فارسی را خراب می‌کند یا <code>UnicodeDecodeError</code> می‌دهد. قاعده‌ی بی‌استثنا:</p>
<p><strong>هر open متنی، encoding="utf-8" صریح دارد.</strong></p>
<pre><code class="language-python">from pathlib import Path

notes = Path("notes.txt")

with open(notes, "w", encoding="utf-8") as f:
    f.write("سفارش KSH-101 ثبت شد\n")
    print("ارسال به کاشان", file=f)       # print هم می‌تواند در فایل بنویسد

with open(notes, encoding="utf-8") as f:
    for line_no, line in enumerate(f, start=1):
        print(line_no, line.rstrip("\n"))</code></pre>
<h3>with: بستن تضمینی</h3>
<p>فایل باز منبع سیستم‌عامل است و باید بسته شود. بلوک <code>with</code> تضمین می‌کند فایل در پایان بلوک بسته شود، <strong>حتی اگر وسط کار خطا رخ دهد</strong>. بدون with، اگر خطایی بین open و close پیش بیاید، فایل باز می‌ماند؛ در ویندوز فایل باز قفل است و نه می‌توانید حذفش کنید، نه اکسل می‌تواند آن را بنویسد.</p>
<h3>حالت‌های باز کردن</h3>
<table><thead><tr><th>حالت</th><th>معنی</th><th>اگر فایل وجود داشته باشد</th></tr></thead><tbody>
<tr><td><code>"r"</code></td><td>خواندن (پیش‌فرض)</td><td>باز می‌شود؛ اگر نباشد FileNotFoundError</td></tr>
<tr><td><code>"w"</code></td><td>نوشتن</td><td><strong>محتوا بدون هشدار پاک می‌شود</strong></td></tr>
<tr><td><code>"a"</code></td><td>افزودن به انتها</td><td>حفظ می‌شود؛ متن به انتها اضافه می‌شود</td></tr>
<tr><td><code>"x"</code></td><td>ساخت انحصاری</td><td>FileExistsError؛ جلوی بازنویسی تصادفی را می‌گیرد</td></tr>
<tr><td><code>"rb"</code> / <code>"wb"</code></td><td>باینری (تصویر، PDF)</td><td>بدون encoding؛ با bytes کار می‌کند</td></tr>
</tbody></table>
<h3>خواندن فایل بزرگ</h3>
<p><code>f.read()</code> کل فایل را یک‌جا در حافظه می‌آورد. برای فایل لاگ چند گیگابایتی، روی خود شیء فایل حلقه بزنید (مثل مثال بالا)؛ پایتون خط‌به‌خط می‌خواند و حافظه ثابت می‌ماند.</p>
<h3>وقتی کدگذاری فایل را نمی‌دانید</h3>
<p>فایلی که از یک نرم‌افزار حسابداری قدیمی یا Notepad ویندوز ۷ آمده، احتمالاً cp1256 است. اول با UTF-8 امتحان کنید و اگر خطا داد، با <code>encoding="cp1256"</code> بخوانید و خروجی را UTF-8 ذخیره کنید. پارامتر <code>errors="replace"</code> به‌جای خطا، کاراکترهای خراب را با � جایگزین می‌کند؛ برای «یک نگاه سریع» خوب است، برای داده‌ی واقعی نه.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>اجرای پایتون با <code>py -X utf8 script.py</code> یا تنظیم متغیر محیطی <code>PYTHONUTF8=1</code> پیش‌فرض همه‌ی open ها را UTF-8 می‌کند؛ طبق PEP 686 این رفتار در نسخه‌های آینده‌ی پایتون پیش‌فرض می‌شود.</li>
<li><code>py -X warn_default_encoding script.py</code> هر open بدون encoding را با هشدار EncodingWarning به شما نشان می‌دهد؛ روش سریع پیدا کردن همه‌ی جاهای خطرناک.</li>
<li>پایتون در حالت متنی <code>\r\n</code> ویندوزی را هنگام خواندن به <code>\n</code> تبدیل می‌کند و هنگام نوشتن در ویندوز برعکس؛ اگر فایل برای لینوکس است، <code>newline="\n"</code> بدهید.</li>
<li><code>f.write</code> خط جدید اضافه نمی‌کند؛ <code>print(..., file=f)</code> اضافه می‌کند. <code>writelines</code> هم با وجود نامش خط جدید نمی‌گذارد.</li>
<li>بعد از <code>open(..., "w")</code> حتی اگر هیچ چیزی ننویسید، فایل قبلی خالی شده است؛ برای ذخیره‌ی امن، در فایل موقت بنویسید و بعد با <code>Path.replace</code> جایگزین کنید.</li>
</ul>""",
                },
                {
                    "title": "CSV و JSON: utf-8-sig برای اکسل فارسی و ensure_ascii=False",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>دو قالب داده‌ای که هر روز با آن‌ها سروکار دارید</h2>
<p><strong>CSV</strong> زبان مشترک اکسل، نرم‌افزارهای حسابداری و خروجی سامانه‌هاست. <strong>JSON</strong> زبان مشترک وب، API ها و فایل‌های تنظیمات. پایتون برای هر دو ماژول استاندارد دارد و هر دو یک دام فارسی مهم دارند.</p>
<h3>نوشتن CSV که اکسل فارسی را درست نشان دهد</h3>
<p>اگر یک CSV با UTF-8 معمولی بسازید و در اکسل ویندوز دوبار کلیک کنید، به‌جای «مریم کاشانی» حروف درهم (Ø¯Ù…...) می‌بینید. دلیل: اکسل بدون نشانه‌ی خاص، فایل را با کدگذاری پیش‌فرض ویندوز می‌خواند. آن نشانه، <strong>BOM</strong> است؛ سه بایت در ابتدای فایل که کدگذاری <code>utf-8-sig</code> خودکار می‌گذارد:</p>
<pre><code class="language-python">import csv
from pathlib import Path

rows = [
    {"code": "KSH-101", "customer": "مریم کاشانی", "area": 6, "price": 57_000_000},
    {"code": "TBZ-220", "customer": "رضا احمدی", "area": 12, "price": 98_000_000},
]

path = Path("orders.csv")
with open(path, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["code", "customer", "area", "price"])
    writer.writeheader()
    writer.writerows(rows)</code></pre>
<p>و <code>newline=""</code>: ماژول csv خودش پایان خط را مدیریت می‌کند؛ بدون این آرگومان، در ویندوز بین هر دو سطر یک سطر خالی ظاهر می‌شود.</p>
<h3>خواندن CSV</h3>
<pre><code class="language-python">with open("orders.csv", encoding="utf-8-sig", newline="") as f:
    for row in csv.DictReader(f):
        price = int(row["price"])          # همه‌چیز رشته است!
        print(row["customer"], f"{price // 10:,} تومان")</code></pre>
<p>خواندن با <code>utf-8-sig</code> هم امن است: اگر BOM باشد حذفش می‌کند و اگر نباشد، مثل utf-8 معمولی رفتار می‌کند. بدون آن، اولین کلید دیکشنری به‌جای <code>"code"</code> چیزی مثل <code>"\ufeffcode"</code> می‌شود و <code>row["code"]</code> خطای KeyError می‌دهد؛ باگی که ساعت‌ها وقت می‌گیرد.</p>
<h3>JSON</h3>
<pre><code class="language-python">import json

text = json.dumps(rows, ensure_ascii=False, indent=2)
Path("orders.json").write_text(text, encoding="utf-8")

loaded = json.loads(Path("orders.json").read_text(encoding="utf-8"))
print(loaded[0]["customer"])      # مریم کاشانی

with open("orders.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)   # مستقیم در فایل</code></pre>
<p>به‌طور پیش‌فرض json هر کاراکتر غیرانگلیسی را به شکل <code>\u0645\u0631...</code> می‌نویسد؛ فایل درست است ولی برای انسان خواندنی نیست و حجمش چند برابر می‌شود. <code>ensure_ascii=False</code> فارسی را همان‌طور که هست ذخیره می‌کند.</p>
<table><thead><tr><th>پایتون</th><th>JSON</th><th>نکته</th></tr></thead><tbody>
<tr><td>dict</td><td>object</td><td>کلیدها همیشه رشته می‌شوند</td></tr>
<tr><td>list، tuple</td><td>array</td><td>tuple پس از بارگذاری list می‌شود</td></tr>
<tr><td>None / True</td><td>null / true</td><td>—</td></tr>
<tr><td>Decimal، datetime، set</td><td>پشتیبانی نمی‌شود</td><td>TypeError؛ با <code>default=str</code> حل می‌شود</td></tr>
</tbody></table>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>کلید عددی بعد از رفت‌وبرگشت JSON رشته می‌شود: <code>{1: "a"}</code> پس از dumps و loads می‌شود <code>{'1': 'a'}</code> و <code>d[1]</code> دیگر کار نمی‌کند.</li>
<li>CSV با جداکننده‌ی نقطه‌ویرگول (رایج در خروجی اکسل با تنظیمات اروپایی) را با <code>csv.DictReader(f, delimiter=";")</code> بخوانید؛ <code>csv.Sniffer</code> هم می‌تواند جداکننده را حدس بزند.</li>
<li>در قالب CSV اکسل، کد سفارشی مثل <code>0087</code> صفرهای ابتدایی‌اش را از دست می‌دهد؛ این کار اکسل است، نه پایتون. فایل را با Data ← From Text/CSV باز کنید و نوع ستون را Text بگذارید.</li>
<li><code>json.dumps(data, ensure_ascii=False, sort_keys=True)</code> خروجی ثابت و قابل مقایسه در git تولید می‌کند.</li>
<li>برای فایل‌های واقعی xlsx (نه CSV) کتابخانه‌ی <code>openpyxl</code> را نصب کنید؛ CSV فقط متن است و فرمول، رنگ و چند شیت ندارد.</li>
</ul>""",
                },
                {
                    "title": "try/except/else/finally و سلسله‌مراتب استثناها",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>خطا بخشی از برنامه است، نه پایانش</h2>
<p>کاربر به‌جای عدد «دوازده» تایپ می‌کند، فایل وجود ندارد، اینترنت قطع است. در پایتون این رویدادها <strong>استثنا</strong> (exception) ایجاد می‌کنند؛ اگر کسی آن را نگیرد، برنامه با یک <strong>traceback</strong> متوقف می‌شود. traceback را از <em>پایین</em> بخوانید: خط آخر نوع و پیام خطاست و خطوط بالاتر مسیر فراخوانی تا محل خطا.</p>
<h3>ساختار کامل</h3>
<pre><code class="language-python">import json
from pathlib import Path

def load_orders(path: Path) -&gt; list:
    try:
        text = path.read_text(encoding="utf-8")
        orders = json.loads(text)
    except FileNotFoundError:
        print("فایل سفارش‌ها هنوز ساخته نشده؛ از لیست خالی شروع می‌کنیم.")
        return []
    except json.JSONDecodeError as e:
        print(f"فایل خراب است (خط {e.lineno}): {e.msg}")
        raise
    else:
        print(f"{len(orders)} سفارش بارگذاری شد.")
        return orders
    finally:
        print("پایان تلاش برای خواندن.")</code></pre>
<table><thead><tr><th>بخش</th><th>کی اجرا می‌شود</th></tr></thead><tbody>
<tr><td><code>try</code></td><td>کدی که ممکن است خطا بدهد؛ تا حد ممکن کوتاه</td></tr>
<tr><td><code>except X</code></td><td>فقط اگر خطای نوع X (یا زیرکلاس‌هایش) رخ دهد</td></tr>
<tr><td><code>else</code></td><td>فقط اگر try <strong>بدون خطا</strong> تمام شود</td></tr>
<tr><td><code>finally</code></td><td><strong>همیشه</strong>؛ با خطا، بدون خطا، حتی بعد از return</td></tr>
</tbody></table>
<p>چرا else؟ چون کدی که فقط در صورت موفقیت اجرا می‌شود نباید داخل try باشد؛ وگرنه ممکن است خطای <em>آن</em> کد را هم به‌اشتباه بگیرید و پنهان کنید.</p>
<h3>سلسله‌مراتب استثناها</h3>
<pre><code class="language-text">BaseException
 ├── KeyboardInterrupt        # Ctrl+C
 ├── SystemExit               # sys.exit()
 └── Exception                # همه‌ی خطاهای «عادی»
      ├── ValueError          # نوع درست، مقدار غلط: int("دوازده")
      ├── TypeError           # نوع غلط: "۵" + 5
      ├── LookupError
      │    ├── KeyError       # کلید دیکشنری نیست
      │    └── IndexError     # اندیس لیست بیرون از بازه
      ├── OSError
      │    ├── FileNotFoundError
      │    └── PermissionError   # فایل در اکسل باز و قفل است
      ├── ZeroDivisionError
      └── ...</code></pre>
<p>گرفتن یک کلاس، همه‌ی زیرکلاس‌هایش را هم می‌گیرد: <code>except LookupError</code> هم KeyError و هم IndexError را. ترتیب except ها مهم است؛ خاص‌تر را بالاتر بگذارید.</p>
<h3>بدترین الگو</h3>
<pre><code class="language-python">try:
    process()
except:            # هرگز!
    pass</code></pre>
<p><code>except:</code> خالی حتی Ctrl+C را می‌گیرد و همراه <code>pass</code> هر باگی را بی‌صدا دفن می‌کند. فقط خطاهایی را بگیرید که <strong>می‌دانید چطور مدیریتشان کنید</strong>؛ بقیه باید بالا بروند و دیده شوند.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>چند نوع را با تاپل در یک except بگیرید: <code>except (ValueError, TypeError) as e:</code>.</li>
<li><code>raise</code> خالی داخل except همان خطا را با traceback اصلی دوباره پرتاب می‌کند؛ برای «ثبت کن و بگذار برود» عالی است.</li>
<li>اگر در finally از <code>return</code> استفاده کنید، هر خطای در حال انتشار بی‌صدا بلعیده می‌شود؛ پایتون ۳.۱۴ برای همین هشدار SyntaxWarning می‌دهد.</li>
<li>متغیر <code>e</code> در <code>except ... as e</code> بعد از بلوک except پاک می‌شود؛ اگر لازمش دارید، در متغیر دیگری ذخیره کنید.</li>
<li>سبک پایتونیک «EAFP» است: به‌جای بررسی <code>if path.exists()</code> و بعد باز کردن (که بینشان ممکن است فایل حذف شود)، مستقیم باز کنید و FileNotFoundError را بگیرید.</li>
</ul>""",
                },
                {
                    "title": "raise، استثنای سفارشی و logging به‌جای print",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>خطای خودتان را بسازید و ردپا بگذارید</h2>
<p>گرفتن خطا نیمی از ماجراست؛ نیم دیگر <strong>پرتاب</strong> خطای معنادار است. تابعی که ورودی نامعتبر می‌گیرد نباید مقدار عجیبی مثل ‎-1 یا None برگرداند که فراخواننده فراموش کند بررسی‌اش کند؛ باید با <code>raise</code> صریحاً اعلام کند.</p>
<pre><code class="language-python">def rug_area(width_cm: int, length_cm: int) -&gt; float:
    if width_cm &lt;= 0 or length_cm &lt;= 0:
        raise ValueError(f"ابعاد نامعتبر: {width_cm}×{length_cm}")
    return width_cm * length_cm / 10_000</code></pre>
<h3>استثنای سفارشی</h3>
<p>وقتی برنامه بزرگ می‌شود، خطاهای «کسب‌وکاری» را از خطاهای فنی جدا کنید. یک کلاس پایه برای پروژه بسازید و خطاهای خاص را از آن مشتق کنید (کلاس‌ها را در فصل بعد عمیق می‌بینیم؛ این‌جا فقط الگو را حفظ کنید):</p>
<pre><code class="language-python">class OrderError(Exception):
    &quot;&quot;&quot;پایه‌ی همه‌ی خطاهای مربوط به سفارش.&quot;&quot;&quot;

class OutOfStockError(OrderError):
    def __init__(self, code: str, requested: int, available: int):
        super().__init__(f"موجودی {code} کافی نیست: {requested} درخواست، {available} موجود")
        self.code = code
        self.requested = requested
        self.available = available

try:
    raise OutOfStockError("KSH-101", 5, 2)
except OrderError as e:          # همه‌ی خطاهای سفارش را یک‌جا بگیر
    print(e, "| کد:", e.code)</code></pre>
<p>حالا لایه‌ی رابط کاربری می‌تواند با یک <code>except OrderError</code> پیام مناسب نشان دهد و باگ‌های واقعی (TypeError و…) همچنان بالا بروند و دیده شوند.</p>
<h3>زنجیره‌ی علت: raise ... from</h3>
<pre><code class="language-python">def parse_qty(text: str) -&gt; int:
    try:
        return int(text)
    except ValueError as e:
        raise OrderError(f"تعداد نامعتبر: {text!r}") from e</code></pre>
<p>با <code>from e</code> خطای اصلی در traceback به‌عنوان «علت مستقیم» نمایش داده می‌شود و اطلاعات دیباگ گم نمی‌شود.</p>
<h3>logging: print حرفه‌ای</h3>
<p>print برای پیام به کاربر است، نه برای ردگیری رفتار برنامه. ماژول <strong>logging</strong> سطح اهمیت، زمان، نام ماژول و مقصد (فایل، کنسول) دارد و بدون حذف کد می‌توانید سطح جزئیات را کم و زیاد کنید:</p>
<pre><code class="language-python">import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s: %(message)s",
    filename="app.log",
    encoding="utf-8",          # بدون این، فارسی در ویندوز خراب می‌شود
)
log = logging.getLogger(__name__)

log.info("سفارش %s ثبت شد", "KSH-101")
log.warning("موجودی %s کمتر از ۳ تخته است", "TBZ-220")
try:
    1 / 0
except ZeroDivisionError:
    log.exception("خطا در محاسبه‌ی تخفیف")   # traceback کامل را هم ثبت می‌کند</code></pre>
<table><thead><tr><th>سطح</th><th>کاربرد</th></tr></thead><tbody>
<tr><td>DEBUG</td><td>جزئیات برای توسعه‌دهنده</td></tr>
<tr><td>INFO</td><td>رویدادهای عادی: «سفارش ثبت شد»</td></tr>
<tr><td>WARNING</td><td>غیرعادی ولی قابل ادامه (سطح پیش‌فرض)</td></tr>
<tr><td>ERROR / CRITICAL</td><td>شکست یک عمل / شکست کل برنامه</td></tr>
</tbody></table>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>در log پیام را با <code>%s</code> و آرگومان جدا بدهید، نه f-string؛ اگر آن سطح غیرفعال باشد، رشته اصلاً ساخته نمی‌شود و ابزارهای جمع‌آوری لاگ پیام‌های هم‌شکل را گروه‌بندی می‌کنند.</li>
<li><code>basicConfig</code> فقط بار اول اثر دارد؛ اگر کتابخانه‌ای قبل از شما logging را پیکربندی کرده باشد، تنظیمات شما نادیده گرفته می‌شود. در این حالت <code>force=True</code> بدهید.</li>
<li><code>e.add_note("سفارش مشتری: رضا")</code> (3.11+) به خطای موجود یادداشت اضافه می‌کند که در traceback چاپ می‌شود، بدون ساختن استثنای جدید.</li>
<li>نام کلاس استثنای سفارشی را با <code>Error</code> تمام کنید (قرارداد PEP 8) و مستقیماً از <code>Exception</code> ارث ببرید، نه از <code>BaseException</code>.</li>
<li><code>assert</code> برای اعتبارسنجی ورودی کاربر نیست: با اجرای <code>python -O</code> همه‌ی assert ها حذف می‌شوند. برای ورودی‌ها از raise استفاده کنید.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۷ ─────────────────────────────
        {
            "title": "فصل ۷: ماژول‌ها، کتابخانه‌ی استاندارد و شیءگرایی",
            "lessons": [
                {
                    "title": "import، __name__ == \"__main__\" و ساخت پکیج",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>از یک فایل بلند به پروژه‌ی مرتب</h2>
<p>هر فایل <code>.py</code> یک <strong>ماژول</strong> است و هر پوشه‌ای از ماژول‌ها (معمولاً با فایل <code>__init__.py</code>) یک <strong>پکیج</strong>. وقتی برنامه از چند صد خط گذشت، آن را بر اساس مسئولیت به ماژول‌ها تقسیم کنید: مدل داده، ذخیره‌سازی، گزارش، رابط کاربری.</p>
<h3>شکل‌های import</h3>
<pre><code class="language-python">import json                          # کل ماژول؛ استفاده: json.dumps
from pathlib import Path             # فقط یک نام
from collections import Counter, defaultdict
import datetime as dt                # نام مستعار
from decimal import Decimal as D     # کوتاه، اما با احتیاط</code></pre>
<p><code>from module import *</code> را ننویسید: معلوم نیست چه نام‌هایی وارد شده و ممکن است نام‌های شما را بی‌صدا بازنویسی کند. ترتیب استاندارد import ها در بالای فایل: اول کتابخانه‌ی استاندارد، بعد کتابخانه‌های نصب‌شده، بعد ماژول‌های خود پروژه؛ هر گروه با یک خط خالی جدا. Ruff این ترتیب را خودکار مرتب می‌کند.</p>
<h3>ساختار یک پکیج</h3>
<pre><code class="language-text">carpet_orders/            ← ریشه‌ی پروژه (از این‌جا اجرا می‌کنید)
├── .venv/
├── requirements.txt
└── orders/               ← پکیج
    ├── __init__.py
    ├── models.py
    ├── storage.py
    ├── reports.py
    └── cli.py</code></pre>
<pre><code class="language-python"># orders/storage.py
from .models import Order            # import نسبی: «از همین پکیج»

# orders/cli.py
from orders.storage import load_orders   # import مطلق؛ همیشه واضح‌تر</code></pre>
<h3>__name__ == "__main__"</h3>
<p>هر ماژول متغیری به نام <code>__name__</code> دارد. وقتی فایل <em>مستقیم اجرا</em> شود مقدارش <code>"__main__"</code> است و وقتی <em>import</em> شود، نام خود ماژول. این الگو اجازه می‌دهد یک فایل هم قابل import باشد و هم قابل اجرا:</p>
<pre><code class="language-python"># orders/reports.py
def monthly_total(orders):
    return sum(o["price"] for o in orders)

def main():
    sample = [{"price": 57_000_000}, {"price": 98_000_000}]
    print(f"{monthly_total(sample):,}")

if __name__ == "__main__":
    main()          # فقط هنگام اجرای مستقیم، نه هنگام import</code></pre>
<p>بدون این شرط، هر بار که فایل دیگری <code>from orders.reports import monthly_total</code> بنویسد، کد نمونه هم اجرا می‌شود. تست‌ها (فصل ۸) هم دقیقاً به همین دلیل به این الگو نیاز دارند.</p>
<h3>اجرای ماژول داخل پکیج</h3>
<pre><code class="language-powershell">cd D:\projects\carpet_orders
python -m orders.cli</code></pre>
<p>با <code>-m</code> پایتون پوشه‌ی جاری را در مسیر جست‌وجو قرار می‌دهد و import های پکیج درست کار می‌کنند. اگر به‌جایش <code>python orders\cli.py</code> بزنید، import نسبی خطای «attempted relative import with no known parent package» می‌دهد.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>هر ماژول فقط <strong>یک بار</strong> در هر اجرا بارگذاری می‌شود و در <code>sys.modules</code> کش می‌شود؛ import دوم کد را دوباره اجرا نمی‌کند.</li>
<li>پایتون اول پوشه‌ی اسکریپت اجراشده را جست‌وجو می‌کند؛ برای همین فایلی به نام <code>random.py</code> یا <code>csv.py</code> در پروژه، کتابخانه‌ی استاندارد را «سایه» می‌زند. <code>print(module.__file__)</code> نشان می‌دهد کدام فایل import شده است.</li>
<li>import چرخه‌ای (A، B را import کند و B، A را) خطای «partially initialized module» می‌دهد؛ معمولاً یعنی مسئولیت‌ها درست تقسیم نشده‌اند و کد مشترک باید به ماژول سوم برود.</li>
<li>پوشه‌ی <code>__pycache__</code> بایت‌کد کامپایل‌شده است؛ پاک کردنش بی‌خطر است و باید در <code>.gitignore</code> باشد.</li>
<li><code>python -m</code> برای ابزارها هم کار می‌کند: <code>python -m http.server 8000</code> پوشه‌ی جاری را در شبکه‌ی محلی به اشتراک می‌گذارد و <code>python -m json.tool file.json</code> فایل JSON را مرتب چاپ می‌کند.</li>
</ul>""",
                },
                {
                    "title": "datetime، منطقه‌ی زمانی تهران و تاریخ شمسی با jdatetime",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>زمان، سخت‌تر از آن است که به نظر می‌رسد</h2>
<p>ماژول استاندارد <code>datetime</code> چند نوع اصلی دارد: <code>date</code> (فقط تاریخ)، <code>datetime</code> (تاریخ و ساعت)، <code>timedelta</code> (فاصله‌ی زمانی) و <code>timezone</code>. از Python 3.9 هم ماژول <code>zoneinfo</code> منطقه‌های زمانی واقعی مثل <code>Asia/Tehran</code> را می‌شناسد.</p>
<pre><code class="language-python">from datetime import date, datetime, timedelta, UTC
from zoneinfo import ZoneInfo

TEHRAN = ZoneInfo("Asia/Tehran")

now = datetime.now(TEHRAN)                  # زمان «آگاه» (aware) با منطقه‌ی زمانی
print(now.isoformat())                      # مثلاً 2026-09-28T14:05:12+03:30
print(now.astimezone(UTC))                  # همان لحظه به وقت جهانی

due = date.today() + timedelta(days=45)     # تحویل ۴۵ روز بعد
days_left = (due - date.today()).days

stamp = datetime.strptime("2025-03-20 14:30", "%Y-%m-%d %H:%M")   # رشته به تاریخ
print(stamp.strftime("%d/%m/%Y"))                                 # تاریخ به رشته</code></pre>
<h3>naive در برابر aware</h3>
<p><code>datetime.now()</code> بدون آرگومان یک زمان <strong>naive</strong> می‌دهد: عدد ساعت دارد ولی نمی‌داند مال کدام منطقه است. روی لپ‌تاپ شما وقت تهران است و روی سرور خارجی وقت UTC؛ و اختلاف سه‌ونیم ساعته‌ای که گزارش‌ها را به روز اشتباه می‌برد. قاعده: <strong>در ذخیره‌سازی UTC، در نمایش تهران.</strong> مقایسه‌ی یک زمان naive با aware هم TypeError می‌دهد.</p>
<h3>تاریخ شمسی با jdatetime</h3>
<p>کتابخانه‌ی استاندارد تقویم شمسی ندارد. کتابخانه‌ی <strong>jdatetime</strong> رابطی تقریباً یکسان با datetime برای تقویم جلالی فراهم می‌کند:</p>
<pre><code class="language-powershell">python -m pip install jdatetime tzdata</code></pre>
<pre><code class="language-python">import jdatetime
from datetime import date, datetime

today = jdatetime.date.today()
print(today.strftime("%Y/%m/%d"))            # مثلاً 1405/07/06

j = jdatetime.date.fromgregorian(date=date(2025, 3, 21))
print(j)                                     # 1404-01-01
print(jdatetime.date(1404, 1, 1).togregorian())   # 2025-03-21

jnow = jdatetime.datetime.fromgregorian(datetime=datetime.now(TEHRAN))
print(jnow.strftime("%Y/%m/%d %H:%M"))

parsed = jdatetime.datetime.strptime("1403/05/20", "%Y/%m/%d")
print(parsed.togregorian().date())           # 2024-08-10

jdatetime.set_locale(jdatetime.FA_LOCALE)    # نام روز و ماه فارسی
print(jdatetime.date(1404, 1, 1).strftime("%A %d %B %Y"))</code></pre>
<p>راهبرد درست در یک برنامه‌ی واقعی: <strong>همه‌جا با datetime میلادی (ترجیحاً UTC) کار و ذخیره کنید و فقط در لحظه‌ی نمایش یا دریافت از کاربر، به شمسی تبدیل کنید.</strong> ذخیره‌ی رشته‌ی «۱۴۰۳/۰۵/۲۰» در دیتابیس، مرتب‌سازی، فیلتر بازه و محاسبه‌ی فاصله را سخت و پرخطا می‌کند.</p>
<table><thead><tr><th>کد قالب</th><th>معنی</th></tr></thead><tbody>
<tr><td><code>%Y</code> / <code>%m</code> / <code>%d</code></td><td>سال چهاررقمی / ماه / روز</td></tr>
<tr><td><code>%H:%M:%S</code></td><td>ساعت ۲۴ ساعته</td></tr>
<tr><td><code>%A</code> / <code>%B</code></td><td>نام روز هفته / نام ماه</td></tr>
<tr><td><code>%j</code></td><td>شماره‌ی روز در سال</td></tr>
</tbody></table>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>ویندوز پایگاه داده‌ی منطقه‌های زمانی IANA را ندارد؛ بدون نصب بسته‌ی <code>tzdata</code>، دستور <code>ZoneInfo("Asia/Tehran")</code> در ویندوز خطای ZoneInfoNotFoundError می‌دهد.</li>
<li>ایران از سال ۱۴۰۲ دیگر ساعت تابستانی ندارد؛ tzdata به‌روز این را می‌داند. اگر اختلاف تهران در سرور شما در تابستان ‎+04:30 است، tzdata سیستم قدیمی است.</li>
<li><code>datetime.utcnow()</code> در Python 3.12 منسوخ (deprecated) شده، چون زمان naive برمی‌گرداند؛ به‌جایش <code>datetime.now(UTC)</code> بنویسید.</li>
<li><code>jdatetime.date(1403, 12, 30)</code> معتبر است (۱۴۰۳ کبیسه بود) ولی <code>jdatetime.date(1404, 12, 30)</code> ValueError می‌دهد؛ اعتبارسنجی ورودی تاریخ شمسی را به خود کتابخانه بسپارید و <code>isleap()</code> را برای بررسی سال به کار ببرید.</li>
<li><code>datetime.fromisoformat</code> از 3.11 تقریباً هر رشته‌ی ISO 8601 (از جمله <code>+03:30</code> و <code>Z</code>) را می‌خواند و برای داده‌ی API ها بهترین انتخاب است.</li>
</ul>""",
                },
                {
                    "title": "random، secrets و itertools",
                    "kind": "text",
                    "minutes": 18,
                    "is_preview": False,
                    "body": r"""<h2>تصادف، امنیت و ترکیب‌های هوشمند</h2>
<p>سه ماژول کوچک از کتابخانه‌ی استاندارد که تقریباً در هر پروژه‌ای به کار می‌آیند، و یکی از آن‌ها اگر اشتباه انتخاب شود، حفره‌ی امنیتی می‌سازد.</p>
<h3>random: برای شبیه‌سازی و بازی</h3>
<pre><code class="language-python">import random

random.seed(1403)                              # نتیجه‌ی تکرارپذیر برای تست
print(random.randint(1, 6))                    # عدد صحیح، هر دو سر شامل
print(random.random())                         # float بین 0 و 1
print(random.choice(["لاکی", "سرمه‌ای", "کرم"]))
print(random.sample(range(1, 101), 5))         # ۵ عدد یکتا
print(random.choices(["کاشان", "تبریز"], weights=[3, 1], k=5))   # وزن‌دار، با تکرار

colors = ["لاکی", "سرمه‌ای", "کرم"]
random.shuffle(colors)                         # درجا؛ None برمی‌گرداند</code></pre>
<h3>secrets: برای هر چیز امنیتی</h3>
<p>مولد اعداد random «شبه‌تصادفی» و <strong>قابل پیش‌بینی</strong> است: با دیدن چند خروجی، می‌توان بقیه را حدس زد. برای رمز عبور، کد تأیید پیامکی، توکن بازیابی رمز یا لینک دعوت، <strong>فقط</strong> از <code>secrets</code> استفاده کنید:</p>
<pre><code class="language-python">import secrets
import string

otp = "".join(secrets.choice(string.digits) for _ in range(6))   # کد تأیید ۶ رقمی
token = secrets.token_urlsafe(32)          # توکن مناسب URL
api_key = secrets.token_hex(16)            # ۳۲ کاراکتر هگز

alphabet = string.ascii_letters + string.digits
password = "".join(secrets.choice(alphabet) for _ in range(12))
print(secrets.compare_digest(token, token))   # مقایسه‌ی امن در برابر حمله‌ی زمانی</code></pre>
<h3>itertools: جعبه‌ابزار پیمایش</h3>
<table><thead><tr><th>تابع</th><th>کار</th><th>مثال</th></tr></thead><tbody>
<tr><td><code>batched(it, n)</code></td><td>تکه‌های n تایی (3.12+)</td><td>ارسال پیامک‌ها در دسته‌های ۱۰۰تایی</td></tr>
<tr><td><code>pairwise(it)</code></td><td>جفت‌های پشت‌سرهم</td><td>تغییر قیمت روزبه‌روز</td></tr>
<tr><td><code>product(a, b)</code></td><td>ضرب دکارتی</td><td>همه‌ی ترکیب‌های رنگ و اندازه</td></tr>
<tr><td><code>combinations(it, r)</code></td><td>ترکیب‌های r تایی بدون ترتیب</td><td>جفت‌رنگ‌های ممکن</td></tr>
<tr><td><code>accumulate(it)</code></td><td>جمع تجمعی</td><td>فروش تجمعی ماه‌به‌ماه</td></tr>
<tr><td><code>chain(a, b)</code></td><td>پشت‌سرهم کردن</td><td>پیمایش دو لیست بدون ساختن لیست سوم</td></tr>
<tr><td><code>count(start)</code> / <code>islice</code></td><td>شمارنده‌ی بی‌پایان / برش</td><td>تولید شماره‌ی سفارش</td></tr>
</tbody></table>
<pre><code class="language-python">from itertools import batched, pairwise, product, accumulate, groupby

phones = [f"0912{n:07}" for n in range(250)]
for batch in batched(phones, 100):
    print(len(batch))                      # 100، 100، 50

prices = [9_500_000, 9_800_000, 9_650_000]
changes = [b - a for a, b in pairwise(prices)]    # [300000, -150000]

variants = list(product(["لاکی", "کرم"], ["۶ متری", "۹ متری"]))
monthly = list(accumulate([42, 17, 29]))           # [42, 59, 88]

rows = sorted([("کاشان", "K1"), ("تبریز", "T1"), ("کاشان", "K2")])
for city, group in groupby(rows, key=lambda r: r[0]):
    print(city, [code for _, code in group])</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>groupby</code> فقط عضوهای <em>پشت‌سرهم</em> با کلید یکسان را گروه می‌کند؛ بدون مرتب‌سازی قبلی، «کاشان» دو گروه جدا می‌شود. برای گروه‌بندی بدون مرتب‌سازی از defaultdict استفاده کنید.</li>
<li><code>random.shuffle(x)</code> چیزی برنمی‌گرداند؛ <code>x = random.shuffle(x)</code> لیست را به None تبدیل می‌کند. برای نسخه‌ی جدید: <code>random.sample(x, len(x))</code>.</li>
<li>گروه‌های groupby یک‌بار مصرف‌اند و با رفتن به گروه بعد از بین می‌روند؛ اگر لازمشان دارید، همان‌جا <code>list(group)</code> کنید.</li>
<li><code>random.seed</code> را در کد اصلی ثابت نگذارید؛ فقط در تست‌ها. seed ثابت در تولید یعنی هر بار همان «تصادف».</li>
<li><code>secrets.randbelow(n)</code> عدد صحیح امن بین 0 و n-1 می‌دهد؛ جایگزین امن <code>random.randint</code> در قرعه‌کشی‌های واقعی جشنواره‌ی فروش.</li>
</ul>""",
                },
                {
                    "title": "کلاس و شیء: __init__، self، متدها و property",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>داده و رفتار، کنار هم</h2>
<p>تا این‌جا سفارش را با dict نشان می‌دادیم و توابع جداگانه رویش کار می‌کردند. وقتی داده و رفتارِ مربوط به آن زیاد شود، <strong>کلاس</strong> آن‌ها را یک‌جا جمع می‌کند. کلاس نقشه یا قالب است و <strong>شیء</strong> (instance) نمونه‌ای ساخته‌شده از آن نقشه. «فرش» کلاس است؛ «فرش KSH-101 به ابعاد ۲×۳» یک شیء.</p>
<pre><code class="language-python">class Rug:
    def __init__(self, code: str, width_cm: int, length_cm: int, price_per_sqm: int):
        self.code = code
        self.width_cm = width_cm
        self.length_cm = length_cm
        self.price_per_sqm = price_per_sqm

    def area(self) -&gt; float:
        return self.width_cm * self.length_cm / 10_000

    def total_price(self) -&gt; int:
        return round(self.area() * self.price_per_sqm)

r = Rug("KSH-101", 200, 300, 9_500_000)
print(r.code, r.area(), f"{r.total_price():,}")   # KSH-101 6.0 57,000,000</code></pre>
<h3>__init__ و self</h3>
<p><code>__init__</code> «مقداردهی اولیه» است و هنگام ساختن شیء (<code>Rug(...)</code>) خودکار صدا زده می‌شود. <code>self</code> خودِ شیء در حال ساخت یا استفاده است؛ پایتون آن را خودکار به‌عنوان اولین آرگومان می‌فرستد. <code>r.total_price()</code> در واقع همان <code>Rug.total_price(r)</code> است. هر چیزی که با <code>self.x = ...</code> تعریف شود، <strong>ویژگی</strong> (attribute) آن شیء است و هر شیء نسخه‌ی خودش را دارد.</p>
<h3>property: ویژگی محاسباتی و اعتبارسنجی</h3>
<p>مساحت در واقع یک ویژگی است، نه یک «عمل». با <code>@property</code> می‌توانیم آن را بدون پرانتز بخوانیم و با setter جلوی مقدار نامعتبر را بگیریم:</p>
<pre><code class="language-python">class Rug:
    def __init__(self, code, width_cm, length_cm, price_per_sqm):
        self.code = code
        self.width_cm = width_cm
        self.length_cm = length_cm
        self.price_per_sqm = price_per_sqm      # از setter عبور می‌کند

    @property
    def area(self) -&gt; float:
        return self.width_cm * self.length_cm / 10_000

    @property
    def price_per_sqm(self) -&gt; int:
        return self._price_per_sqm

    @price_per_sqm.setter
    def price_per_sqm(self, value: int) -&gt; None:
        if value &lt;= 0:
            raise ValueError("قیمت باید مثبت باشد")
        self._price_per_sqm = value

r = Rug("KSH-101", 200, 300, 9_500_000)
print(r.area)                 # 6.0 — بدون پرانتز
r.price_per_sqm = -5          # ValueError</code></pre>
<p>زیبایی property این است که می‌توانید اول ویژگی ساده بنویسید و بعدها، بدون تغییر حتی یک خط از کد استفاده‌کننده، اعتبارسنجی اضافه کنید. به همین دلیل در پایتون برخلاف جاوا getter و setter دستی (<code>get_price()</code>) نمی‌نویسیم.</p>
<h3>ویژگی کلاس در برابر ویژگی شیء</h3>
<table><thead><tr><th></th><th>ویژگی شیء</th><th>ویژگی کلاس</th></tr></thead><tbody>
<tr><td>تعریف</td><td>داخل متد با <code>self.x = ...</code></td><td>مستقیم در بدنه‌ی کلاس</td></tr>
<tr><td>اشتراک</td><td>هر شیء جدا</td><td>بین همه‌ی شیءها مشترک</td></tr>
<tr><td>کاربرد</td><td>کد، ابعاد، قیمت</td><td>ثابت‌ها: <code>VAT = 0.10</code></td></tr>
</tbody></table>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>ویژگی کلاس <em>تغییرپذیر</em> (مثل <code>items = []</code> در بدنه‌ی کلاس) بین همه‌ی شیءها مشترک است؛ افزودن به سبد یک مشتری، در سبد همه ظاهر می‌شود. لیست را در <code>__init__</code> بسازید.</li>
<li>زیرخط ابتدای نام (<code>_price_per_sqm</code>) فقط قرارداد «دست نزنید» است و پایتون جلوی دسترسی را نمی‌گیرد؛ پایتون «private» واقعی ندارد.</li>
<li>property را بدون setter تعریف کنید تا فقط‌خواندنی شود: <code>r.area = 5</code> خطای AttributeError می‌دهد.</li>
<li><code>vars(r)</code> دیکشنری ویژگی‌های شیء را نشان می‌دهد؛ برای دیباگ سریع عالی است.</li>
<li>متدی که به self نیاز ندارد ولی منطقاً مال کلاس است را با <code>@staticmethod</code> و سازنده‌ی جایگزین (مثل <code>Rug.from_dict(d)</code>) را با <code>@classmethod</code> بنویسید.</li>
</ul>""",
                },
                {
                    "title": "وراثت، dunder methods (__str__، __repr__، __eq__) و dataclass",
                    "kind": "text",
                    "minutes": 26,
                    "is_preview": False,
                    "body": r"""<h2>کلاس‌هایی که با پایتون هماهنگ‌اند</h2>
<h3>وراثت</h3>
<p>وراثت یعنی کلاس جدید، همه‌چیز کلاس والد را به ارث ببرد و فقط تفاوت‌ها را تعریف کند. فرش ابریشمی همان فرش است، با یک ویژگی اضافه و قیمت‌گذاری متفاوت:</p>
<pre><code class="language-python">class SilkRug(Rug):
    def __init__(self, code, width_cm, length_cm, price_per_sqm, raj: int):
        super().__init__(code, width_cm, length_cm, price_per_sqm)   # کار والد را انجام بده
        self.raj = raj

    def total_price(self) -&gt; int:
        base = super().total_price()
        return round(base * 1.4) if self.raj &gt;= 60 else base

s = SilkRug("KSH-777", 150, 225, 20_000_000, raj=70)
print(isinstance(s, Rug))       # True — فرش ابریشمی، فرش هم هست</code></pre>
<p>وراثت را فقط برای رابطه‌ی واقعی «... یک نوع ... است» به کار ببرید. برای «... یک ... دارد» (سفارش <em>یک</em> مشتری دارد) از <strong>ترکیب</strong> استفاده کنید: شیء مشتری را به‌عنوان ویژگی در سفارش بگذارید. سلسله‌مراتب عمیق وراثت، کد را شکننده می‌کند.</p>
<h3>متدهای dunder</h3>
<p>متدهایی که با دو زیرخط شروع و تمام می‌شوند (double underscore، «dunder») به کلاس شما اجازه می‌دهند با عملگرها و توابع داخلی پایتون کار کند:</p>
<pre><code class="language-python">class Rug:
    # ... __init__ و بقیه مثل درس قبل
    def __repr__(self) -&gt; str:          # برای برنامه‌نویس: دیباگ، لاگ، REPL
        return f"Rug({self.code!r}, {self.width_cm}, {self.length_cm})"

    def __str__(self) -&gt; str:           # برای کاربر: print و f-string
        return f"فرش {self.code} — {self.area:g} متر مربع"

    def __eq__(self, other) -&gt; bool:    # عملگر ==
        if not isinstance(other, Rug):
            return NotImplemented
        return self.code == other.code</code></pre>
<table><thead><tr><th>متد</th><th>با چه چیزی فعال می‌شود</th></tr></thead><tbody>
<tr><td><code>__str__</code></td><td><code>print(r)</code>، <code>str(r)</code>، f-string</td></tr>
<tr><td><code>__repr__</code></td><td>REPL، نمایش داخل لیست، <code>repr(r)</code>، <code>{r!r}</code></td></tr>
<tr><td><code>__eq__</code></td><td><code>==</code> و <code>in</code></td></tr>
<tr><td><code>__lt__</code></td><td><code>&lt;</code> و در نتیجه <code>sorted</code></td></tr>
<tr><td><code>__len__</code></td><td><code>len(obj)</code> و truthiness</td></tr>
</tbody></table>
<p>اگر فقط یکی را تعریف می‌کنید، <code>__repr__</code> باشد؛ print در نبود <code>__str__</code> از آن استفاده می‌کند.</p>
<h3>dataclass: کلاس داده بدون کد تکراری</h3>
<p>نوشتن <code>__init__</code>، <code>__repr__</code> و <code>__eq__</code> برای هر کلاس داده خسته‌کننده است. دکوراتور <code>@dataclass</code> همه را از روی فیلدهای annotate‌شده خودکار می‌سازد:</p>
<pre><code class="language-python">from dataclasses import dataclass, field, asdict

@dataclass
class Order:
    code: str
    customer: str
    area: float
    price: int
    tags: list[str] = field(default_factory=list)   # نه tags: list = []
    status: str = "new"

    def __post_init__(self):
        if self.price &lt;= 0:
            raise ValueError("قیمت نامعتبر")

o = Order("KSH-101", "مریم کاشانی", 6, 57_000_000)
print(o)             # Order(code='KSH-101', customer='مریم کاشانی', ..., status='new')
print(asdict(o))     # dict آماده برای json.dumps
print(o == Order("KSH-101", "مریم کاشانی", 6, 57_000_000))   # True

@dataclass(frozen=True, order=True)
class Size:
    width: int
    length: int      # تغییرناپذیر، قابل مرتب‌سازی و قابل استفاده به‌عنوان کلید dict</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>تعریف <code>__eq__</code> بدون <code>__hash__</code>، شیء را unhashable می‌کند: دیگر نمی‌توانید آن را در set یا به‌عنوان کلید dict بگذارید. <code>frozen=True</code> در dataclass این مشکل را حل می‌کند.</li>
<li>برگرداندن <code>NotImplemented</code> (نه False) در <code>__eq__</code> به پایتون اجازه می‌دهد مقایسه را از طرف دیگر امتحان کند؛ خود NotImplemented یک مقدار ویژه است، نه استثنا.</li>
<li><code>field(default_factory=list)</code> همان راه‌حل دام «پیش‌فرض mutable» در فصل ۵ است؛ dataclass اصلاً اجازه‌ی <code>tags: list = []</code> را نمی‌دهد و ValueError می‌دهد.</li>
<li><code>Order(**row)</code> یک dict خوانده‌شده از JSON یا CSV را مستقیم به dataclass تبدیل می‌کند، به شرط این‌که کلیدها با نام فیلدها یکی باشند.</li>
<li><code>@dataclass(slots=True)</code> (3.10+) مصرف حافظه‌ی هر شیء را کم می‌کند و غلط تایپی در نام ویژگی (<code>o.custmer = ...</code>) را به خطا تبدیل می‌کند.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۸ ─────────────────────────────
        {
            "title": "فصل ۸: پروژه و حرفه‌ای شدن — پروژه‌ی پایانی، API، تست، دیباگ و کلینیک خطا",
            "lessons": [
                {
                    "title": "پروژه‌ی پایانی (۱): طراحی «مدیریت سفارش فرش»، مدل داده و ذخیره‌ی JSON",
                    "kind": "text",
                    "minutes": 26,
                    "is_preview": False,
                    "body": r"""<h2>از تمرین‌های پراکنده تا یک برنامه‌ی واقعی</h2>
<p>در این دو درس همه‌ی فصل‌ها را کنار هم می‌گذاریم و برنامه‌ی خط فرمانی برای یک کارگاه فرش در کاشان می‌سازیم: ثبت سفارش، تغییر وضعیت (در صف، روی دار، آماده، تحویل‌شده)، ذخیره در JSON و گزارش ماهانه‌ی شمسی. مهم‌تر از کد، <strong>تصمیم‌های طراحی</strong> است.</p>
<h3>ساختار پروژه</h3>
<pre><code class="language-text">carpet-orders/
├── .venv/
├── requirements.txt      # jdatetime، pytest، requests
├── store.py              # مدل داده و ذخیره‌سازی — بدون print و input
├── cli.py                # رابط خط فرمان — فقط ورودی و خروجی
└── tests/
    └── test_store.py</code></pre>
<p>قاعده‌ی طلایی: <strong>منطق را از ورودی و خروجی جدا کنید.</strong> <code>store.py</code> هیچ <code>print</code> یا <code>input</code> ندارد؛ پس تست‌پذیر است و روزی بدون تغییر زیر یک سایت جنگو هم کار می‌کند.</p>
<h3>store.py: مدل و ذخیره‌سازی</h3>
<pre><code class="language-python"># store.py — مدل داده و ذخیره‌سازی سفارش‌های فرش (بدون print و input)
import json
import os
from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from pathlib import Path

DATA_FILE = Path(__file__).with_name("orders.json")
STATUSES = ("queued", "weaving", "ready", "delivered")


def now_utc() -&gt; str:
    return datetime.now(UTC).isoformat(timespec="seconds")


@dataclass
class Order:
    code: str
    customer: str
    design: str          # افشان، ماهی، لچک‌ترنج ...
    size: str            # مثل "3x4"
    price: int           # تومان — پول را float نمی‌گذاریم
    status: str = "queued"
    created: str = field(default_factory=now_utc)

    def __post_init__(self):
        if self.price &lt;= 0:
            raise ValueError(f"قیمت نامعتبر: {self.price}")
        if self.status not in STATUSES:
            raise ValueError(f"وضعیت نامعتبر: {self.status}")


def load_orders(path: Path = DATA_FILE) -&gt; list[Order]:
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8").strip()
    if not text:                       # فایل خالی، نه JSON خراب
        return []
    return [Order(**row) for row in json.loads(text)]


def save_orders(orders: list[Order], path: Path = DATA_FILE) -&gt; None:
    tmp = path.with_suffix(".tmp")
    data = [asdict(o) for o in orders]
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    os.replace(tmp, path)              # جایگزینی اتمیک


def next_code(orders: list[Order], prefix: str = "KSH") -&gt; str:
    numbers = [int(o.code.split("-")[1]) for o in orders]
    return f"{prefix}-{max(numbers, default=100) + 1}"


def toman(text: str) -&gt; int:
    # '۵۷٬۰۰۰٬۰۰۰' یا '57,000,000' را به 57000000 تبدیل می‌کند
    table = str.maketrans("۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩", "01234567890123456789", ",٬ ")
    return int(text.translate(table))</code></pre>
<h3>چرا این‌طور نوشتیم؟</h3>
<ul>
<li><strong>کد سفارش</strong> رشته است: «KSH-107» پیشوند شعبه دارد و <code>max(..., default=100)</code> حالت فایل خالی را بدون if پوشش می‌دهد.</li>
<li><strong>قیمت</strong> int و به تومان است (فصل ۲). <code>toman</code> ارقام فارسی و عربی و جداکننده‌ی هزارگان را می‌پذیرد.</li>
<li><strong>زمان ثبت</strong> به‌صورت ISO و UTC ذخیره می‌شود و فقط هنگام نمایش شمسی می‌شود؛ قاعده‌ی فصل ۷.</li>
<li><strong>ذخیره‌ی اتمیک</strong>: اول در فایل موقت می‌نویسیم و بعد با <code>os.replace</code> جایگزین می‌کنیم. اگر وسط نوشتن برق برود، فایل اصلی سالم می‌ماند، نه نیمه‌نوشته.</li>
</ul>
<h3>امتحان سریع</h3>
<pre><code class="language-python">from pathlib import Path
from store import Order, load_orders, save_orders, next_code

path = Path("demo.json")
orders = load_orders(path)                       # فایل وجود ندارد: []
orders.append(Order(next_code(orders), "رضا نراقی", "افشان", "3x4", 57_000_000))
orders.append(Order(next_code(orders), "زهرا قمصری", "ماهی", "2x3", 31_500_000))
save_orders(orders, path)
print([o.code for o in load_orders(path)])       # ['KSH-101', 'KSH-102']</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>در ویندوز <code>os.rename</code> اگر فایل مقصد وجود داشته باشد FileExistsError می‌دهد، ولی <code>os.replace</code> روی هر دو سیستم‌عامل جایگزین می‌کند و اتمیک است؛ برای الگوی «فایل موقت، بعد جایگزینی» همیشه replace.</li>
<li><code>Path(__file__).with_name(...)</code> فایل داده را کنار اسکریپت نگه می‌دارد. اگر فقط <code>Path("orders.json")</code> بنویسید و برنامه را از پوشه‌ی دیگری اجرا کنید، فایل خالی تازه‌ای ساخته می‌شود و خیال می‌کنید سفارش‌ها پاک شده‌اند.</li>
<li><code>Order(**row)</code> با کلید اضافه در JSON خطای TypeError (unexpected keyword argument) می‌دهد. وقتی فیلدی را حذف می‌کنید، فایل‌های قدیمی را با <code>{k: v for k, v in row.items() if k in Order.__dataclass_fields__}</code> بخوانید.</li>
<li><code>json.loads("")</code> لیست خالی نمی‌دهد، JSONDecodeError می‌دهد؛ برای همین فایل صفربایتی (مثلاً خالی‌شده با Notepad) را جدا بررسی کردیم.</li>
<li>JSON برای چند هزار سفارش و یک کاربر کافی است؛ وقتی دو نفر هم‌زمان می‌نویسند، آخرین ذخیره کار دیگری را پاک می‌کند. آن روز وقت مهاجرت به <code>sqlite3</code> کتابخانه‌ی استاندارد یا جنگو است.</li>
</ul>""",
                },
                {
                    "title": "پروژه‌ی پایانی (۲): رابط خط فرمان با argparse، گزارش با Counter و تاریخ شمسی",
                    "kind": "text",
                    "minutes": 26,
                    "is_preview": False,
                    "body": r"""<h2>یک برنامه، چند فرمان</h2>
<p>برنامه‌های خط فرمان حرفه‌ای (مثل git و pip) یک «فرمان اصلی» و چند «زیرفرمان» دارند. ماژول استاندارد <code>argparse</code> همین را با چند خط می‌سازد و راهنمای <code>--help</code>، بررسی نوع و پیام خطا را هم رایگان تحویل می‌دهد؛ دیگر لازم نیست با <code>input()</code> و منوهای عددی کلنجار بروید.</p>
<h3>cli.py</h3>
<pre><code class="language-python"># cli.py — رابط خط فرمان مدیریت سفارش فرش
import argparse
import sys
from collections import Counter
from datetime import datetime
from zoneinfo import ZoneInfo

import jdatetime

from store import STATUSES, Order, load_orders, next_code, save_orders, toman

TEHRAN = ZoneInfo("Asia/Tehran")


def to_jalali(iso: str, fmt: str = "%Y/%m/%d") -&gt; str:
    local = datetime.fromisoformat(iso).astimezone(TEHRAN)
    return jdatetime.datetime.fromgregorian(datetime=local).strftime(fmt)


def cmd_add(args) -&gt; int:
    orders = load_orders()
    order = Order(next_code(orders), args.customer, args.design, args.size, args.price)
    save_orders(orders + [order])
    print(f"سفارش {order.code} ثبت شد.")
    return 0


def cmd_list(args) -&gt; int:
    for o in load_orders():
        if args.status is None or o.status == args.status:
            print(f"{o.code}  {o.customer}  {o.design}  {o.price:,}  {to_jalali(o.created)}  {o.status}")
    return 0


def cmd_status(args) -&gt; int:
    orders = load_orders()
    for o in orders:
        if o.code == args.code.upper():
            o.status = args.status
            save_orders(orders)
            print(f"{o.code}: {o.status}")
            return 0
    print(f"سفارش {args.code} پیدا نشد.", file=sys.stderr)
    return 1


def cmd_report(args) -&gt; int:
    orders = load_orders()
    sales = Counter()
    for o in orders:
        sales[to_jalali(o.created, "%Y/%m")] += o.price
    print("بر اساس وضعیت:", dict(Counter(o.status for o in orders)))
    for design, count in Counter(o.design for o in orders).most_common(3):
        print(f"  طرح {design}: {count} سفارش")
    for month, total in sorted(sales.items()):
        print(f"  {month}: {total:,} تومان")
    return 0


def build_parser() -&gt; argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="orders", description="مدیریت سفارش فرش")
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("add", help="ثبت سفارش")
    p.add_argument("customer")
    p.add_argument("design")
    p.add_argument("size")
    p.add_argument("--price", type=toman, required=True)
    p.set_defaults(func=cmd_add)
    p = sub.add_parser("list", help="فهرست سفارش‌ها")
    p.add_argument("--status", choices=STATUSES)
    p.set_defaults(func=cmd_list)
    p = sub.add_parser("status", help="تغییر وضعیت")
    p.add_argument("code")
    p.add_argument("status", choices=STATUSES)
    p.set_defaults(func=cmd_status)
    sub.add_parser("report", help="گزارش").set_defaults(func=cmd_report)
    return parser


def main(argv: list[str] | None = None) -&gt; int:
    args = build_parser().parse_args(argv)
    try:
        return args.func(args)
    except ValueError as exc:
        print(f"خطا: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())</code></pre>
<h3>اجرا در PowerShell</h3>
<pre><code class="language-powershell">python cli.py add "رضا نراقی" افشان 3x4 --price ۵۷٬۰۰۰٬۰۰۰
python cli.py add "زهرا قمصری" ماهی 2x3 --price 31,500,000
python cli.py status ksh-101 weaving
python cli.py list --status weaving
python cli.py report
python cli.py add --help</code></pre>
<h3>سه ایده‌ی کلیدی</h3>
<ul>
<li><strong>set_defaults(func=...)</strong>: هر زیرفرمان تابع خودش را با خود می‌آورد؛ به‌جای زنجیره‌ی بلند if/elif فقط <code>args.func(args)</code> صدا زده می‌شود.</li>
<li><strong>Counter</strong> سه کار گزارش را انجام می‌دهد: شمارش وضعیت‌ها، پرسفارش‌ترین طرح‌ها با <code>most_common</code> و جمع فروش هر ماه شمسی با <code>+=</code> بدون مقداردهی اولیه.</li>
<li><strong>main(argv)</strong> لیست آرگومان می‌گیرد؛ پس در تست یا REPL می‌نویسید <code>main(["report"])</code> و دیگر به ترمینال نیازی نیست.</li>
</ul>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>هر تابعی که رشته بگیرد و ValueError بدهد، می‌تواند <code>type=</code> در argparse باشد؛ argparse خطا را به پیام «invalid toman value» تبدیل می‌کند و با کد خروج 2 بیرون می‌رود، بدون این‌که try بنویسید.</li>
<li><code>sys.exit(main())</code> کد خروج را به سیستم‌عامل می‌دهد؛ در PowerShell متغیر <code>$LASTEXITCODE</code> آن را نشان می‌دهد و در Task Scheduler یا اسکریپت‌های پشتیبان، شکست برنامه تشخیص‌پذیر می‌شود.</li>
<li>اگر خروجی را در PowerShell با <code>&gt;</code> به فایل بفرستید، پایتون در ویندوز برای stdout هدایت‌شده کدگذاری ANSI سیستم (cp1252 یا cp1256) را برمی‌دارد و ممکن است UnicodeEncodeError بگیرید؛ <code>$env:PYTHONUTF8 = "1"</code> را تنظیم کنید.</li>
<li>تراز ستونی با <code>:16</code> برای متن فارسی در ترمینال قابل اعتماد نیست، چون ترمینال حروف را متصل و راست‌به‌چپ نمایش می‌دهد؛ برای گزارش جدی CSV با utf-8-sig بسازید و در اکسل باز کنید.</li>
<li><code>Counter.total()</code> (از 3.10) جمع همه‌ی مقادیر را می‌دهد و دو Counter را می‌توان با <code>+</code> جمع کرد؛ مثلاً فروش دو شعبه‌ی کاشان و آران.</li>
</ul>""",
                },
                {
                    "title": "کار با API و requests: timeout، مدیریت خطا، retry و پراکسی در شرایط تحریم",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>برنامه‌ای که با دنیای بیرون حرف می‌زند</h2>
<p>فرض کنید کارگاه می‌خواهد قیمت سفارش‌های صادراتی را با نرخ روز دلار نشان دهد، یا وضعیت ارسال را از API یک شرکت پست بگیرد. کتابخانه‌ی <strong>requests</strong> استاندارد عملی پایتون برای HTTP است (<code>python -m pip install requests</code>). فرستادن درخواست یک خط است؛ کار حرفه‌ای، <strong>رفتار درست وقتی چیزی خراب می‌شود</strong> است، و در ایران چیزها زیاد خراب می‌شوند: قطعی، کندی، فیلتر و 403 تحریم.</p>
<h3>کد کامل با همه‌ی محافظ‌ها</h3>
<pre><code class="language-python">import logging

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

log = logging.getLogger(__name__)
API_URL = "https://api.example.ir/v1/rates"     # آدرس فرضی


def make_session() -&gt; requests.Session:
    session = requests.Session()
    retry = Retry(
        total=3,
        backoff_factor=0.5,                      # مکث بین تلاش‌ها، هر بار دو برابر
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=("GET",),
    )
    session.mount("https://", HTTPAdapter(max_retries=retry))
    session.headers["User-Agent"] = "carpet-orders/1.0"
    return session


def usd_rate(session: requests.Session) -&gt; int | None:
    try:
        resp = session.get(API_URL, params={"symbol": "USD"}, timeout=(3.05, 10))
        resp.raise_for_status()
        return int(resp.json()["price"])
    except requests.Timeout:
        log.warning("سرور در زمان مقرر پاسخ نداد")
    except requests.ConnectionError:
        log.warning("اتصال برقرار نشد: اینترنت، DNS یا فیلتر")
    except requests.exceptions.RetryError:
        log.warning("سرور بعد از چند تلاش هم خطای 5xx یا 429 داد")
    except requests.HTTPError as exc:
        code = exc.response.status_code
        reason = "احتمالاً تحریم یا کلید API" if code == 403 else "خطای HTTP"
        log.warning("%s (%s)", reason, code)
    except (ValueError, KeyError):
        log.warning("پاسخ JSON معتبر نبود یا فیلد price نداشت")
    return None


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    rate = usd_rate(make_session())
    print("نرخ دلار:", rate if rate is not None else "فعلاً در دسترس نیست")</code></pre>
<h3>استثناها چه می‌گویند؟</h3>
<table><thead><tr><th>استثنا</th><th>معنی</th><th>واکنش منطقی</th></tr></thead><tbody>
<tr><td><code>Timeout</code></td><td>اتصال یا پاسخ در زمان تعیین‌شده نرسید</td><td>تلاش دوباره یا مقدار ذخیره‌شده‌ی قبلی</td></tr>
<tr><td><code>ConnectionError</code></td><td>اصلاً وصل نشد (DNS، قطعی، فیلتر)</td><td>پیام روشن به کاربر، بررسی پراکسی</td></tr>
<tr><td><code>HTTPError</code> با 403</td><td>سرور شما را نمی‌پذیرد؛ برای سرویس‌های خارجی معمولاً تحریم IP ایران</td><td>تلاش دوباره فایده ندارد؛ پراکسی یا سرویس جایگزین</td></tr>
<tr><td><code>HTTPError</code> با 401</td><td>کلید یا توکن نامعتبر</td><td>بررسی تنظیمات، نه retry</td></tr>
<tr><td><code>ValueError</code> از <code>json()</code></td><td>پاسخ JSON نیست، مثلاً صفحه‌ی HTML فیلترینگ</td><td>لاگ کردن <code>resp.text[:200]</code></td></tr>
</tbody></table>
<h3>پراکسی و سایت‌های داخلی</h3>
<p>requests پراکسی را از متغیرهای محیطی می‌خواند، یا می‌توانید صریحاً بدهید. برای سرویس خارجی پراکسی لازم است و برای سایت داخلی نه:</p>
<pre><code class="language-powershell">$env:HTTPS_PROXY = "http://127.0.0.1:10809"
$env:NO_PROXY = "localhost,127.0.0.1,.ir"
python rates.py</code></pre>
<pre><code class="language-python">proxies = {"https": "http://127.0.0.1:10809"}
resp = requests.get("https://api.example.com/status", proxies=proxies, timeout=10)</code></pre>
<p>برای ارسال داده هم <code>session.post(url, json={"code": "KSH-101"}, timeout=10)</code> بنویسید؛ آرگومان <code>json=</code> هم بدنه را می‌سازد و هم هدر Content-Type را درست تنظیم می‌کند.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>requests هیچ timeout پیش‌فرضی ندارد؛ درخواست بدون timeout می‌تواند برای همیشه گیر کند و برنامه‌ی زمان‌بندی‌شده را بی‌صدا متوقف کند.</li>
<li>timeout «زمان کل» نیست: عدد دوم سقف فاصله‌ی بین دو تکه‌ی داده است. پاسخی که آهسته ولی پیوسته برسد، می‌تواند دقیقه‌ها طول بکشد.</li>
<li>وقتی تلاش‌های Retry روی کدهای 5xx تمام شود، استثنا <code>RetryError</code> است نه <code>HTTPError</code>؛ اگر فقط HTTPError را بگیرید، برنامه با traceback می‌افتد.</li>
<li>سایتی که در هدر charset اعلام نکند، با کدگذاری ISO-8859-1 خوانده می‌شود و <code>resp.text</code> فارسی را به‌هم‌ریخته نشان می‌دهد؛ قبل از خواندن متن <code>resp.encoding = "utf-8"</code> بگذارید.</li>
<li>اگر پراکسی در متغیرهای محیطی تنظیم باشد، درخواست به سایت‌های داخلی هم از آن رد می‌شود و کند یا مسدود می‌شود؛ <code>NO_PROXY</code> با پسوند <code>.ir</code> یا <code>session.trust_env = False</code> مشکل را حل می‌کند.</li>
</ul>""",
                },
                {
                    "title": "تست خودکار با pytest: assert ساده، fixture، tmp_path و parametrize",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>چرا تست بنویسیم وقتی برنامه «کار می‌کند»؟</h2>
<p>امروز برنامه کار می‌کند. سه ماه بعد که فیلد تازه‌ای به Order اضافه می‌کنید، از کجا می‌دانید <code>next_code</code> یا تبدیل ارقام فارسی خراب نشده؟ تست خودکار یعنی کدی که کد شما را امتحان می‌کند و در یک ثانیه می‌گوید چیزی شکسته یا نه. <strong>pytest</strong> محبوب‌ترین ابزار تست پایتون است چون تست در آن فقط یک تابع با <code>assert</code> ساده است.</p>
<pre><code class="language-powershell">python -m pip install pytest
python -m pytest -q</code></pre>
<h3>اولین فایل تست</h3>
<p>pytest فایل‌هایی را که نامشان با <code>test_</code> شروع می‌شود و تابع‌های <code>test_*</code> داخل آن‌ها را خودکار پیدا و اجرا می‌کند:</p>
<pre><code class="language-python"># tests/test_store.py
import pytest

from store import Order, load_orders, next_code, save_orders, toman


def make(code="KSH-101", **changes):
    data = dict(code=code, customer="مریم کاشانی", design="افشان", size="3x4", price=57_000_000)
    data.update(changes)
    return Order(**data)


def test_next_code_on_empty_list():
    assert next_code([]) == "KSH-101"


def test_next_code_uses_max_not_last():
    assert next_code([make("KSH-105"), make("KSH-102")]) == "KSH-106"


def test_zero_price_is_rejected():
    with pytest.raises(ValueError, match="قیمت"):
        make(price=0)


def test_missing_file_gives_empty_list(tmp_path):
    assert load_orders(tmp_path / "nothing.json") == []


def test_save_and_load_round_trip(tmp_path):
    path = tmp_path / "orders.json"
    save_orders([make(), make("KSH-102", status="ready")], path)
    loaded = load_orders(path)
    assert [o.code for o in loaded] == ["KSH-101", "KSH-102"]
    assert loaded[1].status == "ready"
    assert "مریم" in path.read_text(encoding="utf-8")   # فارسی، نه م


@pytest.mark.parametrize("text, expected", [
    ("57000000", 57_000_000),
    ("۵۷٬۰۰۰٬۰۰۰", 57_000_000),
    ("31,500,000", 31_500_000),
])
def test_toman_accepts_persian_and_commas(text, expected):
    assert toman(text) == expected</code></pre>
<h3>سه ابزار اصلی</h3>
<ul>
<li><strong>assert ساده</strong>: pytest عبارت را تحلیل می‌کند و در شکست، مقدار دو طرف را نشان می‌دهد؛ دیگر لازم نیست <code>assertEqual</code> حفظ کنید.</li>
<li><strong>fixture</strong>: آرگومانی مثل <code>tmp_path</code> را pytest خودش می‌سازد و تحویل می‌دهد؛ این یکی پوشه‌ی موقت تازه‌ای برای هر تست است، پس تست‌ها هرگز به <code>orders.json</code> واقعی دست نمی‌زنند. fixture خودتان را با <code>@pytest.fixture</code> می‌سازید.</li>
<li><strong>parametrize</strong>: یک تست، چند ورودی؛ هر ردیف یک تست جدا در گزارش است.</li>
</ul>
<h3>پیکربندی و اجرای هدفمند</h3>
<pre><code class="language-toml"># pyproject.toml
[tool.pytest.ini_options]
pythonpath = ["."]
testpaths = ["tests"]</code></pre>
<table><thead><tr><th>دستور</th><th>کار</th></tr></thead><tbody>
<tr><td><code>python -m pytest -q</code></td><td>اجرای همه، خروجی کوتاه</td></tr>
<tr><td><code>python -m pytest -k toman</code></td><td>فقط تست‌هایی که نامشان toman دارد</td></tr>
<tr><td><code>python -m pytest -x --lf</code></td><td>توقف در اولین شکست؛ فقط شکست‌خورده‌های دفعه‌ی قبل</td></tr>
<tr><td><code>python -m pytest -s</code></td><td>نمایش print ها (pytest آن‌ها را پنهان می‌کند)</td></tr>
</tbody></table>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>اگر <code>pytest</code> خالی ModuleNotFoundError: No module named 'store' داد ولی <code>python -m pytest</code> کار کرد، دلیلش این است که فقط حالت دوم پوشه‌ی جاری را به sys.path اضافه می‌کند؛ تنظیم <code>pythonpath</code> بالا هر دو را یکسان می‌کند.</li>
<li>آرگومان <code>match</code> در <code>pytest.raises</code> یک الگوی regex است و با <code>re.search</code> بررسی می‌شود؛ برای پیامی که پرانتز یا نقطه دارد از <code>re.escape</code> استفاده کنید.</li>
<li>تست‌ها باید مستقل باشند: اگر یک تست فقط وقتی پاس می‌شود که تست دیگری قبلش اجرا شده باشد، روزی که با <code>-k</code> تنها اجرایش کنید، بی‌دلیل می‌شکند.</li>
<li>fixture ای که به‌جای return از <code>yield</code> استفاده کند، کد بعد از yield را پس از پایان تست اجرا می‌کند؛ جای مناسب پاک‌سازی، حتی وقتی تست شکست خورده.</li>
<li><code>capsys</code> یک fixture آماده است که خروجی print را می‌گیرد: <code>main(["report"])</code> را صدا بزنید و <code>capsys.readouterr().out</code> را assert کنید؛ رابط خط فرمان هم تست‌پذیر است.</li>
</ul>""",
                },
                {
                    "title": "دیباگ حرفه‌ای: breakpoint()، فرمان‌های pdb و دیباگر VS Code",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>به‌جای حدس زدن، برنامه را وسط اجرا نگه دارید</h2>
<p>بیشتر تازه‌کارها با <code>print</code> دیباگ می‌کنند: چند خط چاپ اضافه، اجرا، حدس، پاک کردن و دوباره. دیباگر یعنی برنامه را در یک خط مشخص <strong>متوقف کنید</strong>، همه‌ی متغیرها را همان لحظه ببینید، قدم‌به‌قدم جلو بروید و حتی عبارت دلخواه اجرا کنید. این کد گزارش ماهانه را ببینید که عدد غلط می‌دهد:</p>
<pre><code class="language-python">orders = [
    {"created": "2025-04-02", "price": 57_000_000},
    {"created": "2025-04-19", "price": 31_500_000},
    {"created": "2025-05-03", "price": 12_000_000},
]


def monthly_total(orders):
    totals = {}
    for o in orders:
        month = o["created"][:7]
        breakpoint()                     # اجرا این‌جا می‌ایستد
        totals[month] = o["price"]       # باگ: جایگزین می‌کند، جمع نمی‌زند
    return totals


print(monthly_total(orders))   # جمع 2025-04 باید 88,500,000 باشد</code></pre>
<p>با اجرای فایل، پایتون در خط <code>breakpoint()</code> می‌ایستد و اعلان <code>(Pdb)</code> ظاهر می‌شود:</p>
<pre><code class="language-text">&gt; report.py(13)monthly_total()
-&gt; totals[month] = o["price"]       # باگ: جایگزین می‌کند، جمع نمی‌زند
(Pdb) p month, totals
('2025-04', {})
(Pdb) c
&gt; report.py(13)monthly_total()
-&gt; totals[month] = o["price"]       # باگ: جایگزین می‌کند، جمع نمی‌زند
(Pdb) p totals
{'2025-04': 57000000}
(Pdb) n
&gt; report.py(10)monthly_total()
-&gt; for o in orders:
(Pdb) p totals
{'2025-04': 31500000}          # همین‌جا باگ پیدا شد
(Pdb) q</code></pre>
<p>درمان: <code>totals[month] = totals.get(month, 0) + o["price"]</code>، یا همان Counter درس پروژه.</p>
<h3>فرمان‌های پرکاربرد pdb</h3>
<table><thead><tr><th>فرمان</th><th>کار</th></tr></thead><tbody>
<tr><td><code>n</code> (next)</td><td>اجرای خط فعلی و رفتن به خط بعد، بدون ورود به تابع‌ها</td></tr>
<tr><td><code>s</code> (step)</td><td>ورود به داخل تابعی که در خط فعلی صدا زده می‌شود</td></tr>
<tr><td><code>c</code> (continue)</td><td>ادامه تا breakpoint بعدی</td></tr>
<tr><td><code>p</code> / <code>pp</code></td><td>چاپ مقدار / چاپ مرتب dict و لیست‌های بزرگ</td></tr>
<tr><td><code>l</code> / <code>ll</code></td><td>نمایش کد اطراف / کل تابع فعلی</td></tr>
<tr><td><code>w</code>، <code>u</code>، <code>d</code></td><td>پشته‌ی فراخوانی؛ بالا و پایین رفتن بین تابع‌ها</td></tr>
<tr><td><code>b 13</code></td><td>گذاشتن breakpoint در خط ۱۳</td></tr>
<tr><td><code>q</code></td><td>خروج</td></tr>
</tbody></table>
<h3>دیباگر VS Code</h3>
<p>با افزونه‌ی Python، روی شماره‌ی خط کلیک کنید (یا <code>F9</code>) تا نقطه‌ی قرمز بنشیند و با <code>F5</code> اجرا کنید. پنل Variables همه‌ی متغیرها را نشان می‌دهد، Watch عبارت دلخواه را دنبال می‌کند و در Debug Console هر کد پایتونی را در همان لحظه اجرا می‌کنید. <code>F10</code> معادل n و <code>F11</code> معادل s است. برای برنامه‌ی خط فرمان، آرگومان‌ها را در <code>.vscode/launch.json</code> بدهید:</p>
<pre><code class="language-json">{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "orders report",
      "type": "debugpy",
      "request": "launch",
      "program": "${workspaceFolder}/cli.py",
      "args": ["report"],
      "console": "integratedTerminal",
      "justMyCode": true,
      "env": {"PYTHONUTF8": "1"}
    }
  ]
}</code></pre>
<p>با راست‌کلیک روی نقطه‌ی قرمز و Edit Breakpoint، شرط بگذارید (مثلاً <code>o["price"] &gt; 50_000_000</code>) تا فقط سفارش‌های مشکوک متوقف شوند؛ یا Logpoint بسازید که بدون توقف و بدون تغییر کد، پیامی مثل <code>{month}</code> چاپ کند.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>متغیر محیطی <code>PYTHONBREAKPOINT=0</code> همه‌ی <code>breakpoint()</code> ها را بی‌اثر می‌کند؛ ولی بهتر است اصلاً در کد نمانند. قاعده‌ی T100 در ruff، breakpoint جامانده را پیش از commit پیدا می‌کند.</li>
<li>اگر متغیری به نام <code>n</code>، <code>c</code> یا <code>l</code> دارید، تایپ نامش در pdb فرمان را اجرا می‌کند نه چاپ را؛ بنویسید <code>p n</code> یا <code>!n</code>.</li>
<li><code>python -m pdb -c continue cli.py report</code> برنامه را عادی اجرا می‌کند و فقط وقتی استثنا رخ دهد، دیباگر را در همان نقطه باز می‌کند (post-mortem). در REPL هم بعد از خطا <code>import pdb; pdb.pm()</code> همین کار را می‌کند.</li>
<li>فرمان <code>interact</code> در pdb یک REPL کامل با همه‌ی متغیرهای محلی باز می‌کند؛ برای امتحان چند خط درمان پیش از تغییر فایل عالی است.</li>
<li>اگر VS Code نقطه‌ی قرمز را خاکستری نشان می‌دهد و نمی‌ایستد، معمولاً مفسر انتخاب‌شده (Python: Select Interpreter) همان <code>.venv</code> پروژه نیست، یا فایل در کتابخانه‌ای است که <code>justMyCode</code> آن را رد می‌کند.</li>
</ul>""",
                },
                {
                    "title": "کلینیک خطاهای رایج و نقشه‌ی راه بعد از این دوره",
                    "kind": "text",
                    "minutes": 26,
                    "is_preview": False,
                    "body": r"""<h2>traceback را از پایین بخوانید</h2>
<p>پیام خطای پایتون ترسناک به نظر می‌رسد ولی دقیق‌ترین راهنمای شماست. <strong>آخرین خط</strong> نوع و پیام خطاست و خط‌های بالاتر مسیر رسیدن به آن. در traceback های بلند، اولین فریمی را پیدا کنید که در فایل‌های <em>خودتان</em> است؛ مشکل تقریباً همیشه همان‌جاست، نه در کتابخانه.</p>
<h3>شش بیمار همیشگی</h3>
<table><thead><tr><th>خطا</th><th>علت رایج</th><th>درمان</th></tr></thead><tbody>
<tr><td><code>IndentationError</code> / <code>TabError</code></td><td>قاطی شدن Tab و فاصله؛ کد کپی‌شده از تلگرام یا Word</td><td>در VS Code: Convert Indentation to Spaces؛ همیشه ۴ فاصله</td></tr>
<tr><td><code>UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc7</code></td><td>فایل قدیمی ویندوزی با کدگذاری cp1256</td><td><code>encoding="cp1256"</code>، سپس ذخیره‌ی دوباره با UTF-8</td></tr>
<tr><td><code>ModuleNotFoundError</code></td><td>venv فعال نیست، یا VS Code مفسر دیگری را اجرا می‌کند</td><td>بررسی <code>sys.executable</code> و نصب با <code>python -m pip</code></td></tr>
<tr><td><code>TypeError</code></td><td>جمع str و int، صدا زدن روی None، آرگومان جاافتاده</td><td>خواندن پیام کامل؛ <code>type(x)</code> در دیباگر</td></tr>
<tr><td>تغییر «خودبه‌خود» داده</td><td>دو نام برای یک لیست (فصل ۴)</td><td><code>copy()</code>، <code>deepcopy</code> یا ساختن لیست تازه</td></tr>
<tr><td><code>ReadTimeoutError</code> در pip</td><td>کندی یا قطعی PyPI از ایران</td><td>میرور ایرانی و <code>--default-timeout=120</code> (فصل ۱)</td></tr>
</tbody></table>
<h3>نمونه‌های کد</h3>
<pre><code class="language-python">import sys
from copy import deepcopy
from pathlib import Path

# ۱) کدام پایتون در حال اجراست؟ اولین قدم برای ModuleNotFoundError
print(sys.executable)          # باید داخل ...\.venv\Scripts\ باشد


# ۲) خواندن فایل قدیمی و جدید؛ ترتیب مهم است
def read_text_any(path: Path) -&gt; str:
    for enc in ("utf-8-sig", "cp1256"):
        try:
            return path.read_text(encoding=enc)
        except UnicodeDecodeError:
            continue
    return path.read_text(encoding="utf-8", errors="replace")


# ۳) TypeError های کلاسیک
price = "57000000"             # از input یا CSV: همیشه str
total = 0 + int(price)         # بدون int: unsupported operand type(s) for +
codes = ["KSH-103", "KSH-101"]
result = codes.sort()          # sort درجا مرتب می‌کند و None برمی‌گرداند
print(result, codes[0])        # None KSH-101 — پس result[0] یعنی TypeError

# ۴) دام کپی: همه‌ی کلیدها یک لیست مشترک دارند
by_design = dict.fromkeys(["افشان", "ماهی"], [])
by_design["افشان"].append("KSH-101")
print(by_design)               # هر دو طرح KSH-101 دارند!
by_design = {d: [] for d in ["افشان", "ماهی"]}   # درست
snapshot = deepcopy(by_design) # کپی مستقل از ساختار تودرتو</code></pre>
<pre><code class="language-powershell">python -m pip install jdatetime --default-timeout=120 -i https://mirror-pypi.runflare.com/simple
Get-Command python | Select-Object Source</code></pre>
<h3>بعد از این دوره چه بخوانیم؟</h3>
<ol>
<li><strong>پروژه‌ی خودتان</strong>: همین برنامه‌ی سفارش را گسترش دهید (خروجی CSV، جست‌وجو بر اساس مشتری، تست برای cli). هیچ دوره‌ای جای یک پروژه‌ی واقعی را نمی‌گیرد.</li>
<li><strong>دوره‌ی پایتون پیشرفته</strong>: شیءگرایی عمیق، دکوراتور، generator، context manager، type hints جدی، asyncio و pytest حرفه‌ای و بسته‌بندی پروژه.</li>
<li><strong>دوره‌ی جامع جنگو</strong>: <code>Order</code> امروز به مدل جنگو، <code>store.py</code> به ORM و <code>cli.py</code> به پنل ادمین و صفحه‌ی وب تبدیل می‌شود؛ همان پروژه، این بار برای چند کاربر هم‌زمان.</li>
<li><strong>گیت و SQL</strong>: هر پروژه‌ی جدی کنترل نسخه و پایگاه داده می‌خواهد؛ دوره‌های گیت و PostgreSQL آکادمی مکمل همین مسیرند.</li>
</ol>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>متن کپی‌شده از تلگرام یا وب گاهی فاصله‌ی نشکن (U+00A0) دارد و پایتون خطای عجیب <code>invalid non-printable character U+00A0</code> می‌دهد؛ در VS Code با Find و regex <code> </code> پیدا و با فاصله‌ی عادی جایگزین کنید.</li>
<li>cp1256 تقریباً هر بایتی را بدون خطا می‌خواند، پس اگر اول آن را امتحان کنید، فایل UTF-8 هم «باز می‌شود» ولی به‌صورت حروف درهم؛ همیشه اول UTF-8، بعد cp1256.</li>
<li>در ویندوز، فرمان <code>python</code> گاهی به نسخه‌ی جعلی Microsoft Store اشاره می‌کند که فقط فروشگاه را باز می‌کند؛ از App execution aliases در تنظیمات ویندوز خاموشش کنید.</li>
<li>نام‌گذاری فایل یا پوشه‌ای به اسم کتابخانه (مثلاً <code>jdatetime.py</code>) خطای <code>partially initialized module</code> می‌دهد؛ پوشه‌ی <code>__pycache__</code> هم‌نام را هم پاک کنید.</li>
<li>هر خطای ناآشنا را دقیقاً کپی کنید و بخش‌های مخصوص خودتان (مسیر، نام متغیر) را حذف کنید؛ جست‌وجوی متن عینی پیام، سریع‌ترین راه پیدا کردن کسی است که قبلاً همین مشکل را حل کرده.</li>
</ul>""",
                },
            ],
        },
    ],
}

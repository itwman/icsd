# -*- coding: utf-8 -*-
# دوره‌ی جامع MySQL — ۸ فصل، ۴۲ درس. متن‌ها r""" هستند تا بک‌اسلش‌های کد دست‌نخورده بمانند.
# هدف: MySQL 8.0 / 8.4 LTS؛ تفاوت‌های MariaDB هرجا مهم است گفته شده.

COURSE = {
    "slug": "mysql",
    "title": "آموزش جامع MySQL",
    "category": "دیتابیس",
    "level": "intermediate",
    "summary": "از نصب و utf8mb4 درست برای فارسی تا طراحی جدول، JOIN و Window Function، ایندکس و EXPLAIN، تراکنش و قفل، بکاپ و Replication و اتصال امن به جنگو — با ده‌ها نکته‌ای که کمتر کسی می‌داند.",
    "description": (
        "<p>MySQL موتور پشت وردپرس، ووکامرس، بسیاری از سامانه‌های سفارش و حسابداری و هزاران پروژه‌ی جنگو و لاراول است؛ "
        "اما بیشتر کسانی که با آن کار می‌کنند فقط SELECT و INSERT بلدند و روزی که سایت کند شد، فارسی‌ها «؟؟؟» شد یا "
        "خطای Deadlock آمد، نمی‌دانند از کجا شروع کنند. این دوره برای برنامه‌نویسان وب، مدیران سرور و هر کسی نوشته شده "
        "که می‌خواهد MySQL را «درست» بفهمد، نه فقط کار راه بیندازد.</p>"
        "<p>از صفر SQL شروع می‌کنیم و خیلی زود به لایه‌ی حرفه‌ای می‌رسیم: <strong>utf8mb4</strong> و collation برای فارسی و "
        "مسئله‌ی ی/ک عربی، انتخاب درست نوع داده (DECIMAL برای پول، DATETIME در برابر TIMESTAMP)، کلید اصلی و خارجی و "
        "نرمال‌سازی، JOIN و CTE بازگشتی و <strong>Window Function</strong>، ایندکس B-Tree و <strong>EXPLAIN ANALYZE</strong>، "
        "MVCC و سطوح ایزوله‌سازی و قفل‌ها، کاربران و Roleها، بکاپ و بازیابی لحظه‌ای با binlog، Replication با GTID، "
        "تنظیمات کارایی و اتصال از پایتون و جنگو. در پایان یک دیتابیس کامل سفارش و تولید کارخانه‌ی فرش با گزارش‌های مدیریتی "
        "می‌سازیم و خطاهای رایج را یکی‌یکی درمان می‌کنیم.</p>"
        "<p>هر درس با بخش «نکته‌هایی که کمتر کسی می‌داند» تمام می‌شود؛ دام‌ها و ترفندهایی که معمولاً بعد از چند سال و چند "
        "حادثه‌ی تولید یاد گرفته می‌شوند. پیش‌نیاز: آشنایی مقدماتی با خط فرمان. تمرکز روی MySQL 8.0 و 8.4 LTS است و تفاوت‌های "
        "MariaDB هرجا اهمیت دارد گفته می‌شود.</p>"
    ),
    "price": 0,
    "duration_minutes": 930,
    "tags": ["MySQL", "دیتابیس", "SQL", "MariaDB", "InnoDB", "بهینه‌سازی کوئری", "جنگو"],
    "modules": [
        # ───────────────────────────── فصل ۱ ─────────────────────────────
        {
            "title": "فصل ۱: شروع درست — نصب، کلاینت‌ها و تنظیمات فارسی",
            "lessons": [
                {
                    "title": "دیتابیس رابطه‌ای و جایگاه MySQL",
                    "kind": "text",
                    "minutes": 16,
                    "is_preview": True,
                    "body": r"""<h2>دیتابیس رابطه‌ای به زبان ساده</h2>
<p>در یک دیتابیس رابطه‌ای، داده در <strong>جدول</strong>ها نگه‌داری می‌شود: هر ردیف یک «چیز» است (یک مشتری، یک سفارش، یک تخته فرش) و هر ستون یک ویژگی آن. جدول‌ها با <strong>کلید</strong> به هم وصل می‌شوند؛ مثلاً ستون <code>customer_id</code> در جدول سفارش‌ها به کلید اصلی جدول مشتریان اشاره می‌کند. زبان کار با این داده‌ها <strong>SQL</strong> است؛ زبانی «اعلانی» که در آن می‌گویید <em>چه</em> می‌خواهید، نه <em>چطور</em> پیدایش کنید. پیدا کردن بهترین مسیر اجرا کار بهینه‌ساز (Optimizer) است.</p>
<p>ارزش واقعی یک سیستم مدیریت دیتابیس (RDBMS) فقط ذخیره‌ی داده نیست؛ این است که وقتی صد کاربر هم‌زمان سفارش ثبت می‌کنند، برق می‌رود یا دو نفر یک رکورد را هم‌زمان ویرایش می‌کنند، داده سالم بماند. در فصل ششم می‌بینیم MySQL این را با موتور <strong>InnoDB</strong>، تراکنش و قفل تضمین می‌کند.</p>
<h3>چرا MySQL؟</h3>
<ul>
<li>پشت وردپرس، ووکامرس، Magento و بخش بزرگی از وب؛ تقریباً هر هاست اشتراکی ایرانی آن را دارد.</li>
<li>پشتیبانی کامل در جنگو، لاراول، Node.js و هر زبان دیگر.</li>
<li>Replication ساده و بالغ، ابزارهای بکاپ فراوان و جامعه‌ی بزرگ.</li>
<li>از نسخه‌ی 8.0 امکانات مدرن: CTE، Window Function، JSON، CHECK و ایندکس نامرئی.</li>
</ul>
<h3>کدام نسخه؟</h3>
<table><thead><tr><th>نسخه</th><th>وضعیت</th><th>توصیه</th></tr></thead><tbody>
<tr><td>5.7</td><td>پایان پشتیبانی (اکتبر 2023)</td><td>فقط مهاجرت؛ هیچ پروژه‌ی جدیدی</td></tr>
<tr><td>8.0</td><td>پایان پشتیبانی رسمی در آوریل 2026</td><td>هنوز بسیار رایج؛ برنامه‌ی ارتقا به 8.4 داشته باشید</td></tr>
<tr><td>8.4 LTS</td><td>نسخه‌ی پشتیبانی بلندمدت</td><td>انتخاب پیش‌فرض برای تولید</td></tr>
<tr><td>9.x Innovation</td><td>انتشار فصلی، عمر کوتاه</td><td>برای آزمایش امکانات جدید، نه سرور اصلی</td></tr>
</tbody></table>
<h3>MySQL، MariaDB یا PostgreSQL؟</h3>
<table><thead><tr><th>موضوع</th><th>MySQL 8.4</th><th>MariaDB 11</th><th>PostgreSQL</th></tr></thead><tbody>
<tr><td>مالک</td><td>Oracle</td><td>بنیاد MariaDB (انشعاب از MySQL)</td><td>جامعه‌ی متن‌باز</td></tr>
<tr><td>JSON</td><td>نوع دودویی واقعی</td><td>مستعار LONGTEXT با بررسی اعتبار</td><td>JSONB بسیار قوی</td></tr>
<tr><td>احراز هویت پیش‌فرض</td><td>caching_sha2_password</td><td>mysql_native_password / ed25519</td><td>SCRAM-SHA-256</td></tr>
<tr><td>GTID</td><td>قالب UUID:N</td><td>قالب domain-server-seq (ناسازگار)</td><td>—</td></tr>
<tr><td>نقطه‌ی قوت</td><td>سادگی، اکوسیستم وب</td><td>امکانات اضافه، سازگاری با سیستم‌عامل‌ها</td><td>SQL غنی، افزونه‌ها</td></tr>
</tbody></table>
<p>MariaDB در ظاهر «همان MySQL» است و کلاینت و بیشتر SQL مشترک است، اما از نسخه‌ی 10 به بعد مسیرشان جدا شده؛ فایل بکاپ، Replication و بعضی collationها بین این دو لزوماً جابه‌جا نمی‌شوند. در این دوره هرجا تفاوت مهم باشد اشاره می‌کنیم.</p>
<pre><code class="language-sql">-- نسخه‌ی سرور و موتور پیش‌فرض را همیشه اول بدانید
SELECT VERSION(), @@version_comment, @@default_storage_engine;</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>اگر خروجی <code>VERSION()</code> چیزی مثل <code>10.11.6-MariaDB</code> بود، شما MySQL ندارید؛ بسیاری از هاست‌ها و توزیع‌ها بسته‌ی <code>mysql</code> را در واقع با MariaDB پر می‌کنند.</li>
<li>بکاپی که از MySQL 8 گرفته شده ممکن است در MariaDB با خطای <code>Unknown collation: utf8mb4_0900_ai_ci</code> بازیابی نشود؛ این collation در MariaDB (دست‌کم نسخه‌های قدیمی‌تر) وجود ندارد.</li>
<li>MyISAM هنوز در MySQL هست، اما تراکنش، کلید خارجی و بازیابی پس از خرابی ندارد. هر جدول MyISAM در پروژه‌ی قدیمی را به InnoDB تبدیل کنید.</li>
<li>شماره‌ی نسخه‌ی 8.0.x مهم است: امکاناتی مثل CHECK (8.0.16)، EXPLAIN ANALYZE (8.0.18) و INTERSECT (8.0.31) در میانه‌ی عمر 8.0 اضافه شده‌اند.</li>
<li>Query Cache معروف MySQL در 8.0 کاملاً حذف شده؛ راهنماهای قدیمی که <code>query_cache_size</code> را تنظیم می‌کنند باعث خطای شروع سرور می‌شوند.</li>
</ul>""",
                },
                {
                    "title": "نصب MySQL روی ویندوز، اوبونتو و داکر",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>سه راه نصب، یک هدف: سرور سالم و امن</h2>
<p>برای یادگیری و توسعه هر سه روش زیر کار می‌کند. برای سرور تولید، اوبونتو یا داکر رایج‌تر است. اولین تصمیم مهم انتخاب نسخه است: 8.4 LTS، مگر اینکه برنامه‌ی قدیمی شما فقط با 8.0 آزموده شده باشد.</p>
<h3>ویندوز</h3>
<p>از نسخه‌ی 8.1 به بعد ابزار قدیمی MySQL Installer کنار گذاشته شده و سرور به صورت یک فایل MSI مستقل ارائه می‌شود که در پایان <strong>MySQL Configurator</strong> را اجرا می‌کند. در Configurator نوع پیکربندی را Development Computer بگذارید، رمز root قوی تعیین کنید و گزینه‌ی اجرا به‌عنوان Windows Service را فعال نگه دارید. فایل تنظیمات در <code>C:\ProgramData\MySQL\MySQL Server 8.4\my.ini</code> ساخته می‌شود (پوشه‌ی ProgramData مخفی است).</p>
<pre><code class="language-bash"># در PowerShell: وضعیت سرویس و افزودن کلاینت به PATH همین نشست
Get-Service MySQL*
$env:Path += ";C:\Program Files\MySQL\MySQL Server 8.4\bin"
mysql -u root -p</code></pre>
<h3>اوبونتو</h3>
<p>مخزن رسمی اوبونتو (22.04 و 24.04) نسخه‌ی 8.0 را می‌دهد. نصب ساده است اما دو نکته دارد: کاربر root به‌جای رمز با <code>auth_socket</code> احراز می‌شود (یعنی فقط <code>sudo mysql</code> کار می‌کند) و بلافاصله باید اسکریپت امن‌سازی را اجرا کنید.</p>
<pre><code class="language-bash">sudo apt update
sudo apt install -y mysql-server
sudo systemctl enable --now mysql
sudo mysql_secure_installation   # حذف کاربر ناشناس و دیتابیس test، غیرفعال کردن root از راه دور
sudo mysql -e "SELECT VERSION();"</code></pre>
<p>برای 8.4 روی اوبونتو باید مخزن APT خود Oracle را اضافه کنید؛ دانلود از سایت Oracle از IP ایران معمولاً مسدود است. در این حالت داکر ساده‌ترین مسیر است.</p>
<h3>داکر (پیشنهاد برای توسعه و بسیاری از سرورها)</h3>
<pre><code class="language-bash"># اگر Docker Hub در دسترس نیست از میرور داخلی استفاده کنید، مثلاً:
# docker pull docker.arvancloud.ir/mysql:8.4
docker volume create mysql_data
docker run -d --name mysql84 --restart unless-stopped \
  -p 127.0.0.1:3306:3306 \
  -e MYSQL_ROOT_PASSWORD='Kashan#1403' \
  -e TZ=Asia/Tehran \
  -v mysql_data:/var/lib/mysql \
  mysql:8.4 \
  --character-set-server=utf8mb4 --collation-server=utf8mb4_0900_ai_ci
docker exec -it mysql84 mysql -u root -p</code></pre>
<p>داده در volume نگه‌داری می‌شود و با حذف کانتینر از بین نمی‌رود. پارامترهای بعد از نام image مستقیماً به <code>mysqld</code> داده می‌شوند.</p>
<h3>پس از نصب: چک‌لیست پنج‌دقیقه‌ای</h3>
<ol>
<li>نسخه و charset سرور را ببینید: <code>SELECT VERSION(), @@character_set_server;</code></li>
<li>root فقط از localhost وصل شود.</li>
<li>برای هر برنامه کاربر جدا بسازید (درس بعد).</li>
<li>پورت 3306 را روی اینترنت باز نکنید؛ اتصال از بیرون با تونل SSH یا VPN.</li>
<li>از همین روز اول بکاپ خودکار داشته باشید (فصل هفتم).</li>
</ol>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>داکر قوانین فایروال UFW را دور می‌زند؛ <code>-p 3306:3306</code> پورت را روی همه‌ی کارت‌های شبکه باز می‌کند حتی اگر UFW آن را بسته باشد. همیشه <code>127.0.0.1:</code> را جلوی پورت بگذارید.</li>
<li>متغیر <code>MYSQL_ROOT_PASSWORD</code> فقط بار اول و روی volume خالی اعمال می‌شود؛ عوض کردنش بعداً رمز را تغییر نمی‌دهد.</li>
<li>هر فایل <code>.sql</code> یا <code>.sh</code> که در <code>/docker-entrypoint-initdb.d</code> کانتینر بگذارید، فقط در اولین راه‌اندازی اجرا می‌شود؛ جای خوبی برای ساخت دیتابیس و کاربر اولیه است.</li>
<li>در اوبونتو اگر بخواهید root با رمز وصل شود: <code>ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY '...';</code> اما بهتر است root را همان‌طور با socket نگه دارید و یک کاربر مدیر جدا بسازید.</li>
<li>در ویندوز، اگر پورت 3306 را نسخه‌ی قدیمی XAMPP (که MariaDB است) گرفته باشد، سرویس جدید بالا نمی‌آید؛ با <code>netstat -ano | findstr 3306</code> مقصر را پیدا کنید.</li>
</ul>""",
                },
                {
                    "title": "کلاینت mysql، Workbench و DBeaver؛ ساخت دیتابیس و کاربر",
                    "kind": "text",
                    "minutes": 18,
                    "is_preview": False,
                    "body": r"""<h2>ابزار کار هر روز</h2>
<p>کلاینت خط فرمان <code>mysql</code> همیشه و همه‌جا هست — روی سرور بدون رابط گرافیکی، داخل کانتینر و در اسکریپت‌ها. پس حتی اگر با ابزار گرافیکی کار می‌کنید، این کلاینت را خوب یاد بگیرید.</p>
<pre><code class="language-bash">mysql -u admin -p -h 127.0.0.1 -P 3306 carpet_shop
mysql -u admin -p -e "SHOW DATABASES;"          # اجرای یک دستور و خروج
mysql -u admin -p carpet_shop &lt; schema.sql      # اجرای یک فایل (در bash)</code></pre>
<h3>دستورهای داخلی کلاینت</h3>
<table><thead><tr><th>دستور</th><th>کار</th></tr></thead><tbody>
<tr><td><code>\G</code> به‌جای <code>;</code></td><td>نمایش عمودی نتیجه؛ برای جدول‌های پهن عالی است</td></tr>
<tr><td><code>\s</code> یا <code>status</code></td><td>نسخه، کاربر فعلی، charset اتصال، نوع اتصال (socket یا TCP)</td></tr>
<tr><td><code>SOURCE file.sql</code></td><td>اجرای فایل از داخل کلاینت</td></tr>
<tr><td><code>\c</code></td><td>لغو دستوری که نیمه‌کاره تایپ شده</td></tr>
<tr><td><code>SHOW CREATE TABLE t\G</code></td><td>تعریف کامل جدول، شامل ایندکس‌ها و charset</td></tr>
</tbody></table>
<h3>ساخت دیتابیس و کاربر برنامه</h3>
<p>هرگز برنامه را با root به دیتابیس وصل نکنید. برای هر برنامه یک دیتابیس و یک کاربر با دسترسی محدود بسازید:</p>
<pre><code class="language-sql">CREATE DATABASE carpet_shop
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_0900_ai_ci;

CREATE USER 'shop_app'@'localhost' IDENTIFIED BY 'Rug$Kashan2025';
CREATE USER 'shop_app'@'172.18.%'  IDENTIFIED BY 'Rug$Kashan2025';  -- شبکه‌ی داکر

GRANT SELECT, INSERT, UPDATE, DELETE ON carpet_shop.* TO 'shop_app'@'localhost';
GRANT SELECT, INSERT, UPDATE, DELETE ON carpet_shop.* TO 'shop_app'@'172.18.%';

SHOW GRANTS FOR 'shop_app'@'localhost';</code></pre>
<p>در MySQL هویت کاربر ترکیب «نام + میزبان» است؛ <code>'shop_app'@'localhost'</code> و <code>'shop_app'@'%'</code> دو کاربر کاملاً جدا با رمز و دسترسی جدا هستند. برای مایگریشن‌های جنگو یا لاراول معمولاً دسترسی‌های <code>CREATE, ALTER, INDEX, DROP, REFERENCES</code> هم لازم است؛ در فصل هفتم یاد می‌گیریم آن را به یک کاربر جدای «مهاجرت» بدهیم.</p>
<h3>ابزار گرافیکی</h3>
<table><thead><tr><th>ابزار</th><th>نقطه‌ی قوت</th><th>ضعف</th></tr></thead><tbody>
<tr><td>MySQL Workbench</td><td>رسمی، طراحی ER و Performance Reports</td><td>سنگین، گاهی ناپایدار با نسخه‌های جدید سرور</td></tr>
<tr><td>DBeaver Community</td><td>رایگان، چنددیتابیسی، ویرایشگر داده‌ی عالی</td><td>تنظیمات زیاد، مصرف حافظه‌ی Java</td></tr>
<tr><td>phpMyAdmin</td><td>روی هاست‌ها آماده است</td><td>برای جدول بزرگ و ایمپورت حجیم مناسب نیست</td></tr>
</tbody></table>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>در لینوکس <code>-h localhost</code> یعنی اتصال با Unix socket و <code>-h 127.0.0.1</code> یعنی TCP؛ این دو به کاربرهای متفاوتی تطبیق می‌خورند و علت بسیاری از خطاهای Access denied همین است.</li>
<li>با <code>mysql_config_editor set --login-path=shop -u admin -p</code> رمز به شکل مبهم‌شده در <code>~/.mylogin.cnf</code> ذخیره می‌شود و بعد فقط <code>mysql --login-path=shop</code> می‌زنید؛ رمز در تاریخچه‌ی shell و فهرست پردازه‌ها دیده نمی‌شود.</li>
<li>در PowerShell عملگر <code>&lt;</code> برای ورودی فایل کار نمی‌کند؛ به‌جای آن <code>mysql -u admin -p carpet_shop -e "source schema.sql"</code> بزنید.</li>
<li>گزینه‌ی <code>--safe-updates</code> (یا نام بامزه‌اش <code>--i-am-a-dummy</code>) را در بخش <code>[mysql]</code> فایل تنظیمات بگذارید تا UPDATE و DELETE بدون WHERE کلیدی در کلاینت اجرا نشوند.</li>
<li>در MySQL 8 دستور GRANT دیگر کاربر نمی‌سازد؛ اول باید CREATE USER بزنید. آموزش‌های قدیمی که <code>GRANT ... IDENTIFIED BY</code> دارند خطای نحوی می‌دهند.</li>
</ul>""",
                },
                {
                    "title": "charset و collation برای فارسی: دام utf8 در برابر utf8mb4",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>معروف‌ترین دام MySQL برای متن فارسی</h2>
<p><strong>Character set</strong> تعیین می‌کند هر کاراکتر با چه بایت‌هایی ذخیره شود و <strong>Collation</strong> تعیین می‌کند مقایسه و مرتب‌سازی چطور انجام شود (بزرگ و کوچکی حروف، اعراب، ترتیب الفبا). دام تاریخی این است: در MySQL نام <code>utf8</code> در واقع یعنی <code>utf8mb3</code>، یعنی حداکثر ۳ بایت برای هر کاراکتر. متن فارسی معمولی در ۲ بایت جا می‌شود، پس سال‌ها همه‌چیز درست کار می‌کرد — تا روزی که کاربری در نظرات ایموجی گذاشت یا نامی با یک کاراکتر نادر وارد کرد و خطای زیر آمد:</p>
<pre><code class="language-sql">ERROR 1366 (HY000): Incorrect string value: '\xF0\x9F\x8C\xB9' for column 'comment' at row 1</code></pre>
<p><code>utf8mb4</code> یونیکد کامل (تا ۴ بایت) است. در MySQL 8 پیش‌فرض سرور همین است، اما دیتابیس‌ها و جدول‌هایی که از 5.7 مهاجرت کرده‌اند هنوز ممکن است utf8mb3 یا حتی latin1 باشند. <code>utf8mb3</code> منسوخ شده و در نسخه‌های آینده حذف می‌شود.</p>
<h3>چهار سطح، و سطح پنجم که همه فراموش می‌کنند</h3>
<p>charset در سطح سرور، دیتابیس، جدول و ستون تعریف می‌شود و هر سطح پیش‌فرض سطح پایین‌تر است. اما سطح پنجم <strong>اتصال</strong> است: کلاینت باید بگوید بایت‌هایی که می‌فرستد با چه charset‌ای است. اگر اتصال latin1 باشد و ستون utf8mb4، فارسی‌ها «؟؟؟؟» یا «Ø³Ù„Ø§Ù…» ذخیره می‌شوند.</p>
<pre><code class="language-sql">SHOW VARIABLES LIKE 'character_set%';
SHOW VARIABLES LIKE 'collation%';
SET NAMES utf8mb4 COLLATE utf8mb4_0900_ai_ci;   -- تنظیم charset اتصال

-- کدام ستون‌ها هنوز utf8mb4 نیستند؟
SELECT table_name, column_name, character_set_name, collation_name
FROM information_schema.columns
WHERE table_schema = 'carpet_shop'
  AND character_set_name IS NOT NULL
  AND character_set_name &lt;&gt; 'utf8mb4';

-- تبدیل یک جدول (کل جدول بازسازی می‌شود؛ روی جدول بزرگ در ساعت کم‌بار)
ALTER TABLE customers CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;</code></pre>
<h3>کدام collation؟</h3>
<table><thead><tr><th>Collation</th><th>رفتار</th><th>کاربرد</th></tr></thead><tbody>
<tr><td><code>utf8mb4_0900_ai_ci</code></td><td>UCA 9.0، بی‌حساس به اعراب و بزرگی حروف، NO PAD، سریع</td><td>پیش‌فرض MySQL 8؛ انتخاب عمومی خوب</td></tr>
<tr><td><code>utf8mb4_0900_as_cs</code></td><td>حساس به اعراب و بزرگی حروف</td><td>کد محصول، نام کاربری حساس</td></tr>
<tr><td><code>utf8mb4_persian_ci</code></td><td>UCA قدیمی‌تر با تنظیم مخصوص الفبای فارسی، PAD SPACE</td><td>وقتی ترتیب الفبایی دقیق فارسی مهم است</td></tr>
<tr><td><code>utf8mb4_unicode_ci</code></td><td>UCA 4.0، قدیمی</td><td>سازگاری با MariaDB و پروژه‌های قدیمی</td></tr>
<tr><td><code>utf8mb4_bin</code></td><td>مقایسه‌ی بایت‌به‌بایت</td><td>توکن، هش، شناسه‌های دقیق</td></tr>
</tbody></table>
<p>قبل از انتخاب نهایی، روی داده‌ی واقعی خودتان مرتب‌سازی را ببینید:</p>
<pre><code class="language-sql">SELECT name FROM (
  SELECT 'گلیم' AS name UNION ALL SELECT 'پشتی' UNION ALL SELECT 'ژاکت'
  UNION ALL SELECT 'کناره' UNION ALL SELECT 'چله' UNION ALL SELECT 'بافت'
) t ORDER BY name COLLATE utf8mb4_persian_ci;</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>collationهای <code>0900</code> از نوع NO PAD هستند: <code>'فرش' = 'فرش '</code> (با فاصله‌ی انتهایی) در آن‌ها <em>نادرست</em> است، اما در <code>utf8mb4_unicode_ci</code> درست. مهاجرت collation می‌تواند رفتار UNIQUE را عوض کند.</li>
<li>در collationهای UCA نیم‌فاصله کاراکتری «قابل چشم‌پوشی» است؛ بنابراین معمولاً <code>'می‌شود' = 'میشود'</code> درست است. برای جست‌وجو خوب است، برای UNIQUE ممکن است غافلگیرتان کند.</li>
<li>JOIN بین دو ستون با collation متفاوت یا خطای <code>Illegal mix of collations</code> می‌دهد یا ایندکس را بی‌استفاده می‌کند؛ کل دیتابیس را یکدست نگه دارید.</li>
<li>ستون <code>VARCHAR(255)</code> در utf8mb4 تا 1020 بایت جا می‌گیرد؛ محدودیت قدیمی 767 بایت ایندکس در 5.6 دلیل آن <code>VARCHAR(191)</code>های معروف لاراول بود که در MySQL 8 دیگر لازم نیست.</li>
<li>برای یک ستون خاص می‌توانید collation جدا بگذارید: <code>sku VARCHAR(30) COLLATE utf8mb4_bin</code>؛ بقیه‌ی جدول دست نمی‌خورد.</li>
</ul>""",
                },
                {
                    "title": "مسئله‌ی ی و ک عربی، ارقام فارسی و فایل my.cnf",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>«علی» که پیدا نمی‌شود</h2>
<p>کاربر در جست‌وجو «کاشانی» تایپ می‌کند و نتیجه‌ای نمی‌آید، در حالی که رکورد وجود دارد. علت: داده با کیبورد قدیمی ویندوز، از فایل اکسل یا از یک نرم‌افزار حسابداری قدیمی وارد شده و به‌جای «ی» فارسی (U+06CC) و «ک» فارسی (U+06A9)، «ي» عربی (U+064A) و «ك» عربی (U+0643) دارد. این دو از نظر ظاهری تقریباً یکسان‌اند اما کاراکترهای متفاوتی هستند و هیچ collationی را نمی‌توان با اطمینان کامل مسئول یکسان دیدنشان دانست.</p>
<pre><code class="language-sql">SELECT HEX('ی'), HEX('ي'), HEX('ک'), HEX('ك');
-- DB8C       D98A       DAA9       D983

-- پیدا کردن رکوردهای آلوده (مقایسه‌ی دودویی تا collation دخالت نکند)
SELECT id, full_name
FROM customers
WHERE full_name COLLATE utf8mb4_bin LIKE '%ي%'
   OR full_name COLLATE utf8mb4_bin LIKE '%ك%';</code></pre>
<h3>درمان: یکسان‌سازی در ورودی، نه در جست‌وجو</h3>
<p>راه درست این است که داده <em>همیشه</em> با حروف فارسی ذخیره شود. یک بار داده‌ی موجود را اصلاح کنید و بعد جلوی ورود دوباره را بگیرید؛ بهترین جا لایه‌ی برنامه است (مثلاً متد <code>clean</code> در فرم جنگو)، و به‌عنوان تور ایمنی یک Trigger در خود دیتابیس:</p>
<pre><code class="language-sql">UPDATE customers
SET full_name = REPLACE(REPLACE(full_name, 'ي', 'ی'), 'ك', 'ک')
WHERE full_name COLLATE utf8mb4_bin LIKE '%ي%'
   OR full_name COLLATE utf8mb4_bin LIKE '%ك%';

CREATE TRIGGER customers_fa_bi BEFORE INSERT ON customers
FOR EACH ROW
  SET NEW.full_name = REPLACE(REPLACE(NEW.full_name, 'ي', 'ی'), 'ك', 'ک');</code></pre>
<p>ارقام هم همین داستان را دارند: «۰۹۱۲» فارسی، «٠٩١٢» عربی و «0912» لاتین سه رشته‌ی متفاوت‌اند. شماره‌ی موبایل، کد ملی و کد پستی را همیشه با ارقام لاتین ذخیره کنید و نمایش فارسی را به لایه‌ی نمایش بسپارید.</p>
<h3>فایل تنظیمات: my.cnf و my.ini</h3>
<table><thead><tr><th>محیط</th><th>مسیر رایج</th></tr></thead><tbody>
<tr><td>اوبونتو (بسته‌ی رسمی)</td><td><code>/etc/mysql/mysql.conf.d/mysqld.cnf</code></td></tr>
<tr><td>داکر</td><td><code>/etc/mysql/conf.d/*.cnf</code> (فایل خود را mount کنید)</td></tr>
<tr><td>ویندوز</td><td><code>C:\ProgramData\MySQL\MySQL Server 8.4\my.ini</code></td></tr>
</tbody></table>
<pre><code class="language-ini">[mysqld]
character-set-server = utf8mb4
collation-server     = utf8mb4_0900_ai_ci
default-time-zone    = '+03:30'
sql_mode             = STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION,ONLY_FULL_GROUP_BY
max_allowed_packet   = 64M

[client]
default-character-set = utf8mb4

[mysql]
safe-updates
prompt = "\u@\h [\d]&gt; "</code></pre>
<p>بخش <code>[mysqld]</code> برای سرور، <code>[client]</code> برای همه‌ی ابزارهای کلاینت (mysql، mysqldump) و <code>[mysql]</code> فقط برای کلاینت تعاملی است. پس از تغییر، سرویس را ری‌استارت کنید.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>mysqld --verbose --help | grep -A1 "Default options"</code> ترتیب دقیق فایل‌هایی را که سرور می‌خواند نشان می‌دهد؛ اگر تنظیمی اعمال نمی‌شود، احتمالاً فایل دیگری بعد از فایل شما آن را بازنویسی کرده است.</li>
<li><code>SET PERSIST max_connections = 300;</code> تنظیم را بدون ری‌استارت اعمال و در <code>mysqld-auto.cnf</code> داخل پوشه‌ی داده ذخیره می‌کند؛ این فایل بعد از my.cnf خوانده می‌شود و بر آن غلبه دارد — منشأ رایج «تنظیم را در my.cnf عوض کردم ولی اثر ندارد».</li>
<li>تابع <code>REPLACE()</code> در MySQL همیشه حساس به حروف و دودویی تطبیق می‌دهد، مستقل از collation ستون؛ برای همین برای اصلاح ی/ک قابل اعتماد است.</li>
<li>مقدار ثابت <code>+03:30</code> برای ایران از زمان حذف ساعت تابستانی (۱۴۰۱) کافی است؛ برای داده‌ی تاریخی قبل از آن، نام منطقه‌ی <code>Asia/Tehran</code> و جدول‌های timezone لازم است.</li>
<li>در ویندوز، Notepad ممکن است my.ini را با BOM ذخیره کند و سرور خط اول را نفهمد؛ با VS Code و کدگذاری UTF-8 بدون BOM ذخیره کنید.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۲ ─────────────────────────────
        {
            "title": "فصل ۲: SQL پایه — خواندن و نوشتن داده، درست و امن",
            "lessons": [
                {
                    "title": "SELECT، WHERE، ORDER BY و LIMIT؛ و ترتیب واقعی اجرای کوئری",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>اولین جدول و اولین کوئری‌ها</h2>
<p>در سراسر این فصل با جدول فرش‌های یک فروشگاه کار می‌کنیم. قیمت‌ها به ریال و با DECIMAL ذخیره می‌شوند (دلیلش را در فصل سوم می‌بینیم).</p>
<pre><code class="language-sql">CREATE TABLE carpets (
  id          INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  sku         VARCHAR(20)  NOT NULL UNIQUE,
  title       VARCHAR(150) NOT NULL,
  city        VARCHAR(40)  NOT NULL,
  reeds       SMALLINT UNSIGNED NULL,        -- تراکم (شانه)
  width_cm    SMALLINT UNSIGNED NOT NULL,
  length_cm   SMALLINT UNSIGNED NOT NULL,
  price       DECIMAL(14,0) NOT NULL,         -- ریال
  stock       INT NOT NULL DEFAULT 0,
  created_at  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO carpets (sku, title, city, reeds, width_cm, length_cm, price, stock) VALUES
('KSH-1001', 'فرش دستباف کاشان لچک‌ترنج', 'کاشان', 50, 200, 300, 480000000, 2),
('TBZ-2040', 'فرش تبریز ماهی', 'تبریز', 60, 150, 225, 350000000, 1),
('NAN-0310', 'نائین ۹ لا ابریشم', 'نائین', NULL, 100, 150, 920000000, 0),
('KSH-M700', 'فرش ماشینی ۷۰۰ شانه', 'کاشان', 700, 250, 350, 65000000, 40),
('QOM-0120', 'قم تمام ابریشم', 'قم', 70, 100, 150, 1250000000, 1);</code></pre>
<h3>خواندن با شرط، مرتب‌سازی و محدود کردن</h3>
<pre><code class="language-sql">SELECT sku, title, price / 10 AS price_toman
FROM carpets
WHERE city = 'کاشان' AND stock &gt; 0
ORDER BY price DESC, id
LIMIT 10;

-- صفحه‌ی سوم با ۲۰ ردیف در هر صفحه
SELECT id, title FROM carpets ORDER BY id LIMIT 20 OFFSET 40;</code></pre>
<p><code>SELECT *</code> را فقط برای کاوش دستی بزنید. در کد برنامه ستون‌ها را نام ببرید: هم داده‌ی کمتری جابه‌جا می‌شود، هم اضافه شدن ستون جدید برنامه را نمی‌شکند و هم (در فصل پنجم) امکان covering index فراهم می‌شود.</p>
<h3>ترتیب منطقی اجرا</h3>
<p>کوئری به ترتیبی که می‌نویسید اجرا <em>نمی‌شود</em>. ترتیب منطقی این است:</p>
<ol>
<li><code>FROM</code> و <code>JOIN</code> — کدام ردیف‌ها در دسترس‌اند</li>
<li><code>WHERE</code> — فیلتر ردیف‌ها</li>
<li><code>GROUP BY</code> و بعد <code>HAVING</code></li>
<li><code>SELECT</code> — محاسبه‌ی ستون‌ها و نام مستعار (alias)</li>
<li><code>ORDER BY</code> و در پایان <code>LIMIT</code></li>
</ol>
<p>به همین دلیل نمی‌توانید در WHERE از aliasی که در SELECT ساخته‌اید استفاده کنید (هنوز ساخته نشده)، اما در ORDER BY می‌توانید. MySQL در HAVING هم alias را می‌پذیرد که یک توسعه‌ی غیراستاندارد است.</p>
<pre><code class="language-sql">-- خطا: Unknown column 'price_toman' in 'where clause'
SELECT price / 10 AS price_toman FROM carpets WHERE price_toman &gt; 1000000;
-- درست
SELECT price / 10 AS price_toman FROM carpets WHERE price &gt; 10000000 ORDER BY price_toman;</code></pre>
<h3>صفحه‌بندی سریع با keyset</h3>
<p><code>LIMIT 20 OFFSET 200000</code> یعنی سرور ۲۰۰٬۰۲۰ ردیف را بخواند و ۲۰۰٬۰۰۰ تا را دور بریزد؛ صفحه‌های آخر فهرست‌های بزرگ به همین دلیل کندند. روش keyset (یا seek) به‌جای شماره‌ی صفحه، آخرین کلید دیده‌شده را می‌گیرد:</p>
<pre><code class="language-sql">SELECT id, title FROM carpets
WHERE id &gt; 18340          -- آخرین id صفحه‌ی قبل
ORDER BY id
LIMIT 20;</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>بدون ORDER BY، ترتیب نتیجه هیچ تضمینی ندارد؛ ممکن است امروز بر اساس id باشد و فردا بعد از اضافه شدن یک ایندکس عوض شود.</li>
<li>اگر ORDER BY روی ستونی غیریکتا باشد (مثلاً price)، صفحه‌بندی با LIMIT ممکن است یک ردیف را دو بار نشان دهد و یکی را هرگز؛ همیشه یک ستون یکتا (id) را به‌عنوان مرتب‌سازی دوم اضافه کنید.</li>
<li>در MySQL می‌توانید بنویسید <code>ORDER BY 2</code> (ستون دوم SELECT)؛ کوتاه است اما با جابه‌جا شدن ستون‌ها بی‌صدا عوض می‌شود.</li>
<li>نتیجه‌ی تقسیم <code>price / 10</code> همیشه اعشاری است (<code>div_precision_increment</code> رقم اعشار)؛ برای تقسیم صحیح از <code>price DIV 10</code> استفاده کنید.</li>
<li>در کلاینت، <code>SELECT ... \G</code> برای جدول‌هایی با ستون فارسی طولانی خواناتر است، چون چینش راست‌به‌چپ در جدول ASCII به هم می‌ریزد.</li>
</ul>""",
                },
                {
                    "title": "عملگرها، NULL و منطق سه‌ارزشی، LIKE و REGEXP",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>شرط‌ها دقیق‌تر از آن‌اند که به نظر می‌رسند</h2>
<p>عملگرهای مقایسه (<code>= &lt;&gt; &lt; &gt; &lt;= &gt;=</code>)، منطقی (<code>AND OR NOT</code>) و مجموعه‌ای (<code>IN</code>، <code>BETWEEN</code>) را همه می‌شناسند. دام‌ها در جزئیات است.</p>
<pre><code class="language-sql">SELECT sku FROM carpets
WHERE city IN ('کاشان', 'قم')
  AND price BETWEEN 50000000 AND 500000000      -- شامل هر دو سر
  AND (reeds &gt;= 50 OR reeds IS NULL);</code></pre>
<p>اولویت <code>AND</code> از <code>OR</code> بیشتر است؛ <code>a OR b AND c</code> یعنی <code>a OR (b AND c)</code>. هر وقت هر دو را دارید پرانتز بگذارید.</p>
<h3>BETWEEN و تاریخ</h3>
<p><code>created_at BETWEEN '2025-03-01' AND '2025-03-31'</code> سفارش‌های ساعت 10 صبح روز 31 را جا می‌اندازد، چون <code>'2025-03-31'</code> یعنی نیمه‌شب ابتدای آن روز. الگوی درست بازه‌ی نیمه‌باز است:</p>
<pre><code class="language-sql">WHERE created_at &gt;= '2025-03-01' AND created_at &lt; '2025-04-01'</code></pre>
<h3>NULL یعنی «نامعلوم»، نه صفر و نه خالی</h3>
<p>هر مقایسه با NULL نتیجه‌ی <strong>UNKNOWN</strong> می‌دهد و WHERE فقط ردیف‌هایی را برمی‌گرداند که شرطشان TRUE باشد. این منطق سه‌ارزشی است:</p>
<table><thead><tr><th>عبارت</th><th>نتیجه</th></tr></thead><tbody>
<tr><td><code>NULL = NULL</code></td><td>NULL (نه TRUE)</td></tr>
<tr><td><code>NULL &lt;&gt; 5</code></td><td>NULL</td></tr>
<tr><td><code>TRUE AND NULL</code></td><td>NULL</td></tr>
<tr><td><code>FALSE AND NULL</code></td><td>FALSE</td></tr>
<tr><td><code>TRUE OR NULL</code></td><td>TRUE</td></tr>
<tr><td><code>NULL IS NULL</code></td><td>TRUE</td></tr>
<tr><td><code>NULL &lt;=&gt; NULL</code></td><td>TRUE (مقایسه‌ی NULL-امن)</td></tr>
</tbody></table>
<pre><code class="language-sql">-- فرش نائین (reeds = NULL) در هیچ‌کدام از این دو نیست!
SELECT COUNT(*) FROM carpets WHERE reeds &gt;= 60;
SELECT COUNT(*) FROM carpets WHERE NOT (reeds &gt;= 60);

SELECT sku, COALESCE(reeds, 0) AS reeds_or_zero FROM carpets;
SELECT COUNT(*), COUNT(reeds) FROM carpets;   -- COUNT(ستون) NULLها را نمی‌شمارد</code></pre>
<h3>LIKE و ایندکس</h3>
<p><code>%</code> یعنی هر تعداد کاراکتر و <code>_</code> یعنی دقیقاً یک کاراکتر. حساس بودن به بزرگی حروف به collation ستون بستگی دارد، نه به LIKE.</p>
<pre><code class="language-sql">SELECT sku FROM carpets WHERE sku LIKE 'KSH-%';     -- می‌تواند از ایندکس sku استفاده کند
SELECT sku FROM carpets WHERE title LIKE '%ابریشم%'; -- اسکن کامل جدول
SELECT sku FROM carpets WHERE sku LIKE 'KSH\_%';     -- خود کاراکتر _ را جست‌وجو کن
SELECT title FROM carpets WHERE title REGEXP '^فرش (دستباف|ماشینی)';</code></pre>
<p>LIKE با پیشوند ثابت (<code>'KSH-%'</code>) مثل یک بازه عمل می‌کند و ایندکس را به کار می‌گیرد؛ <code>%</code> در ابتدا یعنی بررسی تک‌تک ردیف‌ها. برای جست‌وجوی واقعی متن فارسی در فصل پنجم سراغ FULLTEXT می‌رویم. REGEXP در MySQL 8 بر پایه‌ی کتابخانه‌ی ICU است و یونیکد را درست می‌فهمد.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>WHERE id NOT IN (SELECT customer_id FROM orders)</code> اگر حتی یک customer_id برابر NULL باشد، <em>هیچ</em> ردیفی برنمی‌گرداند؛ به‌جایش NOT EXISTS بنویسید (فصل چهارم).</li>
<li>ستون UNIQUE می‌تواند چند NULL داشته باشد، چون NULLها با هم «برابر» نیستند؛ اگر یکتایی واقعی می‌خواهید ستون را NOT NULL کنید.</li>
<li>در مرتب‌سازی صعودی NULLها اول می‌آیند. برای آخر بردنشان: <code>ORDER BY reeds IS NULL, reeds</code>.</li>
<li><code>'12abc' = 12</code> در MySQL TRUE است (با یک warning)، چون رشته به عدد تبدیل می‌شود؛ مقایسه‌ی ستون متنی با عدد هم نتیجه‌ی غلط می‌دهد و هم ایندکس را از کار می‌اندازد.</li>
<li><code>SHOW WARNINGS;</code> را بلافاصله بعد از هر دستوری که «n warnings» گزارش کرد اجرا کنید؛ MySQL بسیاری از خطاهای داده را بی‌صدا به warning تبدیل می‌کند.</li>
</ul>""",
                },
                {
                    "title": "INSERT، UPDATE و DELETE امن؛ safe updates و sql_mode",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>نوشتن داده بدون ترس</h2>
<p>هر برنامه‌نویسی دست‌کم یک بار UPDATE بدون WHERE اجرا کرده است. در این درس الگوهایی را می‌بینیم که این اتفاق را تقریباً ناممکن می‌کنند.</p>
<h3>INSERT</h3>
<pre><code class="language-sql">-- چند ردیف در یک دستور: ده‌ها برابر سریع‌تر از INSERTهای جدا
INSERT INTO carpets (sku, title, city, width_cm, length_cm, price, stock) VALUES
  ('KSH-M701', 'ماشینی ۱۲۰۰ شانه طرح افشان', 'کاشان', 200, 300, 98000000, 25),
  ('KSH-M702', 'ماشینی ۱۰۰۰ شانه طرح هریس',  'کاشان', 150, 225, 54000000, 18);

SELECT LAST_INSERT_ID();   -- id اولین ردیفِ آخرین INSERT همین اتصال

-- کپی از یک جدول دیگر (مثلاً جدول موقت ورود از اکسل)
INSERT INTO carpets (sku, title, city, width_cm, length_cm, price)
SELECT sku, title, city, w, l, price FROM import_batch WHERE valid = 1;</code></pre>
<h3>UPDATE و DELETE با روال سه‌مرحله‌ای</h3>
<ol>
<li>اول همان WHERE را با SELECT اجرا کنید و تعداد ردیف‌ها را ببینید.</li>
<li>تراکنش باز کنید، UPDATE یا DELETE را اجرا کنید و «rows affected» را با عدد مرحله‌ی ۱ مقایسه کنید.</li>
<li>اگر درست بود COMMIT، وگرنه ROLLBACK.</li>
</ol>
<pre><code class="language-sql">SELECT COUNT(*) FROM carpets WHERE city = 'کاشان' AND sku LIKE 'KSH-M%';   -- 3

START TRANSACTION;
UPDATE carpets SET price = ROUND(price * 1.15, -5)      -- ۱۵٪ افزایش، گرد به صد هزار ریال
WHERE city = 'کاشان' AND sku LIKE 'KSH-M%';
-- Query OK, 3 rows affected
COMMIT;

-- حذف دسته‌ای جدول بزرگ: تکه‌تکه تا قفل و undo log سنگین نشود
DELETE FROM audit_log WHERE created_at &lt; '2024-01-01' ORDER BY id LIMIT 5000;</code></pre>
<p>دستور آخر را در یک حلقه تا وقتی «0 rows affected» شود تکرار کنید. حذف میلیون‌ها ردیف در یک دستور، تراکنشی عظیم می‌سازد که Replica را عقب می‌اندازد و ROLLBACK آن ممکن است ساعت‌ها طول بکشد.</p>
<h3>Safe updates</h3>
<p>با <code>SET sql_safe_updates = 1</code> (یا گزینه‌ی <code>safe-updates</code> کلاینت) هر UPDATE یا DELETE که در WHERE از ستون کلیددار استفاده نکند و LIMIT هم نداشته باشد، با <code>ERROR 1175</code> رد می‌شود. MySQL Workbench این گزینه را به‌طور پیش‌فرض روشن دارد.</p>
<h3>sql_mode: سخت‌گیر باشید</h3>
<pre><code class="language-sql">SET SESSION sql_mode = 'TRADITIONAL';
INSERT INTO carpets (sku, title, city, width_cm, length_cm, price)
VALUES ('X-1', REPEAT('ا', 300), 'کاشان', 100, 150, 1);
-- ERROR 1406: Data too long for column 'title'
-- بدون حالت strict: فقط یک warning و متن بی‌صدا بریده می‌شد!</code></pre>
<table><thead><tr><th>دستور</th><th>تراکنشی؟</th><th>AUTO_INCREMENT</th><th>Trigger</th></tr></thead><tbody>
<tr><td><code>DELETE FROM t</code></td><td>بله، قابل ROLLBACK</td><td>ادامه می‌یابد</td><td>اجرا می‌شود</td></tr>
<tr><td><code>TRUNCATE t</code></td><td>خیر (DDL)</td><td>صفر می‌شود</td><td>اجرا نمی‌شود</td></tr>
<tr><td><code>DROP TABLE t</code></td><td>خیر</td><td>—</td><td>—</td></tr>
</tbody></table>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>MySQL به‌طور پیش‌فرض «rows affected» را برای ردیف‌هایی که واقعاً تغییر کرده‌اند می‌شمارد، نه ردیف‌های منطبق؛ UPDATE که مقدار را به همان مقدار قبلی می‌برد «0 rows affected» می‌گوید. پیام «Rows matched» را ببینید.</li>
<li>بعد از INSERT چندردیفی، <code>LAST_INSERT_ID()</code> شناسه‌ی <em>اولین</em> ردیف را می‌دهد، نه آخرین؛ و مخصوص همان اتصال است، پس بین کاربران هم‌زمان قاطی نمی‌شود.</li>
<li>TRUNCATE روی جدولی که کلید خارجی به آن اشاره می‌کند، حتی اگر جدول فرزند خالی باشد، خطا می‌دهد.</li>
<li>در UPDATE چندستونی، MySQL انتسابات را از چپ به راست اعمال می‌کند: <code>SET a = b, b = a</code> هر دو را برابر b می‌کند، نه جابه‌جا (برخلاف استاندارد SQL و PostgreSQL).</li>
<li>عملیات روی جدول بزرگ را با <code>LIMIT</code> تکه‌تکه کنید و بین تکه‌ها یک مکث کوتاه بگذارید تا Replicaها و بقیه‌ی کاربران نفس بکشند.</li>
</ul>""",
                },
                {
                    "title": "Upsert با INSERT ... ON DUPLICATE KEY UPDATE؛ و دام‌های REPLACE و INSERT IGNORE",
                    "kind": "text",
                    "minutes": 18,
                    "is_preview": False,
                    "body": r"""<h2>«اگر هست به‌روز کن، اگر نیست اضافه کن»</h2>
<p>سناریوی رایج: هر شب فایل موجودی انبار کارخانه (مثلاً خروجی اکسل) باید با جدول محصولات هماهنگ شود. کالاهای جدید اضافه و کالاهای موجود به‌روز شوند. راه ساده‌لوحانه «SELECT، بعد تصمیم، بعد INSERT یا UPDATE» است که زیر بار هم‌زمان شرایط رقابتی (race condition) می‌سازد: دو پردازه هم‌زمان می‌بینند ردیف وجود ندارد و هر دو INSERT می‌کنند. MySQL این کار را در یک دستور اتمی انجام می‌دهد، به شرط آنکه یک کلید <strong>UNIQUE</strong> یا PRIMARY KEY برخورد را تشخیص دهد.</p>
<pre><code class="language-sql">-- sku در جدول carpets یکتاست
INSERT INTO carpets (sku, title, city, width_cm, length_cm, price, stock)
VALUES ('KSH-M700', 'فرش ماشینی ۷۰۰ شانه', 'کاشان', 250, 350, 69000000, 12)
AS new
ON DUPLICATE KEY UPDATE
  price = new.price,
  stock = carpets.stock + new.stock;</code></pre>
<p>نحو <code>AS new</code> از نسخه‌ی 8.0.19 آمده و جایگزین تابع قدیمی <code>VALUES(col)</code> شده که منسوخ اعلام شده است. در MariaDB و MySQL قدیمی همان <code>VALUES(price)</code> را بنویسید.</p>
<h3>معنی «rows affected»</h3>
<table><thead><tr><th>عدد</th><th>معنا</th></tr></thead><tbody>
<tr><td>1</td><td>ردیف جدید درج شد</td></tr>
<tr><td>2</td><td>ردیف موجود به‌روز شد</td></tr>
<tr><td>0</td><td>ردیف موجود بود و مقادیر جدید با قبلی یکسان بود</td></tr>
</tbody></table>
<h3>ورود دسته‌ای از جدول موقت</h3>
<pre><code class="language-sql">INSERT INTO carpets (sku, title, city, width_cm, length_cm, price, stock)
SELECT sku, title, city, w, l, price, qty FROM import_batch
ON DUPLICATE KEY UPDATE
  price = VALUES(price),        -- در حالت INSERT ... SELECT هنوز رایج است
  stock = VALUES(stock);

-- گرفتن id ردیف، چه درج شده باشد چه به‌روز
INSERT INTO tags (name) VALUES ('ابریشم')
ON DUPLICATE KEY UPDATE id = LAST_INSERT_ID(id);
SELECT LAST_INSERT_ID();</code></pre>
<h3>REPLACE و INSERT IGNORE: دو میان‌بر خطرناک</h3>
<p><code>REPLACE INTO</code> ردیف قدیمی را <strong>حذف</strong> و ردیف تازه را درج می‌کند. یعنی: id عوض می‌شود، ستون‌هایی که نام نبرده‌اید به پیش‌فرض برمی‌گردند، Triggerهای DELETE اجرا می‌شوند و اگر کلید خارجی با <code>ON DELETE CASCADE</code> داشته باشید، ردیف‌های فرزند (مثلاً اقلام سفارش) هم پاک می‌شوند.</p>
<p><code>INSERT IGNORE</code> فقط تکراری‌ها را نادیده نمی‌گیرد؛ <em>همه‌ی</em> خطاهای قابل‌تبدیل را به warning تبدیل می‌کند: متن بلند بریده می‌شود، NULL در ستون NOT NULL به صفر یا رشته‌ی خالی تبدیل می‌شود و تاریخ نامعتبر صفر می‌شود — حتی در حالت strict.</p>
<pre><code class="language-sql">INSERT IGNORE INTO carpets (sku, title, city, width_cm, length_cm, price)
VALUES ('KSH-1001', 'تکراری', 'کاشان', 1, 1, 1);
SHOW WARNINGS;   -- Duplicate entry 'KSH-1001' for key 'carpets.sku'</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>اگر جدول چند کلید UNIQUE داشته باشد و ردیف ورودی با دو ردیف مختلف برخورد کند، ODKU فقط <em>یکی</em> از آن‌ها را به‌روز می‌کند و کدام، قابل پیش‌بینی نیست؛ upsert را روی جدول‌هایی با یک کلید یکتای منطقی انجام دهید.</li>
<li>هر ODKU که به UPDATE ختم شود هم یک عدد AUTO_INCREMENT مصرف می‌کند؛ جدولی که روزی میلیون‌ها upsert می‌خورد با INT معمولی سریع‌تر از آنچه فکر می‌کنید به سقف می‌رسد.</li>
<li>ترتیب انتساب‌ها در ODKU مهم است: در <code>SET a = new.a, b = a + 1</code> ستون b از مقدار <em>جدید</em> a استفاده می‌کند.</li>
<li>برای «فقط اگر نیست درج کن» بدون خاموش کردن بقیه‌ی خطاها از <code>ON DUPLICATE KEY UPDATE id = id</code> استفاده کنید؛ امن‌تر از INSERT IGNORE است.</li>
<li>MySQL برخلاف MariaDB و PostgreSQL عبارت <code>RETURNING</code> ندارد؛ ستون‌های محاسبه‌شده را با یک SELECT بعدی بخوانید.</li>
</ul>""",
                },
                {
                    "title": "توابع رشته، عدد و تاریخ، CASE و تاریخ شمسی",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>جعبه‌ابزار توابع داخلی</h2>
<p>MySQL صدها تابع دارد؛ این درس آن‌هایی را پوشش می‌دهد که هر روز لازم می‌شوند، به‌همراه رفتارهایی که مخصوص متن فارسی و پول ریالی است.</p>
<h3>رشته‌ها</h3>
<pre><code class="language-sql">SELECT
  LENGTH('کاشان')        AS bytes,       -- 10 : تعداد بایت
  CHAR_LENGTH('کاشان')   AS chars,       -- 5  : تعداد کاراکتر
  CONCAT('فرش ', NULL)   AS c1,          -- NULL !
  CONCAT_WS(' - ', 'کاشان', NULL, 'لچک‌ترنج') AS c2,  -- NULLها رد می‌شوند
  SUBSTRING('KSH-1001', 5)     AS num,   -- 1001
  LPAD(42, 6, '0')             AS code,  -- 000042
  TRIM('  فرش  ')              AS t,
  UPPER('ksh')                 AS u;</code></pre>
<p>برای شمارش طول متن فارسی همیشه <code>CHAR_LENGTH</code> را به کار ببرید؛ <code>LENGTH</code> بایت می‌شمارد و برای هر حرف فارسی ۲ برمی‌گرداند.</p>
<h3>اعداد و پول</h3>
<pre><code class="language-sql">SELECT
  ROUND(48750000, -5)            AS r,      -- 48800000 : گرد به صد هزار ریال
  TRUNCATE(123.789, 1)           AS tr,     -- 123.7
  17 DIV 5 AS q, 17 MOD 5 AS m,             -- 3 و 2
  FORMAT(480000000 / 10, 0)      AS toman;  -- '48,000,000'</code></pre>
<h3>تاریخ و زمان</h3>
<pre><code class="language-sql">SELECT
  NOW(), CURDATE(), CURRENT_TIME(),
  DATE_ADD(CURDATE(), INTERVAL 45 DAY)                  AS due_date,
  DATEDIFF('2025-06-01', '2025-03-21')                  AS days,
  TIMESTAMPDIFF(MONTH, '2024-03-20', CURDATE())         AS months,
  DATE_FORMAT(NOW(), '%Y-%m-%d %H:%i')                  AS formatted,
  LAST_DAY(CURDATE())                                   AS month_end;</code></pre>
<h3>CASE: منطق شرطی داخل کوئری</h3>
<pre><code class="language-sql">SELECT sku,
  CASE
    WHEN reeds IS NULL THEN 'نامشخص'
    WHEN reeds &gt;= 70   THEN 'ممتاز'
    WHEN reeds &gt;= 50   THEN 'خوب'
    ELSE 'معمولی'
  END AS grade,
  IF(stock &gt; 0, 'موجود', 'ناموجود') AS availability
FROM carpets
ORDER BY CASE city WHEN 'کاشان' THEN 1 WHEN 'قم' THEN 2 ELSE 3 END, sku;</code></pre>
<p>CASE اولین شاخه‌ی TRUE را برمی‌گرداند، پس شرط‌ها را از خاص به عام بنویسید. ترفند ORDER BY با CASE برای ترتیب دلخواه (نه الفبایی) بسیار کاربردی است.</p>
<h3>تاریخ شمسی</h3>
<p>MySQL تقویم جلالی ندارد. سه راه وجود دارد:</p>
<table><thead><tr><th>روش</th><th>مزیت</th><th>عیب</th></tr></thead><tbody>
<tr><td>تبدیل در برنامه (jdatetime در پایتون، verta در لاراول)</td><td>ساده، دقیق</td><td>گزارش‌گیری ماهانه‌ی شمسی در SQL سخت است</td></tr>
<tr><td>Stored Function تبدیل</td><td>در همه‌ی کوئری‌ها در دسترس</td><td>کند روی میلیون‌ها ردیف، مانع ایندکس</td></tr>
<tr><td>جدول تقویم (هر روز یک ردیف با سال و ماه شمسی)</td><td>سریع، قابل JOIN و ایندکس</td><td>یک بار ساختن جدول</td></tr>
</tbody></table>
<p>ستون‌ها را همیشه میلادی (DATE/DATETIME) ذخیره کنید و شمسی را فقط برای نمایش و گروه‌بندی بسازید. در پروژه‌ی پایانی جدول تقویم را به کار می‌گیریم.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>NOW()</code> در طول یک دستور ثابت است، اما <code>SYSDATE()</code> لحظه‌ی واقعی اجرای همان تابع را می‌دهد و با Replication مبتنی بر statement ناسازگار است؛ تقریباً همیشه NOW را بخواهید.</li>
<li><code>ROUND</code> روی DECIMAL «نیمه به دور از صفر» گرد می‌کند اما روی FLOAT و DOUBLE به کتابخانه‌ی C وابسته است و ممکن است 2.5 را 2 کند؛ یکی دیگر از دلایل DECIMAL برای پول.</li>
<li><code>FORMAT()</code> رشته برمی‌گرداند؛ مرتب‌سازی روی خروجی آن الفبایی است و '9,000' بعد از '10,000' می‌آید. فقط برای نمایش نهایی.</li>
<li>تقسیم بر صفر در SELECT فقط NULL و یک warning می‌دهد، اما در INSERT و UPDATE با sql_mode سخت‌گیر خطاست؛ برای درصدها از <code>x / NULLIF(y, 0)</code> استفاده کنید.</li>
<li><code>GROUP_CONCAT</code> به‌طور پیش‌فرض خروجی را در 1024 بایت (حدود ۵۰۰ حرف فارسی) می‌بُرد و فقط یک warning می‌دهد؛ <code>SET SESSION group_concat_max_len = 100000;</code> را فراموش نکنید.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۳ ─────────────────────────────
        {
            "title": "فصل ۳: طراحی دیتابیس — نوع داده، کلیدها و نرمال‌سازی",
            "lessons": [
                {
                    "title": "انواع عددی و متنی: INT و UNSIGNED، DECIMAL برای پول، VARCHAR با utf8mb4",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>نوع داده یک قرارداد است، نه فقط یک ظرف</h2>
<p>نوع درست ستون سه کار می‌کند: جلوی داده‌ی غلط را می‌گیرد، فضای دیسک و حافظه را کم می‌کند (ایندکس‌ها کوچک‌تر و سریع‌تر می‌شوند) و مقایسه‌ها را درست انجام می‌دهد. تغییر نوع ستون روی جدول چندمیلیونی بعداً یعنی بازسازی کل جدول؛ پس از اول درست انتخاب کنید.</p>
<h3>اعداد صحیح</h3>
<table><thead><tr><th>نوع</th><th>بایت</th><th>بازه‌ی UNSIGNED</th><th>مثال کاربرد</th></tr></thead><tbody>
<tr><td>TINYINT</td><td>1</td><td>0 تا 255</td><td>وضعیت، پرچم بولی</td></tr>
<tr><td>SMALLINT</td><td>2</td><td>0 تا 65,535</td><td>ابعاد به سانتی‌متر، تراکم شانه</td></tr>
<tr><td>MEDIUMINT</td><td>3</td><td>0 تا 16.7 میلیون</td><td>جدول‌های مرجع متوسط</td></tr>
<tr><td>INT</td><td>4</td><td>0 تا 4.29 میلیارد</td><td>شناسه‌ی اغلب جدول‌ها</td></tr>
<tr><td>BIGINT</td><td>8</td><td>0 تا 1.8×10^19</td><td>شناسه‌ی لاگ و رویداد، مبلغ ریالی به‌صورت عدد صحیح</td></tr>
</tbody></table>
<p>عدد داخل پرانتز در <code>INT(11)</code> «عرض نمایش» است، نه محدودیت؛ در MySQL 8 منسوخ شده و بی‌اثر است. <code>BOOLEAN</code> هم فقط نام دیگر <code>TINYINT(1)</code> است و مقدار 7 را هم می‌پذیرد.</p>
<h3>پول: DECIMAL، هرگز FLOAT</h3>
<pre><code class="language-sql">SELECT 0.1 + 0.2 = 0.3;                                   -- 1 (لیترال‌ها DECIMAL هستند)
SELECT CAST(0.1 AS DOUBLE) + CAST(0.2 AS DOUBLE) = 0.3;   -- 0 !

CREATE TABLE invoices (
  id         INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  amount     DECIMAL(15,0) NOT NULL,      -- ریال؛ تا 999 تریلیون
  tax_rate   DECIMAL(5,2)  NOT NULL DEFAULT 10.00,
  usd_rate   DECIMAL(12,2) NULL,          -- نرخ ارز با دو رقم اعشار
  weight_kg  FLOAT NULL                   -- اندازه‌گیری فیزیکی؛ خطای کوچک مهم نیست
);</code></pre>
<p>FLOAT و DOUBLE اعداد را به‌صورت تقریبی دودویی نگه می‌دارند؛ جمع هزاران ردیف، اختلاف چندریالی می‌سازد که حسابدار هرگز نمی‌بخشد. <code>DECIMAL(M,D)</code> دقیق است: M کل ارقام و D ارقام اعشار. برای ریال D=0 کافی است؛ اگر سیستم تومان با اعشار (مثل ۱۲٬۵۰۰٫۵) لازم دارد، ریال ذخیره کنید و در نمایش تبدیل کنید.</p>
<h3>متن: CHAR، VARCHAR و TEXT</h3>
<ul>
<li><code>VARCHAR(n)</code>: n به <strong>کاراکتر</strong> است، نه بایت. در utf8mb4 هر کاراکتر تا ۴ بایت جا می‌گیرد.</li>
<li><code>CHAR(n)</code>: طول ثابت؛ برای کدهای هم‌طول مثل کد کشور. در utf8mb4 مزیت فضایی ندارد.</li>
<li><code>TEXT</code> (64KB)، <code>MEDIUMTEXT</code> (16MB)، <code>LONGTEXT</code> (4GB): برای متن بلند؛ بیرون از ردیف اصلی ذخیره می‌شوند، پیش‌فرض ثابت (جز عبارت در پرانتز در 8.0.13 به بعد) ندارند و فقط با پیشوند ایندکس می‌شوند.</li>
</ul>
<pre><code class="language-sql">CREATE TABLE customers (
  id          INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  full_name   VARCHAR(120) NOT NULL,
  mobile      CHAR(11)     NOT NULL,         -- 09121234567 ؛ رشته، نه عدد!
  national_id CHAR(10)     NULL,             -- صفر ابتدایی حفظ می‌شود
  notes       TEXT         NULL,
  UNIQUE KEY uq_mobile (mobile)
);</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>مجموع طول همه‌ی ستون‌های VARCHAR یک ردیف (بر حسب بایت بیشینه) نباید از 65,535 بایت بگذرد؛ در utf8mb4 یعنی حدود 16,000 کاراکتر برای کل ردیف. به همین دلیل VARCHAR(20000) خطای Row size too large می‌دهد.</li>
<li>کلید ایندکس در InnoDB حداکثر 3072 بایت است؛ یعنی VARCHAR(768) در utf8mb4. ایندکس ترکیبی هم مجموع بایت‌ها را حساب می‌کند.</li>
<li>شماره‌ی موبایل، کد ملی و کد پستی را هرگز INT نکنید؛ صفر ابتدایی کد ملی حذف می‌شود و روی آن محاسبه‌ی ریاضی هم انجام نمی‌دهید.</li>
<li><code>UNSIGNED</code> روی DECIMAL و FLOAT در 8.0.17 منسوخ شده؛ برای جلوگیری از مبلغ منفی از <code>CHECK (amount &gt;= 0)</code> استفاده کنید.</li>
<li>تفریق دو ستون UNSIGNED که نتیجه‌اش منفی شود، خطای <code>BIGINT UNSIGNED value is out of range</code> می‌دهد؛ مثلاً <code>stock - reserved</code>. یکی را CAST به SIGNED کنید.</li>
</ul>""",
                },
                {
                    "title": "تاریخ و زمان، JSON و ENUM: انتخاب‌هایی با دام‌های پنهان",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>DATETIME یا TIMESTAMP؟</h2>
<table><thead><tr><th>ویژگی</th><th>DATETIME</th><th>TIMESTAMP</th></tr></thead><tbody>
<tr><td>بازه</td><td>سال 1000 تا 9999</td><td>1970 تا 2038-01-19</td></tr>
<tr><td>ذخیره</td><td>همان مقداری که داده‌اید</td><td>به UTC تبدیل و هنگام خواندن به time_zone اتصال برگردانده می‌شود</td></tr>
<tr><td>فضا</td><td>5 بایت (+ کسر ثانیه)</td><td>4 بایت (+ کسر ثانیه)</td></tr>
<tr><td>مناسب برای</td><td>تاریخ تحویل، تولد، قرارداد</td><td>لحظه‌ی رویداد در سیستم‌های چندمنطقه‌ای (تا پیش از 2038)</td></tr>
</tbody></table>
<p><strong>مسئله‌ی 2038:</strong> TIMESTAMP عدد ثانیه از 1970 در ۳۲ بیت است و در 19 ژانویه‌ی 2038 سرریز می‌شود. قراردادهای اجاره‌ی ۱۵ساله یا اقساط بلندمدت همین حالا به آن برخورد می‌کنند. توصیه‌ی عملی: DATETIME استفاده کنید و قرار بگذارید همه‌ی مقادیر به UTC (یا همه به وقت تهران) ذخیره شوند؛ جنگو با <code>USE_TZ = True</code> خودش UTC ذخیره می‌کند.</p>
<pre><code class="language-sql">CREATE TABLE orders (
  id          BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  created_at  DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
  updated_at  DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3)
                          ON UPDATE CURRENT_TIMESTAMP(3),
  deliver_on  DATE NULL
);

SET time_zone = '+00:00';  SELECT NOW();
SET time_zone = '+03:30';  SELECT NOW();   -- NOW تحت تأثیر time_zone اتصال است</code></pre>
<h3>JSON: انعطاف با حساب و کتاب</h3>
<p>نوع JSON در MySQL به شکل دودویی و اعتبارسنجی‌شده ذخیره می‌شود. برای ویژگی‌های متغیر محصول (رنگ زمینه، رنگ حاشیه، نوع نخ) که برای هر دسته فرق دارد مناسب است؛ برای داده‌ای که در WHERE و JOIN مرتب استفاده می‌شود، ستون معمولی بهتر است.</p>
<pre><code class="language-sql">ALTER TABLE carpets ADD attrs JSON NULL;
UPDATE carpets SET attrs = JSON_OBJECT('field_color', 'لاکی', 'yarn', 'پشم', 'colors', 8)
WHERE sku = 'KSH-1001';

SELECT sku, attrs-&gt;&gt;'$.field_color' AS field_color      -- -&gt;&gt; یعنی مقدار بدون کوتیشن
FROM carpets WHERE attrs-&gt;&gt;'$.yarn' = 'پشم';

-- ایندکس روی یک کلید JSON با ستون تولیدشده
ALTER TABLE carpets
  ADD field_color VARCHAR(30) AS (attrs-&gt;&gt;'$.field_color') VIRTUAL,
  ADD INDEX ix_field_color (field_color);</code></pre>
<h3>ENUM: راحت، اما سفت</h3>
<p><code>ENUM('draft','paid','shipped')</code> فضای کمی می‌گیرد و مقدار نامعتبر را (در حالت strict) رد می‌کند، اما:</p>
<ul>
<li>درونی به‌صورت شماره‌ی ترتیب ذخیره می‌شود و <code>ORDER BY status</code> بر اساس ترتیب تعریف مرتب می‌کند، نه الفبا.</li>
<li>افزودن مقدار به <em>انتهای</em> فهرست سریع است، اما درج در وسط یا تغییر نام، کل جدول را بازسازی می‌کند.</li>
<li>در حالت غیر strict مقدار نامعتبر به رشته‌ی خالی با اندیس 0 تبدیل می‌شود.</li>
</ul>
<p>جایگزین منعطف‌تر: <code>VARCHAR(20)</code> با <code>CHECK (status IN (...))</code> یا یک جدول مرجع کوچک با کلید خارجی.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>برای TIMESTAMP با نام منطقه (مثل <code>'Asia/Tehran'</code>) باید جدول‌های timezone در دیتابیس mysql بارگذاری شده باشد: <code>mysql_tzinfo_to_sql /usr/share/zoneinfo | mysql -u root -p mysql</code>. image رسمی داکر این کار را هنگام راه‌اندازی اول خودش انجام می‌دهد.</li>
<li>از 8.0.19 می‌توانید در لیترال زمان، offset بدهید: <code>'2025-03-21 10:00:00+03:30'</code>؛ MySQL آن را به time_zone اتصال تبدیل می‌کند.</li>
<li>مقایسه‌ی <code>attrs-&gt;'$.colors' = 8</code> با <code>attrs-&gt;&gt;'$.colors' = '8'</code> فرق دارد؛ اولی مقایسه‌ی JSON و دومی مقایسه‌ی رشته است. در ایندکس و WHERE یکی را انتخاب و همه‌جا رعایت کنید.</li>
<li>ایندکس چندمقداری (8.0.17) روی آرایه‌ی JSON: <code>INDEX ((CAST(attrs-&gt;'$.tags' AS CHAR(30) ARRAY)))</code> و جست‌وجو با <code>MEMBER OF</code> یا <code>JSON_CONTAINS</code>.</li>
<li>در MariaDB نوع JSON فقط LONGTEXT با CHECK اعتبارسنجی است و عملگر <code>-&gt;&gt;</code> ندارد؛ کد مشترک باید از <code>JSON_UNQUOTE(JSON_EXTRACT(...))</code> استفاده کند.</li>
</ul>""",
                },
                {
                    "title": "کلید اصلی: AUTO_INCREMENT، UUID و اهمیت ترتیب درج",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>کلید اصلی در InnoDB فقط یک شناسه نیست</h2>
<p>در InnoDB جدول <em>خودش</em> یک B-Tree است که بر اساس کلید اصلی مرتب شده (clustered index، فصل پنجم). یعنی کلید اصلی ترتیب فیزیکی ذخیره‌ی ردیف‌ها را تعیین می‌کند و در تک‌تک ایندکس‌های دیگر هم کپی می‌شود. سه پیامد مستقیم:</p>
<ol>
<li>کلید اصلی کوچک یعنی همه‌ی ایندکس‌ها کوچک‌تر.</li>
<li>کلید صعودی (AUTO_INCREMENT) یعنی درج همیشه در انتهای درخت؛ سریع و بدون شکافتن صفحه.</li>
<li>کلید تصادفی (UUID نسخه‌ی ۴) یعنی درج در وسط درخت؛ page split، تکه‌تکه شدن و افت شدید سرعت درج در جدول‌های بزرگ.</li>
</ol>
<h3>AUTO_INCREMENT</h3>
<pre><code class="language-sql">CREATE TABLE order_items (
  id        BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  order_id  BIGINT UNSIGNED NOT NULL,
  carpet_id INT UNSIGNED    NOT NULL,
  qty       SMALLINT UNSIGNED NOT NULL
);

SHOW TABLE STATUS LIKE 'order_items'\G         -- مقدار Auto_increment بعدی
ALTER TABLE order_items AUTO_INCREMENT = 100000; -- شروع از عدد دلخواه</code></pre>
<p>شماره‌ها <strong>شکاف</strong> دارند و این طبیعی است: تراکنش ROLLBACK‌شده، INSERT IGNORE یا upsert، شماره را مصرف می‌کنند و پس نمی‌دهند. هرگز از id برای «شماره‌ی فاکتور پشت‌سرهم» استفاده نکنید؛ شماره‌ی فاکتور رسمی را با جدول شمارنده و قفل (فصل ششم) بسازید.</p>
<h3>UUID: وقتی لازم است، درستش را بسازید</h3>
<p>UUID وقتی مفید است که شناسه باید قبل از درج در کلاینت یا چند سرور مستقل ساخته شود، یا نباید قابل حدس باشد (در URL). راه درست در MySQL:</p>
<pre><code class="language-sql">CREATE TABLE devices (
  id    BINARY(16) PRIMARY KEY,           -- 16 بایت، نه CHAR(36) با 144 بایت در utf8mb4
  name  VARCHAR(80) NOT NULL
);

-- UUID() در MySQL نسخه‌ی ۱ (مبتنی بر زمان) است؛ آرگومان 1 بخش زمان را جلو می‌آورد تا صعودی شود
INSERT INTO devices VALUES (UUID_TO_BIN(UUID(), 1), 'دستگاه بافندگی ۳');

SELECT BIN_TO_UUID(id, 1) AS id, name FROM devices;</code></pre>
<p>اگر UUID در برنامه ساخته می‌شود، نسخه‌ی ۷ (UUIDv7) را انتخاب کنید که ذاتاً بر اساس زمان مرتب است و مشکل درج تصادفی را ندارد. الگوی رایج دیگر: کلید اصلی داخلی BIGINT AUTO_INCREMENT و یک ستون UNIQUE جدا برای شناسه‌ی عمومی.</p>
<h3>کلید طبیعی یا جانشین؟</h3>
<table><thead><tr><th>نوع</th><th>مثال</th><th>ملاحظه</th></tr></thead><tbody>
<tr><td>طبیعی</td><td>کد ملی، SKU</td><td>معنادار است اما ممکن است عوض شود یا اشتباه وارد شده باشد</td></tr>
<tr><td>جانشین</td><td>AUTO_INCREMENT</td><td>پایدار و کوچک؛ کلید طبیعی را با UNIQUE حفظ کنید</td></tr>
<tr><td>ترکیبی</td><td>(order_id, carpet_id) در جدول واسط</td><td>برای جدول‌های رابطه‌ی چندبه‌چند عالی است</td></tr>
</tbody></table>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>تا قبل از 8.0، شمارنده‌ی AUTO_INCREMENT پس از ری‌استارت به max(id)+1 برمی‌گشت و idهای حذف‌شده‌ی آخر دوباره استفاده می‌شدند؛ از 8.0 مقدار آن ماندگار است.</li>
<li>جدول InnoDB بدون کلید اصلی و بدون UNIQUE NOT NULL، یک کلید پنهان ۶بایتی می‌گیرد که بین همه‌ی این جدول‌ها یک شمارنده‌ی سراسری مشترک دارد؛ هم کند است و هم Replication ردیفی را بسیار کند می‌کند.</li>
<li>متغیر <code>sql_require_primary_key = ON</code> ساخت جدول بدون کلید اصلی را ممنوع می‌کند؛ بسیاری از سرویس‌های دیتابیس ابری آن را روشن دارند و مایگریشن‌های قدیمی را می‌شکنند.</li>
<li>از 8.0.30 با <code>sql_generate_invisible_primary_key = ON</code>، MySQL برای جدول بی‌کلید خودش یک ستون نامرئی <code>my_row_id</code> می‌سازد.</li>
<li>INT UNSIGNED حدود ۴٫۳ میلیارد مقدار دارد؛ برای جدول لاگ و رویداد از اول BIGINT بگذارید، چون تبدیل بعدی روی جدول میلیاردی یعنی ساعت‌ها بازسازی.</li>
</ul>""",
                },
                {
                    "title": "کلید خارجی، ON DELETE و CHECK constraint",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>بگذارید دیتابیس از داده دفاع کند</h2>
<p>برنامه‌ها عوض می‌شوند، اسکریپت‌های ایمپورت دستی نوشته می‌شوند و کسی مستقیم در DBeaver ردیف پاک می‌کند. قیدها (constraints) آخرین خط دفاع‌اند: سفارشی بدون مشتری، قلم سفارشی با تعداد منفی یا تخفیف بیش از صد درصد اصلاً نباید قابل ذخیره باشد.</p>
<h3>کلید خارجی</h3>
<pre><code class="language-sql">CREATE TABLE customers (
  id        INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  full_name VARCHAR(120) NOT NULL
);

CREATE TABLE orders (
  id          BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  customer_id INT UNSIGNED NOT NULL,
  status      VARCHAR(20)  NOT NULL DEFAULT 'draft',
  discount    DECIMAL(5,2) NOT NULL DEFAULT 0,
  created_at  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_orders_customer FOREIGN KEY (customer_id)
    REFERENCES customers (id) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT chk_orders_status CHECK (status IN ('draft','paid','weaving','shipped','cancelled')),
  CONSTRAINT chk_orders_discount CHECK (discount BETWEEN 0 AND 100)
);

INSERT INTO orders (customer_id) VALUES (999);
-- ERROR 1452: Cannot add or update a child row: a foreign key constraint fails
INSERT INTO orders (customer_id, discount) VALUES (1, 120);
-- ERROR 3819: Check constraint 'chk_orders_discount' is violated.</code></pre>
<h3>رفتار هنگام حذف والد</h3>
<table><thead><tr><th>گزینه</th><th>رفتار</th><th>مثال مناسب</th></tr></thead><tbody>
<tr><td><code>RESTRICT</code> / <code>NO ACTION</code></td><td>حذف والد دارای فرزند خطا می‌دهد (ERROR 1451)؛ در InnoDB این دو یکسان‌اند</td><td>مشتری دارای سفارش</td></tr>
<tr><td><code>CASCADE</code></td><td>فرزندان هم حذف می‌شوند</td><td>اقلام یک سفارش پیش‌نویس</td></tr>
<tr><td><code>SET NULL</code></td><td>ستون فرزند NULL می‌شود (باید NULLپذیر باشد)</td><td>بازاریاب معرف که از سیستم رفته</td></tr>
</tbody></table>
<p>برای داده‌ی مالی CASCADE را با احتیاط به کار ببرید؛ یک DELETE اشتباه روی مشتری نباید تاریخچه‌ی فروش را پاک کند. در سیستم‌های تجاری به‌جای حذف، معمولاً «حذف نرم» (ستون <code>is_active</code> یا <code>deleted_at</code>) انجام می‌شود.</p>
<h3>شرط‌های لازم برای ساخت کلید خارجی</h3>
<ul>
<li>هر دو جدول InnoDB باشند.</li>
<li>نوع ستون‌ها <em>دقیقاً</em> یکسان باشد: INT با INT UNSIGNED سازگار نیست (ERROR 3780).</li>
<li>ستون والد کلید اصلی یا دارای ایندکس UNIQUE باشد.</li>
<li>charset و collation ستون‌های متنی یکسان باشد.</li>
</ul>
<h3>ورود داده‌ی حجیم</h3>
<pre><code class="language-sql">SET FOREIGN_KEY_CHECKS = 0;   -- فقط در همین نشست
SOURCE big_import.sql;
SET FOREIGN_KEY_CHECKS = 1;   -- داده‌ی واردشده دوباره بررسی نمی‌شود!

-- پیدا کردن یتیم‌ها پس از ورود
SELECT o.id FROM orders o LEFT JOIN customers c ON c.id = o.customer_id WHERE c.id IS NULL;</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>حذف و به‌روزرسانی‌هایی که با CASCADE روی جدول فرزند انجام می‌شوند، Triggerهای جدول فرزند را اجرا <em>نمی‌کنند</em>؛ اگر لاگ حسابرسی را با Trigger می‌سازید، این حذف‌ها در لاگ نمی‌آیند.</li>
<li>InnoDB برای ستون کلید خارجی اگر ایندکس نباشد خودش یکی می‌سازد؛ بدون این ایندکس، هر حذف والد به اسکن کامل جدول فرزند و قفل‌های گسترده منجر می‌شد.</li>
<li>تا نسخه‌ی 8.0.15، CHECK خوانده و بی‌صدا نادیده گرفته می‌شد؛ جدولی که در آن نسخه‌ها ساخته شده، قید را ندارد. با <code>SHOW CREATE TABLE</code> مطمئن شوید.</li>
<li>CHECK نمی‌تواند به جدول دیگر، زیرکوئری یا توابع غیرقطعی مثل <code>NOW()</code> ارجاع دهد؛ برای «تاریخ تحویل بعد از امروز» از منطق برنامه یا Trigger استفاده کنید.</li>
<li>با <code>ALTER TABLE orders ALTER CHECK chk_orders_discount NOT ENFORCED;</code> می‌توانید قید را موقتاً غیرفعال کنید بدون اینکه تعریفش را از دست بدهید.</li>
</ul>""",
                },
                {
                    "title": "نرمال‌سازی ۱NF تا ۳NF و طراحی دیتابیس فروشگاه فرش",
                    "kind": "text",
                    "minutes": 26,
                    "is_preview": False,
                    "body": r"""<h2>از یک جدول اکسلی تا یک مدل درست</h2>
<p>بیشتر دیتابیس‌های مشکل‌دار از یک «جدول اکسل بزرگ» شروع شده‌اند: هر ردیف یک فروش، با نام مشتری، تلفن، نام فرش، قیمت و شهر بافت. نرمال‌سازی یعنی هر واقعیت فقط <strong>یک جا</strong> ذخیره شود تا تغییرش هم یک جا باشد.</p>
<h3>سه قدم اول</h3>
<table><thead><tr><th>فرم</th><th>قاعده</th><th>نقض رایج</th></tr></thead><tbody>
<tr><td>1NF</td><td>هر خانه یک مقدار اتمی؛ بدون گروه تکرارشونده</td><td>ستون <code>items</code> با مقدار «فرش۱،فرش۲» یا ستون‌های item1، item2، item3</td></tr>
<tr><td>2NF</td><td>در کلید ترکیبی، هر ستون به <em>کل</em> کلید وابسته باشد</td><td>در order_items با کلید (order_id, carpet_id)، ستون carpet_title فقط به carpet_id وابسته است</td></tr>
<tr><td>3NF</td><td>ستون غیرکلیدی به ستون غیرکلیدی دیگر وابسته نباشد</td><td>در customers، ستون province از city به دست می‌آید</td></tr>
</tbody></table>
<p>نتیجه‌ی ناهنجاری‌ها: تلفن مشتری در ۴۰ ردیف تکرار شده و بعد از تغییر شماره فقط ۳۹ تا اصلاح می‌شود (ناهنجاری به‌روزرسانی)؛ نمی‌توان فرش جدیدی را قبل از اولین فروش ثبت کرد (ناهنجاری درج)؛ با حذف تنها فروش یک مشتری، خود مشتری هم گم می‌شود (ناهنجاری حذف).</p>
<h3>طراحی: فروشگاه فرش</h3>
<pre><code class="language-sql">CREATE TABLE cities (
  id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(40) NOT NULL, province VARCHAR(40) NOT NULL,
  UNIQUE KEY uq_city (province, name)
);

CREATE TABLE customers (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  full_name VARCHAR(120) NOT NULL,
  mobile CHAR(11) NOT NULL UNIQUE,
  city_id SMALLINT UNSIGNED NULL,
  FOREIGN KEY (city_id) REFERENCES cities (id)
);

CREATE TABLE designs (                         -- نقشه/طرح: لچک‌ترنج، افشان، هریس
  id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(60) NOT NULL UNIQUE
);

CREATE TABLE products (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  sku VARCHAR(20) NOT NULL UNIQUE,
  title VARCHAR(150) NOT NULL,
  design_id SMALLINT UNSIGNED NOT NULL,
  reeds SMALLINT UNSIGNED NULL,
  width_cm SMALLINT UNSIGNED NOT NULL, length_cm SMALLINT UNSIGNED NOT NULL,
  list_price DECIMAL(15,0) NOT NULL CHECK (list_price &gt;= 0),
  FOREIGN KEY (design_id) REFERENCES designs (id)
);

CREATE TABLE orders (
  id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  customer_id INT UNSIGNED NOT NULL,
  status VARCHAR(20) NOT NULL DEFAULT 'draft',
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  total_amount DECIMAL(15,0) NOT NULL DEFAULT 0,   -- دنرمال‌سازی آگاهانه
  FOREIGN KEY (customer_id) REFERENCES customers (id),
  INDEX ix_orders_status_created (status, created_at)
);

CREATE TABLE order_items (
  order_id BIGINT UNSIGNED NOT NULL,
  product_id INT UNSIGNED NOT NULL,
  qty SMALLINT UNSIGNED NOT NULL CHECK (qty &gt; 0),
  unit_price DECIMAL(15,0) NOT NULL,               -- قیمت در لحظه‌ی فروش
  PRIMARY KEY (order_id, product_id),
  FOREIGN KEY (order_id) REFERENCES orders (id) ON DELETE CASCADE,
  FOREIGN KEY (product_id) REFERENCES products (id)
);</code></pre>
<h3>دنرمال‌سازی آگاهانه</h3>
<p>ستون <code>total_amount</code> از روی اقلام قابل محاسبه است، پس از نظر نظری تکراری است. اما فهرست سفارش‌ها با جمع مبلغ روزی هزاران بار خوانده می‌شود و محاسبه‌ی آن با JOIN و SUM گران است. این یک <em>تصمیم</em> است، نه تنبلی: باید سازوکار همگام‌سازی داشته باشد (در یک تراکنش با درج اقلام، یا Trigger) و گاهی با یک کوئری بررسی شود که با جمع واقعی می‌خواند.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>unit_price</code> در order_items تکرار قیمت محصول <em>نیست</em>؛ یک واقعیت تاریخی است («این فرش به این قیمت فروخته شد»). اگر آن را از products بخوانید، با هر تغییر قیمت فاکتورهای قدیمی عوض می‌شوند.</li>
<li>آدرس ارسال هم همین‌طور است: آدرس را هنگام ثبت سفارش در خود سفارش کپی کنید؛ مشتری ممکن است فردا اسباب‌کشی کند.</li>
<li>برای ویژگی‌های متغیر، الگوی EAV (جدول attribute/value) معمولاً به کوئری‌های کابوس‌وار می‌رسد؛ در MySQL 8 یک ستون JSON با ستون تولیدشده‌ی ایندکس‌دار اغلب انتخاب بهتری است.</li>
<li>در جدول واسط، ترتیب ستون‌های کلید اصلی ترکیبی مهم است: <code>(order_id, product_id)</code> پرس‌وجوی «اقلام یک سفارش» را سریع می‌کند، و برای «سفارش‌های یک محصول» ایندکس جدا روی product_id لازم است (کلید خارجی خودش آن را می‌سازد).</li>
<li>نام‌گذاری یکدست (جمع برای جدول، <code>_id</code> برای کلید خارجی، snake_case) را از روز اول قانون کنید؛ MySQL روی لینوکس به بزرگی و کوچکی نام جدول حساس است و روی ویندوز نیست (<code>lower_case_table_names</code>).</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۴ ─────────────────────────────
        {
            "title": "فصل ۴: کوئری پیشرفته — JOIN، تجمیع، CTE و Window Function",
            "lessons": [
                {
                    "title": "JOINها از INNER تا شبیه‌سازی FULL OUTER، و UNION",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>ترکیب جدول‌ها</h2>
<p>قدرت مدل رابطه‌ای در JOIN است: داده‌ای که نرمال‌سازی آن را در چند جدول پخش کرده، هنگام خواندن دوباره کنار هم قرار می‌گیرد. در این فصل از طرح فروشگاه فرش فصل قبل استفاده می‌کنیم.</p>
<pre><code class="language-sql">-- INNER JOIN: فقط سفارش‌هایی که مشتری دارند (یعنی همه، به لطف FK)
SELECT o.id, c.full_name, o.total_amount
FROM orders AS o
JOIN customers AS c ON c.id = o.customer_id
WHERE o.status = 'paid';

-- LEFT JOIN: همه‌ی مشتری‌ها، حتی بدون سفارش
SELECT c.full_name, COUNT(o.id) AS orders_count
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
GROUP BY c.id, c.full_name;

-- anti-join: مشتری‌هایی که هرگز خرید نکرده‌اند
SELECT c.id, c.full_name
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
WHERE o.id IS NULL;</code></pre>
<h3>بزرگ‌ترین دام LEFT JOIN: شرط در ON یا در WHERE؟</h3>
<pre><code class="language-sql">-- می‌خواهیم همه‌ی مشتری‌ها + تعداد سفارش‌های پرداخت‌شده
-- غلط: WHERE ردیف‌های NULL را حذف می‌کند و LEFT عملاً INNER می‌شود
SELECT c.full_name, COUNT(o.id)
FROM customers c LEFT JOIN orders o ON o.customer_id = c.id
WHERE o.status = 'paid'
GROUP BY c.id, c.full_name;

-- درست: شرط روی جدول سمت راست داخل ON
SELECT c.full_name, COUNT(o.id)
FROM customers c LEFT JOIN orders o ON o.customer_id = c.id AND o.status = 'paid'
GROUP BY c.id, c.full_name;</code></pre>
<p>قاعده: شرط‌های جدول سمت «اختیاری» (راست در LEFT JOIN) را در ON بگذارید؛ شرط‌های جدول اصلی در WHERE.</p>
<h3>انواع دیگر</h3>
<table><thead><tr><th>نوع</th><th>نتیجه</th></tr></thead><tbody>
<tr><td><code>RIGHT JOIN</code></td><td>قرینه‌ی LEFT؛ در عمل بهتر است جدول‌ها را جابه‌جا و LEFT بنویسید</td></tr>
<tr><td><code>CROSS JOIN</code></td><td>ضرب دکارتی؛ مثلاً همه‌ی ترکیب‌های «طرح × اندازه» برای ساخت کاتالوگ</td></tr>
<tr><td>Self join</td><td>جدول با خودش؛ مثلاً کارمند و سرپرست در یک جدول</td></tr>
<tr><td><code>FULL OUTER JOIN</code></td><td>در MySQL وجود ندارد؛ باید شبیه‌سازی شود</td></tr>
</tbody></table>
<h3>شبیه‌سازی FULL OUTER JOIN با UNION</h3>
<p>فرض کنید موجودی انبار (<code>stock_counts</code>) و فهرست محصولات را مقایسه می‌کنیم و هم محصولات بی‌شمارش و هم شمارش‌های بی‌محصول را می‌خواهیم:</p>
<pre><code class="language-sql">SELECT p.sku, s.qty
FROM products p LEFT JOIN stock_counts s ON s.sku = p.sku
UNION ALL
SELECT s.sku, s.qty
FROM products p RIGHT JOIN stock_counts s ON s.sku = p.sku
WHERE p.sku IS NULL;</code></pre>
<p>بخش دوم فقط ردیف‌هایی را می‌آورد که در بخش اول نبوده‌اند، پس <code>UNION ALL</code> کافی و سریع‌تر از <code>UNION</code> است. <code>UNION</code> ساده تکراری‌ها را حذف می‌کند و برای این کار باید نتیجه را مرتب یا هش کند.</p>
<h3>INTERSECT و EXCEPT</h3>
<pre><code class="language-sql">-- MySQL 8.0.31 به بعد: مشتری‌هایی که هم در ۱۴۰۲ و هم در ۱۴۰۳ خرید کرده‌اند
SELECT customer_id FROM orders WHERE created_at &gt;= '2023-03-21' AND created_at &lt; '2024-03-20'
INTERSECT
SELECT customer_id FROM orders WHERE created_at &gt;= '2024-03-20' AND created_at &lt; '2025-03-21';</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>در MySQL، <code>JOIN</code> بدون ON و <code>CROSS JOIN</code> و کاما، همگی ضرب دکارتی‌اند؛ یک ON فراموش‌شده روی دو جدول ده‌هزارتایی، صد میلیون ردیف می‌سازد.</li>
<li>JOIN روی ستون‌هایی با نوع یا collation متفاوت (مثلاً INT در یک طرف و VARCHAR در طرف دیگر) جلوی استفاده از ایندکس را می‌گیرد؛ در EXPLAIN نوع <code>ALL</code> می‌بینید.</li>
<li><code>USING (customer_id)</code> وقتی نام ستون در هر دو جدول یکی است کوتاه‌تر از ON است و ستون را فقط یک بار در <code>SELECT *</code> برمی‌گرداند.</li>
<li>ترتیب نوشتن جدول‌ها در INNER JOIN بر عملکرد اثری ندارد؛ بهینه‌ساز ترتیب را خودش انتخاب می‌کند. <code>STRAIGHT_JOIN</code> این انتخاب را لغو می‌کند؛ فقط آخرین راه‌حل.</li>
<li>نام ستون‌های خروجی UNION از SELECT <em>اول</em> گرفته می‌شود و ستون‌ها فقط بر اساس جایگاه جفت می‌شوند؛ اگر در بخش دوم ترتیب ستون‌ها را جابه‌جا بنویسید، MySQL خطا نمی‌دهد و داده بی‌صدا زیر عنوان اشتباه می‌نشیند.</li>
</ul>""",
                },
                {
                    "title": "GROUP BY، HAVING، ONLY_FULL_GROUP_BY و گزارش‌های تجمیعی",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>از ردیف‌ها به گزارش</h2>
<p>توابع تجمیعی (<code>COUNT</code>، <code>SUM</code>، <code>AVG</code>، <code>MIN</code>، <code>MAX</code>، <code>GROUP_CONCAT</code>) چند ردیف را به یک مقدار تبدیل می‌کنند و GROUP BY تعیین می‌کند که گروه‌ها چطور ساخته شوند.</p>
<pre><code class="language-sql">SELECT d.name AS design,
       COUNT(*)                 AS items,
       SUM(oi.qty)              AS carpets_sold,
       SUM(oi.qty * oi.unit_price) AS revenue_rial,
       ROUND(AVG(oi.unit_price))   AS avg_price
FROM order_items oi
JOIN products p ON p.id = oi.product_id
JOIN designs  d ON d.id = p.design_id
JOIN orders   o ON o.id = oi.order_id
WHERE o.status IN ('paid', 'shipped')               -- فیلتر ردیف‌ها، قبل از گروه‌بندی
GROUP BY d.id, d.name
HAVING SUM(oi.qty) &gt;= 10                           -- فیلتر گروه‌ها، بعد از گروه‌بندی
ORDER BY revenue_rial DESC;</code></pre>
<p>هر شرطی که می‌تواند در WHERE باشد، در WHERE بگذارید؛ HAVING بعد از ساختن همه‌ی گروه‌ها اجرا می‌شود و از ایندکس برای حذف زودهنگام ردیف‌ها کمکی نمی‌گیرد.</p>
<h3>ONLY_FULL_GROUP_BY</h3>
<pre><code class="language-sql">SELECT customer_id, created_at, SUM(total_amount)
FROM orders GROUP BY customer_id;
-- ERROR 1055: Expression #2 of SELECT list is not in GROUP BY clause
-- and contains nonaggregated column 'orders.created_at'...</code></pre>
<p>MySQL قدیمی این کوئری را اجرا می‌کرد و برای created_at یک مقدار <em>تصادفی</em> از گروه برمی‌گرداند؛ نتیجه‌ای که امروز درست به نظر می‌رسید و فردا عوض می‌شد. از 5.7 حالت <code>ONLY_FULL_GROUP_BY</code> پیش‌فرض است. راه‌حل‌ها:</p>
<ul>
<li>ستون را تجمیع کنید: <code>MAX(created_at) AS last_order</code>.</li>
<li>اگر ستون به کلید گروه وابستگی تابعی دارد، MySQL خودش می‌فهمد: <code>GROUP BY c.id</code> و انتخاب <code>c.full_name</code> مجاز است، چون id کلید اصلی customers است.</li>
<li>اگر واقعاً فرقی نمی‌کند کدام مقدار بیاید: <code>ANY_VALUE(col)</code>.</li>
</ul>
<h3>جدول محوری (Pivot) با تجمیع شرطی</h3>
<pre><code class="language-sql">SELECT YEAR(o.created_at) AS y,
  SUM(CASE WHEN o.status = 'paid'      THEN 1 ELSE 0 END) AS paid,
  SUM(o.status = 'shipped')                               AS shipped,   -- کوتاه‌نویسی MySQL
  SUM(o.status = 'cancelled')                             AS cancelled
FROM orders o
GROUP BY y;</code></pre>
<p>در MySQL عبارت منطقی مقدار 1 یا 0 دارد، پس <code>SUM(شرط)</code> تعداد ردیف‌های صادق را می‌شمارد.</p>
<h3>جمع جزء و کل با ROLLUP</h3>
<pre><code class="language-sql">SELECT IF(GROUPING(ci.province), 'جمع کل', ci.province) AS province,
       IF(GROUPING(ci.name), 'جمع استان', ci.name)     AS city,
       COUNT(*) AS customers
FROM customers c JOIN cities ci ON ci.id = c.city_id
GROUP BY ci.province, ci.name WITH ROLLUP;</code></pre>
<p>تابع <code>GROUPING()</code> (از 8.0) تشخیص می‌دهد NULL خروجی از ROLLUP آمده یا مقدار واقعی NULL است.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>از MySQL 8، GROUP BY دیگر نتیجه را به‌طور ضمنی مرتب نمی‌کند؛ گزارش‌هایی که به این رفتار 5.7 تکیه کرده بودند بعد از ارتقا نامرتب می‌شوند. همیشه ORDER BY صریح بنویسید.</li>
<li><code>COUNT(*)</code> و <code>COUNT(1)</code> در InnoDB هیچ فرقی ندارند؛ اما <code>COUNT(col)</code> ردیف‌های NULL را نمی‌شمارد و معنای دیگری دارد.</li>
<li><code>COUNT(*)</code> بدون WHERE روی جدول InnoDB بزرگ کند است، چون InnoDB (برخلاف MyISAM) تعداد ردیف را جایی نگه نمی‌دارد؛ برای عدد تقریبی از <code>information_schema.tables.table_rows</code> استفاده کنید.</li>
<li><code>AVG</code> ردیف‌های NULL را نادیده می‌گیرد؛ میانگین تخفیف با NULL به‌جای صفر، عدد بزرگ‌تری از واقعیت نشان می‌دهد. <code>AVG(COALESCE(discount, 0))</code>.</li>
<li><code>COUNT(DISTINCT a, b)</code> در MySQL مجاز است و ترکیب‌های یکتا را می‌شمارد؛ ولی ترکیب‌هایی که یکی از اجزایشان NULL است شمرده نمی‌شوند.</li>
</ul>""",
                },
                {
                    "title": "زیرکوئری، EXISTS، Derived Table، LATERAL و View",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>کوئری داخل کوئری</h2>
<p>زیرکوئری می‌تواند یک مقدار (scalar)، یک فهرست (برای IN)، یک «وجود دارد یا نه» (EXISTS) یا یک جدول موقت (derived table) برگرداند.</p>
<pre><code class="language-sql">-- scalar: محصولات گران‌تر از میانگین
SELECT sku, list_price FROM products
WHERE list_price &gt; (SELECT AVG(list_price) FROM products);

-- EXISTS: مشتری‌هایی که دست‌کم یک سفارش بالای ۵۰۰ میلیون ریال دارند
SELECT c.id, c.full_name FROM customers c
WHERE EXISTS (
  SELECT 1 FROM orders o
  WHERE o.customer_id = c.id AND o.total_amount &gt; 500000000
);</code></pre>
<p>زیرکوئری دوم «هم‌بسته» (correlated) است: به ستون کوئری بیرونی (<code>c.id</code>) ارجاع می‌دهد. EXISTS به محض پیدا کردن اولین ردیف متوقف می‌شود و مهم نیست داخلش چه چیزی SELECT کنید.</p>
<h3>NOT IN در برابر NOT EXISTS</h3>
<pre><code class="language-sql">-- محصولاتی که هرگز فروش نرفته‌اند
SELECT p.sku FROM products p
WHERE NOT EXISTS (SELECT 1 FROM order_items oi WHERE oi.product_id = p.id);</code></pre>
<p>اگر ستون زیرکوئری NULL داشته باشد، <code>NOT IN</code> برای همه‌ی ردیف‌ها UNKNOWN می‌شود و نتیجه خالی می‌آید. NOT EXISTS این مشکل را ندارد و MySQL 8 آن را به anti-join بهینه تبدیل می‌کند.</p>
<h3>Derived table و LATERAL</h3>
<pre><code class="language-sql">-- derived table: میانگین خرید هر مشتری، سپس فقط مشتری‌های بالای میانگین کل
SELECT t.customer_id, t.spent
FROM (SELECT customer_id, SUM(total_amount) AS spent
      FROM orders GROUP BY customer_id) AS t
WHERE t.spent &gt; 1000000000;

-- LATERAL (8.0.14+): سه سفارش آخر هر مشتری
SELECT c.full_name, last3.id, last3.created_at
FROM customers c
JOIN LATERAL (
  SELECT o.id, o.created_at FROM orders o
  WHERE o.customer_id = c.id
  ORDER BY o.created_at DESC LIMIT 3
) AS last3 ON TRUE;</code></pre>
<p>derived table معمولی نمی‌تواند به جدول‌های کنارش ارجاع دهد؛ LATERAL این اجازه را می‌دهد و برای «N ردیف آخر هر گروه» با ایندکس <code>(customer_id, created_at)</code> بسیار سریع است.</p>
<h3>View: کوئری نام‌دار</h3>
<pre><code class="language-sql">CREATE OR REPLACE VIEW v_order_summary AS
SELECT o.id, o.created_at, o.status, c.full_name, c.mobile, o.total_amount
FROM orders o JOIN customers c ON c.id = o.customer_id;

SELECT * FROM v_order_summary WHERE status = 'paid' ORDER BY created_at DESC LIMIT 20;

-- View قابل به‌روزرسانی با محافظ
CREATE VIEW v_draft_orders AS
SELECT id, customer_id, status FROM orders WHERE status = 'draft'
WITH CHECK OPTION;   -- UPDATE که ردیف را از شرط View بیرون ببرد رد می‌شود</code></pre>
<p>View داده ذخیره نمی‌کند (MySQL «Materialized View» ندارد). مزیتش پنهان کردن پیچیدگی و محدود کردن دسترسی است: می‌توانید به کاربر گزارش‌گیر فقط روی View دسترسی بدهید و ستون‌های حساس را نشان ندهید.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>SELECT *</code> در تعریف View هنگام ساخت به فهرست ثابت ستون‌ها تبدیل می‌شود؛ ستون‌هایی که بعداً به جدول اضافه کنید در View نمی‌آیند تا View را دوباره بسازید.</li>
<li>View با ALGORITHM=MERGE در کوئری بیرونی ادغام می‌شود و از ایندکس‌ها استفاده می‌کند؛ اما اگر GROUP BY، DISTINCT، UNION یا LIMIT داشته باشد به TEMPTABLE تبدیل می‌شود و فیلتر بیرونی بعد از ساخت کل نتیجه اعمال می‌شود.</li>
<li>View به‌طور پیش‌فرض با <code>SQL SECURITY DEFINER</code> ساخته می‌شود؛ اگر کاربر سازنده حذف شود، View با خطای «The user specified as a definer does not exist» از کار می‌افتد — دردسر رایج بعد از انتقال بکاپ به سرور دیگر.</li>
<li>زیرکوئری scalar که بیش از یک ردیف برگرداند، خطای 1242 می‌دهد، اما فقط وقتی داده‌ی تکراری واقعاً پیدا شود؛ یعنی ممکن است ماه‌ها درست کار کند و ناگهان بشکند.</li>
<li>بهینه‌ساز MySQL 8 بسیاری از <code>IN (subquery)</code>ها را به semi-join تبدیل می‌کند؛ توصیه‌ی قدیمی «همیشه زیرکوئری را به JOIN تبدیل کن» دیگر قانون نیست — با EXPLAIN بسنجید.</li>
</ul>""",
                },
                {
                    "title": "CTE و CTE بازگشتی: دسته‌بندی درختی و سری تاریخ",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>کوئری‌های خوانا با WITH</h2>
<p>Common Table Expression (از MySQL 8.0) به یک زیرکوئری نام می‌دهد تا کوئری‌های پیچیده را مثل یک متن چندمرحله‌ای بنویسید. یک CTE می‌تواند چند بار در همان کوئری استفاده شود و به CTEهای قبلی ارجاع دهد.</p>
<pre><code class="language-sql">WITH monthly AS (
  SELECT DATE_FORMAT(created_at, '%Y-%m') AS ym, SUM(total_amount) AS revenue
  FROM orders WHERE status IN ('paid','shipped')
  GROUP BY ym
),
stats AS (
  SELECT AVG(revenue) AS avg_rev FROM monthly
)
SELECT m.ym, m.revenue,
       ROUND(100 * m.revenue / s.avg_rev) AS pct_of_avg
FROM monthly m CROSS JOIN stats s
ORDER BY m.ym;</code></pre>
<h3>CTE بازگشتی: دسته‌بندی درختی</h3>
<p>دسته‌بندی فروشگاه معمولاً درختی است: «فرش ← دستباف ← کاشان ← لچک‌ترنج». ساده‌ترین مدل، جدولی با ستون <code>parent_id</code> است (Adjacency List). CTE بازگشتی این درخت را در یک کوئری پیمایش می‌کند:</p>
<pre><code class="language-sql">CREATE TABLE categories (
  id INT UNSIGNED PRIMARY KEY,
  parent_id INT UNSIGNED NULL,
  name VARCHAR(60) NOT NULL,
  FOREIGN KEY (parent_id) REFERENCES categories (id)
);
INSERT INTO categories VALUES
 (1, NULL, 'فرش'), (2, 1, 'دستباف'), (3, 1, 'ماشینی'),
 (4, 2, 'کاشان'), (5, 2, 'تبریز'), (6, 4, 'لچک‌ترنج'), (7, 3, '۱۲۰۰ شانه');

WITH RECURSIVE tree AS (
  SELECT id, name, parent_id, 0 AS depth,
         CAST(name AS CHAR(500)) AS path            -- CAST ضروری است!
  FROM categories WHERE parent_id IS NULL
  UNION ALL
  SELECT c.id, c.name, c.parent_id, t.depth + 1,
         CONCAT(t.path, ' / ', c.name)
  FROM categories c JOIN tree t ON c.parent_id = t.id
)
SELECT id, CONCAT(REPEAT('    ', depth), name) AS indented, path
FROM tree ORDER BY path;</code></pre>
<p>بخش اول (anchor) ریشه‌ها را می‌دهد و بخش دوم در هر دور، فرزندان ردیف‌های دور قبل را اضافه می‌کند تا دیگر ردیف تازه‌ای پیدا نشود. برعکسش هم ممکن است: از یک دسته‌ی برگ شروع کنید و با <code>t.parent_id = c.id</code> به بالا بروید تا مسیر breadcrumb صفحه‌ی محصول ساخته شود.</p>
<h3>سری تاریخ برای گزارش بدون روز خالی</h3>
<pre><code class="language-sql">WITH RECURSIVE days AS (
  SELECT DATE('2025-03-21') AS d
  UNION ALL
  SELECT d + INTERVAL 1 DAY FROM days WHERE d &lt; '2025-04-20'
)
SELECT days.d, COUNT(o.id) AS orders_count
FROM days
LEFT JOIN orders o ON o.created_at &gt;= days.d AND o.created_at &lt; days.d + INTERVAL 1 DAY
GROUP BY days.d ORDER BY days.d;</code></pre>
<p>بدون سری تاریخ، روزهایی که فروش نداشته‌اند اصلاً در نمودار ظاهر نمی‌شوند و محور زمان دروغ می‌گوید.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>نوع ستون‌های CTE بازگشتی فقط از بخش anchor تعیین می‌شود؛ بدون <code>CAST(name AS CHAR(500))</code> مسیر به طول نام ریشه بریده می‌شود و در حالت strict خطای <code>Data too long</code> می‌گیرید.</li>
<li>حداکثر عمق بازگشت با <code>cte_max_recursion_depth</code> (پیش‌فرض 1000) محدود است؛ داده‌ی چرخه‌دار (دسته‌ای که والد خودش باشد) با خطا متوقف می‌شود، نه حلقه‌ی بی‌پایان. برای سری طولانی‌تر مقدار آن را در نشست بالا ببرید.</li>
<li>برای تشخیص چرخه در داده، مسیر idها را نگه دارید و شرط <code>FIND_IN_SET(c.id, t.id_path) = 0</code> را به بخش بازگشتی اضافه کنید.</li>
<li>CTE غیربازگشتی که چند بار ارجاع شود، معمولاً یک بار ساخته (materialize) می‌شود؛ در حالی که همان زیرکوئری تکرارشده در derived table ممکن است دو بار اجرا شود.</li>
<li>MariaDB از 10.2 CTE و CTE بازگشتی دارد؛ اما LATERAL را ندارد، که در کدهای مشترک باید در نظر گرفت.</li>
</ul>""",
                },
                {
                    "title": "Window Functions: رتبه‌بندی، LAG و جمع تجمعی",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>تجمیع بدون از دست دادن ردیف‌ها</h2>
<p>GROUP BY ردیف‌ها را فشرده می‌کند؛ Window Function (از MySQL 8.0) برای هر ردیف مقداری بر اساس «پنجره‌ای» از ردیف‌های مرتبط حساب می‌کند و ردیف را نگه می‌دارد. با آن کارهایی که قبلاً به زیرکوئری‌های پیچیده یا متغیرهای <code>@row</code> نیاز داشت، در یک خط انجام می‌شود.</p>
<pre><code class="language-sql">SELECT o.id, o.customer_id, o.total_amount,
       SUM(o.total_amount) OVER (PARTITION BY o.customer_id) AS customer_total,
       ROUND(100 * o.total_amount / SUM(o.total_amount) OVER (PARTITION BY o.customer_id), 1) AS pct
FROM orders o;</code></pre>
<p><code>PARTITION BY</code> گروه را تعیین می‌کند و <code>ORDER BY</code> داخل OVER ترتیب ردیف‌ها در پنجره را.</p>
<h3>رتبه‌بندی</h3>
<table><thead><tr><th>تابع</th><th>برای مقادیر 100، 90، 90، 80</th></tr></thead><tbody>
<tr><td><code>ROW_NUMBER()</code></td><td>1، 2، 3، 4 — یکتا، تساوی را دلبخواه می‌شکند</td></tr>
<tr><td><code>RANK()</code></td><td>1، 2، 2، 4 — با پرش</td></tr>
<tr><td><code>DENSE_RANK()</code></td><td>1، 2، 2، 3 — بدون پرش</td></tr>
<tr><td><code>NTILE(4)</code></td><td>تقسیم به چهار دسته‌ی تقریباً هم‌اندازه (چارک)</td></tr>
</tbody></table>
<pre><code class="language-sql">-- پرفروش‌ترین ۳ محصول هر طرح (Top-N per group)
WITH ranked AS (
  SELECT d.name AS design, p.sku, SUM(oi.qty) AS sold,
         ROW_NUMBER() OVER (PARTITION BY d.id ORDER BY SUM(oi.qty) DESC, p.id) AS rn
  FROM order_items oi
  JOIN products p ON p.id = oi.product_id
  JOIN designs d  ON d.id = p.design_id
  GROUP BY d.id, d.name, p.id, p.sku
)
SELECT design, sku, sold FROM ranked WHERE rn &lt;= 3;</code></pre>
<p>Window Function را نمی‌توان در WHERE استفاده کرد (بعد از WHERE محاسبه می‌شود)؛ به همین دلیل نتیجه را در CTE می‌پیچیم و بیرون فیلتر می‌کنیم.</p>
<h3>LAG و LEAD: مقایسه با ردیف قبل</h3>
<pre><code class="language-sql">WITH m AS (
  SELECT DATE_FORMAT(created_at, '%Y-%m') AS ym, SUM(total_amount) AS rev
  FROM orders GROUP BY ym
)
SELECT ym, rev,
       LAG(rev) OVER w AS prev_rev,
       ROUND(100 * (rev - LAG(rev) OVER w) / LAG(rev) OVER w, 1) AS growth_pct,
       SUM(rev) OVER (w ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total,
       AVG(rev) OVER (w ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)        AS moving_avg_3m
FROM m
WINDOW w AS (ORDER BY ym);</code></pre>
<p>عبارت <code>WINDOW w AS (...)</code> تعریف پنجره را یک بار می‌نویسد و چند تابع از آن استفاده می‌کنند.</p>
<h3>قاب پنجره: ROWS در برابر RANGE</h3>
<p>وقتی داخل OVER فقط ORDER BY می‌نویسید، قاب پیش‌فرض <code>RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW</code> است؛ یعنی همه‌ی ردیف‌های <em>هم‌مقدار</em> با ردیف جاری هم داخل جمع می‌آیند. اگر دو سفارش تاریخ یکسان داشته باشند، جمع تجمعی هر دو یکی نشان داده می‌شود. برای جمع تجمعی ردیف‌به‌ردیف صریحاً <code>ROWS</code> بنویسید.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>ROW_NUMBER()</code> بدون مرتب‌سازی یکتا (مثلاً فقط روی تاریخ) در هر اجرا ممکن است عدد متفاوتی بدهد؛ همیشه id را به‌عنوان شکننده‌ی تساوی اضافه کنید.</li>
<li><code>LAST_VALUE(x) OVER (ORDER BY d)</code> تقریباً همیشه خود ردیف جاری را برمی‌گرداند، به‌خاطر همان قاب پیش‌فرض؛ قاب را <code>ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING</code> کنید.</li>
<li>برای حذف ردیف‌های تکراری با نگه داشتن جدیدترین: ROW_NUMBER روی گروه تکراری، سپس <code>DELETE ... WHERE id IN (SELECT id FROM (...) t WHERE rn &gt; 1)</code>؛ لایه‌ی اضافی derived table برای دور زدن خطای 1093 لازم است.</li>
<li><code>LAG(rev, 12)</code> مقدار دوازده ردیف قبل را می‌دهد؛ برای مقایسه با «همین ماه سال قبل»، به شرطی که هیچ ماهی در سری جا نیفتاده باشد (ترکیب با سری تاریخ درس قبل).</li>
<li>متغیرهای کاربر مثل <code>@rn := @rn + 1</code> برای شماره‌گذاری در 8.0 منسوخ شده‌اند و ترتیب ارزیابی‌شان تضمینی ندارد؛ کدهای قدیمی را به Window Function تبدیل کنید.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۵ ─────────────────────────────
        {
            "title": "فصل ۵: ایندکس و کارایی — از B-Tree تا EXPLAIN ANALYZE",
            "lessons": [
                {
                    "title": "B-Tree و Clustered Index در InnoDB: ایندکس واقعاً چیست؟",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>چرا یک کوئری ۲ ثانیه و دیگری ۲ میلی‌ثانیه طول می‌کشد؟</h2>
<p>بدون ایندکس، پیدا کردن سفارش‌های یک مشتری یعنی خواندن تک‌تک ردیف‌های جدول (full table scan). ایندکس یک ساختار مرتب جداگانه است که مثل فهرست الفبایی آخر کتاب، مستقیم به جای درست می‌برد. نوع پیش‌فرض ایندکس در InnoDB درخت <strong>B+Tree</strong> است.</p>
<h3>ساختار B+Tree</h3>
<ul>
<li>داده در <strong>صفحه</strong>های 16 کیلوبایتی ذخیره می‌شود. هر صفحه‌ی میانی صدها کلید و اشاره‌گر دارد، پس درخت خیلی «پهن و کوتاه» است.</li>
<li>جدولی با ده‌ها میلیون ردیف معمولاً فقط ۳ یا ۴ سطح دارد؛ یعنی هر جست‌وجوی نقطه‌ای با ۳ یا ۴ خواندن صفحه تمام می‌شود و صفحه‌های بالایی همیشه در حافظه (buffer pool) هستند.</li>
<li>برگ‌ها به هم زنجیر شده‌اند، پس پیمایش بازه (<code>BETWEEN</code>، <code>&gt;</code>، <code>ORDER BY</code>) پس از پیدا کردن نقطه‌ی شروع، فقط خواندن پشت‌سرهم است.</li>
</ul>
<h3>Clustered Index: جدول همان ایندکس است</h3>
<p>در InnoDB برگ‌های ایندکس کلید اصلی <em>کل ردیف</em> را در خود دارند؛ جدول جدا از این ایندکس وجود ندارد. هر ایندکس دیگر (secondary index) در برگ‌هایش فقط ستون‌های ایندکس به‌علاوه‌ی <strong>مقدار کلید اصلی</strong> را نگه می‌دارد.</p>
<pre><code class="language-sql">CREATE TABLE orders (
  id          BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,   -- clustered
  customer_id INT UNSIGNED NOT NULL,
  status      VARCHAR(20) NOT NULL,
  created_at  DATETIME NOT NULL,
  total_amount DECIMAL(15,0) NOT NULL,
  INDEX ix_customer (customer_id)       -- برگ‌ها: (customer_id, id)
);

-- این کوئری دو مرحله دارد:
-- ۱) در ix_customer همه‌ی idهای مشتری 42 پیدا می‌شود
-- ۲) برای هر id یک جست‌وجو در clustered index تا بقیه‌ی ستون‌ها خوانده شود
SELECT created_at, total_amount FROM orders WHERE customer_id = 42;</code></pre>
<p>مرحله‌ی دوم (lookup به کلید اصلی) هزینه دارد. اگر مشتری ۵ سفارش دارد ناچیز است؛ اگر شرط ۳۰٪ جدول را برگرداند، بهینه‌ساز ترجیح می‌دهد کل جدول را پیمایش کند و ایندکس را کنار بگذارد. به همین دلیل ایندکس روی ستون کم‌تنوع (مثل جنسیت یا وضعیت دوحالته) به‌تنهایی معمولاً بی‌فایده است.</p>
<h3>دیدن و سنجیدن ایندکس‌ها</h3>
<pre><code class="language-sql">SHOW INDEX FROM orders;          -- Cardinality: تخمین تعداد مقادیر متمایز
ANALYZE TABLE orders;            -- به‌روزرسانی آمار ایندکس‌ها

-- اندازه‌ی هر ایندکس به مگابایت
SELECT index_name,
       ROUND(stat_value * @@innodb_page_size / 1024 / 1024, 1) AS size_mb
FROM mysql.innodb_index_stats
WHERE database_name = 'carpet_shop' AND table_name = 'orders'
  AND stat_name = 'size';</code></pre>
<h3>هزینه‌ی ایندکس</h3>
<p>هر ایندکس خواندن را سریع و نوشتن را کندتر می‌کند: هر INSERT، UPDATE روی ستون ایندکس‌دار و DELETE باید همه‌ی ایندکس‌ها را به‌روز کند و فضای دیسک و buffer pool مصرف می‌کند. هدف «ایندکس روی همه‌ی ستون‌ها» نیست؛ ایندکس برای کوئری‌های واقعی و پرتکرار است.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>چون کلید اصلی در هر ایندکس ثانویه کپی می‌شود، کلید اصلی CHAR(36) با utf8mb4 می‌تواند حجم همه‌ی ایندکس‌ها را چند برابر کند؛ یکی دیگر از دلایل BIGINT یا BINARY(16).</li>
<li>ایندکس ثانویه به‌طور ضمنی کلید اصلی را در انتها دارد؛ پس <code>INDEX (customer_id)</code> برای <code>WHERE customer_id = 42 ORDER BY id</code> مرتب‌سازی جداگانه لازم ندارد.</li>
<li>Cardinality در SHOW INDEX تخمینی از نمونه‌گیری چند صفحه است و ممکن است بعد از تغییرات بزرگ داده، بهینه‌ساز را به اشتباه بیندازد؛ پس از ورود دسته‌ای حجیم ANALYZE TABLE بزنید.</li>
<li>InnoDB یک Adaptive Hash Index هم دارد که روی صفحه‌های داغ خودکار ساخته می‌شود؛ در 8.4 به‌طور پیش‌فرض خاموش است، چون در بار هم‌زمان بالا خودش گلوگاه قفل می‌شد.</li>
<li>ایندکس‌های تکراری رایج‌اند: <code>INDEX (a)</code> وقتی <code>INDEX (a, b)</code> هم وجود دارد زائد است. <code>SELECT * FROM sys.schema_redundant_indexes;</code> آن‌ها را نشان می‌دهد.</li>
</ul>""",
                },
                {
                    "title": "ایندکس ترکیبی، قانون leftmost prefix، Covering و Invisible Index",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>ترتیب ستون‌ها همه‌چیز است</h2>
<p>ایندکس ترکیبی <code>(status, customer_id, created_at)</code> مثل دفترچه تلفنی است که اول بر اساس نام خانوادگی، بعد نام و بعد شهر مرتب شده. پیدا کردن «همه‌ی محمدی‌ها» سریع است؛ پیدا کردن «همه‌ی علی‌ها» بدون دانستن نام خانوادگی نه. این قانون <strong>leftmost prefix</strong> است.</p>
<pre><code class="language-sql">ALTER TABLE orders ADD INDEX ix_s_c_d (status, customer_id, created_at);</code></pre>
<table><thead><tr><th>شرط</th><th>استفاده از ایندکس</th></tr></thead><tbody>
<tr><td><code>status = 'paid'</code></td><td>بله، ستون اول</td></tr>
<tr><td><code>status = 'paid' AND customer_id = 42</code></td><td>بله، دو ستون</td></tr>
<tr><td><code>status = 'paid' AND customer_id = 42 AND created_at &gt;= '2025-01-01'</code></td><td>بله، هر سه ستون</td></tr>
<tr><td><code>customer_id = 42</code></td><td>معمولاً نه (ستون اول نیامده)</td></tr>
<tr><td><code>status = 'paid' AND created_at &gt;= '2025-01-01'</code></td><td>فقط ستون اول؛ created_at با فیلتر روی ردیف‌ها بررسی می‌شود</td></tr>
<tr><td><code>status IN ('paid','shipped') AND customer_id = 42</code></td><td>بله؛ IN مثل چند برابری عمل می‌کند</td></tr>
</tbody></table>
<h3>قاعده‌ی طلایی: برابری اول، بازه آخر</h3>
<p>بعد از اولین ستونی که با بازه (<code>&gt;</code>، <code>BETWEEN</code>، <code>LIKE 'x%'</code>) فیلتر شود، ستون‌های بعدی ایندکس برای جست‌وجو استفاده نمی‌شوند. پس ستون‌هایی که با <code>=</code> فیلتر می‌شوند جلو، و ستون بازه یا مرتب‌سازی آخر.</p>
<pre><code class="language-sql">-- کوئری پرتکرار پنل: سفارش‌های پرداخت‌شده‌ی یک مشتری، جدیدترین اول
SELECT id, created_at, total_amount
FROM orders
WHERE customer_id = 42 AND status = 'paid'
ORDER BY created_at DESC
LIMIT 20;

-- ایندکس مناسب: دو برابری، سپس ستون مرتب‌سازی
ALTER TABLE orders ADD INDEX ix_cust_status_created (customer_id, status, created_at);</code></pre>
<h3>Covering Index: بدون مراجعه به جدول</h3>
<p>اگر همه‌ی ستون‌های مورد نیاز کوئری در خود ایندکس باشند، مرحله‌ی lookup به clustered index حذف می‌شود و در EXPLAIN عبارت <code>Using index</code> می‌آید. با افزودن <code>total_amount</code> به انتهای ایندکس بالا، کوئری کاملاً از ایندکس پاسخ داده می‌شود (<code>id</code> که کلید اصلی است خودش در ایندکس هست).</p>
<h3>ابزارهای MySQL 8</h3>
<pre><code class="language-sql">-- ایندکس نزولی واقعی (قبل از 8.0 کلمه‌ی DESC نادیده گرفته می‌شد)
ALTER TABLE orders ADD INDEX ix_created_desc (created_at DESC);

-- ایندکس تابعی (8.0.13): پرانتز دوتایی الزامی است
ALTER TABLE orders ADD INDEX ix_order_day ((DATE(created_at)));

-- ایندکس نامرئی: آزمایش حذف بدون حذف واقعی
ALTER TABLE orders ALTER INDEX ix_customer INVISIBLE;
-- چند روز پایش؛ اگر چیزی کند نشد:
ALTER TABLE orders DROP INDEX ix_customer;
-- اگر کند شد، فوری و بدون بازسازی:
ALTER TABLE orders ALTER INDEX ix_customer VISIBLE;</code></pre>
<p>ایندکس نامرئی همچنان به‌روز نگه داشته می‌شود، پس برگرداندنش آنی است؛ حذف و ساخت دوباره‌ی ایندکس روی جدول بزرگ ممکن است ساعت‌ها طول بکشد.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>از 8.0.13 «Index Skip Scan» گاهی ایندکس <code>(status, created_at)</code> را برای شرط فقط روی created_at هم به کار می‌گیرد، به شرط کم‌تنوع بودن ستون اول؛ در EXPLAIN با <code>Using index for skip scan</code> دیده می‌شود.</li>
<li>ایندکس پیشوندی <code>INDEX (title(20))</code> برای ستون‌های متنی بلند فضا را کم می‌کند، اما هرگز covering نیست و برای ORDER BY کامل هم به کار نمی‌آید.</li>
<li>ایندکس UNIQUE ترکیبی با ستون NULLپذیر، ردیف‌های تکراری را که یک جزء NULL دارند رد نمی‌کند؛ <code>(order_id, coupon_code)</code> با coupon_code NULL چند بار ثبت می‌شود.</li>
<li>با <code>SET SESSION optimizer_switch = 'use_invisible_indexes=on';</code> می‌توانید اثر یک ایندکس نامرئی را فقط در نشست خودتان آزمایش کنید.</li>
<li><code>sys.schema_unused_indexes</code> ایندکس‌هایی را نشان می‌دهد که از آخرین راه‌اندازی سرور استفاده نشده‌اند؛ اما گزارش ماهانه‌ای که هنوز اجرا نشده هم آنجاست — قبل از حذف، نامرئی کنید.</li>
</ul>""",
                },
                {
                    "title": "خواندن EXPLAIN و EXPLAIN ANALYZE",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>از بهینه‌ساز بپرسید چه نقشه‌ای دارد</h2>
<p><code>EXPLAIN</code> نقشه‌ی اجرای کوئری را بدون اجرای آن نشان می‌دهد. <code>EXPLAIN ANALYZE</code> (از 8.0.18) کوئری را <em>واقعاً اجرا</em> می‌کند و زمان و تعداد ردیف واقعی هر مرحله را کنار تخمین‌ها می‌گذارد. هر بهینه‌سازی باید با یکی از این دو شروع و با آن تأیید شود؛ حدس زدن کافی نیست.</p>
<pre><code class="language-sql">EXPLAIN
SELECT o.id, o.total_amount, c.full_name
FROM orders o JOIN customers c ON c.id = o.customer_id
WHERE o.status = 'paid' AND o.created_at &gt;= '2025-03-21'
ORDER BY o.created_at DESC LIMIT 50;</code></pre>
<h3>ستون‌های مهم</h3>
<table><thead><tr><th>ستون</th><th>معنا</th></tr></thead><tbody>
<tr><td><code>type</code></td><td>روش دسترسی؛ مهم‌ترین ستون (جدول بعدی)</td></tr>
<tr><td><code>possible_keys</code> / <code>key</code></td><td>ایندکس‌های قابل استفاده و ایندکسی که انتخاب شد</td></tr>
<tr><td><code>key_len</code></td><td>چند بایت از ایندکس استفاده شد؛ نشان می‌دهد چند ستون از ایندکس ترکیبی به کار رفته</td></tr>
<tr><td><code>rows</code></td><td>تخمین ردیف‌هایی که باید بررسی شوند</td></tr>
<tr><td><code>filtered</code></td><td>درصد تخمینی ردیف‌هایی که از شرط‌های باقی‌مانده عبور می‌کنند</td></tr>
<tr><td><code>Extra</code></td><td>جزئیات: Using index، Using where، Using filesort، Using temporary</td></tr>
</tbody></table>
<h3>نردبان type، از بهترین تا بدترین</h3>
<table><thead><tr><th>type</th><th>یعنی</th></tr></thead><tbody>
<tr><td><code>const</code></td><td>حداکثر یک ردیف با کلید اصلی یا UNIQUE</td></tr>
<tr><td><code>eq_ref</code></td><td>در JOIN، برای هر ردیف یک ردیف با کلید یکتا</td></tr>
<tr><td><code>ref</code></td><td>جست‌وجوی برابری روی ایندکس غیریکتا</td></tr>
<tr><td><code>range</code></td><td>پیمایش بازه‌ای از ایندکس</td></tr>
<tr><td><code>index</code></td><td>پیمایش <em>کل</em> ایندکس (بهتر از ALL ولی باز هم کامل)</td></tr>
<tr><td><code>ALL</code></td><td>پیمایش کل جدول؛ روی جدول بزرگ زنگ خطر</td></tr>
</tbody></table>
<p>در Extra، <code>Using filesort</code> یعنی مرتب‌سازی جداگانه (نه لزوماً روی دیسک) و <code>Using temporary</code> یعنی جدول موقت؛ هر دو روی نتیجه‌های بزرگ گران‌اند و معمولاً با ایندکسی که ترتیب مورد نیاز را دارد حذف می‌شوند.</p>
<h3>EXPLAIN ANALYZE و قالب درختی</h3>
<pre><code class="language-sql">EXPLAIN ANALYZE
SELECT customer_id, COUNT(*) FROM orders
WHERE created_at &gt;= '2025-01-01' GROUP BY customer_id\G

-- خروجی (خلاصه):
-- -&gt; Table scan on &lt;temporary&gt;  (actual time=45.2..46.0 rows=2870 loops=1)
--     -&gt; Aggregate using temporary table  (actual time=45.1..45.1 rows=2870 loops=1)
--         -&gt; Index range scan on orders using ix_created
--            (cost=6010 rows=30020) (actual time=0.1..35.7 rows=28750 loops=1)</code></pre>
<p>درخت را از داخلی‌ترین (پایین‌ترین) سطر به بیرون بخوانید. <code>actual time=a..b</code> زمان اولین ردیف و همه‌ی ردیف‌ها به میلی‌ثانیه است و <code>loops</code> تعداد دفعات اجرای آن گره؛ زمان کل گره تقریباً b × loops است. اختلاف بزرگ بین <code>rows</code> تخمینی و واقعی یعنی آمار غلط است و بهینه‌ساز تصمیم اشتباه گرفته.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>EXPLAIN ANALYZE کوئری را کامل اجرا می‌کند؛ روی کوئری ده‌دقیقه‌ای، ده دقیقه منتظر می‌مانید. روی سرور تولید در ساعت شلوغ مراقب باشید.</li>
<li>بعد از <code>EXPLAIN</code> معمولی، <code>SHOW WARNINGS;</code> کوئری بازنویسی‌شده توسط بهینه‌ساز را نشان می‌دهد؛ می‌بینید زیرکوئری شما به semi-join تبدیل شده یا نه.</li>
<li><code>EXPLAIN FOR CONNECTION 1234;</code> نقشه‌ی کوئری در حال اجرای یک اتصال دیگر را (شماره از SHOW PROCESSLIST) نشان می‌دهد؛ برای کوئری گیرکرده‌ی تولید بی‌نظیر است.</li>
<li>برای فهم «چرا این ایندکس انتخاب نشد»، optimizer trace را روشن کنید: <code>SET optimizer_trace='enabled=on';</code>، کوئری را اجرا و <code>SELECT * FROM information_schema.optimizer_trace\G</code> را بخوانید.</li>
<li>اگر آمار ستون‌های بدون ایندکس غلط است، هیستوگرام بسازید: <code>ANALYZE TABLE orders UPDATE HISTOGRAM ON status WITH 16 BUCKETS;</code>؛ تخمین filtered دقیق‌تر می‌شود بدون هزینه‌ی نگه‌داری ایندکس.</li>
</ul>""",
                },
                {
                    "title": "Slow Query Log و دام‌های رایجی که ایندکس را بی‌اثر می‌کنند",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>اول پیدا کنید کدام کوئری کند است</h2>
<p>بهینه‌سازی بدون اندازه‌گیری، حدس است. Slow query log همه‌ی کوئری‌هایی را که بیش از یک آستانه طول کشیده‌اند ثبت می‌کند.</p>
<pre><code class="language-sql">SET PERSIST slow_query_log = ON;
SET PERSIST long_query_time = 0.5;                 -- نیم ثانیه؛ اعشار مجاز است
SET PERSIST log_slow_extra = ON;                   -- 8.0.14+: ستون‌های اضافه مثل Rows_examined دقیق
SHOW VARIABLES LIKE 'slow_query_log_file';</code></pre>
<pre><code class="language-bash"># خلاصه‌سازی: کوئری‌های مشابه با پارامتر متفاوت یکی می‌شوند
sudo mysqldumpslow -s t -t 10 /var/lib/mysql/server-slow.log
# ابزار حرفه‌ای‌تر (Percona Toolkit)
pt-query-digest /var/lib/mysql/server-slow.log &gt; digest.txt</code></pre>
<p>بدون فایل لاگ هم می‌توانید از performance_schema استفاده کنید که آمار همه‌ی کوئری‌ها را از زمان راه‌اندازی جمع کرده است:</p>
<pre><code class="language-sql">SELECT query, exec_count, total_latency, avg_latency, rows_examined_avg
FROM sys.statement_analysis
ORDER BY total_latency DESC LIMIT 10;</code></pre>
<p>مرتب‌سازی بر اساس <strong>زمان کل</strong> مهم است: کوئری ۵۰ میلی‌ثانیه‌ای که روزی یک میلیون بار اجرا می‌شود از کوئری ۱۰ ثانیه‌ای روزی یک بار مهم‌تر است.</p>
<h3>دام‌هایی که ایندکس را خاموش می‌کنند</h3>
<table><thead><tr><th>الگوی بد</th><th>چرا</th><th>بازنویسی</th></tr></thead><tbody>
<tr><td><code>WHERE DATE(created_at) = '2025-03-21'</code></td><td>تابع روی ستون؛ مقدار ایندکس‌شده دیگر مستقیم مقایسه نمی‌شود</td><td><code>created_at &gt;= '2025-03-21' AND created_at &lt; '2025-03-22'</code></td></tr>
<tr><td><code>WHERE YEAR(created_at) = 2025</code></td><td>همان</td><td>بازه‌ی نیمه‌باز سال</td></tr>
<tr><td><code>WHERE mobile = 9121234567</code></td><td>ستون VARCHAR با عدد مقایسه می‌شود؛ هر ردیف به عدد تبدیل می‌شود</td><td><code>mobile = '09121234567'</code></td></tr>
<tr><td><code>WHERE price * 1.1 &gt; 1000000</code></td><td>محاسبه روی ستون</td><td><code>price &gt; 1000000 / 1.1</code></td></tr>
<tr><td><code>WHERE title LIKE '%کاشان%'</code></td><td>پیشوند نامعلوم</td><td>FULLTEXT (درس بعد)</td></tr>
<tr><td><code>WHERE a = 1 OR b = 2</code></td><td>دو ستون مختلف؛ گاهی index_merge، اغلب ALL</td><td>دو SELECT با <code>UNION</code></td></tr>
<tr><td><code>ORDER BY RAND() LIMIT 5</code></td><td>کل جدول مرتب می‌شود</td><td>انتخاب تصادفی id در برنامه</td></tr>
</tbody></table>
<pre><code class="language-sql">-- OR روی دو ستون، بازنویسی با UNION (هر بخش ایندکس خودش را دارد)
SELECT id FROM customers WHERE mobile = '09121234567'
UNION
SELECT id FROM customers WHERE national_id = '1234567890';</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>عکس حالت تبدیل ضمنی بی‌خطر است: ستون عددی با رشته (<code>id = '42'</code>) مشکلی ندارد، چون ثابت یک بار تبدیل می‌شود. مشکل فقط ستون <em>متنی</em> با ثابت عددی است — رایج در کد PHP و پایتونی که شماره موبایل را int می‌کند.</li>
<li>JOIN بین دو ستون با collation متفاوت (مثلاً یک جدول قدیمی utf8mb3_general_ci و جدول جدید utf8mb4_0900_ai_ci) همان اثر تابع روی ستون را دارد؛ EXPLAIN با type=ALL لو می‌دهد.</li>
<li>به‌جای تغییر کوئری‌های قدیمی با <code>DATE(col)</code> می‌توانید ایندکس تابعی <code>((DATE(created_at)))</code> بسازید؛ عبارت کوئری باید دقیقاً با عبارت ایندکس یکی باشد.</li>
<li><code>log_queries_not_using_indexes</code> را همراه با <code>log_throttle_queries_not_using_indexes</code> روشن کنید، وگرنه جدول‌های کوچکی که همیشه اسکن کامل می‌شوند لاگ را پر می‌کنند.</li>
<li><code>long_query_time = 0</code> برای چند دقیقه در زمان اوج، تصویری کامل از بار واقعی می‌دهد (همه‌ی کوئری‌ها لاگ می‌شوند)؛ فقط فضای دیسک را زیر نظر داشته باشید و فوراً برگردانید.</li>
</ul>""",
                },
                {
                    "title": "جست‌وجوی متن فارسی با FULLTEXT و ngram parser",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>وقتی LIKE '%...%' دیگر جواب نمی‌دهد</h2>
<p>جست‌وجوی «فرش ابریشم کاشان» در عنوان و توضیحات ده‌ها هزار محصول با LIKE یعنی اسکن کامل و بدون رتبه‌بندی. ایندکس <strong>FULLTEXT</strong> (در InnoDB از 5.6) یک ایندکس معکوس از «کلمه ← ردیف‌ها» می‌سازد و نتیجه را بر اساس ارتباط رتبه‌بندی می‌کند.</p>
<pre><code class="language-sql">ALTER TABLE products ADD FULLTEXT INDEX ft_title_desc (title, description);

-- حالت زبان طبیعی: رتبه‌بندی بر اساس ارتباط
SELECT sku, title, MATCH(title, description) AGAINST ('فرش ابریشم کاشان') AS score
FROM products
WHERE MATCH(title, description) AGAINST ('فرش ابریشم کاشان')
ORDER BY score DESC LIMIT 20;

-- حالت بولی: + الزامی، - ممنوع، * پیشوند، "..." عبارت دقیق
SELECT sku, title FROM products
WHERE MATCH(title, description)
      AGAINST ('+ابریشم +کاشان -ماشینی "لچک ترنج"' IN BOOLEAN MODE);</code></pre>
<p>ستون‌های داخل MATCH باید <em>دقیقاً</em> با ستون‌های یک ایندکس FULLTEXT یکی باشند.</p>
<h3>مشکل‌های parser پیش‌فرض با فارسی</h3>
<ul>
<li>کلمات را با فاصله و علائم جدا می‌کند؛ برای فارسی کار می‌کند، اما «فرش» و «فرش‌ها» دو کلمه‌ی مستقل‌اند (ریشه‌یابی ندارد).</li>
<li><code>innodb_ft_min_token_size</code> پیش‌فرض 3 است؛ کلمات دوحرفی مثل «گل»، «نخ» و «قم» اصلاً ایندکس نمی‌شوند و جست‌وجویشان هیچ نتیجه‌ای نمی‌دهد.</li>
<li>فهرست stopword پیش‌فرض انگلیسی است و کلمات پرتکرار فارسی مثل «و» و «از» را نمی‌شناسد.</li>
</ul>
<pre><code class="language-ini">[mysqld]
innodb_ft_min_token_size = 2
ngram_token_size         = 2</code></pre>
<p>این متغیرها فقط هنگام راه‌اندازی خوانده می‌شوند و پس از تغییرشان باید ایندکس FULLTEXT را حذف و دوباره بسازید.</p>
<h3>ngram parser</h3>
<p>parser داخلی <code>ngram</code> متن را به تکه‌های n کاراکتری پشت‌سرهم می‌شکند؛ با n=2، «کاشان» می‌شود «کا، اش، شا، ان». در نتیجه جست‌وجوی «فرش» در «فرش‌ها» و «فرشینه» هم پیدا می‌شود و به جداکننده‌ی کلمه وابسته نیست.</p>
<pre><code class="language-sql">ALTER TABLE products ADD FULLTEXT INDEX ft_title_ngram (title) WITH PARSER ngram;

SELECT sku, title FROM products
WHERE MATCH(title) AGAINST ('ابریشم' IN BOOLEAN MODE);</code></pre>
<table><thead><tr><th>روش</th><th>مزیت</th><th>عیب</th></tr></thead><tbody>
<tr><td>parser پیش‌فرض</td><td>ایندکس کوچک، رتبه‌بندی معقول</td><td>بدون ریشه‌یابی، مشکل کلمات کوتاه</td></tr>
<tr><td>ngram</td><td>پیدا کردن بخشی از کلمه، مستقل از جداکننده</td><td>ایندکس بزرگ، نتایج نامربوط بیشتر</td></tr>
<tr><td>Elasticsearch / Meilisearch</td><td>تحلیلگر فارسی، تحمل غلط املایی، facet</td><td>یک سرویس دیگر برای نگه‌داری و همگام‌سازی</td></tr>
</tbody></table>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>برای دیدن اینکه متن واقعاً به چه توکن‌هایی شکسته شده: <code>SET GLOBAL innodb_ft_aux_table = 'carpet_shop/products';</code> و سپس <code>SELECT word FROM information_schema.innodb_ft_index_cache;</code> — بهترین راه آزمایش رفتار با نیم‌فاصله و ی/ک.</li>
<li>قبل از ایندکس کردن، متن را نرمال کنید: ی/ک عربی، ارقام و اعراب. یک ستون <code>search_text</code> (که برنامه هنگام ذخیره پر می‌کند یا ستون تولیدشده‌ی STORED با REPLACE) و FULLTEXT روی آن، نتایج را بسیار بهتر می‌کند.</li>
<li>تغییرات FULLTEXT در InnoDB فقط پس از COMMIT دیده می‌شوند؛ در تستی که داخل تراکنش داده درج و بلافاصله جست‌وجو می‌کند، نتیجه خالی است.</li>
<li>قاعده‌ی معروف «کلمه‌ای که در بیش از ۵۰٪ ردیف‌ها باشد نادیده گرفته می‌شود» فقط مخصوص MyISAM است و در InnoDB وجود ندارد.</li>
<li>با حذف و ویرایش زیاد، ایندکس FULLTEXT ردیف‌های حذف‌شده را نگه می‌دارد؛ <code>SET GLOBAL innodb_optimize_fulltext_only = ON; OPTIMIZE TABLE products;</code> فقط ایندکس متنی را بهینه می‌کند.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۶ ─────────────────────────────
        {
            "title": "فصل ۶: تراکنش و هم‌زمانی — ACID، MVCC، قفل و Deadlock",
            "lessons": [
                {
                    "title": "ACID، autocommit و مدیریت تراکنش",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>همه یا هیچ</h2>
<p>ثبت یک فروش یعنی چند کار: درج سفارش، درج اقلام، کم کردن موجودی انبار و ثبت پرداخت. اگر برق وسط کار برود یا یکی از مراحل خطا بدهد، نباید سفارشی بدون اقلام یا موجودی کم‌شده بدون فروش باقی بماند. تراکنش این چند دستور را به یک واحد تجزیه‌ناپذیر تبدیل می‌کند.</p>
<table><thead><tr><th>ویژگی</th><th>معنا</th><th>در InnoDB با</th></tr></thead><tbody>
<tr><td>Atomicity</td><td>همه‌ی دستورها اعمال می‌شوند یا هیچ‌کدام</td><td>undo log</td></tr>
<tr><td>Consistency</td><td>قیدها (FK، UNIQUE، CHECK) همیشه برقرارند</td><td>بررسی قیدها</td></tr>
<tr><td>Isolation</td><td>تراکنش‌های هم‌زمان کار یکدیگر را نیمه‌کاره نمی‌بینند</td><td>MVCC و قفل‌ها</td></tr>
<tr><td>Durability</td><td>پس از COMMIT، با قطع برق هم از دست نمی‌رود</td><td>redo log و doublewrite</td></tr>
</tbody></table>
<h3>نحو تراکنش</h3>
<pre><code class="language-sql">START TRANSACTION;

INSERT INTO orders (customer_id, status, total_amount) VALUES (42, 'paid', 480000000);
SET @order_id = LAST_INSERT_ID();

INSERT INTO order_items (order_id, product_id, qty, unit_price)
VALUES (@order_id, 7, 1, 480000000);

UPDATE products SET stock = stock - 1 WHERE id = 7 AND stock &gt;= 1;
-- اگر 0 rows affected بود، موجودی کافی نبوده: ROLLBACK
SAVEPOINT before_payment;

INSERT INTO payments (order_id, amount, gateway_ref) VALUES (@order_id, 480000000, 'ZP-99812');
-- اگر فقط ثبت پرداخت مشکل داشت:
-- ROLLBACK TO SAVEPOINT before_payment;

COMMIT;</code></pre>
<h3>autocommit</h3>
<p>در حالت پیش‌فرض (<code>autocommit = 1</code>) هر دستور به‌تنهایی یک تراکنش است و بلافاصله COMMIT می‌شود. <code>START TRANSACTION</code> این حالت را تا COMMIT یا ROLLBACK بعدی معلق می‌کند. اگر <code>SET autocommit = 0</code> بزنید، تراکنش همیشه باز است و تا COMMIT صریح هیچ‌چیز ذخیره نمی‌شود — منشأ رایج «داده را درج کردم ولی در برنامه‌ی دیگر دیده نمی‌شود».</p>
<h3>تراکنش در کد برنامه</h3>
<pre><code class="language-python">import MySQLdb

conn = MySQLdb.connect(read_default_file="~/.my.cnf", db="carpet_shop", charset="utf8mb4")
try:
    with conn.cursor() as cur:
        cur.execute("UPDATE wallets SET balance = balance - %s WHERE user_id = %s AND balance &gt;= %s",
                    (amount, buyer_id, amount))
        if cur.rowcount != 1:
            raise ValueError("موجودی کافی نیست")
        cur.execute("UPDATE wallets SET balance = balance + %s WHERE user_id = %s", (amount, seller_id))
    conn.commit()
except Exception:
    conn.rollback()
    raise</code></pre>
<p>درایورهای پایتونی (DB-API) به‌طور پیش‌فرض autocommit را خاموش دارند؛ بدون <code>commit()</code> همه‌چیز با بسته شدن اتصال ROLLBACK می‌شود. جنگو برعکس، autocommit را روشن می‌کند و تراکنش را با <code>transaction.atomic()</code> می‌سازد.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>دستورهای DDL (<code>CREATE</code>، <code>ALTER</code>، <code>DROP</code>، <code>TRUNCATE</code>) قبل از اجرا تراکنش باز را به‌طور <em>ضمنی COMMIT</em> می‌کنند و خودشان قابل ROLLBACK نیستند؛ مایگریشنی که وسط کار شکست بخورد، نیمه‌کاره می‌ماند.</li>
<li>تراکنشی که بی‌کار باز مانده (مثلاً برنامه‌نویسی که در DBeaver دستوری زده و COMMIT نکرده) قفل‌ها را نگه می‌دارد و undo log را رشد می‌دهد؛ <code>SELECT * FROM information_schema.innodb_trx ORDER BY trx_started;</code> قدیمی‌ترین‌ها را نشان می‌دهد.</li>
<li><code>START TRANSACTION READ ONLY</code> برای گزارش‌های طولانی به InnoDB اجازه‌ی بهینه‌سازی‌های داخلی می‌دهد و از نوشتن تصادفی هم جلوگیری می‌کند.</li>
<li>جدول‌های MyISAM در تراکنش شرکت نمی‌کنند؛ ROLLBACK روی آن‌ها بی‌اثر است و فقط یک warning می‌دهد.</li>
<li>درج گروهی هزاران ردیف داخل یک تراکنش (به‌جای autocommit برای هر ردیف) معمولاً ده‌ها برابر سریع‌تر است، چون هر COMMIT یک flush روی دیسک است.</li>
</ul>""",
                },
                {
                    "title": "MVCC و سطوح ایزوله‌سازی: چرا REPEATABLE READ پیش‌فرض است",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>خواننده‌ها منتظر نویسنده‌ها نمی‌مانند</h2>
<p>InnoDB از <strong>MVCC</strong> (کنترل هم‌زمانی چندنسخه‌ای) استفاده می‌کند: وقتی ردیفی تغییر می‌کند، نسخه‌ی قبلی در undo log نگه داشته می‌شود. هر تراکنشی که در حال خواندن است یک «عکس فوری» (snapshot) دارد و نسخه‌ای را می‌بیند که در لحظه‌ی عکس معتبر بوده. در نتیجه SELECT معمولی هیچ قفلی نمی‌گیرد و منتظر UPDATEهای هم‌زمان نمی‌ماند.</p>
<h3>چهار سطح ایزوله‌سازی</h3>
<table><thead><tr><th>سطح</th><th>Dirty read</th><th>Non-repeatable read</th><th>Phantom</th><th>کاربرد</th></tr></thead><tbody>
<tr><td>READ UNCOMMITTED</td><td>ممکن</td><td>ممکن</td><td>ممکن</td><td>تقریباً هرگز</td></tr>
<tr><td>READ COMMITTED</td><td>خیر</td><td>ممکن</td><td>ممکن</td><td>پیش‌فرض PostgreSQL و جنگو روی MySQL</td></tr>
<tr><td>REPEATABLE READ</td><td>خیر</td><td>خیر</td><td>در خواندن معمولی خیر</td><td>پیش‌فرض MySQL</td></tr>
<tr><td>SERIALIZABLE</td><td>خیر</td><td>خیر</td><td>خیر</td><td>موارد خاص؛ همه‌ی SELECTها قفل اشتراکی می‌گیرند</td></tr>
</tbody></table>
<p>در READ COMMITTED هر دستور SELECT عکس فوری تازه می‌گیرد؛ در REPEATABLE READ کل تراکنش با یک عکس کار می‌کند، پس گزارشی که چند SELECT پشت‌سرهم دارد اعداد سازگار می‌بیند.</p>
<h3>آزمایش با دو پنجره</h3>
<pre><code class="language-sql">-- نشست A                                   -- نشست B
SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;
START TRANSACTION;
SELECT stock FROM products WHERE id = 7;     -- 5
                                              UPDATE products SET stock = 3 WHERE id = 7;  -- autocommit
SELECT stock FROM products WHERE id = 7;     -- هنوز 5 (همان snapshot)
UPDATE products SET stock = stock - 1 WHERE id = 7;
SELECT stock FROM products WHERE id = 7;     -- 2 !
COMMIT;</code></pre>
<p>نتیجه‌ی آخر غافلگیرکننده است: SELECT معمولی «خواندن سازگار» (consistent read) از snapshot است، اما UPDATE یک «خواندن جاری» (current read) است و همیشه آخرین نسخه‌ی COMMIT‌شده را می‌بیند (3)، یک واحد کم می‌کند و از آن به بعد تراکنش تغییر خودش را می‌بیند. به همین دلیل منطق «اول SELECT کن، در برنامه حساب کن، بعد مقدار ثابت را UPDATE کن» زیر بار هم‌زمان غلط است؛ یا محاسبه را در خود UPDATE انجام دهید (<code>stock = stock - 1</code>) یا با <code>SELECT ... FOR UPDATE</code> ردیف را قفل کنید.</p>
<h3>تنظیم سطح</h3>
<pre><code class="language-sql">SELECT @@transaction_isolation;
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;   -- فقط این نشست
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;             -- فقط تراکنش بعدی</code></pre>
<pre><code class="language-ini">[mysqld]
transaction_isolation = READ-COMMITTED</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>snapshot در REPEATABLE READ هنگام <code>START TRANSACTION</code> گرفته <em>نمی‌شود</em>، بلکه هنگام اولین SELECT؛ اگر همان لحظه لازم است: <code>START TRANSACTION WITH CONSISTENT SNAPSHOT</code>. mysqldump با <code>--single-transaction</code> دقیقاً از همین استفاده می‌کند.</li>
<li>تراکنش خواندنی که ساعت‌ها باز بماند، مانع پاک‌سازی (purge) نسخه‌های قدیمی می‌شود؛ مقدار <code>History list length</code> در SHOW ENGINE INNODB STATUS رشد می‌کند و کل سرور کند می‌شود.</li>
<li>متغیر قدیمی <code>tx_isolation</code> در MySQL 8 حذف شده و نامش <code>transaction_isolation</code> است؛ کتابخانه‌ها و ORMهای قدیمی به همین دلیل خطا می‌دهند.</li>
<li>جنگو از نسخه‌ی 2.0 به بعد روی MySQL به‌طور پیش‌فرض READ COMMITTED تنظیم می‌کند، نه REPEATABLE READ پیش‌فرض سرور؛ رفتار برنامه و کلاینت دستی شما ممکن است متفاوت باشد.</li>
<li>READ COMMITTED تعداد gap lockها را به‌شدت کم می‌کند و در سیستم‌های پرنوشتن deadlockها را کاهش می‌دهد؛ اما با binlog مبتنی بر statement سازگار نیست و binlog_format باید ROW باشد (که پیش‌فرض است).</li>
</ul>""",
                },
                {
                    "title": "قفل‌ها در InnoDB: record، gap، next-key و metadata lock",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>وقتی دو نفر یک چیز را می‌خواهند</h2>
<p>MVCC خواندن را بدون قفل حل می‌کند، اما دو نوشتن هم‌زمان روی یک ردیف باید پشت هم بایستند. InnoDB قفل را در سطح <strong>ردیف</strong> (در واقع روی رکوردهای ایندکس) می‌گیرد، نه کل جدول؛ یعنی دو کاربر می‌توانند هم‌زمان دو سفارش مختلف را ویرایش کنند.</p>
<h3>انواع قفل</h3>
<table><thead><tr><th>قفل</th><th>چه چیزی را قفل می‌کند</th><th>چه زمانی</th></tr></thead><tbody>
<tr><td>Shared (S)</td><td>ردیف؛ دیگران هم می‌توانند S بگیرند اما نمی‌توانند بنویسند</td><td><code>SELECT ... FOR SHARE</code></td></tr>
<tr><td>Exclusive (X)</td><td>ردیف؛ هیچ قفل دیگری مجاز نیست</td><td>UPDATE، DELETE، <code>SELECT ... FOR UPDATE</code></td></tr>
<tr><td>Record lock</td><td>یک رکورد ایندکس</td><td>جست‌وجوی برابری روی ایندکس یکتا</td></tr>
<tr><td>Gap lock</td><td>فاصله‌ی <em>بین</em> دو رکورد ایندکس؛ جلوی درج را می‌گیرد</td><td>REPEATABLE READ، اسکن بازه‌ای</td></tr>
<tr><td>Next-key lock</td><td>رکورد + فاصله‌ی قبل از آن</td><td>حالت پیش‌فرض قفل در RR</td></tr>
<tr><td>Metadata lock (MDL)</td><td>تعریف جدول</td><td>هر دستوری که از جدول استفاده می‌کند؛ ALTER قفل انحصاری می‌خواهد</td></tr>
</tbody></table>
<p>Gap lock دلیلی است که REPEATABLE READ در قفل‌گیری هم phantom ندارد: اگر تراکنشی «همه‌ی سفارش‌های مشتری 42» را با FOR UPDATE قفل کند، کسی نمی‌تواند سفارش جدیدی برای مشتری 42 وسط کار درج کند.</p>
<h3>قفل به ایندکس بستگی دارد</h3>
<pre><code class="language-sql">-- ستون status ایندکس ندارد:
START TRANSACTION;
UPDATE orders SET status = 'cancelled' WHERE status = 'draft' AND created_at &lt; '2024-01-01';
-- InnoDB برای پیدا کردن ردیف‌ها کل جدول را اسکن می‌کند و روی
-- همه‌ی رکوردهای اسکن‌شده قفل می‌گذارد؛ عملاً کل جدول تا COMMIT قفل است.</code></pre>
<p>قفل روی رکوردهایی گذاشته می‌شود که <em>پیمایش</em> می‌شوند، نه فقط رکوردهایی که تغییر می‌کنند. ایندکس مناسب در UPDATE و DELETE فقط برای سرعت نیست؛ دامنه‌ی قفل را هم کوچک می‌کند.</p>
<h3>چه کسی چه کسی را قفل کرده؟</h3>
<pre><code class="language-sql">SELECT waiting_pid, waiting_query, blocking_pid, blocking_query, wait_age
FROM sys.innodb_lock_waits;

SELECT object_name, index_name, lock_type, lock_mode, lock_status, lock_data
FROM performance_schema.data_locks;

-- در صورت لزوم، اتصال مزاحم را ببندید
KILL 1234;</code></pre>
<h3>دام Metadata Lock</h3>
<p>سناریوی کلاسیک قطعی سایت: یک تراکنش طولانی (یا یک SELECT سنگین گزارش) روی جدول orders در حال اجراست. شما <code>ALTER TABLE orders ADD COLUMN ...</code> می‌زنید. ALTER منتظر قفل انحصاری metadata می‌ماند، و از این لحظه <em>همه‌ی</em> کوئری‌های بعدی روی orders، حتی SELECTهای ساده، پشت ALTER صف می‌کشند. در SHOW PROCESSLIST وضعیت <code>Waiting for table metadata lock</code> می‌بینید.</p>
<pre><code class="language-sql">SET SESSION lock_wait_timeout = 5;   -- ALTER بعد از ۵ ثانیه تسلیم شود، نه اینکه سایت را بخواباند
ALTER TABLE orders ADD COLUMN note VARCHAR(200) NULL, ALGORITHM=INSTANT;</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>lock_wait_timeout</code> (برای metadata lock) با <code>innodb_lock_wait_timeout</code> (برای قفل ردیف) فرق دارد؛ پیش‌فرض اولی یک سال است! برای مایگریشن‌ها همیشه کمش کنید.</li>
<li>در READ COMMITTED، InnoDB قفل ردیف‌هایی را که در شرط WHERE صدق نکردند بلافاصله پس از بررسی آزاد می‌کند؛ در RR تا پایان تراکنش نگه می‌دارد.</li>
<li>درج ردیف با کلید تکراری در UNIQUE یک قفل اشتراکی روی رکورد موجود می‌گیرد؛ چند INSERT هم‌زمان با کلید یکسان منشأ رایج deadlockهای عجیب است.</li>
<li><code>ALGORITHM=INSTANT</code> (افزودن ستون از 8.0.12 و در هر جایگاهی از 8.0.29) تغییر را فقط در متادیتا اعمال می‌کند؛ اگر ممکن نباشد خطا می‌دهد، به‌جای اینکه بی‌صدا جدول را بازسازی کند.</li>
<li>برای ALTER روی جدول‌های خیلی بزرگ و پرترافیک، ابزارهای <code>gh-ost</code> و <code>pt-online-schema-change</code> جدول سایه می‌سازند و بدون قفل طولانی جابه‌جا می‌کنند.</li>
</ul>""",
                },
                {
                    "title": "Deadlock: تشخیص، خواندن SHOW ENGINE INNODB STATUS و پیشگیری",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>دو تراکنش، هر کدام منتظر دیگری</h2>
<p>Deadlock وقتی رخ می‌دهد که تراکنش A قفلی دارد که B می‌خواهد و B قفلی دارد که A می‌خواهد. هیچ‌کدام نمی‌توانند ادامه دهند. InnoDB این چرخه را فوراً تشخیص می‌دهد، یکی از تراکنش‌ها (معمولاً آن که تغییرات کمتری داشته) را ROLLBACK می‌کند و به برنامه خطای زیر را می‌دهد:</p>
<pre><code class="language-sql">ERROR 1213 (40001): Deadlock found when trying to get lock; try restarting transaction</code></pre>
<h3>بازسازی یک deadlock</h3>
<pre><code class="language-sql">-- نشست A                                      -- نشست B
START TRANSACTION;                              START TRANSACTION;
UPDATE products SET stock = stock - 1
WHERE id = 7;                                   UPDATE products SET stock = stock - 1
                                                WHERE id = 9;
UPDATE products SET stock = stock - 1
WHERE id = 9;       -- منتظر B می‌ماند
                                                UPDATE products SET stock = stock - 1
                                                WHERE id = 7;   -- ERROR 1213 (قربانی)</code></pre>
<p>این دقیقاً چیزی است که در سبد خرید رخ می‌دهد: مشتری اول فرش 7 و بعد 9 را می‌خرد و مشتری دوم هم‌زمان 9 و بعد 7 را.</p>
<h3>خواندن گزارش</h3>
<pre><code class="language-sql">SHOW ENGINE INNODB STATUS\G
-- ------------------------
-- LATEST DETECTED DEADLOCK
-- ------------------------
-- *** (1) TRANSACTION: ... UPDATE products SET stock = stock - 1 WHERE id = 9
-- *** (1) HOLDS THE LOCK(S): RECORD LOCKS ... index PRIMARY of table `carpet_shop`.`products`
-- *** (1) WAITING FOR THIS LOCK TO BE GRANTED: ... lock_mode X locks rec but not gap
-- *** (2) TRANSACTION: ... UPDATE products SET stock = stock - 1 WHERE id = 7
-- *** WE ROLL BACK TRANSACTION (2)</code></pre>
<p>از گزارش سه چیز بیرون بکشید: کدام دو کوئری، روی کدام ایندکس (PRIMARY یا یک ایندکس ثانویه) و چه نوع قفلی (<code>locks rec but not gap</code> یعنی record lock، <code>locks gap before rec</code> یعنی gap lock). این گزارش فقط <em>آخرین</em> deadlock را نگه می‌دارد؛ برای ثبت همه در لاگ خطا:</p>
<pre><code class="language-sql">SET PERSIST innodb_print_all_deadlocks = ON;</code></pre>
<h3>پیشگیری</h3>
<ol>
<li><strong>ترتیب ثابت:</strong> ردیف‌ها را همیشه به یک ترتیب قفل کنید؛ مثلاً اقلام سبد را قبل از UPDATE بر اساس product_id مرتب کنید.</li>
<li><strong>تراکنش کوتاه:</strong> فراخوانی درگاه پرداخت، ارسال پیامک یا هر کار شبکه‌ای را بیرون از تراکنش انجام دهید.</li>
<li><strong>ایندکس مناسب:</strong> تا UPDATE و DELETE ردیف‌های کمتری را پیمایش و قفل کنند.</li>
<li><strong>READ COMMITTED</strong> برای کاهش gap lockها، اگر منطق برنامه اجازه می‌دهد.</li>
<li><strong>تلاش دوباره:</strong> deadlock در سیستم پرترافیک کاملاً از بین نمی‌رود؛ برنامه باید خطای 1213 را بگیرد و کل تراکنش را یکی دو بار تکرار کند.</li>
</ol>
<h3>Lock wait timeout</h3>
<p>اگر چرخه‌ای در کار نباشد و فقط یک تراکنش قفل را طولانی نگه داشته باشد، منتظرها پس از <code>innodb_lock_wait_timeout</code> (پیش‌فرض ۵۰ ثانیه) خطای <code>ERROR 1205: Lock wait timeout exceeded</code> می‌گیرند. برای وب، ۵۰ ثانیه خیلی زیاد است؛ عدد کمتر (مثلاً ۱۰) در نشست برنامه منطقی‌تر است.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>پس از خطای 1205، به‌طور پیش‌فرض فقط <em>همان دستور</em> برگردانده می‌شود، نه کل تراکنش (<code>innodb_rollback_on_timeout = OFF</code>)؛ اگر برنامه ادامه دهد و COMMIT کند، نیمی از کار ذخیره می‌شود. پس از 1205 همیشه صریحاً ROLLBACK کنید.</li>
<li>برخلاف 1205، پس از 1213 کل تراکنش برگردانده شده است؛ تکرار فقط آخرین دستور اشتباه است و باید از START TRANSACTION دوباره شروع کرد.</li>
<li>روی سرورهای با هم‌زمانی بسیار بالا، خود تشخیص deadlock گران می‌شود؛ <code>innodb_deadlock_detect = OFF</code> آن را خاموش می‌کند و به lock wait timeout تکیه می‌کند — فقط با timeout کوتاه و دانستن عواقب.</li>
<li>Deadlock می‌تواند فقط با یک ردیف و دو INSERT هم رخ دهد (به‌خاطر قفل اشتراکی روی کلید تکراری و سپس درخواست انحصاری)؛ اگر گزارش دو INSERT نشان داد، به کلیدهای UNIQUE مشکوک شوید.</li>
<li>کلید خارجی هم قفل می‌گیرد: درج در order_items یک قفل اشتراکی روی ردیف والد در orders می‌گذارد و می‌تواند با UPDATE هم‌زمان سفارش در چرخه‌ی deadlock بیفتد.</li>
</ul>""",
                },
                {
                    "title": "SELECT ... FOR UPDATE، SKIP LOCKED و ساخت صف کار و شماره‌ی فاکتور",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>قفل صریح، وقتی لازم است</h2>
<p><code>SELECT ... FOR UPDATE</code> ردیف‌های خوانده‌شده را با قفل انحصاری تا پایان تراکنش نگه می‌دارد؛ الگوی «بخوان، تصمیم بگیر، بنویس» را امن می‌کند. <code>FOR SHARE</code> قفل اشتراکی می‌گیرد: دیگران می‌توانند بخوانند اما نمی‌توانند تغییر دهند.</p>
<h3>شماره‌ی فاکتور پشت‌سرهم و بدون شکاف</h3>
<p>AUTO_INCREMENT شکاف دارد (فصل سوم). شماره‌ی فاکتور رسمی باید بدون شکاف و به تفکیک سال باشد:</p>
<pre><code class="language-sql">CREATE TABLE invoice_counters (
  fiscal_year SMALLINT UNSIGNED PRIMARY KEY,   -- 1404
  last_no     INT UNSIGNED NOT NULL
);

START TRANSACTION;
SELECT last_no FROM invoice_counters WHERE fiscal_year = 1404 FOR UPDATE;
UPDATE invoice_counters SET last_no = last_no + 1 WHERE fiscal_year = 1404;
INSERT INTO invoices (fiscal_year, invoice_no, order_id, amount)
SELECT 1404, last_no, 5531, 480000000 FROM invoice_counters WHERE fiscal_year = 1404;
COMMIT;</code></pre>
<p>اگر تراکنش ROLLBACK شود، شمارنده هم برمی‌گردد و شکافی نمی‌ماند. هزینه‌اش این است که صدور فاکتور سریالی می‌شود؛ پس این تراکنش را تا حد ممکن کوتاه نگه دارید.</p>
<h3>صف کار با SKIP LOCKED</h3>
<p>فرض کنید چند worker باید سفارش‌های تازه را برای کارخانه ارسال کنند. اگر همه با FOR UPDATE اولین کار آزاد را بخواهند، همه پشت یک ردیف صف می‌کشند. از 8.0 گزینه‌ی <code>SKIP LOCKED</code> ردیف‌های قفل‌شده را رد می‌کند و هر worker کار متفاوتی برمی‌دارد:</p>
<pre><code class="language-sql">CREATE TABLE jobs (
  id          BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  kind        VARCHAR(30) NOT NULL,
  payload     JSON NOT NULL,
  status      ENUM('pending','running','done','failed') NOT NULL DEFAULT 'pending',
  run_after   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  attempts    TINYINT UNSIGNED NOT NULL DEFAULT 0,
  INDEX ix_pick (status, run_after, id)
);

-- هر worker:
START TRANSACTION;
SELECT id, kind, payload FROM jobs
WHERE status = 'pending' AND run_after &lt;= NOW()
ORDER BY id
LIMIT 5
FOR UPDATE SKIP LOCKED;
UPDATE jobs SET status = 'running', attempts = attempts + 1 WHERE id IN (101, 102, 103);
COMMIT;
-- کار را انجام بده، سپس:
UPDATE jobs SET status = 'done' WHERE id = 101;</code></pre>
<p>تراکنش فقط برای «برداشتن» کار است و کوتاه می‌ماند؛ خود کار (ارسال پیامک، ساخت PDF) بیرون از تراکنش انجام می‌شود. برای کارهای «running» که worker آن‌ها مرده، یک ستون <code>locked_at</code> و یک کار دوره‌ای برای بازگرداندنشان لازم است.</p>
<h3>NOWAIT و رزرو موجودی</h3>
<pre><code class="language-sql">-- اگر کس دیگری در حال ویرایش سفارش است، فوراً خطا بده، منتظر نمان
SELECT * FROM orders WHERE id = 5531 FOR UPDATE NOWAIT;
-- ERROR 3572: Statement aborted because lock(s) could not be acquired immediately and NOWAIT is set.

-- رزرو اتمی موجودی بدون قفل صریح
UPDATE products SET stock = stock - 1 WHERE id = 7 AND stock &gt;= 1;
-- rows affected = 1 : رزرو شد ؛ 0 : ناموجود</code></pre>
<p>دستور آخر اتمی است: شرط و تغییر با هم انجام می‌شوند و موجودی هرگز منفی نمی‌شود، حتی با صد خرید هم‌زمان.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>FOR UPDATE بیرون از تراکنش (با autocommit روشن) بی‌معناست: قفل گرفته و بلافاصله با COMMIT خودکار آزاد می‌شود.</li>
<li>SKIP LOCKED نتیجه‌ی ناسازگار می‌دهد و برای صف مناسب است، نه برای گزارش یا محاسبه‌ی موجودی.</li>
<li>بدون ایندکسی مثل <code>(status, run_after, id)</code>، کوئری SKIP LOCKED کل جدول را پیمایش و قفل می‌کند و مزیتش از بین می‌رود.</li>
<li>در جنگو معادل این‌ها <code>select_for_update(skip_locked=True)</code> و <code>select_for_update(nowait=True)</code> است که فقط داخل <code>transaction.atomic()</code> کار می‌کند.</li>
<li>کارهای انجام‌شده را در جدول صف نگه ندارید؛ جدول jobs با میلیون‌ها ردیف done، اسکن‌ها و قفل‌ها را کند می‌کند. آن‌ها را به جدول آرشیو منتقل یا حذف کنید.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۷ ─────────────────────────────
        {
            "title": "فصل ۷: مدیریت و امنیت — کاربران، بکاپ، Replication و کد سمت سرور",
            "lessons": [
                {
                    "title": "کاربران، GRANT با اصل کمترین دسترسی و Roleها",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>اصل کمترین دسترسی در عمل</h2>
<p>در فصل اول یک کاربر ساده برای برنامه ساختیم. در محیط واقعی چند نوع مصرف‌کننده دارید: خود برنامه‌ی وب، فرمان مایگریشن، کاربر گزارش‌گیری که به ابزار BI وصل می‌شود، کاربر پشتیبان‌گیری و مدیر انسانی. اصل کمترین دسترسی می‌گوید هر کدام فقط همان مجوزی را بگیرد که کارش لازم دارد. اگر رمز برنامه‌ی وب از یک فایل <code>.env</code> نشت کرد، مهاجم نباید بتواند <code>DROP DATABASE</code> بزند یا دیتابیس سایت دیگری را که روی همان سرور است بخواند.</p>
<h3>سطوح مجوز</h3>
<table><thead><tr><th>سطح</th><th>نمونه</th><th>کاربرد</th></tr></thead><tbody>
<tr><td>سراسری</td><td><code>ON *.*</code></td><td>فقط برای مدیر، بکاپ و Replication</td></tr>
<tr><td>دیتابیس</td><td><code>ON carpet_factory.*</code></td><td>حالت معمول برای برنامه</td></tr>
<tr><td>جدول</td><td><code>ON carpet_factory.orders</code></td><td>کاربر گزارش یا سرویس جانبی</td></tr>
<tr><td>ستون</td><td><code>SELECT (id, city) ON ...customers</code></td><td>پنهان کردن موبایل و آدرس</td></tr>
<tr><td>روتین</td><td><code>EXECUTE ON PROCEDURE ...</code></td><td>اجازه‌ی اجرای یک رویه‌ی مشخص</td></tr>
</tbody></table>
<h3>نقش‌ها: مجوز را به نقش بدهید، نه به آدم</h3>
<p>از MySQL 8 می‌توان مجموعه‌ای از مجوزها را یک‌بار در قالب Role تعریف و به چند کاربر داد. وقتی کارمند جدیدی به واحد گزارش آمد، فقط نقش را به او می‌دهید.</p>
<pre><code class="language-sql">CREATE ROLE 'app_rw', 'app_migrate', 'report_ro';

GRANT SELECT, INSERT, UPDATE, DELETE ON carpet_factory.* TO 'app_rw';
GRANT ALTER, CREATE, DROP, INDEX, REFERENCES ON carpet_factory.* TO 'app_migrate';

GRANT SELECT ON carpet_factory.orders      TO 'report_ro';
GRANT SELECT ON carpet_factory.order_items TO 'report_ro';
GRANT SELECT (id, full_name, city) ON carpet_factory.customers TO 'report_ro';

CREATE USER 'web'@'10.0.0.%' IDENTIFIED BY 'Long-Random-Secret-1405'
  FAILED_LOGIN_ATTEMPTS 5 PASSWORD_LOCK_TIME 1;
CREATE USER 'sara_bi'@'10.0.0.25' IDENTIFIED BY 'Another-Long-Secret'
  PASSWORD EXPIRE INTERVAL 90 DAY;

GRANT 'app_rw'    TO 'web'@'10.0.0.%';
GRANT 'report_ro' TO 'sara_bi'@'10.0.0.25';
SET DEFAULT ROLE ALL TO 'web'@'10.0.0.%', 'sara_bi'@'10.0.0.25';

SHOW GRANTS FOR 'sara_bi'@'10.0.0.25' USING 'report_ro';</code></pre>
<p>برنامه‌ی جنگو در حالت عادی با نقش <code>app_rw</code> کار می‌کند و <code>manage.py migrate</code> در زمان استقرار با کاربر جداگانه‌ای اجرا می‌شود که <code>app_migrate</code> هم دارد. نقشی که به کاربر داده شده تا وقتی فعال نشود اثری ندارد؛ <code>SET DEFAULT ROLE</code> را فراموش نکنید و برای بررسی، <code>SELECT CURRENT_ROLE();</code> بزنید.</p>
<h3>بازبینی دوره‌ای</h3>
<pre><code class="language-sql">SELECT user, host, account_locked, password_last_changed
FROM mysql.user ORDER BY user;

ALTER USER 'old_intern'@'%' ACCOUNT LOCK;   -- قبل از حذف، مدتی قفل کنید
DROP USER 'old_intern'@'%';</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>در GRANT سطح دیتابیس، <code>_</code> و <code>%</code> wildcard هستند: <code>GRANT ... ON my_db.*</code> دیتابیس <code>myxdb</code> را هم شامل می‌شود. برای دقت بنویسید <code>my\_db</code>.</li>
<li><code>ALL ON carpet_factory.*</code> مجوز <code>DROP</code> را هم دارد؛ یعنی کاربر برنامه می‌تواند کل دیتابیس را حذف کند. همچنین TRIGGER و CREATE ROUTINE را می‌دهد که برای ماندگاری مهاجم کافی است.</li>
<li>مجوز سراسری <code>FILE</code> اجازه‌ی خواندن فایل‌های سرور با <code>LOAD_FILE()</code> را می‌دهد؛ هرگز به کاربر برنامه ندهید و <code>secure_file_priv</code> را خالی نگذارید.</li>
<li>با <code>partial_revokes = ON</code> می‌توان «همه به‌جز» ساخت: <code>GRANT SELECT ON *.*</code> و سپس <code>REVOKE SELECT ON mysql.*</code>.</li>
<li><code>'web'@'localhost'</code> و <code>'web'@'%'</code> دو حساب جدا با رمز و مجوز جدا هستند؛ MySQL هنگام ورود، خاص‌ترین host را انتخاب می‌کند، نه حسابی را که شما در ذهن دارید.</li>
<li>متغیر <code>mandatory_roles</code> نقشی را به همه‌ی کاربران می‌دهد و <code>activate_all_roles_on_login = ON</code> نیاز به SET DEFAULT ROLE را برمی‌دارد.</li>
</ul>""",
                },
                {
                    "title": "احراز هویت caching_sha2_password، TLS و کلاینت‌های قدیمی",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>چرا برنامه‌ی قدیمی بعد از ارتقا وصل نمی‌شود؟</h2>
<p>از MySQL 8.0 پلاگین پیش‌فرض احراز هویت <strong>caching_sha2_password</strong> است که از SHA-256 و نمک استفاده می‌کند و بسیار امن‌تر از <code>mysql_native_password</code> قدیمی (SHA-1) است. کلاینت‌های قدیمی مثل PHP پیش از 7.4، Connector/J سری 5.1، نسخه‌های قدیمی Navicat یا نرم‌افزارهای حسابداری ده سال پیش این پلاگین را نمی‌شناسند و با پیام‌هایی مثل <code>Authentication plugin 'caching_sha2_password' cannot be loaded</code> یا <code>The server requested authentication method unknown to the client</code> شکست می‌خورند.</p>
<p>در MySQL 8.4 پلاگین قدیمی به‌طور پیش‌فرض <em>غیرفعال</em> است و در نسخه‌های 9 کاملاً حذف شده؛ پس راه درست، ارتقای کلاینت است و فعال کردن پلاگین قدیمی فقط یک راه موقت.</p>
<pre><code class="language-sql">-- چه کسی با چه پلاگینی وارد می‌شود؟
SELECT user, host, plugin FROM mysql.user;

-- راه موقت برای یک نرم‌افزار قدیمی (در 8.4 اول در my.cnf بنویسید: mysql_native_password=ON)
ALTER USER 'legacy_erp'@'10.0.0.40'
  IDENTIFIED WITH mysql_native_password BY 'Temp-Secret-Until-Upgrade';

-- اجبار رمزنگاری برای یک کاربر یا کل سرور
ALTER USER 'sara_bi'@'10.0.0.25' REQUIRE SSL;
SET PERSIST require_secure_transport = ON;</code></pre>
<h3>caching_sha2 چطور کار می‌کند</h3>
<p>اولین ورود هر کاربر باید روی کانال امن انجام شود: TLS، سوکت یونیکس یا تبادل رمز با کلید عمومی RSA سرور. پس از ورود موفق، چکیده‌ی رمز در حافظه‌ی سرور cache می‌شود و ورودهای بعدی سریع‌اند. این cache با ری‌استارت سرور خالی می‌شود؛ به همین دلیل گاهی برنامه‌ای که هفته‌ها بدون TLS کار می‌کرد، بعد از ری‌استارت با <code>Authentication requires secure connection</code> قطع می‌شود.</p>
<pre><code class="language-bash">mysql -h 10.0.0.11 -u web -p --ssl-mode=VERIFY_CA --ssl-ca=/etc/mysql/ca.pem
# اگر TLS ندارید (فقط در شبکه‌ی داخلی مطمئن):
mysql -h 10.0.0.11 -u web -p --get-server-public-key</code></pre>
<p>در JDBC معادل گزینه‌ی دوم <code>allowPublicKeyRetrieval=true</code> است.</p>
<h3>حالت‌های TLS در کلاینت</h3>
<table><thead><tr><th>ssl-mode</th><th>رمزنگاری</th><th>بررسی هویت سرور</th></tr></thead><tbody>
<tr><td>PREFERRED (پیش‌فرض)</td><td>اگر سرور پشتیبانی کند</td><td>خیر</td></tr>
<tr><td>REQUIRED</td><td>اجباری</td><td>خیر</td></tr>
<tr><td>VERIFY_CA</td><td>اجباری</td><td>گواهی توسط CA شما امضا شده باشد</td></tr>
<tr><td>VERIFY_IDENTITY</td><td>اجباری</td><td>CA و تطابق نام میزبان</td></tr>
</tbody></table>
<p>MySQL 8 در اولین راه‌اندازی گواهی self-signed می‌سازد، پس اتصال‌ها معمولاً رمز شده‌اند؛ اما بدون VERIFY_CA جلوی حمله‌ی مرد میانی گرفته نمی‌شود. برای دیدن وضعیت اتصال فعلی: <code>SHOW SESSION STATUS LIKE 'Ssl_cipher';</code></p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>اتصال با سوکت (host برابر <code>localhost</code> در لینوکس) امن حساب می‌شود؛ برای همین caching_sha2 روی خود سرور بی‌دردسر است و از ماشین دیگر خطا می‌دهد.</li>
<li>چرخش رمز بدون قطعی: <code>ALTER USER 'web'@'10.0.0.%' IDENTIFIED BY 'New' RETAIN CURRENT PASSWORD;</code> سپس برنامه‌ها را یکی‌یکی به‌روز کنید و در پایان <code>ALTER USER ... DISCARD OLD PASSWORD;</code></li>
<li>متغیر <code>default_authentication_plugin</code> منسوخ شده و در 8.4 وجود ندارد؛ جایگزینش <code>authentication_policy</code> است.</li>
<li>رمز را در اسکریپت‌های cron ننویسید؛ <code>mysql_config_editor set --login-path=backup ...</code> آن را در فایل مبهم‌شده‌ی <code>.mylogin.cnf</code> نگه می‌دارد و با <code>--login-path=backup</code> استفاده می‌شود.</li>
<li>کامپوننت <code>validate_password</code> با <code>INSTALL COMPONENT 'file://component_validate_password';</code> نصب می‌شود و رمزهای ضعیف را در CREATE USER رد می‌کند.</li>
</ul>""",
                },
                {
                    "title": "پشتیبان‌گیری: mysqldump --single-transaction و MySQL Shell dump",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>بکاپی که بازیابی‌اش را امتحان نکرده‌اید، بکاپ نیست</h2>
<p>بیشتر حادثه‌های از دست رفتن داده به‌خاطر نبودن بکاپ نیست؛ به‌خاطر بکاپی است که ناقص، خراب یا غیرقابل بازیابی بوده و کسی تا روز حادثه امتحانش نکرده بود. دو خانواده‌ی اصلی بکاپ داریم:</p>
<table><thead><tr><th></th><th>منطقی (mysqldump، MySQL Shell)</th><th>فیزیکی (XtraBackup، Clone، snapshot دیسک)</th></tr></thead><tbody>
<tr><td>خروجی</td><td>دستورهای SQL یا فایل‌های داده‌ی متنی</td><td>کپی فایل‌های InnoDB</td></tr>
<tr><td>سرعت روی ۲۰۰ گیگ</td><td>کند، به‌ویژه بازیابی</td><td>سریع</td></tr>
<tr><td>انتقال بین نسخه‌ها</td><td>آسان</td><td>معمولاً فقط همان نسخه</td></tr>
<tr><td>بازیابی یک جدول</td><td>آسان</td><td>دشوارتر</td></tr>
</tbody></table>
<h3>mysqldump درست</h3>
<pre><code class="language-bash">mysqldump --login-path=backup \
  --single-transaction --routines --events --triggers \
  --source-data=2 --set-gtid-purged=AUTO \
  --default-character-set=utf8mb4 --hex-blob \
  --databases carpet_factory \
  | gzip &gt; /backup/carpet_factory_$(date +%F).sql.gz

# بازیابی
gunzip &lt; /backup/carpet_factory_2026-10-01.sql.gz | mysql --login-path=admin</code></pre>
<p><code>--single-transaction</code> یک snapshot سازگار با REPEATABLE READ می‌گیرد و جدول‌های InnoDB را قفل نمی‌کند؛ سایت در طول بکاپ کار می‌کند. <code>--source-data=2</code> (جایگزین <code>--master-data</code> از 8.0.26) مختصات binlog را به‌صورت کامنت در فایل می‌نویسد که در درس بعد برای بازیابی لحظه‌ای لازم است.</p>
<pre><code class="language-sql">CREATE USER 'backup'@'localhost' IDENTIFIED BY 'Backup-Secret';
GRANT SELECT, SHOW VIEW, TRIGGER, EVENT, LOCK TABLES, RELOAD,
      PROCESS, REPLICATION CLIENT, BACKUP_ADMIN ON *.* TO 'backup'@'localhost';</code></pre>
<h3>MySQL Shell: بکاپ منطقی موازی</h3>
<p>ابزار <code>mysqlsh</code> بکاپ را با چند thread و فشرده‌سازی zstd می‌گیرد و بازیابی‌اش چند برابر سریع‌تر از اجرای یک فایل SQL بزرگ است:</p>
<pre><code class="language-javascript">// mysqlsh backup@localhost --js
util.dumpSchemas(["carpet_factory"], "/backup/shell/2026-10-01",
                 {threads: 8, compression: "zstd"})
util.dumpInstance("/backup/shell/full-2026-10-01", {threads: 8})

// روی سرور مقصد (local_infile باید ON باشد)
util.loadDump("/backup/shell/2026-10-01", {threads: 8, dryRun: true})
util.loadDump("/backup/shell/2026-10-01", {threads: 8})</code></pre>
<h3>برنامه‌ی نگهداری</h3>
<p>قاعده‌ی 3-2-1: سه نسخه، روی دو رسانه‌ی مختلف، یکی بیرون از سرور. بکاپ شبانه با cron، نگهداری ۱۴ روزه با <code>find /backup -name '*.sql.gz' -mtime +14 -delete</code> و هر ماه یک بازیابی آزمایشی روی سرور جداگانه که با یک کوئری شمارش ردیف‌ها تأیید شود.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>mysqldump بدون <code>--single-transaction</code> به‌طور پیش‌فرض <code>--lock-tables</code> می‌زند؛ یعنی در طول بکاپ هیچ سفارشی ثبت نمی‌شود.</li>
<li>اگر وسط dump یک <code>ALTER TABLE</code> اجرا شود، snapshot شکسته می‌شود و خطای <code>Table definition has changed</code> یا جدول ناقص می‌گیرید؛ مایگریشن و بکاپ را هم‌زمان نگذارید.</li>
<li>خطای <code>Access denied; you need the PROCESS privilege</code> در نسخه‌های جدید با <code>--no-tablespaces</code> برطرف می‌شود اگر نمی‌خواهید PROCESS بدهید.</li>
<li>dumpی که DEFINER آن کاربری ناموجود است، بعد از بازیابی تریگر و View را با ERROR 1449 از کار می‌اندازد؛ در MySQL Shell گزینه‌ی <code>compatibility: ["strip_definers"]</code> این را حل می‌کند.</li>
<li>برای بارگذاری اولیه‌ی یک سرور تازه، <code>ALTER INSTANCE DISABLE INNODB REDO_LOG;</code> سرعت را چند برابر می‌کند؛ فقط برای همان لحظه و هرگز روی سرور در حال سرویس.</li>
<li>هنگام وارد کردن dump در سروری که GTID اجراشده دارد، <code>--set-gtid-purged=OFF</code> بگیرید وگرنه بازیابی با خطای GTID_PURGED متوقف می‌شود.</li>
</ul>""",
                },
                {
                    "title": "binlog و بازیابی لحظه‌ای (Point-in-Time Recovery)",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>ساعت ۱۴:۳۷ کسی جدول سفارش‌ها را پاک کرد</h2>
<p>بکاپ کامل ساعت ۲ بامداد گرفته شده. ساعت ۱۴:۳۷ یک نفر در DBeaver یک <code>DELETE</code> بدون WHERE روی جدول <code>orders</code> زده است. اگر فقط بکاپ شبانه را برگردانید، دوازده ساعت سفارش از دست می‌رود. <strong>binlog</strong> همه‌ی تغییرات بعد از بکاپ را نگه داشته؛ کافی است بکاپ را برگردانید و binlog را تا درست قبل از دستور مخرب دوباره اجرا کنید.</p>
<h3>تنظیم binlog</h3>
<p>در MySQL 8 binlog به‌طور پیش‌فرض روشن و با فرمت ROW است. تنظیمات توصیه‌شده:</p>
<pre><code class="language-ini">[mysqld]
server_id                  = 1
log_bin                    = /var/lib/mysql/binlog
binlog_format              = ROW
binlog_expire_logs_seconds = 1209600   # 14 روز
sync_binlog                = 1</code></pre>
<pre><code class="language-sql">SHOW BINARY LOGS;
SHOW BINARY LOG STATUS;    -- 8.4؛ در 8.0: SHOW MASTER STATUS
FLUSH BINARY LOGS;         -- بستن فایل فعلی و شروع فایل تازه
PURGE BINARY LOGS BEFORE NOW() - INTERVAL 14 DAY;</code></pre>
<h3>بازیابی قدم‌به‌قدم</h3>
<pre><code class="language-bash"># 1) مختصات binlog در لحظه‌ی بکاپ (از --source-data=2)
zcat /backup/carpet_factory_2026-10-01.sql.gz | head -60 | grep -m1 'LOG_POS'
# -- CHANGE REPLICATION SOURCE TO SOURCE_LOG_FILE='binlog.000412', SOURCE_LOG_POS=1543;

# 2) پیدا کردن موقعیت دستور مخرب
mysqlbinlog --base64-output=DECODE-ROWS -vv \
  --start-datetime='2026-10-01 14:30:00' /var/lib/mysql/binlog.000415 \
  | grep -n -B 30 '### DELETE FROM `carpet_factory`.`orders`' | grep '# at'

# 3) بازیابی بکاپ کامل روی یک سرور جداگانه
gunzip &lt; /backup/carpet_factory_2026-10-01.sql.gz | mysql --login-path=admin

# 4) اجرای binlogها تا قبل از دستور مخرب، در یک فراخوانی
mysqlbinlog --start-position=1543 --stop-position=88213 \
  binlog.000412 binlog.000413 binlog.000414 binlog.000415 \
  | mysql --login-path=admin</code></pre>
<p>بهتر است بازیابی را روی سرور جداگانه انجام دهید، داده‌ی سالم را بررسی کنید و سپس فقط جدول آسیب‌دیده را به سرور اصلی برگردانید؛ این‌طور سفارش‌هایی که بعد از ۱۴:۳۷ ثبت شده‌اند هم حفظ می‌شوند.</p>
<h3>راه دوم با GTID</h3>
<p>اگر GTID روشن است، می‌توانید به‌جای توقف، فقط همان یک تراکنش را کنار بگذارید و بقیه را اجرا کنید: <code>mysqlbinlog --exclude-gtids='3e11fa47-...:9921' ...</code>. شناسه‌ی GTID در خروجی مرحله‌ی ۲ کنار <code>SET @@SESSION.GTID_NEXT</code> دیده می‌شود.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>--start-position</code> فقط به اولین فایل و <code>--stop-position</code> فقط به آخرین فایل فهرست اعمال می‌شود؛ ترتیب فایل‌ها را درست بدهید.</li>
<li><code>--stop-datetime</code> با منطقه‌ی زمانی ماشینی تفسیر می‌شود که mysqlbinlog روی آن اجرا شده؛ اختلاف ساعت تهران و UTC یعنی سه ساعت و نیم داده‌ی اضافه یا کم.</li>
<li>همه‌ی فایل‌ها را در یک فراخوانی mysqlbinlog بدهید؛ اجرای جداگانه‌ی هر فایل جدول‌های موقت بین فایل‌ها را از دست می‌دهد.</li>
<li><code>binlog_expire_logs_seconds</code> باید از فاصله‌ی دو بکاپ کامل بیشتر باشد؛ وگرنه بین آخرین بکاپ و قدیمی‌ترین binlog شکاف می‌افتد و PITR ممکن نیست.</li>
<li>binlog روی همان دیسک داده، با خرابی دیسک از بین می‌رود. <code>mysqlbinlog --read-from-remote-server --raw --stop-never</code> روی سرور دیگری binlogها را لحظه‌به‌لحظه کپی می‌کند.</li>
<li>اگر binlogها را روی همان سروری اجرا کنید که GTIDهایشان از قبل در <code>gtid_executed</code> هست، تراکنش‌ها بی‌صدا رد می‌شوند؛ در آن حالت <code>--skip-gtids</code> لازم است.</li>
</ul>""",
                },
                {
                    "title": "Replication مقدماتی با GTID",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>سرور دومی که همیشه به‌روز است</h2>
<p>Replication یعنی یک سرور (source) تغییرات را در binlog می‌نویسد و سرور دیگر (replica) آن‌ها را می‌خواند و اجرا می‌کند. کاربردهای رایج: انتقال گزارش‌های سنگین مدیریتی به replica تا سایت کند نشود، گرفتن بکاپ از replica، و داشتن سرور آماده برای جایگزینی در صورت خرابی. در replica دو thread کار می‌کنند: <strong>IO thread</strong> که رویدادها را از source می‌گیرد و در relay log می‌نویسد، و <strong>SQL (applier) thread</strong> که آن‌ها را اجرا می‌کند.</p>
<p><strong>GTID</strong> به هر تراکنش شناسه‌ای یکتا به شکل <code>server_uuid:شماره</code> می‌دهد. با GTID دیگر لازم نیست نام فایل و موقعیت binlog را دستی پیدا کنید؛ replica خودش می‌داند کدام تراکنش‌ها را اجرا کرده و از کجا ادامه دهد (auto-positioning).</p>
<h3>پیکربندی</h3>
<pre><code class="language-ini"># source: 10.0.0.11
[mysqld]
server_id                = 1
gtid_mode                = ON
enforce_gtid_consistency = ON
log_bin                  = binlog

# replica: 10.0.0.12
[mysqld]
server_id                = 2
gtid_mode                = ON
enforce_gtid_consistency = ON
log_bin                  = binlog
read_only                = ON
super_read_only          = ON
relay_log_recovery       = ON</code></pre>
<pre><code class="language-sql">-- روی source
CREATE USER 'repl'@'10.0.0.12' IDENTIFIED BY 'Repl-Secret' REQUIRE SSL;
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'10.0.0.12';</code></pre>
<p>داده‌ی اولیه را با mysqldump (با <code>--source-data=2 --set-gtid-purged=ON</code> و <code>--all-databases</code>) یا ساده‌تر با Clone plugin به replica منتقل کنید: <code>CLONE INSTANCE FROM 'clone_user'@'10.0.0.11':3306 IDENTIFIED BY '...';</code> که کل داده و وضعیت GTID را یکجا کپی می‌کند.</p>
<pre><code class="language-sql">-- روی replica
CHANGE REPLICATION SOURCE TO
  SOURCE_HOST = '10.0.0.11',
  SOURCE_USER = 'repl',
  SOURCE_PASSWORD = 'Repl-Secret',
  SOURCE_AUTO_POSITION = 1,
  SOURCE_SSL = 1;
START REPLICA;
SHOW REPLICA STATUS\G</code></pre>
<p>در خروجی، <code>Replica_IO_Running</code> و <code>Replica_SQL_Running</code> باید هر دو <code>Yes</code> باشند. <code>Seconds_Behind_Source</code> تأخیر را نشان می‌دهد و <code>Last_SQL_Error</code> علت توقف را.</p>
<h3>خواندن از replica در برنامه</h3>
<p>در جنگو با یک Database Router می‌توان گزارش‌ها را به replica فرستاد. حواستان به تأخیر باشد: کاربری که همین الان سفارش ثبت کرده، اگر صفحه‌ی «سفارش‌های من» از replica خوانده شود، ممکن است سفارشش را نبیند.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>Replication بکاپ نیست: <code>DROP TABLE</code> در کسری از ثانیه روی replica هم اجرا می‌شود. یک replica تأخیری با <code>SOURCE_DELAY = 3600</code> یک ساعت فرصت نجات می‌دهد.</li>
<li><code>read_only</code> جلوی کاربران دارای SUPER یا CONNECTION_ADMIN را نمی‌گیرد؛ <code>super_read_only</code> لازم است تا مدیری اشتباهی روی replica ننویسد.</li>
<li>اگر پوشه‌ی داده یا ماشین مجازی را کپی کرده‌اید، فایل <code>auto.cnf</code> را حذف کنید؛ دو سرور با <code>server_uuid</code> یکسان رفتارهای عجیب و بی‌صدا ایجاد می‌کنند.</li>
<li>با GTID متغیر <code>sql_replica_skip_counter</code> کار نمی‌کند؛ برای رد کردن یک تراکنش مشکل‌دار یک تراکنش خالی با همان GTID تزریق کنید: <code>SET GTID_NEXT='uuid:N'; BEGIN; COMMIT; SET GTID_NEXT='AUTOMATIC';</code></li>
<li><code>Seconds_Behind_Source = 0</code> وقتی IO thread قطع است هم ممکن است دیده شود؛ همیشه وضعیت هر دو thread را با هم پایش کنید.</li>
<li>از 8.0.27 اجرای موازی روی replica با <code>replica_parallel_workers = 4</code> پیش‌فرض است و تأخیر را در بار سنگین کم می‌کند.</li>
</ul>""",
                },
                {
                    "title": "Stored Procedure، Function، Trigger و Event: کِی استفاده کنیم؟",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>منطق داخل دیتابیس: ابزاری دولبه</h2>
<p>MySQL می‌تواند کد را خودش اجرا کند: رویه (Procedure)، تابع (Function)، تریگر و رویداد زمان‌بندی‌شده (Event). این ابزارها قدرتمندند، اما منطقی که داخل دیتابیس است در git و code review و تست‌های برنامه کمتر دیده می‌شود و ORM جنگو از آن خبر ندارد.</p>
<table><thead><tr><th>ابزار</th><th>مناسب برای</th><th>نامناسب برای</th></tr></thead><tbody>
<tr><td>Procedure</td><td>عملیات دسته‌ای نزدیک داده، بستن ماه مالی</td><td>منطق کسب‌وکار روزمره</td></tr>
<tr><td>Function</td><td>محاسبه‌ی کوچک و قطعی مثل متراژ</td><td>کوئری درون تابع که در WHERE صدا زده شود</td></tr>
<tr><td>Trigger</td><td>یکدست‌سازی داده، لاگ ممیزی</td><td>ارسال پیامک یا منطق پیچیده</td></tr>
<tr><td>Event</td><td>پاک‌سازی دوره‌ای جدول‌ها</td><td>کارهایی که نیاز به پایش و تکرار دارند</td></tr>
</tbody></table>
<h3>Procedure با خطای کنترل‌شده</h3>
<pre><code class="language-sql">DELIMITER $$
CREATE PROCEDURE reserve_stock(IN p_product_id INT UNSIGNED, IN p_qty INT UNSIGNED)
BEGIN
  UPDATE products SET stock = stock - p_qty
   WHERE id = p_product_id AND stock &gt;= p_qty;
  IF ROW_COUNT() = 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'insufficient stock';
  END IF;
END$$
DELIMITER ;

CALL reserve_stock(7, 2);</code></pre>
<h3>Function و Trigger</h3>
<pre><code class="language-sql">CREATE FUNCTION carpet_area_m2(p_width_cm INT, p_length_cm INT)
RETURNS DECIMAL(8,2) DETERMINISTIC NO SQL
RETURN ROUND(p_width_cm * p_length_cm / 10000, 2);

-- یکدست کردن ی و ک عربی پیش از ذخیره
DELIMITER $$
CREATE TRIGGER customers_bi BEFORE INSERT ON customers
FOR EACH ROW
BEGIN
  SET NEW.full_name = REPLACE(REPLACE(NEW.full_name, 'ي', 'ی'), 'ك', 'ک');
END$$
DELIMITER ;</code></pre>
<p>همین تریگر را برای <code>BEFORE UPDATE</code> هم بسازید؛ وگرنه ویرایش نام دوباره حروف عربی را وارد می‌کند. تریگر در این‌جا مناسب است چون داده از چند مسیر (پنل، API، ورود از اکسل) وارد می‌شود و دیتابیس تنها نقطه‌ی مشترک است.</p>
<h3>Event: نظافت شبانه</h3>
<pre><code class="language-sql">CREATE EVENT purge_done_jobs
  ON SCHEDULE EVERY 1 DAY STARTS '2026-10-03 03:30:00'
  DO DELETE FROM jobs
     WHERE status = 'done' AND finished_at &lt; NOW() - INTERVAL 30 DAY;

SHOW EVENTS FROM carpet_factory;</code></pre>
<p>قاعده‌ی سرانگشتی: قیدهایی که «هر برنامه‌ای» باید رعایت کند و پاک‌سازی‌های ساده را در دیتابیس بگذارید؛ منطق کسب‌وکار را در کد برنامه که تست و نسخه‌بندی می‌شود.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>تریگرها برای تغییراتی که با <code>ON DELETE CASCADE</code> کلید خارجی انجام می‌شوند اجرا <em>نمی‌شوند</em>؛ لاگ ممیزی مبتنی بر تریگر این حذف‌ها را نمی‌بیند.</li>
<li>با binlog روشن، ساخت تابع بدون یکی از عبارت‌های <code>DETERMINISTIC</code>، <code>NO SQL</code> یا <code>READS SQL DATA</code> خطای 1418 می‌دهد.</li>
<li><code>DELIMITER</code> دستور کلاینت <code>mysql</code> است، نه SQL؛ در <code>RunSQL</code> مایگریشن جنگو یا درایور پایتون، CREATE PROCEDURE را بدون آن و به‌صورت یک دستور بفرستید.</li>
<li>روتین‌ها به‌طور پیش‌فرض با مجوزهای DEFINER اجرا می‌شوند؛ اگر آن کاربر حذف شود، با ERROR 1449 از کار می‌افتند. <code>SQL SECURITY INVOKER</code> این وابستگی را برمی‌دارد.</li>
<li>Eventها روی replica با وضعیت <code>SLAVESIDE_DISABLED</code> ساخته می‌شوند تا دوبار اجرا نشوند؛ بعد از جایگزینی replica به‌جای source، آن‌ها را دستی فعال کنید.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۸ ─────────────────────────────
        {
            "title": "فصل ۸: تنظیم، اتصال به برنامه و پروژه‌ی پایانی",
            "lessons": [
                {
                    "title": "تنظیمات کلیدی سرور: buffer pool، max_connections و redo log",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>چند تنظیم که بیشترِ اثر را دارند</h2>
<p>MySQL صدها متغیر دارد، اما روی یک سرور معمولی سه چهار تنظیم بیشترین اثر را می‌گذارند. پیش‌فرض‌ها برای ماشینی کوچک انتخاب شده‌اند؛ مثلاً buffer pool پیش‌فرض فقط ۱۲۸ مگابایت است، حتی اگر سرور شما ۳۲ گیگابایت حافظه داشته باشد.</p>
<h3>نمونه‌ی my.cnf برای سرور اختصاصی ۱۶ گیگابایتی</h3>
<pre><code class="language-ini">[mysqld]
innodb_buffer_pool_size        = 11G
innodb_redo_log_capacity       = 2G     # از 8.0.30
innodb_flush_log_at_trx_commit = 1
max_connections                = 300
wait_timeout                   = 600
table_open_cache               = 4000
slow_query_log                 = ON
long_query_time                = 1</code></pre>
<table><thead><tr><th>تنظیم</th><th>چه می‌کند</th><th>قاعده‌ی سرانگشتی</th></tr></thead><tbody>
<tr><td>innodb_buffer_pool_size</td><td>cache صفحه‌های داده و ایندکس</td><td>۵۰ تا ۷۵ درصد RAM روی سرور اختصاصی</td></tr>
<tr><td>innodb_redo_log_capacity</td><td>حجم redo log؛ کوچک باشد، flushهای پیاپی و افت نوشتن</td><td>به اندازه‌ی حدود یک ساعت نوشتن</td></tr>
<tr><td>innodb_flush_log_at_trx_commit</td><td>۱: هر COMMIT روی دیسک؛ ۲: هر ثانیه</td><td>برای داده‌ی مالی همیشه ۱</td></tr>
<tr><td>max_connections</td><td>سقف اتصال هم‌زمان (پیش‌فرض ۱۵۱)</td><td>بر اساس pool برنامه، نه حدس</td></tr>
</tbody></table>
<h3>اندازه‌گیری، نه حدس</h3>
<pre><code class="language-sql">-- نسبت خواندن از دیسک به کل خواندن‌ها؛ باید زیر یک درصد باشد
SHOW GLOBAL STATUS LIKE 'Innodb_buffer_pool_read%';

-- بیشترین اتصال هم‌زمانی که تا امروز رخ داده
SHOW GLOBAL STATUS LIKE 'Max_used_connections';
SHOW GLOBAL STATUS LIKE 'Threads_running';

-- حجم redo نوشته‌شده؛ دو بار با فاصله‌ی یک ساعت بگیرید و تفاضل را ببینید
SHOW GLOBAL STATUS LIKE 'Innodb_os_log_written';

-- چه چیزی حافظه را گرفته؟
SELECT * FROM sys.memory_global_by_current_bytes LIMIT 10;

-- تغییر بدون ری‌استارت
SET PERSIST innodb_buffer_pool_size = 12884901888;
SET PERSIST innodb_redo_log_capacity = 2147483648;</code></pre>
<p>اگر سرور فقط برای MySQL است، <code>innodb_dedicated_server = ON</code> اندازه‌ی buffer pool و redo log را بر اساس RAM خودکار تعیین می‌کند. روی VPS اشتراکی که جنگو و Nginx و Redis هم روی آن‌اند، این گزینه را روشن نکنید و حافظه را دستی تقسیم کنید.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>بافرهای <code>sort_buffer_size</code> و <code>join_buffer_size</code> برای هر اتصال (و گاهی هر عملیات) جدا گرفته می‌شوند؛ بالا بردن سراسری‌شان با ۳۰۰ اتصال، سرور را به دست OOM killer می‌سپارد. برای یک گزارش سنگین فقط در همان session افزایش دهید.</li>
<li><code>innodb_flush_log_at_trx_commit = 2</code> با کرش خود mysqld داده از دست نمی‌دهد؛ فقط با کرش سیستم‌عامل یا قطع برق تا حدود یک ثانیه تراکنش از بین می‌رود.</li>
<li>عدد مهم <code>Threads_running</code> است، نه <code>Threads_connected</code>؛ صدها اتصال بی‌کار ارزان‌اند، اما بیش از چند برابر تعداد هسته کوئری فعال یعنی صف و کندی.</li>
<li>buffer pool هنگام خاموشی فهرست صفحه‌های داغ را ذخیره و در راه‌اندازی بعدی بارگذاری می‌کند (<code>innodb_buffer_pool_dump_at_shutdown</code>)؛ برای همین بعد از ری‌استارت چند دقیقه طول می‌کشد تا سرعت عادی برگردد.</li>
<li>در داکر، اگر برای کانتینر محدودیت حافظه گذاشته‌اید، buffer pool را بر اساس همان محدودیت تنظیم کنید؛ وگرنه کانتینر بی‌صدا kill و ری‌استارت می‌شود.</li>
</ul>""",
                },
                {
                    "title": "اتصال از پایتون و جنگو: mysqlclient یا PyMySQL، و OPTIONS درست",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>دو درایور، یک رابط</h2>
<p>هر دو درایور اصلی پایتون رابط استاندارد DB-API را پیاده می‌کنند، پس کد شما تقریباً یکسان است؛ تفاوت در نصب و سرعت است.</p>
<table><thead><tr><th></th><th>mysqlclient</th><th>PyMySQL</th></tr></thead><tbody>
<tr><td>پیاده‌سازی</td><td>افزونه‌ی C روی libmysqlclient</td><td>پایتون خالص</td></tr>
<tr><td>سرعت</td><td>سریع‌تر</td><td>کندتر در نتایج بزرگ</td></tr>
<tr><td>نصب</td><td>در لینوکس به کامپایلر و هدرها نیاز دارد</td><td>همیشه بی‌دردسر</td></tr>
<tr><td>جنگو</td><td>درایور توصیه‌شده‌ی رسمی</td><td>با install_as_MySQLdb</td></tr>
</tbody></table>
<pre><code class="language-bash"># اوبونتو و دبیان
sudo apt install python3-dev default-libmysqlclient-dev build-essential pkg-config
pip install mysqlclient

# جایی که کامپایل ممکن نیست (مثلاً هاست اشتراکی)
pip install PyMySQL</code></pre>
<pre><code class="language-python"># config/__init__.py  (فقط اگر PyMySQL را انتخاب کرده‌اید)
import pymysql
pymysql.install_as_MySQLdb()</code></pre>
<h3>تنظیم DATABASES</h3>
<pre><code class="language-python">DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "carpet_factory",
        "USER": "web",
        "PASSWORD": os.environ["DB_PASSWORD"],
        "HOST": "127.0.0.1",
        "PORT": "3306",
        "CONN_MAX_AGE": 60,
        "CONN_HEALTH_CHECKS": True,
        "OPTIONS": {
            "charset": "utf8mb4",
            "init_command": (
                "SET sql_mode='STRICT_TRANS_TABLES,ONLY_FULL_GROUP_BY,"
                "NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,"
                "NO_ENGINE_SUBSTITUTION'"
            ),
            "isolation_level": "read committed",
        },
        "TEST": {"CHARSET": "utf8mb4", "COLLATION": "utf8mb4_0900_ai_ci"},
    }
}</code></pre>
<p><strong>charset</strong> مجموعه‌کاراکتر <em>اتصال</em> را تعیین می‌کند؛ اگر جدول utf8mb4 باشد اما اتصال نباشد، ایموجی در نام محصول یا نظر مشتری خطا می‌دهد. <strong>STRICT_TRANS_TABLES</strong> باعث می‌شود رشته‌ی بلندتر از ستون یا عدد نامعتبر به‌جای بریده شدن بی‌صدا خطا بدهد؛ جنگو بدون آن هشدار <code>mysql.W002</code> می‌دهد. <strong>isolation_level</strong> را جنگو به‌طور پیش‌فرض read committed می‌گذارد که با الگوی ORM سازگارتر است.</p>
<h3>کوئری خام امن</h3>
<pre><code class="language-python">from django.db import connection

with connection.cursor() as cur:
    cur.execute(
        "SELECT id, status FROM production_jobs WHERE loom_id = %s AND status = %s",
        [loom_id, "weaving"],
    )
    rows = cur.fetchall()</code></pre>
<p>هرگز مقدار را با f-string داخل SQL نگذارید؛ placeholder ‏<code>%s</code> را درایور به‌درستی escape می‌کند.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>HOST = "localhost"</code> با سوکت یونیکس وصل می‌شود و <code>"127.0.0.1"</code> با TCP؛ این دو از دید MySQL حساب‌های متفاوت‌اند و منشأ رایج Access denied.</li>
<li>init_command کل sql_mode را جایگزین می‌کند؛ اگر فقط <code>STRICT_TRANS_TABLES</code> بنویسید، ONLY_FULL_GROUP_BY و بقیه‌ی حالت‌های پیش‌فرض خاموش می‌شوند.</li>
<li>با <code>USE_TZ = True</code> و <code>TIME_ZONE = "Asia/Tehran"</code>، lookupهایی مثل <code>__date</code> بدون بارگذاری جدول‌های منطقه‌ی زمانی نتیجه‌ی خالی می‌دهند: <code>mysql_tzinfo_to_sql /usr/share/zoneinfo | sudo mysql mysql</code></li>
<li>ایندکس روی <code>CharField(unique=True, max_length=1000)</code> با utf8mb4 خطای <code>Specified key was too long</code> می‌دهد؛ سقف کلید ۳۰۷۲ بایت، یعنی ۷۶۸ کاراکتر است.</li>
<li>در ویندوز، mysqlclient چرخ (wheel) آماده دارد و کامپایلر نمی‌خواهد؛ اگر به‌خاطر تحریم دسترسی به PyPI کند است، با <code>pip config set global.index-url</code> از یک میرور داخلی استفاده کنید.</li>
</ul>""",
                },
                {
                    "title": "Connection Pooling و مدیریت اتصال‌ها",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>چرا اتصال را دوباره استفاده کنیم؟</h2>
<p>هر اتصال تازه یعنی handshake شبکه، احتمالاً TLS، احراز هویت و ساخت thread در سرور: چند میلی‌ثانیه برای هر درخواست. در بار بالا هم مسئله فقط زمان نیست؛ تعداد اتصال‌ها به <code>max_connections</code> می‌رسد و کاربران خطای Too many connections می‌بینند. Pool تعدادی اتصال باز نگه می‌دارد و به درخواست‌ها قرض می‌دهد.</p>
<table><thead><tr><th>روش</th><th>کجا</th><th>توضیح</th></tr></thead><tbody>
<tr><td>CONN_MAX_AGE جنگو</td><td>داخل هر thread</td><td>اتصال پایدار، نه pool واقعی؛ هر thread یک اتصال</td></tr>
<tr><td>QueuePool در SQLAlchemy</td><td>داخل هر پروسه</td><td>pool واقعی با سقف و صف انتظار</td></tr>
<tr><td>ProxySQL</td><td>سرویس جدا</td><td>multiplexing صدها اتصال برنامه روی چند اتصال واقعی، مسیریابی خواندن به replica</td></tr>
</tbody></table>
<h3>حساب‌وکتاب ساده</h3>
<p>اگر gunicorn با ۴ پروسه و هر کدام ۲ thread اجرا شود و <code>CONN_MAX_AGE</code> بزرگ‌تر از صفر باشد، هر سرور برنامه حداکثر ۸ اتصال پایدار دارد. سه سرور برنامه یعنی ۲۴، به‌علاوه‌ی workerهای Celery و کاربران مدیریتی. <code>max_connections</code> باید این جمع را به‌علاوه‌ی حاشیه‌ی امن پوشش دهد. زیر ASGI توصیه‌ی خود جنگو <code>CONN_MAX_AGE = 0</code> و استفاده از pooler بیرونی است.</p>
<h3>SQLAlchemy برای اسکریپت‌ها و سرویس‌ها</h3>
<pre><code class="language-python">from sqlalchemy import create_engine, text

engine = create_engine(
    "mysql+mysqldb://web:secret@127.0.0.1:3306/carpet_factory?charset=utf8mb4",
    pool_size=10,        # اتصال‌های همیشه باز
    max_overflow=5,      # اتصال اضافه در اوج بار
    pool_timeout=10,     # انتظار برای اتصال آزاد، بعد خطا
    pool_recycle=1800,   # کمتر از wait_timeout سرور
    pool_pre_ping=True,  # بررسی زنده بودن پیش از قرض دادن
)

with engine.begin() as conn:
    rows = conn.execute(
        text("SELECT code, hall FROM looms WHERE is_active = :a"), {"a": True}
    ).all()</code></pre>
<h3>پایش اتصال‌ها در سرور</h3>
<pre><code class="language-sql">SELECT user, SUBSTRING_INDEX(host, ':', 1) AS client, command, COUNT(*) AS n
FROM performance_schema.processlist
GROUP BY user, client, command
ORDER BY n DESC;

SHOW GLOBAL STATUS LIKE 'Threads_%';
SHOW GLOBAL STATUS LIKE 'Aborted_c%';</code></pre>
<p>اگر ده‌ها اتصال با command برابر <code>Sleep</code> و زمان طولانی از یک میزبان می‌بینید، احتمالاً برنامه‌ای اتصال را باز می‌کند و نمی‌بندد.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>pool_recycle</code> باید از <code>wait_timeout</code> سرور کمتر باشد؛ وگرنه صبح اولین درخواست با <code>MySQL server has gone away</code> (خطای 2006) شکست می‌خورد، چون سرور شب اتصال بی‌کار را بسته است.</li>
<li>اتصال قرضی وضعیت session را با خود می‌برد: متغیرهای <code>SET @x</code>، جدول‌های موقت و <code>SET SESSION</code>. در کد برنامه از تغییر وضعیت session پرهیز کنید یا قبل از برگرداندن پاکش کنید.</li>
<li>اتصالی که قبل از fork در پروسه‌ی والد ساخته شده نباید در فرزندان (مثل workerهای Celery در حالت prefork) استفاده شود؛ نتیجه خطاهای عجیبی مثل <code>Packet sequence number wrong</code> است. در SQLAlchemy بعد از fork <code>engine.dispose()</code> بزنید.</li>
<li>اگر <code>Threads_created</code> پیوسته بالا می‌رود، سرور برای هر اتصال thread تازه می‌سازد؛ بزرگ‌تر کردن <code>thread_cache_size</code> هزینه‌ی اتصال را کم می‌کند.</li>
<li>ProxySQL برای اتصالی که از متغیر کاربری، جدول موقت یا تراکنش باز استفاده کند multiplexing را خاموش می‌کند؛ کد پر از <code>SET @var</code> مزیتش را از بین می‌برد.</li>
</ul>""",
                },
                {
                    "title": "پروژه‌ی پایانی (۱): طراحی دیتابیس سفارش و تولید کارخانه‌ی فرش",
                    "kind": "text",
                    "minutes": 28,
                    "is_preview": False,
                    "body": r"""<h2>صورت مسئله</h2>
<p>یک کارخانه‌ی فرش ماشینی در کاشان از نمایندگی‌های فروش در شهرهای مختلف سفارش می‌گیرد. هر محصول ترکیبی از یک نقشه (افشان، ماهی، هریس)، تراکم شانه (۷۰۰، ۱۰۰۰، ۱۲۰۰) و ابعاد است. سفارش‌ها روی دستگاه‌های بافندگی سالن‌های مختلف برنامه‌ریزی می‌شوند و مدیر می‌خواهد بداند چه سفارش‌هایی عقب افتاده‌اند، کدام دستگاه بیشترین ضایعات را دارد و فروش ماهانه‌ی هر نقشه چقدر است. همه‌ی آموخته‌های دوره را این‌جا کنار هم می‌گذاریم.</p>
<h3>جدول‌ها</h3>
<pre><code class="language-sql">CREATE DATABASE carpet_factory CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE carpet_factory;

CREATE TABLE customers (
  id         INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  full_name  VARCHAR(120) NOT NULL,
  city       VARCHAR(60)  NOT NULL,
  mobile     CHAR(11)     NOT NULL,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY uq_customers_mobile (mobile)
);

CREATE TABLE designs (
  id     SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  name   VARCHAR(80) NOT NULL UNIQUE,
  colors TINYINT UNSIGNED NOT NULL CHECK (colors BETWEEN 1 AND 16)
);

CREATE TABLE products (
  id          INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  design_id   SMALLINT UNSIGNED NOT NULL,
  reeds       SMALLINT UNSIGNED NOT NULL,
  width_cm    SMALLINT UNSIGNED NOT NULL,
  length_cm   SMALLINT UNSIGNED NOT NULL,
  area_m2     DECIMAL(6,2) AS (width_cm * length_cm / 10000) STORED,
  price_toman DECIMAL(12,0) NOT NULL,
  UNIQUE KEY uq_product (design_id, reeds, width_cm, length_cm),
  CONSTRAINT fk_products_design FOREIGN KEY (design_id) REFERENCES designs (id),
  CONSTRAINT ck_products_reeds CHECK (reeds IN (500, 700, 1000, 1200, 1500))
);

CREATE TABLE orders (
  id          INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  customer_id INT UNSIGNED NOT NULL,
  status      ENUM('draft','confirmed','in_production','ready','shipped','cancelled')
              NOT NULL DEFAULT 'draft',
  ordered_at  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  due_date    DATE NOT NULL,
  KEY ix_orders_status_due (status, due_date),
  KEY ix_orders_ordered_at (ordered_at),
  CONSTRAINT fk_orders_customer FOREIGN KEY (customer_id) REFERENCES customers (id)
);

CREATE TABLE order_items (
  id               INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  order_id         INT UNSIGNED NOT NULL,
  product_id       INT UNSIGNED NOT NULL,
  qty              SMALLINT UNSIGNED NOT NULL CHECK (qty &gt; 0),
  unit_price_toman DECIMAL(12,0) NOT NULL,
  UNIQUE KEY uq_item (order_id, product_id),
  CONSTRAINT fk_items_order   FOREIGN KEY (order_id)   REFERENCES orders (id) ON DELETE CASCADE,
  CONSTRAINT fk_items_product FOREIGN KEY (product_id) REFERENCES products (id)
);

CREATE TABLE looms (
  id        SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  code      VARCHAR(10) NOT NULL UNIQUE,
  reeds     SMALLINT UNSIGNED NOT NULL,
  hall      VARCHAR(20) NOT NULL,
  is_active BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE production_jobs (
  id            INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  order_item_id INT UNSIGNED NOT NULL,
  loom_id       SMALLINT UNSIGNED NOT NULL,
  planned_qty   SMALLINT UNSIGNED NOT NULL,
  produced_qty  SMALLINT UNSIGNED NOT NULL DEFAULT 0,
  defect_qty    SMALLINT UNSIGNED NOT NULL DEFAULT 0,
  status        ENUM('queued','weaving','paused','done') NOT NULL DEFAULT 'queued',
  started_at    DATETIME NULL,
  finished_at   DATETIME NULL,
  KEY ix_jobs_loom_status (loom_id, status),
  KEY ix_jobs_finished (finished_at),
  CONSTRAINT fk_jobs_item FOREIGN KEY (order_item_id) REFERENCES order_items (id),
  CONSTRAINT fk_jobs_loom FOREIGN KEY (loom_id) REFERENCES looms (id),
  CONSTRAINT ck_jobs_time CHECK (finished_at IS NULL OR finished_at &gt;= started_at)
);</code></pre>
<h3>تصمیم‌های طراحی</h3>
<p>متراژ ستون محاسبه‌شده‌ی STORED است تا در گزارش‌ها جمع زده و در صورت نیاز ایندکس شود. قیمت در <code>order_items</code> تکرار شده، چون قیمت روز سفارش با تغییر لیست قیمت نباید عوض شود. حذف سفارش اقلامش را با CASCADE حذف می‌کند، اما اگر برای قلمی کار تولید ثبت شده باشد، کلید خارجی بدون CASCADE جلوی حذف را می‌گیرد؛ دقیقاً همان رفتاری که می‌خواهیم.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>CHECK روی ستونی که در کلید خارجی با عمل CASCADE یا SET NULL به کار رفته مجاز نیست؛ آن قید را باید در سطح برنامه یا تریگر گذاشت.</li>
<li>MySQL برای هر کلید خارجی، اگر ایندکس مناسبی نباشد، خودش ایندکس می‌سازد؛ پس ایندکس جداگانه روی <code>customer_id</code> تکراری است.</li>
<li>نام‌گذاری صریح قیدها (<code>fk_...</code> و <code>ck_...</code>) پیام خطا را خوانا می‌کند و حذف بعدی را بدون جست‌وجو در information_schema ممکن می‌سازد.</li>
<li>ENUM برای وضعیت فشرده است، اما افزودن مقدار وسط فهرست، جدول را بازسازی می‌کند؛ مقدار جدید را همیشه در انتها اضافه کنید.</li>
</ul>""",
                },
                {
                    "title": "پروژه‌ی پایانی (۲): گزارش‌های مدیریتی، View و دسترسی گزارش‌گیر",
                    "kind": "text",
                    "minutes": 26,
                    "is_preview": False,
                    "body": r"""<h2>از داده به تصمیم</h2>
<p>مدیر کارخانه هر صبح سه سؤال دارد: کدام سفارش‌ها عقب افتاده‌اند، کدام دستگاه‌ها بهره‌وری کم یا ضایعات زیاد دارند، و فروش هر نقشه در ماه‌های اخیر چطور بوده است. هر کدام را با ابزارهایی که در فصل‌های قبل دیدیم پاسخ می‌دهیم.</p>
<h3>۱. سفارش‌های عقب‌افتاده</h3>
<pre><code class="language-sql">WITH produced AS (
  SELECT order_item_id, SUM(produced_qty) AS made
  FROM production_jobs
  GROUP BY order_item_id
)
SELECT o.id AS order_id, c.full_name, c.city, o.due_date,
       SUM(GREATEST(CAST(oi.qty AS SIGNED) - COALESCE(pr.made, 0), 0)) AS remaining,
       DATEDIFF(CURDATE(), o.due_date) AS days_late
FROM orders o
JOIN customers c   ON c.id = o.customer_id
JOIN order_items oi ON oi.order_id = o.id
LEFT JOIN produced pr ON pr.order_item_id = oi.id
WHERE o.status IN ('confirmed', 'in_production')
  AND o.due_date &lt; CURDATE()
GROUP BY o.id, c.full_name, c.city, o.due_date
HAVING remaining &gt; 0
ORDER BY days_late DESC;</code></pre>
<h3>۲. بهره‌وری و ضایعات دستگاه‌ها در ۳۰ روز اخیر</h3>
<pre><code class="language-sql">SELECT l.code, l.hall,
       SUM(j.produced_qty) AS produced,
       SUM(j.defect_qty)   AS defects,
       ROUND(100 * SUM(j.defect_qty)
             / NULLIF(SUM(j.produced_qty + j.defect_qty), 0), 2) AS defect_pct,
       RANK() OVER (PARTITION BY l.hall ORDER BY SUM(j.produced_qty) DESC) AS rank_in_hall
FROM looms l
JOIN production_jobs j ON j.loom_id = l.id
WHERE j.finished_at &gt;= CURDATE() - INTERVAL 30 DAY
GROUP BY l.id, l.code, l.hall
ORDER BY l.hall, rank_in_hall;</code></pre>
<p>Window Function روی نتیجه‌ی GROUP BY اجرا می‌شود؛ برای همین می‌توان <code>SUM()</code> را داخل <code>ORDER BY</code> پنجره نوشت.</p>
<h3>۳. فروش ماهانه‌ی هر نقشه با جمع ماه</h3>
<pre><code class="language-sql">SELECT DATE_FORMAT(o.ordered_at, '%Y-%m') AS month,
       IF(GROUPING(d.name), 'TOTAL', d.name) AS design,
       SUM(oi.qty * p.area_m2)          AS sold_m2,
       SUM(oi.qty * oi.unit_price_toman) AS revenue_toman
FROM orders o
JOIN order_items oi ON oi.order_id = o.id
JOIN products p     ON p.id = oi.product_id
JOIN designs d      ON d.id = p.design_id
WHERE o.status &lt;&gt; 'cancelled'
  AND o.ordered_at &gt;= '2026-03-21'          -- ابتدای ۱۴۰۵
GROUP BY DATE_FORMAT(o.ordered_at, '%Y-%m'), d.name WITH ROLLUP;</code></pre>
<p>برای ماه‌های شمسی، به‌جای DATE_FORMAT یک جدول تقویم (<code>dim_date</code> با ستون‌های سال و ماه شمسی) بسازید و با <code>DATE(o.ordered_at)</code> به آن JOIN کنید؛ همان روشی که در فصل دوم برای تاریخ شمسی دیدیم.</p>
<h3>۴. View و دسترسی فقط‌خواندنی</h3>
<pre><code class="language-sql">CREATE VIEW v_loom_last30 AS
SELECT l.code, l.hall, SUM(j.produced_qty) AS produced, SUM(j.defect_qty) AS defects
FROM looms l JOIN production_jobs j ON j.loom_id = l.id
WHERE j.finished_at &gt;= CURDATE() - INTERVAL 30 DAY
GROUP BY l.id, l.code, l.hall;

GRANT SELECT ON carpet_factory.v_loom_last30 TO 'report_ro';</code></pre>
<p>گزارش‌گیر فقط View را می‌بیند و به جدول‌های خام دسترسی ندارد. اگر replica دارید، ابزار گزارش را به آن وصل کنید و پیش از هر گزارش جدید، <code>EXPLAIN ANALYZE</code> بگیرید.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>تفریق دو ستون UNSIGNED که نتیجه‌اش منفی شود خطای <code>BIGINT UNSIGNED value is out of range</code> (ERROR 1690) می‌دهد؛ برای همین در گزارش اول <code>CAST(... AS SIGNED)</code> آمده است.</li>
<li>تابع <code>GROUPING()</code> ردیف‌های جمع ROLLUP را از ردیف‌هایی که واقعاً NULL دارند جدا می‌کند؛ <code>IFNULL</code> این دو را با هم قاطی می‌کند.</li>
<li>View در MySQL نتیجه را ذخیره نمی‌کند؛ برای داشبوردی که هر دقیقه رفرش می‌شود، جدول خلاصه‌ای بسازید که یک Event هر ساعت پرش کند.</li>
<li>شرطی مثل <code>DATE(finished_at) = CURDATE()</code> ایندکس <code>ix_jobs_finished</code> را بی‌اثر می‌کند؛ بازه‌ای بنویسید: <code>finished_at &gt;= CURDATE() AND finished_at &lt; CURDATE() + INTERVAL 1 DAY</code>.</li>
</ul>""",
                },
                {
                    "title": "کلینیک خطاهای رایج و نگاهی به مهاجرت به/از PostgreSQL",
                    "kind": "text",
                    "minutes": 28,
                    "is_preview": False,
                    "body": r"""<h2>هفت خطایی که حتماً می‌بینید</h2>
<table><thead><tr><th>خطا</th><th>علت رایج</th><th>درمان</th></tr></thead><tbody>
<tr><td>1366 Incorrect string value</td><td>ستون یا اتصال utf8mb3 است و ایموجی یا کاراکتر چهاربایتی آمده</td><td>CONVERT TO utf8mb4 و charset اتصال</td></tr>
<tr><td>1040 Too many connections</td><td>نشت اتصال، pool بزرگ یا کوئری‌های کند که اتصال را نگه می‌دارند</td><td>پیدا کردن منشأ، نه فقط بالا بردن سقف</td></tr>
<tr><td>1205 Lock wait timeout exceeded</td><td>تراکنش طولانی یا باز مانده قفل را نگه داشته</td><td>یافتن تراکنش مسدودکننده، کوتاه کردن تراکنش‌ها</td></tr>
<tr><td>1045 Access denied</td><td>رمز اشتباه یا تطبیق نخوردن host</td><td>بررسی USER() و CURRENT_USER()</td></tr>
<tr><td>1153 / 2020 max_allowed_packet</td><td>INSERT بزرگ یا فایل در BLOB</td><td>افزایش در سرور و کلاینت</td></tr>
<tr><td>1452 foreign key constraint fails</td><td>ردیف والد وجود ندارد یا ترتیب درج غلط است</td><td>یافتن یتیم‌ها با LEFT JOIN</td></tr>
<tr><td>2013 Lost connection</td><td>timeout، کرش سرور یا OOM killer</td><td>لاگ خطا و dmesg</td></tr>
</tbody></table>
<h3>ابزارهای تشخیص</h3>
<pre><code class="language-sql">-- 1366: کدام ستون‌ها هنوز utf8mb4 نیستند؟
SELECT table_name, column_name, character_set_name
FROM information_schema.columns
WHERE table_schema = 'carpet_factory' AND character_set_name &lt;&gt; 'utf8mb4';
ALTER TABLE customers CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;

-- 1205: چه کسی منتظر چه کسی است؟
SELECT waiting_pid, waiting_query, blocking_pid, blocking_query, wait_age
FROM sys.innodb_lock_waits;

-- 1045: با کدام حساب شناخته شدید؟
SELECT USER(), CURRENT_USER();
SELECT user, host, plugin, account_locked FROM mysql.user WHERE user = 'web';

-- 1452: اقلام بدون سفارش
SELECT oi.id, oi.order_id
FROM order_items oi LEFT JOIN orders o ON o.id = oi.order_id
WHERE o.id IS NULL;

-- max_allowed_packet (کلاینت هم سقف خودش را دارد: mysql --max-allowed-packet=256M)
SET PERSIST max_allowed_packet = 268435456;</code></pre>
<p>برای 2013 اول لاگ خطای MySQL و خروجی <code>dmesg | grep -i oom</code> را ببینید؛ اگر سرور ری‌استارت شده، مشکل حافظه است نه شبکه. اگر فقط کوئری‌های طولانی قطع می‌شوند، <code>net_read_timeout</code> و timeout پروکسی یا load balancer بین برنامه و دیتابیس را بررسی کنید.</p>
<h3>مهاجرت به PostgreSQL یا از آن</h3>
<p>برای پروژه‌ی جنگو کوچک، <code>dumpdata</code> و <code>loaddata</code> کافی است؛ برای دیتابیس بزرگ ابزار pgloader از MySQL به PostgreSQL را خودکار انجام می‌دهد. تفاوت‌هایی که کد را می‌شکنند: بک‌تیک در برابر کوتیشن دوتایی برای نام‌ها، <code>ON DUPLICATE KEY UPDATE</code> در برابر <code>ON CONFLICT</code>، <code>TINYINT(1)</code> در برابر boolean، مقایسه‌ی رشته که در collation پیش‌فرض MySQL به حروف کوچک و بزرگ حساس نیست ولی در PostgreSQL حساس است، و تاریخ‌های <code>0000-00-00</code> که PostgreSQL نمی‌پذیرد.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>MySQL همیشه یک اتصال بیش از <code>max_connections</code> برای کاربر دارای CONNECTION_ADMIN نگه می‌دارد؛ اگر برنامه با root وصل شود، همین راه نجات را هم مصرف کرده است. از 8.0.14 پورت مدیریتی جدا (<code>admin_address</code>، پورت 33062) هم هست.</li>
<li>بعد از Lock wait timeout فقط همان دستور ROLLBACK می‌شود، نه کل تراکنش؛ مگر <code>innodb_rollback_on_timeout = ON</code> باشد. برنامه‌ای که بعد از خطا COMMIT می‌زند، نیمی از کار را ثبت می‌کند.</li>
<li><code>SET FOREIGN_KEY_CHECKS = 0</code> برای ورود داده سریع است، اما وقتی دوباره روشن شود داده‌ی موجود را بررسی نمی‌کند؛ یتیم‌ها بی‌صدا باقی می‌مانند.</li>
<li>پیام Access denied با <code>(using password: NO)</code> یعنی برنامه اصلاً رمز را نفرستاده؛ معمولاً متغیر محیطی خالی است، نه رمز اشتباه.</li>
<li>در مهاجرت، شمارنده‌ی sequenceها در PostgreSQL پس از ورود داده خودکار به‌روز نمی‌شود؛ بدون <code>setval</code> اولین INSERT خطای کلید تکراری می‌دهد.</li>
</ul>""",
                },
            ],
        },
    ],
}

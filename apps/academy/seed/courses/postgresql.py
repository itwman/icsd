# -*- coding: utf-8 -*-
# دوره‌ی جامع PostgreSQL — ۸ فصل، ۴۱ درس. متن‌ها r""" هستند تا بک‌اسلش‌های psql و regex دست‌نخورده بمانند.

COURSE = {
    "slug": "postgresql",
    "title": "آموزش جامع PostgreSQL",
    "category": "دیتابیس",
    "level": "intermediate",
    "summary": "از نصب و psql تا طراحی با قیدهای واقعی، کوئری پیشرفته، ایندکس و EXPLAIN، MVCC و VACUUM، بکاپ و Replication و اتصال به جنگو — با جست‌وجوی فارسی و ده‌ها نکته‌ای که کمتر کسی می‌داند.",
    "description": (
        "<p>PostgreSQL امروز انتخاب پیش‌فرض تیم‌هایی است که درستی داده برایشان مهم است؛ اما بیشتر برنامه‌نویس‌ها آن را "
        "مثل یک MySQL دیگر به کار می‌برند: همه‌چیز varchar، پول در float، تاریخ بدون منطقه‌ی زمانی، بدون قید، بدون ایندکس "
        "مناسب و بدون هیچ تصوری از VACUUM — تا روزی که دیتابیس کند می‌شود، دیسک پر می‌شود یا بکاپ بازنمی‌گردد. این دوره برای "
        "برنامه‌نویسان بک‌اند، مدیران سیستم و تحلیل‌گرانی است که می‌خواهند پستگرس را واقعاً بشناسند.</p>"
        "<p>از نصب روی ویندوز، اوبونتو و داکر و کار حرفه‌ای با <strong>psql</strong> شروع می‌کنیم؛ بعد انواع داده‌ی ویژه، "
        "طراحی با <strong>قیدهای واقعی</strong> (EXCLUDE، DEFERRABLE، domain)، کوئری پیشرفته (LATERAL، CTE بازگشتی، "
        "Window Function، jsonb)، <strong>ایندکس و خواندن EXPLAIN</strong>، جست‌وجوی فارسی با full-text و pg_trgm، "
        "<strong>MVCC، VACUUM و قفل‌ها</strong>، امنیت و RLS، بکاپ منطقی و فیزیکی و PITR، Replication، PgBouncer، "
        "partitioning، PL/pgSQL و اتصال از پایتون و جنگو را می‌بینیم و در پایان دیتابیس تولید و سفارش یک کارخانه‌ی فرش "
        "را از صفر می‌سازیم و خطاهای رایج را یکی‌یکی درمان می‌کنیم.</p>"
        "<p>پیش‌نیاز: آشنایی اولیه با مفهوم جدول و یک زبان برنامه‌نویسی؛ SQL را از پایه مرور می‌کنیم اما سریع عمیق می‌شویم. "
        "هدف نسخه‌های 16 و 17 است و تفاوت‌های مهم نسخه‌ی 18 هرجا لازم باشد گفته می‌شود. هر درس با بخش "
        "«نکته‌هایی که کمتر کسی می‌داند» تمام می‌شود؛ همان تجربه‌هایی که معمولاً با یک قطعی نیمه‌شب به دست می‌آیند.</p>"
    ),
    "price": 1100000,
    "duration_minutes": 928,
    "tags": ["PostgreSQL", "دیتابیس", "SQL"],
    "modules": [
        # ───────────────────────────── فصل ۱ ─────────────────────────────
        {
            "title": "فصل ۱: شروع — نصب، معماری و ابزارها",
            "lessons": [
                {
                    "title": "چرا PostgreSQL؟ جایگاه، نسخه‌ها و تفاوت با MySQL",
                    "kind": "text",
                    "minutes": 16,
                    "is_preview": True,
                    "body": r"""<h2>دیتابیسی که «درستی داده» را جدی می‌گیرد</h2>
<p>PostgreSQL (به اختصار «پستگرس») ریشه در پروژه‌ی POSTGRES دانشگاه برکلی در دهه‌ی ۱۹۸۰ دارد و از ۱۹۹۶ با نام فعلی به‌صورت متن‌باز توسعه داده می‌شود. پشت آن یک شرکت واحد نیست؛ یک جامعه‌ی جهانی و ده‌ها شرکت با هم آن را جلو می‌برند و مجوزش (PostgreSQL License، شبیه BSD) هر استفاده‌ی تجاری را بدون هزینه و بدون الزام انتشار کد مجاز می‌کند. برای ما یک مزیت عملی دیگر هم دارد: هیچ بخشی از آن پشت لایسنس اشتراکی یا فعال‌سازی آنلاین نیست که با تحریم از کار بیفتد.</p>
<h3>چه چیزی آن را متمایز می‌کند</h3>
<ul>
<li><strong>قیدها واقعاً اجرا می‌شوند:</strong> رشته‌ی بلندتر از ستون بی‌صدا بریده نمی‌شود، تاریخ نامعتبر به صفر تبدیل نمی‌شود و تبدیل نوع ضمنیِ خطرناک انجام نمی‌شود؛ خطا می‌گیرید.</li>
<li><strong>DDL تراکنشی:</strong> CREATE TABLE و ALTER TABLE را می‌توان داخل یک تراکنش گذاشت؛ اگر مرحله‌ی سوم یک migration شکست بخورد، دو مرحله‌ی قبلی هم برمی‌گردند. در MySQL هر DDL یک commit ضمنی است.</li>
<li><strong>توسعه‌پذیری:</strong> نوع داده، تابع، عملگر و حتی نوع ایندکس جدید را می‌شود به‌صورت اکستنشن اضافه کرد؛ PostGIS، pgvector و TimescaleDB همه اکستنشن‌اند.</li>
<li><strong>SQL غنی:</strong> Window Function، CTE بازگشتی، LATERAL، jsonb با ایندکس GIN، انواع range، قید EXCLUDE و Full-Text Search داخلی.</li>
<li><strong>MVCC:</strong> خواننده‌ها نویسنده‌ها را معطل نمی‌کنند و برعکس؛ بهای آن نیاز به VACUUM است که در فصل ۶ کامل می‌بینیم.</li>
</ul>
<h3>مقایسه‌ی کوتاه با MySQL</h3>
<table><thead><tr><th>موضوع</th><th>PostgreSQL</th><th>MySQL (InnoDB)</th></tr></thead><tbody>
<tr><td>DDL داخل تراکنش</td><td>بله، قابل ROLLBACK</td><td>خیر، commit ضمنی</td></tr>
<tr><td>مدل اتصال</td><td>یک پروسه برای هر اتصال؛ pooler تقریباً ضروری</td><td>یک thread برای هر اتصال</td></tr>
<tr><td>ایندکس جزئی (partial)</td><td>دارد</td><td>ندارد</td></tr>
<tr><td>JSON</td><td>jsonb باینری با ایندکس GIN روی کل سند</td><td>JSON با ایندکس روی ستون‌های مجازی</td></tr>
<tr><td>انواع ویژه</td><td>array، range، uuid، inet، enum واقعی</td><td>محدودتر</td></tr>
<tr><td>نگهداری</td><td>VACUUM و autovacuum</td><td>purge داخلی InnoDB</td></tr>
</tbody></table>
<h3>نسخه‌ها و چرخه‌ی انتشار</h3>
<p>هر سال حدود مهرماه یک نسخه‌ی اصلی منتشر می‌شود: 16 در ۲۰۲۳، 17 در ۲۰۲۴ و 18 در ۲۰۲۵. هر نسخه‌ی اصلی پنج سال به‌روزرسانی می‌گیرد و هر سه ماه یک نسخه‌ی فرعی (مثل 17.6) می‌آید. از نسخه‌ی 10 به بعد، عدد اول نسخه‌ی اصلی است: رفتن از 17.2 به 17.6 فقط عوض کردن باینری‌ها و یک restart است، اما رفتن از 16 به 17 ارتقای واقعی با pg_upgrade یا dump/restore لازم دارد (فصل ۷).</p>
<pre><code class="language-sql">SELECT version();
SHOW server_version_num;      -- 170006 یعنی 17.6
SELECT current_setting('server_version_num')::int &gt;= 160000 AS is_16_or_newer;</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>نام‌های بدون کوتیشن به حروف کوچک تبدیل می‌شوند: <code>CREATE TABLE Orders</code> همان orders است. اما اگر ابزاری جدول را با <code>"Orders"</code> بسازد، از آن به بعد همیشه باید با دابل‌کوتیشن صدایش کنید. از روز اول همه‌چیز را کوچک و snake_case بنویسید.</li>
<li>رشته با تک‌کوتیشن است و شناسه با دابل‌کوتیشن؛ <code>WHERE name = "ali"</code> یعنی «ستونی به نام ali» و خطای column does not exist می‌دهد. این اولین دام کسانی است که از MySQL می‌آیند.</li>
<li>در release notes نسخه‌های فرعی گاهی نوشته می‌شود «پس از ارتقا این نوع ایندکس‌ها را REINDEX کنید»؛ بخش Migration هر نسخه‌ی فرعی را همیشه بخوانید.</li>
<li>در اسکریپت‌ها به‌جای تجزیه‌ی رشته‌ی version() از <code>server_version_num</code> استفاده کنید؛ یک عدد قابل‌مقایسه است.</li>
<li>حتی داخل یک تراکنش می‌توانید <code>CREATE INDEX</code> و <code>DROP TABLE</code> را امتحان و بعد ROLLBACK کنید؛ روشی امن برای آزمودن اثر یک تغییر روی پلن کوئری (به‌جز CREATE INDEX CONCURRENTLY که داخل تراکنش مجاز نیست).</li>
</ul>""",
                },
                {
                    "title": "نصب روی ویندوز، اوبونتو (مخزن PGDG) و داکر",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>سه راه نصب و انتخاب درست</h2>
<p>برای یادگیری و توسعه روی ویندوز، نصاب رسمی کافی است؛ برای سرور، لینوکس با مخزن رسمی PGDG؛ و برای محیط‌های تکرارپذیر و CI، داکر. نکته‌ی مشترک هر سه: نسخه‌ی اصلی را آگاهانه انتخاب کنید (در این دوره 17) و بدانید داده‌ها کجا ذخیره می‌شوند.</p>
<h3>ویندوز</h3>
<p>نصاب EDB چهار جزء دارد: سرور، pgAdmin، Stack Builder و ابزارهای خط فرمان. رمز کاربر <strong>postgres</strong> را که می‌پرسد جایی امن نگه دارید؛ پورت پیش‌فرض 5432 است و سرویس با نام postgresql-x64-17 ثبت می‌شود. بعد از نصب، پوشه‌ی bin را به PATH اضافه کنید تا psql در PowerShell در دسترس باشد:</p>
<pre><code class="language-powershell">$env:Path += ";C:\Program Files\PostgreSQL\17\bin"
$env:PGCLIENTENCODING = "UTF8"
chcp 65001
psql -U postgres -h localhost</code></pre>
<p>دو خط وسط برای فارسی است: بدون آن‌ها psql در کنسول ویندوز هشدار code page می‌دهد و حروف فارسی را خراب نمایش می‌دهد.</p>
<h3>اوبونتو با مخزن PGDG</h3>
<p>مخزن پیش‌فرض اوبونتو فقط یک نسخه (و معمولاً قدیمی‌تر) دارد. مخزن رسمی پروژه (PGDG) همه‌ی نسخه‌های پشتیبانی‌شده و اکستنشن‌ها را به‌صورت بسته‌ی آماده می‌دهد:</p>
<pre><code class="language-bash">sudo apt install -y postgresql-common
sudo /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh
sudo apt install -y postgresql-17 postgresql-contrib
pg_lsclusters                       # Ver Cluster Port Status Owner Data directory
sudo systemctl status postgresql@17-main
sudo -u postgres psql</code></pre>
<p>در دبیان و اوبونتو پیکربندی در <code>/etc/postgresql/17/main/</code> و داده در <code>/var/lib/postgresql/17/main</code> است. ابزارهای <code>pg_ctlcluster</code> و <code>pg_createcluster</code> اجازه می‌دهند چند نسخه کنار هم با پورت‌های مختلف اجرا شوند.</p>
<h3>داکر</h3>
<pre><code class="language-bash">docker run -d --name pg17 \
  -e POSTGRES_PASSWORD='S3cret!' \
  -e POSTGRES_INITDB_ARGS='--locale-provider=icu --icu-locale=fa-IR' \
  -e TZ=Asia/Tehran \
  -p 127.0.0.1:5432:5432 \
  -v pgdata17:/var/lib/postgresql/data \
  postgres:17

docker exec -it pg17 psql -U postgres</code></pre>
<p>volume نام‌دار اجباری است؛ بدون آن با حذف کانتینر همه‌ی داده از بین می‌رود. متغیرهای POSTGRES_* فقط بار اول (وقتی پوشه‌ی داده خالی است) اثر دارند. اگر Docker Hub در دسترس نیست، image را از میرورهای داخلی (مثلاً میرور آروان) بکشید و در <code>daemon.json</code> به‌عنوان registry-mirrors معرفی کنید.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>در image رسمی نسخه‌ی 18 مسیر پیش‌فرض داده به <code>/var/lib/postgresql/18/docker</code> تغییر کرده و volume باید روی <code>/var/lib/postgresql</code> سوار شود؛ کپی کردن دستور docker run نسخه‌ی 17 برای 18 داده را بیرون volume می‌نویسد.</li>
<li><code>-p 127.0.0.1:5432:5432</code> پورت را فقط روی localhost باز می‌کند. با <code>-p 5432:5432</code> داکر قوانین iptables را دور می‌زند و دیتابیس شما حتی با وجود ufw روی اینترنت باز است.</li>
<li>پوشه‌ی <code>/docker-entrypoint-initdb.d/</code> در image رسمی فایل‌های .sql و .sh را فقط در اولین راه‌اندازی اجرا می‌کند؛ برای ساخت خودکار دیتابیس و کاربر برنامه عالی است.</li>
<li>روی ویندوز، سرویس با حساب NETWORK SERVICE اجرا می‌شود؛ اگر پوشه‌ی داده را جابه‌جا کردید، مجوز آن حساب را روی پوشه‌ی جدید بدهید وگرنه سرویس بی‌صدا بالا نمی‌آید.</li>
<li>نصب هم‌زمان postgresql از مخزن اوبونتو و PGDG دو کلاستر روی پورت‌های 5432 و 5433 می‌سازد؛ اگر وصل می‌شوید ولی جدول‌هایتان را نمی‌بینید، اول <code>pg_lsclusters</code> را نگاه کنید.</li>
</ul>""",
                },
                {
                    "title": "معماری: کلاستر، پروسه‌ها، postgresql.conf و pg_hba.conf",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>زیر کاپوت پستگرس</h2>
<p>وقتی می‌گوییم «سرور PostgreSQL» در واقع منظورمان یک <strong>کلاستر</strong> است: یک پوشه‌ی داده (data directory) که یک پروسه‌ی اصلی به نام postmaster روی یک پورت آن را سرویس می‌دهد. یک کلاستر چند <strong>database</strong> دارد، هر database چند <strong>schema</strong> و هر schema جدول‌ها و ویوها و توابع. <strong>role</strong>ها (کاربران) در سطح کلاستر تعریف می‌شوند و در همه‌ی دیتابیس‌ها مشترک‌اند.</p>
<h3>مدل پروسه</h3>
<p>برای هر اتصال کلاینت، postmaster یک پروسه‌ی جدید (backend) fork می‌کند. هر backend چند مگابایت حافظه‌ی خصوصی دارد؛ به همین دلیل هزار اتصال هم‌زمان برای پستگرس سنگین است و در فصل ۷ PgBouncer را می‌بینیم. در کنار backendها پروسه‌های پس‌زمینه کار می‌کنند:</p>
<table><thead><tr><th>پروسه</th><th>وظیفه</th></tr></thead><tbody>
<tr><td>checkpointer</td><td>صفحه‌های تغییرکرده‌ی حافظه را در فواصل منظم روی دیسک می‌نویسد</td></tr>
<tr><td>background writer</td><td>نوشتن تدریجی صفحه‌های کثیف تا backendها معطل نشوند</td></tr>
<tr><td>walwriter</td><td>نوشتن Write-Ahead Log؛ ضامن دوام تراکنش پس از commit</td></tr>
<tr><td>autovacuum launcher</td><td>راه‌اندازی workerهای VACUUM و ANALYZE</td></tr>
<tr><td>walsender / walreceiver</td><td>ارسال و دریافت WAL در Replication</td></tr>
</tbody></table>
<p>هر تغییر اول در WAL (پوشه‌ی <code>pg_wal</code>) ثبت می‌شود و بعد در فایل جدول. اگر برق برود، هنگام بالا آمدن WAL دوباره اجرا می‌شود. بکاپ فیزیکی و Replication هم هر دو روی همین WAL سوارند.</p>
<h3>دو فایل پیکربندی اصلی</h3>
<p><strong>postgresql.conf</strong> رفتار سرور را تعیین می‌کند و <strong>pg_hba.conf</strong> می‌گوید چه کسی از کجا و با چه روشی حق اتصال دارد. پستگرس pg_hba را از بالا به پایین می‌خواند و <em>اولین</em> خط منطبق تصمیم می‌گیرد.</p>
<pre><code class="language-ini"># postgresql.conf
listen_addresses = 'localhost,10.0.0.5'   # پیش‌فرض فقط localhost
port = 5432
password_encryption = scram-sha-256
ssl = on
timezone = 'UTC'

# pg_hba.conf
# TYPE    DATABASE  USER      ADDRESS        METHOD
local     all       postgres                 peer
local     all       all                      scram-sha-256
hostssl   carpet    app_user  10.0.0.0/24    scram-sha-256
host      all       all       0.0.0.0/0      reject</code></pre>
<p><strong>peer</strong> یعنی نام کاربر سیستم‌عامل باید با نام role یکی باشد (فقط برای اتصال سوکت محلی)؛ <strong>scram-sha-256</strong> روش امن رمز است و از نسخه‌ی 14 پیش‌فرض است. md5 قدیمی و در نسخه‌ی 18 منسوخ اعلام شده است.</p>
<pre><code class="language-sql">SHOW config_file;
SHOW hba_file;
SELECT name, setting, unit, context FROM pg_settings WHERE name IN ('shared_buffers','work_mem');
ALTER SYSTEM SET log_min_duration_statement = '500ms';
SELECT pg_reload_conf();
SELECT line_number, type, database, user_name, auth_method, error FROM pg_hba_file_rules;</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>ستون <code>context</code> در pg_settings می‌گوید تغییر چه لازم دارد: <code>postmaster</code> یعنی restart، <code>sighup</code> یعنی reload کافی است، <code>user</code> یعنی در هر نشست با SET قابل تغییر است.</li>
<li><code>ALTER SYSTEM</code> در فایل <code>postgresql.auto.conf</code> می‌نویسد که <em>بعد از</em> postgresql.conf خوانده می‌شود و بر آن غلبه می‌کند؛ اگر تغییرتان در conf اثر نمی‌کند، اول این فایل را ببینید.</li>
<li>قبل از reload، نمای <code>pg_hba_file_rules</code> خطاهای نحوی pg_hba را در ستون error نشان می‌دهد؛ یک خط اشتباه می‌تواند همه را پشت در نگه دارد.</li>
<li>ترتیب خطوط pg_hba مهم است: یک خط <code>host all all 0.0.0.0/0 reject</code> بالای بقیه، همه‌ی اتصال‌های TCP را می‌بندد حتی اگر پایین‌تر خط مجاز داشته باشید.</li>
<li>برای تغییر رمز postgres بعد از عوض کردن روش به scram، رمز را دوباره با <code>\password</code> در psql تنظیم کنید؛ هش md5 قدیمی با scram قابل تأیید نیست.</li>
</ul>""",
                },
                {
                    "title": "psql حرفه‌ای و ابزارهای گرافیکی (pgAdmin و DBeaver)",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>psql؛ ابزاری که روی هر سرور هست</h2>
<p>ابزار گرافیکی راحت است، اما روی سرور تولید، در اسکریپت‌های بکاپ و در ساعت دو بامداد فقط psql دارید. فرمان‌هایی که با بک‌اسلش شروع می‌شوند را خود psql اجرا می‌کند (نه سرور) و نقطه‌ویرگول نمی‌خواهند.</p>
<pre><code class="language-bash">psql -h 127.0.0.1 -p 5432 -U app_user -d carpet
psql "postgresql://app_user@127.0.0.1:5432/carpet?sslmode=require"
psql -d carpet -c "SELECT count(*) FROM orders"
psql -d carpet -f schema.sql -v ON_ERROR_STOP=1</code></pre>
<h3>فرمان‌های بک‌اسلشی پرکاربرد</h3>
<table><thead><tr><th>فرمان</th><th>کار</th></tr></thead><tbody>
<tr><td><code>\l</code> / <code>\c dbname</code></td><td>فهرست دیتابیس‌ها / اتصال به دیتابیس دیگر</td></tr>
<tr><td><code>\dn</code> / <code>\dt app.*</code></td><td>schemaها / جدول‌های یک schema</td></tr>
<tr><td><code>\d+ orders</code></td><td>ساختار کامل جدول: ستون‌ها، ایندکس‌ها، قیدها، triggerها، حجم</td></tr>
<tr><td><code>\du</code> / <code>\dp</code></td><td>roleها / مجوزهای جدول‌ها</td></tr>
<tr><td><code>\df+ name</code> / <code>\sf name</code></td><td>توابع / نمایش کد یک تابع</td></tr>
<tr><td><code>\x auto</code></td><td>نمایش عمودی خودکار وقتی ردیف در عرض صفحه جا نمی‌شود</td></tr>
<tr><td><code>\timing on</code></td><td>نمایش زمان اجرای هر کوئری</td></tr>
<tr><td><code>\e</code> / <code>\ef name</code></td><td>باز کردن آخرین کوئری یا یک تابع در ویرایشگر</td></tr>
<tr><td><code>\watch 5</code></td><td>اجرای دوباره‌ی آخرین کوئری هر ۵ ثانیه</td></tr>
<tr><td><code>\gx</code></td><td>اجرای کوئری فعلی با خروجی عمودی (فقط همین یک بار)</td></tr>
<tr><td><code>\copy</code></td><td>ورود و خروج CSV از دید کلاینت</td></tr>
</tbody></table>
<h3>فایل ‎.psqlrc</h3>
<p>این فایل در پوشه‌ی خانه (در ویندوز <code>%APPDATA%\postgresql\psqlrc.conf</code>) هر بار اجرا می‌شود:</p>
<pre><code class="language-sql">\set QUIET 1
\pset null '(null)'
\x auto
\timing on
\set ON_ERROR_ROLLBACK interactive
\set HISTFILE ~/.psql_history- :DBNAME
\set PROMPT1 '%n@%/%R%# '
\unset QUIET</code></pre>
<h3>ابزارهای گرافیکی</h3>
<p><strong>pgAdmin</strong> ابزار رسمی و وب‌محور است؛ برای مدیریت roleها، مشاهده‌ی نشست‌ها و EXPLAIN گرافیکی خوب است. <strong>DBeaver</strong> چنددیتابیسی است و برای کسی که هم‌زمان با MySQL و SQL Server کار می‌کند راحت‌تر است؛ نمودار ER و ویرایش جدولی داده را هم دارد. در هر دو، تنظیم encoding اتصال را روی UTF8 و فونت ویرایشگر را روی فونتی با پشتیبانی فارسی (مثل Vazirmatn Code) بگذارید.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>ON_ERROR_ROLLBACK interactive</code> قبل از هر دستور یک SAVEPOINT مخفی می‌سازد؛ در حالت تعاملی یک غلط تایپی دیگر کل تراکنش باز را خراب نمی‌کند (خطای current transaction is aborted).</li>
<li>psql با گزینه‌ی <code>-E</code> کوئری‌های واقعی پشت فرمان‌های بک‌اسلشی را نشان می‌دهد؛ بهترین راه برای یاد گرفتن کاتالوگ سیستمی.</li>
<li><code>\copy</code> فایل را روی ماشین کلاینت می‌خواند، اما <code>COPY ... FROM '/path'</code> فایل را روی سرور و با مجوز سرور؛ روی سرور راه دور تقریباً همیشه \copy می‌خواهید.</li>
<li>فایل <code>~/.pgpass</code> (در ویندوز <code>%APPDATA%\postgresql\pgpass.conf</code>) با قالب host:port:db:user:password رمز را برای اسکریپت‌ها نگه می‌دارد؛ روی لینوکس مجوزش باید 600 باشد وگرنه نادیده گرفته می‌شود.</li>
<li>با <code>\set</code> متغیر بسازید و با <code>:'name'</code> به‌صورت رشته‌ی امن در کوئری بگذارید: <code>\set city 'کاشان'</code> و سپس <code>WHERE city = :'city'</code>.</li>
</ul>""",
                },
                {
                    "title": "دیتابیس، schema، role و search_path؛ encoding و collation فارسی",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>ساختن دیتابیس به روش درست</h2>
<p>بیشتر دردسرهای فارسی از همان لحظه‌ی CREATE DATABASE شروع می‌شود. encoding باید <strong>UTF8</strong> باشد و collation (قاعده‌ی مقایسه و مرتب‌سازی) آگاهانه انتخاب شود؛ هر دو بعداً قابل تغییر نیستند مگر با dump و restore.</p>
<pre><code class="language-sql">CREATE ROLE carpet_owner LOGIN PASSWORD 'change-me';

CREATE DATABASE carpet
  OWNER carpet_owner
  ENCODING 'UTF8'
  LOCALE_PROVIDER icu
  ICU_LOCALE 'fa-IR'
  TEMPLATE template0;

\c carpet
CREATE SCHEMA app AUTHORIZATION carpet_owner;
ALTER ROLE carpet_owner IN DATABASE carpet SET search_path = app, public;</code></pre>
<p><code>TEMPLATE template0</code> لازم است چون template1 ممکن است encoding یا locale دیگری داشته باشد. هر دیتابیس جدید در واقع کپی template1 است؛ هرچه (اکستنشن، جدول) در template1 بگذارید، در دیتابیس‌های بعدی هم خواهد بود.</p>
<h3>collation: libc، ICU و builtin</h3>
<table><thead><tr><th>ارائه‌دهنده</th><th>ویژگی</th></tr></thead><tbody>
<tr><td>libc</td><td>از کتابخانه‌ی سیستم‌عامل؛ ارتقای glibc می‌تواند ترتیب را عوض و ایندکس‌ها را خراب کند</td></tr>
<tr><td>ICU</td><td>مستقل از سیستم‌عامل، پشتیبانی کامل از قواعد زبان‌ها از جمله فارسی</td></tr>
<tr><td>builtin (17+)</td><td>فقط C و C.UTF-8؛ سریع و پایدار، مرتب‌سازی بر اساس کد یونیکد</td></tr>
</tbody></table>
<p>با collation نوع C، حروف بر اساس کد یونیکد مرتب می‌شوند؛ «پ»، «چ»، «ژ» و «گ» که کدشان بعد از حروف عربی است، بعد از «و» می‌نشینند و «پرویز» بعد از «وحید» می‌آید. با ICU و fa-IR ترتیب الفبای فارسی رعایت می‌شود. می‌توانید دیتابیس را C نگه دارید و فقط جایی که لازم است collation بدهید:</p>
<pre><code class="language-sql">SELECT name FROM customers ORDER BY name COLLATE "fa-IR-x-icu";
CREATE INDEX ON customers (name COLLATE "fa-IR-x-icu");</code></pre>
<h3>مسئله‌ی «ی» و «ک»</h3>
<p>«ي» عربی (U+064A) و «ی» فارسی (U+06CC) و همین‌طور «ك» و «ک» از نظر دیتابیس دو کاراکتر متفاوت‌اند؛ هیچ collationی مشکل را کامل حل نمی‌کند. راه درست، <strong>یکسان‌سازی در ورود داده</strong> است (در برنامه یا با trigger) و یک CHECK برای اطمینان:</p>
<pre><code class="language-sql">ALTER TABLE customers
  ADD CONSTRAINT name_persian_chars CHECK (name !~ '[يك]');
UPDATE customers SET name = translate(name, 'يك', 'یک') WHERE name ~ '[يك]';</code></pre>
<h3>schema و search_path</h3>
<p>schema فضای نام است: <code>app.orders</code> و <code>report.orders</code> دو جدول مجزایند. وقتی نام را بدون schema می‌نویسید، پستگرس آن را در schemaهای <code>search_path</code> به ترتیب جست‌وجو می‌کند. پیش‌فرض <code>"$user", public</code> است؛ یعنی اگر schemaی هم‌نام کاربر وجود داشته باشد، اول آن‌جا را می‌گردد.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>از نسخه‌ی 15 کاربران عادی دیگر حق CREATE در schemaی public را ندارند؛ خطای permission denied for schema public پس از ارتقا از همین است. راه تمیز: یک schemaی اختصاصی برای برنامه بسازید.</li>
<li>بعد از ارتقای سیستم‌عامل با تغییر نسخه‌ی glibc (معروف‌ترینش glibc 2.28 در دبیان 10) ایندکس‌های متنی با collation libc باید REINDEX شوند؛ نمای <code>pg_database</code> ستون datcollversion دارد و پستگرس هنگام عدم تطابق هشدار می‌دهد.</li>
<li>collation غیرقطعی (deterministic = false) می‌تواند مقایسه‌ی بدون حساسیت به حروف بزرگ و کوچک بسازد، اما LIKE روی آن تا نسخه‌ی 18 اصلاً پشتیبانی نمی‌شد و ایندکس B-tree آن برای جست‌وجوی پیشوندی به کار نمی‌آید؛ با احتیاط استفاده کنید.</li>
<li><code>SET search_path</code> در یک تابع SECURITY DEFINER حیاتی است؛ بدون آن کاربر می‌تواند با ساختن تابع هم‌نام در schemaی خودش کد شما را ربوده و با مجوز صاحب تابع اجرا کند.</li>
<li>ICU_LOCALE با پسوندها قابل تنظیم است؛ مثلاً <code>fa-IR-u-kn-true</code> اعداد داخل رشته را عددی مرتب می‌کند تا «فرش 9» قبل از «فرش 10» بیاید.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۲ ─────────────────────────────
        {
            "title": "فصل ۲: SQL و انواع داده‌ی پستگرس",
            "lessons": [
                {
                    "title": "SQL پایه به سبک پستگرس: از SELECT تا RETURNING",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>چهار فرمان، با جزئیاتی که فرق ایجاد می‌کند</h2>
<p>SELECT، INSERT، UPDATE و DELETE را احتمالاً می‌شناسید؛ این درس روی جزئیاتی تمرکز دارد که پستگرس را از بقیه جدا می‌کند. یک جدول ساده برای تمرین:</p>
<pre><code class="language-sql">CREATE TABLE customers (
  id         bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  full_name  text NOT NULL,
  city       text,
  mobile     text,
  created_at timestamptz NOT NULL DEFAULT now()
);

INSERT INTO customers (full_name, city, mobile) VALUES
  ('فرش صدرا', 'کاشان', '09131234567'),
  ('بازرگانی نیک‌نام', 'تهران', NULL),
  ('گالری مهرآذین', 'آران و بیدگل', '09121112233')
RETURNING id, full_name;</code></pre>
<p><strong>RETURNING</strong> ردیف‌های درج‌شده، به‌روزشده یا حذف‌شده را همان‌جا برمی‌گرداند؛ دیگر لازم نیست برای گرفتن id یک SELECT جدا بزنید (کاری که در MySQL با LAST_INSERT_ID می‌کنید).</p>
<h3>فیلتر، NULL و مرتب‌سازی</h3>
<pre><code class="language-sql">SELECT id, full_name, coalesce(mobile, 'ندارد') AS mobile
FROM customers
WHERE city ILIKE 'کاشان%'            -- ILIKE: بدون حساسیت به بزرگی و کوچکی حروف لاتین
  AND mobile IS DISTINCT FROM '09130000000'
ORDER BY created_at DESC NULLS LAST, id
LIMIT 20;</code></pre>
<p>مقایسه با NULL همیشه NULL است، نه true یا false؛ پس <code>mobile &lt;&gt; 'x'</code> ردیف‌هایی که mobile ندارند را حذف می‌کند. <code>IS DISTINCT FROM</code> با NULL مثل یک مقدار عادی رفتار می‌کند.</p>
<h3>UPDATE و DELETE با جدول دیگر</h3>
<pre><code class="language-sql">UPDATE orders o
SET    status = 'cancelled'
FROM   customers c
WHERE  o.customer_id = c.id AND c.city = 'تهران' AND o.status = 'draft'
RETURNING o.id;

DELETE FROM order_items oi
USING  orders o
WHERE  oi.order_id = o.id AND o.status = 'cancelled';</code></pre>
<p>برای انتقال امن داده، RETURNING را با CTE ترکیب کنید: ردیف‌ها در یک دستور از جدول اصلی حذف و در آرشیو درج می‌شوند (در فصل ۴ مفصل‌تر):</p>
<pre><code class="language-sql">WITH moved AS (
  DELETE FROM orders WHERE created_at &lt; now() - interval '3 years' RETURNING *
)
INSERT INTO orders_archive SELECT * FROM moved;</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>در پستگرس NULLها در مرتب‌سازی صعودی <em>آخر</em> می‌آیند؛ در MySQL اول. اگر گزارشی را از MySQL منتقل می‌کنید، <code>NULLS FIRST/LAST</code> را صریح بنویسید.</li>
<li>صفحه‌بندی با OFFSET بزرگ کند است، چون همه‌ی ردیف‌های قبلی خوانده و دور ریخته می‌شوند. صفحه‌بندی keyset سریع است: <code>WHERE (created_at, id) &lt; ($1, $2) ORDER BY created_at DESC, id DESC LIMIT 20</code>؛ مقایسه‌ی ردیفی (tuple) در پستگرس از ایندکس چندستونی استفاده می‌کند.</li>
<li>ORDER BY بدون ستون یکتا (مثلاً فقط created_at) صفحه‌بندی ناپایدار می‌دهد؛ همیشه id را به‌عنوان ستون آخر اضافه کنید.</li>
<li>قبل از UPDATE دستی روی سرور تولید، <code>BEGIN;</code> بزنید، تعداد ردیف‌های گزارش‌شده را ببینید و بعد COMMIT یا ROLLBACK کنید؛ psql پیام UPDATE 3812 را درست قبل از فاجعه نشان می‌دهد.</li>
<li><code>TRUNCATE orders RESTART IDENTITY CASCADE</code> جدول و جدول‌های وابسته را خالی و شمارنده را صفر می‌کند؛ برخلاف MySQL، TRUNCATE در پستگرس تراکنشی است و ROLLBACK می‌شود.</li>
</ul>""",
                },
                {
                    "title": "عدد، متن و boolean: numeric برای پول، text در برابر varchar",
                    "kind": "text",
                    "minutes": 18,
                    "is_preview": False,
                    "body": r"""<h2>نوع داده‌ی درست، باگ‌های آینده را حذف می‌کند</h2>
<h3>انواع عددی</h3>
<table><thead><tr><th>نوع</th><th>بازه / دقت</th><th>کاربرد</th></tr></thead><tbody>
<tr><td>smallint</td><td>±32 هزار</td><td>کد وضعیت، تعداد رنگ نقشه</td></tr>
<tr><td>integer</td><td>±2.1 میلیارد</td><td>شمارنده‌های معمولی</td></tr>
<tr><td>bigint</td><td>±9.2×10^18</td><td>کلید اصلی، مبلغ به ریال</td></tr>
<tr><td>numeric(p,s)</td><td>دقیق، تا 131072 رقم</td><td>پول با اعشار، نرخ ارز، وزن دقیق</td></tr>
<tr><td>real / double precision</td><td>تقریبی (IEEE 754)</td><td>اندازه‌گیری علمی؛ هرگز پول</td></tr>
</tbody></table>
<p>حد integer برای مبالغ ریالی خطرناک است: 2,147,483,647 ریال فقط حدود ۲۱۴ میلیون تومان است و یک فاکتور فرش ماشینی عمده به‌راحتی از آن رد می‌شود. برای مبلغ ریالی بدون اعشار <code>bigint</code>، و اگر اعشار (دلار، یورو، نرخ) دارید <code>numeric(18,2)</code> یا دقت بیشتر.</p>
<pre><code class="language-sql">SELECT 0.1::float8 + 0.2::float8 = 0.3;        -- false
SELECT 0.1::numeric + 0.2::numeric = 0.3;      -- true
SELECT 7 / 2, 7 / 2.0, 7::numeric / 2;         -- 3 | 3.5000000000000000 | 3.5000000000000000
SELECT round(2.5::numeric), round(2.5::float8); -- 3 | 2</code></pre>
<p>نوع <code>money</code> را کنار بگذارید: نمایشش به تنظیم lc_monetary سرور وابسته است و با تغییر آن، همان داده متفاوت خوانده می‌شود.</p>
<h3>text، varchar و char</h3>
<p>در پستگرس <code>text</code> و <code>varchar(n)</code> دقیقاً یک ساختار ذخیره‌سازی دارند و از نظر سرعت فرقی نمی‌کنند؛ n فقط یک قید طول است. <code>char(n)</code> با فاصله پر می‌شود و تقریباً هیچ‌وقت انتخاب خوبی نیست. توصیه‌ی رایج: <code>text</code> به‌علاوه‌ی CHECK برای قاعده‌ی کسب‌وکار.</p>
<pre><code class="language-sql">CREATE TABLE designs (
  code   text PRIMARY KEY CHECK (code ~ '^[A-Z]{2}-[0-9]{3,5}$'),
  title  text NOT NULL CHECK (length(title) BETWEEN 2 AND 120),
  colors smallint NOT NULL CHECK (colors BETWEEN 1 AND 16),
  is_active boolean NOT NULL DEFAULT true
);
SELECT length('فرش کاشان'), octet_length('فرش کاشان');   -- 9 | 17</code></pre>
<p>مقادیر بلندتر از حدود ۲ کیلوبایت به‌طور خودکار فشرده و در جدول جانبی TOAST ذخیره می‌شوند؛ پس ذخیره‌ی توضیحات طولانی در text هیچ جریمه‌ای برای بقیه‌ی ستون‌ها ندارد.</p>
<h3>boolean</h3>
<p>boolean سه حالت دارد: true، false و NULL. ورودی‌های 't'، 'yes'، 'on' و '1' همه true پذیرفته می‌شوند. در WHERE مستقیم بنویسید <code>WHERE is_active</code> یا <code>WHERE NOT is_active</code>.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>round</code> روی numeric نیمه را از صفر دور می‌کند (2.5 به 3) اما روی float8 به نزدیک‌ترین زوج (2.5 به 2)؛ اختلاف چندریالی فاکتورها گاهی از همین است.</li>
<li>تبدیل <code>varchar(50)</code> به <code>varchar(100)</code> یا به <code>text</code> جدول را بازنویسی نمی‌کند و فوری است؛ اما کوتاه کردن طول یا تغییر به نوعی دیگر، کل جدول را با قفل انحصاری بازنویسی می‌کند.</li>
<li>هر کاراکتر فارسی در UTF-8 دو بایت است؛ <code>octet_length</code> برای برآورد حجم و <code>length</code> برای شمارش حروف. نیم‌فاصله هم یک کاراکتر (سه بایت) حساب می‌شود.</li>
<li>از نسخه‌ی 14 numeric مقدار Infinity هم می‌پذیرد؛ اگر نمی‌خواهید، <code>CHECK (price &lt; 'Infinity')</code> یا یک سقف واقعی بگذارید.</li>
<li>تبدیل رشته‌ی دارای ارقام فارسی به عدد خطا می‌دهد: <code>'۱۲۳'::int</code> نامعتبر است. در ورود داده <code>translate(s, '۰۱۲۳۴۵۶۷۸۹', '0123456789')</code> را بزنید.</li>
</ul>""",
                },
                {
                    "title": "زمان درست: timestamptz، interval و منطقه‌ی زمانی تهران",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>همیشه لحظه را ذخیره کنید، نه ساعت دیواری را</h2>
<p>پستگرس دو نوع زمان دارد: <code>timestamp</code> (بدون منطقه‌ی زمانی) و <code>timestamptz</code> (با منطقه‌ی زمانی). اسم دومی گمراه‌کننده است: timestamptz منطقه‌ی زمانی را ذخیره <em>نمی‌کند</em>؛ ورودی را به UTC تبدیل و ذخیره می‌کند و هنگام نمایش، با تنظیم <code>TimeZone</code> نشست به ساعت محلی برمی‌گرداند. یعنی یک لحظه‌ی مطلق در زمان. timestamp فقط «عددی روی ساعت دیواری» است که معلوم نیست مال کجاست.</p>
<pre><code class="language-sql">SET TIME ZONE 'Asia/Tehran';
SELECT now();                                  -- 2026-09-28 14:30:00.123+03:30
SELECT now() AT TIME ZONE 'UTC';               -- timestamp بدون منطقه: 11:00
SELECT '2026-03-20 08:00'::timestamptz;         -- در منطقه‌ی نشست تفسیر می‌شود
SELECT '2026-03-20 08:00+03:30'::timestamptz = '2026-03-20 04:30Z'::timestamptz;  -- true</code></pre>
<p>قاعده‌ی عملی: ستون‌های زمانی را <strong>timestamptz</strong> بگیرید، سرور را روی <code>timezone = 'UTC'</code> نگه دارید و در برنامه یا نشست، منطقه‌ی نمایش را تعیین کنید. جنگو با <code>USE_TZ = True</code> دقیقاً همین کار را می‌کند.</p>
<h3>date، time و interval</h3>
<pre><code class="language-sql">SELECT current_date + 7;                          -- date + عدد صحیح = روز
SELECT now() - interval '90 minutes';
SELECT age(timestamptz '2026-09-28', timestamptz '1990-03-21');  -- 36 years 6 mons 7 days
SELECT extract(epoch FROM interval '2 hours');   -- 7200
SELECT date_trunc('month', now());               -- ابتدای ماه میلادی
SELECT date_bin('15 minutes', now(), timestamptz '2026-01-01');  -- گرد کردن به بازه‌ی ۱۵ دقیقه‌ای</code></pre>
<h3>تاریخ شمسی</h3>
<p>پستگرس تقویم جلالی داخلی ندارد. روش استاندارد: همیشه میلادی (timestamptz) ذخیره کنید و تبدیل به شمسی را در لایه‌ی نمایش (مثلاً jdatetime در پایتون) انجام دهید. برای گزارش ماهانه‌ی شمسی، مرزهای ماه را در برنامه حساب کنید و به کوئری بدهید:</p>
<pre><code class="language-sql">-- مهر ۱۴۰۵ = 2026-09-23 تا 2026-10-23 (نیمه‌باز)
SELECT count(*), sum(total_rial)
FROM orders
WHERE created_at &gt;= timestamptz '2026-09-23 00:00+03:30'
  AND created_at &lt;  timestamptz '2026-10-23 00:00+03:30';</code></pre>
<p>اگر گزارش‌ها زیاد است، یک جدول تقویم (calendar) با ستون‌های تاریخ میلادی، سال و ماه و روز شمسی و تعطیلی بسازید و با آن JOIN کنید؛ یک بار پر می‌شود و همه‌ی گزارش‌ها ساده می‌شوند.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>now()</code> زمان <em>شروع تراکنش</em> است و در تمام تراکنش ثابت می‌ماند؛ برای زمان واقعی لحظه (مثلاً اندازه‌گیری مدت یک حلقه) از <code>clock_timestamp()</code> استفاده کنید.</li>
<li>ایران از سال ۲۰۲۳ ساعت تابستانی ندارد. اگر سروری tzdata قدیمی داشته باشد، ساعت‌های تابستان را با +04:30 نشان می‌دهد؛ بسته‌ی tzdata سیستم‌عامل را به‌روز کنید (بسته‌های دبیان و اوبونتو از tzdata سیستم استفاده می‌کنند).</li>
<li>برای بازه‌ی زمانی از <code>BETWEEN</code> استفاده نکنید؛ <code>BETWEEN '2026-09-01' AND '2026-09-30'</code> تقریباً کل روز آخر را جا می‌اندازد. همیشه <code>&gt;= شروع AND &lt; شروعِ بعدی</code>.</li>
<li>جمع کردن ماه با تاریخ آخر ماه عجیب است: <code>date '2026-01-31' + interval '1 month'</code> می‌شود 2026-02-28. برای سررسید اقساط، از روز اول ماه حساب کنید.</li>
<li><code>AT TIME ZONE</code> جهت را عوض می‌کند: روی timestamptz یک timestamp محلی می‌دهد و روی timestamp یک timestamptz. دوبار پشت‌سرهم زدنش منشأ خطای رایج ۳.۵ ساعته است.</li>
</ul>""",
                },
                {
                    "title": "شناسه‌ها و انواع ویژه: identity، uuid، enum، array، range و jsonb",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>ابزارهایی که MySQL ندارد</h2>
<h3>identity در برابر serial</h3>
<p><code>serial</code> روش قدیمی است: یک sequence جدا می‌سازد و DEFAULT ستون را روی nextval می‌گذارد. <code>GENERATED ... AS IDENTITY</code> روش استاندارد SQL و توصیه‌ی امروز است: sequence به ستون گره خورده، مجوزها ساده‌ترند و با ALWAYS نمی‌شود تصادفاً مقدار دستی درج کرد.</p>
<pre><code class="language-sql">CREATE TABLE looms (
  id        int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  code      text UNIQUE NOT NULL,
  reed      smallint NOT NULL,            -- شانه: 700، 1000، 1200
  density   smallint NOT NULL             -- تراکم: 2550، 3000
);
-- درج مقدار دستی (مثلاً هنگام مهاجرت داده):
INSERT INTO looms (id, code, reed, density) OVERRIDING SYSTEM VALUE VALUES (100, 'L-100', 1200, 3600);
SELECT setval(pg_get_serial_sequence('looms', 'id'), (SELECT max(id) FROM looms));</code></pre>
<h3>uuid</h3>
<p><code>gen_random_uuid()</code> از نسخه‌ی 13 داخلی است و uuid نسخه‌ی 4 (کاملاً تصادفی) می‌سازد. uuid برای شناسه‌ای که در URL یا بین سیستم‌ها جابه‌جا می‌شود عالی است، اما تصادفی بودن آن درج در ایندکس B-tree را پراکنده می‌کند. نسخه‌ی 18 تابع <code>uuidv7()</code> را اضافه کرده که بر اساس زمان مرتب است و این مشکل را ندارد.</p>
<h3>enum</h3>
<pre><code class="language-sql">CREATE TYPE order_status AS ENUM ('draft', 'confirmed', 'weaving', 'finishing', 'delivered', 'cancelled');
ALTER TYPE order_status ADD VALUE 'qc' BEFORE 'finishing';</code></pre>
<p>enum چهار بایت جا می‌گیرد و به ترتیب تعریف مرتب می‌شود. اما حذف یا تغییر نام مقدار دردسر دارد؛ برای فهرست‌هایی که کاربر مدیریت می‌کند جدول مرجع با کلید خارجی بهتر است.</p>
<h3>array</h3>
<pre><code class="language-sql">CREATE TABLE products (id int PRIMARY KEY, name text, tags text[] NOT NULL DEFAULT '{}');
INSERT INTO products VALUES (1, 'فرش ۱۲۰۰ شانه افشان', ARRAY['ماشینی', 'اکریلیک', 'کلاسیک']);
SELECT name FROM products WHERE 'کلاسیک' = ANY (tags);
SELECT name FROM products WHERE tags @&gt; ARRAY['ماشینی', 'اکریلیک'];   -- شامل هر دو</code></pre>
<h3>range</h3>
<p>بازه‌ها (<code>int4range</code>، <code>numrange</code>، <code>daterange</code>، <code>tstzrange</code>) یک نوع داده‌اند با عملگرهای هم‌پوشانی (<code>&amp;&amp;</code>) و شمول (<code>@&gt;</code>). پیش‌فرض کران‌ها <code>[)</code> است: ابتدا شامل، انتها نه.</p>
<pre><code class="language-sql">SELECT tstzrange('2026-09-28 08:00+03:30', '2026-09-28 16:00+03:30') &amp;&amp;
       tstzrange('2026-09-28 15:00+03:30', '2026-09-28 20:00+03:30');   -- true
SELECT daterange('2026-09-23', '2026-10-23') @&gt; current_date;</code></pre>
<h3>jsonb</h3>
<p><code>json</code> متن خام را نگه می‌دارد؛ <code>jsonb</code> ساختار باینری تجزیه‌شده است: کلیدهای تکراری حذف و ترتیب کلیدها عوض می‌شود، اما قابل ایندکس و بسیار سریع‌تر در جست‌وجوست. تقریباً همیشه jsonb می‌خواهید؛ عملگرها و ایندکس آن در فصل‌های ۴ و ۵.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>sequenceها تراکنشی نیستند: INSERT ناموفق یا ROLLBACK‌شده هم یک عدد مصرف می‌کند. شماره‌ی فاکتور بدون حفره را با sequence نسازید؛ یک جدول شمارنده با <code>UPDATE ... RETURNING</code> داخل همان تراکنش لازم است.</li>
<li>آرایه‌ها از ۱ شروع می‌شوند و <code>array_length('{}'::int[], 1)</code> مقدار NULL برمی‌گرداند نه صفر؛ برای شمارش از <code>cardinality()</code> استفاده کنید.</li>
<li><code>ALTER TYPE ... ADD VALUE</code> داخل تراکنش مجاز است، اما مقدار جدید تا commit همان تراکنش قابل استفاده نیست؛ migrationی که مقدار را اضافه و بلافاصله استفاده می‌کند شکست می‌خورد.</li>
<li>از نسخه‌ی 14، multirange هم داریم: <code>range_agg(during)</code> چند بازه‌ی هم‌پوشان را به یک مجموعه‌ی ادغام‌شده تبدیل می‌کند؛ برای محاسبه‌ی «ساعت‌های کاری واقعی یک دستگاه» عالی است.</li>
<li>در jsonb عدد با دقت numeric ذخیره می‌شود، اما در JavaScript بیشتر از 2^53 دقت از دست می‌رود؛ شناسه‌های bigint را در API به‌صورت رشته بفرستید.</li>
</ul>""",
                },
                {
                    "title": "upsert با ON CONFLICT، MERGE، DISTINCT ON و generate_series",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>چهار ابزار که کد برنامه را کوتاه می‌کنند</h2>
<h3>INSERT ... ON CONFLICT (upsert)</h3>
<p>مسئله‌ی کلاسیک: موجودی انبار نخ را به‌روز کنید؛ اگر ردیف نیست بسازید، اگر هست اضافه کنید. «اول SELECT، بعد INSERT یا UPDATE» در بار هم‌زمان شکست می‌خورد. ON CONFLICT این کار را اتمی انجام می‌دهد:</p>
<pre><code class="language-sql">CREATE TABLE yarn_stock (
  warehouse_id int,
  yarn_code    text,
  kg           numeric(12,3) NOT NULL,
  updated_at   timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (warehouse_id, yarn_code)
);

INSERT INTO yarn_stock AS s (warehouse_id, yarn_code, kg)
VALUES (1, 'AC-RED-12', 250)
ON CONFLICT (warehouse_id, yarn_code)
DO UPDATE SET kg = s.kg + EXCLUDED.kg, updated_at = now()
WHERE s.kg + EXCLUDED.kg &gt;= 0
RETURNING *, (xmax = 0) AS inserted;</code></pre>
<p><code>EXCLUDED</code> ردیفی است که قصد درجش را داشتید. هدف تعارض باید یک UNIQUE یا PRIMARY KEY واقعی (یا ایندکس یکتای منطبق) باشد. <code>DO NOTHING</code> هم برای «اگر هست، کاری نکن» کاربرد دارد.</p>
<h3>MERGE (نسخه‌ی 15 به بعد)</h3>
<p>MERGE استاندارد SQL است و برای همگام‌سازی یک جدول با جدول staging خواناتر است؛ حذف را هم پوشش می‌دهد. از نسخه‌ی 17 RETURNING و تابع <code>merge_action()</code> هم دارد:</p>
<pre><code class="language-sql">MERGE INTO designs d
USING staging_designs s ON d.code = s.code
WHEN MATCHED AND s.deleted THEN DELETE
WHEN MATCHED THEN UPDATE SET title = s.title, colors = s.colors
WHEN NOT MATCHED AND NOT s.deleted THEN INSERT (code, title, colors) VALUES (s.code, s.title, s.colors)
RETURNING merge_action(), d.code;</code></pre>
<h3>DISTINCT ON: «آخرین ردیف هر گروه»</h3>
<pre><code class="language-sql">-- آخرین سفارش هر مشتری
SELECT DISTINCT ON (customer_id) customer_id, id, total_rial, created_at
FROM orders
ORDER BY customer_id, created_at DESC, id DESC;</code></pre>
<p>ستون‌های DISTINCT ON باید اول ORDER BY بیایند؛ باقی ORDER BY تعیین می‌کند کدام ردیف گروه نگه داشته شود.</p>
<h3>generate_series: پر کردن جاهای خالی</h3>
<pre><code class="language-sql">-- فروش روزانه‌ی ۳۰ روز اخیر، حتی روزهایی که فروش صفر بوده
SELECT d::date AS day, coalesce(sum(o.total_rial), 0) AS sales
FROM generate_series(current_date - 29, current_date, interval '1 day') AS d
LEFT JOIN orders o ON o.created_at &gt;= d AND o.created_at &lt; d + interval '1 day'
GROUP BY d ORDER BY d;

-- ۱۰۰ هزار ردیف داده‌ی آزمایشی
INSERT INTO customers (full_name, city)
SELECT 'مشتری ' || i, (ARRAY['کاشان','تهران','مشهد','تبریز'])[1 + i % 4]
FROM generate_series(1, 100000) AS i;</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>ترفند <code>RETURNING (xmax = 0) AS inserted</code> نشان می‌دهد ردیف تازه درج شده یا به‌روز شده است؛ رسمی مستند نیست اما سال‌هاست همه از آن استفاده می‌کنند.</li>
<li>اگر یک دستور INSERT چندردیفی دو ردیف با کلید یکسان داشته باشد، خطای <code>ON CONFLICT DO UPDATE command cannot affect row a second time</code> می‌گیرید؛ داده را قبلاً با DISTINCT ON یکتا کنید.</li>
<li>هر upsert حتی وقتی به UPDATE ختم شود یک عدد از sequence مصرف می‌کند؛ جدول‌هایی که بیشتر upsert می‌خورند شناسه‌های پرحفره دارند و با int زودتر به سقف می‌رسند.</li>
<li>MERGE برخلاف ON CONFLICT در برابر درج هم‌زمان مقاوم نیست و ممکن است خطای کلید تکراری بدهد؛ برای بار هم‌زمان بالا ON CONFLICT امن‌تر است.</li>
<li>برای اینکه DISTINCT ON روی جدول بزرگ سریع باشد، ایندکس <code>(customer_id, created_at DESC)</code> بسازید؛ اگر تعداد گروه‌ها کم و ردیف‌ها زیاد است، LATERAL با LIMIT 1 (فصل ۴) سریع‌تر است.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۳ ─────────────────────────────
        {
            "title": "فصل ۳: طراحی و قیدها — داده‌ای که نمی‌شود خرابش کرد",
            "lessons": [
                {
                    "title": "کلید اصلی و خارجی: ON DELETE، ایندکس FK، DEFERRABLE و NOT VALID",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>روابط را به دیتابیس بسپارید، نه به برنامه</h2>
<p>هر برنامه‌ای یک روز باگ دارد، یک اسکریپت دستی روی سرور اجرا می‌شود یا یک سرویس دوم به همان دیتابیس وصل می‌شود. کلید خارجی (FOREIGN KEY) تضمین می‌کند سفارشی بدون مشتری یا ردیف سفارشی بدون سفارش هیچ‌وقت وجود نداشته باشد، مهم نیست داده از کجا آمده باشد.</p>
<pre><code class="language-sql">CREATE TABLE orders (
  id          bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  customer_id bigint NOT NULL REFERENCES customers (id) ON DELETE RESTRICT,
  created_at  timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE order_items (
  id       bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  order_id bigint NOT NULL REFERENCES orders (id) ON DELETE CASCADE,
  qty      int NOT NULL CHECK (qty &gt; 0)
);
CREATE INDEX ON orders (customer_id);
CREATE INDEX ON order_items (order_id);</code></pre>
<table><thead><tr><th>رفتار</th><th>وقتی والد حذف شود</th><th>مناسب برای</th></tr></thead><tbody>
<tr><td>NO ACTION / RESTRICT</td><td>خطا (پیش‌فرض)</td><td>مشتری و سفارش؛ حذف نباید ممکن باشد</td></tr>
<tr><td>CASCADE</td><td>فرزندها هم حذف می‌شوند</td><td>اقلام سفارش که بدون سفارش معنا ندارند</td></tr>
<tr><td>SET NULL / SET DEFAULT</td><td>ستون فرزند خالی می‌شود</td><td>«مسئول پیگیری» که ممکن است از شرکت برود</td></tr>
</tbody></table>
<h3>ایندکس ستون FK خودکار نیست</h3>
<p>پستگرس برای ستون مرجع (مثل orders.customer_id) ایندکس نمی‌سازد. بدون آن، حذف یا تغییر هر مشتری یک Seq Scan کامل روی orders اجرا می‌کند و JOINها هم کند می‌شوند. این کوئری FKهای بدون ایندکس (ستون اول) را پیدا می‌کند:</p>
<pre><code class="language-sql">SELECT c.conrelid::regclass AS tbl, c.conname, a.attname
FROM pg_constraint c
JOIN pg_attribute a ON a.attrelid = c.conrelid AND a.attnum = c.conkey[1]
WHERE c.contype = 'f'
  AND NOT EXISTS (SELECT 1 FROM pg_index i
                  WHERE i.indrelid = c.conrelid AND i.indkey[0] = c.conkey[1]);</code></pre>
<h3>DEFERRABLE: بررسی در پایان تراکنش</h3>
<p>به‌طور پیش‌فرض قید بعد از هر دستور بررسی می‌شود. گاهی لازم است وضعیت موقتاً نامعتبر باشد؛ مثلاً جابه‌جا کردن ترتیب دو نقشه در کاتالوگ که روی (catalog_id, position) قید UNIQUE دارد:</p>
<pre><code class="language-sql">ALTER TABLE catalog_items
  ADD CONSTRAINT uq_position UNIQUE (catalog_id, position) DEFERRABLE INITIALLY IMMEDIATE;

BEGIN;
SET CONSTRAINTS uq_position DEFERRED;
UPDATE catalog_items SET position = 2 WHERE id = 10;
UPDATE catalog_items SET position = 1 WHERE id = 11;
COMMIT;   -- بررسی همین‌جا انجام می‌شود</code></pre>
<h3>افزودن FK به جدول بزرگ بدون توقف</h3>
<pre><code class="language-sql">ALTER TABLE order_items ADD CONSTRAINT fk_design
  FOREIGN KEY (design_code) REFERENCES designs (code) NOT VALID;   -- فوری
ALTER TABLE order_items VALIDATE CONSTRAINT fk_design;             -- بدون قفل سنگین نوشتن</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>هر درج در جدول فرزند روی ردیف والد قفل <code>FOR KEY SHARE</code> می‌گیرد؛ اگر هزاران درج هم‌زمان به یک والد اشاره کنند (مثلاً «مشتری نقدی» پیش‌فرض)، روی آن ردیف رقابت قفل ایجاد می‌شود.</li>
<li>قید UNIQUE یا PK که DEFERRABLE باشد نمی‌تواند هدف <code>ON CONFLICT</code> باشد؛ اگر upsert لازم دارید، آن قید را immediate نگه دارید.</li>
<li>از نسخه‌ی 15 می‌توانید فقط بخشی از ستون‌های FK مرکب را NULL کنید: <code>ON DELETE SET NULL (assignee_id)</code> بدون دست زدن به tenant_id.</li>
<li>ON DELETE CASCADE زنجیره‌ای می‌تواند با یک DELETE کوچک هزاران ردیف را در چند جدول پاک کند؛ روی جدول‌های مالی به‌جای آن soft delete یا RESTRICT را ترجیح دهید.</li>
<li>pg_dump داده را اول و قیدها را آخر بازمی‌گرداند؛ پس ترتیب درج جدول‌ها هنگام restore مشکل FK نمی‌سازد، اما <code>--data-only</code> چنین مزیتی ندارد و <code>--disable-triggers</code> لازم می‌شود.</li>
</ul>""",
                },
                {
                    "title": "UNIQUE، CHECK، domain و ستون‌های generated",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>قاعده‌های کسب‌وکار را در خود جدول بنویسید</h2>
<h3>UNIQUE و NULL</h3>
<p>در SQL دو NULL با هم برابر نیستند؛ پس UNIQUE اجازه می‌دهد چند ردیف NULL داشته باشید. گاهی همین را می‌خواهیم (مشتری‌هایی که ایمیل ندارند) و گاهی نه. از نسخه‌ی 15:</p>
<pre><code class="language-sql">CREATE TABLE price_list (
  design_code text NOT NULL,
  size_code   text NOT NULL,
  dealer_id   int,                 -- NULL یعنی قیمت عمومی
  price_rial  bigint NOT NULL CHECK (price_rial &gt; 0),
  UNIQUE NULLS NOT DISTINCT (design_code, size_code, dealer_id)
);

-- یکتایی فقط بین رکوردهای فعال (soft delete)
CREATE UNIQUE INDEX uq_customer_mobile_active
  ON customers (mobile) WHERE deleted_at IS NULL;</code></pre>
<h3>CHECK</h3>
<p>CHECK هر عبارتی روی ستون‌های <em>همان ردیف</em> را می‌پذیرد:</p>
<pre><code class="language-sql">ALTER TABLE orders
  ADD CONSTRAINT chk_delivery CHECK (delivered_at IS NULL OR delivered_at &gt;= created_at),
  ADD CONSTRAINT chk_discount CHECK (discount_pct BETWEEN 0 AND 30);</code></pre>
<h3>domain: نوع داده با قاعده</h3>
<p>domain یک نوع پایه به‌علاوه‌ی قید است که یک بار تعریف و همه‌جا استفاده می‌شود. مثال بومی: موبایل و کد ملی با الگوریتم رقم کنترل.</p>
<pre><code class="language-sql">CREATE DOMAIN mobile_ir AS text CHECK (VALUE ~ '^09[0-9]{9}$');

CREATE FUNCTION is_valid_melli_code(c text) RETURNS boolean
LANGUAGE sql IMMUTABLE STRICT AS $$
  SELECT CASE WHEN c !~ '^[0-9]{10}$' OR c ~ '^(\d)\1{9}$' THEN false
  ELSE (SELECT CASE WHEN r &lt; 2 THEN r ELSE 11 - r END = substr(c, 10, 1)::int
        FROM (SELECT sum(substr(c, i, 1)::int * (11 - i)) % 11 AS r
              FROM generate_series(1, 9) AS i) s)
  END
$$;

CREATE DOMAIN melli_code AS text CHECK (is_valid_melli_code(VALUE));

CREATE TABLE weavers (
  id     int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name   text NOT NULL,
  mobile mobile_ir,
  code   melli_code UNIQUE
);</code></pre>
<h3>ستون‌های generated</h3>
<p>ستونی که همیشه از ستون‌های دیگر حساب می‌شود و دستی قابل نوشتن نیست؛ مساحت فرش یا جمع ردیف فاکتور:</p>
<pre><code class="language-sql">ALTER TABLE order_items
  ADD COLUMN width_cm  int NOT NULL DEFAULT 300,
  ADD COLUMN length_cm int NOT NULL DEFAULT 400,
  ADD COLUMN area_m2 numeric(6,2) GENERATED ALWAYS AS (width_cm * length_cm / 10000.0) STORED;</code></pre>
<p>در نسخه‌های 16 و 17 فقط STORED داریم (روی دیسک ذخیره می‌شود و قابل ایندکس است). نسخه‌ی 18 ستون VIRTUAL را اضافه کرده و آن را پیش‌فرض کرده است؛ هنگام خواندن محاسبه می‌شود.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>CHECK با نتیجه‌ی NULL <em>قبول</em> می‌شود؛ <code>CHECK (discount_pct &lt;= 30)</code> ردیف با discount_pct خالی را رد نمی‌کند. اگر مقدار الزامی است NOT NULL را جدا بگذارید.</li>
<li>عبارت ستون generated و ایندکس عبارتی باید IMMUTABLE باشد و پستگرس آن را بررسی می‌کند؛ در CHECK بررسی نمی‌شود، اما قاعده همان است: CHECK با <code>now()</code> یا ::date روی timestamptz فقط لحظه‌ی درج را می‌سنجد و بعد از restore ممکن است شکست بخورد. اگر تابعی را به دروغ IMMUTABLE اعلام کنید، ایندکس‌ها بی‌صدا نادرست می‌شوند.</li>
<li>UNIQUE و PRIMARY KEY خودشان ایندکس می‌سازند؛ ایندکس دستی روی همان ستون فقط نوشتن را کند و فضا را دوبرابر می‌کند. در <code>\d</code> جدول، ایندکس‌های تکراری را جست‌وجو کنید.</li>
<li><code>ALTER TABLE ... ADD CONSTRAINT ... CHECK (...) NOT VALID</code> و سپس VALIDATE، مثل FK، اجازه می‌دهد روی جدول بزرگ بدون قفل طولانی قید اضافه کنید.</li>
<li>domainی که NOT NULL دارد باز هم در خروجی LEFT JOIN یا ستون تازه اضافه‌شده NULL می‌گیرد؛ مستندات خود پستگرس توصیه می‌کند NOT NULL را روی ستون بگذارید نه روی domain.</li>
</ul>""",
                },
                {
                    "title": "قید EXCLUDE: جلوگیری از هم‌پوشانی رزرو دستگاه بافندگی",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>قیدی که هیچ دیتابیس رایج دیگری ندارد</h2>
<p>برنامه‌ریزی تولید در یک کارخانه‌ی فرش ماشینی: هر سفارش باید در یک بازه‌ی زمانی روی یک دستگاه بافندگی بافته شود و یک دستگاه نمی‌تواند هم‌زمان دو کار داشته باشد. UNIQUE این را تضمین نمی‌کند، چون بازه‌ها لازم نیست برابر باشند تا تداخل کنند؛ کافی است <em>هم‌پوشانی</em> داشته باشند. کد برنامه هم در بار هم‌زمان قابل اعتماد نیست: دو برنامه‌ریز هم‌زمان SELECT می‌زنند، هر دو دستگاه را خالی می‌بینند و هر دو رزرو می‌کنند.</p>
<p>قید <strong>EXCLUDE</strong> تعمیم UNIQUE است: «هیچ دو ردیفی نباشند که برای همه‌ی این جفت‌ستون‌ها، این عملگرها true برگردانند».</p>
<pre><code class="language-sql">CREATE EXTENSION IF NOT EXISTS btree_gist;

CREATE TABLE loom_bookings (
  id       bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  loom_id  int NOT NULL REFERENCES looms (id),
  order_id bigint NOT NULL REFERENCES orders (id),
  during   tstzrange NOT NULL CHECK (NOT isempty(during)),
  status   text NOT NULL DEFAULT 'planned',
  EXCLUDE USING gist (loom_id WITH =, during WITH &amp;&amp;) WHERE (status &lt;&gt; 'cancelled')
);</code></pre>
<p>ترجمه: هیچ دو رزرو غیرلغوشده‌ای نباشند که loom_id آن‌ها برابر و بازه‌شان هم‌پوشان باشد. اکستنشن <strong>btree_gist</strong> لازم است چون ایندکس GiST به‌طور پیش‌فرض عملگر = را برای int بلد نیست.</p>
<pre><code class="language-sql">INSERT INTO loom_bookings (loom_id, order_id, during)
VALUES (3, 501, '[2026-09-28 08:00+03:30, 2026-09-30 20:00+03:30)');

INSERT INTO loom_bookings (loom_id, order_id, during)
VALUES (3, 502, '[2026-09-30 18:00+03:30, 2026-10-02 08:00+03:30)');
-- ERROR:  conflicting key value violates exclusion constraint "loom_bookings_loom_id_during_excl"

INSERT INTO loom_bookings (loom_id, order_id, during)
VALUES (3, 502, '[2026-09-30 20:00+03:30, 2026-10-02 08:00+03:30)');   -- مجاز: بازه‌ها فقط مجاورند</code></pre>
<h3>پرسیدن از همان ایندکس</h3>
<pre><code class="language-sql">-- الان روی دستگاه ۳ چه چیزی بافته می‌شود؟
SELECT order_id FROM loom_bookings
WHERE loom_id = 3 AND during @&gt; now() AND status &lt;&gt; 'cancelled';

-- مجموع ساعت‌های رزروشده‌ی هر دستگاه در مهر
SELECT loom_id,
       sum(upper(r) - lower(r)) AS busy
FROM loom_bookings,
     LATERAL (SELECT during * tstzrange('2026-09-23 00:00+03:30','2026-10-23 00:00+03:30') AS r) x
WHERE status &lt;&gt; 'cancelled' AND NOT isempty(r)
GROUP BY loom_id;</code></pre>
<p>عملگر <code>*</code> روی range، اشتراک دو بازه است؛ همین باعث می‌شود رزروی که از شهریور شروع شده فقط سهم مهرش را حساب کند.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>کد خطای نقض EXCLUDE <code>23P01</code> (exclusion_violation) است، متفاوت با <code>23505</code> برای UNIQUE؛ در برنامه هر دو را جدا بگیرید تا پیام مناسب («دستگاه در این بازه رزرو است») نشان دهید.</li>
<li>قید EXCLUDE فقط با <code>ON CONFLICT DO NOTHING</code> کار می‌کند، نه DO UPDATE.</li>
<li>نوشتن بازه با <code>[)</code> (نیمه‌باز) کلید کار است: پایان یک شیفت دقیقاً شروع شیفت بعدی است و تداخل حساب نمی‌شود. با <code>[]</code> دو شیفت پشت‌سرهم با هم تعارض پیدا می‌کنند.</li>
<li>برای رزرو با واحد روز (اتاق مهمان‌سرا یا سالن نمایشگاه) از <code>daterange</code> استفاده کنید؛ daterange خودش کران‌ها را به شکل canonical <code>[)</code> درمی‌آورد.</li>
<li>نسخه‌ی 18 کلید اصلی زمانی را اضافه کرده است: <code>PRIMARY KEY (loom_id, during WITHOUT OVERLAPS)</code> که همین قید را با نحو استاندارد SQL:2011 می‌سازد.</li>
</ul>""",
                },
                {
                    "title": "نرمال‌سازی، jsonb آگاهانه و schemaها برای جداسازی",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>کجا ستون، کجا jsonb، کجا جدول جدا</h2>
<h3>نرمال‌سازی در یک نگاه</h3>
<p>هدف نرمال‌سازی این است که هر واقعیت فقط یک جا ثبت شود. اگر نام شهر مشتری در جدول سفارش هم کپی شود، روزی که مشتری آدرس عوض کند، سفارش‌های قدیمی و جدید دو شهر مختلف نشان می‌دهند و نمی‌دانید کدام درست است.</p>
<table><thead><tr><th>فرم</th><th>قاعده</th><th>مثال نقض</th></tr></thead><tbody>
<tr><td>1NF</td><td>هر خانه یک مقدار اتمی</td><td>ستون colors با مقدار «لاکی، سرمه‌ای، کرم» به‌صورت رشته‌ی جداشده با ویرگول</td></tr>
<tr><td>2NF</td><td>ستون‌ها به کل کلید وابسته‌اند</td><td>نام نقشه در order_items که فقط به design_code وابسته است</td></tr>
<tr><td>3NF</td><td>ستون غیرکلیدی به ستون غیرکلیدی دیگر وابسته نیست</td><td>استان مشتری کنار شهرش (استان از شهر معلوم است)</td></tr>
</tbody></table>
<p>استثنای آگاهانه: <strong>قیمت در لحظه‌ی فروش</strong>. unit_price در ردیف سفارش باید کپی شود، چون قیمت نقشه فردا عوض می‌شود ولی فاکتور دیروز نباید عوض شود. این تکرار نیست، ثبت یک واقعیت تاریخی است.</p>
<h3>jsonb: برای چه چیزی، نه برای همه‌چیز</h3>
<p>jsonb جای مناسبی است برای ویژگی‌هایی که واقعاً متغیرند: مشخصات فنی که برای فرش ماشینی، دستباف و تابلوفرش فرق می‌کند؛ پاسخ خام درگاه پرداخت؛ تنظیمات کاربر. اما ستونی که در WHERE و JOIN و گزارش مدام استفاده می‌شود، یا کلید خارجی است، باید ستون واقعی باشد.</p>
<pre><code class="language-sql">CREATE TABLE products (
  id        bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  kind      text NOT NULL CHECK (kind IN ('machine', 'handmade', 'tableau')),
  title     text NOT NULL,
  price_rial bigint NOT NULL,
  specs     jsonb NOT NULL DEFAULT '{}',
  CONSTRAINT specs_is_object CHECK (jsonb_typeof(specs) = 'object'),
  CONSTRAINT machine_specs CHECK (kind &lt;&gt; 'machine' OR specs ?&amp; ARRAY['reed', 'density'])
);
INSERT INTO products (kind, title, price_rial, specs) VALUES
 ('machine', 'افشان لاکی', 185000000, '{"reed": 1200, "density": 3600, "yarn": "اکریلیک"}'),
 ('handmade', 'کاشان کرک', 2400000000, '{"knots_per_cm2": 64, "material": "کرک و ابریشم"}');</code></pre>
<h3>schemaها برای جداسازی</h3>
<pre><code class="language-sql">CREATE SCHEMA factory;   -- جدول‌های اصلی
CREATE SCHEMA audit;     -- تاریخچه‌ی تغییرات
CREATE SCHEMA report;    -- ویوها و materialized viewهای گزارش
CREATE SCHEMA staging;   -- داده‌ی ورودی خام اکسل پیش از پاک‌سازی
GRANT USAGE ON SCHEMA report TO bi_reader;</code></pre>
<p>schema واحد مجوز هم هست: به تیم گزارش فقط USAGE روی report بدهید و هیچ دسترسی به factory نداشته باشند.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>هر UPDATE روی یک کلید jsonb کل سند را بازنویسی می‌کند (و اگر بزرگ باشد، کل مقدار TOAST را)؛ سند چندصد کیلوبایتی که مدام یک شمارنده‌اش عوض می‌شود، WAL و bloat عظیم می‌سازد. شمارنده را ستون کنید.</li>
<li>برنامه‌ریز برای عبارت‌های داخل jsonb آمار ندارد و معمولاً تعداد ردیف را اشتباه تخمین می‌زند؛ اگر یک کلید jsonb در فیلترها زیاد می‌آید، آن را ستون generated کنید یا روی عبارتش ایندکس بسازید تا آمار جمع شود.</li>
<li>الگوی EAV (جدول entity، attribute، value) تقریباً همیشه از jsonb بدتر است: هر کوئری ده JOIN و هیچ نوع داده‌ای.</li>
<li>مدل «یک schema برای هر مشتری» (multi-tenant) با چند ده مشتری خوب است، اما با هزاران schema کاتالوگ سیستمی حجیم، pg_dump کند و هر migration هزار برابر می‌شود؛ برای تعداد بالا ستون tenant_id و RLS (فصل ۷) بهتر است.</li>
<li><code>COMMENT ON COLUMN products.specs IS '...'</code> مستندات را کنار خود داده نگه می‌دارد و در <code>\d+</code> و pgAdmin و DBeaver دیده می‌شود.</li>
</ul>""",
                },
                {
                    "title": "طراحی نمونه: دیتابیس تولید و سفارش کارخانه‌ی فرش",
                    "kind": "text",
                    "minutes": 26,
                    "is_preview": False,
                    "body": r"""<h2>از نیازمندی تا DDL</h2>
<p>یک کارخانه‌ی فرش ماشینی در کاشان را در نظر بگیرید: مشتری‌ها (فروشگاه‌ها و بنکداران) سفارش می‌دهند؛ هر سفارش چند ردیف دارد (نقشه، ابعاد، تعداد، قیمت)؛ هر ردیف روی یک دستگاه بافندگی در یک بازه‌ی زمانی بافته می‌شود و پس از بافت، کنترل کیفیت درجه و عیوب را ثبت می‌کند. همین طرح در فصل‌های بعد پایه‌ی کوئری‌ها، ایندکس‌ها و پروژه‌ی پایانی است.</p>
<pre><code class="language-sql">CREATE SCHEMA factory;
SET search_path = factory, public;
CREATE EXTENSION IF NOT EXISTS btree_gist;

CREATE DOMAIN mobile_ir AS text CHECK (VALUE ~ '^09[0-9]{9}$');
CREATE TYPE order_status AS ENUM ('draft','confirmed','weaving','finishing','delivered','cancelled');

CREATE TABLE customers (
  id         bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  full_name  text NOT NULL,
  city       text NOT NULL,
  mobile     mobile_ir,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE designs (
  code    text PRIMARY KEY,                 -- مثل AF-1203
  title   text NOT NULL,                    -- افشان، هریس، وکیلی
  reed    smallint NOT NULL CHECK (reed IN (500, 700, 1000, 1200, 1500)),
  density smallint NOT NULL,
  colors  smallint NOT NULL CHECK (colors BETWEEN 1 AND 16),
  tags    text[] NOT NULL DEFAULT '{}'
);

CREATE TABLE looms (
  id        int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  code      text NOT NULL UNIQUE,
  reed      smallint NOT NULL,
  hall      text NOT NULL,
  is_active boolean NOT NULL DEFAULT true
);

CREATE TABLE orders (
  id          bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  customer_id bigint NOT NULL REFERENCES customers,
  status      order_status NOT NULL DEFAULT 'draft',
  due_date    date,
  created_at  timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE order_items (
  id              bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  order_id        bigint NOT NULL REFERENCES orders ON DELETE CASCADE,
  design_code     text NOT NULL REFERENCES designs,
  width_cm        int NOT NULL CHECK (width_cm BETWEEN 50 AND 600),
  length_cm       int NOT NULL CHECK (length_cm BETWEEN 50 AND 1200),
  qty             int NOT NULL CHECK (qty &gt; 0),
  unit_price_rial bigint NOT NULL CHECK (unit_price_rial &gt;= 0),
  line_total_rial bigint GENERATED ALWAYS AS (qty * unit_price_rial) STORED
);

CREATE TABLE production_runs (
  id            bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  order_item_id bigint NOT NULL REFERENCES order_items,
  loom_id       int NOT NULL REFERENCES looms,
  during        tstzrange NOT NULL,
  produced_qty  int NOT NULL DEFAULT 0,
  EXCLUDE USING gist (loom_id WITH =, during WITH &amp;&amp;)
);

CREATE TABLE qc_inspections (
  id           bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  run_id       bigint NOT NULL REFERENCES production_runs,
  inspected_at timestamptz NOT NULL DEFAULT now(),
  grade        smallint NOT NULL CHECK (grade BETWEEN 1 AND 3),
  defects      jsonb NOT NULL DEFAULT '{}'    -- {"رج_کشی": 2, "پرز_دهی": 1}
);

CREATE INDEX ON orders (customer_id);
CREATE INDEX ON orders (status, created_at);
CREATE INDEX ON order_items (order_id);
CREATE INDEX ON order_items (design_code);
CREATE INDEX ON production_runs (order_item_id);
CREATE INDEX ON qc_inspections (run_id);</code></pre>
<h3>تصمیم‌های طراحی</h3>
<ul>
<li>کلید نقشه طبیعی (code) است چون در کارخانه همه با همین کد صحبت می‌کنند و ثابت است؛ بقیه کلید جایگزین bigint دارند.</li>
<li>قیمت در order_items کپی می‌شود (واقعیت تاریخی) و جمع ردیف generated است تا هیچ‌وقت با qty و قیمت ناهمخوان نشود.</li>
<li>عیوب کنترل کیفیت متغیرند، پس jsonb؛ اما درجه (grade) که در گزارش‌ها فیلتر می‌شود ستون واقعی است.</li>
</ul>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>REFERENCES customers</code> بدون نام ستون، خودکار به کلید اصلی آن جدول اشاره می‌کند.</li>
<li>کل این اسکریپت را داخل <code>BEGIN; ... COMMIT;</code> اجرا کنید؛ اگر خط چهلم خطا داشت، نیمه‌کاره نمی‌ماند (DDL تراکنشی).</li>
<li>ایندکس <code>(status, created_at)</code> برای کوئری‌های «سفارش‌های باز این ماه» است؛ ستون تساوی (status) اول و ستون بازه (created_at) دوم بیاید.</li>
<li>برای ثابت ماندن نام قیدها در migrationها، به آن‌ها نام صریح بدهید؛ نام خودکار (مثل orders_customer_id_fkey) با تغییر نام ستون عوض نمی‌شود و بعدها گیج‌کننده است.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۴ ─────────────────────────────
        {
            "title": "فصل ۴: کوئری‌نویسی پیشرفته",
            "lessons": [
                {
                    "title": "JOINها، EXISTS و LATERAL",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>ترکیب جدول‌ها بدون غافل‌گیری</h2>
<p>INNER JOIN فقط ردیف‌های منطبق را نگه می‌دارد، LEFT JOIN همه‌ی ردیف‌های چپ را (با NULL برای سمت راستِ بی‌جفت)، FULL JOIN همه‌ی ردیف‌های هر دو طرف، و CROSS JOIN هر ردیف را با همه‌ی ردیف‌های دیگر. تا این‌جا آشناست؛ دام‌ها در جزئیات است.</p>
<h3>شرط در ON یا در WHERE؟</h3>
<pre><code class="language-sql">-- همه‌ی مشتری‌ها + سفارش‌های تأییدشده‌شان (مشتری بدون سفارش هم می‌ماند)
SELECT c.full_name, o.id
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id AND o.status = 'confirmed';

-- اشتباه رایج: همین شرط در WHERE، LEFT JOIN را عملاً INNER می‌کند
SELECT c.full_name, o.id
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
WHERE o.status = 'confirmed';</code></pre>
<h3>semi-join و anti-join</h3>
<pre><code class="language-sql">-- مشتری‌هایی که دست‌کم یک سفارش دارند (بدون تکرار ردیف)
SELECT * FROM customers c
WHERE EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id);

-- نقشه‌هایی که هیچ‌وقت سفارش نداشته‌اند
SELECT d.code, d.title FROM designs d
WHERE NOT EXISTS (SELECT 1 FROM order_items oi WHERE oi.design_code = d.code);</code></pre>
<p>برای anti-join همیشه <code>NOT EXISTS</code> بنویسید، نه <code>NOT IN</code>. اگر زیرکوئری NOT IN حتی یک NULL برگرداند، نتیجه‌ی کل شرط NULL می‌شود و <em>هیچ</em> ردیفی برنمی‌گردد.</p>
<h3>LATERAL: زیرکوئری‌ای که ردیف بیرونی را می‌بیند</h3>
<p>زیرکوئری معمولی در FROM نمی‌تواند به جدول‌های کنارش ارجاع دهد. با <strong>LATERAL</strong> می‌تواند؛ مثل یک حلقه‌ی for روی هر ردیف. کلاسیک‌ترین کاربرد: «N ردیف برتر هر گروه».</p>
<pre><code class="language-sql">-- سه سفارش آخر هر مشتری کاشانی
SELECT c.full_name, last3.id, last3.created_at
FROM customers c
CROSS JOIN LATERAL (
  SELECT o.id, o.created_at
  FROM orders o
  WHERE o.customer_id = c.id
  ORDER BY o.created_at DESC
  LIMIT 3
) AS last3
WHERE c.city = 'کاشان';

-- با LEFT JOIN LATERAL مشتری بدون سفارش هم می‌ماند
SELECT c.full_name, s.cnt, s.total
FROM customers c
LEFT JOIN LATERAL (
  SELECT count(*) AS cnt, sum(oi.line_total_rial) AS total
  FROM orders o JOIN order_items oi ON oi.order_id = o.id
  WHERE o.customer_id = c.id
) s ON true;</code></pre>
<p>با ایندکس <code>orders (customer_id, created_at DESC)</code>، کوئری اول برای هر مشتری فقط سه ورودی ایندکس می‌خواند؛ روی جدول میلیونی تفاوت ثانیه و میلی‌ثانیه است.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>در LEFT JOIN، <code>count(*)</code> مشتری بی‌سفارش را ۱ می‌شمارد؛ <code>count(o.id)</code> درست ۰ می‌دهد چون NULLها را نمی‌شمارد.</li>
<li>توابعی که مجموعه برمی‌گردانند (unnest، jsonb_array_elements، generate_series) در FROM به‌طور ضمنی LATERAL‌اند: <code>FROM products p, unnest(p.tags) AS t</code> بدون کلمه‌ی LATERAL کار می‌کند.</li>
<li>با بیش از ۸ جدول در یک کوئری، برنامه‌ریز (به خاطر <code>join_collapse_limit</code> و <code>from_collapse_limit</code>) دیگر همه‌ی ترتیب‌ها را امتحان نمی‌کند و ترتیب نوشتن شما مهم می‌شود؛ از ۱۲ جدول به بالا الگوریتم ژنتیک (GEQO) وارد می‌شود و پلن ممکن است بین اجراها فرق کند.</li>
<li><code>JOIN ... USING (customer_id)</code> ستون مشترک را یک بار در خروجی می‌آورد؛ اما NATURAL JOIN را هرگز در کد تولید استفاده نکنید: افزودن یک ستون هم‌نام (مثل created_at) بی‌صدا شرط JOIN را عوض می‌کند.</li>
<li>برای «آیا وجود دارد؟» در برنامه، <code>SELECT EXISTS (SELECT 1 FROM ...)</code> بسیار سریع‌تر از <code>count(*) &gt; 0</code> است؛ با اولین ردیف متوقف می‌شود.</li>
</ul>""",
                },
                {
                    "title": "گروه‌بندی حرفه‌ای: FILTER، ROLLUP، CUBE و GROUPING SETS",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>گزارش چندسطحی در یک کوئری</h2>
<h3>FILTER به‌جای SUM(CASE ...)</h3>
<p>گزارش رایج: برای هر شهر، تعداد کل سفارش‌ها، تحویل‌شده‌ها و لغوشده‌ها. به‌جای چند زیرکوئری یا CASEهای طولانی:</p>
<pre><code class="language-sql">SELECT c.city,
       count(*)                                           AS all_orders,
       count(*) FILTER (WHERE o.status = 'delivered')     AS delivered,
       count(*) FILTER (WHERE o.status = 'cancelled')     AS cancelled,
       round(100.0 * count(*) FILTER (WHERE o.status = 'cancelled') / count(*), 1) AS cancel_pct
FROM orders o JOIN customers c ON c.id = o.customer_id
WHERE o.created_at &gt;= timestamptz '2026-03-21 00:00+03:30'
GROUP BY c.city
HAVING count(*) &gt;= 10
ORDER BY all_orders DESC;</code></pre>
<h3>ROLLUP: جمع‌های میانی و کل</h3>
<pre><code class="language-sql">SELECT coalesce(c.city, 'جمع کل') AS city,
       coalesce(d.title, 'جمع شهر') AS design,
       sum(oi.qty) AS pieces,
       sum(oi.line_total_rial) AS revenue,
       GROUPING(c.city, d.title) AS lvl
FROM order_items oi
JOIN orders o    ON o.id = oi.order_id
JOIN customers c ON c.id = o.customer_id
JOIN designs d   ON d.code = oi.design_code
GROUP BY ROLLUP (c.city, d.title)
ORDER BY c.city NULLS LAST, lvl, revenue DESC;</code></pre>
<p><code>ROLLUP (a, b)</code> معادل سه گروه‌بندی است: (a, b)، (a) و () یعنی جمع کل. تابع <code>GROUPING()</code> یک عدد بیتی برمی‌گرداند که نشان می‌دهد کدام ستون‌ها در این ردیف «جمع زده شده‌اند»؛ به این ترتیب ردیف جمع از NULL واقعی داده قابل تشخیص است.</p>
<h3>CUBE و GROUPING SETS</h3>
<table><thead><tr><th>نحو</th><th>گروه‌بندی‌های تولیدشده</th></tr></thead><tbody>
<tr><td><code>ROLLUP (a, b, c)</code></td><td>(a,b,c)، (a,b)، (a)، ()</td></tr>
<tr><td><code>CUBE (a, b)</code></td><td>(a,b)، (a)، (b)، ()</td></tr>
<tr><td><code>GROUPING SETS ((a), (b), ())</code></td><td>دقیقاً همین سه</td></tr>
</tbody></table>
<pre><code class="language-sql">-- فروش به تفکیک شهر، به تفکیک شانه، و جمع کل؛ در یک پیمایش
SELECT c.city, d.reed, sum(oi.line_total_rial)
FROM order_items oi
JOIN orders o ON o.id = oi.order_id
JOIN customers c ON c.id = o.customer_id
JOIN designs d ON d.code = oi.design_code
GROUP BY GROUPING SETS ((c.city), (d.reed), ());</code></pre>
<h3>aggregateهای کاربردی</h3>
<pre><code class="language-sql">SELECT o.id,
       string_agg(oi.design_code, '، ' ORDER BY oi.id) AS designs,
       percentile_cont(0.5) WITHIN GROUP (ORDER BY oi.unit_price_rial) AS median_price,
       bool_and(oi.qty &gt;= 10) AS all_wholesale
FROM orders o JOIN order_items oi ON oi.order_id = o.id
GROUP BY o.id;</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>اگر بر اساس کلید اصلی گروه‌بندی کنید، می‌توانید بقیه‌ی ستون‌های همان جدول را بدون آوردن در GROUP BY انتخاب کنید (وابستگی تابعی): <code>GROUP BY c.id</code> و سپس <code>c.full_name, c.city</code> در SELECT.</li>
<li>از نسخه‌ی 16 تابع <code>any_value(col)</code> یک مقدار دلخواه از گروه برمی‌گرداند؛ جایگزین استاندارد ترفند <code>min(col)</code> وقتی همه‌ی مقادیر یکسان‌اند.</li>
<li>FILTER روی هر aggregateی کار می‌کند، نه فقط count: <code>array_agg(code) FILTER (WHERE colors &gt; 8)</code>.</li>
<li><code>count(DISTINCT x)</code> همیشه مرتب‌سازی دارد و روی میلیون‌ها ردیف کند است؛ گاهی <code>SELECT count(*) FROM (SELECT DISTINCT x ...) t</code> پلن بهتری (HashAggregate) می‌گیرد.</li>
<li>تقسیم دو عدد صحیح در درصدگیری صفر می‌دهد؛ همیشه یکی را numeric کنید (<code>100.0 *</code>) و برای جلوگیری از تقسیم بر صفر از <code>NULLIF(count(*), 0)</code> در مخرج استفاده کنید.</li>
</ul>""",
                },
                {
                    "title": "CTE، CTE بازگشتی و CTE تغییردهنده‌ی داده",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>کوئری‌های خوانا و قدرتمند با WITH</h2>
<p>CTE (Common Table Expression) یک زیرکوئری نام‌دار است که کوئری طولانی را به گام‌های خوانا می‌شکند:</p>
<pre><code class="language-sql">WITH monthly AS (
  SELECT o.customer_id, sum(oi.line_total_rial) AS revenue
  FROM orders o JOIN order_items oi ON oi.order_id = o.id
  WHERE o.created_at &gt;= timestamptz '2026-09-23 00:00+03:30'
  GROUP BY o.customer_id
), ranked AS (
  SELECT customer_id, revenue, ntile(4) OVER (ORDER BY revenue DESC) AS quartile
  FROM monthly
)
SELECT c.full_name, r.revenue
FROM ranked r JOIN customers c ON c.id = r.customer_id
WHERE r.quartile = 1;</code></pre>
<h3>MATERIALIZED یا NOT MATERIALIZED</h3>
<p>تا نسخه‌ی 11 هر CTE یک «حصار بهینه‌سازی» بود: جدا اجرا و نتیجه‌اش ذخیره می‌شد و شرط‌های بیرونی به داخلش نمی‌رفت. از نسخه‌ی 12 CTEی که یک بار ارجاع شده و عارضه‌ی جانبی ندارد، مثل زیرکوئری inline می‌شود. می‌توانید صریح تعیین کنید:</p>
<pre><code class="language-sql">WITH big AS MATERIALIZED (SELECT ...)           -- یک بار محاسبه، چند بار استفاده
WITH filtered AS NOT MATERIALIZED (SELECT ...)  -- اجازه بده شرط‌ها به داخل بروند</code></pre>
<h3>CTE بازگشتی</h3>
<p>برای داده‌ی درختی: دسته‌بندی محصولات، ساختار سازمانی یا فهرست مواد (BOM). مثال: یک فرش از نخ‌های رنگی ساخته می‌شود و هر نخ رنگی از نخ خام و رنگ:</p>
<pre><code class="language-sql">CREATE TABLE bom (parent text, child text, qty numeric, PRIMARY KEY (parent, child));
INSERT INTO bom VALUES
 ('AF-1203', 'نخ-لاکی', 4.2), ('AF-1203', 'نخ-سرمه‌ای', 3.1),
 ('نخ-لاکی', 'اکریلیک-خام', 1.02), ('نخ-لاکی', 'رنگ-قرمز', 0.05);

WITH RECURSIVE tree AS (
  SELECT child, qty, 1 AS depth, ARRAY[parent, child] AS path
  FROM bom WHERE parent = 'AF-1203'
  UNION ALL
  SELECT b.child, t.qty * b.qty, t.depth + 1, t.path || b.child
  FROM bom b JOIN tree t ON b.parent = t.child
  WHERE t.depth &lt; 10 AND NOT b.child = ANY (t.path)
)
SELECT repeat('  ', depth - 1) || child AS item, round(qty, 3) AS kg_per_m2
FROM tree ORDER BY path;</code></pre>
<p>بخش اول «لنگر» است و یک بار اجرا می‌شود؛ بخش دوم با ردیف‌های تولیدشده در دور قبل تکرار می‌شود تا وقتی ردیف جدیدی تولید نشود. شرط depth و path جلوی حلقه‌ی بی‌نهایت را در داده‌ی خراب می‌گیرد. از نسخه‌ی 14 می‌توانید به‌جای ساختن دستی path از <code>SEARCH DEPTH FIRST BY child SET ord</code> و <code>CYCLE child SET is_cycle USING path</code> استفاده کنید.</p>
<h3>CTE تغییردهنده‌ی داده</h3>
<pre><code class="language-sql">WITH closed AS (
  UPDATE orders SET status = 'delivered'
  WHERE status = 'finishing' AND id = ANY ('{501,502,503}')
  RETURNING id, customer_id
)
INSERT INTO notifications (customer_id, message)
SELECT customer_id, 'سفارش ' || id || ' تحویل شد' FROM closed;</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>همه‌ی بخش‌های یک WITH روی یک snapshot اجرا می‌شوند: اگر در یک CTE ردیفی را UPDATE کنید، CTE دیگر یا کوئری اصلی مقدار <em>قدیمی</em> جدول را می‌بیند؛ فقط از طریق RETURNING به داده‌ی جدید دسترسی دارید.</li>
<li>CTEهای شامل INSERT/UPDATE/DELETE همیشه کامل اجرا می‌شوند، حتی اگر کوئری اصلی به آن‌ها ارجاع ندهد.</li>
<li>در CTE بازگشتی، <code>UNION</code> (بدون ALL) ردیف‌های تکراری را حذف می‌کند و در گراف‌های ساده جلوی حلقه را می‌گیرد؛ اما وقتی ستون depth یا path دارید، هر ردیف یکتاست و UNION دیگر نجاتتان نمی‌دهد.</li>
<li>اگر بعد از ارتقا از نسخه‌ی 11 کوئری‌ای کند شد، احتمالاً CTE آن inline شده و برنامه‌ریز مسیر بدتری انتخاب کرده؛ <code>AS MATERIALIZED</code> رفتار قدیم را برمی‌گرداند.</li>
<li>برای پرهیز از محاسبه‌ی تکراری یک تابع گران (مثلاً فراخوانی تابع PL/pgSQL روی هر ردیف) در چند جای کوئری، آن را در یک CTE با MATERIALIZED حساب کنید؛ inline شدن می‌تواند آن را چند بار اجرا کند.</li>
</ul>""",
                },
                {
                    "title": "Window Functions کامل: رتبه، مقایسه با قبل و frame",
                    "kind": "text",
                    "minutes": 26,
                    "is_preview": False,
                    "body": r"""<h2>محاسبه روی «پنجره‌ای» از ردیف‌ها، بدون گروه‌بندی</h2>
<p>aggregate معمولی ردیف‌ها را در هم ادغام می‌کند؛ window function هر ردیف را نگه می‌دارد و کنارش مقداری محاسبه‌شده از ردیف‌های مرتبط می‌گذارد. نحو کلی: <code>func(...) OVER (PARTITION BY ... ORDER BY ... frame)</code>.</p>
<h3>رتبه‌بندی</h3>
<pre><code class="language-sql">SELECT d.reed, d.code, s.pieces,
       row_number() OVER w AS rn,      -- 1,2,3,4
       rank()       OVER w AS rnk,     -- 1,2,2,4
       dense_rank() OVER w AS drnk     -- 1,2,2,3
FROM designs d
JOIN (SELECT design_code, sum(qty) AS pieces FROM order_items GROUP BY 1) s
  ON s.design_code = d.code
WINDOW w AS (PARTITION BY d.reed ORDER BY s.pieces DESC);</code></pre>
<p>برای «سه نقشه‌ی پرفروش هر شانه» نمی‌توانید window function را در WHERE بگذارید (WHERE قبل از آن اجرا می‌شود)؛ یک لایه زیرکوئری لازم است: <code>SELECT * FROM (...) t WHERE rn &lt;= 3</code>. از نسخه‌ی 15 پستگرس این الگو را تشخیص می‌دهد و محاسبه‌ی row_number هر partition را بعد از رسیدن به ۳ متوقف می‌کند.</p>
<h3>مقایسه با ردیف قبل: LAG و LEAD</h3>
<pre><code class="language-sql">WITH m AS (
  SELECT date_trunc('month', o.created_at AT TIME ZONE 'Asia/Tehran') AS month,
         sum(oi.line_total_rial) AS revenue
  FROM orders o JOIN order_items oi ON oi.order_id = o.id
  GROUP BY 1
)
SELECT month, revenue,
       lag(revenue) OVER (ORDER BY month) AS prev,
       round(100.0 * (revenue - lag(revenue) OVER (ORDER BY month))
             / NULLIF(lag(revenue) OVER (ORDER BY month), 0), 1) AS growth_pct,
       sum(revenue) OVER (ORDER BY month) AS running_total,
       avg(revenue) OVER (ORDER BY month ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS avg_3m
FROM m ORDER BY month;</code></pre>
<h3>frame: کدام ردیف‌ها در پنجره‌اند</h3>
<table><thead><tr><th>frame</th><th>معنا</th></tr></thead><tbody>
<tr><td><code>ROWS BETWEEN 6 PRECEDING AND CURRENT ROW</code></td><td>دقیقاً ۷ ردیف فیزیکی (میانگین متحرک ۷روزه اگر هر روز یک ردیف باشد)</td></tr>
<tr><td><code>RANGE BETWEEN interval '7 days' PRECEDING AND CURRENT ROW</code></td><td>ردیف‌هایی که مقدار ORDER BY آن‌ها تا ۷ روز قبل است، حتی اگر روزهایی بی‌داده باشند</td></tr>
<tr><td><code>GROUPS BETWEEN 1 PRECEDING AND CURRENT ROW</code></td><td>گروه هم‌مقدار فعلی و گروه قبلی</td></tr>
<tr><td><code>ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING</code></td><td>کل partition</td></tr>
</tbody></table>
<p>frame پیش‌فرض وقتی ORDER BY دارید <code>RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW</code> است. کلمه‌ی RANGE یعنی ردیف‌های <em>هم‌مقدار</em> (peers) با ردیف فعلی هم داخل پنجره‌اند.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>جمع تجمعی با frame پیش‌فرض برای ردیف‌های هم‌تاریخ یک عدد تکراری نشان می‌دهد (چون همه‌ی peerها با هم جمع می‌شوند)؛ برای جمع ردیف‌به‌ردیف <code>ROWS</code> بنویسید یا id را به ORDER BY اضافه کنید.</li>
<li><code>last_value(x) OVER (ORDER BY ...)</code> تقریباً همیشه خود ردیف فعلی را برمی‌گرداند، چون frame پیش‌فرض به CURRENT ROW ختم می‌شود؛ frame را تا <code>UNBOUNDED FOLLOWING</code> باز کنید.</li>
<li>aggregate پنجره‌ای FILTER هم می‌پذیرد: <code>count(*) FILTER (WHERE status = 'cancelled') OVER (PARTITION BY customer_id)</code>.</li>
<li>عبارت <code>EXCLUDE CURRENT ROW</code> در frame، ردیف فعلی را از محاسبه کنار می‌گذارد؛ برای «میانگین همکاران به‌جز خودم» در مقایسه‌ی بافنده‌ها بی‌نظیر است.</li>
<li>توابع پنجره‌ای که تعریف OVER یکسان دارند با یک مرتب‌سازی محاسبه می‌شوند؛ هر تعریف متفاوت یک Sort جدا می‌خواهد. با بند <code>WINDOW</code> تعریف‌ها را یکسان و خوانا نگه دارید.</li>
</ul>""",
                },
                {
                    "title": "jsonb و آرایه در کوئری: عملگرها، jsonpath و توابع",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>کار با داده‌ی نیمه‌ساخت‌یافته</h2>
<h3>عملگرهای jsonb</h3>
<table><thead><tr><th>عملگر</th><th>کار</th><th>مثال</th></tr></thead><tbody>
<tr><td><code>-&gt;</code></td><td>عنصر به‌صورت jsonb</td><td><code>specs -&gt; 'reed'</code></td></tr>
<tr><td><code>-&gt;&gt;</code></td><td>عنصر به‌صورت text</td><td><code>specs -&gt;&gt; 'yarn'</code></td></tr>
<tr><td><code>#&gt;&gt;</code></td><td>مسیر تو در تو به‌صورت text</td><td><code>data #&gt;&gt; '{buyer,city}'</code></td></tr>
<tr><td><code>@&gt;</code></td><td>شامل بودن (قابل ایندکس با GIN)</td><td><code>specs @&gt; '{"yarn":"اکریلیک"}'</code></td></tr>
<tr><td><code>?</code> / <code>?|</code> / <code>?&amp;</code></td><td>وجود کلید / یکی از کلیدها / همه‌ی کلیدها</td><td><code>specs ? 'density'</code></td></tr>
<tr><td><code>||</code> / <code>-</code> / <code>#-</code></td><td>ادغام / حذف کلید / حذف مسیر</td><td><code>specs || '{"shine":true}'</code></td></tr>
</tbody></table>
<pre><code class="language-sql">SELECT title,
       (specs -&gt;&gt; 'reed')::int AS reed,
       specs['yarn'] AS yarn_json          -- subscripting از نسخه‌ی 14
FROM products
WHERE specs @&gt; '{"yarn": "اکریلیک"}'
  AND (specs -&gt;&gt; 'density')::int &gt;= 3000;

UPDATE products
SET specs = jsonb_set(specs, '{finish}', '"براق"', true)
WHERE id = 1;</code></pre>
<h3>باز کردن jsonb به ردیف</h3>
<p>عیوب کنترل کیفیت را به‌صورت <code>{"رج_کشی": 2, "پرز_دهی": 1}</code> ذخیره کرده‌ایم. مجموع هر نوع عیب در ماه:</p>
<pre><code class="language-sql">SELECT e.key AS defect, sum(e.value::int) AS total
FROM qc_inspections q
CROSS JOIN LATERAL jsonb_each_text(q.defects) AS e(key, value)
WHERE q.inspected_at &gt;= timestamptz '2026-09-23 00:00+03:30'
GROUP BY e.key ORDER BY total DESC;

-- ساختن JSON برای API در خود دیتابیس
SELECT jsonb_build_object('order', o.id,
         'items', jsonb_agg(jsonb_build_object('design', oi.design_code, 'qty', oi.qty) ORDER BY oi.id))
FROM orders o JOIN order_items oi ON oi.order_id = o.id
WHERE o.id = 501 GROUP BY o.id;</code></pre>
<h3>jsonpath</h3>
<pre><code class="language-sql">-- بازرسی‌هایی که دست‌کم یک عیب با تعداد بیش از ۲ دارند
SELECT id FROM qc_inspections WHERE defects @? '$.* ? (@ &gt; 2)';
SELECT id, jsonb_path_query(defects, '$.keyvalue() ? (@.value &gt;= 2).key') FROM qc_inspections;</code></pre>
<p>نسخه‌ی 17 توابع استاندارد SQL/JSON را کامل کرده است: <code>JSON_VALUE</code>، <code>JSON_QUERY</code>، <code>JSON_EXISTS</code> و <code>JSON_TABLE</code> که یک سند را مستقیم به جدول ستون‌دار تبدیل می‌کند.</p>
<h3>توابع آرایه</h3>
<pre><code class="language-sql">SELECT code, t.tag, t.pos
FROM designs, unnest(tags) WITH ORDINALITY AS t(tag, pos);

SELECT array_agg(DISTINCT city ORDER BY city) FROM customers;
SELECT string_to_array('لاکی،سرمه‌ای،کرم', '،');
UPDATE designs SET tags = array_remove(tags, 'قدیمی') WHERE 'قدیمی' = ANY (tags);
SELECT code FROM designs WHERE tags &amp;&amp; ARRAY['کلاسیک', 'افشان'];   -- دست‌کم یک برچسب مشترک</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>specs -&gt;&gt; 'reed' = '1200'</code> مقایسه‌ی متنی است؛ برای مقایسه‌ی عددی cast کنید. اما <code>@&gt; '{"reed":1200}'</code> نوع JSON را رعایت می‌کند و با GIN ایندکس می‌شود؛ هرجا ممکن است از @&gt; استفاده کنید.</li>
<li><code>jsonb_set</code> اگر مقدار جدید NULL (SQL) باشد کل نتیجه را NULL می‌کند و ستون پاک می‌شود! از <code>jsonb_set_lax</code> یا <code>coalesce(to_jsonb(x), 'null')</code> استفاده کنید.</li>
<li>subscripting در UPDATE هم کار می‌کند: <code>UPDATE products SET specs['yarn'] = '"پشم"'</code> و مسیرهای میانی ناموجود را خودش می‌سازد.</li>
<li><code>jsonb_strip_nulls</code> کلیدهای با مقدار null را حذف می‌کند؛ قبل از ذخیره‌ی پاسخ‌های حجیم درگاه‌ها حجم را محسوس کم می‌کند.</li>
<li>عملگر <code>@&gt;</code> روی آرایه‌ی jsonb هم کار می‌کند: <code>'["a","b","c"]'::jsonb @&gt; '["b"]'</code>؛ برای برچسب‌های داخل jsonb نیازی به unnest نیست.</li>
</ul>""",
                },
                {
                    "title": "View و Materialized View با REFRESH CONCURRENTLY",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>کوئری نام‌دار و کوئری ذخیره‌شده</h2>
<h3>View</h3>
<p>view یک کوئری ذخیره‌شده است که مثل جدول صدا زده می‌شود. داده‌ای نگه نمی‌دارد و هر بار اجرا می‌شود؛ برنامه‌ریز کوئری view را در کوئری شما ادغام می‌کند، پس معمولاً هزینه‌ی اضافه ندارد.</p>
<pre><code class="language-sql">CREATE VIEW report.order_summary AS
SELECT o.id, o.status, o.created_at, c.full_name, c.city,
       sum(oi.line_total_rial) AS total_rial,
       sum(oi.qty) AS pieces
FROM factory.orders o
JOIN factory.customers c ON c.id = o.customer_id
JOIN factory.order_items oi ON oi.order_id = o.id
GROUP BY o.id, c.id;

GRANT SELECT ON report.order_summary TO bi_reader;</code></pre>
<p>کاربر bi_reader حتی بدون دسترسی به جدول‌های factory می‌تواند view را بخواند، چون view به‌طور پیش‌فرض با مجوز <em>صاحبش</em> به جدول‌ها دسترسی می‌گیرد. اگر می‌خواهید مجوز و RLS کاربر خواننده بررسی شود، از نسخه‌ی 15 <code>WITH (security_invoker = true)</code> بگذارید.</p>
<h3>view قابل به‌روزرسانی</h3>
<p>viewی که فقط از یک جدول، بدون GROUP BY و DISTINCT و aggregate ساخته شده باشد، خودبه‌خود INSERT و UPDATE و DELETE می‌پذیرد. <code>WITH CHECK OPTION</code> جلوی نوشتن ردیفی را می‌گیرد که از دید view خارج شود:</p>
<pre><code class="language-sql">CREATE VIEW factory.kashan_customers AS
SELECT * FROM factory.customers WHERE city = 'کاشان'
WITH CHECK OPTION;
-- INSERT با city = 'تهران' از طریق این view خطا می‌دهد</code></pre>
<h3>Materialized View</h3>
<p>materialized view نتیجه را واقعاً روی دیسک ذخیره می‌کند؛ مناسب داشبوردی که کوئری سنگینش لازم نیست هر لحظه تازه باشد.</p>
<pre><code class="language-sql">CREATE MATERIALIZED VIEW report.daily_sales AS
SELECT (o.created_at AT TIME ZONE 'Asia/Tehran')::date AS day,
       oi.design_code,
       sum(oi.qty) AS pieces,
       sum(oi.line_total_rial) AS revenue
FROM factory.orders o JOIN factory.order_items oi ON oi.order_id = o.id
WHERE o.status &lt;&gt; 'cancelled'
GROUP BY 1, 2
WITH DATA;

CREATE UNIQUE INDEX ON report.daily_sales (day, design_code);

REFRESH MATERIALIZED VIEW CONCURRENTLY report.daily_sales;</code></pre>
<p>REFRESH معمولی قفل انحصاری می‌گیرد و در تمام مدت، خواندن از view مسدود است. نسخه‌ی <strong>CONCURRENTLY</strong> نتیجه‌ی جدید را جدا می‌سازد و فقط تفاوت‌ها را اعمال می‌کند؛ خواننده‌ها معطل نمی‌شوند. شرطش یک ایندکس UNIQUE روی ستون‌های ساده (بدون WHERE) است.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>SELECT *</code> در تعریف view هنگام ساخت به فهرست ثابت ستون‌ها تبدیل می‌شود؛ ستونی که بعداً به جدول اضافه کنید در view ظاهر نمی‌شود.</li>
<li>تا وقتی viewی به یک ستون وابسته است، <code>ALTER COLUMN ... TYPE</code> روی آن ستون خطا می‌دهد؛ باید view را DROP، ستون را تغییر و view را دوباره بسازید (همه داخل یک تراکنش).</li>
<li><code>CREATE OR REPLACE VIEW</code> فقط اجازه‌ی افزودن ستون در انتها را می‌دهد؛ تغییر نام یا نوع یا ترتیب ستون‌ها نیازمند DROP است.</li>
<li>materialized view خودکار تازه نمی‌شود. زمان‌بندی را با cron سیستم یا اکستنشن <code>pg_cron</code> انجام دهید: <code>SELECT cron.schedule('*/10 * * * *', 'REFRESH MATERIALIZED VIEW CONCURRENTLY report.daily_sales')</code>.</li>
<li>REFRESH CONCURRENTLY وقتی بخش بزرگی از داده عوض شده باشد از REFRESH معمولی کندتر است و bloat تولید می‌کند؛ برای نتیجه‌های کوچکی که کل‌شان عوض می‌شود، REFRESH ساده در ساعت کم‌بار بهتر است.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۵ ─────────────────────────────
        {
            "title": "فصل ۵: ایندکس و کارایی",
            "lessons": [
                {
                    "title": "B-tree از درون: ترتیب ستون‌ها، INCLUDE، partial و expression index",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>ایندکس یعنی یک ساختار دوم که باید نگهداری شود</h2>
<p>ایندکس پیش‌فرض پستگرس <strong>B-tree</strong> است: درختی مرتب از مقدارها که هر برگش به ctid (آدرس فیزیکی ردیف در heap) اشاره می‌کند. هر ایندکس خواندن را سریع و هر INSERT و UPDATE را کمی کندتر می‌کند و فضای دیسک و حافظه‌ی cache می‌گیرد؛ پس سؤال درست «کدام کوئری به این ایندکس نیاز دارد؟» است، نه «کدام ستون را ایندکس کنم؟».</p>
<h3>ترتیب ستون‌ها در ایندکس ترکیبی</h3>
<p>ایندکس <code>(customer_id, created_at)</code> مثل دفتر تلفنی است که اول بر اساس نام خانوادگی و بعد نام مرتب شده: برای «سفارش‌های مشتری ۴۲» و «سفارش‌های مشتری ۴۲ در اسفند» عالی است، اما برای «همه‌ی سفارش‌های اسفند» تقریباً بی‌فایده. قاعده‌ی عملی: ستون‌هایی که با تساوی فیلتر می‌شوند اول، ستون بازه یا مرتب‌سازی آخر.</p>
<pre><code class="language-sql">-- سه سفارش آخر هر مشتری: یک Index Scan بدون Sort
CREATE INDEX orders_cust_created_idx ON factory.orders (customer_id, created_at DESC);

SELECT id, status, created_at
FROM factory.orders
WHERE customer_id = 42
ORDER BY created_at DESC
LIMIT 3;</code></pre>
<h3>Index Only Scan و INCLUDE</h3>
<p>اگر همه‌ی ستون‌های لازم داخل ایندکس باشند، پستگرس می‌تواند اصلاً سراغ جدول نرود (<strong>Index Only Scan</strong>)، به شرطی که صفحه‌های جدول در visibility map «همه‌قابل‌مشاهده» علامت خورده باشند؛ کاری که VACUUM انجام می‌دهد. با <code>INCLUDE</code> ستون‌هایی را به برگ‌ها اضافه می‌کنید که در جست‌وجو نقشی ندارند و فقط برای خواندن آن‌جا هستند:</p>
<pre><code class="language-sql">CREATE INDEX order_items_order_cover ON factory.order_items (order_id)
  INCLUDE (qty, line_total_rial);

-- جمع هر سفارش بدون خواندن heap
SELECT sum(qty), sum(line_total_rial) FROM factory.order_items WHERE order_id = 1001;

-- در ایندکس UNIQUE، یکتایی فقط روی ستون‌های کلید است، نه ستون‌های INCLUDE
CREATE UNIQUE INDEX looms_code_cover ON factory.looms (code) INCLUDE (hall);</code></pre>
<h3>partial index: فقط ردیف‌هایی که مهم‌اند</h3>
<p>در کارخانه، ۹۵ درصد سفارش‌ها delivered هستند و صفحه‌ی «کارهای باز» فقط بقیه را می‌خواهد. ایندکس جزئی کوچک‌تر، سریع‌تر و ارزان‌تر در نگهداری است:</p>
<pre><code class="language-sql">CREATE INDEX orders_open_idx ON factory.orders (due_date)
WHERE status IN ('confirmed', 'weaving', 'finishing');

-- یکتایی شرطی: هر مشتری فقط یک سفارش draft
CREATE UNIQUE INDEX one_draft_per_customer ON factory.orders (customer_id)
WHERE status = 'draft';</code></pre>
<p>برنامه‌ریز فقط وقتی از این ایندکس استفاده می‌کند که بتواند <em>اثبات</em> کند شرط کوئری زیرمجموعه‌ی شرط ایندکس است؛ <code>WHERE status = 'weaving'</code> کار می‌کند، اما اگر status را به صورت پارامتر بفرستید (‎$1) و پلن عمومی (generic plan) ساخته شود، ممکن است ایندکس کنار گذاشته شود.</p>
<h3>expression index</h3>
<pre><code class="language-sql">CREATE INDEX customers_lower_name_idx ON factory.customers (lower(full_name));
CREATE INDEX orders_day_idx ON factory.orders (((created_at AT TIME ZONE 'Asia/Tehran')::date));

SELECT * FROM factory.customers WHERE lower(full_name) = lower('Reza Kashani');</code></pre>
<p>شرط کوئری باید <em>دقیقاً</em> همان عبارت ایندکس باشد و تابع باید IMMUTABLE باشد؛ به همین دلیل <code>created_at::date</code> روی timestamptz قابل ایندکس نیست (به منطقه‌ی زمانی نشست وابسته است) اما نسخه‌ی AT TIME ZONE با منطقه‌ی ثابت هست.</p>
<h3>Hash</h3>
<p>ایندکس Hash فقط تساوی را پشتیبانی می‌کند و از نسخه‌ی 10 امن (WAL-logged) است. برای ستون‌های متنی بلند مثل توکن یا URL که فقط با = جست‌وجو می‌شوند گاهی کوچک‌تر از B-tree است، اما UNIQUE و مرتب‌سازی ندارد؛ در عمل B-tree انتخاب پیش‌فرض می‌ماند.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>از نسخه‌ی 13، B-tree مقدارهای تکراری را deduplicate می‌کند؛ ایندکس روی ستون کم‌تنوعی مثل status چند برابر کوچک‌تر از نسخه‌های قدیمی است، اما هنوز معمولاً partial index انتخاب بهتری است.</li>
<li>B-tree در هر دو جهت پیمایش می‌شود؛ <code>DESC</code> در ایندکس تک‌ستونی بی‌اثر است و فقط در ایندکس چندستونی با جهت‌های مختلط (مثل <code>a ASC, b DESC</code>) معنا دارد.</li>
<li>از نسخه‌ی 18، «skip scan» اجازه می‌دهد ایندکس <code>(status, created_at)</code> برای شرطی فقط روی created_at هم استفاده شود؛ در 16 و 17 هنوز باید ترتیب ستون‌ها را درست بچینید.</li>
<li>نمای <code>pg_stat_user_indexes</code> با <code>idx_scan = 0</code> ایندکس‌های بی‌استفاده را نشان می‌دهد؛ قبل از حذف، مطمئن شوید آمار از ماه‌ها پیش reset نشده و ایندکس پشتیبان UNIQUE یا PK نیست.</li>
<li>ایندکس روی <code>(a)</code> وقتی <code>(a, b)</code> وجود دارد معمولاً زائد است؛ این ایندکس‌های تکراری را با مقایسه‌ی <code>indkey</code> در <code>pg_index</code> پیدا کنید.</li>
</ul>""",
                },
                {
                    "title": "GIN، GiST و BRIN: ایندکس مناسب برای jsonb، آرایه، بازه و جدول‌های عظیم",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>وقتی B-tree جواب نمی‌دهد</h2>
<p>B-tree برای مقایسه‌ی مقدارهای مرتب‌شدنی (=، &lt;، BETWEEN، ORDER BY) ساخته شده است. اما «کدام نقشه‌ها برچسب ابریشمی دارند؟»، «کدام بازرسی‌ها عیب رج‌کشی دارند؟» یا «کدام رزروها با این بازه هم‌پوشانی دارند؟» سؤال مرتب‌سازی نیستند؛ برای آن‌ها پستگرس ایندکس‌های دیگری دارد.</p>
<table>
<thead><tr><th>نوع</th><th>مناسب برای</th><th>عملگرهای نمونه</th></tr></thead>
<tbody>
<tr><td>B-tree</td><td>تساوی، بازه، مرتب‌سازی، UNIQUE</td><td>= &lt; &gt; BETWEEN LIKE 'abc%'</td></tr>
<tr><td>GIN</td><td>مقدارهای «چندعضوی»: jsonb، آرایه، tsvector، trigram</td><td>@&gt; ? &amp;&amp; @@</td></tr>
<tr><td>GiST</td><td>بازه، هندسه، نزدیک‌ترین همسایه، EXCLUDE</td><td>&amp;&amp; @&gt; &lt;-&gt;</td></tr>
<tr><td>BRIN</td><td>جدول بسیار بزرگ که ترتیب فیزیکی‌اش با ستون هم‌بسته است</td><td>= &lt; &gt; روی زمان یا شناسه‌ی صعودی</td></tr>
<tr><td>Hash</td><td>فقط تساوی</td><td>=</td></tr>
</tbody>
</table>
<h3>GIN برای jsonb و آرایه</h3>
<p>GIN یک «ایندکس معکوس» است: برای هر کلید یا عضو، فهرست ردیف‌هایی که آن را دارند. مثل فهرست موضوعی انتهای کتاب.</p>
<pre><code class="language-sql">-- آرایه‌ی برچسب نقشه‌ها
CREATE INDEX designs_tags_gin ON factory.designs USING gin (tags);
SELECT code FROM factory.designs WHERE tags @&gt; ARRAY['ابریشم'];
SELECT code FROM factory.designs WHERE tags &amp;&amp; ARRAY['کلاسیک', 'افشان'];

-- jsonb عیوب کنترل کیفیت؛ jsonb_path_ops کوچک‌تر و سریع‌تر برای @&gt;
CREATE INDEX qc_defects_gin ON factory.qc_inspections USING gin (defects jsonb_path_ops);
SELECT id FROM factory.qc_inspections WHERE defects @&gt; '{"رج_کشی": 2}';</code></pre>
<p>کلاس پیش‌فرض <code>jsonb_ops</code> عملگرهای وجود کلید (<code>?</code>، <code>?|</code>، <code>?&amp;</code>) را هم پشتیبانی می‌کند؛ <code>jsonb_path_ops</code> فقط <code>@&gt;</code> و jsonpath (<code>@?</code>، <code>@@</code>) را، اما معمولاً دو تا سه برابر کوچک‌تر است. نکته‌ی مهم: <code>defects-&gt;&gt;'رج_کشی' = '2'</code> از ایندکس GIN استفاده <em>نمی‌کند</em>؛ یا کوئری را با <code>@&gt;</code> بنویسید یا یک expression index از نوع B-tree روی همان عبارت بسازید.</p>
<h3>GiST برای بازه و نزدیکی</h3>
<pre><code class="language-sql">CREATE INDEX runs_during_gist ON factory.production_runs USING gist (during);
SELECT loom_id FROM factory.production_runs
WHERE during &amp;&amp; tstzrange('2026-03-01 08:00+03:30', '2026-03-01 16:00+03:30');</code></pre>
<p>قید EXCLUDE فصل ۳ هم پشت صحنه همین ایندکس GiST را می‌سازد. GiST «زیان‌ده» است: ممکن است ردیف‌های نامربوط را هم پیشنهاد دهد و پستگرس آن‌ها را دوباره بررسی (recheck) می‌کند.</p>
<h3>BRIN برای جدول‌های لاگ</h3>
<p>جدول قرائت حسگرهای دستگاه بافندگی روزی میلیون‌ها ردیف می‌گیرد و ردیف‌ها به ترتیب زمان اضافه می‌شوند. BRIN برای هر گروه صفحه (پیش‌فرض ۱۲۸ صفحه) فقط کمینه و بیشینه را نگه می‌دارد؛ ایندکسی چند کیلوبایتی برای جدول چند ده گیگابایتی:</p>
<pre><code class="language-sql">CREATE INDEX sensor_ts_brin ON factory.loom_sensor_log USING brin (recorded_at)
WITH (pages_per_range = 64);</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>GIN درج‌ها را ابتدا در یک «pending list» جمع می‌کند (<code>fastupdate</code>)؛ اگر یک INSERT گاهی بی‌دلیل کند است، احتمالاً نوبت تخلیه‌ی همین فهرست به آن افتاده. <code>gin_pending_list_limit</code> را کم کنید یا fastupdate را خاموش کنید.</li>
<li>همبستگی ترتیب فیزیکی را در <code>pg_stats.correlation</code> ببینید؛ BRIN فقط وقتی مفید است که این عدد نزدیک 1 یا ‎-1 باشد. UPDATEهای پراکنده و حذف‌های قدیمی این همبستگی را خراب می‌کنند.</li>
<li>کلاس <code>brin minmax_multi_ops</code> (نسخه‌ی 14 به بعد) چند بازه برای هر گروه نگه می‌دارد و با داده‌ای که کمی نامرتب است بهتر کنار می‌آید.</li>
<li>برای ایندکس ترکیبی از ستون عادی و jsonb در یک GIN، اکستنشن <code>btree_gin</code> لازم است؛ مثل btree_gist برای GiST.</li>
<li>GiST از جست‌وجوی «K نزدیک‌ترین» پشتیبانی می‌کند: <code>ORDER BY location &lt;-&gt; point(51.43, 33.98) LIMIT 5</code> بدون محاسبه‌ی فاصله برای همه‌ی ردیف‌ها.</li>
</ul>""",
                },
                {
                    "title": "خواندن EXPLAIN (ANALYZE, BUFFERS) خط‌به‌خط",
                    "kind": "text",
                    "minutes": 26,
                    "is_preview": False,
                    "body": r"""<h2>پلن اجرا، داستان کوئری است</h2>
<p><code>EXPLAIN</code> پلنی را نشان می‌دهد که برنامه‌ریز <em>انتخاب کرده</em> با تخمین‌هایش؛ <code>EXPLAIN ANALYZE</code> کوئری را واقعاً اجرا می‌کند و عددهای واقعی را کنار تخمین می‌گذارد؛ <code>BUFFERS</code> می‌گوید چند صفحه از cache و چند صفحه از دیسک خوانده شده. همیشه این سه را با هم بخواهید.</p>
<pre><code class="language-sql">EXPLAIN (ANALYZE, BUFFERS, SETTINGS)
SELECT c.full_name, sum(oi.line_total_rial) AS total
FROM factory.orders o
JOIN factory.customers c ON c.id = o.customer_id
JOIN factory.order_items oi ON oi.order_id = o.id
WHERE o.created_at &gt;= '2026-03-21' AND o.status = 'delivered'
GROUP BY c.full_name
ORDER BY total DESC
LIMIT 10;</code></pre>
<pre><code class="language-text">Limit  (cost=4210.55..4210.58 rows=10 width=40) (actual time=38.112..38.115 rows=10 loops=1)
  Buffers: shared hit=2950 read=412
  -&gt;  Sort  (cost=4210.55..4212.80 rows=900 width=40) (actual time=38.110..38.112 rows=10 loops=1)
        Sort Key: (sum(oi.line_total_rial)) DESC
        Sort Method: top-N heapsort  Memory: 26kB
        -&gt;  HashAggregate  (... rows=900 ...) (actual ... rows=870 loops=1)
              -&gt;  Hash Join  (... rows=5200 ...) (actual ... rows=61340 loops=1)
                    Hash Cond: (oi.order_id = o.id)
                    -&gt;  Seq Scan on order_items oi  (... rows=480000 ...) (actual ... rows=480000 loops=1)
                    -&gt;  Hash  (... rows=1300 ...) (actual ... rows=15335 loops=1)
                          -&gt;  Index Scan using orders_status_created_at_idx on orders o ...
                                Index Cond: ((status = 'delivered') AND (created_at &gt;= ...))
Planning Time: 0.9 ms
Execution Time: 38.4 ms</code></pre>
<h3>چگونه بخوانیم</h3>
<ol>
<li><strong>از داخلی‌ترین گره به بیرون</strong> بخوانید؛ گره‌های تورفته‌تر زودتر اجرا می‌شوند و خروجی‌شان به والد می‌رود.</li>
<li><strong>cost</strong> دو عدد دارد: هزینه‌ی شروع (تا اولین ردیف) و هزینه‌ی کل. واحدش دلخواه است (یک صفحه‌ی ترتیبی = 1)، نه میلی‌ثانیه.</li>
<li><strong>rows تخمینی را با actual rows مقایسه کنید.</strong> در مثال بالا تخمین Hash Join پنج هزار و واقعیت شصت هزار است؛ ده برابر خطا. ریشه‌ی بیشتر پلن‌های بد همین‌جاست: آمار کهنه یا همبستگی بین ستون‌ها که برنامه‌ریز نمی‌داند.</li>
<li><strong>loops</strong> را ضرب کنید: actual time و rows برای <em>هر بار</em> اجرای گره‌اند. Index Scan با ‎time=0.05 و loops=200000 یعنی ده ثانیه.</li>
<li><strong>Buffers</strong>: hit یعنی از shared_buffers، read یعنی از سیستم‌عامل یا دیسک. هر صفحه 8KB است؛ read=412 حدود 3.3MB خواندن است.</li>
</ol>
<h3>علامت‌های خطر</h3>
<table>
<thead><tr><th>آنچه می‌بینید</th><th>معنی</th><th>اقدام</th></tr></thead>
<tbody>
<tr><td>Rows Removed by Filter بزرگ</td><td>ردیف‌های زیادی خوانده و دور ریخته شده</td><td>ایندکس یا partial index مناسب</td></tr>
<tr><td>Sort Method: external merge Disk</td><td>work_mem کافی نبوده</td><td>افزایش work_mem برای همان نشست یا ایندکس برای ORDER BY</td></tr>
<tr><td>Nested Loop با loops عظیم</td><td>تخمین سطر داخلی خیلی کم بوده</td><td>ANALYZE، CREATE STATISTICS</td></tr>
<tr><td>Heap Fetches بالا در Index Only Scan</td><td>visibility map به‌روز نیست</td><td>VACUUM</td></tr>
<tr><td>Batches بیش از 1 در Hash</td><td>جدول hash روی دیسک ریخته</td><td>work_mem یا hash_mem_multiplier</td></tr>
</tbody>
</table>
<p>برای DML از ANALYZE با احتیاط استفاده کنید؛ <code>EXPLAIN ANALYZE DELETE</code> واقعاً حذف می‌کند. آن را داخل <code>BEGIN; ... ROLLBACK;</code> بگذارید.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>گزینه‌ی <code>SETTINGS</code> پارامترهای غیرپیش‌فرضی را که روی پلن اثر گذاشته‌اند فهرست می‌کند؛ وقتی پلن روی لپ‌تاپ و سرور فرق دارد، اول همین را مقایسه کنید.</li>
<li>در نسخه‌ی 18، BUFFERS همراه ANALYZE به‌طور پیش‌فرض نمایش داده می‌شود؛ در 16 و 17 باید صریحاً بنویسید.</li>
<li>اکستنشن <code>auto_explain</code> پلن کوئری‌های کندتر از یک آستانه را خودکار در لاگ می‌نویسد؛ تنها راه دیدن پلن کوئری‌ای که فقط در ساعت شلوغی کند است.</li>
<li>زمان‌سنجی ANALYZE خودش سربار دارد (به‌ویژه روی ماشین مجازی با ساعت کند)؛ <code>EXPLAIN (ANALYZE, TIMING OFF)</code> فقط rows واقعی را می‌دهد و نزدیک‌تر به زمان واقعی اجراست.</li>
<li>عبارت «never executed» یعنی آن شاخه اصلاً اجرا نشده (مثلاً چون طرف دیگر Join خالی بود)؛ این گره را در تحلیل زمان نادیده بگیرید.</li>
</ul>""",
                },
                {
                    "title": "آمار، ANALYZE، pg_stat_statements و ساخت ایندکس بدون توقف",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>برنامه‌ریز به اندازه‌ی آمارش باهوش است</h2>
<p>برنامه‌ریز برای هر ستون یک خلاصه نگه می‌دارد: درصد NULL، تعداد مقدارهای متمایز، پرتکرارترین مقدارها (MCV) و هیستوگرام توزیع. این آمار را <code>ANALYZE</code> با نمونه‌گیری (۳۰۰ برابر default_statistics_target ردیف، یعنی ۳۰ هزار ردیف) می‌سازد و autovacuum وقتی حدود ده درصد جدول تغییر کرد، خودکار اجرایش می‌کند.</p>
<pre><code class="language-sql">SELECT attname, null_frac, n_distinct, most_common_vals, correlation
FROM pg_stats
WHERE schemaname = 'factory' AND tablename = 'orders';

SELECT relname, last_analyze, last_autoanalyze, n_mod_since_analyze
FROM pg_stat_user_tables ORDER BY n_mod_since_analyze DESC LIMIT 10;</code></pre>
<h3>وقتی آمار کافی نیست</h3>
<p>برنامه‌ریز فرض می‌کند ستون‌ها مستقل‌اند. فرض کنید جدول مشتری ستون province هم دارد؛ شهر «کاشان» و استان «اصفهان» کاملاً وابسته‌اند؛ برنامه‌ریز احتمال دو شرط را ضرب می‌کند و تعداد ردیف را خیلی کم تخمین می‌زند. آمار چندستونی این را درست می‌کند:</p>
<pre><code class="language-sql">CREATE STATISTICS customers_city_prov (dependencies, ndistinct, mcv)
  ON city, province FROM factory.customers;
ANALYZE factory.customers;

-- ستون با توزیع نامتقارن: نمونه‌ی بزرگ‌تر
ALTER TABLE factory.order_items ALTER COLUMN design_code SET STATISTICS 1000;
ANALYZE factory.order_items;</code></pre>
<h3>pg_stat_statements: کدام کوئری واقعاً گران است؟</h3>
<p>کندترین کوئری لزوماً مشکل اصلی نیست؛ کوئری ۵ میلی‌ثانیه‌ای که روزی دو میلیون بار اجرا می‌شود، از گزارش ماهانه‌ی ۲۰ ثانیه‌ای سنگین‌تر است. pg_stat_statements همه‌ی کوئری‌ها را با پارامترهای نرمال‌شده جمع می‌زند:</p>
<pre><code class="language-ini"># postgresql.conf (نیاز به restart)
shared_preload_libraries = 'pg_stat_statements'
pg_stat_statements.track = top
compute_query_id = on</code></pre>
<pre><code class="language-sql">CREATE EXTENSION pg_stat_statements;

SELECT round(total_exec_time) AS total_ms,
       calls,
       round(mean_exec_time::numeric, 2) AS mean_ms,
       rows,
       round(100.0 * shared_blks_hit / nullif(shared_blks_hit + shared_blks_read, 0), 1) AS hit_pct,
       left(query, 80) AS query
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 15;

SELECT pg_stat_statements_reset();  -- شروع یک دوره‌ی اندازه‌گیری تازه</code></pre>
<h3>CREATE INDEX CONCURRENTLY</h3>
<p>CREATE INDEX معمولی تا پایان ساخت، نوشتن در جدول را قفل می‌کند؛ روی جدول ده میلیونی یعنی چند دقیقه توقف ثبت سفارش. نسخه‌ی CONCURRENTLY جدول را دو بار پیمایش می‌کند و منتظر تمام تراکنش‌های قدیمی می‌ماند، اما نوشتن را متوقف نمی‌کند:</p>
<pre><code class="language-sql">CREATE INDEX CONCURRENTLY orders_due_idx ON factory.orders (due_date);

-- اگر وسط کار خطا داد، ایندکس INVALID باقی می‌ماند
SELECT indexrelid::regclass FROM pg_index WHERE NOT indisvalid;
DROP INDEX CONCURRENTLY orders_due_idx;

-- بازسازی ایندکس پف‌کرده بدون توقف (نسخه‌ی 12 به بعد)
REINDEX INDEX CONCURRENTLY factory.orders_status_created_at_idx;</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>CREATE INDEX CONCURRENTLY داخل بلوک تراکنش اجرا نمی‌شود؛ در جنگو از عملیات <code>AddIndexConcurrently</code> (در django.contrib.postgres.operations) استفاده کنید و در کلاس Migration مقدار <code>atomic = False</code> بگذارید.</li>
<li>یک تراکنش طولانی یا idle in transaction، CONCURRENTLY را تا ابد منتظر نگه می‌دارد؛ پیشرفت را در <code>pg_stat_progress_create_index</code> ببینید.</li>
<li>autovacuum جدول‌های موقت (TEMP) و جدول والد partition‌شده را ANALYZE نمی‌کند؛ بعد از پر کردن جدول موقت بزرگ، خودتان ANALYZE بزنید.</li>
<li>بعد از بارگذاری انبوه داده (مثلاً ورود اطلاعات یک سال از اکسل)، ANALYZE دستی بزنید؛ تا autovacuum برسد، کوئری‌های گزارش با پلن غلط اجرا می‌شوند.</li>
<li><code>maintenance_work_mem</code> بزرگ‌تر (مثلاً 1GB فقط برای همان نشست با SET) ساخت ایندکس روی جدول بزرگ را چند برابر سریع‌تر می‌کند.</li>
</ul>""",
                },
                {
                    "title": "جست‌وجوی فارسی: full-text با simple، نرمال‌سازی و pg_trgm",
                    "kind": "text",
                    "minutes": 26,
                    "is_preview": False,
                    "body": r"""<h2>جست‌وجویی که «كاشان» عربی و «کاشان» فارسی را یکی بداند</h2>
<p>پستگرس برای انگلیسی و چند زبان اروپایی دیکشنری ریشه‌یاب (stemmer) دارد، اما برای فارسی نه. با این حال با پیکربندی <strong>simple</strong> (فقط شکستن به کلمه و کوچک‌کردن حروف لاتین) به‌علاوه‌ی یک تابع نرمال‌سازی، جست‌وجوی کلمه‌ای خوب و سریعی برای فارسی می‌سازید.</p>
<h3>گام ۱: تابع نرمال‌سازی</h3>
<pre><code class="language-sql">CREATE OR REPLACE FUNCTION factory.fa_normalize(t text)
RETURNS text
LANGUAGE sql IMMUTABLE PARALLEL SAFE STRICT
AS $$
  SELECT regexp_replace(
           translate(t,
             'يكىۀة۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩' || chr(8204),
             'یکیهه01234567890123456789 '),
           '[ً-ْ]', '', 'g')          -- حذف اعراب
$$;

SELECT factory.fa_normalize('فرش‌هاي كاشان ۱۲۰۰ شانه');  -- فرش های کاشان 1200 شانه</code></pre>
<p>«ي» و «ك» عربی، ارقام فارسی و عربی، نیم‌فاصله (U+200C که با <code>chr(8204)</code> ساخته‌ایم) و اعراب یکسان می‌شوند. نیم‌فاصله به فاصله تبدیل می‌شود تا «فرش‌ها» و «فرش ها» یکی شوند. مهم این است که <em>همین تابع</em> هم روی داده و هم روی عبارت جست‌وجو اعمال شود.</p>
<h3>گام ۲: ستون tsvector و ایندکس GIN</h3>
<p>تابع <code>array_to_string</code> در کاتالوگ STABLE علامت خورده (چون برای نوع‌های دیگر به تنظیمات نشست وابسته است) و ستون generated فقط تابع IMMUTABLE می‌پذیرد؛ برای آرایه‌ی text یک پوشش IMMUTABLE کوچک می‌سازیم:</p>
<pre><code class="language-sql">CREATE FUNCTION factory.tags_text(text[]) RETURNS text
LANGUAGE sql IMMUTABLE PARALLEL SAFE AS $$ SELECT array_to_string($1, ' ') $$;

ALTER TABLE factory.designs
  ADD COLUMN search tsvector GENERATED ALWAYS AS (
    setweight(to_tsvector('simple', factory.fa_normalize(coalesce(title, ''))), 'A') ||
    setweight(to_tsvector('simple', factory.fa_normalize(factory.tags_text(tags))), 'B')
  ) STORED;

CREATE INDEX designs_search_gin ON factory.designs USING gin (search);

SELECT code, title, ts_rank(search, q) AS rank
FROM factory.designs,
     websearch_to_tsquery('simple', factory.fa_normalize('افشان -ابریشم')) AS q
WHERE search @@ q
ORDER BY rank DESC
LIMIT 20;</code></pre>
<p><code>websearch_to_tsquery</code> نحو آشنای موتورهای جست‌وجو را می‌فهمد: عبارت داخل گیومه، OR و منفی با «-»، و هیچ‌وقت به خاطر ورودی کاربر خطای نحوی نمی‌دهد. برای جست‌وجوی پیشوندی (تکمیل خودکار) از <code>to_tsquery('simple', 'کاش:*')</code> استفاده کنید.</p>
<h3>گام ۳: pg_trgm برای LIKE '%...%' و غلط تایپی</h3>
<p>full-text کلمه‌ی کامل می‌خواهد؛ اما کاربر «شانه۱۲» یا بخشی از کد نقشه را تایپ می‌کند. <code>LIKE '%...%'</code> هیچ B-treeی را استفاده نمی‌کند، مگر ایندکس trigram (سه‌حرفی):</p>
<pre><code class="language-sql">CREATE EXTENSION IF NOT EXISTS pg_trgm;

CREATE INDEX customers_name_trgm ON factory.customers
  USING gin (factory.fa_normalize(full_name) gin_trgm_ops);

-- بخشی از نام، با ایندکس
SELECT id, full_name FROM factory.customers
WHERE factory.fa_normalize(full_name) LIKE '%' || factory.fa_normalize('رضای') || '%';

-- جست‌وجوی تقریبی: «محمدرضا کاشانی» با غلط تایپی
SELECT full_name, similarity(factory.fa_normalize(full_name), 'محمد رضا کاشانی') AS sim
FROM factory.customers
WHERE factory.fa_normalize(full_name) % 'محمد رضا کاشانی'
ORDER BY sim DESC LIMIT 5;</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>قبل از هر چیز <code>SELECT show_trgm('فرش');</code> را اجرا کنید. اگر آرایه‌ی خالی برگشت، LC_CTYPE دیتابیس C است و pg_trgm حروف فارسی را «حرف» به حساب نمی‌آورد؛ دیتابیس را با locale UTF-8 واقعی (مثل en_US.UTF-8 یا ICU) بسازید.</li>
<li>آستانه‌ی عملگر <code>%</code> پیش‌فرض 0.3 است و با <code>SET pg_trgm.similarity_threshold = 0.45</code> برای همان نشست تنظیم می‌شود؛ برای نام‌های کوتاه فارسی 0.3 نتایج پرتی زیادی می‌آورد.</li>
<li>عبارت جست‌وجوی کمتر از سه حرف (مثلاً «رض») در ایندکس trigram عملاً همه‌ی ردیف‌ها را کاندید می‌کند؛ در رابط کاربری حداقل سه حرف بخواهید.</li>
<li>تابع نرمال‌سازی را اگر بعداً تغییر دهید، ستون generated و ایندکس‌ها خودکار بازسازی نمی‌شوند؛ چون آن را IMMUTABLE اعلام کرده‌اید، پستگرس فرض می‌کند خروجی‌اش هرگز عوض نمی‌شود. بعد از تغییر، ستون را دوباره بسازید و REINDEX کنید.</li>
<li>برای رتبه‌بندی، <code>ts_rank_cd</code> نزدیکی کلمه‌ها به هم را هم در نظر می‌گیرد؛ «فرش کاشان» کنار هم بالاتر از دو کلمه‌ی دور از هم می‌نشیند.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۶ ─────────────────────────────
        {
            "title": "فصل ۶: تراکنش، MVCC و نگهداری",
            "lessons": [
                {
                    "title": "MVCC، tuple مرده و VACUUM: چرا جدول پف می‌کند",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>پستگرس هیچ ردیفی را درجا عوض نمی‌کند</h2>
<p>در پستگرس، UPDATE یعنی «نسخه‌ی قدیمی را منقضی کن و نسخه‌ی جدیدی بنویس» و DELETE یعنی «نسخه را منقضی کن». به این مدل <strong>MVCC</strong> (کنترل همروندی چندنسخه‌ای) می‌گویند. هر نسخه (tuple) دو برچسب پنهان دارد: <code>xmin</code> شماره‌ی تراکنشی که آن را ساخته و <code>xmax</code> شماره‌ی تراکنشی که منقضی‌اش کرده. هر تراکنش با یک snapshot تصمیم می‌گیرد کدام نسخه‌ها را ببیند. نتیجه‌ی شیرین: خواننده هرگز نویسنده را معطل نمی‌کند و برعکس.</p>
<pre><code class="language-sql">CREATE TABLE demo (id int PRIMARY KEY, qty int);
INSERT INTO demo VALUES (1, 10);
SELECT ctid, xmin, xmax, * FROM demo;   -- (0,1) | 812 | 0 | 1 | 10
UPDATE demo SET qty = 9 WHERE id = 1;
SELECT ctid, xmin, xmax, * FROM demo;   -- (0,2) | 813 | 0 | 1 | 9
-- نسخه‌ی (0,1) هنوز روی دیسک است: یک tuple مرده</code></pre>
<p>هزینه‌ی این مدل: نسخه‌های مرده تا وقتی کسی پاکشان نکند فضا می‌گیرند. جدول انبار نخ که روزی صدها هزار بار موجودی‌اش UPDATE می‌شود، بدون نگهداری چند برابر حجم واقعی‌اش می‌شود؛ این همان <strong>bloat</strong> است.</p>
<h3>VACUUM و autovacuum</h3>
<p><code>VACUUM</code> نسخه‌هایی را که دیگر هیچ تراکنشی نمی‌بیند، علامت «قابل استفاده‌ی مجدد» می‌زند، visibility map را به‌روز می‌کند (برای Index Only Scan) و ورودی‌های ایندکس متناظر را پاک می‌کند. فایل را کوچک نمی‌کند؛ فقط فضای خالی را برای درج‌های بعدی آماده می‌کند. <code>VACUUM FULL</code> جدول را از نو می‌نویسد و کوچک می‌کند، اما در تمام مدت قفل ACCESS EXCLUSIVE دارد: نه خواندن، نه نوشتن.</p>
<p>autovacuum وقتی سراغ جدول می‌رود که تعداد tuple مرده از <code>50 + 0.2 × تعداد ردیف‌ها</code> بیشتر شود. برای جدول ۵۰ میلیونی یعنی ده میلیون ردیف مرده؛ خیلی دیر. برای جدول‌های بزرگ و پرتغییر، تنظیم جدول‌به‌جدول بدهید:</p>
<pre><code class="language-sql">ALTER TABLE factory.yarn_stock SET (
  autovacuum_vacuum_scale_factor = 0.01,
  autovacuum_vacuum_threshold    = 1000,
  autovacuum_analyze_scale_factor = 0.02
);

-- وضعیت tupleهای مرده و آخرین vacuum
SELECT relname, n_live_tup, n_dead_tup,
       round(100.0 * n_dead_tup / nullif(n_live_tup + n_dead_tup, 0), 1) AS dead_pct,
       last_autovacuum, autovacuum_count
FROM pg_stat_user_tables
ORDER BY n_dead_tup DESC LIMIT 10;</code></pre>
<h3>HOT و fillfactor</h3>
<p>اگر UPDATE هیچ ستون ایندکس‌شده‌ای را تغییر ندهد و در همان صفحه جای خالی باشد، پستگرس نسخه‌ی جدید را در همان صفحه می‌نویسد و ایندکس‌ها را دست نمی‌زند (<strong>HOT update</strong>). برای جدول‌هایی که مدام UPDATE می‌شوند، fillfactor کمتر از ۱۰۰ جا برای HOT می‌گذارد:</p>
<pre><code class="language-sql">ALTER TABLE factory.yarn_stock SET (fillfactor = 80);
SELECT relname, n_tup_upd, n_tup_hot_upd FROM pg_stat_user_tables WHERE relname = 'yarn_stock';</code></pre>
<h3>اندازه‌گیری bloat</h3>
<pre><code class="language-sql">CREATE EXTENSION IF NOT EXISTS pgstattuple;
SELECT table_len, tuple_percent, dead_tuple_percent, free_percent
FROM pgstattuple('factory.yarn_stock');</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>افزودن یک ایندکس روی ستونی که مدام UPDATE می‌شود (مثل updated_at) همه‌ی HOT updateهای جدول را از بین می‌برد؛ گاهی حذف همین یک ایندکس bloat را حل می‌کند.</li>
<li>برای کوچک کردن جدول پف‌کرده بدون قفل طولانی، اکستنشن <code>pg_repack</code> همان کار VACUUM FULL را با قفل لحظه‌ای انجام می‌دهد.</li>
<li>VACUUM فقط صفحه‌های خالیِ <em>انتهای</em> فایل را به سیستم‌عامل برمی‌گرداند؛ فضای خالی وسط فایل فقط برای درج‌های بعدی همان جدول قابل استفاده است.</li>
<li>از نسخه‌ی 13، autovacuum با درج‌های زیاد هم فعال می‌شود (<code>autovacuum_vacuum_insert_threshold</code>)؛ جدول‌های فقط‌درج (لاگ) هم visibility map به‌روز می‌گیرند.</li>
<li>هر <code>ROLLBACK</code> هم tuple مرده تولید می‌کند؛ برنامه‌ای که هزاران INSERT را به خاطر خطا rollback می‌کند، بی‌صدا bloat می‌سازد.</li>
</ul>""",
                },
                {
                    "title": "wraparound، تراکنش‌های رهاشده و timeoutها",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>بمب ساعتیِ شماره‌ی تراکنش</h2>
<p>شماره‌ی تراکنش (xid) در پستگرس ۳۲ بیتی است: حدود چهار میلیارد مقدار که به صورت دایره‌ای استفاده می‌شود؛ هر تراکنش دو میلیارد شماره‌ی قبل از خودش را «گذشته» و دو میلیارد بعد را «آینده» می‌بیند. اگر ردیفی خیلی قدیمی شود و فکری به حالش نشود، ناگهان «در آینده» قرار می‌گیرد و نامرئی می‌شود. برای جلوگیری، VACUUM ردیف‌های قدیمی را <strong>freeze</strong> می‌کند: علامتی که می‌گوید «این ردیف برای همه قابل مشاهده است، شماره‌اش را نادیده بگیر».</p>
<p>اگر freeze عقب بیفتد، پستگرس ابتدا در لاگ هشدار می‌دهد و وقتی فقط چند میلیون شماره باقی مانده باشد، برای حفاظت از داده <strong>دیگر هیچ تراکنش نوشتنی را نمی‌پذیرد</strong>. این یکی از معدود حالت‌هایی است که دیتابیس سالم عملاً از کار می‌افتد.</p>
<pre><code class="language-sql">-- چقدر به مرز نزدیکیم؟ (حدود 2.1 میلیارد مرز است)
SELECT datname, age(datfrozenxid) AS xid_age,
       round(100.0 * age(datfrozenxid) / 2147483647, 1) AS pct
FROM pg_database ORDER BY 2 DESC;

SELECT c.oid::regclass AS table_name, age(c.relfrozenxid) AS xid_age,
       pg_size_pretty(pg_total_relation_size(c.oid)) AS size
FROM pg_class c
WHERE c.relkind IN ('r', 'm', 't')
ORDER BY age(c.relfrozenxid) DESC LIMIT 10;</code></pre>
<p>autovacuum وقتی سن جدول از <code>autovacuum_freeze_max_age</code> (پیش‌فرض ۲۰۰ میلیون) بگذرد، حتی اگر autovacuum خاموش باشد، یک vacuum «to prevent wraparound» اجرا می‌کند. در pg_stat_activity آن را با همین عبارت می‌بینید؛ <em>آن را kill نکنید</em>، دوباره شروع می‌شود و کار از اول.</p>
<h3>چه چیزی جلوی VACUUM را می‌گیرد؟</h3>
<p>VACUUM فقط نسخه‌هایی را پاک یا freeze می‌کند که از قدیمی‌ترین snapshot فعال در کل کلاستر قدیمی‌تر باشند. یک چیز کهنه کافی است تا همه‌چیز گیر کند:</p>
<table>
<thead><tr><th>عامل</th><th>کجا ببینیم</th></tr></thead>
<tbody>
<tr><td>تراکنش طولانی یا «idle in transaction»</td><td>pg_stat_activity، ستون‌های xact_start و backend_xmin</td></tr>
<tr><td>replication slot رهاشده</td><td>pg_replication_slots، ستون‌های active و xmin</td></tr>
<tr><td>prepared transaction فراموش‌شده</td><td>pg_prepared_xacts</td></tr>
<tr><td>standby با hot_standby_feedback = on و کوئری طولانی</td><td>pg_stat_replication، ستون backend_xmin</td></tr>
</tbody>
</table>
<pre><code class="language-sql">SELECT pid, usename, application_name, state,
       now() - xact_start AS xact_age, backend_xmin, left(query, 60) AS last_query
FROM pg_stat_activity
WHERE xact_start IS NOT NULL
ORDER BY xact_start LIMIT 10;

SELECT pg_terminate_backend(12345);   -- با احتیاط، پس از بررسی</code></pre>
<p>«idle in transaction» یعنی برنامه BEGIN زده، کاری کرده و بعد مشغول چیز دیگری شده (مثلاً منتظر پاسخ یک وب‌سرویس پرداخت یا کاربر). این اتصال قفل‌هایش را نگه می‌دارد و جلوی VACUUM کل کلاستر را می‌گیرد.</p>
<h3>timeoutها: کمربند ایمنی</h3>
<pre><code class="language-sql">ALTER ROLE app_user SET idle_in_transaction_session_timeout = '60s';
ALTER ROLE app_user SET statement_timeout = '30s';
ALTER ROLE report_user SET statement_timeout = '10min';
ALTER ROLE app_user SET lock_timeout = '5s';
-- نسخه‌ی 17 به بعد: سقف عمر کل تراکنش
ALTER ROLE app_user SET transaction_timeout = '2min';</code></pre>
<p>تنظیم روی role بهتر از تنظیم سراسری است: گزارش‌گیر شبانه و pg_dump نباید با timeout سی‌ثانیه‌ای برنامه قطع شوند.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>از نسخه‌ی 14، وقتی سن جدول به <code>vacuum_failsafe_age</code> (۱.۶ میلیارد) برسد، VACUUM حالت اضطراری می‌گیرد: محدودیت سرعت (cost delay) و پاک‌سازی ایندکس را رها می‌کند تا فقط freeze را زودتر تمام کند.</li>
<li>جدول‌های TEMP هرگز توسط autovacuum پردازش نمی‌شوند؛ نشستی که روزها باز است و جدول موقت بزرگی دارد، می‌تواند در سن xid سهم داشته باشد.</li>
<li><code>idle_session_timeout</code> (نسخه‌ی 14) اتصال‌های بی‌کار را می‌بندد؛ آن را پشت PgBouncer یا pool جنگو فعال نکنید، چون pool از بسته شدن بی‌خبر است و با خطای «connection closed» روبه‌رو می‌شود.</li>
<li>statement_timeout را سراسری در <code>postgresql.conf</code> نگذارید: روی migrationها، <code>CREATE INDEX</code> دستی و اسکریپت‌های نگهداری هم اثر می‌کند. autovacuum و pg_dump خودشان آن را صفر می‌کنند، اما ابزارهای دستی شما نه.</li>
<li><code>SET LOCAL statement_timeout = '2s'</code> فقط تا پایان همان تراکنش اعتبار دارد؛ راهی امن برای محدود کردن یک کوئری خاص در برنامه بدون اثر روی بقیه‌ی اتصال‌ها.</li>
</ul>""",
                },
                {
                    "title": "سطوح ایزوله‌سازی، lost update و retry در SERIALIZABLE",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>دو کاربر، یک موجودی</h2>
<p>دو فروشنده هم‌زمان آخرین تخته‌ی فرش ۱۲۰۰ شانه‌ی نقشه‌ی افشان را می‌فروشند. هر دو موجودی را ۱ می‌خوانند، هر دو ۱ کم می‌کنند و ذخیره می‌کنند. نتیجه: موجودی صفر و دو سفارش برای یک فرش. این <strong>lost update</strong> است و سطح ایزوله‌سازی پیش‌فرض پستگرس جلویش را نمی‌گیرد.</p>
<table>
<thead><tr><th>سطح</th><th>snapshot</th><th>رفتار</th></tr></thead>
<tbody>
<tr><td>Read Committed (پیش‌فرض)</td><td>برای هر دستور تازه</td><td>هر SELECT آخرین داده‌ی commit‌شده را می‌بیند؛ دو SELECT در یک تراکنش می‌توانند نتیجه‌ی متفاوت بدهند</td></tr>
<tr><td>Repeatable Read</td><td>یک بار برای کل تراکنش</td><td>دیدِ ثابت؛ اگر ردیفی را که دیگری تغییر داده UPDATE کنید، خطای serialization می‌گیرید</td></tr>
<tr><td>Serializable</td><td>مثل RR + ردیابی وابستگی‌ها</td><td>نتیجه هم‌ارز اجرای پشت‌سرهم است؛ در صورت تعارض یکی از تراکنش‌ها خطا می‌گیرد</td></tr>
</tbody>
</table>
<p>Read Uncommitted در پستگرس وجود ندارد و همان Read Committed رفتار می‌کند؛ dirty read هرگز اتفاق نمی‌افتد.</p>
<h3>سه راه درمان lost update</h3>
<pre><code class="language-sql">-- ۱) UPDATE اتمی: شرط را در خود UPDATE بگذارید (ساده‌ترین و بهترین)
UPDATE factory.stock
SET qty = qty - 1
WHERE design_code = 'AF-1203' AND reed = 1200 AND qty &gt;= 1
RETURNING qty;
-- اگر صفر ردیف برگشت، موجودی کافی نبوده

-- ۲) قفل بدبینانه: ردیف را برای خواندن-و-نوشتن قفل کنید
BEGIN;
SELECT qty FROM factory.stock
WHERE design_code = 'AF-1203' AND reed = 1200
FOR UPDATE;
-- منطق برنامه ...
UPDATE factory.stock SET qty = qty - 1 WHERE design_code = 'AF-1203' AND reed = 1200;
COMMIT;

-- ۳) SERIALIZABLE و تکرار در صورت شکست
BEGIN ISOLATION LEVEL SERIALIZABLE;
-- خواندن‌ها و نوشتن‌های پیچیده
COMMIT;</code></pre>
<h3>retry: بخش اجباری SERIALIZABLE</h3>
<p>در Repeatable Read و Serializable، خطای <code>could not serialize access</code> با SQLSTATE <strong>40001</strong> بخشی از کار عادی است، نه باگ. برنامه باید <em>کل تراکنش</em> را از اول تکرار کند، نه فقط دستور آخر را:</p>
<pre><code class="language-python">import time
import psycopg
from psycopg import errors

def run_serializable(conn, work, attempts=5):
    for i in range(attempts):
        try:
            with conn.transaction():
                conn.execute("SET TRANSACTION ISOLATION LEVEL SERIALIZABLE")
                return work(conn)
        except (errors.SerializationFailure, errors.DeadlockDetected):
            time.sleep(0.05 * 2 ** i)   # backoff نمایی
    raise RuntimeError("تراکنش پس از چند تلاش موفق نشد")</code></pre>
<p>تابع <code>work</code> نباید اثر جانبی بیرون از دیتابیس داشته باشد (ارسال پیامک، فراخوانی درگاه پرداخت)؛ چون ممکن است چند بار اجرا شود. اثرهای بیرونی را بعد از COMMIT موفق انجام دهید.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>در Read Committed، اگر UPDATE به ردیفی برسد که تراکنش دیگری در حال تغییرش است، منتظر می‌ماند و بعد شرط WHERE را روی <em>نسخه‌ی جدید</em> دوباره ارزیابی می‌کند؛ به همین دلیل روش ۱ بدون هیچ قفل صریحی درست کار می‌کند.</li>
<li>SERIALIZABLE فقط بین تراکنش‌هایی که همه SERIALIZABLE هستند تضمین می‌دهد؛ یک تراکنش Read Committed هم‌زمان می‌تواند ناهنجاری بسازد. یا همه، یا هیچ.</li>
<li><code>SET TRANSACTION</code> باید اولین دستور تراکنش باشد؛ بعد از اولین SELECT خطا می‌دهد. برای کل نشست از <code>SET default_transaction_isolation</code> استفاده کنید.</li>
<li>تراکنش‌های فقط‌خواندنی SERIALIZABLE با <code>READ ONLY DEFERRABLE</code> منتظر یک snapshot امن می‌مانند و هرگز خطای 40001 نمی‌گیرند؛ مناسب گزارش‌های طولانی مالی.</li>
<li>در Serializable، ایندکس مناسب نرخ خطاهای کاذب را کم می‌کند؛ بدون ایندکس، پستگرس قفل‌های پیش‌بینی (SIRead) را در سطح کل جدول می‌گیرد و تعارض‌های بی‌دلیل زیاد می‌شود.</li>
</ul>""",
                },
                {
                    "title": "قفل‌ها، deadlock، صف با SKIP LOCKED و advisory lock",
                    "kind": "text",
                    "minutes": 26,
                    "is_preview": False,
                    "body": r"""<h2>چه کسی منتظر چه کسی است؟</h2>
<p>پستگرس دو دسته قفل دارد: <strong>قفل جدول</strong> (هشت حالت، از ACCESS SHARE که هر SELECT می‌گیرد تا ACCESS EXCLUSIVE که DROP و بیشتر ALTER TABLEها می‌گیرند) و <strong>قفل ردیف</strong> (FOR UPDATE، FOR NO KEY UPDATE، FOR SHARE، FOR KEY SHARE). قفل‌های ردیف روی خود tuple نوشته می‌شوند، نه در حافظه؛ برای همین قفل کردن میلیون‌ها ردیف حافظه‌ی مشترک را پر نمی‌کند.</p>
<h3>پیدا کردن زنجیره‌ی انتظار</h3>
<pre><code class="language-sql">SELECT a.pid,
       pg_blocking_pids(a.pid) AS blocked_by,
       a.wait_event_type, a.state,
       now() - a.query_start AS waiting,
       left(a.query, 70) AS query
FROM pg_stat_activity a
WHERE cardinality(pg_blocking_pids(a.pid)) &gt; 0;

-- جزئیات قفل‌ها
SELECT l.pid, l.locktype, l.relation::regclass, l.mode, l.granted
FROM pg_locks l
WHERE NOT l.granted OR l.relation = 'factory.orders'::regclass;</code></pre>
<h3>صف قفل: چرا یک ALTER ساده سایت را می‌خواباند</h3>
<p>فرض کنید یک گزارش ۵ دقیقه‌ای روی orders در حال اجراست (ACCESS SHARE). شما <code>ALTER TABLE orders ADD COLUMN note text</code> می‌زنید که ACCESS EXCLUSIVE می‌خواهد و منتظر می‌ماند. حالا <em>هر</em> SELECT تازه پشت ALTER شما در صف می‌ایستد، چون قفل‌ها به ترتیب صف داده می‌شوند. نتیجه: ۵ دقیقه هیچ صفحه‌ای باز نمی‌شود. درمان: در migrationها همیشه lock_timeout کوتاه بگذارید و در صورت شکست دوباره تلاش کنید.</p>
<pre><code class="language-sql">SET lock_timeout = '3s';
ALTER TABLE factory.orders ADD COLUMN note text;</code></pre>
<h3>deadlock</h3>
<p>تراکنش A ردیف ۱ را قفل کرده و ردیف ۲ را می‌خواهد؛ B ردیف ۲ را دارد و ردیف ۱ را می‌خواهد. پستگرس پس از <code>deadlock_timeout</code> (پیش‌فرض ۱ ثانیه) چرخه را پیدا می‌کند و یکی را با خطای <code>deadlock detected</code> (SQLSTATE 40P01) قربانی می‌کند. راه پیشگیری: ردیف‌ها را همیشه به یک ترتیب ثابت قفل کنید.</p>
<pre><code class="language-sql">-- انتقال نخ بین دو انبار: همیشه به ترتیب id قفل کنید
SELECT id FROM factory.yarn_stock WHERE id IN (7, 3) ORDER BY id FOR UPDATE;</code></pre>
<h3>صف کار با FOR UPDATE SKIP LOCKED</h3>
<p>برای صف کارهای پس‌زمینه (ساخت PDF فاکتور، ارسال پیامک) لازم نیست Redis یا RabbitMQ بیاورید. با SKIP LOCKED هر worker ردیفی برمی‌دارد که دیگری قفل نکرده، بی‌آن‌که منتظر بماند:</p>
<pre><code class="language-sql">CREATE TABLE factory.jobs (
  id         bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  kind       text NOT NULL,
  payload    jsonb NOT NULL,
  status     text NOT NULL DEFAULT 'pending',
  attempts   int NOT NULL DEFAULT 0,
  run_after  timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX jobs_pending_idx ON factory.jobs (run_after) WHERE status = 'pending';

-- هر worker در یک تراکنش:
WITH next AS (
  SELECT id FROM factory.jobs
  WHERE status = 'pending' AND run_after &lt;= now()
  ORDER BY run_after
  LIMIT 1
  FOR UPDATE SKIP LOCKED
)
UPDATE factory.jobs j
SET status = 'running', attempts = attempts + 1
FROM next WHERE j.id = next.id
RETURNING j.id, j.kind, j.payload;</code></pre>
<h3>advisory lock: قفل روی یک مفهوم</h3>
<p>گاهی می‌خواهید چیزی را قفل کنید که ردیف نیست؛ مثلاً «فقط یک نمونه از اسکریپت محاسبه‌ی حقوق ماهانه اجرا شود».</p>
<pre><code class="language-sql">SELECT pg_try_advisory_lock(hashtext('payroll-1405-01'));      -- true یا false، بدون انتظار
-- ... کار ...
SELECT pg_advisory_unlock(hashtext('payroll-1405-01'));

-- نسخه‌ی تراکنشی: با COMMIT یا ROLLBACK خودکار آزاد می‌شود
SELECT pg_advisory_xact_lock(42, 1001);</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>INSERT در جدول فرزند روی ردیف والد قفل FOR KEY SHARE می‌گیرد؛ به همین دلیل UPDATE ستون‌های غیرکلیدی والد (که FOR NO KEY UPDATE می‌گیرد) با آن تداخل ندارد، اما UPDATE کلید اصلی والد دارد.</li>
<li>advisory lock سطح نشست با PgBouncer در حالت transaction pooling خطرناک است: قفل روی اتصال سرور می‌ماند و ممکن است به کلاینت دیگری برسد؛ آن‌جا فقط <code>pg_advisory_xact_lock</code> استفاده کنید.</li>
<li><code>log_lock_waits = on</code> هر انتظار قفل طولانی‌تر از deadlock_timeout را با pid طرفین لاگ می‌کند؛ بهترین ابزار برای پیدا کردن قفل‌هایی که فقط گاهی پیش می‌آیند.</li>
<li>در صف SKIP LOCKED، کار رهاشده (worker که وسط کار مرد) با ROLLBACK خودکار دوباره pending می‌شود، به شرطی که status را در همان تراکنشی که کار را انجام می‌دهید عوض کرده باشید.</li>
<li><code>NOWAIT</code> به‌جای SKIP LOCKED بلافاصله خطا می‌دهد؛ برای رابط کاربری («این سفارش را کاربر دیگری در حال ویرایش است») مناسب‌تر از انتظار است.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۷ ─────────────────────────────
        {
            "title": "فصل ۷: مدیریت، امنیت و دسترس‌پذیری",
            "lessons": [
                {
                    "title": "role، GRANT و DEFAULT PRIVILEGES؛ اتصال امن با scram-sha-256 و SSL",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>کمترین دسترسی لازم، نه superuser برای همه</h2>
<p>رایج‌ترین پیکربندی ناامن در پروژه‌های ایرانی این است که برنامه با کاربر postgres وصل می‌شود. یک SQL injection کافی است تا مهاجم با <code>COPY ... TO PROGRAM</code> روی خود سرور فرمان اجرا کند. الگوی درست سه لایه دارد: <strong>مالک</strong> (owner) که جدول‌ها را می‌سازد و فقط migration با آن اجرا می‌شود، <strong>نقش‌های گروهی</strong> بدون LOGIN که مجموعه‌ی دسترسی‌اند، و <strong>کاربرهای ورود</strong> که عضو گروه‌ها هستند.</p>
<pre><code class="language-sql">CREATE ROLE carpet_owner NOLOGIN;
CREATE ROLE carpet_rw    NOLOGIN;
CREATE ROLE carpet_ro    NOLOGIN;

CREATE ROLE migrator   LOGIN PASSWORD 'رمز-قوی-۱' IN ROLE carpet_owner;
CREATE ROLE app_user   LOGIN PASSWORD 'رمز-قوی-۲' IN ROLE carpet_rw;
CREATE ROLE bi_reader  LOGIN PASSWORD 'رمز-قوی-۳' IN ROLE carpet_ro CONNECTION LIMIT 5;

REVOKE ALL ON DATABASE carpet FROM PUBLIC;
GRANT CONNECT ON DATABASE carpet TO carpet_rw, carpet_ro;
ALTER SCHEMA factory OWNER TO carpet_owner;

GRANT USAGE ON SCHEMA factory TO carpet_rw, carpet_ro;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA factory TO carpet_rw;
GRANT SELECT ON ALL TABLES IN SCHEMA factory TO carpet_ro;
GRANT USAGE ON ALL SEQUENCES IN SCHEMA factory TO carpet_rw;</code></pre>
<h3>DEFAULT PRIVILEGES: برای جدول‌هایی که فردا ساخته می‌شوند</h3>
<p><code>GRANT ... ON ALL TABLES</code> فقط جدول‌های <em>موجود</em> را می‌گیرد. migration هفته‌ی بعد جدول تازه‌ای می‌سازد و برنامه با «permission denied» از کار می‌افتد. DEFAULT PRIVILEGES این را حل می‌کند، اما فقط برای اشیایی که <strong>همان role مشخص‌شده</strong> می‌سازد:</p>
<pre><code class="language-sql">ALTER DEFAULT PRIVILEGES FOR ROLE carpet_owner IN SCHEMA factory
  GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO carpet_rw;
ALTER DEFAULT PRIVILEGES FOR ROLE carpet_owner IN SCHEMA factory
  GRANT SELECT ON TABLES TO carpet_ro;
ALTER DEFAULT PRIVILEGES FOR ROLE carpet_owner IN SCHEMA factory
  GRANT USAGE ON SEQUENCES TO carpet_rw;

-- migration باید با همین نقش جدول بسازد
SET ROLE carpet_owner;</code></pre>
<p>با <code>\ddp</code> در psql پیش‌فرض‌ها را ببینید و با <code>\dp factory.*</code> دسترسی واقعی هر جدول را.</p>
<h3>scram-sha-256 و SSL</h3>
<p>روش احراز هویت در pg_hba را در فصل ۱ دیدیم. برای اتصال از شبکه دو چیز دیگر لازم است: رمز با هش scram (نه md5) و رمزنگاری کانال با SSL، به‌خصوص وقتی برنامه و دیتابیس در دو دیتاسنتر جدا هستند.</p>
<pre><code class="language-bash">sudo -u postgres psql -c "SELECT rolname FROM pg_authid WHERE rolpassword LIKE 'md5%';"
# این roleها باید رمزشان دوباره تنظیم شود

# گواهی خودامضا برای شبکه‌ی داخلی (برای اینترنت از CA معتبر استفاده کنید)
cd /etc/postgresql/16/main
sudo openssl req -new -x509 -days 825 -nodes -subj "/CN=db.carpet.local" \
  -keyout server.key -out server.crt
sudo chown postgres:postgres server.key server.crt
sudo chmod 600 server.key
# سپس در postgresql.conf مسیر ssl_cert_file و ssl_key_file را به این دو فایل بدهید و reload کنید</code></pre>
<pre><code class="language-sql">SELECT pid, ssl, version, cipher FROM pg_stat_ssl JOIN pg_stat_activity USING (pid)
WHERE usename = 'app_user';</code></pre>
<p>سمت کلاینت <code>sslmode=verify-full</code> هم کانال را رمز می‌کند و هم هویت سرور را بررسی می‌کند؛ <code>require</code> رمز می‌کند اما جلوی سرور جعلی را نمی‌گیرد.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>ستون‌های identity برای INSERT به مجوز USAGE روی sequence نیاز ندارند؛ اما serial قدیمی دارد. خطای «permission denied for sequence» تقریباً همیشه از جدول‌های serial است.</li>
<li>نقش‌های آماده‌ی <code>pg_read_all_data</code> و <code>pg_write_all_data</code> (نسخه‌ی 14) و <code>pg_monitor</code> برای گزارش‌گیر و مانیتورینگ، نیاز به GRANT تک‌تک را از بین می‌برند. نسخه‌ی 17 مجوز <code>MAINTAIN</code> و نقش <code>pg_maintain</code> را اضافه کرد تا VACUUM و REINDEX بدون مالکیت ممکن شود.</li>
<li><code>ALTER ROLE app_user SET search_path = factory</code> باعث می‌شود برنامه بدون پیشوند schema کار کند، بی‌آن‌که search_path سراسری را عوض کنید.</li>
<li>رمزی که با <code>CREATE ROLE ... PASSWORD '...'</code> می‌دهید ممکن است در لاگ سرور (اگر log_statement فعال باشد) و تاریخچه‌ی psql بماند؛ از <code>\password app_user</code> استفاده کنید که هش را در کلاینت می‌سازد.</li>
<li>فایل server.key با مجوزی بازتر از 0600 باعث می‌شود سرور اصلاً بالا نیاید؛ پیام خطا در لاگ است، نه در خروجی systemctl.</li>
</ul>""",
                },
                {
                    "title": "Row Level Security: هر نمایندگی فقط سفارش‌های خودش",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>فیلتری که برنامه نمی‌تواند فراموش کند</h2>
<p>کارخانه نمایندگی‌هایی در تهران، مشهد و تبریز دارد و هر نمایندگی باید فقط مشتری‌ها و سفارش‌های خودش را ببیند. راه معمول، اضافه کردن <code>WHERE branch_id = ...</code> به همه‌ی کوئری‌های برنامه است؛ کافی است یک گزارش جدید آن را فراموش کند تا داده‌ی همه‌ی نمایندگی‌ها نشت کند. <strong>Row Level Security</strong> این شرط را به خود جدول می‌سپارد.</p>
<pre><code class="language-sql">ALTER TABLE factory.orders ADD COLUMN branch_id int NOT NULL DEFAULT 1;

ALTER TABLE factory.orders ENABLE ROW LEVEL SECURITY;

CREATE POLICY branch_isolation ON factory.orders
  FOR ALL
  TO carpet_rw
  USING (branch_id = current_setting('app.branch_id')::int)
  WITH CHECK (branch_id = current_setting('app.branch_id')::int);

-- نقش ستاد مرکزی همه را می‌بیند
CREATE POLICY hq_all ON factory.orders
  FOR SELECT TO carpet_ro
  USING (true);</code></pre>
<p><code>USING</code> تعیین می‌کند کدام ردیف‌ها <em>دیده</em> شوند (SELECT، UPDATE، DELETE) و <code>WITH CHECK</code> کدام ردیف‌ها <em>نوشته</em> شوند (INSERT و نتیجه‌ی UPDATE). بدون WITH CHECK، نمایندگی تهران می‌تواند سفارشی با branch_id مشهد درج کند.</p>
<h3>تنظیم شناسه در هر درخواست</h3>
<pre><code class="language-sql">BEGIN;
SET LOCAL app.branch_id = '3';
SELECT count(*) FROM factory.orders;     -- فقط سفارش‌های نمایندگی ۳
COMMIT;</code></pre>
<p>با <code>SET LOCAL</code> مقدار در پایان تراکنش پاک می‌شود؛ این برای PgBouncer در حالت transaction pooling حیاتی است، چون اتصال بعدی ممکن است متعلق به نمایندگی دیگری باشد. در جنگو می‌توانید در یک middleware داخل <code>transaction.atomic()</code> این SET LOCAL را اجرا کنید.</p>
<h3>چه کسی RLS را دور می‌زند</h3>
<table>
<thead><tr><th>نقش</th><th>RLS اعمال می‌شود؟</th></tr></thead>
<tbody>
<tr><td>superuser</td><td>هرگز</td></tr>
<tr><td>role با ویژگی BYPASSRLS</td><td>خیر</td></tr>
<tr><td>مالک جدول</td><td>خیر، مگر <code>FORCE ROW LEVEL SECURITY</code></td></tr>
<tr><td>بقیه بدون هیچ policy</td><td>هیچ ردیفی نمی‌بینند (پیش‌فرض بسته)</td></tr>
</tbody>
</table>
<h3>کارایی</h3>
<p>شرط policy مثل یک WHERE به کوئری اضافه می‌شود؛ پس روی <code>branch_id</code> ایندکس بگذارید یا آن را ستون اول ایندکس‌های ترکیبی کنید. اگر policy تابعی صدا می‌زند، آن را داخل زیرکوئری بنویسید تا یک بار برای کل کوئری محاسبه شود، نه برای هر ردیف:</p>
<pre><code class="language-sql">-- با فرض ستون branch_id در customers
CREATE POLICY branch_isolation_fast ON factory.customers
  TO carpet_rw
  USING (branch_id = (SELECT current_setting('app.branch_id')::int));</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>اگر <code>app.branch_id</code> تنظیم نشده باشد، <code>current_setting('app.branch_id')</code> خطا می‌دهد؛ با آرگومان دوم <code>true</code> به‌جای خطا NULL برمی‌گرداند و هیچ ردیفی دیده نمی‌شود. خطا دادن معمولاً امن‌تر است چون باگ را آشکار می‌کند.</li>
<li>policyهای چندگانه‌ی PERMISSIVE با OR ترکیب می‌شوند؛ با <code>AS RESTRICTIVE</code> شرطی می‌سازید که با AND اضافه شود، مثلاً «و فقط سفارش‌های حذف‌نشده».</li>
<li>بررسی FK و UNIQUE از RLS عبور می‌کند؛ کاربر با درج یک کد تکراری و دیدن خطای duplicate key می‌تواند وجود ردیفی را که نمی‌بیند تشخیص دهد.</li>
<li>pg_dump با کاربری که مشمول RLS است، به‌طور پیش‌فرض خطا می‌دهد تا بکاپ ناقص نگیرد؛ بکاپ را با مالک یا نقش BYPASSRLS بگیرید.</li>
<li>view در حالت پیش‌فرض با مجوز صاحبش اجرا می‌شود و اگر صاحبش مالک جدول باشد، RLS را دور می‌زند؛ برای viewهای روی جدول RLS‌دار <code>security_invoker = true</code> بگذارید.</li>
</ul>""",
                },
                {
                    "title": "بکاپ منطقی: pg_dump -Fc، pg_restore -j و pg_dumpall --globals-only",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>بکاپی که بازگردانی‌اش را تمرین نکرده‌اید، بکاپ نیست</h2>
<p><code>pg_dump</code> از یک دیتابیس در یک snapshot سازگار خروجی منطقی (دستورهای SQL یا معادل فشرده‌اش) می‌گیرد، بدون توقف و بدون قفل کردن نوشتن. برای دیتابیس‌های تا چند ده گیگابایت و برای انتقال بین نسخه‌ها و سرورها، ابزار اصلی همین است.</p>
<table>
<thead><tr><th>قالب</th><th>گزینه</th><th>ویژگی</th></tr></thead>
<tbody>
<tr><td>plain</td><td>-Fp</td><td>فایل SQL متنی؛ با psql بازگردانی می‌شود، انتخابی بازگرداندن سخت است</td></tr>
<tr><td>custom</td><td>-Fc</td><td>فشرده، بازگردانی انتخابی و موازی با pg_restore؛ <strong>انتخاب پیش‌فرض</strong></td></tr>
<tr><td>directory</td><td>-Fd</td><td>یک فایل برای هر جدول؛ تنها قالبی که <em>dump موازی</em> (-j) دارد</td></tr>
<tr><td>tar</td><td>-Ft</td><td>کاربرد کم؛ بدون فشرده‌سازی و بازگردانی موازی</td></tr>
</tbody>
</table>
<pre><code class="language-bash"># بکاپ روزانه با تاریخ
pg_dump -h localhost -U migrator -d carpet -Fc -Z 6 \
  -f /backup/carpet_$(date +%F).dump

# roleها، رمزها و tablespaceها در pg_dump نیستند!
pg_dumpall -h localhost -U postgres --globals-only -f /backup/globals_$(date +%F).sql

# دیتابیس بزرگ: dump موازی با ۴ پروسه
pg_dump -d carpet -Fd -j 4 -f /backup/carpet_dir</code></pre>
<h3>بازگردانی</h3>
<pre><code class="language-bash"># ۱) roleها روی سرور جدید
psql -U postgres -f /backup/globals_2026-03-10.sql

# ۲) دیتابیس خالی و بازگردانی موازی
createdb -U postgres -O carpet_owner carpet
pg_restore -U postgres -d carpet -j 4 --exit-on-error /backup/carpet_2026-03-10.dump

# فقط یک جدول را از بکاپ برگردانید
pg_restore -d carpet_tmp -t orders /backup/carpet_2026-03-10.dump

# فهرست محتوا، ویرایش و بازگردانی گزینشی
pg_restore -l carpet.dump &gt; toc.list
pg_restore -d carpet -L toc.list carpet.dump</code></pre>
<p>اگر روی سرور مقصد roleهای مبدأ وجود ندارند (مثلاً بازگردانی روی لپ‌تاپ)، <code>--no-owner --no-privileges</code> اشیا را به کاربر بازگرداننده می‌دهد و خطاهای GRANT را حذف می‌کند.</p>
<h3>آزمودن بکاپ</h3>
<pre><code class="language-bash">pg_restore -l /backup/carpet_$(date +%F).dump &gt; /dev/null &amp;&amp; echo "فایل سالم است"
# بهتر: بازگردانی کامل هفتگی روی سرور تست و مقایسه‌ی تعداد ردیف‌ها</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>همیشه با <code>pg_dump</code> نسخه‌ی <em>جدیدتر</em> (برابر نسخه‌ی مقصد) dump بگیرید؛ pg_dump 17 از سرور 12 بکاپ می‌گیرد، اما pg_dump 12 از سرور 17 امتناع می‌کند.</li>
<li><code>-j</code> در pg_restore با <code>--single-transaction</code> (یا ‎-1) سازگار نیست؛ یا موازی، یا اتمی.</li>
<li>بیشتر زمان restore صرف ساخت ایندکس‌ها و قیدهای FK می‌شود؛ <code>maintenance_work_mem</code> بزرگ در سرور مقصد آن را چند برابر سریع‌تر می‌کند.</li>
<li>در نسخه‌های 16 و 17، pg_dump آمار برنامه‌ریز را منتقل نمی‌کند؛ بلافاصله بعد از restore یک <code>ANALYZE</code> (یا <code>vacuumdb --analyze-in-stages</code>) بزنید، وگرنه ساعت اول همه‌ی کوئری‌ها پلن بد دارند.</li>
<li>با <code>--exclude-table-data='factory.loom_sensor_log*'</code> ساختار جدول‌های لاگ حجیم را نگه می‌دارید اما داده‌شان را نه؛ بکاپ روزانه چند برابر کوچک‌تر می‌شود.</li>
</ul>""",
                },
                {
                    "title": "بکاپ فیزیکی و PITR: pg_basebackup و آرشیو WAL",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>برگشت به ساعت ۱۴:۲۹، یک دقیقه قبل از DELETE اشتباه</h2>
<p>ساعت ۱۴:۳۰ کسی در psql نوشت <code>DELETE FROM orders</code> و WHERE را فراموش کرد. بکاپ شبانه‌ی pg_dump یعنی از دست دادن ۱۴ ساعت سفارش. <strong>PITR</strong> (بازیابی به نقطه‌ای از زمان) این را حل می‌کند: یک بکاپ فیزیکی پایه به‌علاوه‌ی همه‌ی فایل‌های WAL بعد از آن، دیتابیس را به هر ثانیه‌ی دلخواه برمی‌گرداند.</p>
<h3>WAL چیست</h3>
<p>هر تغییر قبل از نوشتن در فایل‌های داده، در Write-Ahead Log (پوشه‌ی pg_wal، قطعه‌های ۱۶ مگابایتی) ثبت می‌شود. پس از crash، پستگرس WAL را بازپخش می‌کند. اگر این قطعه‌ها را جایی امن آرشیو کنیم، می‌توانیم هر بازه‌ای را دوباره پخش کنیم.</p>
<pre><code class="language-ini"># postgresql.conf روی سرور اصلی (نیاز به restart)
wal_level = replica
archive_mode = on
archive_command = 'test ! -f /mnt/wal_archive/%f &amp;&amp; cp %p /mnt/wal_archive/%f'
archive_timeout = 300        # حداکثر ۵ دقیقه داده‌ی آرشیونشده</code></pre>
<h3>بکاپ پایه</h3>
<pre><code class="language-bash">sudo -u postgres pg_basebackup -D /backup/base_$(date +%F) \
  -Ft -z -P -X stream -c fast --manifest-checksums=SHA256

# pg_verifybackup در 16 و 17 فقط بکاپ قالب plain (-Fp) را با manifest بررسی می‌کند</code></pre>
<p><code>-X stream</code> فایل‌های WAL لازم برای سازگار بودن خود بکاپ را هم‌زمان می‌گیرد؛ بدون آن، بکاپ به‌تنهایی قابل بازگردانی نیست.</p>
<h3>بازیابی به یک لحظه</h3>
<pre><code class="language-bash">sudo systemctl stop postgresql
sudo mv /var/lib/postgresql/16/main /var/lib/postgresql/16/main.broken
sudo -u postgres mkdir -m 700 /var/lib/postgresql/16/main
sudo -u postgres tar -xzf /backup/base_2026-03-10/base.tar.gz -C /var/lib/postgresql/16/main
sudo -u postgres tar -xzf /backup/base_2026-03-10/pg_wal.tar.gz -C /var/lib/postgresql/16/main/pg_wal
sudo -u postgres touch /var/lib/postgresql/16/main/recovery.signal</code></pre>
<pre><code class="language-ini"># postgresql.conf (یا postgresql.auto.conf)
restore_command = 'cp /mnt/wal_archive/%f %p'
recovery_target_time = '2026-03-10 14:29:00+03:30'
recovery_target_action = 'pause'</code></pre>
<p>با <code>pause</code> سرور در لحظه‌ی هدف می‌ایستد و فقط خواندن را می‌پذیرد؛ داده را بررسی کنید و اگر درست بود <code>SELECT pg_wal_replay_resume();</code> بزنید تا سرور promote شود. اگر هدف زودتر از لازم بود، زمان دیرتری بگذارید و سرور را دوباره راه بیندازید تا بازپخش ادامه یابد؛ اما اگر از لحظه‌ی خطا گذشته باشید، راه برگشت فقط شروع دوباره از بکاپ پایه است.</p>
<h3>ابزارهای حرفه‌ای</h3>
<p>در تولید، به‌جای cp از ابزارهایی مثل <strong>pgBackRest</strong>، <strong>Barman</strong> یا <strong>WAL-G</strong> استفاده کنید: فشرده‌سازی، رمزنگاری، نگهداری دوره‌ای و بکاپ افزایشی دارند و archive_command را امن انجام می‌دهند. نسخه‌ی 17 خودش بکاپ افزایشی را با <code>pg_basebackup --incremental</code> و <code>pg_combinebackup</code> اضافه کرد (نیازمند <code>summarize_wal = on</code>).</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>اگر archive_command خطا بدهد، پستگرس WAL را پاک نمی‌کند و pg_wal تا پر شدن دیسک رشد می‌کند. <code>pg_stat_archiver</code> را پایش کنید: <code>failed_count</code> و <code>last_failed_time</code>.</li>
<li>بخش <code>test ! -f</code> در archive_command تصادفی نیست: جلوی بازنویسی یک قطعه‌ی آرشیوشده با نسخه‌ی دیگری (مثلاً از سرور دوم با همان مسیر) را می‌گیرد.</li>
<li>منطقه‌ی زمانی recovery_target_time را صریح بنویسید (‎+03:30)؛ بدون آن، زمان بر اساس تنظیم timezone سرور تفسیر می‌شود که معمولاً UTC است و سه ساعت و نیم اشتباه می‌کنید.</li>
<li>بکاپ فیزیکی کل کلاستر است: نمی‌توان فقط یک دیتابیس یا یک جدول را با PITR برگرداند. راه معمول: بازیابی روی سرور موقت و برداشتن جدول با pg_dump.</li>
<li>بکاپ فیزیکی فقط روی همان نسخه‌ی اصلی (major) و همان معماری پردازنده بازمی‌گردد؛ برای انتقال بین نسخه‌ها pg_dump یا pg_upgrade لازم است.</li>
</ul>""",
                },
                {
                    "title": "Streaming و Logical Replication",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>یک سرور کافی نیست</h2>
<p>Replication دو هدف دارد: <strong>دسترس‌پذیری</strong> (اگر سرور اصلی سوخت، یکی دیگر جایش بنشیند) و <strong>تقسیم بار</strong> (گزارش‌های سنگین روی نسخه‌ی خواندنی). پستگرس دو نوع کاملاً متفاوت دارد.</p>
<table>
<thead><tr><th></th><th>Streaming (فیزیکی)</th><th>Logical</th></tr></thead>
<tbody>
<tr><td>چه چیزی منتقل می‌شود</td><td>بایت‌های WAL؛ کپی دقیق کل کلاستر</td><td>تغییرات ردیفی جدول‌های انتخابی</td></tr>
<tr><td>نسخه‌ی مقصد</td><td>باید همان نسخه‌ی اصلی باشد</td><td>می‌تواند متفاوت باشد (ابزار ارتقای بی‌توقف)</td></tr>
<tr><td>مقصد قابل نوشتن؟</td><td>خیر، فقط خواندن</td><td>بله</td></tr>
<tr><td>DDL و sequence</td><td>بله، همه‌چیز</td><td>خیر؛ باید دستی هماهنگ شود</td></tr>
<tr><td>کاربرد</td><td>standby برای failover و خواندن</td><td>هم‌گام‌سازی بخشی از داده، ارتقا، تجمیع</td></tr>
</tbody>
</table>
<h3>راه‌اندازی Streaming Replication</h3>
<pre><code class="language-sql">-- روی سرور اصلی
CREATE ROLE replicator WITH REPLICATION LOGIN PASSWORD 'رمز-تکثیر';</code></pre>
<pre><code class="language-ini"># pg_hba.conf روی سرور اصلی
hostssl  replication  replicator  10.0.0.6/32  scram-sha-256</code></pre>
<pre><code class="language-bash"># روی سرور standby (پوشه‌ی داده خالی)
sudo -u postgres pg_basebackup -h 10.0.0.5 -U replicator \
  -D /var/lib/postgresql/16/main -X stream -P -R -C -S standby_tehran
sudo systemctl start postgresql</code></pre>
<p><code>-R</code> فایل standby.signal و تنظیم primary_conninfo را خودکار می‌نویسد؛ <code>-C -S</code> یک replication slot می‌سازد تا سرور اصلی WAL موردنیاز standby را تا رسیدنش نگه دارد.</p>
<pre><code class="language-sql">-- روی سرور اصلی: وضعیت و تأخیر
SELECT application_name, state, sync_state,
       pg_size_pretty(pg_wal_lsn_diff(pg_current_wal_lsn(), replay_lsn)) AS lag_bytes,
       replay_lag
FROM pg_stat_replication;

-- روی standby: ارتقا به اصلی هنگام خرابی
SELECT pg_promote();</code></pre>
<p>Replication به‌طور پیش‌فرض ناهمگام است: COMMIT منتظر standby نمی‌ماند و در لحظه‌ی خرابی ممکن است چند تراکنش آخر از دست برود. با <code>synchronous_standby_names</code> و <code>synchronous_commit = on</code> هیچ تراکنش تأییدشده‌ای گم نمی‌شود، به بهای تأخیر بیشتر در هر COMMIT. برای failover خودکار از ابزاری مثل <strong>Patroni</strong> استفاده کنید؛ promote دستی ساعت سه صبح قابل اتکا نیست.</p>
<h3>Logical Replication</h3>
<pre><code class="language-sql">-- مبدأ (wal_level = logical)
CREATE PUBLICATION pub_sales FOR TABLE factory.orders, factory.order_items, factory.customers;

-- مقصد: ساختار جدول‌ها باید از قبل وجود داشته باشد
CREATE SUBSCRIPTION sub_sales
  CONNECTION 'host=10.0.0.5 dbname=carpet user=replicator password=...'
  PUBLICATION pub_sales;

SELECT * FROM pg_stat_subscription;</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>replication slot رهاشده (standby که خاموش شد و فراموشش کردید) WAL را تا بی‌نهایت نگه می‌دارد و دیسک سرور اصلی را پر می‌کند؛ <code>max_slot_wal_keep_size</code> (نسخه‌ی 13) سقف می‌گذارد.</li>
<li>جدولی که در Logical Replication شرکت دارد برای UPDATE و DELETE به کلید اصلی (یا REPLICA IDENTITY) نیاز دارد؛ بدون آن، UPDATE روی مبدأ خطا می‌دهد.</li>
<li>بعد از سوییچ به سرور مقصد Logical، sequenceها عقب‌اند؛ قبل از باز کردن نوشتن، همه را با setval جلو ببرید.</li>
<li>کوئری طولانی روی standby ممکن است با خطای «canceling statement due to conflict with recovery» قطع شود؛ <code>hot_standby_feedback = on</code> این را کم می‌کند اما باعث bloat روی سرور اصلی می‌شود.</li>
<li>نسخه‌ی 17 ابزار <code>pg_createsubscriber</code> را آورد که یک standby فیزیکی را بدون کپی دوباره‌ی داده به subscriber منطقی تبدیل می‌کند؛ برای دیتابیس‌های بزرگ ساعت‌ها صرفه‌جویی است.</li>
</ul>""",
                },
                {
                    "title": "PgBouncer و محدودیت‌های transaction pooling؛ ارتقا با pg_upgrade",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>هر اتصال یک پروسه است</h2>
<p>در پستگرس هر اتصال یک پروسه‌ی سیستم‌عامل با چند مگابایت حافظه است. ۵۰۰ اتصال بی‌کار از چند worker جنگو و Celery سرور را کند می‌کند و با پیام «too many clients» از کار می‌اندازد. <strong>PgBouncer</strong> یک pool سبک بین برنامه و دیتابیس است: هزاران اتصال کلاینت را روی چند ده اتصال واقعی سوار می‌کند.</p>
<table>
<thead><tr><th>حالت</th><th>اتصال سرور کی آزاد می‌شود</th><th>ملاحظه</th></tr></thead>
<tbody>
<tr><td>session</td><td>وقتی کلاینت قطع شود</td><td>سازگاری کامل، صرفه‌جویی کم</td></tr>
<tr><td>transaction</td><td>پایان هر تراکنش</td><td>بیشترین صرفه‌جویی؛ محدودیت‌های مهم دارد</td></tr>
<tr><td>statement</td><td>پایان هر دستور</td><td>تراکنش چنددستوری ممنوع؛ کاربرد خاص</td></tr>
</tbody>
</table>
<pre><code class="language-ini">; /etc/pgbouncer/pgbouncer.ini
[databases]
carpet = host=127.0.0.1 port=5432 dbname=carpet

[pgbouncer]
listen_addr = 0.0.0.0
listen_port = 6432
auth_type = scram-sha-256
auth_file = /etc/pgbouncer/userlist.txt
pool_mode = transaction
default_pool_size = 20
max_client_conn = 2000
max_prepared_statements = 100
server_reset_query =</code></pre>
<h3>چه چیزهایی در transaction pooling خراب می‌شود</h3>
<p>در این حالت، دو تراکنش پشت‌سرهم یک کلاینت ممکن است روی دو اتصال سرور مختلف اجرا شوند؛ پس هر چیزی که به «نشست» وابسته است قابل اتکا نیست:</p>
<ul>
<li><code>SET</code> معمولی (به‌جایش <code>SET LOCAL</code> داخل تراکنش)</li>
<li>advisory lock سطح نشست، <code>LISTEN</code>، جدول TEMP بیرون از تراکنش</li>
<li>cursorهای WITH HOLD و server-side cursor بیرون از تراکنش</li>
<li>prepared statement، مگر با PgBouncer 1.21 به بعد و <code>max_prepared_statements</code></li>
</ul>
<p>در جنگو پشت PgBouncer تراکنشی، <code>DISABLE_SERVER_SIDE_CURSORS = True</code> بگذارید؛ وگرنه <code>.iterator()</code> با خطای «cursor does not exist» می‌شکند.</p>
<h3>ارتقای نسخه‌ی اصلی با pg_upgrade</h3>
<p>نسخه‌های اصلی (مثلاً 16 به 17) قالب فایل داده‌ی متفاوتی دارند. pg_dump/restore امن اما برای چند صد گیگابایت کند است. <code>pg_upgrade</code> کاتالوگ را منتقل می‌کند و فایل‌های داده را کپی یا لینک می‌کند:</p>
<pre><code class="language-bash"># اوبونتو: نسخه‌ی جدید نصب، سپس
sudo systemctl stop postgresql
cd /tmp    # pg_upgrade فایل‌های لاگش را در پوشه‌ی جاری می‌نویسد
sudo -u postgres /usr/lib/postgresql/17/bin/pg_upgrade \
  -b /usr/lib/postgresql/16/bin -B /usr/lib/postgresql/17/bin \
  -d /var/lib/postgresql/16/main -D /var/lib/postgresql/17/main \
  -o '-c config_file=/etc/postgresql/16/main/postgresql.conf' \
  -O '-c config_file=/etc/postgresql/17/main/postgresql.conf' \
  --link --check
# اگر --check تمیز بود، همان فرمان بدون --check

sudo -u postgres /usr/lib/postgresql/17/bin/vacuumdb --all --analyze-in-stages</code></pre>
<p>روی اوبونتو، <code>pg_upgradecluster 16 main</code> همین مراحل را با تنظیمات بسته‌ی PGDG انجام می‌دهد.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>با <code>--link</code> ارتقا چند ثانیه طول می‌کشد، اما بعد از اولین اجرای کلاستر جدید، کلاستر قدیمی دیگر قابل استفاده نیست؛ قبلش بکاپ بگیرید. <code>--clone</code> روی فایل‌سیستم‌های XFS و Btrfs همان سرعت را بدون این ریسک می‌دهد.</li>
<li>کلاستر جدید باید با همان encoding و locale قدیمی initdb شود؛ تفاوت locale یکی از رایج‌ترین دلایل شکست <code>--check</code> است.</li>
<li>تغییر نسخه‌ی glibc (مشهورترینش عبور از glibc 2.28، مثلاً ارتقای اوبونتو 18.04 به 20.04) ترتیب مرتب‌سازی متن را عوض می‌کند و ایندکس‌های متنی را بی‌صدا خراب می‌کند؛ بعد از ارتقای سیستم‌عامل REINDEX کنید یا از ICU استفاده کنید.</li>
<li>PgBouncer پس از <code>RELOAD</code> در کنسول مدیریتی‌اش (اتصال به دیتابیس مجازی pgbouncer) تنظیمات را بدون قطع اتصال‌ها دوباره می‌خواند و <code>SHOW POOLS</code> صف انتظار کلاینت‌ها را نشان می‌دهد.</li>
<li>اندازه‌ی pool را بزرگ نگیرید: معمولاً چند برابر تعداد هسته‌های CPU کافی است؛ اتصال واقعی بیشتر فقط رقابت روی قفل‌ها و CPU را بیشتر می‌کند.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۸ ─────────────────────────────
        {
            "title": "فصل ۸: اکستنشن‌ها، اتصال به برنامه و پروژه‌ی پایانی",
            "lessons": [
                {
                    "title": "اکستنشن‌های مهم و partitioning اعلانی",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>پستگرس را با اکستنشن بزرگ کنید، نه با سرویس جدید</h2>
<p>بخش بزرگی از قدرت پستگرس در اکستنشن‌هاست: نوع داده، ایندکس، تابع و حتی زبان جدید که مثل بخشی از هسته رفتار می‌کنند. بسیاری از آن‌ها همراه بسته‌ی <code>postgresql-contrib</code> (در نسخه‌های جدید PGDG داخل خود بسته‌ی اصلی) نصب‌اند و فقط باید در هر دیتابیس فعال شوند.</p>
<table>
<thead><tr><th>اکستنشن</th><th>کاربرد</th></tr></thead>
<tbody>
<tr><td>pg_trgm</td><td>LIKE '%..%' سریع، جست‌وجوی تقریبی (فصل ۵)</td></tr>
<tr><td>unaccent</td><td>حذف علائم؛ با فایل قاعده‌ی سفارشی برای یکسان‌سازی حروف عربی و فارسی در full-text</td></tr>
<tr><td>btree_gist / btree_gin</td><td>ستون معمولی در ایندکس GiST یا GIN؛ لازم برای EXCLUDE با = (فصل ۳)</td></tr>
<tr><td>pg_stat_statements</td><td>آمار تجمعی کوئری‌ها (فصل ۵)</td></tr>
<tr><td>pgcrypto</td><td>هش و رمزنگاری در SQL؛ gen_random_uuid از نسخه‌ی 13 در هسته است</td></tr>
<tr><td>postgis</td><td>داده‌ی مکانی: فاصله‌ی نمایندگی‌ها، محدوده‌ی پخش</td></tr>
<tr><td>pgvector</td><td>بردار embedding و جست‌وجوی شباهت با ایندکس HNSW برای هوش مصنوعی</td></tr>
</tbody>
</table>
<pre><code class="language-sql">SELECT name, default_version, installed_version
FROM pg_available_extensions WHERE name IN ('pg_trgm', 'unaccent', 'postgis', 'vector');

CREATE EXTENSION IF NOT EXISTS pg_trgm WITH SCHEMA public;
\dx</code></pre>
<h3>partitioning اعلانی</h3>
<p>جدول لاگ حسگرهای دستگاه‌ها سالی چند صد میلیون ردیف می‌گیرد. اگر آن را بر اساس زمان به پارتیشن‌های ماهانه بشکنیم، کوئری‌های «این ماه» فقط یک پارتیشن را می‌خوانند (<strong>partition pruning</strong>) و پاک کردن داده‌ی یک سال پیش یک DROP لحظه‌ای است، نه DELETE میلیونی که bloat بسازد. مرز پارتیشن‌ها را می‌توان با ماه‌های شمسی گذاشت:</p>
<pre><code class="language-sql">CREATE TABLE factory.loom_sensor_log (
  loom_id     int NOT NULL,
  recorded_at timestamptz NOT NULL,
  rpm         smallint,
  temp_c      numeric(4,1),
  PRIMARY KEY (loom_id, recorded_at)
) PARTITION BY RANGE (recorded_at);

-- فروردین و اردیبهشت ۱۴۰۵
CREATE TABLE factory.loom_sensor_log_1405_01 PARTITION OF factory.loom_sensor_log
  FOR VALUES FROM ('2026-03-21 00:00+03:30') TO ('2026-04-21 00:00+03:30');
CREATE TABLE factory.loom_sensor_log_1405_02 PARTITION OF factory.loom_sensor_log
  FOR VALUES FROM ('2026-04-21 00:00+03:30') TO ('2026-05-22 00:00+03:30');

CREATE INDEX ON factory.loom_sensor_log USING brin (recorded_at);

-- بایگانی یک ماه: جدا کردن بدون قفل سنگین (نسخه‌ی 14)
ALTER TABLE factory.loom_sensor_log DETACH PARTITION factory.loom_sensor_log_1405_01 CONCURRENTLY;</code></pre>
<p>ایندکسی که روی والد بسازید خودکار روی همه‌ی پارتیشن‌ها، از جمله پارتیشن‌های آینده، ساخته می‌شود.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>کلید اصلی و UNIQUE روی جدول partition‌شده باید ستون پارتیشن را شامل شود؛ برای همین PRIMARY KEY بالا (loom_id, recorded_at) است، نه یک id تنها.</li>
<li>پارتیشن DEFAULT (<code>PARTITION OF ... DEFAULT</code>) تله دارد: ساختن هر پارتیشن جدید باید کل آن را اسکن کند تا ردیفی از بازه‌ی جدید در آن نباشد، و وجودش <code>DETACH ... CONCURRENTLY</code> را غیرممکن می‌کند. به‌جایش پارتیشن‌های آینده را زودتر بسازید.</li>
<li>pruning فقط وقتی کار می‌کند که شرط مستقیم روی ستون پارتیشن باشد؛ <code>WHERE recorded_at::date = '2026-04-01'</code> همه‌ی پارتیشن‌ها را می‌خواند.</li>
<li>زیر چند ده میلیون ردیف، partitioning معمولاً فقط پیچیدگی اضافه می‌کند؛ ایندکس مناسب کافی است. برای ساخت خودکار پارتیشن‌های آینده از اکستنشن <code>pg_partman</code> کمک بگیرید.</li>
<li>CREATE EXTENSION در 13 به بعد برای اکستنشن‌های «trusted» (مثل pg_trgm و unaccent) به superuser نیاز ندارد؛ مالک دیتابیس با مجوز CREATE کافی است.</li>
</ul>""",
                },
                {
                    "title": "PL/pgSQL و trigger: updated_at، audit log و LISTEN/NOTIFY",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>منطقی که باید هر بار و برای همه اجرا شود</h2>
<p>trigger برای قاعده‌هایی است که نباید به حافظه‌ی برنامه‌نویس وابسته باشند: ثبت زمان آخرین تغییر، ثبت تاریخچه‌ی تغییرات، یکسان‌سازی «ی» و «ک». هر کسی از هر مسیری (جنگو، psql، اسکریپت ورود اکسل) داده را عوض کند، trigger اجرا می‌شود.</p>
<h3>updated_at خودکار</h3>
<pre><code class="language-sql">CREATE OR REPLACE FUNCTION factory.touch_updated_at()
RETURNS trigger
LANGUAGE plpgsql AS $$
BEGIN
  NEW.updated_at := now();
  RETURN NEW;
END;
$$;

ALTER TABLE factory.orders ADD COLUMN updated_at timestamptz NOT NULL DEFAULT now();

CREATE TRIGGER orders_touch
BEFORE UPDATE ON factory.orders
FOR EACH ROW
WHEN (OLD.* IS DISTINCT FROM NEW.*)
EXECUTE FUNCTION factory.touch_updated_at();</code></pre>
<p>شرط <code>WHEN</code> باعث می‌شود UPDATEی که چیزی را عوض نکرده، زمان را هم عوض نکند.</p>
<h3>audit log با jsonb</h3>
<pre><code class="language-sql">CREATE TABLE factory.audit_log (
  id         bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  table_name text NOT NULL,
  op         text NOT NULL,
  row_pk     text,
  old_row    jsonb,
  new_row    jsonb,
  changed_by text NOT NULL DEFAULT current_user,
  app_user   text DEFAULT current_setting('app.user', true),
  changed_at timestamptz NOT NULL DEFAULT now()
);

CREATE OR REPLACE FUNCTION factory.audit_row()
RETURNS trigger
LANGUAGE plpgsql
SECURITY DEFINER SET search_path = factory, pg_temp
AS $$
BEGIN
  INSERT INTO factory.audit_log (table_name, op, row_pk, old_row, new_row)
  VALUES (
    TG_TABLE_NAME,
    TG_OP,
    COALESCE(to_jsonb(NEW) -&gt;&gt; 'id', to_jsonb(OLD) -&gt;&gt; 'id'),
    CASE WHEN TG_OP IN ('UPDATE', 'DELETE') THEN to_jsonb(OLD) END,
    CASE WHEN TG_OP IN ('INSERT', 'UPDATE') THEN to_jsonb(NEW) END
  );
  RETURN NULL;   -- trigger از نوع AFTER است؛ مقدار بازگشتی نادیده گرفته می‌شود
END;
$$;

CREATE TRIGGER orders_audit
AFTER INSERT OR UPDATE OR DELETE ON factory.orders
FOR EACH ROW EXECUTE FUNCTION factory.audit_row();</code></pre>
<p>ستون <code>app_user</code> نام کاربر برنامه را از متغیری می‌خواند که برنامه با <code>SET LOCAL app.user = 'zahra.karimi'</code> تنظیم می‌کند؛ چون کاربر دیتابیس برای همه app_user است و به‌تنهایی نمی‌گوید چه کسی قیمت را عوض کرد.</p>
<h3>LISTEN/NOTIFY: خبر دادن به برنامه</h3>
<pre><code class="language-sql">CREATE OR REPLACE FUNCTION factory.notify_order_status()
RETURNS trigger LANGUAGE plpgsql AS $$
BEGIN
  PERFORM pg_notify('order_status',
    json_build_object('id', NEW.id, 'status', NEW.status)::text);
  RETURN NULL;
END;
$$;

CREATE TRIGGER orders_notify
AFTER UPDATE OF status ON factory.orders
FOR EACH ROW EXECUTE FUNCTION factory.notify_order_status();

-- در یک نشست دیگر:
LISTEN order_status;</code></pre>
<p>پیام فقط پس از COMMIT تحویل می‌شود؛ اگر تراکنش rollback شود، هیچ پیامی نمی‌رود. سرویسی که داشبورد سالن بافندگی را زنده به‌روز می‌کند می‌تواند به‌جای پرسیدن هر ثانیه، فقط گوش بدهد.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>NOTIFY پیام تکراری با کانال و محتوای یکسان در یک تراکنش را یکی می‌کند و حداکثر حدود 8000 بایت محتوا می‌پذیرد؛ شناسه بفرستید، نه کل ردیف.</li>
<li>LISTEN پشت PgBouncer در حالت transaction کار نمی‌کند؛ شنونده باید مستقیم به پستگرس (یا یک pool با حالت session) وصل شود.</li>
<li>در تابع SECURITY DEFINER همیشه <code>SET search_path</code> بگذارید؛ وگرنه کاربری که schema خودش را جلوی search_path بگذارد، می‌تواند تابع یا جدولی هم‌نام بسازد و با مجوز مالک اجرا شود.</li>
<li>trigger سطح دستور با «transition table» (<code>REFERENCING NEW TABLE AS new_rows</code> و <code>FOR EACH STATEMENT</code>) برای UPDATE صدهزار ردیفی یک بار اجرا می‌شود، نه صدهزار بار؛ audit گروهی را خیلی سریع‌تر می‌کند.</li>
<li>از نسخه‌ی 14، <code>CREATE OR REPLACE TRIGGER</code> وجود دارد و migrationهای trigger دیگر به DROP و CREATE جدا نیاز ندارند.</li>
</ul>""",
                },
                {
                    "title": "اتصال از پایتون و جنگو: psycopg 3 و django.contrib.postgres",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>از کد برنامه به دیتابیس، درست و امن</h2>
<h3>psycopg 3</h3>
<p>psycopg 3 جانشین psycopg2 است: پشتیبانی بومی از async، COPY راحت، pool جدا و ارسال پارامتر سمت سرور. اگر pip به خاطر تحریم یا کندی شبکه به مشکل خورد، از یک میرور داخلی PyPI با گزینه‌ی <code>-i</code> استفاده کنید.</p>
<pre><code class="language-bash">pip install "psycopg[binary]" psycopg_pool</code></pre>
<pre><code class="language-python">import psycopg
from psycopg.rows import dict_row

DSN = "host=127.0.0.1 port=5432 dbname=carpet user=app_user password=... sslmode=prefer"

with psycopg.connect(DSN, row_factory=dict_row) as conn:
    # پارامتر همیشه با %s، هرگز با f-string (SQL injection)
    rows = conn.execute(
        "SELECT id, status FROM factory.orders WHERE customer_id = %s AND status = %s",
        (42, "weaving"),
    ).fetchall()

    # ورود انبوه با COPY: ده‌ها برابر سریع‌تر از INSERTهای تکی
    with conn.cursor() as cur:
        with cur.copy("COPY factory.customers (full_name, city) FROM STDIN") as copy:
            for name, city in [("زهرا کریمی", "کاشان"), ("علی نراقی", "آران و بیدگل")]:
                copy.write_row((name, city))
# خروج از with: COMMIT (یا ROLLBACK در صورت خطا) و بستن اتصال</code></pre>
<h3>تنظیمات جنگو</h3>
<pre><code class="language-python"># settings.py
import os

INSTALLED_APPS += ["django.contrib.postgres"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",   # جنگو 4.2+ خودکار psycopg 3 را برمی‌دارد
        "NAME": "carpet",
        "USER": "app_user",
        "PASSWORD": os.environ["DB_PASSWORD"],
        "HOST": "127.0.0.1",
        "PORT": "5432",
        "CONN_MAX_AGE": 60,            # اتصال را ۶۰ ثانیه بین درخواست‌ها نگه دار
        "CONN_HEALTH_CHECKS": True,    # قبل از استفاده‌ی مجدد، سلامت اتصال را بسنج
        "OPTIONS": {
            "options": "-c search_path=factory,public -c statement_timeout=30000",
        },
    }
}</code></pre>
<h3>django.contrib.postgres در عمل</h3>
<pre><code class="language-python">from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, TrigramSimilarity
from django.db import models

class Design(models.Model):
    code = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=100)
    tags = ArrayField(models.CharField(max_length=30), default=list, blank=True)

    class Meta:
        indexes = [GinIndex(fields=["tags"], name="design_tags_gin")]

Design.objects.filter(tags__contains=["ابریشم"])          # tags @&gt; ARRAY[...]
Design.objects.filter(tags__overlap=["افشان", "هریس"])     # tags &amp;&amp; ARRAY[...]

q = SearchQuery("افشان", config="simple", search_type="websearch")
(Design.objects
   .annotate(rank=SearchRank(SearchVector("title", config="simple"), q))
   .filter(rank__gt=0).order_by("-rank"))

Design.objects.annotate(sim=TrigramSimilarity("title", "افشن")).filter(sim__gt=0.3).order_by("-sim")</code></pre>
<p>TrigramSimilarity به اکستنشن pg_trgm نیاز دارد؛ آن را در یک migration با عملیات <code>TrigramExtension()</code> فعال کنید تا روی سرور تازه فراموش نشود.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>از جنگو 5.1 می‌توانید با <code>"OPTIONS": {"pool": True}</code> از pool داخلی psycopg استفاده کنید؛ در این حالت CONN_MAX_AGE باید 0 بماند و پشت PgBouncer هم به آن نیازی ندارید.</li>
<li><code>CONN_MAX_AGE = None</code> (اتصال دائمی) در کنار gunicorn با worker زیاد سریع به سقف max_connections می‌رسد؛ تعداد اتصال‌ها برابر workers × threads است.</li>
<li>جست‌وجوی SearchVector در کوئری، tsvector را برای هر ردیف از نو می‌سازد؛ برای جدول بزرگ ستون tsvector ذخیره‌شده با ایندکس GIN (مثل فصل ۵) بسازید و با <code>SearchVectorField</code> به آن اشاره کنید.</li>
<li>psycopg 3 پارامترها را سمت سرور می‌فرستد؛ پس <code>%s</code> فقط جای <em>مقدار</em> می‌نشیند، نه نام جدول یا ستون. برای شناسه‌ها از <code>psycopg.sql.Identifier</code> استفاده کنید.</li>
<li>متد <code>.iterator()</code> در جنگو روی پستگرس server-side cursor می‌سازد و حافظه را برای میلیون‌ها ردیف ثابت نگه می‌دارد؛ اما پشت PgBouncer تراکنشی باید DISABLE_SERVER_SIDE_CURSORS را روشن کنید (فصل ۷).</li>
</ul>""",
                },
                {
                    "title": "پروژه‌ی پایانی: آماده‌سازی دیتابیس کارخانه‌ی فرش برای تولید",
                    "kind": "text",
                    "minutes": 30,
                    "is_preview": False,
                    "body": r"""<h2>از طرح فصل ۳ تا سروری که می‌شود به آن تکیه کرد</h2>
<p>در این پروژه دیتابیس کارخانه‌ی فرش را که در فصل ۳ طراحی کردیم، برای سرور واقعی آماده می‌کنیم: سروری با ۸ هسته، ۳۲ گیگابایت RAM و SSD که برنامه‌ی جنگوی ثبت سفارش، داشبورد سالن بافندگی و گزارش‌های مالی به آن وصل‌اند. هر گام را اجرا کنید و نتیجه را با کوئری بررسی کنید.</p>
<h3>گام ۱: تنظیمات کلیدی</h3>
<pre><code class="language-ini"># /etc/postgresql/17/main/conf.d/tuning.conf
shared_buffers = 8GB               # حدود ۲۵٪ RAM؛ نیاز به restart
effective_cache_size = 24GB        # تخمین cache کل (پستگرس + سیستم‌عامل)؛ فقط راهنمای برنامه‌ریز
work_mem = 32MB                    # برای هر Sort/Hash در هر کوئری، نه برای هر اتصال
maintenance_work_mem = 1GB         # VACUUM، CREATE INDEX، restore
random_page_cost = 1.1             # SSD؛ پیش‌فرض 4 برای دیسک چرخان است
effective_io_concurrency = 200
max_connections = 100              # پشت PgBouncer
max_wal_size = 8GB
checkpoint_completion_target = 0.9
wal_compression = lz4

log_min_duration_statement = 500ms
log_lock_waits = on
log_autovacuum_min_duration = 10s
log_line_prefix = '%m [%p] %q%u@%d '
shared_preload_libraries = 'pg_stat_statements'

idle_in_transaction_session_timeout = 5min
autovacuum_vacuum_cost_limit = 2000</code></pre>
<p>حساب سرانگشتی work_mem: ۱۰۰ اتصال × چند گره‌ی Sort در هر کوئری × 32MB می‌تواند از RAM بیشتر شود. مقدار سراسری را محتاط بگیرید و برای نقش گزارش‌گیر بیشتر کنید: <code>ALTER ROLE bi_reader SET work_mem = '256MB';</code></p>
<h3>گام ۲: نقش‌ها و امنیت</h3>
<p>سه نقش گروهی فصل ۷ (owner، rw، ro) با DEFAULT PRIVILEGES؛ برنامه فقط با app_user، migration فقط با migrator. pg_hba فقط hostssl با scram-sha-256 از زیرشبکه‌ی سرور برنامه.</p>
<h3>گام ۳: ایندکس‌ها بر اساس کوئری‌های واقعی</h3>
<pre><code class="language-sql">CREATE INDEX CONCURRENTLY orders_open_due_idx ON factory.orders (due_date)
  WHERE status IN ('confirmed', 'weaving', 'finishing');
CREATE INDEX CONCURRENTLY qc_defects_gin ON factory.qc_inspections USING gin (defects jsonb_path_ops);
CREATE INDEX CONCURRENTLY customers_name_trgm ON factory.customers
  USING gin (factory.fa_normalize(full_name) gin_trgm_ops);

-- بعد از یک هفته کار واقعی:
SELECT left(query, 70), calls, round(mean_exec_time::numeric, 1) AS mean_ms
FROM pg_stat_statements ORDER BY total_exec_time DESC LIMIT 10;</code></pre>
<h3>گام ۴: نگهداری و تاریخچه</h3>
<p>trigger updated_at و audit_log روی orders و order_items؛ جدول لاگ حسگرها partition ماهانه‌ی شمسی؛ autovacuum تهاجمی برای جدول موجودی نخ. صف کارهای پس‌زمینه (صدور فاکتور PDF، پیامک ارسال سفارش) با جدول jobs و SKIP LOCKED.</p>
<h3>گام ۵: بکاپ و بازیابی</h3>
<table>
<thead><tr><th>چه</th><th>چگونه</th><th>چه وقت</th></tr></thead>
<tbody>
<tr><td>بکاپ فیزیکی + WAL</td><td>pgBackRest یا pg_basebackup و archive_command</td><td>کامل هفتگی، WAL پیوسته</td></tr>
<tr><td>بکاپ منطقی</td><td>pg_dump -Fc + pg_dumpall --globals-only</td><td>شبانه، نگهداری ۱۴ روز</td></tr>
<tr><td>آزمون بازگردانی</td><td>restore روی سرور تست و مقایسه‌ی تعداد ردیف</td><td>ماهانه</td></tr>
<tr><td>نسخه‌ی خارج از سایت</td><td>کپی رمزشده به دیتاسنتر دوم</td><td>روزانه</td></tr>
</tbody>
</table>
<h3>گام ۶: پایش</h3>
<pre><code class="language-sql">-- نسبت cache hit (باید بالای ۹۹٪ باشد)
SELECT round(100.0 * sum(blks_hit) / nullif(sum(blks_hit) + sum(blks_read), 0), 2) AS hit_pct
FROM pg_stat_database;

-- سن xid، اتصال‌ها بر اساس وضعیت، slotهای غیرفعال
SELECT max(age(datfrozenxid)) FROM pg_database;
SELECT state, count(*) FROM pg_stat_activity GROUP BY state;
SELECT slot_name, active, wal_status FROM pg_replication_slots WHERE NOT active;</code></pre>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>shared_buffers بیش از ۴۰٪ RAM معمولاً بهتر نمی‌کند، چون پستگرس به cache سیستم‌عامل هم تکیه دارد و داده دو بار cache می‌شود.</li>
<li>با shared_buffers چند گیگابایتی، <code>huge_pages = try</code> و تنظیم <code>vm.nr_hugepages</code> در لینوکس سربار مدیریت حافظه را محسوس کم می‌کند.</li>
<li>فایل‌های <code>conf.d</code> در اوبونتو بعد از postgresql.conf خوانده می‌شوند؛ تنظیمات خودتان را آن‌جا بگذارید تا ارتقای بسته فایل اصلی را بی‌دردسر عوض کند.</li>
<li>ابزار <code>pg_test_fsync</code> سرعت واقعی fsync دیسک را می‌سنجد؛ روی بعضی سرورهای مجازی ارزان، همین عدد سقف تراکنش در ثانیه‌ی شماست.</li>
<li>عدد بالای <code>num_requested</code> در نمای <code>pg_stat_checkpointer</code> (نسخه‌ی 17؛ در 16 ستون <code>checkpoints_req</code> در pg_stat_bgwriter) یعنی max_wal_size کوچک است و checkpointها زودتر از موعد اجرا می‌شوند.</li>
</ul>""",
                },
                {
                    "title": "کلینیک خطاهای رایج PostgreSQL",
                    "kind": "text",
                    "minutes": 26,
                    "is_preview": False,
                    "body": r"""<h2>پیام خطا را بخوانید؛ معمولاً دقیقاً می‌گوید چه شده</h2>
<p>این درس فهرست مشکلاتی است که تقریباً هر تیمی دیر یا زود با آن‌ها روبه‌رو می‌شود؛ برای هرکدام علت و درمان را آورده‌ایم. اول جدول خلاصه، بعد جزئیات.</p>
<table>
<thead><tr><th>نشانه</th><th>علت رایج</th><th>درمان کوتاه</th></tr></thead>
<tbody>
<tr><td>Peer authentication failed for user</td><td>اتصال سوکت محلی با روش peer و نام کاربری متفاوت با کاربر سیستم‌عامل</td><td>با <code>-h localhost</code> وصل شوید یا خط local را scram-sha-256 کنید و reload</td></tr>
<tr><td>sorry, too many clients already</td><td>pool نامحدود، CONN_MAX_AGE دائمی، اتصال‌های بی‌کار</td><td>PgBouncer، کاهش workers، بستن اتصال‌های بی‌کار</td></tr>
<tr><td>permission denied for schema public</td><td>نسخه‌ی 15 به بعد مجوز CREATE را از PUBLIC گرفته</td><td>schema اختصاصی یا GRANT CREATE صریح</td></tr>
<tr><td>duplicate key value violates unique constraint "..._pkey" بعد از restore</td><td>sequence از max(id) عقب مانده</td><td>setval</td></tr>
<tr><td>deadlock detected</td><td>قفل ردیف‌ها با ترتیب متفاوت</td><td>ترتیب ثابت، retry</td></tr>
<tr><td>could not write to file ... No space left on device</td><td>WAL انباشته از slot رهاشده یا archive شکست‌خورده</td><td>حذف slot، درست کردن archive_command</td></tr>
<tr><td>کندی تدریجی بدون تغییر کد</td><td>bloat یا آمار کهنه</td><td>VACUUM/ANALYZE، تنظیم autovacuum</td></tr>
</tbody>
</table>
<h3>permission denied for schema public</h3>
<pre><code class="language-sql">-- بهترین راه: schema اختصاصی برای برنامه
CREATE SCHEMA app AUTHORIZATION carpet_owner;
ALTER ROLE migrator SET search_path = app;

-- یا: مالک دیتابیس کردن نقش مالک (public از 15 مال pg_database_owner است)
ALTER DATABASE carpet OWNER TO carpet_owner;

-- یا ساده و کمتر امن
GRANT CREATE ON SCHEMA public TO migrator;</code></pre>
<h3>duplicate key پس از restore یا ورود دستی داده</h3>
<pre><code class="language-sql">SELECT setval(pg_get_serial_sequence('factory.orders', 'id'),
              coalesce(max(id), 0) + 1, false)
FROM factory.orders;</code></pre>
<p>این حالت معمولاً وقتی پیش می‌آید که داده با id صریح وارد شده (مثلاً <code>OVERRIDING SYSTEM VALUE</code> یا COPY فقط داده بدون sequence). تابع pg_get_serial_sequence برای identity هم کار می‌کند.</p>
<h3>دیسک پر از WAL</h3>
<pre><code class="language-sql">SELECT slot_name, active, wal_status,
       pg_size_pretty(pg_wal_lsn_diff(pg_current_wal_lsn(), restart_lsn)) AS retained
FROM pg_replication_slots;
SELECT failed_count, last_failed_wal, last_failed_time FROM pg_stat_archiver;

SELECT pg_drop_replication_slot('standby_old');   -- فقط اگر واقعاً دیگر لازم نیست</code></pre>
<p>هرگز فایل‌های داخل pg_wal را دستی پاک نکنید؛ دیتابیس دیگر بالا نمی‌آید. علت را برطرف کنید؛ پستگرس در checkpoint بعدی خودش پاک می‌کند.</p>
<h3>کندی تدریجی</h3>
<pre><code class="language-sql">SELECT relname, n_dead_tup, last_autovacuum, last_autoanalyze, n_mod_since_analyze
FROM pg_stat_user_tables ORDER BY n_dead_tup DESC LIMIT 10;
VACUUM (VERBOSE, ANALYZE) factory.orders;</code></pre>
<p>اگر n_dead_tup بالاست و VACUUM چیزی پاک نمی‌کند (در خروجی VERBOSE عبارت «are dead but not yet removable» با عددی بزرگ)، دنبال تراکنش قدیمی، idle in transaction یا slot رهاشده بگردید (فصل ۶).</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>superuser_reserved_connections</code> (پیش‌فرض ۳) چند اتصال را برای superuser نگه می‌دارد؛ حتی وقتی برنامه همه را پر کرده، می‌توانید با postgres وارد شوید و اتصال‌ها را ببندید. نسخه‌ی 16 <code>reserved_connections</code> و نقش pg_use_reserved_connections را هم برای نقش‌های غیر superuser آورد.</li>
<li>پیام «could not connect ... Connection refused» با «no pg_hba.conf entry» فرق دارد: اولی یعنی سرور گوش نمی‌دهد (listen_addresses، فایروال)، دومی یعنی رسیده‌اید اما pg_hba راهتان نمی‌دهد.</li>
<li>در خطای duplicate key، بخش DETAIL کلید دقیق را نشان می‌دهد (<code>Key (id)=(1205) already exists</code>)؛ لاگ برنامه‌ها اغلب فقط خط اول را نگه می‌دارند و همین جزئیات گم می‌شود.</li>
<li>متن کامل خطا و SQLSTATE را با <code>\set VERBOSITY verbose</code> در psql ببینید؛ کد SQLSTATE (مثل 23505 یا 40P01) برای مدیریت خطا در برنامه پایدارتر از متن پیام است که با زبان سرور عوض می‌شود.</li>
<li>بعد از restore یک بکاپ قدیمی، اگر برنامه خطای «column does not exist» می‌دهد، جدول <code>django_migrations</code> را با وضعیت واقعی جدول‌ها مقایسه کنید؛ بکاپ و کد از دو زمان متفاوت‌اند.</li>
</ul>""",
                },
            ],
        },
    ],
}

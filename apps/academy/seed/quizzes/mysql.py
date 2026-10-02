# -*- coding: utf-8 -*-
# بانک ۳۶ سؤالی آزمون دوره‌ی جامع MySQL — هر نوبت ۲۰ سؤال تصادفی

QUIZ = {
    "course_slug": "mysql",
    "title": "آزمون پایانی آموزش جامع MySQL",
    "pass_percent": 70,
    "time_limit_minutes": 30,
    "questions_per_attempt": 20,
    "questions": [
        # ── فصل ۱
        {
            "text": "چرا برای ذخیره‌ی متن فارسی همراه با ایموجی باید از `utf8mb4` استفاده کرد و نه `utf8` (utf8mb3)؟",
            "explanation": "utf8mb3 حداکثر سه بایت برای هر کاراکتر ذخیره می‌کند؛ ایموجی و برخی کاراکترها چهاربایتی‌اند و با خطای Incorrect string value رد می‌شوند. utf8mb4 یونیکد کامل است.",
            "choices": [
                {"text": "utf8 حروف فارسی را اصلاً پشتیبانی نمی‌کند", "correct": False},
                {"text": "utf8mb3 فقط تا سه بایت برای هر کاراکتر دارد و کاراکترهای چهاربایتی مثل ایموجی را نمی‌پذیرد", "correct": True},
                {"text": "utf8mb4 فضای کمتری اشغال می‌کند", "correct": False},
                {"text": "utf8 فقط در MyISAM کار می‌کند", "correct": False},
            ],
        },
        {
            "text": "کاربری نام «علي» را با ی عربی وارد کرده و جست‌وجوی «علی» با ی فارسی آن را پیدا نمی‌کند. ریشه‌ی مشکل چیست؟",
            "explanation": "ی عربی (U+064A) و ی فارسی (U+06CC) دو کاراکتر یونیکد متفاوت‌اند؛ باید داده را هنگام ورود یکدست کرد (در برنامه یا با تریگر).",
            "choices": [
                {"text": "collation دیتابیس به حروف بزرگ و کوچک حساس است", "correct": False},
                {"text": "ایندکس جدول خراب شده است", "correct": False},
                {"text": "ی عربی و ی فارسی دو کد یونیکد متفاوت‌اند و باید هنگام ورود یکدست شوند", "correct": True},
                {"text": "MySQL حروف فارسی را با فاصله ذخیره می‌کند", "correct": False},
            ],
        },
        {
            "text": "دستور `SET PERSIST max_connections = 300;` چه تفاوتی با `SET GLOBAL` دارد؟",
            "explanation": "SET PERSIST علاوه بر اعمال فوری، مقدار را در فایل mysqld-auto.cnf داخل پوشه‌ی داده ذخیره می‌کند تا پس از ری‌استارت هم بماند؛ SET GLOBAL با ری‌استارت از بین می‌رود.",
            "choices": [
                {"text": "مقدار را اعمال و در mysqld-auto.cnf ذخیره می‌کند تا پس از ری‌استارت هم بماند", "correct": True},
                {"text": "فقط برای session فعلی اعمال می‌شود", "correct": False},
                {"text": "تا ری‌استارت بعدی اعمال نمی‌شود", "correct": False},
                {"text": "فایل my.cnf اصلی را ویرایش می‌کند", "correct": False},
            ],
        },
        {
            "text": "در MySQL 8 دستور `GRANT ALL ON shop.* TO 'app'@'localhost' IDENTIFIED BY 'x';` چه نتیجه‌ای دارد؟",
            "explanation": "از MySQL 8 دستور GRANT دیگر کاربر نمی‌سازد و عبارت IDENTIFIED BY در آن خطای نحوی است؛ ابتدا باید CREATE USER اجرا شود.",
            "choices": [
                {"text": "کاربر را می‌سازد و مجوز می‌دهد", "correct": False},
                {"text": "فقط رمز کاربر موجود را عوض می‌کند", "correct": False},
                {"text": "یک warning می‌دهد ولی اجرا می‌شود", "correct": False},
                {"text": "خطای نحوی می‌دهد؛ باید اول CREATE USER زد و بعد GRANT", "correct": True},
            ],
        },
        # ── فصل ۲
        {
            "text": "خروجی `SELECT * FROM customers WHERE city <> 'کاشان';` درباره‌ی مشتریانی که `city` آن‌ها NULL است چیست؟",
            "explanation": "مقایسه با NULL نتیجه‌ی UNKNOWN می‌دهد و WHERE فقط ردیف‌های TRUE را برمی‌گرداند؛ برای شامل کردن آن‌ها باید `OR city IS NULL` افزود.",
            "choices": [
                {"text": "در نتیجه می‌آیند چون NULL با کاشان برابر نیست", "correct": False},
                {"text": "در نتیجه نمی‌آیند، چون مقایسه با NULL نتیجه‌ی UNKNOWN دارد", "correct": True},
                {"text": "کوئری خطا می‌دهد", "correct": False},
                {"text": "فقط در حالت strict می‌آیند", "correct": False},
            ],
        },
        {
            "text": "ترتیب منطقی اجرای بندهای یک کوئری SELECT کدام است؟",
            "explanation": "منطقاً ابتدا FROM/JOIN، سپس WHERE، GROUP BY، HAVING، SELECT و در پایان ORDER BY و LIMIT اجرا می‌شوند؛ به همین دلیل alias تعریف‌شده در SELECT در WHERE قابل استفاده نیست.",
            "choices": [
                {"text": "SELECT، FROM، WHERE، ORDER BY", "correct": False},
                {"text": "FROM، SELECT، WHERE، GROUP BY", "correct": False},
                {"text": "FROM، WHERE، GROUP BY، HAVING، SELECT، ORDER BY، LIMIT", "correct": True},
                {"text": "WHERE، FROM، HAVING، SELECT", "correct": False},
            ],
        },
        {
            "text": "دام اصلی `REPLACE INTO` روی جدولی که ردیف‌هایش فرزند دارند (کلید خارجی با ON DELETE CASCADE) چیست؟",
            "explanation": "REPLACE در صورت تکرار کلید، ردیف قبلی را DELETE و ردیف تازه را INSERT می‌کند؛ پس فرزندان با CASCADE حذف می‌شوند و id هم ممکن است عوض شود. ON DUPLICATE KEY UPDATE این مشکل را ندارد.",
            "choices": [
                {"text": "ردیف قدیمی را حذف و دوباره درج می‌کند، پس فرزندان با CASCADE پاک می‌شوند", "correct": True},
                {"text": "روی جدول‌های InnoDB کار نمی‌کند", "correct": False},
                {"text": "همیشه خطای Duplicate entry می‌دهد", "correct": False},
                {"text": "فقط ستون‌های تغییرکرده را به‌روز می‌کند", "correct": False},
            ],
        },
        {
            "text": "با فعال بودن `sql_safe_updates`، کدام دستور رد می‌شود؟",
            "explanation": "safe updates دستور UPDATE یا DELETE بدون WHERE روی ستون کلیددار (یا بدون LIMIT) را رد می‌کند تا از تغییر ناخواسته‌ی کل جدول جلوگیری شود.",
            "choices": [
                {"text": "`SELECT * FROM orders;`", "correct": False},
                {"text": "`UPDATE orders SET status = 'paid' WHERE id = 10;`", "correct": False},
                {"text": "`INSERT INTO orders (customer_id) VALUES (5);`", "correct": False},
                {"text": "`DELETE FROM orders;`", "correct": True},
            ],
        },
        # ── فصل ۳
        {
            "text": "برای ذخیره‌ی مبلغ فاکتور به ریال کدام نوع داده مناسب است؟",
            "explanation": "FLOAT و DOUBLE تقریبی‌اند و در جمع‌ها خطای گرد کردن ایجاد می‌کنند؛ DECIMAL دقیق است و برای پول استاندارد است.",
            "choices": [
                {"text": "FLOAT", "correct": False},
                {"text": "DECIMAL با دقت کافی، مثل DECIMAL(15,0)", "correct": True},
                {"text": "VARCHAR", "correct": False},
                {"text": "DOUBLE", "correct": False},
            ],
        },
        {
            "text": "چرا کلید اصلی UUID تصادفی (نسخه‌ی ۴) در InnoDB برای جدول‌های بزرگ کندی درج ایجاد می‌کند؟",
            "explanation": "InnoDB داده را بر اساس کلید اصلی مرتب ذخیره می‌کند (Clustered Index)؛ مقادیر تصادفی باعث درج در وسط صفحه‌ها، شکستن صفحه و I/O تصادفی می‌شوند. AUTO_INCREMENT یا UUID ترتیبی این مشکل را ندارد.",
            "choices": [
                {"text": "چون UUID را نمی‌توان ایندکس کرد", "correct": False},
                {"text": "چون UUID همیشه تکراری تولید می‌شود", "correct": False},
                {"text": "چون داده بر اساس کلید اصلی مرتب ذخیره می‌شود و مقادیر تصادفی باعث شکستن صفحه و I/O تصادفی می‌شوند", "correct": True},
                {"text": "چون UUID فقط در MyISAM پشتیبانی می‌شود", "correct": False},
            ],
        },
        {
            "text": "تفاوت مهم `TIMESTAMP` با `DATETIME` در MySQL چیست؟",
            "explanation": "TIMESTAMP بر اساس منطقه‌ی زمانی session به UTC تبدیل و ذخیره می‌شود و بازه‌اش تا سال 2038 است؛ DATETIME همان مقدار نوشته‌شده را بدون تبدیل نگه می‌دارد.",
            "choices": [
                {"text": "TIMESTAMP به UTC تبدیل می‌شود و بازه‌اش تا 2038 است؛ DATETIME بدون تبدیل ذخیره می‌شود", "correct": True},
                {"text": "DATETIME ثانیه را ذخیره نمی‌کند", "correct": False},
                {"text": "TIMESTAMP فقط تاریخ را نگه می‌دارد", "correct": False},
                {"text": "هیچ تفاوتی جز نام ندارند", "correct": False},
            ],
        },
        {
            "text": "جدولی ستون‌های `customer_name` و `customer_city` را در هر ردیف سفارش تکرار کرده است. این طراحی کدام صورت نرمال را نقض می‌کند؟",
            "explanation": "شهر مشتری به مشتری وابسته است، نه به کلید سفارش؛ این وابستگی انتقالی نقض 3NF است و باعث ناهمخوانی در به‌روزرسانی می‌شود.",
            "choices": [
                {"text": "1NF، چون ستون‌ها چندمقداری‌اند", "correct": False},
                {"text": "هیچ صورت نرمالی را نقض نمی‌کند", "correct": False},
                {"text": "فقط BCNF را", "correct": False},
                {"text": "3NF، چون ویژگی‌های مشتری به‌طور انتقالی به کلید سفارش وابسته‌اند", "correct": True},
            ],
        },
        # ── فصل ۴
        {
            "text": "در MySQL که `FULL OUTER JOIN` ندارد، چگونه می‌توان آن را شبیه‌سازی کرد؟",
            "explanation": "با UNION یک LEFT JOIN و یک RIGHT JOIN (یا LEFT JOIN معکوس) همه‌ی ردیف‌های دو طرف به دست می‌آید؛ UNION تکراری‌ها را حذف می‌کند.",
            "choices": [
                {"text": "با CROSS JOIN", "correct": False},
                {"text": "با UNION یک LEFT JOIN و یک RIGHT JOIN", "correct": True},
                {"text": "با NATURAL JOIN", "correct": False},
                {"text": "با زیرکوئری در SELECT", "correct": False},
            ],
        },
        {
            "text": "کوئری `SELECT customer_id, city, SUM(total) FROM orders GROUP BY customer_id;` با `ONLY_FULL_GROUP_BY` خطا می‌دهد. چرا؟",
            "explanation": "ستون city نه در GROUP BY است، نه تجمیع شده و نه به‌طور تابعی به customer_id وابسته است؛ MySQL نمی‌داند از کدام ردیف گروه مقدار آن را برگرداند.",
            "choices": [
                {"text": "چون SUM روی DECIMAL مجاز نیست", "correct": False},
                {"text": "چون GROUP BY باید همیشه دو ستون داشته باشد", "correct": False},
                {"text": "چون city نه در GROUP BY است و نه تجمیع شده، پس مقدارش در گروه مبهم است", "correct": True},
                {"text": "چون customer_id ایندکس ندارد", "correct": False},
            ],
        },
        {
            "text": "برای نمایش درخت دسته‌بندی‌های فروشگاه (والد و فرزندان در عمق نامعلوم) کدام ابزار مناسب است؟",
            "explanation": "CTE بازگشتی (WITH RECURSIVE) از ریشه شروع می‌کند و در هر تکرار فرزندان سطح بعد را اضافه می‌کند تا عمق دلخواه.",
            "choices": [
                {"text": "WITH RECURSIVE", "correct": True},
                {"text": "چند LEFT JOIN با تعداد ثابت", "correct": False},
                {"text": "GROUP BY WITH ROLLUP", "correct": False},
                {"text": "FULLTEXT INDEX", "correct": False},
            ],
        },
        {
            "text": "تفاوت `RANK()` و `DENSE_RANK()` در رتبه‌بندی فروشندگان با فروش برابر چیست؟",
            "explanation": "هر دو به مقادیر برابر رتبه‌ی یکسان می‌دهند؛ RANK پس از تساوی شماره‌ها را جا می‌اندازد (1، 1، 3) و DENSE_RANK بدون شکاف ادامه می‌دهد (1، 1، 2).",
            "choices": [
                {"text": "RANK به برابرها رتبه‌ی متفاوت می‌دهد", "correct": False},
                {"text": "DENSE_RANK فقط روی اعداد صحیح کار می‌کند", "correct": False},
                {"text": "هیچ تفاوتی ندارند", "correct": False},
                {"text": "RANK پس از تساوی شکاف می‌اندازد (1، 1، 3) و DENSE_RANK نه (1، 1، 2)", "correct": True},
            ],
        },
        # ── فصل ۵
        {
            "text": "ایندکس ترکیبی `(status, created_at)` روی جدول سفارش‌ها داریم. کدام شرط نمی‌تواند از این ایندکس برای جست‌وجو استفاده کند؟",
            "explanation": "طبق قانون leftmost prefix، ایندکس ترکیبی از ستون اول قابل استفاده است؛ شرطی که فقط روی created_at باشد نمی‌تواند از این ایندکس برای seek استفاده کند.",
            "choices": [
                {"text": "`WHERE status = 'paid'`", "correct": False},
                {"text": "`WHERE created_at >= '2026-03-21'`", "correct": True},
                {"text": "`WHERE status = 'paid' AND created_at >= '2026-03-21'`", "correct": False},
                {"text": "`WHERE status IN ('paid', 'shipped')`", "correct": False},
            ],
        },
        {
            "text": "چرا شرط `WHERE YEAR(created_at) = 2026` با وجود ایندکس روی `created_at` کند است؟",
            "explanation": "اعمال تابع روی ستون باعث می‌شود MySQL نتواند از ترتیب ایندکس استفاده کند؛ شرط بازه‌ای `created_at >= '2026-01-01' AND created_at < '2027-01-01'` قابل استفاده با ایندکس است.",
            "choices": [
                {"text": "چون تابع YEAR در MySQL 8 منسوخ است", "correct": False},
                {"text": "چون ایندکس روی DATETIME ساخته نمی‌شود", "correct": False},
                {"text": "چون اعمال تابع روی ستون مانع استفاده از ایندکس می‌شود؛ باید شرط بازه‌ای نوشت", "correct": True},
                {"text": "چون عدد 2026 باید داخل کوتیشن باشد", "correct": False},
            ],
        },
        {
            "text": "تفاوت `EXPLAIN ANALYZE` با `EXPLAIN` چیست؟",
            "explanation": "EXPLAIN فقط برنامه‌ی تخمینی را نشان می‌دهد؛ EXPLAIN ANALYZE کوئری را واقعاً اجرا می‌کند و زمان و تعداد ردیف واقعی هر مرحله را کنار تخمین‌ها می‌آورد. روی UPDATE/DELETE باید مراقب بود.",
            "choices": [
                {"text": "کوئری را واقعاً اجرا می‌کند و زمان و ردیف‌های واقعی هر مرحله را نشان می‌دهد", "correct": True},
                {"text": "فقط ایندکس‌های پیشنهادی را چاپ می‌کند", "correct": False},
                {"text": "کوئری را اجرا نمی‌کند و فقط خروجی JSON می‌دهد", "correct": False},
                {"text": "فقط روی جدول‌های MyISAM کار می‌کند", "correct": False},
            ],
        },
        {
            "text": "برای جست‌وجوی FULLTEXT در متن فارسی که کلمات کوتاه و پیوسته دارد، کدام parser پیشنهاد شد؟",
            "explanation": "ngram parser متن را به قطعه‌های n کاراکتری می‌شکند و به جداسازی کلمه بر اساس فاصله و حداقل طول کلمه‌ی parser پیش‌فرض وابسته نیست.",
            "choices": [
                {"text": "parser پیش‌فرض با ft_min_word_len=1", "correct": False},
                {"text": "ngram parser", "correct": True},
                {"text": "MeCab parser", "correct": False},
                {"text": "FULLTEXT روی فارسی ممکن نیست", "correct": False},
            ],
        },
        # ── فصل ۶
        {
            "text": "در یک تراکنش باز، دستور `ALTER TABLE` اجرا می‌شود و سپس `ROLLBACK`. چه اتفاقی برای تغییرات قبل از ALTER می‌افتد؟",
            "explanation": "دستورهای DDL قبل از اجرا تراکنش باز را به‌طور ضمنی COMMIT می‌کنند؛ پس تغییرات قبلی ثبت شده‌اند و ROLLBACK اثری روی آن‌ها ندارد.",
            "choices": [
                {"text": "همه برمی‌گردند", "correct": False},
                {"text": "فقط ALTER برمی‌گردد", "correct": False},
                {"text": "خطای deadlock رخ می‌دهد", "correct": False},
                {"text": "ثبت شده‌اند، چون DDL تراکنش باز را به‌طور ضمنی COMMIT می‌کند", "correct": True},
            ],
        },
        {
            "text": "در سطح ایزوله‌سازی REPEATABLE READ، دو SELECT معمولی پشت‌سرهم در یک تراکنش چه می‌بینند؟",
            "explanation": "با MVCC، SELECT معمولی از snapshot گرفته‌شده در اولین خواندن تراکنش می‌خواند؛ پس تغییرات COMMIT‌شده‌ی دیگران در طول تراکنش دیده نمی‌شوند.",
            "choices": [
                {"text": "هر دو از یک snapshot سازگار می‌خوانند و تغییرات دیگران را نمی‌بینند", "correct": True},
                {"text": "دومی همیشه تغییرات COMMIT‌شده‌ی دیگران را می‌بیند", "correct": False},
                {"text": "هر دو تغییرات COMMIT‌نشده را هم می‌بینند", "correct": False},
                {"text": "دومی تا پایان تراکنش‌های دیگر منتظر می‌ماند", "correct": False},
            ],
        },
        {
            "text": "رایج‌ترین راه پیشگیری از deadlock بین دو تراکنش که چند ردیف را به‌روز می‌کنند کدام است؟",
            "explanation": "وقتی همه‌ی تراکنش‌ها ردیف‌ها را با ترتیب یکسان (مثلاً بر اساس id صعودی) قفل کنند، چرخه‌ی انتظار شکل نمی‌گیرد؛ همچنین تراکنش‌ها کوتاه باشند و برنامه برای deadlock تلاش مجدد داشته باشد.",
            "choices": [
                {"text": "خاموش کردن innodb_deadlock_detect", "correct": False},
                {"text": "قفل کردن ردیف‌ها با ترتیب یکسان در همه‌ی تراکنش‌ها و کوتاه نگه داشتن تراکنش", "correct": True},
                {"text": "افزایش innodb_lock_wait_timeout به یک ساعت", "correct": False},
                {"text": "استفاده از MyISAM", "correct": False},
            ],
        },
        {
            "text": "چرا `SELECT ... FOR UPDATE SKIP LOCKED` برای صف کار با چند worker مناسب است؟",
            "explanation": "SKIP LOCKED ردیف‌هایی را که worker دیگر قفل کرده نادیده می‌گیرد؛ پس workerها منتظر هم نمی‌مانند و هر کدام کار آزاد دیگری برمی‌دارد.",
            "choices": [
                {"text": "چون بدون تراکنش هم قفل نگه می‌دارد", "correct": False},
                {"text": "چون همه‌ی ردیف‌های جدول را قفل می‌کند", "correct": False},
                {"text": "چون ردیف‌های قفل‌شده توسط worker دیگر را رد می‌کند و workerها منتظر هم نمی‌مانند", "correct": True},
                {"text": "چون نتیجه‌ی آن برای گزارش موجودی دقیق است", "correct": False},
            ],
        },
        # ── فصل ۷
        {
            "text": "به کاربر `'web'@'10.0.0.%'` نقش `app_rw` داده‌اید، اما هنگام SELECT خطای command denied می‌گیرد. محتمل‌ترین علت چیست؟",
            "explanation": "نقش اعطاشده تا فعال نشود اثری ندارد؛ باید `SET DEFAULT ROLE ALL TO ...` اجرا شود یا `activate_all_roles_on_login` روشن باشد.",
            "choices": [
                {"text": "نقش‌ها فقط در MySQL Enterprise کار می‌کنند", "correct": False},
                {"text": "نقش فعال نشده است؛ SET DEFAULT ROLE فراموش شده", "correct": True},
                {"text": "کاربر باید ری‌استارت شود", "correct": False},
                {"text": "GRANT روی نقش‌ها فقط سراسری است", "correct": False},
            ],
        },
        {
            "text": "یک برنامه‌ی قدیمی که بدون TLS و با caching_sha2_password وصل می‌شد، پس از ری‌استارت سرور با `Authentication requires secure connection` قطع شد. چرا؟",
            "explanation": "caching_sha2 برای اولین ورود به کانال امن (TLS، سوکت یا کلید عمومی RSA) نیاز دارد و سپس چکیده را در حافظه cache می‌کند؛ با ری‌استارت cache خالی شده و ورود بدون کانال امن ممکن نیست.",
            "choices": [
                {"text": "چون رمز کاربر با ری‌استارت منقضی می‌شود", "correct": False},
                {"text": "چون ری‌استارت پلاگین را به mysql_native_password برمی‌گرداند", "correct": False},
                {"text": "چون max_connections پر شده است", "correct": False},
                {"text": "چون cache احراز هویت با ری‌استارت خالی شده و اولین ورود به کانال امن یا کلید RSA نیاز دارد", "correct": True},
            ],
        },
        {
            "text": "گزینه‌ی `--single-transaction` در mysqldump چه کاری انجام می‌دهد؟",
            "explanation": "یک تراکنش REPEATABLE READ با snapshot سازگار باز می‌کند و جدول‌های InnoDB را بدون قفل کردن می‌خواند؛ برای MyISAM سازگاری تضمین نمی‌شود.",
            "choices": [
                {"text": "از جدول‌های InnoDB بدون قفل کردن، یک snapshot سازگار می‌گیرد", "correct": True},
                {"text": "همه‌ی جدول‌ها را تا پایان بکاپ قفل می‌کند", "correct": False},
                {"text": "خروجی را در یک فایل واحد فشرده می‌کند", "correct": False},
                {"text": "فقط یک جدول را بکاپ می‌گیرد", "correct": False},
            ],
        },
        {
            "text": "برای بازیابی دیتابیس تا لحظه‌ی قبل از یک `DELETE` اشتباه در ساعت ۱۴:۳۷، چه چیزهایی لازم است؟",
            "explanation": "Point-in-Time Recovery یعنی بازیابی آخرین بکاپ کامل (با مختصات binlog آن) و سپس اجرای binlogها با mysqlbinlog تا موقعیت قبل از دستور مخرب.",
            "choices": [
                {"text": "فقط slow query log", "correct": False},
                {"text": "یک replica بدون تأخیر کافی است", "correct": False},
                {"text": "بکاپ کامل همراه مختصات binlog، و binlogهای بعد از آن تا قبل از دستور مخرب", "correct": True},
                {"text": "اجرای ROLLBACK روی سرور", "correct": False},
            ],
        },
        {
            "text": "چرا روی replica علاوه بر `read_only` باید `super_read_only` را هم روشن کرد؟",
            "explanation": "read_only کاربران دارای SUPER یا CONNECTION_ADMIN را محدود نمی‌کند؛ super_read_only جلوی نوشتن آن‌ها را هم می‌گیرد تا replica با source ناهمخوان نشود.",
            "choices": [
                {"text": "چون read_only در MySQL 8 حذف شده است", "correct": False},
                {"text": "چون read_only کاربران دارای SUPER را محدود نمی‌کند", "correct": True},
                {"text": "چون بدون آن replication شروع نمی‌شود", "correct": False},
                {"text": "چون super_read_only سرعت applier را بالا می‌برد", "correct": False},
            ],
        },
        {
            "text": "یک لاگ ممیزی با تریگر `AFTER DELETE` روی جدول `order_items` ساخته‌اید. وقتی سفارشی حذف و اقلامش با `ON DELETE CASCADE` پاک می‌شوند، چه ثبت می‌شود؟",
            "explanation": "در MySQL تغییراتی که با عمل‌های کلید خارجی (CASCADE) انجام می‌شوند تریگرها را فعال نمی‌کنند؛ پس حذف اقلام در لاگ ممیزی ثبت نمی‌شود.",
            "choices": [
                {"text": "برای هر قلم یک ردیف لاگ", "correct": False},
                {"text": "فقط یک ردیف برای کل سفارش", "correct": False},
                {"text": "خطا رخ می‌دهد و حذف انجام نمی‌شود", "correct": False},
                {"text": "هیچ؛ تریگرها برای حذف‌های ناشی از CASCADE اجرا نمی‌شوند", "correct": True},
            ],
        },
        # ── فصل ۸
        {
            "text": "روی سرور اختصاصی MySQL با ۱۶ گیگابایت RAM، مقدار معقول برای `innodb_buffer_pool_size` حدوداً چقدر است؟",
            "explanation": "قاعده‌ی سرانگشتی ۵۰ تا ۷۵ درصد RAM روی سرور اختصاصی است تا برای سیستم‌عامل و بافرهای هر اتصال جا بماند؛ پیش‌فرض ۱۲۸ مگابایت برای چنین سروری بسیار کم است.",
            "choices": [
                {"text": "همان ۱۲۸ مگابایت پیش‌فرض", "correct": False},
                {"text": "حدود ۱۱ تا ۱۲ گیگابایت", "correct": True},
                {"text": "۱۶ گیگابایت یعنی کل RAM", "correct": False},
                {"text": "۳۲ گیگابایت با تکیه بر swap", "correct": False},
            ],
        },
        {
            "text": "در `OPTIONS` جنگو مقدار `\"init_command\": \"SET sql_mode='STRICT_TRANS_TABLES'\"` گذاشته‌اید. اثر جانبی آن چیست؟",
            "explanation": "این دستور کل sql_mode را جایگزین می‌کند، پس حالت‌های پیش‌فرض دیگر مثل ONLY_FULL_GROUP_BY و NO_ZERO_DATE خاموش می‌شوند؛ باید فهرست کامل را نوشت.",
            "choices": [
                {"text": "هیچ؛ فقط STRICT به حالت‌های فعلی اضافه می‌شود", "correct": False},
                {"text": "charset اتصال به latin1 برمی‌گردد", "correct": False},
                {"text": "کل sql_mode جایگزین می‌شود و ONLY_FULL_GROUP_BY و حالت‌های دیگر خاموش می‌شوند", "correct": True},
                {"text": "تراکنش‌های جنگو غیرفعال می‌شوند", "correct": False},
            ],
        },
        {
            "text": "در SQLAlchemy چرا باید `pool_recycle` کمتر از `wait_timeout` سرور باشد؟",
            "explanation": "سرور اتصال‌های بی‌کار را پس از wait_timeout می‌بندد؛ اگر pool اتصال قدیمی‌تر را قرض دهد، درخواست با MySQL server has gone away شکست می‌خورد.",
            "choices": [
                {"text": "تا اتصال‌ها قبل از بسته شدن توسط سرور بازسازی شوند و خطای server has gone away رخ ندهد", "correct": True},
                {"text": "تا تعداد اتصال‌ها از max_connections بیشتر شود", "correct": False},
                {"text": "تا تراکنش‌ها سریع‌تر COMMIT شوند", "correct": False},
                {"text": "تا charset اتصال حفظ شود", "correct": False},
            ],
        },
        {
            "text": "در گزارش، عبارت `oi.qty - pr.made` روی ستون‌های `SMALLINT UNSIGNED` خطای `BIGINT UNSIGNED value is out of range` می‌دهد. راه درست چیست؟",
            "explanation": "تفریق مقادیر UNSIGNED با نتیجه‌ی منفی در MySQL خطای 1690 می‌دهد؛ تبدیل یکی از عملوندها به SIGNED (یا حالت NO_UNSIGNED_SUBTRACTION) مشکل را حل می‌کند.",
            "choices": [
                {"text": "تغییر ستون‌ها به FLOAT", "correct": False},
                {"text": "استفاده از ABS() روی نتیجه", "correct": False},
                {"text": "افزودن ORDER BY", "correct": False},
                {"text": "تبدیل یکی از عملوندها به SIGNED، مثل `CAST(oi.qty AS SIGNED) - pr.made`", "correct": True},
            ],
        },
        {
            "text": "خطای `ERROR 1452: Cannot add or update a child row: a foreign key constraint fails` هنگام وارد کردن داده چه معنایی دارد؟",
            "explanation": "ردیف فرزند به کلید والدی اشاره می‌کند که وجود ندارد (یتیم) یا ترتیب ورود داده غلط است؛ با LEFT JOIN و شرط IS NULL می‌توان یتیم‌ها را پیدا کرد.",
            "choices": [
                {"text": "ردیف والد مورد اشاره وجود ندارد یا ترتیب درج غلط است", "correct": True},
                {"text": "ستون فرزند ایندکس ندارد", "correct": False},
                {"text": "رمز کاربر اشتباه است", "correct": False},
                {"text": "اندازه‌ی بسته از max_allowed_packet بیشتر است", "correct": False},
            ],
        },
        {
            "text": "پس از خطای `Lock wait timeout exceeded` (ERROR 1205) با تنظیمات پیش‌فرض، وضعیت تراکنش چیست؟",
            "explanation": "به‌طور پیش‌فرض فقط همان دستور ROLLBACK می‌شود و تراکنش باز می‌ماند؛ برنامه باید خودش کل تراکنش را ROLLBACK کند، مگر innodb_rollback_on_timeout روشن باشد.",
            "choices": [
                {"text": "کل تراکنش خودکار ROLLBACK می‌شود", "correct": False},
                {"text": "اتصال قطع می‌شود", "correct": False},
                {"text": "فقط همان دستور برمی‌گردد و تراکنش باز می‌ماند؛ برنامه باید ROLLBACK کند", "correct": True},
                {"text": "تراکنش خودکار COMMIT می‌شود", "correct": False},
            ],
        },
    ],
}

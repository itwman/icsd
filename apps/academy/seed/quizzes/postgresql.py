# -*- coding: utf-8 -*-
# بانک 36 سؤالی آزمون دوره‌ی جامع PostgreSQL — هر نوبت ۲۰ سؤال تصادفی

QUIZ = {
    "course_slug": "postgresql",
    "title": "آزمون پایانی آموزش جامع PostgreSQL",
    "pass_percent": 70,
    "time_limit_minutes": 30,
    "questions_per_attempt": 20,
    "questions": [
        # ── فصل ۱
        {
            "text": "در فایل pg_hba.conf چند خط با یک اتصال منطبق‌اند. پستگرس کدام را اعمال می‌کند؟",
            "explanation": "pg_hba از بالا به پایین خوانده می‌شود و اولین خط منطبق تصمیم می‌گیرد؛ برای همین یک خط reject کلی در بالای فایل همه را می‌بندد.",
            "choices": [
                {"text": "اولین خط منطبق از بالای فایل", "correct": True},
                {"text": "سخت‌گیرانه‌ترین خط", "correct": False},
                {"text": "آخرین خط منطبق", "correct": False},
                {"text": "خطی که روش scram-sha-256 دارد", "correct": False},
            ],
        },
        {
            "text": "تنظیمی را در postgresql.conf تغییر داده‌اید و reload کرده‌اید، اما SHOW هنوز مقدار قدیمی را نشان می‌دهد و پارامتر نیاز به restart ندارد. محتمل‌ترین علت چیست؟",
            "explanation": "ALTER SYSTEM در postgresql.auto.conf می‌نویسد که بعد از postgresql.conf خوانده می‌شود و بر آن غلبه می‌کند.",
            "choices": [
                {"text": "reload فقط پارامترهای sighup را برای superuser اعمال می‌کند", "correct": False},
                {"text": "postgresql.conf فقط هنگام initdb خوانده می‌شود", "correct": False},
                {"text": "همان پارامتر قبلاً با ALTER SYSTEM در postgresql.auto.conf تنظیم شده است", "correct": True},
                {"text": "باید VACUUM اجرا شود", "correct": False},
            ],
        },
        {
            "text": "در دیتابیسی با collation نوع C، چرا «پرویز» بعد از «وحید» مرتب می‌شود؟",
            "explanation": "در collation نوع C مرتب‌سازی بر اساس کد یونیکد است و پ، چ، ژ و گ کدی بعد از حروف عربی دارند؛ ICU با fa-IR ترتیب الفبای فارسی را رعایت می‌کند.",
            "choices": [
                {"text": "چون encoding دیتابیس UTF8 نیست", "correct": False},
                {"text": "چون مرتب‌سازی بر اساس کد یونیکد است و «پ» کدی بزرگ‌تر از «و» دارد", "correct": True},
                {"text": "چون ORDER BY روی متن فارسی پشتیبانی نمی‌شود", "correct": False},
                {"text": "چون ستون از نوع varchar است نه text", "correct": False},
            ],
        },
        {
            "text": "روش احراز هویت peer در pg_hba.conf به چه معناست؟",
            "explanation": "peer فقط برای اتصال سوکت محلی است و نام کاربر سیستم‌عامل را با نام role مقایسه می‌کند؛ رمزی پرسیده نمی‌شود.",
            "choices": [
                {"text": "اتصال فقط از سرورهای replication پذیرفته می‌شود", "correct": False},
                {"text": "رمز با هش md5 بررسی می‌شود", "correct": False},
                {"text": "هر کاربری بدون رمز از شبکه وارد می‌شود", "correct": False},
                {"text": "نام کاربر سیستم‌عامل باید با نام role یکی باشد و فقط برای اتصال سوکت محلی است", "correct": True},
            ],
        },
        # ── فصل ۲
        {
            "text": "برای ذخیره‌ی مبلغ فاکتور به ریال کدام انتخاب درست است و چرا؟",
            "explanation": "float و real مقدار را تقریبی ذخیره می‌کنند و در جمع‌ها خطای گرد کردن می‌سازند؛ numeric (یا bigint برای ریال بدون اعشار) دقیق است.",
            "choices": [
                {"text": "numeric یا bigint، چون float مقدار را تقریبی ذخیره می‌کند", "correct": True},
                {"text": "double precision، چون سریع‌تر است", "correct": False},
                {"text": "money، چون واحد ریال را خودکار نمایش می‌دهد", "correct": False},
                {"text": "text، تا جداکننده‌ی هزارگان حفظ شود", "correct": False},
            ],
        },
        {
            "text": "درباره‌ی نوع timestamptz کدام جمله درست است؟",
            "explanation": "timestamptz منطقه‌ی زمانی را ذخیره نمی‌کند؛ لحظه را به UTC تبدیل و ذخیره می‌کند و هنگام نمایش به منطقه‌ی زمانی نشست برمی‌گرداند.",
            "choices": [
                {"text": "نام منطقه‌ی زمانی را کنار زمان ذخیره می‌کند", "correct": False},
                {"text": "همیشه به وقت تهران نمایش داده می‌شود", "correct": False},
                {"text": "لحظه‌ی مطلق را (به UTC) ذخیره می‌کند و هنگام نمایش به منطقه‌ی زمانی نشست تبدیل می‌کند", "correct": True},
                {"text": "دو برابر timestamp فضا می‌گیرد چون منطقه را هم نگه می‌دارد", "correct": False},
            ],
        },
        {
            "text": "در `INSERT ... ON CONFLICT (code) DO UPDATE SET price = ...` برای دسترسی به مقدار ردیفی که قصد درجش را داشتیم از چه چیزی استفاده می‌شود؟",
            "explanation": "شبه‌جدول EXCLUDED ردیف پیشنهادی برای درج را نگه می‌دارد؛ مثلاً `SET price = EXCLUDED.price`.",
            "choices": [
                {"text": "`NEW.price`", "correct": False},
                {"text": "`EXCLUDED.price`", "correct": True},
                {"text": "`INSERTED.price`", "correct": False},
                {"text": "`VALUES(price)`", "correct": False},
            ],
        },
        {
            "text": "ستون `id bigint GENERATED ALWAYS AS IDENTITY` در برابر serial چه رفتاری دارد؟",
            "explanation": "با GENERATED ALWAYS درج مقدار صریح خطا می‌دهد مگر با OVERRIDING SYSTEM VALUE؛ همین جلوی ناهماهنگی sequence را می‌گیرد.",
            "choices": [
                {"text": "مقدار id را بعد از هر DELETE دوباره استفاده می‌کند", "correct": False},
                {"text": "فقط با نوع uuid کار می‌کند", "correct": False},
                {"text": "هیچ sequenceی پشتش نیست و id را با max(id)+1 می‌سازد", "correct": False},
                {"text": "درج مقدار صریح برای id خطا می‌دهد مگر با `OVERRIDING SYSTEM VALUE`", "correct": True},
            ],
        },
        # ── فصل ۳
        {
            "text": "روی ستون `orders.customer_id` یک FOREIGN KEY تعریف کرده‌اید. کدام جمله درست است؟",
            "explanation": "پستگرس برای ستون ارجاع‌دهنده ایندکس خودکار نمی‌سازد؛ بدون آن JOINها و DELETE والد (برای بررسی فرزندها) کند می‌شوند.",
            "choices": [
                {"text": "ایندکس روی customer_id خودکار ساخته نمی‌شود و معمولاً باید دستی بسازید", "correct": True},
                {"text": "پستگرس روی customer_id خودکار ایندکس B-tree می‌سازد", "correct": False},
                {"text": "FK فقط وقتی کار می‌کند که customer_id ایندکس UNIQUE داشته باشد", "correct": False},
                {"text": "FK در پستگرس فقط هنگام INSERT بررسی می‌شود", "correct": False},
            ],
        },
        {
            "text": "برای اینکه دو رزرو یک دستگاه بافندگی در زمان هم‌پوشانی نداشته باشند، کدام راه در خود دیتابیس تضمین قطعی می‌دهد؟",
            "explanation": "قید EXCLUDE با GiST و btree_gist برای عملگر = روی loom_id و && روی بازه، هم‌پوشانی را حتی با درج‌های هم‌زمان رد می‌کند.",
            "choices": [
                {"text": "یک UNIQUE روی (loom_id, during)", "correct": False},
                {"text": "یک CHECK که با زیرکوئری هم‌پوشانی را بررسی کند", "correct": False},
                {"text": "`EXCLUDE USING gist (loom_id WITH =, during WITH &&)` با اکستنشن btree_gist", "correct": True},
                {"text": "بررسی در برنامه با SELECT قبل از INSERT", "correct": False},
            ],
        },
        {
            "text": "افزودن FOREIGN KEY به جدولی با ده‌ها میلیون ردیف بدون قفل طولانی چگونه انجام می‌شود؟",
            "explanation": "با NOT VALID قید فوراً برای داده‌های جدید فعال می‌شود و بررسی داده‌های قدیمی بعداً با VALIDATE CONSTRAINT و قفل سبک‌تر انجام می‌شود.",
            "choices": [
                {"text": "با `DEFERRABLE INITIALLY DEFERRED`", "correct": False},
                {"text": "ابتدا قید را با `NOT VALID` اضافه کنید و بعد `VALIDATE CONSTRAINT` بزنید", "correct": True},
                {"text": "با `CREATE INDEX CONCURRENTLY` روی ستون FK", "correct": False},
                {"text": "ممکن نیست؛ باید جدول را بازسازی کرد", "correct": False},
            ],
        },
        # ── فصل ۴
        {
            "text": "کوئری `SELECT * FROM designs WHERE code NOT IN (SELECT design_code FROM order_items)` هیچ ردیفی برنمی‌گرداند، در حالی که نقشه‌ی بی‌سفارش وجود دارد. علت چیست؟",
            "explanation": "اگر زیرکوئری NOT IN حتی یک NULL داشته باشد، نتیجه‌ی شرط برای همه NULL می‌شود؛ برای anti-join از NOT EXISTS استفاده کنید.",
            "choices": [
                {"text": "زیرکوئری دست‌کم یک NULL برمی‌گرداند و NOT IN را برای همه‌ی ردیف‌ها NULL می‌کند", "correct": True},
                {"text": "NOT IN فقط روی ستون‌های عددی کار می‌کند", "correct": False},
                {"text": "زیرکوئری بدون DISTINCT در NOT IN مجاز نیست", "correct": False},
                {"text": "باید از LEFT JOIN با شرط در WHERE استفاده کرد", "correct": False},
            ],
        },
        {
            "text": "برای «سه سفارش آخر هر مشتری» کدام ساختار، به همراه ایندکس `(customer_id, created_at DESC)`، کارآمدترین است؟",
            "explanation": "LATERAL اجازه می‌دهد زیرکوئری به ردیف بیرونی ارجاع دهد و برای هر مشتری فقط سه ورودی ایندکس را بخواند.",
            "choices": [
                {"text": "`GROUP BY customer_id HAVING count(*) <= 3`", "correct": False},
                {"text": "`SELECT DISTINCT customer_id ... LIMIT 3`", "correct": False},
                {"text": "یک CTE بازگشتی روی orders", "correct": False},
                {"text": "`CROSS JOIN LATERAL (SELECT ... WHERE o.customer_id = c.id ORDER BY created_at DESC LIMIT 3)`", "correct": True},
            ],
        },
        {
            "text": "شرط `REFRESH MATERIALIZED VIEW CONCURRENTLY` چیست؟",
            "explanation": "نسخه‌ی CONCURRENTLY تفاوت‌ها را اعمال می‌کند و برای تطبیق ردیف‌ها به یک ایندکس UNIQUE ساده (بدون WHERE) روی materialized view نیاز دارد.",
            "choices": [
                {"text": "materialized view باید WITH NO DATA ساخته شده باشد", "correct": False},
                {"text": "فقط superuser می‌تواند اجرایش کند", "correct": False},
                {"text": "materialized view باید یک ایندکس UNIQUE روی ستون‌های ساده و بدون WHERE داشته باشد", "correct": True},
                {"text": "جدول‌های پایه باید partition شده باشند", "correct": False},
            ],
        },
        {
            "text": "در گزارش LEFT JOIN مشتری‌ها با سفارش‌ها، مشتری بدون سفارش با تعداد ۱ نمایش داده می‌شود. اصلاح درست کدام است؟",
            "explanation": "count(*) ردیف حاصل از LEFT JOIN را می‌شمارد حتی اگر سمت راست NULL باشد؛ count(o.id) مقدارهای NULL را نمی‌شمارد.",
            "choices": [
                {"text": "LEFT JOIN را به FULL JOIN تبدیل کنید", "correct": False},
                {"text": "به‌جای `count(*)` از `count(o.id)` استفاده کنید", "correct": True},
                {"text": "شرط `o.id IS NOT NULL` را در WHERE بگذارید", "correct": False},
                {"text": "از `count(DISTINCT c.id)` استفاده کنید", "correct": False},
            ],
        },
        # ── فصل ۵
        {
            "text": "ایندکس `(customer_id, created_at)` وجود دارد. در PostgreSQL 16 برای کوئری `WHERE created_at >= '2026-03-21'` (بدون شرط روی customer_id) چه انتظاری دارید؟",
            "explanation": "B-tree ترکیبی ابتدا بر اساس ستون اول مرتب است؛ بدون شرط روی آن، ایندکس برای بازه‌ی ستون دوم کارآمد نیست (skip scan از نسخه‌ی 18 آمده).",
            "choices": [
                {"text": "این ایندکس برای این شرط کارآمد نیست؛ ستون اول ایندکس در شرط نیامده", "correct": True},
                {"text": "ایندکس دقیقاً به همان سرعت ایندکس تک‌ستونی created_at استفاده می‌شود", "correct": False},
                {"text": "پستگرس خودکار یک ایندکس موقت روی created_at می‌سازد", "correct": False},
                {"text": "کوئری خطا می‌دهد چون ستون اول ایندکس در شرط نیست", "correct": False},
            ],
        },
        {
            "text": "چرا `CREATE INDEX ON orders ((created_at::date))` روی ستون timestamptz خطا می‌دهد؟",
            "explanation": "تبدیل timestamptz به date به منطقه‌ی زمانی نشست وابسته است و IMMUTABLE نیست؛ نسخه‌ی `(created_at AT TIME ZONE 'Asia/Tehran')::date` با منطقه‌ی ثابت قابل ایندکس است.",
            "choices": [
                {"text": "چون expression index فقط برای ستون‌های متنی مجاز است", "correct": False},
                {"text": "چون نوع date قابل ایندکس B-tree نیست", "correct": False},
                {"text": "چون پرانتز دوتایی در CREATE INDEX مجاز نیست", "correct": False},
                {"text": "چون این تبدیل به منطقه‌ی زمانی نشست وابسته است و تابع IMMUTABLE نیست", "correct": True},
            ],
        },
        {
            "text": "روی ستون jsonb به نام defects ایندکس GIN دارید، اما کوئری `WHERE defects->>'رج_کشی' = '2'` از آن استفاده نمی‌کند. بهترین اصلاح کدام است؟",
            "explanation": "GIN برای عملگرهای شمولی مثل @> ساخته شده است؛ عبارت ->> با = را فقط یک expression index از نوع B-tree پشتیبانی می‌کند.",
            "choices": [
                {"text": "ANALYZE بزنید تا GIN استفاده شود", "correct": False},
                {"text": "کوئری را به `defects @> '{\"رج_کشی\": 2}'` تغییر دهید", "correct": True},
                {"text": "ایندکس را از نوع BRIN بسازید", "correct": False},
                {"text": "jsonb را به json تغییر دهید", "correct": False},
            ],
        },
        {
            "text": "در خروجی EXPLAIN ANALYZE یک گره‌ی Index Scan با `actual time=0.040..0.050 rows=1 loops=200000` دیده می‌شود. زمان کل صرف‌شده در این گره تقریباً چقدر است؟",
            "explanation": "عددهای actual برای هر بار اجرای گره‌اند و باید در loops ضرب شوند: 0.05ms × 200000 ≈ 10 ثانیه.",
            "choices": [
                {"text": "حدود ۰.۰۵ میلی‌ثانیه", "correct": False},
                {"text": "حدود ۲۰۰ میلی‌ثانیه", "correct": False},
                {"text": "حدود ۱۰ ثانیه", "correct": True},
                {"text": "قابل محاسبه نیست چون loops زمان را نشان نمی‌دهد", "correct": False},
            ],
        },
        {
            "text": "کدام ابزار نشان می‌دهد کدام کوئری‌ها در مجموع بیشترین زمان سرور را مصرف کرده‌اند، حتی اگر هر اجرایشان سریع باشد؟",
            "explanation": "pg_stat_statements کوئری‌ها را با پارامتر نرمال‌شده جمع می‌زند و ستون total_exec_time هزینه‌ی تجمعی را نشان می‌دهد.",
            "choices": [
                {"text": "اکستنشن pg_stat_statements و مرتب‌سازی بر اساس total_exec_time", "correct": True},
                {"text": "دستور `EXPLAIN (ANALYZE, BUFFERS)`", "correct": False},
                {"text": "نمای pg_locks", "correct": False},
                {"text": "ستون n_dead_tup در pg_stat_user_tables", "correct": False},
            ],
        },
        {
            "text": "روی دیتابیسی، `SELECT show_trgm('فرش')` آرایه‌ی خالی برمی‌گرداند. معنای این نتیجه چیست؟",
            "explanation": "pg_trgm حروف را با LC_CTYPE دیتابیس تشخیص می‌دهد؛ با ctype برابر C حروف فارسی «حرف» محسوب نمی‌شوند و trigramی ساخته نمی‌شود.",
            "choices": [
                {"text": "کلمه‌ی «فرش» کمتر از سه حرف دارد", "correct": False},
                {"text": "اکستنشن pg_trgm نصب نشده است", "correct": False},
                {"text": "باید اول ایندکس gin_trgm_ops ساخته شود", "correct": False},
                {"text": "LC_CTYPE دیتابیس C است و pg_trgm حروف فارسی را حرف به حساب نمی‌آورد", "correct": True},
            ],
        },
        # ── فصل ۶
        {
            "text": "پس از یک UPDATE روی یک ردیف در PostgreSQL، روی دیسک چه اتفاقی می‌افتد؟",
            "explanation": "در MVCC، UPDATE نسخه‌ی جدیدی می‌نویسد و نسخه‌ی قبلی را با xmax منقضی می‌کند؛ نسخه‌ی قدیمی tuple مرده است تا VACUUM آن را پاک کند.",
            "choices": [
                {"text": "نسخه‌ی جدیدی از ردیف نوشته می‌شود و نسخه‌ی قبلی به tuple مرده تبدیل می‌شود", "correct": True},
                {"text": "ردیف درجا بازنویسی می‌شود", "correct": False},
                {"text": "نسخه‌ی قدیمی بلافاصله در COMMIT پاک می‌شود", "correct": False},
                {"text": "تغییر فقط در WAL ثبت می‌شود و فایل داده تغییر نمی‌کند", "correct": False},
            ],
        },
        {
            "text": "در تراکنش SERIALIZABLE خطای SQLSTATE 40001 گرفته‌اید. برخورد درست برنامه چیست؟",
            "explanation": "خطای serialization بخشی از کار عادی سطح Serializable است؛ کل تراکنش باید از ابتدا دوباره اجرا شود، ترجیحاً با backoff.",
            "choices": [
                {"text": "فقط دستور آخر را دوباره بفرستد", "correct": False},
                {"text": "سطح ایزوله‌سازی را برای همان تراکنش به Read Uncommitted تغییر دهد", "correct": False},
                {"text": "COMMIT را دوباره بفرستد", "correct": False},
                {"text": "کل تراکنش را از ابتدا دوباره اجرا کند", "correct": True},
            ],
        },
        {
            "text": "دو فروشنده هم‌زمان آخرین فرش موجود را می‌فروشند و موجودی منفی یا دوبار فروخته می‌شود. ساده‌ترین درمان در Read Committed کدام است؟",
            "explanation": "UPDATE اتمی با شرط در WHERE روی نسخه‌ی تازه‌ی ردیف دوباره ارزیابی می‌شود؛ اگر صفر ردیف برگشت، موجودی کافی نبوده است.",
            "choices": [
                {"text": "`UPDATE stock SET qty = qty - 1 WHERE ... AND qty >= 1 RETURNING qty`", "correct": True},
                {"text": "خواندن موجودی با SELECT ساده و سپس UPDATE با مقدار محاسبه‌شده در برنامه", "correct": False},
                {"text": "افزودن ایندکس روی qty", "correct": False},
                {"text": "اجرای VACUUM پیش از هر فروش", "correct": False},
            ],
        },
        {
            "text": "چند worker باید کارهای pending را از یک جدول برداشته و هیچ کاری دو بار انجام نشود، بی‌آن‌که workerها منتظر هم بمانند. کدام الگو مناسب است؟",
            "explanation": "FOR UPDATE SKIP LOCKED ردیف‌های قفل‌شده توسط workerهای دیگر را رد می‌کند و ردیف آزاد بعدی را برمی‌دارد.",
            "choices": [
                {"text": "`SELECT ... FOR SHARE`", "correct": False},
                {"text": "`SELECT ... LIMIT 1 FOR UPDATE SKIP LOCKED` و سپس تغییر status در همان تراکنش", "correct": True},
                {"text": "`LOCK TABLE jobs IN ACCESS EXCLUSIVE MODE`", "correct": False},
                {"text": "`SELECT ... FOR UPDATE NOWAIT` در یک حلقه‌ی بی‌پایان", "correct": False},
            ],
        },
        {
            "text": "یک `ALTER TABLE orders ADD COLUMN note text` ساده باعث شد چند دقیقه هیچ صفحه‌ای از سایت باز نشود. علت و پیشگیری چیست؟",
            "explanation": "ALTER منتظر قفل ACCESS EXCLUSIVE پشت یک کوئری طولانی می‌ماند و همه‌ی کوئری‌های بعدی پشت آن در صف قرار می‌گیرند؛ lock_timeout کوتاه این را محدود می‌کند.",
            "choices": [
                {"text": "افزودن ستون همیشه کل جدول را بازنویسی می‌کند؛ باید VACUUM FULL زد", "correct": False},
                {"text": "ستون text نیاز به TOAST دارد و دیسک را پر کرد", "correct": False},
                {"text": "ALTER پشت یک کوئری طولانی در صف قفل ماند و بقیه پشت آن صف کشیدند؛ در migration از `lock_timeout` کوتاه استفاده کنید", "correct": True},
                {"text": "autovacuum همزمان اجرا شده بود و باید خاموش شود", "correct": False},
            ],
        },
        # ── فصل ۷
        {
            "text": "پس از اجرای `ALTER DEFAULT PRIVILEGES IN SCHEMA factory GRANT SELECT ON TABLES TO carpet_ro` (با کاربر admin)، جدولی که migrator می‌سازد برای carpet_ro قابل خواندن نیست. چرا؟",
            "explanation": "DEFAULT PRIVILEGES فقط برای اشیایی اعمال می‌شود که role مشخص‌شده (بدون FOR ROLE، همان کسی که دستور را اجرا کرده) می‌سازد؛ باید `FOR ROLE migrator` یا نقش مالک را مشخص کرد.",
            "choices": [
                {"text": "DEFAULT PRIVILEGES فقط پس از restart اعمال می‌شود", "correct": False},
                {"text": "DEFAULT PRIVILEGES فقط روی schema public کار می‌کند", "correct": False},
                {"text": "carpet_ro باید LOGIN داشته باشد", "correct": False},
                {"text": "پیش‌فرض‌ها فقط برای اشیای ساخته‌شده توسط همان نقشی است که دستور را اجرا کرده؛ باید `FOR ROLE` نقش سازنده را بدهید", "correct": True},
            ],
        },
        {
            "text": "RLS روی جدول orders فعال است و policy دارد، اما مالک جدول همه‌ی ردیف‌ها را می‌بیند. چرا؟",
            "explanation": "مالک جدول (مانند superuser و نقش‌های BYPASSRLS) به‌طور پیش‌فرض مشمول RLS نیست، مگر با ALTER TABLE ... FORCE ROW LEVEL SECURITY.",
            "choices": [
                {"text": "مالک جدول مشمول RLS نیست مگر `FORCE ROW LEVEL SECURITY` فعال شود", "correct": True},
                {"text": "RLS فقط روی SELECT اعمال نمی‌شود", "correct": False},
                {"text": "policy بدون WITH CHECK غیرفعال است", "correct": False},
                {"text": "RLS فقط برای اتصال‌های SSL اعمال می‌شود", "correct": False},
            ],
        },
        {
            "text": "سرور را با `pg_dump -Fc` بکاپ گرفته‌اید و روی سرور تازه restore می‌کنید؛ خطاهای «role does not exist» می‌گیرید. چه چیزی را فراموش کرده‌اید؟",
            "explanation": "pg_dump فقط یک دیتابیس را خروجی می‌گیرد؛ roleها، رمزها و tablespaceها با pg_dumpall --globals-only جدا گرفته می‌شوند.",
            "choices": [
                {"text": "گزینه‌ی `-j 4` در pg_restore", "correct": False},
                {"text": "قالب directory به‌جای custom", "correct": False},
                {"text": "بکاپ roleها با `pg_dumpall --globals-only` و بازگردانی آن پیش از pg_restore", "correct": True},
                {"text": "اجرای ANALYZE پیش از restore", "correct": False},
            ],
        },
        {
            "text": "برای بازگرداندن دیتابیس به ساعت ۱۴:۲۹ امروز (یک دقیقه پیش از یک DELETE اشتباه) چه چیزهایی لازم است؟",
            "explanation": "PITR به یک بکاپ فیزیکی پایه (مثلاً pg_basebackup) و آرشیو پیوسته‌ی WAL از آن زمان تا لحظه‌ی هدف نیاز دارد؛ pg_dump این امکان را ندارد.",
            "choices": [
                {"text": "بکاپ شبانه‌ی pg_dump به‌تنهایی", "correct": False},
                {"text": "یک بکاپ فیزیکی پایه و آرشیو پیوسته‌ی فایل‌های WAL پس از آن", "correct": True},
                {"text": "یک standby با Logical Replication", "correct": False},
                {"text": "فقط فایل‌های پوشه‌ی pg_wal سرور فعلی", "correct": False},
            ],
        },
        {
            "text": "پشت PgBouncer با `pool_mode = transaction`، برنامه با `SET app.branch_id = '3'` شناسه‌ی نمایندگی را برای RLS تنظیم می‌کند و گاهی داده‌ی نمایندگی دیگری را می‌بیند. اصلاح درست کدام است؟",
            "explanation": "در transaction pooling هر تراکنش ممکن است روی اتصال سرور دیگری اجرا شود؛ SET LOCAL داخل همان تراکنش مقدار را محدود به آن تراکنش می‌کند.",
            "choices": [
                {"text": "pool_mode را به statement تغییر دهید", "correct": False},
                {"text": "max_client_conn را افزایش دهید", "correct": False},
                {"text": "SET را دو بار پشت سر هم اجرا کنید", "correct": False},
                {"text": "از `SET LOCAL` داخل همان تراکنش استفاده کنید", "correct": True},
            ],
        },
        # ── فصل ۸
        {
            "text": "روی جدول partition‌شده بر اساس recorded_at، تعریف `id bigint PRIMARY KEY` خطا می‌دهد. چرا؟",
            "explanation": "کلید اصلی و قید UNIQUE روی جدول partition‌شده باید ستون (یا ستون‌های) کلید پارتیشن را شامل شوند، چون یکتایی فقط درون هر پارتیشن تضمین می‌شود.",
            "choices": [
                {"text": "جدول partition‌شده اصلاً کلید اصلی نمی‌پذیرد", "correct": False},
                {"text": "bigint برای کلید partition مجاز نیست", "correct": False},
                {"text": "کلید اصلی باید ستون پارتیشن (recorded_at) را هم شامل شود", "correct": True},
                {"text": "باید ابتدا پارتیشن DEFAULT ساخته شود", "correct": False},
            ],
        },
        {
            "text": "تابع trigger با `pg_notify('order_status', ...)` پیامی می‌فرستد، اما تراکنش در انتها ROLLBACK می‌شود. شنونده چه دریافت می‌کند؟",
            "explanation": "پیام‌های NOTIFY فقط پس از COMMIT موفق تحویل می‌شوند؛ با ROLLBACK هیچ پیامی ارسال نمی‌شود.",
            "choices": [
                {"text": "پیام بلافاصله و پیش از ROLLBACK تحویل شده است", "correct": False},
                {"text": "هیچ پیامی؛ NOTIFY فقط پس از COMMIT تحویل می‌شود", "correct": True},
                {"text": "پیامی با محتوای خالی", "correct": False},
                {"text": "پیام پس از restart سرور تحویل می‌شود", "correct": False},
            ],
        },
        {
            "text": "پس از بازگردانی داده با idهای صریح، INSERT جدید خطای `duplicate key value violates unique constraint \"orders_pkey\"` می‌دهد. درمان کدام است؟",
            "explanation": "sequence از max(id) عقب مانده است؛ با setval روی pg_get_serial_sequence آن را جلو می‌برید.",
            "choices": [
                {"text": "`REINDEX TABLE factory.orders`", "correct": False},
                {"text": "`VACUUM FULL factory.orders`", "correct": False},
                {"text": "حذف قید کلید اصلی و ساخت دوباره‌ی آن", "correct": False},
                {"text": "`SELECT setval(pg_get_serial_sequence('factory.orders','id'), coalesce(max(id),0)+1, false) FROM factory.orders`", "correct": True},
            ],
        },
        {
            "text": "در PostgreSQL 15 به بعد، migration جنگو با کاربر تازه‌ساخته خطای `permission denied for schema public` می‌دهد. علت چیست؟",
            "explanation": "از نسخه‌ی 15 مجوز CREATE روی schema public از PUBLIC گرفته شده و public متعلق به pg_database_owner است؛ schema اختصاصی، مالکیت دیتابیس یا GRANT CREATE صریح لازم است.",
            "choices": [
                {"text": "از نسخه‌ی 15 مجوز CREATE روی schema public دیگر به همه داده نمی‌شود", "correct": True},
                {"text": "schema public در نسخه‌ی 15 حذف شده است", "correct": False},
                {"text": "رمز کاربر با md5 هش شده است", "correct": False},
                {"text": "CONN_MAX_AGE در جنگو صفر است", "correct": False},
            ],
        },
        {
            "text": "دیسک سرور اصلی با فایل‌های پوشه‌ی pg_wal پر شده است. کدام اقدام درست است؟",
            "explanation": "علت معمولاً replication slot رهاشده یا archive_command شکست‌خورده است؛ با رفع علت، پستگرس WAL اضافه را خودش پاک می‌کند. حذف دستی pg_wal دیتابیس را خراب می‌کند.",
            "choices": [
                {"text": "حذف دستی قدیمی‌ترین فایل‌های pg_wal", "correct": False},
                {"text": "بررسی pg_replication_slots و pg_stat_archiver و رفع علت (مثلاً حذف slot رهاشده)", "correct": True},
                {"text": "اجرای VACUUM FULL روی بزرگ‌ترین جدول", "correct": False},
                {"text": "خاموش کردن autovacuum", "correct": False},
            ],
        },
    ],
}

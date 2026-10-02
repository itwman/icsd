# -*- coding: utf-8 -*-

QUIZ = {
    "course_slug": 'sql-server',
    "title": 'آزمون پایانی SQL Server',
    "pass_percent": 70,
    "time_limit_minutes": 20,
    "questions": [
        {
            "text": 'ابزار اصلی مدیریت گرافیکی SQL Server در ویندوز، که امکان اتصال، اجرای کوئری و مدیریت کاربران را می\u200cدهد، چه نام دارد؟',
            "explanation": 'SSMS (SQL Server Management Studio) ابزار رسمی مایکروسافت برای مدیریت گرافیکی SQL Server است.',
            "choices": [
                {"text": 'SSMS (SQL Server Management Studio)', "correct": True},
                {"text": 'psql', "correct": False},
                {"text": 'phpMyAdmin', "correct": False},
                {"text": 'pgAdmin', "correct": False},
            ],
        },
        {
            "text": 'در T-SQL، برای محدود کردن تعداد ردیف\u200cهای بازگشتی یک کوئری، به\u200cجای LIMIT از چه کلیدواژه\u200cای استفاده می\u200cشود؟',
            "explanation": 'T-SQL به\u200cجای LIMIT از کلیدواژه\u200cی TOP برای محدود کردن تعداد نتایج استفاده می\u200cکند.',
            "choices": [
                {"text": 'LIMIT', "correct": False},
                {"text": 'TOP', "correct": True},
                {"text": 'FIRST', "correct": False},
                {"text": 'ROWCOUNT ONLY', "correct": False},
            ],
        },
        {
            "text": "پیشوند N قبل از یک رشته در T-SQL (مانند N'لپ\u200cتاپ') برای چه منظوری استفاده می\u200cشود؟",
            "explanation": 'پیشوند N برای ذخیره\u200cی صحیح متن یونیکد مانند فارسی در ستون\u200cهای NVARCHAR ضروری است.',
            "choices": [
                {"text": 'ذخیره\u200cی صحیح متن یونیکد مانند فارسی', "correct": True},
                {"text": 'علامت\u200cگذاری مقدار به\u200cعنوان null', "correct": False},
                {"text": 'تعریف یک نوع داده\u200cی عددی', "correct": False},
                {"text": 'غیرفعال کردن اعتبارسنجی ورودی', "correct": False},
            ],
        },
        {
            "text": 'برای تعریف یک کلید اصلی خودافزا در جدول SQL Server از کدام ویژگی استفاده می\u200cشود؟',
            "explanation": 'IDENTITY(1,1) شمارنده\u200cای خودافزا می\u200cسازد که از عدد ۱ شروع و هر بار ۱ واحد افزایش می\u200cیابد.',
            "choices": [
                {"text": 'IDENTITY(1,1)', "correct": True},
                {"text": 'AUTO_INCREMENT', "correct": False},
                {"text": 'SERIAL', "correct": False},
                {"text": 'BIGSERIAL', "correct": False},
            ],
        },
        {
            "text": 'چرا برای ذخیره\u200cی متن فارسی در SQL Server باید از NVARCHAR به\u200cجای VARCHAR استفاده کرد؟',
            "explanation": 'NVARCHAR از یونیکد پشتیبانی می\u200cکند، در حالی که VARCHAR فقط کاراکترهای صفحه\u200cکد محلی را به\u200cدرستی ذخیره می\u200cکند.',
            "choices": [
                {"text": 'NVARCHAR از یونیکد پشتیبانی می\u200cکند و VARCHAR فقط صفحه\u200cکد محلی را ذخیره می\u200cکند', "correct": True},
                {"text": 'NVARCHAR فقط از نظر سرعت با VARCHAR تفاوت دارد', "correct": False},
                {"text": 'VARCHAR فقط برای ذخیره\u200cی مقادیر عددی است', "correct": False},
                {"text": 'این دو نوع هیچ تفاوتی با هم ندارند', "correct": False},
            ],
        },
        {
            "text": 'CTE یا Common Table Expression در T-SQL با کدام کلیدواژه تعریف می\u200cشود؟',
            "explanation": 'CTE با کلیدواژه\u200cی WITH تعریف می\u200cشود و یک نتیجه\u200cی موقت برای استفاده در ادامه\u200cی همان کوئری می\u200cسازد.',
            "choices": [
                {"text": 'USING', "correct": False},
                {"text": 'DEFINE', "correct": False},
                {"text": 'TEMP', "correct": False},
                {"text": 'WITH', "correct": True},
            ],
        },
        {
            "text": 'Recursive CTE معمولاً برای پیمایش چه نوع ساختاری در دیتابیس کاربرد دارد؟',
            "explanation": 'Recursive CTE برای پیمایش ساختارهای درختی مانند دسته\u200cبندی\u200cهای تودرتو (parent-child) استفاده می\u200cشود.',
            "choices": [
                {"text": 'ساختارهای درختی مانند دسته\u200cبندی\u200cهای تودرتو', "correct": True},
                {"text": 'جدول\u200cهای تخت بدون هیچ رابطه\u200cای', "correct": False},
                {"text": 'فایل\u200cهای پشتیبان (backup)', "correct": False},
                {"text": 'لاگ تراکنش\u200cهای سیستم', "correct": False},
            ],
        },
        {
            "text": 'تفاوت اصلی Window Function با GROUP BY در یک کوئری چیست؟',
            "explanation": 'Window Function برخلاف GROUP BY، ردیف\u200cها را ادغام نمی\u200cکند و مقدار محاسبه\u200cشده را کنار هر ردیف اصلی نمایش می\u200cدهد.',
            "choices": [
                {"text": 'Window Function دقیقاً همان کار GROUP BY را انجام می\u200cدهد', "correct": False},
                {"text": 'Window Function ردیف\u200cها را ادغام نمی\u200cکند و مقدار را کنار هر ردیف نمایش می\u200cدهد', "correct": True},
                {"text": 'GROUP BY هرگز نمی\u200cتواند همراه با JOIN استفاده شود', "correct": False},
                {"text": 'Window Function فقط در دستور INSERT کاربرد دارد', "correct": False},
            ],
        },
        {
            "text": 'کدام تابع پنجره\u200cای برای شماره\u200cگذاری ردیف\u200cها بر اساس یک ترتیب مشخص (مثلاً PARTITION BY) استفاده می\u200cشود؟',
            "explanation": 'ROW_NUMBER() OVER (...) برای شماره\u200cگذاری ترتیبی ردیف\u200cها در هر پارتیشن به کار می\u200cرود.',
            "choices": [
                {"text": 'ROW_NUMBER()', "correct": True},
                {"text": 'SUM()', "correct": False},
                {"text": 'COUNT(*)', "correct": False},
                {"text": 'GETDATE()', "correct": False},
            ],
        },
        {
            "text": 'تفاوت اصلی Stored Procedure و Function در SQL Server چیست؟',
            "explanation": 'Function می\u200cتواند مستقیم داخل یک عبارت SELECT استفاده شود و مقدار برمی\u200cگرداند، اما Stored Procedure چنین امکانی ندارد.',
            "choices": [
                {"text": 'Function می\u200cتواند مستقیم داخل SELECT استفاده شود، اما Stored Procedure این\u200cطور نیست', "correct": True},
                {"text": 'Stored Procedure اصلاً نمی\u200cتواند پارامتر بگیرد', "correct": False},
                {"text": 'Function هیچ\u200cگاه نمی\u200cتواند مقداری برگرداند', "correct": False},
                {"text": 'این دو هیچ تفاوتی با یکدیگر ندارند', "correct": False},
            ],
        },
        {
            "text": 'کدام نوع ایندکس در SQL Server ترتیب فیزیکی ذخیره\u200cی داده روی دیسک را تعیین می\u200cکند؟',
            "explanation": 'Clustered Index ترتیب فیزیکی داده را مشخص می\u200cکند و هر جدول فقط یکی از آن می\u200cتواند داشته باشد.',
            "choices": [
                {"text": 'Clustered Index', "correct": True},
                {"text": 'Nonclustered Index', "correct": False},
                {"text": 'Composite Index', "correct": False},
                {"text": 'Unique Index', "correct": False},
            ],
        },
        {
            "text": 'مشاهده\u200cی عملیات Index Seek در نقشه\u200cی اجرای کوئری (Execution Plan) نشان\u200cدهنده\u200cی چیست؟',
            "explanation": 'Index Seek نشان می\u200cدهد SQL Server با استفاده از ایندکس، به\u200cطور مستقیم و سریع ردیف موردنظر را پیدا کرده است.',
            "choices": [
                {"text": 'پیدا شدن سریع و مستقیم ردیف موردنظر با استفاده از ایندکس', "correct": True},
                {"text": 'پیمایش کامل و کند تمام جدول', "correct": False},
                {"text": 'بروز خطا در اجرای کوئری', "correct": False},
                {"text": 'نبود هیچ ایندکس مناسبی برای جدول', "correct": False},
            ],
        },
        {
            "text": 'وضعیت Deadlock بین دو تراکنش در SQL Server دقیقاً چه زمانی رخ می\u200cدهد؟',
            "explanation": 'Deadlock زمانی رخ می\u200cدهد که دو تراکنش هم\u200cزمان منتظر آزاد شدن منابعی باشند که یکدیگر قفل کرده\u200cاند.',
            "choices": [
                {"text": 'وقتی دو تراکنش منتظر آزاد شدن منابعی هستند که یکدیگر قفل کرده\u200cاند', "correct": True},
                {"text": 'وقتی یک تراکنش با موفقیت commit می\u200cشود', "correct": False},
                {"text": 'وقتی جدولی هیچ ایندکسی ندارد', "correct": False},
                {"text": 'وقتی از دستور BACKUP استفاده می\u200cشود', "correct": False},
            ],
        },
        {
            "text": 'سطح ایزولاسیون READ UNCOMMITTED چه ریسکی برای صحت داده به همراه دارد؟',
            "explanation": 'این سطح امکان خواندن داده\u200cی هنوز commit\u200cنشده\u200cی تراکنش دیگر را می\u200cدهد که به آن Dirty Read گفته می\u200cشود.',
            "choices": [
                {"text": 'امکان خواندن داده\u200cی هنوز commit\u200cنشده (Dirty Read)', "correct": True},
                {"text": 'کندترین سطح ایزولاسیون ممکن است', "correct": False},
                {"text": 'اصلاً امکان خواندن هیچ داده\u200cای وجود ندارد', "correct": False},
                {"text": 'فقط مخصوص اجرای Stored Procedureهاست', "correct": False},
            ],
        },
        {
            "text": 'کدام نوع پشتیبان\u200cگیری در SQL Server امکان بازیابی نقطه\u200cبه\u200cنقطه (Point-in-Time Recovery) را فراهم می\u200cکند؟',
            "explanation": 'Transaction Log Backup با ثبت تمام تغییرات، امکان بازگرداندن دیتابیس تا یک لحظه\u200cی دقیق مشخص را می\u200cدهد.',
            "choices": [
                {"text": 'Transaction Log Backup', "correct": True},
                {"text": 'Full Backup به\u200cتنهایی', "correct": False},
                {"text": 'Differential Backup به\u200cتنهایی', "correct": False},
                {"text": 'Snapshot Backup', "correct": False},
            ],
        },
    ],
}

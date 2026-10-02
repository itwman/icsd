# -*- coding: utf-8 -*-

COURSE = {
    "slug": "sql-server",
    "title": "SQL Server",
    "category": "دیتابیس",
    "level": "intermediate",
    "summary": "کار حرفه‌ای با SQL Server: از T-SQL تا Stored Procedure، ایندکس و اتوماسیون با Agent.",
    "description": (
        "<p>مایکروسافت SQL Server یکی از پرکاربردترین پایگاه‌های داده‌ی سازمانی در دنیاست که به "
        "دلیل ابزارهای مدیریتی قدرتمند مانند SSMS، پشتیبانی خوب از تراکنش‌های سنگین و یکپارچگی "
        "با اکوسیستم مایکروسافت، در بسیاری از شرکت‌های بزرگ استفاده می‌شود.</p>"
        "<p>در طول دوره با نصب SQL Server و SSMS، نوشتن T-SQL پایه، طراحی جدول و Constraint، "
        "JOIN و CTE و Window Functions، ساخت Stored Procedure و Function، ایندکس‌گذاری و خواندن "
        "Execution Plan، تراکنش و قفل، پشتیبان‌گیری و بازیابی و در نهایت اتوماسیون کارها با "
        "SQL Server Agent آشنا می‌شوید.</p>"
        "<p>پیش‌نیاز این دوره آشنایی مقدماتی با مفاهیم پایگاه داده و SQL است.</p>"
    ),
    "price": 1100000,
    "duration_minutes": 540,
    "tags": ["SQL Server", "دیتابیس", "T-SQL"],
    "modules": [
        {
            "title": "فصل اول: شروع کار با SQL Server",
            "lessons": [
                {
                    "title": "نصب SQL Server و SSMS",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": True,
                    "body": """<h2>آشنایی با SQL Server و ابزارهای آن</h2>
<p>SQL Server محصول پایگاه‌داده‌ی رابطه‌ای شرکت مایکروسافت است که علاوه بر نسخه‌ی ویندوزی، از چند سال پیش روی لینوکس و داخل کانتینر Docker نیز قابل نصب است. برای شروع سریع روی لینوکس می‌توان از تصویر رسمی Docker استفاده کرد:</p>
<pre><code class='language-bash'>docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=StrongPass123!" \\
  -p 1433:1433 --name sqlserver \\
  -d mcr.microsoft.com/mssql/server:2022-latest</code></pre>
<p>ابزار اصلی مدیریت گرافیکی SQL Server در ویندوز، SSMS (SQL Server Management Studio) نام دارد که امکان اتصال به سرور، نوشتن و اجرای کوئری، مشاهده‌ی جدول‌ها و مدیریت کاربران را با رابط گرافیکی فراهم می‌کند. برای اتصال به سرور، کافی است آدرس سرور، نام کاربری sa و رمز عبور را وارد کنید.</p>
<p>برای اجرای کوئری از خط فرمان (بدون SSMS) نیز می‌توان از ابزار sqlcmd استفاده کرد:</p>
<pre><code class='language-bash'>sqlcmd -S localhost -U sa -P 'StrongPass123!' -Q "SELECT @@VERSION"</code></pre>
<p>برای ساخت پایگاه‌داده‌ی جدید:</p>
<pre><code class='language-sql'>CREATE DATABASE Shop;
GO
USE Shop;
GO</code></pre>
<p>دستور GO در T-SQL به معنای پایان یک دسته (batch) از دستورات است و به سرور می‌گوید دستورات قبل از آن را اجرا کند؛ این دستور مخصوص ابزارهای مایکروسافت است و بخشی از استاندارد SQL نیست.</p>""",
                },
                {
                    "title": "T-SQL پایه",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": """<h2>گویش T-SQL در SQL Server</h2>
<p>T-SQL (Transact-SQL) گویش اختصاصی مایکروسافت از SQL است که علاوه بر دستورات استاندارد، امکانات اضافه‌ای مانند متغیر، شرط، حلقه و توابع ویژه‌ی خودش را دارد. دستورات پایه‌ی CRUD مشابه سایر پایگاه‌های داده است:</p>
<pre><code class='language-sql'>SELECT TOP 10 Id, Name, Price FROM Products ORDER BY Price DESC;

INSERT INTO Products (Name, Price) VALUES (N'لپ‌تاپ', 25000000);

UPDATE Products SET Price = 24000000 WHERE Id = 1;

DELETE FROM Products WHERE Id = 5;</code></pre>
<p>نکته‌ی مهم استفاده از TOP به‌جای LIMIT برای محدود کردن تعداد نتایج است که ویژگی خاص T-SQL است. همچنین پیشوند N قبل از رشته‌ها (مانند N'لپ‌تاپ') برای ذخیره‌ی صحیح متن یونیکد مانند فارسی ضروری است، در غیر این صورت ممکن است کاراکترهای غیرانگلیسی به‌درستی ذخیره نشوند.</p>
<p>T-SQL همچنین امکان تعریف متغیر و نوشتن منطق رویه‌ای را می‌دهد:</p>
<pre><code class='language-sql'>DECLARE @minPrice DECIMAL(10, 2) = 1000000;

SELECT Name, Price FROM Products WHERE Price &gt; @minPrice;

IF (SELECT COUNT(*) FROM Products) = 0
    PRINT N'هیچ محصولی ثبت نشده است';
ELSE
    PRINT N'محصولات موجود است';</code></pre>
<p>این ترکیب از SQL استاندارد و امکانات رویه‌ای، T-SQL را برای نوشتن منطق پیچیده‌تر در سطح دیتابیس بسیار قدرتمند می‌کند.</p>""",
                },
                {
                    "title": "طراحی جدول و Constraint",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": """<h2>تعریف جدول و محدودیت‌های داده</h2>
<p>طراحی درست جدول در SQL Server شامل انتخاب نوع داده‌ی مناسب و تعریف Constraint‌های لازم برای تضمین صحت داده است. برای کلید اصلی خودافزا از IDENTITY استفاده می‌شود:</p>
<pre><code class='language-sql'>CREATE TABLE Customers (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    FullName NVARCHAR(150) NOT NULL,
    Email NVARCHAR(150) NOT NULL UNIQUE,
    RegisteredAt DATETIME2 DEFAULT GETDATE()
);

CREATE TABLE Orders (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    CustomerId INT NOT NULL FOREIGN KEY REFERENCES Customers(Id),
    Total DECIMAL(10, 2) NOT NULL CHECK (Total &gt; 0),
    CreatedAt DATETIME2 DEFAULT GETDATE()
);</code></pre>
<p>استفاده از NVARCHAR به‌جای VARCHAR برای متن‌های فارسی و سایر زبان‌های غیرانگلیسی ضروری است، چون NVARCHAR از یونیکد پشتیبانی می‌کند در حالی که VARCHAR فقط کاراکترهای صفحه‌کد محلی را ذخیره می‌کند. IDENTITY(1,1) به این معناست که شمارش از عدد ۱ شروع شده و هر بار ۱ واحد افزایش می‌یابد.</p>
<p>محدودیت CHECK تضمین می‌کند مقدار ستون Total همیشه مثبت باشد و از ثبت داده‌ی نامعتبر جلوگیری می‌کند. محدودیت FOREIGN KEY نیز ارتباط بین دو جدول را برقرار و از ثبت CustomerId نامعتبر جلوگیری می‌کند. DATETIME2 نسبت به نوع قدیمی‌تر DATETIME دقت بیشتری دارد و برای پروژه‌های جدید توصیه می‌شود. رعایت این اصول از همان ابتدای طراحی، از بسیاری از مشکلات داده‌ای در آینده جلوگیری می‌کند.</p>""",
                },
            ],
        },
        {
            "title": "فصل دوم: کوئری‌نویسی پیشرفته",
            "lessons": [
                {
                    "title": "JOIN و CTE",
                    "kind": "text",
                    "minutes": 25,
                    "is_preview": False,
                    "body": """<h2>ترکیب جدول‌ها و ساده‌سازی کوئری با CTE</h2>
<p>JOIN در SQL Server مانند سایر پایگاه‌های داده‌ی رابطه‌ای عمل می‌کند و برای ترکیب داده از چند جدول استفاده می‌شود:</p>
<pre><code class='language-sql'>SELECT c.FullName, o.Total, o.CreatedAt
FROM Orders o
INNER JOIN Customers c ON c.Id = o.CustomerId
WHERE o.Total &gt; 500000
ORDER BY o.CreatedAt DESC;</code></pre>
<p>CTE یا Common Table Expression، که با کلیدواژه‌ی WITH تعریف می‌شود، یک نتیجه‌ی موقت است که می‌توانید در ادامه‌ی همان کوئری از آن استفاده کنید. CTE به‌ویژه برای شکستن کوئری‌های پیچیده به بخش‌های کوچک‌تر و خواناتر بسیار مفید است:</p>
<pre><code class='language-sql'>WITH CustomerTotals AS (
    SELECT CustomerId, SUM(Total) AS TotalSpent
    FROM Orders
    GROUP BY CustomerId
)
SELECT c.FullName, ct.TotalSpent
FROM CustomerTotals ct
JOIN Customers c ON c.Id = ct.CustomerId
WHERE ct.TotalSpent &gt; 1000000;</code></pre>
<p>یکی از کاربردهای مهم CTE، نوشتن کوئری بازگشتی (Recursive CTE) است که برای پیمایش ساختارهای درختی مانند دسته‌بندی‌های تودرتو استفاده می‌شود:</p>
<pre><code class='language-sql'>WITH CategoryTree AS (
    SELECT Id, Name, ParentId, 0 AS Level
    FROM Categories WHERE ParentId IS NULL
    UNION ALL
    SELECT c.Id, c.Name, c.ParentId, ct.Level + 1
    FROM Categories c
    JOIN CategoryTree ct ON c.ParentId = ct.Id
)
SELECT * FROM CategoryTree;</code></pre>
<p>ترکیب JOIN و CTE به شما اجازه می‌دهد گزارش‌های پیچیده را در قالبی خوانا و قابل نگهداری بنویسید.</p>""",
                },
                {
                    "title": "Window Functions",
                    "kind": "text",
                    "minutes": 25,
                    "is_preview": False,
                    "body": """<h2>محاسبات پیشرفته با توابع پنجره‌ای</h2>
<p>Window Function نوعی تابع محاسباتی است که برخلاف GROUP BY، ردیف‌ها را در نتیجه ادغام نمی‌کند، بلکه یک مقدار محاسبه‌شده را در کنار هر ردیف اصلی نمایش می‌دهد. این ابزار برای رتبه‌بندی، محاسبه‌ی مجموع تجمعی و مقایسه با ردیف قبل و بعد بسیار کاربردی است.</p>
<p>تابع ROW_NUMBER برای شماره‌گذاری ردیف‌ها بر اساس یک ترتیب مشخص استفاده می‌شود؛ مثلاً پیدا کردن پرفروش‌ترین محصول هر دسته‌بندی:</p>
<pre><code class='language-sql'>SELECT Name, CategoryId, Price,
    ROW_NUMBER() OVER (PARTITION BY CategoryId ORDER BY Price DESC) AS Rank
FROM Products;</code></pre>
<p>عبارت PARTITION BY محاسبه را در هر دسته‌بندی جداگانه از نو شروع می‌کند، درست مانند GROUP BY اما بدون ادغام ردیف‌ها. توابع RANK و DENSE_RANK نیز مشابه ROW_NUMBER هستند با این تفاوت که در صورت تساوی مقدار، رتبه‌ی یکسانی می‌دهند.</p>
<p>یکی دیگر از کاربردهای رایج، محاسبه‌ی مجموع تجمعی (running total) با SUM همراه با OVER است:</p>
<pre><code class='language-sql'>SELECT OrderDate, Total,
    SUM(Total) OVER (ORDER BY OrderDate) AS RunningTotal
FROM Orders;</code></pre>
<p>توابع LAG و LEAD نیز مقدار ردیف قبلی یا بعدی را در همان دسته برمی‌گردانند که برای محاسبه‌ی تغییرات بین دوره‌ها (مثلاً رشد فروش نسبت به روز قبل) بسیار مفید است. تسلط بر Window Function یکی از مهارت‌های کلیدی برای نوشتن گزارش‌های تحلیلی حرفه‌ای است.</p>""",
                },
                {
                    "title": "Stored Procedure و Function",
                    "kind": "text",
                    "minutes": 25,
                    "is_preview": False,
                    "body": """<h2>نوشتن منطق قابل استفاده‌ی مجدد در دیتابیس</h2>
<p>Stored Procedure مجموعه‌ای از دستورات T-SQL است که یک‌بار روی سرور تعریف می‌شود و می‌توان آن را بارها با پارامترهای مختلف فراخوانی کرد. این کار باعث کاهش ترافیک شبکه، افزایش امنیت (با محدود کردن دسترسی مستقیم به جدول) و امکان استفاده‌ی مجدد از منطق مشترک می‌شود.</p>
<pre><code class='language-sql'>CREATE PROCEDURE GetOrdersByCustomer
    @CustomerId INT
AS
BEGIN
    SELECT Id, Total, CreatedAt
    FROM Orders
    WHERE CustomerId = @CustomerId
    ORDER BY CreatedAt DESC;
END;</code></pre>
<p>فراخوانی این Stored Procedure با دستور EXEC انجام می‌شود:</p>
<pre><code class='language-sql'>EXEC GetOrdersByCustomer @CustomerId = 5;</code></pre>
<p>در مقابل، Function (تابع اسکالر یا جدولی) مقداری را برمی‌گرداند و می‌توان آن را مستقیماً در یک عبارت SELECT استفاده کرد؛ Stored Procedure چنین امکانی ندارد:</p>
<pre><code class='language-sql'>CREATE FUNCTION dbo.GetDiscountedPrice (@Price DECIMAL(10,2), @DiscountPercent INT)
RETURNS DECIMAL(10,2)
AS
BEGIN
    RETURN @Price - (@Price * @DiscountPercent / 100);
END;

SELECT Name, dbo.GetDiscountedPrice(Price, 10) AS FinalPrice FROM Products;</code></pre>
<p>یک قاعده‌ی کلی برای انتخاب بین این دو این است: اگر نیاز به اجرای چند دستور، تراکنش یا تغییر داده دارید از Stored Procedure استفاده کنید؛ اگر فقط یک مقدار محاسبه‌شده در دل کوئری نیاز دارید، از Function بهره بگیرید.</p>""",
                },
            ],
        },
        {
            "title": "فصل سوم: کارایی و تراکنش",
            "lessons": [
                {
                    "title": "ایندکس و Execution Plan",
                    "kind": "text",
                    "minutes": 25,
                    "is_preview": False,
                    "body": """<h2>افزایش سرعت کوئری و خواندن نقشه‌ی اجرا</h2>
<p>ایندکس در SQL Server نیز مانند سایر پایگاه‌های داده، ساختاری است که سرعت جست‌وجو، فیلتر و مرتب‌سازی را افزایش می‌دهد. دو نوع اصلی ایندکس وجود دارد: Clustered Index که ترتیب فیزیکی داده روی دیسک را تعیین می‌کند (هر جدول فقط یکی می‌تواند داشته باشد و معمولاً روی کلید اصلی ساخته می‌شود) و Nonclustered Index که ساختار جداگانه‌ای جدا از داده‌ی اصلی است:</p>
<pre><code class='language-sql'>CREATE NONCLUSTERED INDEX IX_Orders_CustomerId ON Orders(CustomerId);
CREATE NONCLUSTERED INDEX IX_Products_Category_Price ON Products(CategoryId, Price);</code></pre>
<p>برای بررسی نحوه‌ی اجرای یک کوئری، در SSMS می‌توانید گزینه‌ی «Include Actual Execution Plan» را فعال کنید یا از دستور زیر استفاده کنید:</p>
<pre><code class='language-sql'>SET STATISTICS IO ON;
SELECT * FROM Orders WHERE CustomerId = 42;</code></pre>
<p>در نقشه‌ی اجرا، عملیات‌هایی مانند Table Scan (پیمایش کل جدول) نشانه‌ی نبود ایندکس مناسب است، در حالی که Index Seek نشان می‌دهد SQL Server به‌طور مستقیم و سریع ردیف موردنظر را پیدا کرده است. هزینه‌ی نسبی (Cost %) کنار هر مرحله به شما کمک می‌کند بخش‌های پرهزینه‌ی کوئری را شناسایی کنید.</p>
<p>باید توجه داشت ساخت بی‌رویه‌ی ایندکس، عملیات نوشتن را کند می‌کند و فضای دیسک بیشتری مصرف می‌کند؛ بنابراین ایندکس باید بر اساس کوئری‌های واقعی و پرتکرار برنامه طراحی شود، نه به‌صورت حدسی.</p>""",
                },
                {
                    "title": "تراکنش و قفل (Locking)",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": """<h2>مدیریت همزمانی با تراکنش و قفل</h2>
<p>تراکنش در SQL Server نیز مانند سایر پایگاه‌های داده تضمین می‌کند مجموعه‌ای از عملیات یا همگی اجرا شوند یا هیچ‌کدام. برای تعریف صریح یک تراکنش:</p>
<pre><code class='language-sql'>BEGIN TRANSACTION;

UPDATE Accounts SET Balance = Balance - 500000 WHERE Id = 1;
UPDATE Accounts SET Balance = Balance + 500000 WHERE Id = 2;

IF @@ERROR = 0
    COMMIT TRANSACTION;
ELSE
    ROLLBACK TRANSACTION;</code></pre>
<p>هنگام اجرای تراکنش‌ها، SQL Server برای جلوگیری از تداخل داده بین کاربران همزمان، به‌طور خودکار روی ردیف‌ها یا جدول‌های درگیر قفل (Lock) می‌گذارد. قفل‌های رایج شامل Shared Lock (برای خواندن) و Exclusive Lock (برای نوشتن) هستند. اگر دو تراکنش هم‌زمان منتظر آزاد شدن منابعی باشند که یکدیگر قفل کرده‌اند، وضعیتی به نام Deadlock رخ می‌دهد که SQL Server به‌طور خودکار یکی از دو تراکنش را به‌عنوان قربانی (victim) لغو می‌کند.</p>
<p>برای مشاهده‌ی قفل‌های فعال فعلی می‌توان از View سیستمی زیر استفاده کرد:</p>
<pre><code class='language-sql'>SELECT * FROM sys.dm_tran_locks;</code></pre>
<p>سطح ایزولاسیون پیش‌فرض SQL Server، READ COMMITTED است که از خواندن داده‌ی commit‌نشده جلوگیری می‌کند اما ممکن است باعث انتظار طولانی‌تر شود؛ سطح READ COMMITTED SNAPSHOT با استفاده از نسخه‌سازی ردیف (row versioning) می‌تواند بسیاری از این انتظارها را بدون قربانی کردن صحت داده کاهش دهد و در بسیاری از پروژه‌های واقعی فعال می‌شود.</p>""",
                },
                {
                    "title": "سطوح ایزولاسیون تراکنش",
                    "kind": "text",
                    "minutes": 15,
                    "is_preview": False,
                    "body": """<h2>انتخاب سطح مناسب ایزولاسیون</h2>
<p>سطح ایزولاسیون تراکنش تعیین می‌کند تراکنش‌های همزمان تا چه حد از تغییرات یکدیگر تأثیر می‌پذیرند. انتخاب درست این سطح، تعادلی بین صحت داده و کارایی همزمانی برقرار می‌کند. SQL Server چهار سطح استاندارد به همراه یک سطح اضافه دارد.</p>
<p>سطح READ UNCOMMITTED پایین‌ترین سطح است که اجازه می‌دهد یک تراکنش، داده‌ی هنوز commit‌نشده‌ی تراکنش دیگر را بخواند؛ این حالت با نام Dirty Read شناخته می‌شود و ریسک خواندن داده‌ی نادرست را دارد:</p>
<pre><code class='language-sql'>SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
SELECT * FROM Orders;</code></pre>
<p>سطح REPEATABLE READ تضمین می‌کند اگر یک تراکنش دو بار همان ردیف را بخواند، مقدار یکسانی دریافت کند، اما همچنان ممکن است ردیف‌های جدید (Phantom Read) در تکرار دوم ظاهر شوند. بالاترین سطح، SERIALIZABLE است که کاملاً از تداخل جلوگیری می‌کند اما کارایی همزمانی را به شدت کاهش می‌دهد:</p>
<pre><code class='language-sql'>SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;</code></pre>
<p>سطح ویژه‌ی SNAPSHOT، به‌جای قفل کردن، از نسخه‌ای از داده در لحظه‌ی شروع تراکنش استفاده می‌کند و باعث می‌شود خوانندگان هرگز منتظر نویسندگان نمانند؛ این سطح در بسیاری از برنامه‌های پرترافیک امروزی ترجیح داده می‌شود. انتخاب سطح مناسب باید بر اساس نیاز واقعی برنامه به صحت داده در برابر سرعت پاسخ‌دهی انجام شود.</p>""",
                },
            ],
        },
        {
            "title": "فصل چهارم: نگهداری و اتوماسیون",
            "lessons": [
                {
                    "title": "Backup و Restore",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": """<h2>پشتیبان‌گیری و بازیابی در SQL Server</h2>
<p>SQL Server سه نوع اصلی پشتیبان‌گیری دارد: Full Backup که کل پایگاه‌داده را کپی می‌کند، Differential Backup که فقط تغییرات پس از آخرین Full Backup را ذخیره می‌کند و Transaction Log Backup که امکان بازیابی نقطه‌به‌نقطه (Point-in-Time Recovery) را فراهم می‌کند.</p>
<pre><code class='language-sql'>BACKUP DATABASE Shop
TO DISK = 'C:\\Backups\\Shop_Full.bak'
WITH FORMAT, INIT;</code></pre>
<p>برای گرفتن بکاپ افزایشی پس از یک Full Backup:</p>
<pre><code class='language-sql'>BACKUP DATABASE Shop
TO DISK = 'C:\\Backups\\Shop_Diff.bak'
WITH DIFFERENTIAL;</code></pre>
<p>برای بازیابی پایگاه‌داده از فایل بکاپ:</p>
<pre><code class='language-sql'>RESTORE DATABASE Shop
FROM DISK = 'C:\\Backups\\Shop_Full.bak'
WITH REPLACE;</code></pre>
<p>اگر پایگاه‌داده در حالت بازیابی کامل (Full Recovery Model) باشد، باید Transaction Log Backupها را نیز به ترتیب پس از Full Backup بازیابی کنید تا داده تا آخرین لحظه‌ی ممکن پیش از خرابی بازگردانده شود. گزینه‌ی WITH REPLACE به SQL Server می‌گوید پایگاه‌داده‌ی فعلی را با نسخه‌ی داخل فایل بکاپ جایگزین کند، حتی اگر پایگاه‌داده‌ای با همین نام از قبل وجود داشته باشد. تست دوره‌ای فرآیند Restore روی یک سرور جداگانه، تنها راه اطمینان از سالم بودن بکاپ‌هاست.</p>""",
                },
                {
                    "title": "SQL Server Agent و Job",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": """<h2>خودکارسازی وظایف تکراری</h2>
<p>SQL Server Agent سرویسی است که به شما امکان می‌دهد وظایف تکراری مانند پشتیبان‌گیری شبانه، اجرای Stored Procedure در ساعت مشخص یا پاک‌سازی داده‌های قدیمی را به‌صورت خودکار و بر اساس زمان‌بندی اجرا کنید، بدون نیاز به دخالت دستی.</p>
<p>یک Job در Agent از یک یا چند Step (مرحله) تشکیل شده که هر Step می‌تواند یک دستور T-SQL، اجرای یک Stored Procedure یا حتی یک اسکریپت خارجی باشد. برای ساخت یک Job ساده که هر شب بکاپ می‌گیرد، می‌توانید از رویه‌های سیستمی Agent استفاده کنید:</p>
<pre><code class='language-sql'>EXEC msdb.dbo.sp_add_job @job_name = N'Nightly_Backup';

EXEC msdb.dbo.sp_add_jobstep
    @job_name = N'Nightly_Backup',
    @step_name = N'Backup Shop DB',
    @command = N'BACKUP DATABASE Shop TO DISK = ''C:\\Backups\\Shop_Nightly.bak''';

EXEC msdb.dbo.sp_add_schedule
    @schedule_name = N'Every_Night_2AM',
    @freq_type = 4,
    @freq_interval = 1,
    @active_start_time = 020000;</code></pre>
<p>در عمل، بیشتر مدیران دیتابیس این کار را از طریق رابط گرافیکی SSMS در بخش SQL Server Agent انجام می‌دهند که ساخت Job، تعریف زمان‌بندی و مشاهده‌ی تاریخچه‌ی اجرا را با چند کلیک ممکن می‌سازد. Agent همچنین امکان تنظیم هشدار ایمیلی در صورت شکست یک Job را دارد که برای اطمینان از اجرای موفق وظایف حیاتی مانند بکاپ شبانه ضروری است. استفاده‌ی درست از Agent، بار زیادی از دوش مدیر دیتابیس برمی‌دارد و ریسک فراموشی وظایف تکراری را حذف می‌کند.</p>""",
                },
                {
                    "title": "مانیتورینگ و عیب‌یابی",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": """<h2>بررسی سلامت و عملکرد سرور</h2>
<p>پس از استقرار SQL Server در محیط عملیاتی، نظارت مداوم بر عملکرد آن برای جلوگیری از افت سرعت یا از کار افتادن سرویس ضروری است. SQL Server چند ابزار و View سیستمی قدرتمند برای این منظور فراهم می‌کند.</p>
<p>برای مشاهده‌ی کوئری‌ها و session‌های فعال در همین لحظه:</p>
<pre><code class='language-sql'>SELECT session_id, status, command, cpu_time, total_elapsed_time
FROM sys.dm_exec_requests
WHERE session_id &gt; 50;</code></pre>
<p>برای شناسایی کندترین کوئری‌ها بر اساس زمان اجرای تجمعی، می‌توان از View آماری زیر استفاده کرد:</p>
<pre><code class='language-sql'>SELECT TOP 10
    qs.total_worker_time / qs.execution_count AS avg_cpu_time,
    qs.execution_count,
    st.text AS query_text
FROM sys.dm_exec_query_stats qs
CROSS APPLY sys.dm_exec_sql_text(qs.sql_handle) st
ORDER BY avg_cpu_time DESC;</code></pre>
<p>ابزار گرافیکی Activity Monitor در SSMS نمایی سریع از وضعیت پردازنده، دیسک و کوئری‌های پرهزینه ارائه می‌دهد و برای بررسی سریع در لحظه‌ی بحران بسیار مفید است. برای تحلیل عمیق‌تر مشکلات کارایی در طول زمان، ابزار Extended Events جایگزین مدرن و سبک‌تر SQL Profiler قدیمی است و امکان ثبت رویدادهای دقیق بدون افت محسوس کارایی سرور را فراهم می‌کند. رصد منظم فضای دیسک، رشد فایل‌های Log و تعداد Deadlockهای رخ‌داده نیز بخش مهمی از نگهداری پیشگیرانه‌ی یک سرور SQL Server در محیط تولید است.</p>""",
                },
            ],
        },
    ],
}

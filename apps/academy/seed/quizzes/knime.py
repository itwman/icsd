# -*- coding: utf-8 -*-

QUIZ = {
    "course_slug": "knime",
    "title": "آزمون پایانی KNIME",
    "pass_percent": 70,
    "time_limit_minutes": 20,
    "questions": [
        {
            "text": "واحد پایه‌ای که در KNIME یک عملیات مشخص روی داده انجام می‌دهد چه نام دارد؟",
            "explanation": "هر Node یک عملیات مشخص (خواندن فایل، فیلتر، محاسبه و...) روی داده انجام می‌دهد و با اتصال چند node به هم یک Workflow ساخته می‌شود.",
            "choices": [
                {"text": "Workflow", "correct": False},
                {"text": "Node", "correct": True},
                {"text": "Component", "correct": False},
                {"text": "Table View", "correct": False},
            ],
        },
        {
            "text": "رنگ چراغ زیر یک node در KNIME وقتی سبز باشد به چه معناست؟",
            "explanation": "چراغ سبز یعنی node با موفقیت اجرا شده و خروجی آن برای node بعدی آماده است؛ قرمز یعنی پیکربندی یا اجرا نشده و زرد یعنی پیکربندی شده اما اجرا نشده.",
            "choices": [
                {"text": "node پیکربندی نشده است", "correct": False},
                {"text": "node آماده اجراست اما اجرا نشده", "correct": False},
                {"text": "node با موفقیت اجرا شده است", "correct": True},
                {"text": "node دارای خطای دائمی است", "correct": False},
            ],
        },
        {
            "text": "کدام node برای خواندن فایل‌های اکسل با امکان انتخاب شیت مشخص استفاده می‌شود؟",
            "explanation": "Excel Reader مخصوص فایل‌های .xlsx است و امکان انتخاب شیت با نام یا شماره و محدوده دقیق سلول‌ها را می‌دهد؛ CSV Reader برای فایل‌های متنی جداشونده است.",
            "choices": [
                {"text": "CSV Reader", "correct": False},
                {"text": "DB Reader", "correct": False},
                {"text": "Excel Reader", "correct": True},
                {"text": "Table View", "correct": False},
            ],
        },
        {
            "text": "node «Statistics» در KNIME چه خروجی‌ای تولید می‌کند؟",
            "explanation": "Statistics یک جدول آماری شامل میانگین، میانه، انحراف معیار، حداقل، حداکثر و تعداد مقادیر گم‌شده هر ستون تولید می‌کند که برای شناخت اولیه داده مفید است.",
            "choices": [
                {"text": "یک فایل CSV خام", "correct": False},
                {"text": "یک مدل یادگیری ماشین آموزش‌دیده", "correct": False},
                {"text": "یک نمودار میله‌ای رنگی", "correct": False},
                {"text": "جدول آماری شامل میانگین، میانه و مقادیر گم‌شده", "correct": True},
            ],
        },
        {
            "text": "برای جدول‌های بسیار بزرگ در پایگاه داده، بهتر است فیلتر و محدودسازی داده کجا انجام شود؟",
            "explanation": "فیلتر کردن در همان پرس‌وجوی SQL پیش از node «DB Reader» سریع‌تر است و فشار کمتری به حافظه سیستم وارد می‌کند، چون کل جدول به KNIME منتقل نمی‌شود.",
            "choices": [
                {"text": "در پرس‌وجوی SQL، پیش از DB Reader", "correct": True},
                {"text": "بعد از خواندن کامل جدول، داخل KNIME", "correct": False},
                {"text": "در node GroupBy پس از Joiner", "correct": False},
                {"text": "در node Sorter", "correct": False},
            ],
        },
        {
            "text": "برای ستون عددی که مقدار گم‌شده آن کم و تصادفی است، کدام گزینه در node Missing Value مناسب‌تر است؟",
            "explanation": "گزینه Mean/Median برای مقادیر گم‌شده کم و تصادفی در ستون‌های عددی مناسب است؛ Remove row یا Fix value بسته به معنای داده انتخاب‌های دیگری هستند.",
            "choices": [
                {"text": "حذف کامل ستون", "correct": False},
                {"text": "Mean/Median", "correct": True},
                {"text": "Most frequent value", "correct": False},
                {"text": "تبدیل به رشته متنی", "correct": False},
            ],
        },
        {
            "text": "node «Joiner» در KNIME معادل کدام عملیات است؟",
            "explanation": "Joiner معادل JOIN در SQL یا تابع VLOOKUP در اکسل است و دو جدول را بر اساس یک ستون کلید مشترک ترکیب می‌کند، اما قوی‌تر و قابل‌تنظیم‌تر است.",
            "choices": [
                {"text": "GROUP BY در SQL", "correct": False},
                {"text": "Pivot Table در اکسل", "correct": False},
                {"text": "JOIN در SQL / VLOOKUP در اکسل", "correct": True},
                {"text": "مرتب‌سازی سطرها", "correct": False},
            ],
        },
        {
            "text": "کدام node در KNIME معادل Pivot Table اکسل یا دستور GROUP BY در SQL برای خلاصه‌سازی گروهی داده عمل می‌کند؟",
            "explanation": "GroupBy سطرها را بر اساس یک یا چند ستون گروه‌بندی کرده و برای هر گروه یک محاسبه خلاصه مثل جمع یا میانگین انجام می‌دهد.",
            "choices": [
                {"text": "Row Filter", "correct": False},
                {"text": "Column Filter", "correct": False},
                {"text": "Joiner", "correct": False},
                {"text": "GroupBy", "correct": True},
            ],
        },
        {
            "text": "در node «Math Formula»، اگر یکی از ستون‌های استفاده‌شده در فرمول برای یک سطر مقدار گم‌شده داشته باشد، نتیجه محاسبه آن سطر چه می‌شود؟",
            "explanation": "نتیجه محاسبه برای آن سطر هم گم‌شده خواهد بود، نه صفر یا خطا؛ به همین دلیل توصیه می‌شود پیش از Math Formula، مقادیر گم‌شده پاک‌سازی شوند.",
            "choices": [
                {"text": "گم‌شده (missing) خواهد بود", "correct": True},
                {"text": "صفر در نظر گرفته می‌شود", "correct": False},
                {"text": "کل workflow متوقف می‌شود", "correct": False},
                {"text": "یک مقدار تصادفی جایگزین می‌شود", "correct": False},
            ],
        },
        {
            "text": "کدام تابع در node «String Manipulation» فاصله‌های ابتدا و انتهای یک رشته را حذف می‌کند؟",
            "explanation": "تابع trim فاصله‌های ابتدا و انتهای رشته را حذف می‌کند؛ lowerCase حروف را کوچک، substr بخشی از رشته را استخراج و replace بخشی از متن را جایگزین می‌کند.",
            "choices": [
                {"text": "lowerCase", "correct": False},
                {"text": "substr", "correct": False},
                {"text": "trim", "correct": True},
                {"text": "replace", "correct": False},
            ],
        },
        {
            "text": "node «Pivoting» در KNIME یک جدول را از چه فرمتی به چه فرمتی تبدیل می‌کند؟",
            "explanation": "Pivoting یک جدول بلند (long format) را به یک جدول عریض (wide format) تبدیل می‌کند، جایی که مقادیر یک ستون به عنوان ستون‌های جدید تبدیل می‌شوند.",
            "choices": [
                {"text": "از wide به long", "correct": False},
                {"text": "از long به wide", "correct": True},
                {"text": "از CSV به Excel", "correct": False},
                {"text": "از عددی به متنی", "correct": False},
            ],
        },
        {
            "text": "پیش از رسم نمودار «Line Plot» برای نمایش روند زمانی، معمولاً کدام node باید بلافاصله قبل از آن اعمال شود؟",
            "explanation": "اگر داده بر اساس محور افقی (مثلاً ماه) مرتب نشود، خط نمودار درهم و بدون ترتیب منطقی رسم می‌شود؛ بنابراین Sorter باید بلافاصله پیش از node نموداری زمانی قرار گیرد.",
            "choices": [
                {"text": "Sorter", "correct": True},
                {"text": "Joiner", "correct": False},
                {"text": "Missing Value", "correct": False},
                {"text": "Row Filter", "correct": False},
            ],
        },
        {
            "text": "کدام نمودار در KNIME برای بررسی توزیع یک ستون عددی (مثلاً تشخیص تمرکز یا مقادیر پرت) استفاده می‌شود؟",
            "explanation": "Histogram داده یک ستون را به بازه‌های مساوی تقسیم کرده و تعداد سطرهای هر بازه را نشان می‌دهد که برای دیدن توزیع مناسب است؛ Scatter Plot برای رابطه بین دو ستون است.",
            "choices": [
                {"text": "Bar Chart", "correct": False},
                {"text": "Scatter Plot", "correct": False},
                {"text": "Line Plot", "correct": False},
                {"text": "Histogram", "correct": True},
            ],
        },
        {
            "text": "در گردش کار ساخت یک مدل Decision Tree، کدام node برای تقسیم داده به بخش‌های آموزش (train) و آزمون (test) استفاده می‌شود؟",
            "explanation": "Partitioning داده را معمولاً با نسبت ۷۰ به ۳۰ یا ۸۰ به ۲۰ به دو بخش train و test تقسیم می‌کند تا مدل روی train آموزش دیده و روی test ارزیابی شود.",
            "choices": [
                {"text": "Decision Tree Learner", "correct": False},
                {"text": "Scorer", "correct": False},
                {"text": "Partitioning", "correct": True},
                {"text": "GroupBy", "correct": False},
            ],
        },
        {
            "text": "node «Scorer» در KNIME چه معیارهایی را برای ارزیابی یک مدل محاسبه می‌کند؟",
            "explanation": "Scorer پیش‌بینی مدل را با مقدار واقعی مقایسه کرده و معیارهایی مثل Confusion Matrix، Accuracy، Precision و Recall را محاسبه می‌کند.",
            "choices": [
                {"text": "جمع و میانگین ستون‌ها", "correct": False},
                {"text": "نوع Join و تعداد تطابق", "correct": False},
                {"text": "Accuracy و Confusion Matrix", "correct": True},
                {"text": "فرمت فایل خروجی", "correct": False},
            ],
        },
    ],
}

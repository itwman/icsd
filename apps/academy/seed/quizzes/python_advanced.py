# -*- coding: utf-8 -*-

QUIZ = {
    "course_slug": "python-advanced",
    "title": "آزمون پایانی پایتون پیشرفته",
    "pass_percent": 70,
    "time_limit_minutes": 25,
    "questions": [
        {
            "text": "متد `__init__` در یک کلاس پایتونی چه نقشی دارد؟",
            "explanation": "متد __init__ سازنده‌ی کلاس نام دارد و هنگام ساخت هر شیء جدید به‌طور خودکار اجرا می‌شود.",
            "choices": [
                {"text": "حذف یک شیء از حافظه", "correct": False},
                {"text": "سازنده‌ی کلاس است و هنگام ساخت شیء جدید خودکار اجرا می‌شود", "correct": True},
                {"text": "فقط برای نمایش رشته‌ای شیء استفاده می‌شود", "correct": False},
                {"text": "متدی است که فقط در وراثت چندگانه کاربرد دارد", "correct": False},
            ],
        },
        {
            "text": "تابع `super()` در پایتون چه کاربردی دارد؟",
            "explanation": "super() اجازه می‌دهد بدون ذکر مستقیم نام کلاس والد، متد آن را فراخوانی کنیم؛ در وراثت چندگانه اهمیت زیادی دارد.",
            "choices": [
                {"text": "فراخوانی متد کلاس والد بدون ذکر مستقیم نام آن", "correct": True},
                {"text": "ساخت یک نمونه‌ی جدید از کلاس فعلی", "correct": False},
                {"text": "حذف متدهای ارث‌بری‌شده", "correct": False},
                {"text": "تبدیل یک کلاس به دکوراتور", "correct": False},
            ],
        },
        {
            "text": "کدام دکوراتور برای تعریف یک ویژگی با کنترل دسترسی (getter/setter) روی یک attribute استفاده می‌شود؟",
            "explanation": "دکوراتور @property به همراه @نام.setter امکان کنترل دسترسی به یک ویژگی را بدون تغییر ظاهر بیرونی کلاس فراهم می‌کند.",
            "choices": [
                {"text": "@staticmethod", "correct": False},
                {"text": "@classmethod", "correct": False},
                {"text": "@dataclass", "correct": False},
                {"text": "@property", "correct": True},
            ],
        },
        {
            "text": "دکوراتور (decorator) در پایتون دقیقاً چه کاری انجام می‌دهد؟",
            "explanation": "دکوراتور تابعی است که یک تابع دیگر را می‌گیرد، رفتاری به آن اضافه می‌کند و تابعی جدید برمی‌گرداند، بدون تغییر کد اصلی تابع.",
            "choices": [
                {"text": "کد تابع اصلی را برای همیشه تغییر می‌دهد", "correct": False},
                {"text": "تابعی را می‌گیرد و بدون تغییر کد آن، تابع جدیدی با رفتار اضافه‌شده برمی‌گرداند", "correct": True},
                {"text": "فقط برای تعریف متغیرهای سراسری استفاده می‌شود", "correct": False},
                {"text": "یک کلاس را به تابع تبدیل می‌کند", "correct": False},
            ],
        },
        {
            "text": "استفاده از `functools.wraps` هنگام نوشتن یک دکوراتور چه مشکلی را حل می‌کند؟",
            "explanation": "بدون wraps، ویژگی‌های تابع اصلی مانند __name__ و docstring با ویژگی‌های تابع wrapper جایگزین می‌شوند که دیباگ را دشوار می‌کند.",
            "choices": [
                {"text": "سرعت اجرای تابع را افزایش می‌دهد", "correct": False},
                {"text": "تعداد آرگومان‌های تابع را محدود می‌کند", "correct": False},
                {"text": "حفظ متادیتای تابع اصلی مانند __name__ و docstring", "correct": True},
                {"text": "امکان استفاده از async/await را فراهم می‌کند", "correct": False},
            ],
        },
        {
            "text": "کدام کلیدواژه یک تابع معمولی را به یک جنراتور (generator) تبدیل می‌کند؟",
            "explanation": "جنراتور تابعی است که به‌جای return از yield استفاده می‌کند و وضعیت تابع بین فراخوانی‌ها حفظ می‌شود.",
            "choices": [
                {"text": "yield", "correct": True},
                {"text": "return", "correct": False},
                {"text": "await", "correct": False},
                {"text": "async", "correct": False},
            ],
        },
        {
            "text": "مزیت اصلی استفاده از جنراتورها نسبت به ساختن یک لیست کامل از قبل چیست؟",
            "explanation": "جنراتورها با محاسبه‌ی تنبل (lazy evaluation) مقادیر را فقط در لحظه‌ی نیاز تولید می‌کنند و در مصرف حافظه صرفه‌جویی می‌کنند.",
            "choices": [
                {"text": "همیشه سریع‌تر از هر حلقه‌ی دیگری اجرا می‌شوند", "correct": False},
                {"text": "محاسبه‌ی تنبل (lazy evaluation) و صرفه‌جویی در مصرف حافظه", "correct": True},
                {"text": "امکان تغییر نوع داده در حین اجرا را می‌دهند", "correct": False},
                {"text": "نیازی به کلیدواژه‌ی for برای پیمایش ندارند", "correct": False},
            ],
        },
        {
            "text": "تابع `chain` از ماژول `itertools` چه کاری انجام می‌دهد؟",
            "explanation": "chain چند ایتریبل (iterable) را پشت‌سرهم به هم متصل می‌کند، مثلاً list(chain([1,2],[3,4])) برابر [1,2,3,4] است.",
            "choices": [
                {"text": "دو ایتریبل را با هم مقایسه می‌کند", "correct": False},
                {"text": "یک ایتریبل را به‌صورت نامحدود تکرار می‌کند", "correct": False},
                {"text": "چند ایتریبل را پشت‌سرهم به هم متصل می‌کند", "correct": True},
                {"text": "عناصر تکراری یک ایتریبل را حذف می‌کند", "correct": False},
            ],
        },
        {
            "text": "برای این‌که یک کلاس سفارشی از دستور `with` پشتیبانی کند، باید کدام دو متد را پیاده‌سازی کند؟",
            "explanation": "پروتکل context manager بر پایه‌ی دو متد __enter__ (هنگام ورود به بلوک with) و __exit__ (هنگام خروج از بلوک) ساخته شده است.",
            "choices": [
                {"text": "__init__ و __del__", "correct": False},
                {"text": "__str__ و __repr__", "correct": False},
                {"text": "__iter__ و __next__", "correct": False},
                {"text": "__enter__ و __exit__", "correct": True},
            ],
        },
        {
            "text": "برای مقدار پیش‌فرض قابل‌تغییر مانند لیست در یک `@dataclass`، به‌جای نوشتن مستقیم `tags: list = []` باید از چه چیزی استفاده کرد؟",
            "explanation": "استفاده‌ی مستقیم از یک لیست به‌عنوان مقدار پیش‌فرض باعث اشتراک آن بین همه‌ی نمونه‌ها می‌شود؛ به همین دلیل از field(default_factory=list) استفاده می‌شود.",
            "choices": [
                {"text": "field(default_factory=list)", "correct": True},
                {"text": "list()", "correct": False},
                {"text": "@property", "correct": False},
                {"text": "None", "correct": False},
            ],
        },
        {
            "text": "type hints (راهنمای نوع) در پایتون به‌طور پیش‌فرض در زمان اجرا چگونه رفتار می‌کنند؟",
            "explanation": "type hints فقط یک راهنما هستند و پایتون به‌طور پیش‌فرض آن‌ها را در زمان اجرا بررسی نمی‌کند؛ برای بررسی واقعی باید از ابزارهایی مانند mypy استفاده کرد.",
            "choices": [
                {"text": "باعث خطای اجرا در صورت ناهماهنگی نوع می‌شوند", "correct": False},
                {"text": "به‌طور پیش‌فرض بررسی نمی‌شوند و فقط جنبه‌ی راهنما دارند", "correct": True},
                {"text": "نوع متغیر را به‌طور اجباری در حافظه ثابت می‌کنند", "correct": False},
                {"text": "فقط در پایتون نسخه‌ی ۲ کار می‌کنند", "correct": False},
            ],
        },
        {
            "text": "یک تابع تعریف‌شده با `async def` در پایتون چه نامیده می‌شود؟",
            "explanation": "تابعی که با async def تعریف می‌شود coroutine نام دارد و می‌تواند در نقاطی با await اجرای خود را موقتاً متوقف کند.",
            "choices": [
                {"text": "generator", "correct": False},
                {"text": "decorator", "correct": False},
                {"text": "coroutine", "correct": True},
                {"text": "iterator", "correct": False},
            ],
        },
        {
            "text": "تابع `asyncio.gather()` چه کاربردی دارد؟",
            "explanation": "asyncio.gather چند coroutine را به‌طور همزمان (concurrent) اجرا می‌کند تا کل زمان اجرا به‌جای مجموع تأخیرها، تقریباً برابر طولانی‌ترین تأخیر شود.",
            "choices": [
                {"text": "اجرای همزمان چند coroutine و انتظار برای پایان همه‌ی آن‌ها", "correct": True},
                {"text": "متوقف کردن دائمی یک coroutine", "correct": False},
                {"text": "تبدیل یک تابع معمولی به coroutine", "correct": False},
                {"text": "ایجاد یک event loop جدید در هر فراخوانی", "correct": False},
            ],
        },
        {
            "text": "در pytest، نام فایل‌های تست و توابع تست معمولاً باید با چه پیشوندی شروع شوند؟",
            "explanation": "فایل تست معمولاً با پیشوند test_ نام‌گذاری می‌شود و هر تابع تست نیز باید با test_ شروع شود تا pytest آن را شناسایی کند.",
            "choices": [
                {"text": "check_", "correct": False},
                {"text": "run_", "correct": False},
                {"text": "test_", "correct": True},
                {"text": "assert_", "correct": False},
            ],
        },
        {
            "text": "فایل `pyproject.toml` در ساختار یک پکیج مدرن پایتون چه نقشی دارد؟",
            "explanation": "pyproject.toml جایگزین مدرن setup.py شده و متادیتای بسته، وابستگی‌ها و تنظیمات ابزار ساخت را در یک فایل استاندارد نگه می‌دارد.",
            "choices": [
                {"text": "فقط برای نوشتن تست‌های واحد استفاده می‌شود", "correct": False},
                {"text": "نگهداری متادیتا، وابستگی‌ها و تنظیمات ساخت بسته", "correct": True},
                {"text": "جایگزین فایل requirements.txt در محیط مجازی است", "correct": False},
                {"text": "فایل تنظیمات event loop در asyncio است", "correct": False},
            ],
        },
    ],
}

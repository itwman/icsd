# -*- coding: utf-8 -*-
# بانک ۳۵ سؤالی آزمون پایانی دوره‌ی جامع پایتون — هر بار ۲۰ سؤال تصادفی، پوشش هر ۸ فصل.

QUIZ = {
    "course_slug": "python-basics",
    "title": "آزمون پایانی آموزش جامع پایتون",
    "pass_percent": 70,
    "time_limit_minutes": 30,
    "questions_per_attempt": 20,
    "questions": [
        {
            "text": "چرا در این دوره به‌جای `pip install requests` همیشه `python -m pip install requests` نوشته می‌شود؟",
            "explanation": "`python -m pip` همان pip ای را اجرا می‌کند که متعلق به مفسر `python` فعلی است؛ پس بسته دقیقاً برای همان پایتون یا venv ای نصب می‌شود که برنامه را با آن اجرا می‌کنید.",
            "choices": [
                {"text": "چون `pip` خالی در ویندوز اصلاً وجود ندارد", "correct": False},
                {"text": "تا بسته برای همان مفسری نصب شود که `python` به آن اشاره دارد", "correct": True},
                {"text": "چون `python -m pip` همیشه از میرور ایرانی استفاده می‌کند", "correct": False},
                {"text": "تا بسته به‌صورت سراسری برای همه‌ی کاربران نصب شود", "correct": False},
            ],
        },
        {
            "text": "اجرای `.\\.venv\\Scripts\\Activate.ps1` در PowerShell خطای «running scripts is disabled on this system» می‌دهد. راه‌حل معمول و امن چیست؟",
            "explanation": "سیاست اجرای اسکریپت را فقط برای کاربر فعلی روی RemoteSigned بگذارید؛ این کار اسکریپت‌های محلی را مجاز می‌کند و نیازی به دسترسی مدیر ندارد.",
            "choices": [
                {"text": "حذف پوشه‌ی `.venv` و نصب پایتون از Microsoft Store", "correct": False},
                {"text": "اجرای PowerShell با دسترسی Administrator در هر بار کار", "correct": False},
                {"text": "`Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`", "correct": True},
                {"text": "تغییر نام فایل `Activate.ps1` به `Activate.bat`", "correct": False},
            ],
        },
        {
            "text": "در Windows PowerShell 5.1 دستور `pip freeze > requirements.txt` چه مشکلی ایجاد می‌کند؟",
            "explanation": "عملگر `>` در PowerShell 5.1 فایل را با UTF-16 می‌نویسد؛ git و بسیاری از ابزارها آن را باینری می‌بینند. `| Out-File -Encoding utf8` این مشکل را ندارد.",
            "choices": [
                {"text": "فایل با کدگذاری UTF-16 ساخته می‌شود و ابزارهایی مثل git آن را باینری می‌بینند", "correct": True},
                {"text": "فقط بسته‌هایی که با `--user` نصب شده‌اند در فایل نوشته می‌شوند", "correct": False},
                {"text": "نسخه‌ی بسته‌ها حذف می‌شود و فقط نام‌ها می‌مانند", "correct": False},
                {"text": "فایل قبلی پاک نمی‌شود و خروجی به انتهای آن اضافه می‌شود", "correct": False},
            ],
        },
        {
            "text": "برای این‌که pip برای همیشه از یک میرور ایرانی استفاده کند، کدام دستور مناسب است؟",
            "explanation": "`pip config set global.index-url` تنظیم را در فایل pip.ini ذخیره می‌کند و از آن به بعد همه‌ی نصب‌ها از همان میرور انجام می‌شوند.",
            "choices": [
                {"text": "`python -m pip install --mirror iran`", "correct": False},
                {"text": "`python -m pip upgrade --index ir`", "correct": False},
                {"text": "`python -m venv .venv --mirror <آدرس میرور>`", "correct": False},
                {"text": "`python -m pip config set global.index-url <آدرس میرور>`", "correct": True},
            ],
        },
        {
            "text": "برای محاسبه‌ی دقیق پول (مثلاً جمع مبالغ ریالی اعشاری) کدام روش درست است؟",
            "explanation": "float به‌خاطر نمایش دودویی خطای گرد کردن دارد (`0.1 + 0.2 != 0.3`). Decimal باید از رشته ساخته شود؛ `Decimal(0.1)` همان خطای float را با خودش می‌آورد.",
            "choices": [
                {"text": "استفاده از float و گرد کردن با `round` در پایان", "correct": False},
                {"text": "ساختن `Decimal(0.1)` از عدد اعشاری", "correct": False},
                {"text": "ساختن `Decimal(\"0.1\")` از رشته", "correct": True},
                {"text": "ضرب همه‌ی اعداد در 10 و استفاده از float", "correct": False},
            ],
        },
        {
            "text": "حاصل `bool(\"False\")` چیست؟",
            "explanation": "هر رشته‌ی غیرخالی truthy است، حتی اگر متنش «False» باشد. فقط رشته‌ی خالی `\"\"` برابر False است.",
            "choices": [
                {"text": "True", "correct": True},
                {"text": "False", "correct": False},
                {"text": "None", "correct": False},
                {"text": "خطای ValueError", "correct": False},
            ],
        },
        {
            "text": "چرا `s.strip()` نیم‌فاصله‌ای را که اشتباهاً در انتهای یک کلمه‌ی فارسی آمده حذف نمی‌کند؟",
            "explanation": "نیم‌فاصله (ZWNJ، U+200C) از نظر یونیکد کاراکتر فاصله (whitespace) نیست؛ باید صریحاً آن را به strip بدهید.",
            "choices": [
                {"text": "چون strip فقط با رشته‌های ASCII کار می‌کند", "correct": False},
                {"text": "چون ZWNJ از نظر یونیکد whitespace نیست", "correct": True},
                {"text": "چون strip فقط ابتدای رشته را پاک می‌کند", "correct": False},
                {"text": "چون رشته‌های فارسی immutable نیستند", "correct": False},
            ],
        },
        {
            "text": "حاصل `\"۲۵۰\".isdigit()` چیست و چه پیامی برای اعتبارسنجی ورودی دارد؟",
            "explanation": "isdigit ارقام فارسی را هم رقم می‌داند و True می‌دهد؛ اگر فقط ارقام لاتین می‌خواهید باید `isascii()` را هم بررسی کنید یا ابتدا ارقام را با `str.translate` تبدیل کنید.",
            "choices": [
                {"text": "False؛ isdigit فقط ارقام لاتین را می‌شناسد", "correct": False},
                {"text": "خطای UnicodeError", "correct": False},
                {"text": "False؛ چون رشته باید اول به int تبدیل شود", "correct": False},
                {"text": "True؛ پس isdigit به‌تنهایی نشان نمی‌دهد ارقام لاتین هستند", "correct": True},
            ],
        },
        {
            "text": "در یک حلقه‌ی `for ... else`، بخش `else` چه زمانی اجرا می‌شود؟",
            "explanation": "else حلقه وقتی اجرا می‌شود که حلقه کامل تمام شود و با `break` قطع نشده باشد؛ برای الگوی «جست‌وجو کردم و پیدا نشد» مناسب است.",
            "choices": [
                {"text": "وقتی حلقه بدون break به پایان برسد", "correct": True},
                {"text": "فقط وقتی حلقه حتی یک بار هم اجرا نشود", "correct": False},
                {"text": "وقتی داخل حلقه استثنا رخ دهد", "correct": False},
                {"text": "همیشه، بعد از هر بار تکرار", "correct": False},
            ],
        },
        {
            "text": "در دستور `match`، کدام case نقش حالت پیش‌فرض (هر چیز دیگر) را دارد؟",
            "explanation": "`case _:` الگوی wildcard است و با هر مقداری تطبیق می‌خورد، بدون این‌که آن را به نامی ببندد.",
            "choices": [
                {"text": "`case default:`", "correct": False},
                {"text": "`case else:`", "correct": False},
                {"text": "`case _:`", "correct": True},
                {"text": "`case None:`", "correct": False},
            ],
        },
        {
            "text": "خروجی `list(range(1, 10, 3))` چیست؟",
            "explanation": "range از 1 شروع می‌کند، با گام 3 جلو می‌رود و خود 10 را شامل نمی‌شود: 1، 4، 7.",
            "choices": [
                {"text": "`[1, 4, 7, 10]`", "correct": False},
                {"text": "`[1, 4, 7]`", "correct": True},
                {"text": "`[3, 6, 9]`", "correct": False},
                {"text": "`[1, 3, 6, 9]`", "correct": False},
            ],
        },
        {
            "text": "حاصل `any([])` و `all([])` به ترتیب چیست؟",
            "explanation": "any روی ظرف خالی False است چون هیچ عضو truthy ای ندارد؛ all روی ظرف خالی True است چون هیچ عضو falsy ای پیدا نمی‌شود (درستی تهی).",
            "choices": [
                {"text": "True و True", "correct": False},
                {"text": "False و False", "correct": False},
                {"text": "True و False", "correct": False},
                {"text": "False و True", "correct": True},
            ],
        },
        {
            "text": "خروجی این کد چیست؟ `a = [1, 2]` سپس `b = a` سپس `b.append(3)` سپس `print(a)`",
            "explanation": "`b = a` لیست را کپی نمی‌کند؛ هر دو نام به یک شیء اشاره دارند، پس تغییر از طریق b در a هم دیده می‌شود.",
            "choices": [
                {"text": "`[1, 2]`", "correct": False},
                {"text": "`[1, 2, 3]`", "correct": True},
                {"text": "`[3]`", "correct": False},
                {"text": "خطای NameError", "correct": False},
            ],
        },
        {
            "text": "بعد از `grid = [[0] * 3] * 3` و `grid[0][0] = 1`، مقدار `grid` چیست؟",
            "explanation": "ضرب بیرونی سه ارجاع به همان یک لیست داخلی می‌سازد؛ پس تغییر یک سطر در همه دیده می‌شود. راه درست: `[[0] * 3 for _ in range(3)]`.",
            "choices": [
                {"text": "`[[1, 0, 0], [0, 0, 0], [0, 0, 0]]`", "correct": False},
                {"text": "خطای TypeError", "correct": False},
                {"text": "`[[1, 0, 0], [1, 0, 0], [1, 0, 0]]`", "correct": True},
                {"text": "`[[1, 1, 1], [0, 0, 0], [0, 0, 0]]`", "correct": False},
            ],
        },
        {
            "text": "کدام عبارت یک set خالی می‌سازد؟",
            "explanation": "`{}` دیکشنری خالی است؛ set خالی فقط با `set()` ساخته می‌شود.",
            "choices": [
                {"text": "`set()`", "correct": True},
                {"text": "`{}`", "correct": False},
                {"text": "`{,}`", "correct": False},
                {"text": "`[]`", "correct": False},
            ],
        },
        {
            "text": "حاصل `Counter([\"افشان\", \"ماهی\", \"افشان\"]).most_common(1)` چیست؟",
            "explanation": "most_common(n) لیستی از تاپل‌های (عضو، تعداد) برای n عضو پرتکرار برمی‌گرداند.",
            "choices": [
                {"text": "`\"افشان\"`", "correct": False},
                {"text": "`{\"افشان\": 2}`", "correct": False},
                {"text": "`2`", "correct": False},
                {"text": "`[(\"افشان\", 2)]`", "correct": True},
            ],
        },
        {
            "text": "با تعریف `def add(x, items=[]): items.append(x); return items`، اگر اول `add(1)` و بعد `add(2)` صدا زده شود، فراخوانی دوم چه برمی‌گرداند؟",
            "explanation": "مقدار پیش‌فرض فقط یک بار، هنگام تعریف تابع، ساخته می‌شود و بین فراخوانی‌ها مشترک است. الگوی درست `items=None` و ساختن لیست داخل تابع است.",
            "choices": [
                {"text": "`[2]`", "correct": False},
                {"text": "`[1, 2]`", "correct": True},
                {"text": "`[]`", "correct": False},
                {"text": "خطای TypeError", "correct": False},
            ],
        },
        {
            "text": "در تعریف `def make_order(code, *, price)`، پارامتر `price` چه ویژگی‌ای دارد؟",
            "explanation": "هر پارامتر بعد از `*` فقط به‌صورت keyword پذیرفته می‌شود؛ `make_order(\"KSH-1\", 100)` خطای TypeError می‌دهد و باید `price=100` نوشت.",
            "choices": [
                {"text": "اختیاری است و مقدار پیش‌فرض None دارد", "correct": False},
                {"text": "می‌تواند هر تعداد آرگومان موقعیتی بگیرد", "correct": False},
                {"text": "فقط با نام قابل ارسال است، مثل `price=100`", "correct": True},
                {"text": "فقط به‌صورت موقعیتی قابل ارسال است", "correct": False},
            ],
        },
        {
            "text": "ترتیب جست‌وجوی نام‌ها در پایتون (قاعده‌ی LEGB) کدام است؟",
            "explanation": "پایتون نام را به ترتیب در Local، Enclosing (تابع بیرونی)، Global (ماژول) و Built-in جست‌وجو می‌کند.",
            "choices": [
                {"text": "Local، Enclosing، Global، Built-in", "correct": True},
                {"text": "Global، Local، Built-in، Enclosing", "correct": False},
                {"text": "Built-in، Global، Enclosing، Local", "correct": False},
                {"text": "Local، Global، Enclosing، Built-in", "correct": False},
            ],
        },
        {
            "text": "خروجی `[f() for f in [lambda: i for i in range(3)]]` چیست؟",
            "explanation": "lambda ها متغیر i را نگه می‌دارند نه مقدارش را (late binding)؛ وقتی صدا زده می‌شوند i برابر 2 است. راه‌حل: `lambda i=i: i`.",
            "choices": [
                {"text": "`[0, 1, 2]`", "correct": False},
                {"text": "`[0, 0, 0]`", "correct": False},
                {"text": "خطای NameError", "correct": False},
                {"text": "`[2, 2, 2]`", "correct": True},
            ],
        },
        {
            "text": "فایل CSV فارسی را با چه encoding ای بنویسیم تا با دوبار کلیک در اکسل درست باز شود؟",
            "explanation": "`utf-8-sig` در ابتدای فایل BOM می‌گذارد و اکسل از روی آن می‌فهمد فایل UTF-8 است؛ بدون BOM، اکسل فارسی را درهم نشان می‌دهد.",
            "choices": [
                {"text": "`ascii`", "correct": False},
                {"text": "`utf-8-sig`", "correct": True},
                {"text": "`utf-16-be`", "correct": False},
                {"text": "`latin-1`", "correct": False},
            ],
        },
        {
            "text": "خروجی `json.dumps({\"نام\": \"رضا\"})` بدون آرگومان اضافه چه شکلی دارد و چطور فارسی خوانا می‌شود؟",
            "explanation": "پیش‌فرض `ensure_ascii=True` است و حروف غیرASCII را به‌صورت `\\uXXXX` می‌نویسد؛ با `ensure_ascii=False` متن فارسی همان‌طور که هست ذخیره می‌شود.",
            "choices": [
                {"text": "فارسی حذف می‌شود؛ باید `encoding=\"utf-8\"` داد", "correct": False},
                {"text": "خطای UnicodeEncodeError؛ باید `sort_keys=True` داد", "correct": False},
                {"text": "حروف به `\\uXXXX` تبدیل می‌شوند؛ با `ensure_ascii=False` خوانا می‌شود", "correct": True},
                {"text": "فارسی درست چاپ می‌شود و نیازی به تنظیم نیست", "correct": False},
            ],
        },
        {
            "text": "در ساختار `try / except / else / finally`، بخش `else` چه زمانی اجرا می‌شود؟",
            "explanation": "else فقط وقتی اجرا می‌شود که بلوک try بدون استثنا تمام شود؛ کدی که نباید زیر پوشش except باشد آن‌جا می‌رود. finally در هر حالت اجرا می‌شود.",
            "choices": [
                {"text": "وقتی هیچ استثنایی در try رخ نداده باشد", "correct": True},
                {"text": "همیشه، حتی اگر استثنا رخ داده باشد", "correct": False},
                {"text": "فقط وقتی except استثنا را دوباره raise کند", "correct": False},
                {"text": "قبل از اجرای بلوک try", "correct": False},
            ],
        },
        {
            "text": "دیکشنری `{1: \"a\"}` با `json.dumps` ذخیره و با `json.loads` خوانده می‌شود. نتیجه چیست؟",
            "explanation": "در JSON کلید شیء همیشه رشته است؛ کلید عددی بعد از رفت‌وبرگشت به `\"1\"` تبدیل می‌شود و `d[1]` دیگر کار نمی‌کند.",
            "choices": [
                {"text": "`{1: \"a\"}` بدون تغییر", "correct": False},
                {"text": "خطای TypeError هنگام dumps", "correct": False},
                {"text": "`[(1, \"a\")]`", "correct": False},
                {"text": "`{\"1\": \"a\"}`؛ کلید رشته شده است", "correct": True},
            ],
        },
        {
            "text": "هدف بلوک `if __name__ == \"__main__\":` چیست؟",
            "explanation": "وقتی فایل مستقیم اجرا شود `__name__` برابر `\"__main__\"` است و وقتی import شود برابر نام ماژول؛ پس کد آن بلوک هنگام import اجرا نمی‌شود.",
            "choices": [
                {"text": "سرعت اجرای برنامه را بیشتر می‌کند", "correct": False},
                {"text": "کد داخلش فقط وقتی فایل مستقیم اجرا شود اجرا می‌شود، نه هنگام import", "correct": True},
                {"text": "برای تعریف تابع اصلی برنامه اجباری است", "correct": False},
                {"text": "فایل را به پکیج تبدیل می‌کند", "correct": False},
            ],
        },
        {
            "text": "`ZoneInfo(\"Asia/Tehran\")` روی ویندوز خطای ZoneInfoNotFoundError می‌دهد. علت و راه‌حل چیست؟",
            "explanation": "ویندوز پایگاه داده‌ی منطقه‌های زمانی IANA را ندارد؛ نصب بسته‌ی `tzdata` با pip آن را در اختیار zoneinfo می‌گذارد.",
            "choices": [
                {"text": "نام درست `Iran/Tehran` است", "correct": False},
                {"text": "zoneinfo فقط در لینوکس وجود دارد؛ باید از سرور استفاده کرد", "correct": False},
                {"text": "ویندوز داده‌ی IANA ندارد؛ باید بسته‌ی `tzdata` را نصب کرد", "correct": True},
                {"text": "باید ساعت ویندوز را روی UTC گذاشت", "correct": False},
            ],
        },
        {
            "text": "برای ساختن کد تخفیف یا توکن ورود غیرقابل‌حدس، کدام ماژول مناسب است؟",
            "explanation": "random برای شبیه‌سازی و بازی است و خروجی‌اش قابل پیش‌بینی است؛ برای امنیت از `secrets` (مثلاً `secrets.token_urlsafe`) استفاده کنید.",
            "choices": [
                {"text": "`secrets`", "correct": True},
                {"text": "`random`", "correct": False},
                {"text": "`itertools`", "correct": False},
                {"text": "`uuid` با `uuid1()`", "correct": False},
            ],
        },
        {
            "text": "در یک dataclass نوشتن `tags: list = []` چه نتیجه‌ای دارد؟",
            "explanation": "dataclass پیش‌فرض mutable را رد می‌کند و ValueError می‌دهد تا از دام لیست مشترک جلوگیری کند؛ راه درست `field(default_factory=list)` است.",
            "choices": [
                {"text": "همه‌ی اشیاء یک لیست مشترک خواهند داشت، بدون هیچ خطایی", "correct": False},
                {"text": "پایتون خودکار برای هر شیء لیست جدا می‌سازد", "correct": False},
                {"text": "فیلد tags اجباری می‌شود", "correct": False},
                {"text": "خطای ValueError؛ باید `field(default_factory=list)` نوشت", "correct": True},
            ],
        },
        {
            "text": "در پروژه‌ی سفارش فرش، چرا ذخیره ابتدا در فایل موقت انجام می‌شود و بعد `os.replace` صدا زده می‌شود؟",
            "explanation": "اگر وسط نوشتن برنامه بیفتد یا برق برود، فایل اصلی دست‌نخورده می‌ماند؛ os.replace جایگزینی را اتمیک و روی ویندوز و لینوکس یکسان انجام می‌دهد.",
            "choices": [
                {"text": "چون json.dump نمی‌تواند مستقیم در فایل اصلی بنویسد", "correct": False},
                {"text": "تا فایل اصلی هرگز نیمه‌نوشته یا خراب نماند", "correct": True},
                {"text": "چون os.replace فایل را فشرده می‌کند", "correct": False},
                {"text": "تا فایل به‌صورت خودکار پشتیبان‌گیری شود", "correct": False},
            ],
        },
        {
            "text": "درخواستی با `requests.get(url)` بدون آرگومان timeout فرستاده می‌شود و سرور جواب نمی‌دهد. چه اتفاقی می‌افتد؟",
            "explanation": "requests هیچ timeout پیش‌فرضی ندارد؛ درخواست می‌تواند برای همیشه منتظر بماند. همیشه timeout بدهید، مثلاً `timeout=(3.05, 10)`.",
            "choices": [
                {"text": "بعد از 30 ثانیه خطای Timeout می‌دهد", "correct": False},
                {"text": "بعد از 3 تلاش خودکار متوقف می‌شود", "correct": False},
                {"text": "ممکن است برای همیشه منتظر بماند", "correct": True},
                {"text": "فوراً ConnectionError می‌دهد", "correct": False},
            ],
        },
        {
            "text": "یک Session با Retry روی کدهای 503 پیکربندی شده و سرور مدام 503 می‌دهد. پس از تمام شدن تلاش‌ها کدام استثنا رخ می‌دهد؟",
            "explanation": "وقتی تلاش‌های Retry روی status_forcelist تمام شود، requests استثنای `requests.exceptions.RetryError` می‌دهد، نه HTTPError؛ پس باید آن را هم جدا گرفت.",
            "choices": [
                {"text": "`requests.exceptions.RetryError`", "correct": True},
                {"text": "`requests.HTTPError`", "correct": False},
                {"text": "`requests.Timeout`", "correct": False},
                {"text": "هیچ استثنایی؛ پاسخ 503 برگردانده می‌شود", "correct": False},
            ],
        },
        {
            "text": "fixture آماده‌ی `tmp_path` در pytest چه کاری انجام می‌دهد؟",
            "explanation": "tmp_path برای هر تست یک پوشه‌ی موقت تازه (از نوع pathlib.Path) می‌سازد؛ تست‌ها فایل واقعی مثل orders.json را دست نمی‌زنند و از هم مستقل می‌مانند.",
            "choices": [
                {"text": "خروجی print تست را ذخیره می‌کند", "correct": False},
                {"text": "مسیر پروژه را به sys.path اضافه می‌کند", "correct": False},
                {"text": "تست را چند بار با ورودی‌های مختلف اجرا می‌کند", "correct": False},
                {"text": "برای هر تست یک پوشه‌ی موقت تازه به‌صورت Path می‌دهد", "correct": True},
            ],
        },
        {
            "text": "`python -m pytest` درست اجرا می‌شود ولی دستور `pytest` خالی خطای `No module named 'store'` می‌دهد. علت چیست؟",
            "explanation": "`python -m` پوشه‌ی جاری را به sys.path اضافه می‌کند ولی اجرای مستقیم `pytest` این کار را نمی‌کند؛ تنظیم `pythonpath = [\".\"]` در pyproject.toml رفتار را یکسان می‌کند.",
            "choices": [
                {"text": "فایل store.py باید به test_store.py تغییر نام دهد", "correct": False},
                {"text": "فقط `python -m` پوشه‌ی جاری را به sys.path اضافه می‌کند", "correct": True},
                {"text": "pytest خالی فقط با پایتون 2 کار می‌کند", "correct": False},
                {"text": "venv باید غیرفعال شود", "correct": False},
            ],
        },
        {
            "text": "برنامه‌ای چند `breakpoint()` جامانده دارد و می‌خواهید بدون تغییر کد، بدون توقف اجرایش کنید. چه می‌کنید؟",
            "explanation": "متغیر محیطی `PYTHONBREAKPOINT=0` همه‌ی فراخوانی‌های breakpoint() را بی‌اثر می‌کند؛ هرچند بهتر است breakpoint ها اصلاً commit نشوند.",
            "choices": [
                {"text": "با `python -O` اجرا می‌کنم", "correct": False},
                {"text": "فرمان `q` را در pdb از قبل تایپ می‌کنم", "correct": False},
                {"text": "متغیر محیطی `PYTHONBREAKPOINT=0` را تنظیم می‌کنم", "correct": True},
                {"text": "فایل `__pycache__` را پاک می‌کنم", "correct": False},
            ],
        },
        {
            "text": "خواندن یک فایل متنی قدیمی ویندوزی خطای `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc7` می‌دهد. بهترین برخورد کدام است؟",
            "explanation": "این فایل‌ها معمولاً cp1256 هستند. ترتیب درست: اول UTF-8، بعد cp1256؛ چون cp1256 تقریباً هر بایتی را بدون خطا می‌خواند و اگر اول بیاید، فایل UTF-8 هم به‌صورت حروف درهم «باز» می‌شود.",
            "choices": [
                {"text": "همیشه اول cp1256 را امتحان کنید چون هیچ‌وقت خطا نمی‌دهد", "correct": False},
                {"text": "با `errors=\"ignore\"` بخوانید تا خطا نیاید", "correct": False},
                {"text": "فایل را با حالت `\"rb\"` باز کنید و همان bytes را چاپ کنید", "correct": False},
                {"text": "اول UTF-8، در صورت خطا `encoding=\"cp1256\"`، و بعد فایل را با UTF-8 دوباره ذخیره کنید", "correct": True},
            ],
        },
    ],
}

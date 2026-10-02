# -*- coding: utf-8 -*-

COURSE = {
    "slug": "python-advanced",
    "title": "پایتون پیشرفته",
    "category": "برنامه‌نویسی",
    "level": "advanced",
    "summary": "تسلط بر مفاهیم پیشرفته‌ی پایتون: OOP عمیق، دکوراتور، جنراتور، asyncio و تست حرفه‌ای.",
    "description": (
        "<p>این دوره برای کسانی طراحی شده که پایه‌های پایتون را می‌دانند و می‌خواهند به سطح "
        "یک برنامه‌نویس حرفه‌ای برسند. تمرکز دوره روی مفاهیمی است که در پروژه‌های واقعی و "
        "کدهای کتابخانه‌ای پیشرفته دیده می‌شوند اما در آموزش‌های مقدماتی معمولاً پوشش داده "
        "نمی‌شوند.</p>"
        "<p>در طول دوره به‌صورت عمیق با برنامه‌نویسی شیءگرا و متدهای ویژه، دکوراتورها، "
        "جنراتورها و ایتریتورها، مدیریت منابع با context manager، نوع‌نویسی (type hints) و "
        "dataclass، برنامه‌نویسی ناهم‌گام با asyncio، نوشتن تست حرفه‌ای با pytest و در نهایت "
        "بسته‌بندی و انتشار کتابخانه‌ی خودتان آشنا می‌شوید.</p>"
        "<p>پیش‌نیاز این دوره، تسلط به مفاهیم پایه‌ی پایتون شامل متغیر، شرط، حلقه، تابع و "
        "ساختارهای داده است. اگر تازه شروع کرده‌اید، پیشنهاد می‌شود ابتدا دوره‌ی «آموزش پایتون» "
        "را بگذرانید.</p>"
    ),
    "price": 1200000,
    "duration_minutes": 720,
    "tags": ["پایتون", "برنامه‌نویسی", "پیشرفته", "OOP", "asyncio"],
    "modules": [
        {
            "title": "فصل اول: کلاس‌ها و برنامه‌نویسی شیءگرای عمیق",
            "lessons": [
                {
                    "title": "مروری سریع بر کلاس و شیء در پایتون",
                    "kind": "text",
                    "minutes": 14,
                    "is_preview": True,
                    "body": (
                        "<h2>یادآوری مفاهیم پایه‌ی شیءگرایی</h2>"
                        "<p>پیش از ورود به مباحث عمیق‌تر، لازم است روی مفاهیم اولیه‌ی کلاس و شیء "
                        "مروری کوتاه داشته باشیم. کلاس یک قالب برای ساخت شیء است و شیء نمونه‌ای "
                        "واقعی از آن قالب با مقادیر مشخص.</p>"
                        "<pre><code class=\"language-python\">class Book:\n"
                        "    def __init__(self, title, author, pages):\n"
                        "        self.title = title\n"
                        "        self.author = author\n"
                        "        self.pages = pages\n\n"
                        "    def summary(self):\n"
                        "        return f\"{self.title} نوشته‌ی {self.author} ({self.pages} صفحه)\"\n\n"
                        "book = Book(\"کیمیاگر\", \"پائولو کوئیلو\", 210)\n"
                        "print(book.summary())</code></pre>"
                        "<p>متد <code>__init__</code> سازنده‌ی کلاس نام دارد و هنگام ساخت هر شیء "
                        "جدید به‌صورت خودکار اجرا می‌شود. پارامتر <code>self</code> اشاره به همان "
                        "شیءِ در حال ساخته‌شدن دارد و باید به‌عنوان اولین پارامتر هر متد نمونه "
                        "(instance method) نوشته شود.</p>"
                        "<p>در این دوره فرض بر این است که مفاهیمی مانند تعریف کلاس، ویژگی‌های نمونه "
                        "(instance attributes) و متدهای معمولی را می‌دانید. از این درس به بعد، وارد "
                        "مباحثی مانند وراثت چندگانه، متدهای ویژه و کپسوله‌سازی واقعی می‌شویم که در "
                        "پروژه‌های حرفه‌ای و کتابخانه‌های معروف پایتون به‌وفور دیده می‌شوند.</p>"
                    ),
                },
                {
                    "title": "وراثت، MRO و super()",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": (
                        "<h2>وراثت چندگانه و ترتیب تفکیک متد</h2>"
                        "<p>پایتون از <strong>وراثت چندگانه</strong> پشتیبانی می‌کند، یعنی یک کلاس "
                        "می‌تواند از چند کلاس والد به‌طور همزمان ارث‌بری کند. این قابلیت قدرتمند "
                        "است اما اگر بدون دقت استفاده شود، می‌تواند به ابهام در فراخوانی متدها "
                        "منجر شود.</p>"
                        "<pre><code class=\"language-python\">class Flyable:\n"
                        "    def move(self):\n"
                        "        return \"در حال پرواز\"\n\n"
                        "class Swimmable:\n"
                        "    def move(self):\n"
                        "        return \"در حال شنا\"\n\n"
                        "class Duck(Flyable, Swimmable):\n"
                        "    pass\n\n"
                        "d = Duck()\n"
                        "print(d.move())          # در حال پرواز\n"
                        "print(Duck.__mro__)      # ترتیب جست‌وجوی متد</code></pre>"
                        "<p>پایتون برای تعیین این‌که کدام متد فراخوانی شود، از الگوریتمی به نام "
                        "<strong>MRO</strong> (Method Resolution Order) استفاده می‌کند که بر پایه‌ی "
                        "الگوریتم C3 است. می‌توانید این ترتیب را با <code>ClassName.__mro__</code> "
                        "یا <code>ClassName.mro()</code> مشاهده کنید.</p>"
                        "<p>تابع <code>super()</code> ابزاری است که به شما اجازه می‌دهد بدون ذکر "
                        "مستقیم نام کلاس والد، متد آن را فراخوانی کنید. این کار به‌ویژه در وراثت "
                        "چندگانه اهمیت زیادی دارد چون با تغییر ساختار وراثت، کد شما همچنان درست "
                        "کار می‌کند:</p>"
                        "<pre><code class=\"language-python\">class Animal:\n"
                        "    def __init__(self, name):\n"
                        "        self.name = name\n\n"
                        "class Dog(Animal):\n"
                        "    def __init__(self, name, breed):\n"
                        "        super().__init__(name)\n"
                        "        self.breed = breed</code></pre>"
                        "<p>توصیه‌ی عملی در پروژه‌های واقعی این است که وراثت چندگانه را فقط زمانی "
                        "به کار ببرید که واقعاً معنادار باشد، مثل الگوی «میکسین» (mixin) که در "
                        "فریمورک‌هایی مانند جنگو نیز دیده می‌شود.</p>"
                    ),
                },
                {
                    "title": "متدهای ویژه (Dunder Methods)",
                    "kind": "text",
                    "minutes": 19,
                    "is_preview": False,
                    "body": (
                        "<h2>سفارشی‌سازی رفتار شیء با متدهای دو خط زیرین</h2>"
                        "<p>متدهایی که با دو خط زیرین شروع و تمام می‌شوند (مانند "
                        "<code>__init__</code>) به آن‌ها <strong>dunder methods</strong> گفته "
                        "می‌شود و رفتار داخلی شیء را در برابر عملگرها و توابع داخلی پایتون تعیین "
                        "می‌کنند.</p>"
                        "<pre><code class=\"language-python\">class Money:\n"
                        "    def __init__(self, amount):\n"
                        "        self.amount = amount\n\n"
                        "    def __add__(self, other):\n"
                        "        return Money(self.amount + other.amount)\n\n"
                        "    def __repr__(self):\n"
                        "        return f\"Money({self.amount})\"\n\n"
                        "    def __eq__(self, other):\n"
                        "        return self.amount == other.amount\n\n"
                        "a = Money(1000)\n"
                        "b = Money(500)\n"
                        "print(a + b)        # Money(1500)\n"
                        "print(a == Money(1000))   # True</code></pre>"
                        "<p>با پیاده‌سازی <code>__add__</code> عملگر <code>+</code> روی اشیای کلاس "
                        "شما نیز کار می‌کند. متدهای مشابه دیگری مانند <code>__sub__</code>، "
                        "<code>__lt__</code> (کوچک‌تر بودن)، <code>__len__</code> و "
                        "<code>__str__</code> نیز به همین شکل رفتار شیء را در برابر عملگرها و "
                        "توابع داخلی مانند <code>len()</code> یا <code>print()</code> تعیین "
                        "می‌کنند.</p>"
                        "<p>تفاوت <code>__repr__</code> و <code>__str__</code> این است که "
                        "<code>__repr__</code> برای نمایش فنی و دقیق شیء (مثلاً در دیباگر) در نظر "
                        "گرفته شده، در حالی که <code>__str__</code> برای نمایش خوانا به کاربر است. "
                        "اگر فقط یکی را تعریف کنید، پایتون در نبود <code>__str__</code> از "
                        "<code>__repr__</code> استفاده می‌کند.</p>"
                    ),
                },
                {
                    "title": "کپسوله‌سازی با property و attribute خصوصی",
                    "kind": "text",
                    "minutes": 17,
                    "is_preview": False,
                    "body": (
                        "<h2>کنترل دسترسی به ویژگی‌های شیء</h2>"
                        "<p>پایتون سطح دسترسی سخت‌گیرانه مانند private در برخی زبان‌های دیگر ندارد، "
                        "اما با قرارداد نام‌گذاری و دکوراتور <code>@property</code> می‌توان "
                        "کپسوله‌سازی مؤثری پیاده کرد. نام‌گذاری با یک خط زیرین (<code>_name</code>) "
                        "یعنی «داخلی» و استفاده‌ی مستقیم از بیرون توصیه نمی‌شود؛ نام‌گذاری با دو خط "
                        "زیرین (<code>__name</code>) باعث name mangling شده و دسترسی مستقیم از "
                        "بیرون کلاس را دشوارتر می‌کند.</p>"
                        "<pre><code class=\"language-python\">class Account:\n"
                        "    def __init__(self, balance):\n"
                        "        self._balance = balance\n\n"
                        "    @property\n"
                        "    def balance(self):\n"
                        "        return self._balance\n\n"
                        "    @balance.setter\n"
                        "    def balance(self, value):\n"
                        "        if value &lt; 0:\n"
                        "            raise ValueError(\"موجودی نمی‌تواند منفی باشد\")\n"
                        "        self._balance = value\n\n"
                        "acc = Account(1000)\n"
                        "acc.balance = 1500     # از طریق setter\n"
                        "print(acc.balance)     # از طریق getter</code></pre>"
                        "<p>مزیت اصلی <code>property</code> این است که از بیرون کلاس، دسترسی به "
                        "<code>balance</code> دقیقاً مثل یک ویژگی معمولی به نظر می‌رسد، در حالی که "
                        "در پشت صحنه اعتبارسنجی و منطق دلخواه اجرا می‌شود. این الگو به شما اجازه "
                        "می‌دهد بدون تغییر رابط بیرونی کلاس، منطق داخلی را تغییر دهید؛ یکی از "
                        "اصول مهم طراحی نرم‌افزار پایدار.</p>"
                        "<p>همچنین می‌توانید <code>@property</code> بدون setter تعریف کنید تا "
                        "ویژگی فقط‌خواندنی باشد، که برای مقادیر محاسبه‌شده مانند سطح یک دایره بر "
                        "اساس شعاع آن بسیار مناسب است.</p>"
                    ),
                },
            ],
        },
        {
            "title": "فصل دوم: دکوراتورها",
            "lessons": [
                {
                    "title": "توابع به عنوان شیء درجه‌یک",
                    "kind": "text",
                    "minutes": 14,
                    "is_preview": False,
                    "body": (
                        "<h2>پیش‌نیاز درک دکوراتور: تابع به‌عنوان مقدار</h2>"
                        "<p>در پایتون، توابع <strong>شیء درجه‌یک</strong> (first-class object) "
                        "هستند؛ یعنی می‌توان آن‌ها را در متغیر ذخیره کرد، به‌عنوان آرگومان به تابع "
                        "دیگر پاس داد یا از یک تابع بازگرداند. این ویژگی پایه‌ی درک دکوراتورهاست.</p>"
                        "<pre><code class=\"language-python\">def shout(text):\n"
                        "    return text.upper()\n\n"
                        "def apply(func, value):\n"
                        "    return func(value)\n\n"
                        "print(apply(shout, \"hello\"))   # HELLO</code></pre>"
                        "<p>می‌توانیم یک تابع را از داخل تابع دیگر بازگردانیم و به همراه خود، محیط "
                        "متغیرهای اطراف را نیز حفظ کند؛ به این ویژگی <strong>closure</strong> "
                        "گفته می‌شود:</p>"
                        "<pre><code class=\"language-python\">def make_multiplier(factor):\n"
                        "    def multiplier(number):\n"
                        "        return number * factor\n"
                        "    return multiplier\n\n"
                        "double = make_multiplier(2)\n"
                        "triple = make_multiplier(3)\n\n"
                        "print(double(5))   # 10\n"
                        "print(triple(5))   # 15</code></pre>"
                        "<p>در این مثال، تابع درونی <code>multiplier</code> حتی پس از پایان اجرای "
                        "<code>make_multiplier</code>، همچنان به مقدار <code>factor</code> دسترسی "
                        "دارد. این دقیقاً همان مکانیزمی است که دکوراتورها بر پایه‌ی آن ساخته "
                        "می‌شوند و در درس بعد آن را به‌طور کامل بررسی می‌کنیم.</p>"
                        "<p>نکته‌ی مهم این است که closure فقط مقدار متغیر را کپی نمی‌کند، بلکه به "
                        "خود متغیر در محدوده‌ی تابع بیرونی ارجاع می‌دهد. به همین دلیل اگر تابع "
                        "بیرونی چند بار با آرگومان‌های متفاوت فراخوانی شود، هر بار یک closure "
                        "کاملاً مستقل با محیط متغیرهای مخصوص به خودش ساخته می‌شود، بدون این‌که "
                        "closureهای مختلف روی مقدار یکدیگر تأثیر بگذارند. همین رفتار است که به "
                        "توابع تولیدشده در مثال بالا (<code>double</code> و <code>triple</code>) "
                        "اجازه می‌دهد کاملاً مستقل از هم رفتار کنند، حتی با این‌که هر دو از یک "
                        "تابع سازنده ساخته شده‌اند.</p>"
                    ),
                },
                {
                    "title": "نوشتن اولین دکوراتور",
                    "kind": "text",
                    "minutes": 18,
                    "is_preview": False,
                    "body": (
                        "<h2>دکوراتور چیست و چگونه کار می‌کند؟</h2>"
                        "<p>دکوراتور تابعی است که یک تابع دیگر را به‌عنوان ورودی می‌گیرد، رفتاری "
                        "به آن اضافه می‌کند و تابعی جدید بازمی‌گرداند، بدون این‌که کد اصلی تابع "
                        "تغییر کند. این الگو برای اضافه کردن قابلیت‌هایی مانند لاگ‌گیری، اندازه‌گیری "
                        "زمان اجرا یا کنترل دسترسی بسیار رایج است.</p>"
                        "<pre><code class=\"language-python\">import time\n\n"
                        "def timer(func):\n"
                        "    def wrapper(*args, **kwargs):\n"
                        "        start = time.time()\n"
                        "        result = func(*args, **kwargs)\n"
                        "        elapsed = time.time() - start\n"
                        "        print(f\"{func.__name__} در {elapsed:.4f} ثانیه اجرا شد\")\n"
                        "        return result\n"
                        "    return wrapper\n\n"
                        "@timer\n"
                        "def slow_square(n):\n"
                        "    time.sleep(0.5)\n"
                        "    return n * n\n\n"
                        "print(slow_square(4))</code></pre>"
                        "<p>نوشتن <code>@timer</code> بالای تعریف تابع، دقیقاً معادل نوشتن "
                        "<code>slow_square = timer(slow_square)</code> است. استفاده از "
                        "<code>*args</code> و <code>**kwargs</code> در تابع <code>wrapper</code> "
                        "باعث می‌شود دکوراتور برای هر تابعی با هر تعداد آرگومان کار کند.</p>"
                        "<p>یکی از کاربردهای بسیار رایج دکوراتور در پروژه‌های واقعی، دکوراتورهای "
                        "فریمورک جنگو مانند <code>@login_required</code> است که پیش از اجرای یک "
                        "ویو، بررسی می‌کند کاربر وارد سیستم شده باشد؛ همان الگویی که در این درس "
                        "دیدیم، فقط با منطق متفاوت.</p>"
                    ),
                },
                {
                    "title": "دکوراتور با آرگومان و functools.wraps",
                    "kind": "text",
                    "minutes": 18,
                    "is_preview": False,
                    "body": (
                        "<h2>دکوراتورهای پارامتری و حفظ متادیتای تابع</h2>"
                        "<p>گاهی لازم است خود دکوراتور نیز آرگومان بگیرد؛ برای مثال دکوراتوری که "
                        "تعداد دفعات تکرار یک تابع را مشخص می‌کند. برای این کار به یک لایه‌ی "
                        "اضافه‌ی تودرتو نیاز داریم.</p>"
                        "<pre><code class=\"language-python\">from functools import wraps\n\n"
                        "def repeat(times):\n"
                        "    def decorator(func):\n"
                        "        @wraps(func)\n"
                        "        def wrapper(*args, **kwargs):\n"
                        "            result = None\n"
                        "            for _ in range(times):\n"
                        "                result = func(*args, **kwargs)\n"
                        "            return result\n"
                        "        return wrapper\n"
                        "    return decorator\n\n"
                        "@repeat(times=3)\n"
                        "def greet(name):\n"
                        "    print(f\"سلام {name}\")\n\n"
                        "greet(\"نیما\")</code></pre>"
                        "<p>در این ساختار سه‌لایه، <code>repeat</code> آرگومان می‌گیرد و "
                        "<code>decorator</code> واقعی را می‌سازد که خودش تابع اصلی را می‌گیرد. این "
                        "الگو ممکن است در ابتدا گیج‌کننده باشد، اما با تمرین کاملاً قابل درک "
                        "می‌شود.</p>"
                        "<p>نکته‌ی بسیار مهم استفاده از <code>@wraps(func)</code> از ماژول "
                        "<code>functools</code> است. بدون آن، پس از اعمال دکوراتور، ویژگی‌های "
                        "تابع اصلی مانند <code>__name__</code> و مستندات آن (docstring) با "
                        "ویژگی‌های تابع <code>wrapper</code> جایگزین می‌شوند که دیباگ کردن برنامه "
                        "را دشوار می‌کند. <code>wraps</code> این متادیتا را از تابع اصلی حفظ "
                        "می‌کند و استفاده از آن در هر دکوراتور حرفه‌ای یک قاعده‌ی استاندارد است.</p>"
                    ),
                },
            ],
        },
        {
            "title": "فصل سوم: جنراتورها و ایتریتورها",
            "lessons": [
                {
                    "title": "پروتکل Iterable و Iterator",
                    "kind": "text",
                    "minutes": 16,
                    "is_preview": False,
                    "body": (
                        "<h2>چه چیزی یک شیء را قابل پیمایش می‌کند؟</h2>"
                        "<p>وقتی از <code>for item in my_list</code> استفاده می‌کنید، در پشت "
                        "صحنه پایتون از یک پروتکل استاندارد استفاده می‌کند. هر شیئی که متد "
                        "<code>__iter__</code> را پیاده‌سازی کند، <strong>iterable</strong> نام "
                        "دارد و هر شیئی که متد <code>__next__</code> را داشته باشد، "
                        "<strong>iterator</strong> است.</p>"
                        "<pre><code class=\"language-python\">class CountUp:\n"
                        "    def __init__(self, limit):\n"
                        "        self.limit = limit\n"
                        "        self.current = 0\n\n"
                        "    def __iter__(self):\n"
                        "        return self\n\n"
                        "    def __next__(self):\n"
                        "        if self.current &gt;= self.limit:\n"
                        "            raise StopIteration\n"
                        "        self.current += 1\n"
                        "        return self.current\n\n"
                        "for number in CountUp(5):\n"
                        "    print(number)   # 1 2 3 4 5</code></pre>"
                        "<p>حلقه‌ی <code>for</code> ابتدا <code>__iter__</code> شیء را فراخوانی "
                        "می‌کند تا یک iterator بگیرد، سپس به‌طور مکرر <code>__next__</code> را "
                        "صدا می‌زند تا وقتی که <code>StopIteration</code> صادر شود. توابع داخلی "
                        "<code>iter()</code> و <code>next()</code> نیز دقیقاً همین دو متد را "
                        "فراخوانی می‌کنند.</p>"
                        "<p>پیاده‌سازی دستی این پروتکل کمی طولانی است؛ به همین دلیل پایتون راهی "
                        "بسیار ساده‌تر به نام <strong>جنراتور</strong> ارائه می‌دهد که در درس بعد "
                        "با آن آشنا می‌شویم.</p>"
                    ),
                },
                {
                    "title": "جنراتورها و کلیدواژه‌ی yield",
                    "kind": "text",
                    "minutes": 19,
                    "is_preview": False,
                    "body": (
                        "<h2>ساخت ایتریتور به سبک ساده با generator</h2>"
                        "<p>جنراتور تابعی است که به‌جای <code>return</code> از کلیدواژه‌ی "
                        "<code>yield</code> استفاده می‌کند. هر بار که <code>yield</code> اجرا "
                        "شود، مقدار برگردانده می‌شود اما وضعیت تابع (متغیرها و محل اجرا) حفظ "
                        "می‌شود تا فراخوانی بعدی از همان‌جا ادامه یابد.</p>"
                        "<pre><code class=\"language-python\">def count_up(limit):\n"
                        "    current = 1\n"
                        "    while current &lt;= limit:\n"
                        "        yield current\n"
                        "        current += 1\n\n"
                        "for number in count_up(5):\n"
                        "    print(number)   # 1 2 3 4 5</code></pre>"
                        "<p>مزیت بزرگ جنراتورها، <strong>محاسبه‌ی تنبل</strong> (lazy evaluation) "
                        "است؛ یعنی مقادیر فقط در لحظه‌ی نیاز تولید می‌شوند، نه همه‌باهم از قبل. این "
                        "ویژگی برای کار با داده‌های بسیار بزرگ یا حتی بی‌نهایت، صرفه‌جویی زیادی در "
                        "مصرف حافظه ایجاد می‌کند:</p>"
                        "<pre><code class=\"language-python\">def infinite_numbers():\n"
                        "    n = 1\n"
                        "    while True:\n"
                        "        yield n\n"
                        "        n += 1\n\n"
                        "gen = infinite_numbers()\n"
                        "print(next(gen))   # 1\n"
                        "print(next(gen))   # 2</code></pre>"
                        "<p>همچنین <strong>عبارت جنراتوری</strong> (generator expression) نسخه‌ی "
                        "فشرده‌ی list comprehension است که به‌جای براکت از پرانتز استفاده می‌کند و "
                        "نتیجه را به‌صورت تنبل تولید می‌کند: <code>(n * n for n in range(1000000))</code>. "
                        "برخلاف list comprehension، این عبارت تمام مقادیر را همزمان در حافظه "
                        "نگه نمی‌دارد.</p>"
                    ),
                },
                {
                    "title": "ماژول itertools برای ترکیب و پردازش داده",
                    "kind": "text",
                    "minutes": 15,
                    "is_preview": False,
                    "body": (
                        "<h2>ابزارهای آماده برای کار با ایتریتورها</h2>"
                        "<p>ماژول استاندارد <code>itertools</code> مجموعه‌ای از توابع کارآمد برای "
                        "کار با ایتریتورها فراهم می‌کند که نوشتن دستی آن‌ها زمان‌بر و مستعد خطا "
                        "است.</p>"
                        "<pre><code class=\"language-python\">from itertools import chain, cycle, islice, count\n\n"
                        "a = [1, 2, 3]\n"
                        "b = [4, 5, 6]\n"
                        "print(list(chain(a, b)))          # [1, 2, 3, 4, 5, 6]\n\n"
                        "counter = count(start=10, step=5)\n"
                        "print(list(islice(counter, 4)))   # [10, 15, 20, 25]</code></pre>"
                        "<p>در این مثال، <code>chain</code> چند ایتریبل را پشت‌سر‌هم متصل می‌کند، "
                        "<code>count</code> یک شمارنده‌ی بی‌نهایت با گام دلخواه می‌سازد و "
                        "<code>islice</code> بخشی از یک ایتریتور (حتی بی‌نهایت) را بدون نیاز به "
                        "تبدیل کامل آن به لیست استخراج می‌کند.</p>"
                        "<p>تابع <code>groupby</code> نیز برای دسته‌بندی داده‌های مرتب‌شده بر اساس "
                        "یک کلید بسیار پرکاربرد است:</p>"
                        "<pre><code class=\"language-python\">from itertools import groupby\n\n"
                        "words = [\"apple\", \"ant\", \"bear\", \"bee\", \"cat\"]\n"
                        "for letter, group in groupby(words, key=lambda w: w[0]):\n"
                        "    print(letter, list(group))</code></pre>"
                        "<p>نکته‌ی مهم این است که <code>groupby</code> فقط عناصر <strong>پیوسته</strong> "
                        "با کلید یکسان را در یک گروه قرار می‌دهد، پس معمولاً پیش از استفاده از آن "
                        "باید داده را بر اساس همان کلید مرتب کرد. تسلط به <code>itertools</code> "
                        "کد پردازش داده را کوتاه‌تر، سریع‌تر و کم‌حافظه‌تر می‌کند.</p>"
                    ),
                },
            ],
        },
        {
            "title": "فصل چهارم: Context Manager، Type Hints و Dataclass",
            "lessons": [
                {
                    "title": "دستور with و نوشتن context manager سفارشی",
                    "kind": "text",
                    "minutes": 17,
                    "is_preview": False,
                    "body": (
                        "<h2>مدیریت خودکار منابع با with</h2>"
                        "<p>پیش‌تر دیده‌اید که دستور <code>with</code> برای باز و بسته کردن خودکار "
                        "فایل استفاده می‌شود. این رفتار بر پایه‌ی پروتکلی به نام "
                        "<strong>context manager</strong> ساخته شده که هر شیء با پیاده‌سازی دو "
                        "متد <code>__enter__</code> و <code>__exit__</code> می‌تواند از آن "
                        "پشتیبانی کند.</p>"
                        "<pre><code class=\"language-python\">class Timer:\n"
                        "    def __enter__(self):\n"
                        "        import time\n"
                        "        self.start = time.time()\n"
                        "        return self\n\n"
                        "    def __exit__(self, exc_type, exc_value, traceback):\n"
                        "        import time\n"
                        "        print(f\"زمان سپری‌شده: {time.time() - self.start:.4f} ثانیه\")\n"
                        "        return False\n\n"
                        "with Timer():\n"
                        "    total = sum(range(1_000_000))</code></pre>"
                        "<p>متد <code>__enter__</code> هنگام ورود به بلوک <code>with</code> اجرا "
                        "می‌شود و مقدار بازگشتی آن (در صورت استفاده از <code>as</code>) در اختیار "
                        "قرار می‌گیرد. متد <code>__exit__</code> نیز صرف‌نظر از این‌که خطایی رخ داده "
                        "باشد یا نه، در پایان بلوک اجرا می‌شود؛ همین ویژگی است که آن را برای مدیریت "
                        "منابعی مانند فایل، اتصال شبکه یا قفل (lock) بسیار مناسب می‌کند.</p>"
                        "<p>روش کوتاه‌تر برای نوشتن context manager، استفاده از دکوراتور "
                        "<code>@contextmanager</code> از ماژول <code>contextlib</code> است که در "
                        "درس بعد بررسی می‌کنیم و نیاز به تعریف کلاس جداگانه را حذف می‌کند.</p>"
                    ),
                },
                {
                    "title": "ساده‌سازی با contextlib.contextmanager",
                    "kind": "text",
                    "minutes": 14,
                    "is_preview": False,
                    "body": (
                        "<h2>نوشتن context manager با یک تابع جنراتور</h2>"
                        "<p>ماژول <code>contextlib</code> دکوراتوری به نام "
                        "<code>@contextmanager</code> ارائه می‌دهد که با استفاده از "
                        "<code>yield</code> می‌توان یک context manager کامل را تنها با یک تابع "
                        "نوشت، بدون نیاز به کلاس و دو متد جداگانه.</p>"
                        "<pre><code class=\"language-python\">from contextlib import contextmanager\n"
                        "import time\n\n"
                        "@contextmanager\n"
                        "def timer():\n"
                        "    start = time.time()\n"
                        "    try:\n"
                        "        yield\n"
                        "    finally:\n"
                        "        print(f\"زمان سپری‌شده: {time.time() - start:.4f} ثانیه\")\n\n"
                        "with timer():\n"
                        "    total = sum(range(1_000_000))</code></pre>"
                        "<p>هر کدی که پیش از <code>yield</code> نوشته شود معادل <code>__enter__</code> "
                        "است و هر کدی که بعد از آن (در بلوک <code>finally</code>) بیاید معادل "
                        "<code>__exit__</code>. اگر داخل بلوک <code>with</code> خطایی رخ دهد، همان "
                        "خطا در نقطه‌ی <code>yield</code> بازپخش می‌شود، بنابراین استفاده از "
                        "<code>try/finally</code> برای تضمین اجرای کد پاک‌سازی ضروری است.</p>"
                        "<p>ماژول <code>contextlib</code> ابزارهای مفید دیگری نیز دارد، از جمله "
                        "<code>suppress</code> برای نادیده گرفتن خطاهای خاص و "
                        "<code>ExitStack</code> برای مدیریت چند context manager به‌صورت پویا. این "
                        "ابزارها به‌ویژه در کد کتابخانه‌ای و ابزارهای خط فرمان حرفه‌ای بسیار "
                        "پرکاربرد هستند.</p>"
                    ),
                },
                {
                    "title": "Type Hints برای کد ایمن‌تر و خواناتر",
                    "kind": "text",
                    "minutes": 17,
                    "is_preview": False,
                    "body": (
                        "<h2>مشخص کردن نوع داده بدون از دست دادن انعطاف پایتون</h2>"
                        "<p>پایتون یک زبان با نوع‌بندی پویا است، اما از نسخه‌ی ۳.۵ به بعد امکان "
                        "افزودن <strong>type hints</strong> (راهنمای نوع) فراهم شده که به ابزارها و "
                        "ویرایشگرها کمک می‌کند خطاها را پیش از اجرا تشخیص دهند، بدون این‌که نوع‌بندی "
                        "پویای پایتون تغییر کند.</p>"
                        "<pre><code class=\"language-python\">def add(a: int, b: int) -&gt; int:\n"
                        "    return a + b\n\n"
                        "def greet(name: str, times: int = 1) -&gt; str:\n"
                        "    return (f\"سلام {name}! \" * times).strip()</code></pre>"
                        "<p>برای انواع پیچیده‌تر مانند لیست یا دیکشنری، از ماژول <code>typing</code> "
                        "یا (از پایتون ۳.۹ به بعد) مستقیماً از خود انواع داخلی استفاده می‌شود:</p>"
                        "<pre><code class=\"language-python\">from typing import Optional\n\n"
                        "def find_user(user_id: int, users: dict[int, str]) -&gt; Optional[str]:\n"
                        "    return users.get(user_id)\n\n"
                        "def total_price(items: list[float]) -&gt; float:\n"
                        "    return sum(items)</code></pre>"
                        "<p>نکته‌ی مهم این است که type hints فقط یک راهنما هستند و پایتون به‌طور "
                        "پیش‌فرض آن‌ها را در زمان اجرا بررسی نمی‌کند؛ برای بررسی واقعی باید از "
                        "ابزارهایی مانند <strong>mypy</strong> استفاده کرد. با این حال، حتی بدون "
                        "این ابزارها، type hints مستندسازی زنده‌ای برای کد شما فراهم می‌کنند و "
                        "پیشنهادهای هوشمند ویرایشگر را دقیق‌تر می‌کنند؛ به همین دلیل در پروژه‌های "
                        "تیمی حرفه‌ای تقریباً استاندارد شده‌اند.</p>"
                    ),
                },
                {
                    "title": "Dataclass برای ساخت کلاس‌های داده‌محور",
                    "kind": "text",
                    "minutes": 16,
                    "is_preview": False,
                    "body": (
                        "<h2>کاهش کدهای تکراری با dataclass</h2>"
                        "<p>بسیاری از کلاس‌ها فقط برای نگهداری چند مقدار ساخته می‌شوند و شامل "
                        "متدهایی مانند <code>__init__</code>، <code>__repr__</code> و "
                        "<code>__eq__</code> هستند که نوشتن دستی آن‌ها تکراری و خسته‌کننده است. "
                        "دکوراتور <code>@dataclass</code> از ماژول <code>dataclasses</code> این "
                        "متدها را به‌طور خودکار می‌سازد.</p>"
                        "<pre><code class=\"language-python\">from dataclasses import dataclass, field\n\n"
                        "@dataclass\n"
                        "class Product:\n"
                        "    name: str\n"
                        "    price: float\n"
                        "    tags: list[str] = field(default_factory=list)\n\n"
                        "p1 = Product(\"لپ‌تاپ\", 25000000)\n"
                        "p2 = Product(\"لپ‌تاپ\", 25000000)\n\n"
                        "print(p1)              # Product(name='لپ‌تاپ', price=25000000, tags=[])\n"
                        "print(p1 == p2)        # True — مقایسه بر اساس مقدار</code></pre>"
                        "<p>توجه کنید که برای مقادیر پیش‌فرض قابل‌تغییر مانند لیست، نباید مستقیماً "
                        "<code>tags: list = []</code> نوشت، چون این مقدار بین همه‌ی نمونه‌ها به "
                        "اشتراک گذاشته می‌شود. به همین دلیل از <code>field(default_factory=list)</code> "
                        "استفاده می‌شود تا برای هر شیء جدید یک لیست تازه ساخته شود.</p>"
                        "<p>می‌توانید با پارامتر <code>frozen=True</code> یک dataclass "
                        "غیرقابل‌تغییر (immutable) بسازید، مشابه رفتار تاپل، که برای مدل‌سازی "
                        "داده‌های ثابت مانند مختصات جغرافیایی بسیار مناسب است. ترکیب "
                        "<code>dataclass</code> با type hints، یکی از تمیزترین روش‌های مدل‌سازی "
                        "داده در پایتون مدرن است.</p>"
                    ),
                },
            ],
        },
        {
            "title": "فصل پنجم: برنامه‌نویسی ناهم‌گام با asyncio",
            "lessons": [
                {
                    "title": "چرا برنامه‌نویسی ناهم‌گام؟",
                    "kind": "text",
                    "minutes": 15,
                    "is_preview": False,
                    "body": (
                        "<h2>مشکل انتظار در برنامه‌های I/O-محور</h2>"
                        "<p>در بسیاری از برنامه‌ها، بخش زیادی از زمان اجرا صرف انتظار برای پاسخ "
                        "شبکه، خواندن فایل یا پاسخ پایگاه داده می‌شود، نه پردازش واقعی پردازنده. در "
                        "برنامه‌نویسی معمولی (synchronous)، در طول این انتظار کل برنامه متوقف "
                        "می‌ماند. برنامه‌نویسی <strong>ناهم‌گام</strong> (asynchronous) به برنامه "
                        "اجازه می‌دهد در زمان انتظار، به کارهای دیگر بپردازد.</p>"
                        "<p>پایتون این قابلیت را از طریق ماژول <code>asyncio</code> و کلیدواژه‌های "
                        "<code>async</code> و <code>await</code> فراهم می‌کند. یک تابع "
                        "<strong>coroutine</strong> با <code>async def</code> تعریف می‌شود و "
                        "می‌تواند در نقاطی با <code>await</code> اجرای خود را موقتاً به نفع "
                        "coroutine دیگر متوقف کند.</p>"
                        "<pre><code class=\"language-python\">import asyncio\n\n"
                        "async def say_hello():\n"
                        "    print(\"شروع\")\n"
                        "    await asyncio.sleep(1)\n"
                        "    print(\"پایان\")\n\n"
                        "asyncio.run(say_hello())</code></pre>"
                        "<p>نکته‌ی مهم این است که <code>asyncio</code> برای کارهای "
                        "<strong>I/O-محور</strong> مانند درخواست شبکه یا دسترسی به فایل مناسب "
                        "است، نه برای محاسبات سنگین پردازنده‌محور؛ برای آن نوع کارها باید به سراغ "
                        "<code>multiprocessing</code> رفت. تمایز درست بین این دو نوع مسئله، اولین "
                        "قدم برای استفاده‌ی درست از asyncio است.</p>"
                    ),
                },
                {
                    "title": "Event Loop و اجرای چند coroutine",
                    "kind": "text",
                    "minutes": 17,
                    "is_preview": False,
                    "body": (
                        "<h2>موتور اصلی asyncio: حلقه‌ی رویداد</h2>"
                        "<p><strong>حلقه‌ی رویداد</strong> (event loop) قلب اجرای برنامه‌های "
                        "asyncio است؛ وظیفه‌ی آن زمان‌بندی و اجرای coroutine‌هاست و تشخیص می‌دهد "
                        "کدام coroutine آماده‌ی ادامه‌ی اجراست. تابع <code>asyncio.run()</code> "
                        "یک event loop می‌سازد، coroutine اصلی را اجرا می‌کند و در پایان آن را "
                        "می‌بندد.</p>"
                        "<p>برای اجرای چند coroutine به‌طور همزمان (concurrent)، از "
                        "<code>asyncio.gather()</code> استفاده می‌شود:</p>"
                        "<pre><code class=\"language-python\">import asyncio\n\n"
                        "async def fetch_data(name, delay):\n"
                        "    print(f\"شروع دریافت {name}\")\n"
                        "    await asyncio.sleep(delay)\n"
                        "    print(f\"پایان دریافت {name}\")\n"
                        "    return f\"داده‌ی {name}\"\n\n"
                        "async def main():\n"
                        "    results = await asyncio.gather(\n"
                        "        fetch_data(\"کاربران\", 2),\n"
                        "        fetch_data(\"سفارش‌ها\", 1),\n"
                        "    )\n"
                        "    print(results)\n\n"
                        "asyncio.run(main())</code></pre>"
                        "<p>در این مثال، هر دو تابع تقریباً همزمان شروع می‌شوند و کل زمان اجرا "
                        "تقریباً برابر با طولانی‌ترین تأخیر (۲ ثانیه) خواهد بود، نه مجموع آن‌ها "
                        "(۳ ثانیه)، چون در زمان انتظار هر coroutine، حلقه‌ی رویداد به سراغ دیگری "
                        "می‌رود. این دقیقاً همان مزیت اصلی برنامه‌نویسی ناهم‌گام برای کارهای "
                        "شبکه‌ای است، مثل ارسال چند درخواست HTTP به‌صورت موازی.</p>"
                        "<p>نکته‌ی کلیدی این است که <code>await</code> فقط داخل توابع "
                        "<code>async def</code> قابل استفاده است و فراموش کردن آن یکی از "
                        "رایج‌ترین خطاهای تازه‌کاران در asyncio است.</p>"
                    ),
                },
                {
                    "title": "ایجاد Task و مدیریت خطا در asyncio",
                    "kind": "text",
                    "minutes": 16,
                    "is_preview": False,
                    "body": (
                        "<h2>اجرای پس‌زمینه با Task</h2>"
                        "<p>گاهی می‌خواهیم یک coroutine بلافاصله شروع به اجرا کند و منتظر پایان آن "
                        "نمانیم، بلکه بعداً نتیجه‌اش را بگیریم. برای این منظور از "
                        "<code>asyncio.create_task()</code> استفاده می‌شود که coroutine را به یک "
                        "<strong>Task</strong> در پس‌زمینه تبدیل می‌کند.</p>"
                        "<pre><code class=\"language-python\">import asyncio\n\n"
                        "async def background_job():\n"
                        "    await asyncio.sleep(2)\n"
                        "    print(\"کار پس‌زمینه تمام شد\")\n\n"
                        "async def main():\n"
                        "    task = asyncio.create_task(background_job())\n"
                        "    print(\"در حال انجام کارهای دیگر...\")\n"
                        "    await asyncio.sleep(1)\n"
                        "    print(\"هنوز منتظر task هستیم\")\n"
                        "    await task\n\n"
                        "asyncio.run(main())</code></pre>"
                        "<p>برای مدیریت خطا در coroutine‌ها، از همان بلوک آشنای <code>try/except</code> "
                        "استفاده می‌شود، اما باید دقت کنید که خطای یک <code>Task</code> تا زمانی "
                        "که آن را <code>await</code> نکنید ممکن است بی‌سروصدا نادیده گرفته شود:</p>"
                        "<pre><code class=\"language-python\">async def risky():\n"
                        "    raise ValueError(\"خطای عمدی\")\n\n"
                        "async def main():\n"
                        "    task = asyncio.create_task(risky())\n"
                        "    try:\n"
                        "        await task\n"
                        "    except ValueError as e:\n"
                        "        print(f\"خطا مدیریت شد: {e}\")</code></pre>"
                        "<p>در پروژه‌های واقعی، asyncio معمولاً همراه کتابخانه‌هایی مانند "
                        "<code>aiohttp</code> برای درخواست‌های شبکه یا فریمورک‌های ناهم‌گام مانند "
                        "FastAPI استفاده می‌شود، جایی که مدیریت درست خطا و timeout اهمیت زیادی در "
                        "پایداری سرویس دارد.</p>"
                    ),
                },
            ],
        },
        {
            "title": "فصل ششم: تست حرفه‌ای با pytest و بسته‌بندی پروژه",
            "lessons": [
                {
                    "title": "نوشتن اولین تست با pytest",
                    "kind": "text",
                    "minutes": 16,
                    "is_preview": False,
                    "body": (
                        "<h2>چرا تست خودکار می‌نویسیم؟</h2>"
                        "<p>تست خودکار به ما اطمینان می‌دهد که تغییرات جدید در کد، رفتار قبلی "
                        "برنامه را خراب نمی‌کند. <code>pytest</code> یکی از محبوب‌ترین ابزارهای "
                        "تست در پایتون است که با نحو ساده و پیام‌های خطای خوانا شناخته می‌شود.</p>"
                        "<p>ابتدا کتابخانه را نصب می‌کنیم:</p>"
                        "<pre><code class=\"language-bash\">pip install pytest</code></pre>"
                        "<p>فرض کنید تابعی به این شکل داریم:</p>"
                        "<pre><code class=\"language-python\"># calculator.py\n"
                        "def add(a, b):\n"
                        "    return a + b\n\n"
                        "def divide(a, b):\n"
                        "    if b == 0:\n"
                        "        raise ValueError(\"تقسیم بر صفر مجاز نیست\")\n"
                        "    return a / b</code></pre>"
                        "<p>فایل تست معمولاً با پیشوند <code>test_</code> نام‌گذاری می‌شود و هر "
                        "تابع تست نیز باید با <code>test_</code> شروع شود تا pytest آن را شناسایی "
                        "کند:</p>"
                        "<pre><code class=\"language-python\"># test_calculator.py\n"
                        "import pytest\n"
                        "from calculator import add, divide\n\n"
                        "def test_add():\n"
                        "    assert add(2, 3) == 5\n\n"
                        "def test_divide_by_zero():\n"
                        "    with pytest.raises(ValueError):\n"
                        "        divide(10, 0)</code></pre>"
                        "<p>برای اجرای تست‌ها کافی است دستور <code>pytest</code> را در ریشه‌ی "
                        "پروژه اجرا کنید. برخلاف <code>unittest</code> که نیاز به کلاس و متدهای "
                        "خاص دارد، در pytest کافی است از دستور ساده‌ی <code>assert</code> استفاده "
                        "کنید و کتابخانه به‌طور خودکار پیام خطای دقیقی در صورت شکست تست تولید "
                        "می‌کند.</p>"
                    ),
                },
                {
                    "title": "Fixture و پارامتری‌سازی تست‌ها",
                    "kind": "text",
                    "minutes": 18,
                    "is_preview": False,
                    "body": (
                        "<h2>آماده‌سازی داده‌ی مشترک با fixture</h2>"
                        "<p>در بسیاری از تست‌ها به داده یا شیء مشترکی نیاز داریم که باید پیش از هر "
                        "تست آماده شود. <strong>fixture</strong> در pytest دقیقاً همین کار را "
                        "انجام می‌دهد و از تکرار کد جلوگیری می‌کند.</p>"
                        "<pre><code class=\"language-python\">import pytest\n\n"
                        "@pytest.fixture\n"
                        "def sample_cart():\n"
                        "    return {\"apple\": 3, \"banana\": 2}\n\n"
                        "def test_cart_has_apple(sample_cart):\n"
                        "    assert \"apple\" in sample_cart\n\n"
                        "def test_cart_total_items(sample_cart):\n"
                        "    assert sum(sample_cart.values()) == 5</code></pre>"
                        "<p>هر تابع تست که نام fixture را به‌عنوان پارامتر بگیرد، به‌طور خودکار "
                        "مقدار بازگشتی آن را دریافت می‌کند. pytest همچنین با "
                        "<code>@pytest.mark.parametrize</code> امکان اجرای یک تست با چند مجموعه "
                        "ورودی مختلف را فراهم می‌کند، بدون این‌که نیاز به نوشتن چند تابع تست جداگانه "
                        "باشد:</p>"
                        "<pre><code class=\"language-python\">@pytest.mark.parametrize(\"a, b, expected\", [\n"
                        "    (2, 3, 5),\n"
                        "    (0, 0, 0),\n"
                        "    (-1, 1, 0),\n"
                        "])\n"
                        "def test_add_multiple_cases(a, b, expected):\n"
                        "    assert add(a, b) == expected</code></pre>"
                        "<p>این روش باعث می‌شود پوشش تست بیشتری با کد کمتر داشته باشید و اگر یکی "
                        "از حالت‌ها شکست بخورد، pytest دقیقاً مشخص می‌کند کدام مجموعه ورودی مشکل "
                        "داشته است. استفاده‌ی ترکیبی از fixture و parametrize، یکی از نشانه‌های "
                        "تست‌نویسی حرفه‌ای در پروژه‌های پایتون است.</p>"
                    ),
                },
                {
                    "title": "ساختار بسته و pyproject.toml",
                    "kind": "text",
                    "minutes": 17,
                    "is_preview": False,
                    "body": (
                        "<h2>سازمان‌دهی پروژه برای تبدیل شدن به یک بسته</h2>"
                        "<p>وقتی می‌خواهید کد خود را به‌صورت یک کتابخانه‌ی قابل‌نصب منتشر کنید، "
                        "باید ساختار پروژه را استاندارد کنید. ساختار رایج امروزی به این شکل است:</p>"
                        "<pre><code class=\"language-text\">my_package/\n"
                        "├── pyproject.toml\n"
                        "├── README.md\n"
                        "├── src/\n"
                        "│   └── my_package/\n"
                        "│       ├── __init__.py\n"
                        "│       └── core.py\n"
                        "└── tests/\n"
                        "    └── test_core.py</code></pre>"
                        "<p>فایل <code>pyproject.toml</code> جایگزین مدرن فایل قدیمی "
                        "<code>setup.py</code> شده و متادیتای بسته، وابستگی‌ها و تنظیمات ابزار "
                        "ساخت را در یک فایل استاندارد نگه می‌دارد:</p>"
                        "<pre><code class=\"language-toml\">[build-system]\n"
                        "requires = [\"setuptools&gt;=68\"]\n"
                        "build-backend = \"setuptools.build_meta\"\n\n"
                        "[project]\n"
                        "name = \"my-package\"\n"
                        "version = \"0.1.0\"\n"
                        "description = \"یک بسته‌ی نمونه\"\n"
                        "requires-python = \"&gt;=3.10\"\n"
                        "dependencies = [\n"
                        "    \"requests&gt;=2.31\",\n"
                        "]</code></pre>"
                        "<p>استفاده از پوشه‌ی <code>src</code> (به‌جای قرار دادن کد در ریشه‌ی "
                        "پروژه) یک قرارداد رایج است که از وارد کردن اشتباهیِ نسخه‌ی نصب‌نشده‌ی "
                        "بسته در زمان تست جلوگیری می‌کند. نگه‌داشتن تست‌ها در پوشه‌ای جدا نیز باعث "
                        "می‌شود بسته‌ی نهایی حجم کمتری داشته باشد و ساختار پروژه برای دیگر توسعه‌دهندگان "
                        "قابل‌پیش‌بینی‌تر باشد.</p>"
                    ),
                },
                {
                    "title": "ساخت و انتشار بسته در PyPI",
                    "kind": "text",
                    "minutes": 18,
                    "is_preview": False,
                    "body": (
                        "<h2>از کد محلی تا نصب با pip</h2>"
                        "<p>پس از آماده‌سازی ساختار پروژه، مرحله‌ی بعدی ساخت (build) و انتشار "
                        "(publish) بسته است. ابزار استاندارد برای ساخت بسته، پکیج <code>build</code> "
                        "است:</p>"
                        "<pre><code class=\"language-bash\">pip install build twine\n"
                        "python3 -m build</code></pre>"
                        "<p>این دستور دو فایل در پوشه‌ی <code>dist/</code> می‌سازد: یک فایل "
                        "<code>.tar.gz</code> (توزیع منبع) و یک فایل <code>.whl</code> (توزیع "
                        "wheel که برای نصب سریع‌تر بهینه شده است). پیش از انتشار عمومی، توصیه "
                        "می‌شود ابتدا بسته را روی <strong>TestPyPI</strong> (نسخه‌ی آزمایشی مخزن "
                        "PyPI) منتشر کنید تا از صحت آن مطمئن شوید:</p>"
                        "<pre><code class=\"language-bash\">twine upload --repository testpypi dist/*\n"
                        "pip install --index-url https://test.pypi.org/simple/ my-package</code></pre>"
                        "<p>پس از اطمینان از درستی بسته، انتشار نهایی روی مخزن اصلی PyPI با دستور "
                        "زیر انجام می‌شود:</p>"
                        "<pre><code class=\"language-bash\">twine upload dist/*</code></pre>"
                        "<p>برای این کار نیاز به ثبت‌نام در سایت PyPI و ساخت یک توکن API دارید که "
                        "به‌جای رمز عبور در فرایند آپلود استفاده می‌شود. پس از انتشار، هر کاربری در "
                        "دنیا می‌تواند با دستور <code>pip install my-package</code> بسته‌ی شما را "
                        "نصب کند. رعایت نسخه‌بندی معنایی (Semantic Versioning) در فیلد "
                        "<code>version</code> نیز به کاربران کمک می‌کند بفهمند هر بروزرسانی چه نوع "
                        "تغییری (اصلاح جزئی، قابلیت جدید یا تغییر شکننده) به همراه دارد.</p>"
                    ),
                },
            ],
        },
    ],
}

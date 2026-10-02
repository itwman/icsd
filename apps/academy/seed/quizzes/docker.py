# -*- coding: utf-8 -*-

QUIZ = {
    "course_slug": "docker",
    "title": "آزمون پایانی داکر",
    "pass_percent": 70,
    "time_limit_minutes": 20,
    "questions": [
        {
            "text": "تفاوت اصلی کانتینر با ماشین مجازی چیست؟",
            "explanation": "کانتینرها از kernel سیستم‌عامل میزبان استفاده می‌کنند و فقط user space خودشان را ایزوله می‌کنند؛ به همین دلیل سبک‌تر و سریع‌ترند.",
            "choices": [
                {"text": "کانتینرها یک سیستم‌عامل کامل و مستقل شبیه‌سازی می‌کنند", "correct": False},
                {"text": "کانتینرها از kernel سیستم‌عامل میزبان استفاده می‌کنند و فقط فضای کاربری را ایزوله می‌کنند", "correct": True},
                {"text": "کانتینرها همیشه کندتر از ماشین مجازی راه‌اندازی می‌شوند", "correct": False},
                {"text": "کانتینرها به یک هایپروایزر سخت‌افزاری نیاز دارند", "correct": False},
            ],
        },
        {
            "text": "برای نصب داکر روی اوبونتو با اسکریپت رسمی، از کدام دستور استفاده می‌شود؟",
            "explanation": "`curl -fsSL https://get.docker.com | sh` ساده‌ترین راه نصب داکر روی توزیع‌های مبتنی بر دبیان است.",
            "choices": [
                {"text": "docker install ubuntu", "correct": False},
                {"text": "apt install docker-official", "correct": False},
                {"text": "curl -fsSL https://get.docker.com | sh", "correct": True},
                {"text": "docker init --system", "correct": False},
            ],
        },
        {
            "text": "تفاوت image و container در داکر چیست؟",
            "explanation": "image یک بسته‌ی فقط-خواندنی (قالب) است و container نمونه‌ی در حال اجرای آن image است، شبیه کلاس و instance.",
            "choices": [
                {"text": "image نمونه‌ی در حال اجراست و container قالب فقط-خواندنی است", "correct": False},
                {"text": "image و container دقیقاً یک مفهوم هستند و تفاوتی ندارند", "correct": False},
                {"text": "container فقط برای دیتابیس‌ها استفاده می‌شود و image برای وب‌سرورها", "correct": False},
                {"text": "image قالب فقط-خواندنی است و container نمونه‌ی در حال اجرای آن است", "correct": True},
            ],
        },
        {
            "text": "در Dockerfile، کدام دستور یک فرمان را در زمان build اجرا می‌کند؟",
            "explanation": "RUN دستوری است که هنگام ساخت image اجرا می‌شود (مثل نصب پکیج)، برخلاف CMD که هنگام اجرای container اجرا می‌شود.",
            "choices": [
                {"text": "CMD", "correct": False},
                {"text": "RUN", "correct": True},
                {"text": "COPY", "correct": False},
                {"text": "WORKDIR", "correct": False},
            ],
        },
        {
            "text": "چرا در Dockerfile باید `COPY requirements.txt .` را پیش از `COPY . .` قرار داد؟",
            "explanation": "این ترتیب باعث می‌شود لایه‌ی نصب وابستگی‌ها کش شود و با تغییر کد برنامه، مجبور به نصب مجدد وابستگی‌ها نشویم.",
            "choices": [
                {"text": "چون داکر بدون این ترتیب اصلاً image را build نمی‌کند", "correct": False},
                {"text": "برای استفاده‌ی بهتر از کش لایه‌ها و جلوگیری از نصب مجدد غیرضروری وابستگی‌ها", "correct": True},
                {"text": "چون requirements.txt باید همیشه آخرین فایل کپی‌شده باشد", "correct": False},
                {"text": "این ترتیب فقط روی حجم نهایی image تأثیر دارد، نه سرعت build", "correct": False},
            ],
        },
        {
            "text": "مزیت اصلی ساخت چندمرحله‌ای (multi-stage build) چیست؟",
            "explanation": "با multi-stage build فقط نتیجه‌ی نهایی build وارد image آخر می‌شود و ابزارهای توسعه در image نهایی باقی نمی‌مانند، در نتیجه image کوچک‌تر و امن‌تر است.",
            "choices": [
                {"text": "امکان اجرای همزمان چند کانتینر از یک image", "correct": False},
                {"text": "حذف نیاز به فایل Dockerfile", "correct": False},
                {"text": "image نهایی کوچک‌تر و امن‌تر می‌شود چون ابزارهای ساخت در آن باقی نمی‌مانند", "correct": True},
                {"text": "افزایش سرعت اجرای کانتینر در محیط توسعه", "correct": False},
            ],
        },
        {
            "text": "برای ماندگاری داده‌ی یک کانتینر پایگاه‌داده، حتی بعد از حذف کانتینر، از چه چیزی استفاده می‌شود؟",
            "explanation": "Volume فضای ذخیره‌سازی‌ای است که مستقل از چرخه‌ی حیات کانتینر توسط داکر مدیریت می‌شود.",
            "choices": [
                {"text": "docker network", "correct": False},
                {"text": "Volume", "correct": True},
                {"text": "docker cache", "correct": False},
                {"text": "فایل .dockerignore", "correct": False},
            ],
        },
        {
            "text": "در یک network سفارشی داکر، کانتینرها چگونه می‌توانند با استفاده از نام یکدیگر را پیدا کنند؟",
            "explanation": "داکر یک DNS داخلی دارد که نام کانتینرهای متصل به یک network سفارشی را به‌طور خودکار به آدرس داخلی درست ترجمه می‌کند.",
            "choices": [
                {"text": "با نوشتن دستی IP هر کانتینر در فایل hosts", "correct": False},
                {"text": "با استفاده از نام کانتینر که به‌کمک DNS داخلی داکر ترجمه می‌شود", "correct": True},
                {"text": "کانتینرها هرگز نمی‌توانند از طریق نام به هم متصل شوند", "correct": False},
                {"text": "فقط با تعریف دستی route در سیستم‌عامل میزبان", "correct": False},
            ],
        },
        {
            "text": "چرا اطلاعات حساس مثل رمز پایگاه‌داده نباید مستقیماً داخل Dockerfile نوشته شوند؟",
            "explanation": "بهتر است این مقادیر از طریق متغیرهای محیطی یا فایل .env ست شوند تا هرگز وارد کد یا تاریخچه‌ی گیت نشوند.",
            "choices": [
                {"text": "چون Dockerfile فقط از متغیرهای عددی پشتیبانی می‌کند", "correct": False},
                {"text": "چون این کار سرعت build را کاهش می‌دهد", "correct": False},
                {"text": "برای جدا نگه‌داشتن پیکربندی حساس از کد و جلوگیری از افشای آن‌ها، باید از متغیرهای محیطی استفاده کرد", "correct": True},
                {"text": "چون Docker Hub اجازه‌ی این کار را نمی‌دهد", "correct": False},
            ],
        },
        {
            "text": "دستور `docker compose up -d` چه کاری انجام می‌دهد؟",
            "explanation": "این دستور همه‌ی سرویس‌های تعریف‌شده در docker-compose.yml را در پس‌زمینه اجرا می‌کند و به‌طور خودکار یک network مشترک می‌سازد.",
            "choices": [
                {"text": "فقط یک سرویس خاص را می‌سازد، بدون اجرا کردن آن", "correct": False},
                {"text": "همه‌ی سرویس‌های تعریف‌شده را در پس‌زمینه اجرا می‌کند", "correct": True},
                {"text": "تمام کانتینرها و volumeها را حذف می‌کند", "correct": False},
                {"text": "فقط لاگ سرویس‌ها را نمایش می‌دهد", "correct": False},
            ],
        },
        {
            "text": "در docker-compose.yml، کلید `depends_on` دقیقاً چه تضمینی می‌دهد؟",
            "explanation": "depends_on فقط ترتیب راه‌اندازی کانتینرها را کنترل می‌کند، نه اینکه سرویس وابسته کاملاً آماده‌ی پذیرش درخواست باشد.",
            "choices": [
                {"text": "تضمین می‌کند سرویس وابسته کاملاً برای پذیرش اتصال آماده است", "correct": False},
                {"text": "فقط ترتیب راه‌اندازی کانتینرها را کنترل می‌کند، نه آماده بودن کامل سرویس", "correct": True},
                {"text": "باعث می‌شود دو سرویس در یک کانتینر واحد اجرا شوند", "correct": False},
                {"text": "حجم volume سرویس وابسته را افزایش می‌دهد", "correct": False},
            ],
        },
        {
            "text": "چرا در محیط production باید سرور توسعه‌ی جنگو (`runserver`) با gunicorn جایگزین شود؟",
            "explanation": "سرور داخلی جنگو فقط برای توسعه طراحی شده و برای بار ترافیک واقعی مناسب نیست؛ gunicorn یک WSGI Server مناسب production است.",
            "choices": [
                {"text": "چون runserver فقط روی ویندوز کار می‌کند", "correct": False},
                {"text": "چون runserver فقط برای توسعه طراحی شده و برای بار ترافیک واقعی مناسب نیست", "correct": True},
                {"text": "چون runserver نیاز به پایگاه‌داده‌ی پستگرس ندارد", "correct": False},
                {"text": "چون gunicorn سرعت build را افزایش می‌دهد", "correct": False},
            ],
        },
        {
            "text": "دستور `python manage.py collectstatic` چه کاری انجام می‌دهد؟",
            "explanation": "این دستور تمام فایل‌های استاتیک (CSS، JS، تصاویر) پروژه را در یک پوشه‌ی واحد جمع می‌کند تا توسط nginx یا سرویس مشابه سرو شوند.",
            "choices": [
                {"text": "مایگریشن‌های پایگاه‌داده را اجرا می‌کند", "correct": False},
                {"text": "تمام فایل‌های استاتیک پروژه را در یک پوشه‌ی واحد جمع می‌کند", "correct": True},
                {"text": "یک superuser جدید برای جنگو می‌سازد", "correct": False},
                {"text": "کانتینر nginx را ری‌استارت می‌کند", "correct": False},
            ],
        },
        {
            "text": "چرا اتکای همیشگی به تگ `latest` هنگام push کردن image توصیه نمی‌شود؟",
            "explanation": "اگر image همیشه با تگ latest منتشر شود، سرور تولید ممکن است بدون اطلاع نسخه‌ی جدید و تست‌نشده‌ای را pull کند.",
            "choices": [
                {"text": "چون تگ latest فقط روی Docker Hub قابل استفاده است", "correct": False},
                {"text": "چون حجم image با تگ latest همیشه بیشتر است", "correct": False},
                {"text": "چون latest اصلاً قابل push کردن نیست", "correct": False},
                {"text": "چون سرور تولید ممکن است بدون اطلاع، نسخه‌ی جدید و تست‌نشده‌ای را pull کند", "correct": True},
            ],
        },
        {
            "text": "برای انتشار یک image روی یک رجیستری خصوصی (مثل registry.mycompany.com)، چه کاری باید انجام شود؟",
            "explanation": "باید ابتدا image را با فرمت `<آدرس رجیستری>/<نام ایمیج>:<نسخه>` تگ زد و سپس با docker push آن را ارسال کرد.",
            "choices": [
                {"text": "فقط با docker run آن را روی سرور اجرا کرد", "correct": False},
                {"text": "image را با آدرس رجیستری تگ زد و سپس با docker push ارسال کرد", "correct": True},
                {"text": "فایل Dockerfile را مستقیماً به سرور کپی کرد", "correct": False},
                {"text": "از docker compose down برای انتشار استفاده کرد", "correct": False},
            ],
        },
    ],
}

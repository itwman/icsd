# -*- coding: utf-8 -*-
# بانک ۳۶ سؤالی آزمون دوره‌ی جامع جنگو (Django 5.x) — هر نوبت ۲۰ سؤال تصادفی

QUIZ = {
    "course_slug": "django",
    "title": "آزمون پایانی آموزش جامع جنگو (Django)",
    "pass_percent": 70,
    "time_limit_minutes": 30,
    "questions_per_attempt": 20,
    "questions": [
        # ── فصل ۱: معماری، ساختار پروژه و Custom User
        {
            "text": "در چرخه‌ی درخواست/پاسخ جنگو، پاسخ (HttpResponse) به چه ترتیبی از Middlewareها عبور می‌کند؟",
            "explanation": "درخواست به ترتیب تعریف‌شده در MIDDLEWARE از لایه‌ها می‌گذرد و پاسخ به ترتیب برعکس برمی‌گردد؛ مثل لایه‌های پیاز.",
            "choices": [
                {"text": "به همان ترتیب تعریف‌شده در MIDDLEWARE", "correct": False},
                {"text": "به ترتیب برعکس فهرست MIDDLEWARE", "correct": True},
                {"text": "پاسخ اصلاً از Middlewareها عبور نمی‌کند", "correct": False},
                {"text": "به ترتیب تصادفی، بسته به سرور WSGI", "correct": False},
            ],
        },
        {
            "text": "چرا `AuthenticationMiddleware` باید بعد از `SessionMiddleware` در فهرست MIDDLEWARE بیاید؟",
            "explanation": "AuthenticationMiddleware کاربر را از Session می‌خواند و request.user را می‌سازد؛ پس Session باید قبل از آن آماده شده باشد.",
            "choices": [
                {"text": "چون ترتیب Middlewareها فقط روی سرعت اثر دارد", "correct": False},
                {"text": "چون SessionMiddleware توکن CSRF را می‌سازد", "correct": False},
                {"text": "چون شناسه‌ی کاربر را از Session می‌خواند و request.user را از روی آن می‌سازد", "correct": True},
                {"text": "چون جنگو در غیر این صورت migrationها را اجرا نمی‌کند", "correct": False},
            ],
        },
        {
            "text": "در settings کد `DEBUG = bool(os.getenv(\"DJANGO_DEBUG\"))` نوشته شده و روی سرور `DJANGO_DEBUG=False` است. نتیجه چیست؟",
            "explanation": "هر رشته‌ی غیرخالی، از جمله \"False\"، در پایتون True است؛ پس DEBUG روشن می‌ماند. باید مقدار رشته را صریح مقایسه کرد.",
            "choices": [
                {"text": "DEBUG برابر True می‌شود، چون رشته‌ی \"False\" غیرخالی است", "correct": True},
                {"text": "DEBUG برابر False می‌شود", "correct": False},
                {"text": "جنگو خطای ImproperlyConfigured می‌دهد", "correct": False},
                {"text": "DEBUG برابر None می‌شود و جنگو پیش‌فرض را برمی‌دارد", "correct": False},
            ],
        },
        {
            "text": "در یک مدل که به کاربر اشاره می‌کند، روش درست تعریف ForeignKey در پروژه‌ای با Custom User کدام است؟",
            "explanation": "در models.py همیشه settings.AUTH_USER_MODEL به کار می‌رود؛ صدا زدن get_user_model() در سطح ماژول ممکن است پیش از بارگذاری اپ‌ها اجرا شود.",
            "choices": [
                {"text": "`models.ForeignKey(User, ...)` با import از django.contrib.auth.models", "correct": False},
                {"text": "`models.ForeignKey(get_user_model(), ...)` در سطح ماژول", "correct": False},
                {"text": "`models.ForeignKey(\"auth.User\", ...)`", "correct": False},
                {"text": "`models.ForeignKey(settings.AUTH_USER_MODEL, ...)`", "correct": True},
            ],
        },
        # ── فصل ۲: مدل‌ها و ORM
        {
            "text": "برای یک CharField اختیاری مثل «توضیحات سفارش»، کدام تنظیم توصیه‌شده است؟",
            "explanation": "CharField با null=True دو نوع «خالی» (NULL و رشته‌ی خالی) می‌سازد؛ blank=True برای اختیاری بودن در فرم کافی است و مقدار خالی رشته‌ی \"\" ذخیره می‌شود.",
            "choices": [
                {"text": "`null=True, blank=True`", "correct": False},
                {"text": "فقط `null=True`", "correct": False},
                {"text": "فقط `blank=True`", "correct": True},
                {"text": "`default=None`", "correct": False},
            ],
        },
        {
            "text": "فیلد `customer` در مدل Order به Customer اشاره می‌کند. اگر نخواهید با حذف مشتری سوابق سفارش‌ها از بین برود، کدام on_delete مناسب است؟",
            "explanation": "PROTECT حذف والدی را که فرزند دارد با ProtectedError متوقف می‌کند؛ CASCADE سفارش‌ها را هم پاک می‌کند که برای سوابق مالی فاجعه است.",
            "choices": [
                {"text": "`models.PROTECT`", "correct": True},
                {"text": "`models.CASCADE`", "correct": False},
                {"text": "`models.DO_NOTHING` بدون قید پایگاه داده", "correct": False},
                {"text": "on_delete در Django 5 اختیاری است و نیازی نیست", "correct": False},
            ],
        },
        {
            "text": "چرا داخل تابع `RunPython` در یک data migration باید از `apps.get_model(\"orders\", \"Order\")` استفاده کرد نه import مستقیم مدل؟",
            "explanation": "apps.get_model مدل «تاریخی» را در همان نقطه از تاریخچه‌ی migrationها می‌دهد؛ مدل امروز ممکن است فیلدهایی داشته باشد که آن زمان هنوز در جدول نبوده‌اند.",
            "choices": [
                {"text": "چون import مستقیم در migrationها از نظر نحوی ممنوع است", "correct": False},
                {"text": "چون apps.get_model سریع‌تر است", "correct": False},
                {"text": "چون get_model متدهای سفارشی و save بازنویسی‌شده را هم می‌آورد", "correct": False},
                {"text": "چون مدل تاریخی ساختار جدول را در همان مرحله از migrationها منعکس می‌کند", "correct": True},
            ],
        },
        {
            "text": "در مدل Order متد `clean()` نوشته‌اید. یک اسکریپت در shell با `order.save()` سفارش می‌سازد. آیا `clean()` اجرا می‌شود؟",
            "explanation": "save() خودکار full_clean() را صدا نمی‌زند؛ clean فقط در ModelForm، ادمین یا وقتی خودتان full_clean را صدا بزنید اجرا می‌شود. برای ضمانت در پایگاه داده از constraint استفاده کنید.",
            "choices": [
                {"text": "بله، save همیشه full_clean را صدا می‌زند", "correct": False},
                {"text": "خیر؛ save خودکار full_clean را صدا نمی‌زند", "correct": True},
                {"text": "فقط وقتی DEBUG=True باشد", "correct": False},
                {"text": "فقط اگر مدل Meta.constraints داشته باشد", "correct": False},
            ],
        },
        {
            "text": "در سیگنال post_save سفارش، پیامک «سفارش شما ثبت شد» ارسال می‌شود. چرا بهتر است ارسال داخل `transaction.on_commit` باشد؟",
            "explanation": "اگر تراکنش بعد از ذخیره rollback شود، سفارشی وجود ندارد اما پیامک رفته است. on_commit کار خارجی را فقط پس از commit موفق اجرا می‌کند.",
            "choices": [
                {"text": "تا پیامک برای سفارشی که تراکنشش rollback شده ارسال نشود", "correct": True},
                {"text": "چون سیگنال‌ها بیرون از on_commit اجرا نمی‌شوند", "correct": False},
                {"text": "تا پیامک سریع‌تر ارسال شود", "correct": False},
                {"text": "چون on_commit جلوی ثبت دوباره‌ی گیرنده‌ی سیگنال را می‌گیرد", "correct": False},
            ],
        },
        # ── فصل ۳: QuerySet حرفه‌ای
        {
            "text": "کد `qs = Order.objects.filter(status=\"paid\")` چند کوئری به پایگاه داده می‌فرستد، اگر هنوز از qs استفاده نشده باشد؟",
            "explanation": "QuerySet تنبل است؛ ساختن و زنجیر کردن filter هیچ کوئری‌ای نمی‌زند. کوئری فقط هنگام ارزیابی (پیمایش، list، len، bool، ایندکس) اجرا می‌شود.",
            "choices": [
                {"text": "یک کوئری", "correct": False},
                {"text": "دو کوئری: یکی برای شمارش و یکی برای داده", "correct": False},
                {"text": "به تعداد ردیف‌های paid", "correct": False},
                {"text": "هیچ کوئری‌ای؛ QuerySet تا زمان ارزیابی اجرا نمی‌شود", "correct": True},
            ],
        },
        {
            "text": "کدام روش کم کردن موجودی انبار در شرایط هم‌زمانی (دو خرید هم‌زمان) امن‌تر است؟",
            "explanation": "F عملیات را در خود SQL انجام می‌دهد (UPDATE ... SET stock = stock - 1)؛ خواندن مقدار در پایتون و نوشتن دوباره، دچار race condition می‌شود.",
            "choices": [
                {"text": "`carpet.stock = carpet.stock - 1; carpet.save()`", "correct": False},
                {"text": "`Carpet.objects.filter(pk=pk).update(stock=F(\"stock\") - 1)`", "correct": True},
                {"text": "خواندن موجودی با `values_list` و سپس `update` با عدد محاسبه‌شده", "correct": False},
                {"text": "`carpet.refresh_from_db()` و سپس `save()`", "correct": False},
            ],
        },
        {
            "text": "در فهرست سفارش‌ها، برای هر سفارش نام مشتری (ForeignKey) و همه‌ی اقلام آن (رابطه‌ی معکوس چندتایی) نمایش داده می‌شود. ترکیب درست برای جلوگیری از N+1 کدام است؟",
            "explanation": "select_related برای ForeignKey/OneToOne با JOIN کار می‌کند؛ prefetch_related برای روابط چندتایی یک کوئری جدا می‌زند و در پایتون وصل می‌کند.",
            "choices": [
                {"text": "`prefetch_related(\"customer\")` و `select_related(\"items\")`", "correct": False},
                {"text": "فقط `select_related(\"customer\", \"items\")`", "correct": False},
                {"text": "`select_related(\"customer\")` و `prefetch_related(\"items\")`", "correct": True},
                {"text": "`only(\"customer\", \"items\")`", "correct": False},
            ],
        },
        {
            "text": "سفارش‌ها با `prefetch_related(\"items\")` خوانده شده‌اند، اما در قالب برای هر سفارش `order.items.filter(is_active=True)` صدا زده می‌شود. چه اتفاقی می‌افتد؟",
            "explanation": "filter یا order_by روی رابطه‌ی prefetch‌شده کش را دور می‌ریزد و برای هر سفارش کوئری تازه می‌زند؛ راه‌حل Prefetch با queryset فیلترشده و to_attr است.",
            "choices": [
                {"text": "کش prefetch استفاده می‌شود و کوئری اضافه‌ای نمی‌رود", "correct": False},
                {"text": "خطای FieldError می‌گیرید", "correct": False},
                {"text": "جنگو فیلتر را خودکار به کوئری prefetch اضافه می‌کند", "correct": False},
                {"text": "کش prefetch نادیده گرفته می‌شود و برای هر سفارش کوئری جدید می‌رود (N+1 برمی‌گردد)", "correct": True},
            ],
        },
        {
            "text": "حاصل `Order.objects.filter(status=\"canceled\").aggregate(total=Sum(\"total\"))` وقتی هیچ سفارش لغوشده‌ای نیست چیست و چطور آن را صفر کنیم؟",
            "explanation": "Sum روی مجموعه‌ی خالی None برمی‌گرداند؛ با پارامتر default=0 (از Django 4.0) یا Coalesce مقدار صفر می‌گیرید.",
            "choices": [
                {"text": "`{\"total\": None}`؛ با `Sum(\"total\", default=0)` صفر می‌شود", "correct": True},
                {"text": "`{\"total\": 0}` به‌طور پیش‌فرض", "correct": False},
                {"text": "خطای DoesNotExist", "correct": False},
                {"text": "یک دیکشنری خالی `{}`", "correct": False},
            ],
        },
        {
            "text": "برای جلوگیری از فروش بیش از موجودی در پرداخت هم‌زمان، از `select_for_update()` استفاده می‌کنید. کدام جمله درست است؟",
            "explanation": "select_for_update فقط داخل transaction.atomic معنا دارد (بیرون از آن TransactionManagementError می‌دهد) و SQLite قفل ردیفی ندارد؛ رفتار واقعی را روی PostgreSQL بسنجید.",
            "choices": [
                {"text": "بیرون از atomic هم کار می‌کند و قفل تا پایان درخواست می‌ماند", "correct": False},
                {"text": "باید داخل `transaction.atomic` باشد و روی SQLite عملاً قفلی نمی‌گذارد", "correct": True},
                {"text": "روی همه‌ی پایگاه‌داده‌ها از جمله SQLite قفل ردیفی می‌گذارد", "correct": False},
                {"text": "جایگزین F است و دیگر به تراکنش نیازی نیست", "correct": False},
            ],
        },
        # ── فصل ۴: View، URL و Template
        {
            "text": "در یک CreateView ویژگی `success_url` را در سطح کلاس تعریف می‌کنید. چرا باید `reverse_lazy` به کار برود نه `reverse`؟",
            "explanation": "ویژگی کلاس هنگام import ماژول ارزیابی می‌شود، پیش از آن‌که URLconf بارگذاری شده باشد؛ reverse_lazy محاسبه را تا زمان استفاده عقب می‌اندازد.",
            "choices": [
                {"text": "چون reverse در کلاس‌ها کار نمی‌کند", "correct": False},
                {"text": "چون reverse_lazy آدرس را کش می‌کند و سریع‌تر است", "correct": False},
                {"text": "چون reverse در زمان import و پیش از بارگذاری URLconf اجرا می‌شود و خطا می‌دهد", "correct": True},
                {"text": "چون reverse برای namespaceها پشتیبانی ندارد", "correct": False},
            ],
        },
        {
            "text": "View جزئیات سفارش با `get_object_or_404(Order, pk=pk, customer__user=request.user)` نوشته شده. شرط دوم از چه آسیب‌پذیری جلوگیری می‌کند؟",
            "explanation": "بدون این شرط کاربر با تغییر عدد در آدرس سفارش دیگران را می‌بیند (IDOR). با شرط مالکیت، سفارش دیگران برای او 404 است.",
            "choices": [
                {"text": "IDOR: دیدن سفارش دیگران با عوض کردن عدد آدرس", "correct": True},
                {"text": "CSRF", "correct": False},
                {"text": "SQL Injection", "correct": False},
                {"text": "Open Redirect", "correct": False},
            ],
        },
        {
            "text": "کدام تعریف کلاس برای یک UpdateView که فقط کاربر لاگین‌شده باید ببیند درست است؟",
            "explanation": "به‌خاطر MRO پایتون، mixinهای دسترسی باید سمت چپ کلاس پایه باشند تا dispatch آن‌ها پیش از منطق View اجرا شود.",
            "choices": [
                {"text": "`class OrderUpdate(UpdateView, LoginRequiredMixin)`", "correct": False},
                {"text": "`class OrderUpdate(LoginRequiredMixin, UpdateView)`", "correct": True},
                {"text": "ترتیب اهمیتی ندارد", "correct": False},
                {"text": "باید فقط دکوراتور `@login_required` را روی کلاس گذاشت", "correct": False},
            ],
        },
        {
            "text": "فیلتر قالب برای نمایش تاریخ شمسی سفارش‌ها نوشته‌اید، اما سفارشی که ساعت ۲ بامداد تهران ثبت شده، با تاریخ روز قبل نمایش داده می‌شود. علت محتمل چیست؟",
            "explanation": "با USE_TZ=True تاریخ‌ها aware و در UTC ذخیره می‌شوند؛ پیش از تبدیل به شمسی باید با timezone.localtime به وقت تهران برده شوند.",
            "choices": [
                {"text": "USE_TZ باید False باشد", "correct": False},
                {"text": "کتابخانه‌ی jdatetime سال کبیسه را اشتباه حساب می‌کند", "correct": False},
                {"text": "LANGUAGE_CODE روی fa-ir تنظیم نشده", "correct": False},
                {"text": "تاریخ aware پیش از تبدیل با `timezone.localtime` به وقت محلی برده نشده و UTC نمایش داده می‌شود", "correct": True},
            ],
        },
        # ── فصل ۵: فرم‌ها و اعتبارسنجی
        {
            "text": "چرا `fields = \"__all__\"` در ModelForm سفارش، خطر امنیتی دارد؟",
            "explanation": "اگر بعداً فیلدی مثل is_approved یا discount به مدل اضافه شود، خودکار وارد فرم می‌شود و کاربر با دستکاری HTML می‌تواند مقدارش را بفرستد (mass assignment).",
            "choices": [
                {"text": "چون فیلدهای جدید مدل خودکار در فرم قابل‌ارسال می‌شوند و کاربر می‌تواند مقدارشان را دستکاری کند", "correct": True},
                {"text": "چون اعتبارسنجی مدل را غیرفعال می‌کند", "correct": False},
                {"text": "چون توکن CSRF را حذف می‌کند", "correct": False},
                {"text": "چون فرم را کند می‌کند", "correct": False},
            ],
        },
        {
            "text": "در متد `clean()` فرم، چرا باید داده را با `self.cleaned_data.get(\"mobile\")` خواند نه `self.cleaned_data[\"mobile\"]`؟",
            "explanation": "clean() کل فرم حتی وقتی فیلدی خطا داشته اجرا می‌شود و فیلد خطادار در cleaned_data نیست؛ دسترسی با کروشه KeyError می‌دهد.",
            "choices": [
                {"text": "چون get سریع‌تر است", "correct": False},
                {"text": "چون cleaned_data دیکشنری نیست", "correct": False},
                {"text": "چون clean() حتی با خطای فیلدها اجرا می‌شود و فیلد نامعتبر در cleaned_data وجود ندارد", "correct": True},
                {"text": "چون get ارقام فارسی را خودکار نرمال می‌کند", "correct": False},
            ],
        },
        {
            "text": "شماره‌ی موبایل با ارقام فارسی و پیشوند +98 وارد می‌شود و فیلد `max_length=11` دارد. نرمال‌سازی در `clean_mobile` انجام شده اما فرم خطای طول می‌دهد. چرا؟",
            "explanation": "در ترتیب اعتبارسنجی، to_python و validatorهای فیلد (مثل max_length) پیش از clean_<field> اجرا می‌شوند؛ نرمال‌سازی باید در to_python یک فیلد سفارشی یا پیش از اعتبارسنجی انجام شود.",
            "choices": [
                {"text": "چون clean_mobile اصلاً صدا زده نمی‌شود", "correct": False},
                {"text": "چون validatorهای فیلد (از جمله max_length) پیش از clean_mobile اجرا شده‌اند", "correct": True},
                {"text": "چون max_length فقط ارقام لاتین را می‌شمارد", "correct": False},
                {"text": "چون clean() کل فرم پیش از clean_mobile اجرا می‌شود", "correct": False},
            ],
        },
        {
            "text": "صفحه‌ی ثبت سفارش با inline formset خطای «ManagementForm data is missing or has been tampered with» می‌دهد. محتمل‌ترین علت؟",
            "explanation": "formset برای دانستن تعداد فرم‌ها به فیلدهای مخفی management_form نیاز دارد؛ فراموش کردن `{{ formset.management_form }}` در قالب پرتکرارترین باگ formset است.",
            "choices": [
                {"text": "توکن CSRF در فرم نیست", "correct": False},
                {"text": "max_num خیلی کوچک است", "correct": False},
                {"text": "فیلد id هر ردیف رندر نشده", "correct": False},
                {"text": "`{{ formset.management_form }}` در قالب رندر نشده", "correct": True},
            ],
        },
        {
            "text": "پشت nginx و HTTPS، همه‌ی فرم‌های POST با خطای 403 «Origin checking failed» رد می‌شوند. اصلاح درست در Django 5 کدام است؟",
            "explanation": "از Django 4.0 مقادیر CSRF_TRUSTED_ORIGINS باید شامل scheme باشند؛ csrf_exempt سوراخ امنیتی است و راه‌حل نیست.",
            "choices": [
                {"text": "افزودن `\"https://example.ir\"` (با scheme) به CSRF_TRUSTED_ORIGINS", "correct": True},
                {"text": "گذاشتن `@csrf_exempt` روی Viewها", "correct": False},
                {"text": "افزودن `\"example.ir\"` بدون scheme به CSRF_TRUSTED_ORIGINS", "correct": False},
                {"text": "حذف CsrfViewMiddleware از MIDDLEWARE", "correct": False},
            ],
        },
        # ── فصل ۶: ادمین، احراز هویت و دسترسی
        {
            "text": "در Django 5، دکمه‌ی «خروج» به‌صورت لینک ساده‌ی GET به `/accounts/logout/` خطای 405 می‌دهد. چرا؟",
            "explanation": "از Django 5.0 خروج با GET در LogoutView حذف شده است؛ خروج باید با فرم POST همراه توکن CSRF انجام شود تا سایت دیگری نتواند کاربر را خارج کند.",
            "choices": [
                {"text": "چون LogoutView در Django 5 حذف شده", "correct": False},
                {"text": "چون LOGOUT_REDIRECT_URL تنظیم نشده", "correct": False},
                {"text": "چون از Django 5.0 خروج فقط با POST (و توکن CSRF) پذیرفته می‌شود", "correct": True},
                {"text": "چون کاربر is_staff نیست", "correct": False},
            ],
        },
        {
            "text": "کاربری `is_staff=True` دارد اما هیچ مجوزی به او داده نشده. وارد ادمین که می‌شود چه می‌بیند؟",
            "explanation": "is_staff فقط اجازه‌ی ورود به سایت ادمین است، نه مجوز دیدن یا ویرایش مدلی؛ بدون مجوز، صفحه‌ی ادمین خالی است.",
            "choices": [
                {"text": "همه‌ی مدل‌ها را فقط‌خواندنی می‌بیند", "correct": False},
                {"text": "صفحه‌ای خالی؛ is_staff فقط اجازه‌ی ورود به ادمین است", "correct": True},
                {"text": "همه‌ی مدل‌ها را با دسترسی کامل می‌بیند", "correct": False},
                {"text": "خطای 403 در صفحه‌ی ورود", "correct": False},
            ],
        },
        {
            "text": "در ادمین سفارش، `autocomplete_fields = [\"customer\"]` گذاشته‌اید و `check` خطای admin.E040 می‌دهد. چه چیزی کم است؟",
            "explanation": "autocomplete برای جست‌وجو به search_fields در ModelAdmin مدل مقصد (Customer) نیاز دارد.",
            "choices": [
                {"text": "`search_fields` در ModelAdmin مدل Customer", "correct": True},
                {"text": "`list_display` در ModelAdmin سفارش", "correct": False},
                {"text": "`raw_id_fields` کنار autocomplete_fields", "correct": False},
                {"text": "نصب کتابخانه‌ی select2 از CDN", "correct": False},
            ],
        },
        {
            "text": "پیاده‌سازی ورود با OTP روی سرور با چهار worker gunicorn انجام شده و کد در کش پیش‌فرض جنگو ذخیره می‌شود. گاهی کد درست «نامعتبر» اعلام می‌شود. علت؟",
            "explanation": "LocMemCache برای هر پروسه جداست؛ کد ممکن است در worker اول ذخیره و درخواست تأیید به worker دیگر برسد. OTP و rate limit به کش مشترک مثل Redis نیاز دارند.",
            "choices": [
                {"text": "کد با random ساخته شده و تکراری است", "correct": False},
                {"text": "زمان انقضای دو دقیقه خیلی کوتاه است", "correct": False},
                {"text": "هش کد با هر worker فرق می‌کند چون SECRET_KEY متفاوت است", "correct": False},
                {"text": "LocMemCache برای هر worker جداست و کد در worker دیگری ذخیره شده است", "correct": True},
            ],
        },
        # ── فصل ۷: DRF، کش، Celery و امنیت
        {
            "text": "در یک ModelViewSet، permission سفارشی با `has_object_permission` نوشته‌اید تا هر کاربر فقط سفارش‌های خودش را ببیند. در endpoint فهرست (list) هنوز سفارش همه دیده می‌شود. چرا؟",
            "explanation": "has_object_permission فقط وقتی اجرا می‌شود که get_object() صدا زده شود (retrieve، update، destroy)؛ محدودیت فهرست باید در get_queryset اعمال شود.",
            "choices": [
                {"text": "چون permission_classes باید tuple باشد نه list", "correct": False},
                {"text": "چون has_object_permission در list اجرا نمی‌شود؛ فیلتر باید در get_queryset باشد", "correct": True},
                {"text": "چون Router permissionها را نادیده می‌گیرد", "correct": False},
                {"text": "چون pagination فعال است", "correct": False},
            ],
        },
        {
            "text": "روی صفحه‌ای که نام کاربر لاگین‌شده را نشان می‌دهد `@cache_page(60 * 15)` گذاشته‌اید. چه مشکلی پیش می‌آید؟",
            "explanation": "cache_page کل پاسخ را برای همه کش می‌کند؛ کاربر دوم صفحه‌ی کاربر اول (با نامش و حتی توکن CSRF او) را می‌بیند. برای بخش‌های عمومی از کش تکه‌ای یا vary_on_cookie استفاده کنید.",
            "choices": [
                {"text": "مشکلی نیست؛ cache_page خودکار بر اساس کاربر جدا می‌کند", "correct": False},
                {"text": "صفحه هر بار از نو ساخته می‌شود", "correct": False},
                {"text": "کاربران دیگر نسخه‌ی کش‌شده‌ی صفحه‌ی کاربر اول را می‌بینند", "correct": True},
                {"text": "کش فقط برای درخواست‌های POST اعمال می‌شود", "correct": False},
            ],
        },
        {
            "text": "کدام فراخوانی task ارسال پیامک تأیید سفارش در Celery درست‌تر است؟",
            "explanation": "به task شناسه بدهید نه شیء (داده‌ی کهنه و سریال‌سازی)، و آن را پس از commit صف کنید تا worker پیش از commit با DoesNotExist روبه‌رو نشود.",
            "choices": [
                {"text": "`transaction.on_commit(lambda: send_sms.delay(order.id))`", "correct": True},
                {"text": "`send_sms.delay(order)` بلافاصله پس از save", "correct": False},
                {"text": "`send_sms(order)` مستقیم داخل View", "correct": False},
                {"text": "`send_sms.delay(order.id)` قبل از save سفارش", "correct": False},
            ],
        },
        {
            "text": "در models.py برای verbose_name فیلدها از `gettext` (نه `gettext_lazy`) استفاده شده و ترجمه‌ها درست نمایش داده نمی‌شوند. چرا؟",
            "explanation": "کد سطح ماژول و تعریف فیلدها هنگام import اجرا می‌شود، پیش از فعال شدن زبان درخواست؛ gettext_lazy ترجمه را تا زمان نمایش عقب می‌اندازد.",
            "choices": [
                {"text": "چون gettext فقط در قالب‌ها کار می‌کند", "correct": False},
                {"text": "چون فایل .mo کامپایل نشده", "correct": False},
                {"text": "چون gettext متن فارسی را پشتیبانی نمی‌کند", "correct": False},
                {"text": "چون gettext در زمان import، پیش از فعال شدن زبان، ترجمه را انجام می‌دهد", "correct": True},
            ],
        },
        # ── فصل ۸: تست، استقرار و پروژه‌ی پایانی
        {
            "text": "در یک تست با `TestCase`، callback ثبت‌شده با `transaction.on_commit` (مثلاً ارسال پیامک) اجرا نمی‌شود. چطور آن را تست کنیم؟",
            "explanation": "TestCase هر تست را در تراکنشی می‌پیچد که هرگز commit نمی‌شود؛ با `self.captureOnCommitCallbacks(execute=True)` callbackها را می‌گیرید و اجرا می‌کنید.",
            "choices": [
                {"text": "با `self.captureOnCommitCallbacks(execute=True)`", "correct": True},
                {"text": "با تنظیم `ATOMIC_REQUESTS = True`", "correct": False},
                {"text": "با `self.client.force_login`", "correct": False},
                {"text": "on_commit در تست قابل‌تست نیست", "correct": False},
            ],
        },
        {
            "text": "پس از استقرار پشت nginx با `SECURE_SSL_REDIRECT = True`، سایت در حلقه‌ی بی‌نهایت ریدایرکت می‌افتد. تنظیم جاافتاده کدام است؟",
            "explanation": "nginx درخواست را با HTTP به gunicorn می‌دهد؛ بدون SECURE_PROXY_SSL_HEADER (و ارسال X-Forwarded-Proto در nginx) جنگو هر درخواست را HTTP می‌بیند و دوباره ریدایرکت می‌کند.",
            "choices": [
                {"text": "`SESSION_COOKIE_SECURE = True`", "correct": False},
                {"text": "`SECURE_HSTS_SECONDS`", "correct": False},
                {"text": "`SECURE_PROXY_SSL_HEADER = (\"HTTP_X_FORWARDED_PROTO\", \"https\")`", "correct": True},
                {"text": "`ALLOWED_HOSTS = [\"*\"]`", "correct": False},
            ],
        },
        {
            "text": "کد جدید را روی سرور pull کرده‌اید اما سایت هنوز رفتار قبلی را دارد. کدام دستور بدون قطع درخواست‌های در جریان، کد جدید را بارگذاری می‌کند؟",
            "explanation": "gunicorn کد را فقط هنگام شروع worker بارگذاری می‌کند؛ reload (سیگنال HUP) workerها را به‌آرامی عوض می‌کند بی‌آن‌که درخواست‌های در حال اجرا قطع شوند.",
            "choices": [
                {"text": "`sudo systemctl restart nginx`", "correct": False},
                {"text": "`python manage.py collectstatic`", "correct": False},
                {"text": "`python manage.py runserver 0.0.0.0:8000`", "correct": False},
                {"text": "`sudo systemctl reload carpet` (سرویس gunicorn پروژه)", "correct": True},
            ],
        },
        {
            "text": "با `CompressedManifestStaticFilesStorage` و DEBUG=False، یک صفحه خطای 500 «Missing staticfiles manifest entry» می‌دهد. علت چیست؟",
            "explanation": "این storage برای هر فایل static نام هش‌دار را از manifest می‌خواند؛ اگر قالب به فایلی اشاره کند که وجود ندارد یا collectstatic اجرا نشده، خطای 500 می‌دهد.",
            "choices": [
                {"text": "WhiteNoise با nginx سازگار نیست", "correct": False},
                {"text": "قالب به فایل static اشاره می‌کند که وجود ندارد یا collectstatic اجرا نشده", "correct": True},
                {"text": "MEDIA_ROOT تنظیم نشده", "correct": False},
                {"text": "DEBUG باید روی سرور True باشد", "correct": False},
            ],
        },
    ],
}

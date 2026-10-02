# -*- coding: utf-8 -*-

QUIZ = {
    "course_slug": 'laravel',
    "title": 'آزمون پایانی لاراول',
    "pass_percent": 70,
    "time_limit_minutes": 20,
    "questions": [
        {
            "text": 'لاراول از چه الگوی معماری\u200cای برای جدا کردن منطق برنامه پیروی می\u200cکند؟',
            "explanation": 'لاراول از الگوی MVC (Model-View-Controller) پیروی می\u200cکند که کد را به سه بخش جدا تقسیم می\u200cکند.',
            "choices": [
                {"text": 'MVVM', "correct": False},
                {"text": 'Singleton Pattern', "correct": False},
                {"text": 'MVC (Model-View-Controller)', "correct": True},
                {"text": 'فقط معماری REST بدون View', "correct": False},
            ],
        },
        {
            "text": 'دستور خط فرمان artisan در لاراول معمولاً برای چه کارهایی استفاده می\u200cشود؟',
            "explanation": 'artisan برای ساخت Controller، Model، Migration و بسیاری کارهای تکراری دیگر به کار می\u200cرود.',
            "choices": [
                {"text": 'ساخت Controller، Model، Migration و کارهای تکراری مشابه', "correct": True},
                {"text": 'فقط اجرای تست\u200cهای واحد', "correct": False},
                {"text": 'فقط مدیریت گرافیکی دیتابیس', "correct": False},
                {"text": 'جایگزین کامل Composer', "correct": False},
            ],
        },
        {
            "text": 'تمام مسیرهای وب یک پروژه\u200cی لاراول معمولاً در کدام فایل تعریف می\u200cشوند؟',
            "explanation": 'مسیرهای وب در فایل routes/web.php تعریف می\u200cشوند.',
            "choices": [
                {"text": 'app/routes.php', "correct": False},
                {"text": 'config/routes.php', "correct": False},
                {"text": 'resources/routes.php', "correct": False},
                {"text": 'routes/web.php', "correct": True},
            ],
        },
        {
            "text": 'برای نمایش امن یک متغیر در Blade (با escape خودکار در برابر XSS) از چه سینتکسی استفاده می\u200cشود؟',
            "explanation": 'دو آکولاد {{ $variable }} در Blade خروجی را به\u200cطور خودکار escape می\u200cکند.',
            "choices": [
                {"text": '{{ $variable }}', "correct": True},
                {"text": '`<?php echo $variable ?>`', "correct": False},
                {"text": '{% $variable %}', "correct": False},
                {"text": '@$variable', "correct": False},
            ],
        },
        {
            "text": 'Migration در لاراول اصلی\u200cترین هدفش چیست؟',
            "explanation": 'Migration روشی برای تعریف و مدیریت نسخه\u200cدار ساختار جداول دیتابیس با کد PHP است.',
            "choices": [
                {"text": 'تعریف و مدیریت نسخه\u200cدار ساختار جداول دیتابیس با کد PHP', "correct": True},
                {"text": 'اجرای مستقیم کوئری\u200cهای SQL بدون هیچ کدی', "correct": False},
                {"text": 'فقط پشتیبان\u200cگیری از داده\u200cهای موجود', "correct": False},
                {"text": 'جایگزین کامل Eloquent در همه\u200cی موارد', "correct": False},
            ],
        },
        {
            "text": 'کدام دستور artisan تمام Migrationهای در انتظار را روی دیتابیس اجرا می\u200cکند؟',
            "explanation": 'دستور php artisan migrate تمام Migrationهای اجرا\u200cنشده را روی دیتابیس اعمال می\u200cکند.',
            "choices": [
                {"text": 'php artisan db:seed', "correct": False},
                {"text": 'php artisan migrate', "correct": True},
                {"text": 'php artisan make:migration', "correct": False},
                {"text": 'php artisan serve', "correct": False},
            ],
        },
        {
            "text": 'متد findOrFail در Eloquent در صورت پیدا نشدن رکورد موردنظر چه کاری انجام می\u200cدهد؟',
            "explanation": 'findOrFail در صورت نبود رکورد، به\u200cجای بازگرداندن null، خطای 404 مناسب صادر می\u200cکند.',
            "choices": [
                {"text": 'مقدار null برمی\u200cگرداند', "correct": False},
                {"text": 'یک رکورد خالی جدید در دیتابیس می\u200cسازد', "correct": False},
                {"text": 'برنامه را بدون هیچ خطایی متوقف می\u200cکند', "correct": False},
                {"text": 'خطای 404 مناسب صادر می\u200cکند', "correct": True},
            ],
        },
        {
            "text": 'برای تعریف رابطه\u200cی یک\u200cبه\u200cچند در سمت مدل User (مثلاً یک کاربر چند مقاله دارد)، از کدام متد استفاده می\u200cشود؟',
            "explanation": 'متد hasMany() در سمت User برای تعریف رابطه\u200cی یک\u200cبه\u200cچند با مدل Post استفاده می\u200cشود.',
            "choices": [
                {"text": 'hasMany()', "correct": True},
                {"text": 'belongsTo()', "correct": False},
                {"text": 'belongsToMany()', "correct": False},
                {"text": 'hasOne()', "correct": False},
            ],
        },
        {
            "text": 'استفاده از متد with() برای Eager Loading در Eloquent چه مشکلی را برطرف می\u200cکند؟',
            "explanation": 'with() مشکل معروف N+1 Query را حل می\u200cکند و داده\u200cهای مرتبط را در یکی دو کوئری بارگذاری می\u200cکند.',
            "choices": [
                {"text": 'کند شدن اجرای Migration', "correct": False},
                {"text": 'مشکل N+1 Query', "correct": True},
                {"text": 'خطاهای Validation فرم', "correct": False},
                {"text": 'مشکل احراز هویت کاربر', "correct": False},
            ],
        },
        {
            "text": 'اعتبارسنجی ورودی\u200cهای فرم در Controller لاراول معمولاً با کدام متد روی شیء Request انجام می\u200cشود؟',
            "explanation": 'متد validate() روی شیء Request قوانین اعتبارسنجی را بررسی می\u200cکند.',
            "choices": [
                {"text": 'check()', "correct": False},
                {"text": 'verify()', "correct": False},
                {"text": 'validate()', "correct": True},
                {"text": 'sanitize()', "correct": False},
            ],
        },
        {
            "text": 'لاراول به\u200cطور پیش\u200cفرض رمزهای عبور کاربران را با چه الگوریتمی هش می\u200cکند؟',
            "explanation": 'لاراول به\u200cصورت پیش\u200cفرض از الگوریتم bcrypt برای هش کردن امن رمز عبور استفاده می\u200cکند.',
            "choices": [
                {"text": 'bcrypt', "correct": True},
                {"text": 'MD5 ساده', "correct": False},
                {"text": 'بدون هش، به\u200cصورت متن ساده', "correct": False},
                {"text": 'Base64', "correct": False},
            ],
        },
        {
            "text": 'Middleware در لاراول در کدام مرحله از پردازش یک درخواست HTTP اجرا می\u200cشود؟',
            "explanation": 'Middleware پیش از رسیدن درخواست HTTP به Controller اجرا می\u200cشود و می\u200cتواند آن را بررسی یا متوقف کند.',
            "choices": [
                {"text": 'فقط پس از ارسال پاسخ نهایی به کاربر', "correct": False},
                {"text": 'پیش از رسیدن درخواست به Controller', "correct": True},
                {"text": 'فقط هنگام اجرای Migration', "correct": False},
                {"text": 'فقط در محیط توسعه و نه در Production', "correct": False},
            ],
        },
        {
            "text": 'هدف اصلی استفاده از API Resource (مانند PostResource) در لاراول چیست؟',
            "explanation": 'API Resource کنترل کاملی روی ساختار خروجی JSON می\u200cدهد و از فاش شدن فیلدهای حساس جلوگیری می\u200cکند.',
            "choices": [
                {"text": 'کنترل ساختار خروجی JSON و جلوگیری از فاش شدن فیلدهای حساس', "correct": True},
                {"text": 'جایگزین کامل Eloquent برای خواندن داده', "correct": False},
                {"text": 'افزایش سرعت اجرای Migration', "correct": False},
                {"text": 'مدیریت مستقیم Middleware', "correct": False},
            ],
        },
        {
            "text": 'سیستم صف (Queue) در لاراول برای چه نوع عملیاتی کاربرد دارد؟',
            "explanation": 'صف برای انتقال عملیات زمان\u200cبر مانند ارسال ایمیل به یک پردازش پس\u200cزمینه استفاده می\u200cشود تا پاسخ به کاربر سریع بماند.',
            "choices": [
                {"text": 'افزایش سرعت تعریف Routeها', "correct": False},
                {"text": 'جایگزینی کامل موتور قالب Blade', "correct": False},
                {"text": 'انتقال عملیات زمان\u200cبر (مانند ارسال ایمیل) به پردازش پس\u200cزمینه', "correct": True},
                {"text": 'مدیریت مجوزهای کاربران', "correct": False},
            ],
        },
        {
            "text": 'هنگام استقرار (deploy) یک پروژه\u200cی لاراول، Document Root وب\u200cسرور باید به کدام پوشه اشاره کند؟',
            "explanation": 'Document Root باید به پوشه\u200cی public اشاره کند تا فایل\u200cهای حساس مانند .env در دسترس عمومی نباشند.',
            "choices": [
                {"text": 'پوشه\u200cی public', "correct": True},
                {"text": 'ریشه\u200cی اصلی پروژه', "correct": False},
                {"text": 'پوشه\u200cی storage', "correct": False},
                {"text": 'پوشه\u200cی vendor', "correct": False},
            ],
        },
    ],
}

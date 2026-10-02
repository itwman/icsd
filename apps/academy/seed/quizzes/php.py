# -*- coding: utf-8 -*-

QUIZ = {
    "course_slug": 'php',
    "title": 'آزمون پایانی PHP',
    "pass_percent": 70,
    "time_limit_minutes": 20,
    "questions": [
        {
            "text": 'کد PHP کجا اجرا می\u200cشود و نتیجه به چه شکلی به مرورگر کاربر ارسال می\u200cگردد؟',
            "explanation": 'PHP یک زبان سمت سرور است؛ کد روی سرور اجرا و خروجی به\u200cصورت HTML به مرورگر فرستاده می\u200cشود.',
            "choices": [
                {"text": 'مستقیماً روی مرورگر کاربر اجرا می\u200cشود', "correct": False},
                {"text": 'روی سرور اجرا می\u200cشود و خروجی به\u200cصورت HTML به مرورگر فرستاده می\u200cشود', "correct": True},
                {"text": 'فقط به\u200cصورت فایل متنی ذخیره می\u200cشود و اجرا نمی\u200cشود', "correct": False},
                {"text": 'نیازی به هیچ سروری ندارد', "correct": False},
            ],
        },
        {
            "text": 'برای اجرای سریع یک پروژه\u200cی PHP بدون نیاز به نصب Apache، از کدام دستور استفاده می\u200cشود؟',
            "explanation": 'دستور `php -S localhost:8000` وب\u200cسرور توسعه\u200cی داخلی PHP را روی پورت مشخص اجرا می\u200cکند.',
            "choices": [
                {"text": '`php -S localhost:8000`', "correct": True},
                {"text": '`php run server`', "correct": False},
                {"text": '`start-php-server`', "correct": False},
                {"text": '`apache2ctl --php`', "correct": False},
            ],
        },
        {
            "text": 'هر بلوک کد PHP با کدام تگ آغاز می\u200cشود؟',
            "explanation": 'بلوک\u200cهای کد PHP با `<?php` آغاز و با `?>` بسته می\u200cشوند.',
            "choices": [
                {"text": '`<php>`', "correct": False},
                {"text": '`<script php>`', "correct": False},
                {"text": '`<?php`', "correct": True},
                {"text": '`<?php-start>`', "correct": False},
            ],
        },
        {
            "text": 'برای تعریف یک متغیر در PHP، پیش از نام آن از چه علامتی استفاده می\u200cشود؟',
            "explanation": 'نام متغیرها در PHP همیشه با علامت دلار ($) شروع می\u200cشود، مانند `$name`.',
            "choices": [
                {"text": '$', "correct": True},
                {"text": '@', "correct": False},
                {"text": '#', "correct": False},
                {"text": '&', "correct": False},
            ],
        },
        {
            "text": 'تفاوت اصلی عملگر `==` و `===` در PHP چیست؟',
            "explanation": '`===` هم مقدار و هم نوع دو طرف را مقایسه می\u200cکند، در حالی که `==` فقط مقدار را بررسی می\u200cکند.',
            "choices": [
                {"text": 'هیچ تفاوتی ندارند و کاملاً یکسان عمل می\u200cکنند', "correct": False},
                {"text": '== نوع را هم بررسی می\u200cکند ولی === فقط مقدار را', "correct": False},
                {"text": '=== فقط برای رشته\u200cها کاربرد دارد', "correct": False},
                {"text": '=== هم مقدار و هم نوع را مقایسه می\u200cکند، اما == فقط مقدار را بررسی می\u200cکند', "correct": True},
            ],
        },
        {
            "text": 'کدام حلقه برای پیمایش عناصر یک آرایه در PHP پرکاربردتر و ساده\u200cتر است؟',
            "explanation": 'حلقه\u200cی `foreach` ساده\u200cترین و پرکاربردترین روش پیمایش عناصر یک آرایه در PHP است.',
            "choices": [
                {"text": 'for', "correct": False},
                {"text": 'foreach', "correct": True},
                {"text": 'while', "correct": False},
                {"text": 'do-while', "correct": False},
            ],
        },
        {
            "text": 'در آرایه\u200cی انجمنی (associative array) PHP، هر عنصر چگونه مشخص می\u200cشود؟',
            "explanation": "در آرایه\u200cی انجمنی هر عنصر با یک کلید متنی دلخواه (مثل 'name') مشخص می\u200cشود، نه فقط با عدد.",
            "choices": [
                {"text": "با یک کلید متنی دلخواه (مانند 'name')", "correct": True},
                {"text": 'فقط با عدد ایندکس شروع\u200cشده از صفر', "correct": False},
                {"text": 'بدون هیچ کلید یا ایندکسی', "correct": False},
                {"text": 'فقط بر اساس ترتیب تعریف در کد', "correct": False},
            ],
        },
        {
            "text": 'تابع `array_map()` در PHP چه کاری انجام می\u200cدهد؟',
            "explanation": 'array_map یک تابع را روی تک\u200cتک عناصر آرایه اعمال کرده و آرایه\u200cای جدید با نتایج برمی\u200cگرداند.',
            "choices": [
                {"text": 'عناصر آرایه را مرتب\u200cسازی می\u200cکند', "correct": False},
                {"text": 'یک عنصر مشخص را از آرایه حذف می\u200cکند', "correct": False},
                {"text": 'یک تابع را روی تمام عناصر آرایه اعمال می\u200cکند و آرایه\u200cی جدید برمی\u200cگرداند', "correct": True},
                {"text": 'دو آرایه را با هم مقایسه می\u200cکند', "correct": False},
            ],
        },
        {
            "text": 'کدام تابع بررسی می\u200cکند که آیا مقداری در یک آرایه وجود دارد یا نه؟',
            "explanation": 'تابع `in_array()` بررسی می\u200cکند که آیا یک مقدار در آرایه موجود است یا خیر.',
            "choices": [
                {"text": 'array_key_exists()', "correct": False},
                {"text": 'array_sum()', "correct": False},
                {"text": 'count()', "correct": False},
                {"text": 'in_array()', "correct": True},
            ],
        },
        {
            "text": 'در تعریف تابع PHP، اگر پارامتری مقدار پیش\u200cفرض داشته باشد و در فراخوانی برایش مقداری ارسال نشود، چه اتفاقی می\u200cافتد؟',
            "explanation": 'اگر مقداری برای پارامتر دارای مقدار پیش\u200cفرض ارسال نشود، همان مقدار پیش\u200cفرض به\u200cجای آن استفاده می\u200cشود.',
            "choices": [
                {"text": 'همان مقدار پیش\u200cفرض تعریف\u200cشده استفاده می\u200cشود', "correct": True},
                {"text": 'PHP بلافاصله خطای اجرا صادر می\u200cکند', "correct": False},
                {"text": 'مقدار null در نظر گرفته شده و برنامه متوقف می\u200cشود', "correct": False},
                {"text": 'تابع اصلاً اجرا نمی\u200cشود', "correct": False},
            ],
        },
        {
            "text": 'وقتی ویژگی method یک فرم HTML برابر با post باشد، داده\u200cهای ارسالی در کدام متغیر سراسری در دسترس\u200cاند؟',
            "explanation": "در حالت method='post'، داده\u200cها در بدنه\u200cی درخواست ارسال شده و در $_POST قابل دسترسی هستند.",
            "choices": [
                {"text": '$_POST', "correct": True},
                {"text": '$_GET', "correct": False},
                {"text": '$_SESSION', "correct": False},
                {"text": '$_COOKIE', "correct": False},
            ],
        },
        {
            "text": 'تابع `session_start()` باید پیش از چه چیزی در صفحه فراخوانی شود؟',
            "explanation": 'session_start() باید پیش از هرگونه خروجی HTML فراخوانی شود، وگرنه PHP خطای هدر می\u200cدهد.',
            "choices": [
                {"text": 'فقط در انتهای فایل و بعد از چاپ محتوا', "correct": False},
                {"text": 'فقط داخل تابع logout', "correct": False},
                {"text": 'فقط در فایل composer.json', "correct": False},
                {"text": 'پیش از هرگونه خروجی HTML در صفحه', "correct": True},
            ],
        },
        {
            "text": 'برای ذخیره\u200cی داده در سمت مرورگر کاربر (نه روی سرور)، از کدام مکانیزم استفاده می\u200cشود؟',
            "explanation": 'کوکی (Cookie) با تابع setcookie() اطلاعات را در سمت مرورگر کاربر ذخیره می\u200cکند.',
            "choices": [
                {"text": 'Session با تابع session_start()', "correct": False},
                {"text": 'Cookie با تابع setcookie()', "correct": True},
                {"text": 'متغیر سراسری $_SERVER', "correct": False},
                {"text": 'فایل موقت روی سرور', "correct": False},
            ],
        },
        {
            "text": 'برای جلوگیری از حمله\u200cی SQL Injection هنگام کار با PDO، بهترین روش کدام است؟',
            "explanation": 'استفاده از Prepared Statement پارامترها را جدا از متن کوئری ارسال می\u200cکند و در برابر SQL Injection مقاوم است.',
            "choices": [
                {"text": 'استفاده از Prepared Statement و ارسال جداگانه\u200cی پارامترها', "correct": True},
                {"text": 'قرار دادن مستقیم ورودی کاربر داخل رشته\u200cی کوئری', "correct": False},
                {"text": 'غیرفعال کردن ATTR_ERRMODE', "correct": False},
                {"text": 'استفاده از htmlspecialchars روی متن کوئری SQL', "correct": False},
            ],
        },
        {
            "text": 'دستور `composer require nesbot/carbon` چه کاری انجام می\u200cدهد؟',
            "explanation": 'این دستور کتابخانه\u200cی Carbon را از طریق Composer نصب کرده و به پروژه اضافه می\u200cکند.',
            "choices": [
                {"text": 'یک پروژه\u200cی کاملاً جدید PHP می\u200cسازد', "correct": False},
                {"text": 'فایل composer.json را حذف می\u200cکند', "correct": False},
                {"text": 'نسخه\u200cی PHP نصب\u200cشده را به\u200cروزرسانی می\u200cکند', "correct": False},
                {"text": 'کتابخانه\u200cی Carbon را نصب و به پروژه اضافه می\u200cکند', "correct": True},
            ],
        },
    ],
}

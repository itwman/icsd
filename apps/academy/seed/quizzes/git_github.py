# -*- coding: utf-8 -*-

QUIZ = {
    "course_slug": "git-github",
    "title": "آزمون پایانی گیت و گیت‌هاب",
    "pass_percent": 70,
    "time_limit_minutes": 20,
    "questions": [
        {
            "text": "تفاوت اصلی بین گیت (Git) و گیت‌هاب (GitHub) در چیست؟",
            "explanation": "گیت ابزار خط فرمان برای کنترل نسخه است و گیت‌هاب یک سرویس آنلاین برای میزبانی مخازن گیت است که از خود گیت استفاده می‌کند.",
            "choices": [
                {"text": "گیت و گیت‌هاب دقیقاً یک چیز هستند با دو نام متفاوت", "correct": False},
                {"text": "گیت ابزار خط فرمان است و گیت‌هاب یک پلتفرم آنلاین مبتنی بر گیت است", "correct": True},
                {"text": "گیت‌هاب جایگزین کامل نصب گیت روی سیستم است", "correct": False},
                {"text": "گیت فقط برای ویندوز و گیت‌هاب فقط برای لینوکس است", "correct": False},
            ],
        },
        {
            "text": "دستور `git config --global user.email \"ali@example.com\"` چه کاری انجام می‌دهد؟",
            "explanation": "این دستور ایمیل کاربر را برای همه‌ی پروژه‌های روی سیستم تنظیم می‌کند؛ این اطلاعات در هر commit ثبت می‌شود.",
            "choices": [
                {"text": "ثبت ایمیل کاربر برای همه‌ی پروژه‌های روی سیستم", "correct": True},
                {"text": "ارسال یک ایمیل خودکار پس از هر commit", "correct": False},
                {"text": "ساخت یک حساب کاربری جدید در گیت‌هاب", "correct": False},
                {"text": "تغییر ایمیل فقط برای آخرین commit انجام‌شده", "correct": False},
            ],
        },
        {
            "text": "دستور `git init` در یک پوشه‌ی پروژه دقیقاً چه کاری انجام می‌دهد؟",
            "explanation": "git init یک پوشه‌ی مخفی به نام .git می‌سازد که قلب مخزن است و تمام تاریخچه، شاخه‌ها و تنظیمات گیت درون آن ذخیره می‌شود.",
            "choices": [
                {"text": "فایل‌های پروژه را به سرور گیت‌هاب آپلود می‌کند", "correct": False},
                {"text": "یک پوشه‌ی مخفی به نام .git برای شروع ردیابی پروژه می‌سازد", "correct": True},
                {"text": "تمام فایل‌های پروژه را کامپایل می‌کند", "correct": False},
                {"text": "یک نسخه‌ی پشتیبان از پروژه در گیت‌هاب می‌سازد", "correct": False},
            ],
        },
        {
            "text": "ناحیه‌ی «Staging Area» در گیت چیست؟",
            "explanation": "Staging Area ناحیه‌ی میانی بین working directory و repository است که با دستور git add تغییرات به آن اضافه می‌شود، پیش از ثبت نهایی با commit.",
            "choices": [
                {"text": "همان فایل‌های واقعی روی دیسک", "correct": False},
                {"text": "ناحیه‌ی میانی که تغییرات با git add به آن اضافه می‌شوند", "correct": True},
                {"text": "بخشی از گیت‌هاب برای بررسی کد", "correct": False},
                {"text": "پوشه‌ای که فقط commitهای قدیمی در آن نگه‌داری می‌شود", "correct": False},
            ],
        },
        {
            "text": "استفاده از `git commit --amend` در چه شرایطی امن است؟",
            "explanation": "amend فقط برای commitهایی امن است که هنوز به هیچ مخزن مشترکی push نشده‌اند، چون شناسه‌ی commit را تغییر می‌دهد.",
            "choices": [
                {"text": "همیشه، بدون هیچ محدودیتی", "correct": False},
                {"text": "فقط زمانی که commit روی شاخه‌ی main باشد", "correct": False},
                {"text": "فقط برای commitهایی که هنوز push نشده‌اند", "correct": True},
                {"text": "فقط پس از باز شدن Pull Request", "correct": False},
            ],
        },
        {
            "text": "فایل `.gitignore` در ریشه‌ی یک پروژه چه کاربردی دارد؟",
            "explanation": "این فایل مشخص می‌کند کدام فایل‌ها و پوشه‌ها (مانند venv/ یا .env) نباید وارد تاریخچه‌ی گیت شوند.",
            "choices": [
                {"text": "مشخص کردن فایل‌هایی که نباید وارد تاریخچه‌ی گیت شوند", "correct": True},
                {"text": "لیست کردن همه‌ی commitهای انجام‌شده", "correct": False},
                {"text": "تنظیم نام کاربری و ایمیل گیت", "correct": False},
                {"text": "مشخص کردن شاخه‌ی پیش‌فرض پروژه", "correct": False},
            ],
        },
        {
            "text": "تفاوت اصلی «fast-forward merge» با «merge commit» چیست؟",
            "explanation": "اگر main از زمان جدا شدن شاخه‌ی feature پیشرفتی نداشته باشد، فقط اشاره‌گر main جلو می‌رود (fast-forward)؛ در غیر این صورت یک merge commit با دو والد ساخته می‌شود.",
            "choices": [
                {"text": "fast-forward فقط در گیت‌هاب و merge commit فقط محلی است", "correct": False},
                {"text": "fast-forward فقط اشاره‌گر شاخه را جلو می‌برد؛ merge commit یک commit جدید با دو والد می‌سازد", "correct": True},
                {"text": "fast-forward همیشه باعث تعارض (conflict) می‌شود", "correct": False},
                {"text": "هیچ تفاوتی ندارند و نتیجه‌ی هر دو کاملاً یکسان است", "correct": False},
            ],
        },
        {
            "text": "تفاوت اصلی `git rebase` با `git merge` در ترکیب دو شاخه چیست؟",
            "explanation": "rebase کامیت‌های شاخه‌ی فعلی را روی نوک شاخه‌ی مقصد بازپخش می‌کند و تاریخچه‌ای خطی می‌سازد؛ merge یک commit ادغام جدید با دو والد می‌سازد.",
            "choices": [
                {"text": "rebase و merge دقیقاً یک نتیجه‌ی یکسان تولید می‌کنند", "correct": False},
                {"text": "merge فقط برای مخازن گیت‌هاب کار می‌کند", "correct": False},
                {"text": "rebase کامیت‌ها را روی شاخه‌ی مقصد بازپخش می‌کند و تاریخچه را خطی می‌سازد", "correct": True},
                {"text": "rebase هرگز شناسه‌ی commitها را تغییر نمی‌دهد", "correct": False},
            ],
        },
        {
            "text": "«قاعده‌ی طلایی» درباره‌ی استفاده از `git rebase` که در دوره تأکید شده چیست؟",
            "explanation": "هرگز نباید شاخه‌ای را که دیگران هم روی آن کار می‌کنند یا قبلاً push و به اشتراک گذاشته شده، rebase کرد؛ چون شناسه‌ی commitها عوض می‌شود.",
            "choices": [
                {"text": "rebase باید همیشه به‌جای merge استفاده شود", "correct": False},
                {"text": "هرگز شاخه‌ای را که به اشتراک گذاشته شده rebase نکنید", "correct": True},
                {"text": "rebase فقط روی شاخه‌ی main مجاز است", "correct": False},
                {"text": "rebase فقط باید توسط مدیر پروژه اجرا شود", "correct": False},
            ],
        },
        {
            "text": "دستور `git clone https://github.com/username/my-project.git` چه کاری انجام می‌دهد؟",
            "explanation": "این دستور کل تاریخچه‌ی مخزن، همه‌ی شاخه‌ها و فایل‌ها را دانلود کرده و remote به نام origin را به‌صورت خودکار تنظیم می‌کند.",
            "choices": [
                {"text": "فقط آخرین commit را بدون تاریخچه دانلود می‌کند", "correct": False},
                {"text": "کل مخزن به همراه تاریخچه را دانلود و remote origin را خودکار تنظیم می‌کند", "correct": True},
                {"text": "یک شاخه‌ی جدید و خالی روی گیت‌هاب می‌سازد", "correct": False},
                {"text": "فقط فایل README پروژه را دانلود می‌کند", "correct": False},
            ],
        },
        {
            "text": "دستور `git pull` در واقع ترکیبی از کدام دو دستور دیگر است؟",
            "explanation": "git pull ترکیبی از git fetch (دانلود تغییرات جدید) و git merge (ادغام آن‌ها با شاخه‌ی محلی) است.",
            "choices": [
                {"text": "git add و git commit", "correct": False},
                {"text": "git clone و git init", "correct": False},
                {"text": "git fetch و git merge", "correct": True},
                {"text": "git branch و git checkout", "correct": False},
            ],
        },
        {
            "text": "هدف اصلی باز کردن یک Pull Request به‌جای push مستقیم روی شاخه‌ی main چیست؟",
            "explanation": "باز کردن PR فرصت بررسی کد (Code Review) را پیش از ورود تغییرات به نسخه‌ی اصلی پروژه فراهم می‌کند.",
            "choices": [
                {"text": "افزایش سرعت آپلود فایل‌ها به گیت‌هاب", "correct": False},
                {"text": "حذف نیاز به نوشتن پیام commit", "correct": False},
                {"text": "فراهم کردن فرصت بررسی کد پیش از ادغام با شاخه‌ی اصلی", "correct": True},
                {"text": "غیرفعال کردن GitHub Actions برای آن شاخه", "correct": False},
            ],
        },
        {
            "text": "تگ (tag) در گیت، برخلاف branch، چه ویژگی خاصی دارد؟",
            "explanation": "tagها برخلاف branch حرکت نمی‌کنند؛ یعنی همیشه به همان commit خاص اشاره می‌کنند، حتی اگر تاریخچه‌ی شاخه‌ی اصلی جلوتر برود.",
            "choices": [
                {"text": "به‌طور خودکار هر روز به‌روزرسانی می‌شود", "correct": False},
                {"text": "همیشه به یک commit خاص اشاره می‌کند و حرکت نمی‌کند", "correct": True},
                {"text": "فقط در مخازن خصوصی قابل استفاده است", "correct": False},
                {"text": "با هر merge به‌طور خودکار حذف می‌شود", "correct": False},
            ],
        },
        {
            "text": "فایل‌های تنظیمات GitHub Actions معمولاً در کدام مسیر پروژه قرار می‌گیرند؟",
            "explanation": "تنظیمات GitHub Actions با فایل‌های YAML در مسیر .github/workflows/ نوشته می‌شود.",
            "choices": [
                {"text": ".github/workflows/", "correct": True},
                {"text": "actions/config/", "correct": False},
                {"text": "ci/scripts/", "correct": False},
                {"text": ".git/actions/", "correct": False},
            ],
        },
        {
            "text": "رایج‌ترین کاربرد GitHub Actions که در دوره معرفی شد چیست؟",
            "explanation": "رایج‌ترین کاربرد آن، اجرای خودکار تست‌ها پیش از merge (یعنی Continuous Integration یا CI) در پاسخ به رویدادهایی مثل push یا Pull Request است.",
            "choices": [
                {"text": "طراحی گرافیکی صفحات وب", "correct": False},
                {"text": "اجرای خودکار تست‌ها پیش از merge (Continuous Integration)", "correct": True},
                {"text": "جایگزینی کامل دستور git commit", "correct": False},
                {"text": "مدیریت پایگاه داده‌ی پروژه", "correct": False},
            ],
        },
    ],
}

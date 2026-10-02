"""
داده‌ی اولیه‌ی سایت: تنظیمات، منو، بخش‌های صفحه اصلی، خط زمان کاشان، صفحات، محصولات،
ریدایرکت آدرس‌های قدیمی وردپرس. اجرا: python manage.py seed_site
"""
from django.core.management.base import BaseCommand

from apps.core.models import HomeSection, NavLink, Page, SiteSettings, TimelineEvent
from apps.seo.models import Redirect

NAV = [("محصولات", "/products/"), ("آکادمی", "/courses/"), ("از سیلک تا سرور", "/#kashan"),
       ("مقالات", "/blog/"), ("شروع پروژه", "/start-project/")]

SECTIONS = [
    ("sialk", "TAPPEH SIALK · KASHAN · 33.97°N 51.40°E", "تپه‌های شمالی و جنوبی سیلک — هفت هزار سال لایه، و شبکه‌ای که آن‌ها را می‌خواند", ""),
    ("band", "", "نوار نقش سفال سیلک", ""),
    ("products", "محصولات", "نرم‌افزارهایی که می‌سازیم", "هر کدام از دل یک مسئله‌ی واقعی در کارخانه، بازار فرش یا یک سازمان بیرون آمده است."),
    ("customers", "مشتریان", "کسانی که با ما کار می‌کنند", "کارخانه‌ها، بازرگانان و سازمان‌هایی که نرم‌افزارهای ما هر روز در کارشان است."),
    ("timeline", "از سیلک تا سرور", "کاشان، شهر مهندسان", "این فهرست تبلیغات نیست؛ سابقه‌ی فنی یک شهر است که ما نفر بعدی‌اش هستیم."),
    ("academy", "آکادمی", "آنچه در کارگاه یاد گرفتیم، درس می‌دهیم", "هیچ دوره‌ای اینجا نیست که از دل یک پروژه‌ی واقعی بیرون نیامده باشد."),
    ("blog", "مقالات", "از دفترچه‌ی فنی ما", ""),
    ("cta", "تماس", "مسئله‌تان را بگویید، معماری‌اش را می‌نویسیم", "جلسه‌ی اول رایگان است. اگر راهکار آماده‌ای داشته باشیم همان را پیشنهاد می‌دهیم؛ اگر نه، از صفر می‌سازیم."),
]
SECTION_LIMITS = {"products": 8, "customers": 0, "academy": 6, "blog": 3}

TIMELINE = [
    ("۵۵۰۰ پیش از میلاد", "تپه سیلک", "کهن‌ترین سکونتگاه شناخته‌شده‌ی فلات ایران. سفال نقش‌دار، خشت، و نخستین سازه‌ی پلکانی — هفت هزار سال پیش، همین‌جا.", "#D2623E"),
    ("هزاره‌ی اول پیش از میلاد", "قنات", "انتقال آب زیرزمینی با شیب کنترل‌شده در ده‌ها کیلومتر — یک سامانه‌ی توزیع، قرن‌ها پیش از لوله‌کشی.", "#F2A83B"),
    ("۹۹۴ خورشیدی", "باغ فین", "فواره‌های بدون پمپ، فقط با اختلاف ارتفاع. مهندسی هیدرولیک که چهارصد سال است کار می‌کند.", "#16A9C7"),
    ("دوره‌ی قاجار", "بادگیر و خانه‌های تاریخی", "خنک‌سازی غیرفعال در دل کویر — بروجردی‌ها و طباطبایی‌ها، پیش از آنکه کولر اختراع شود.", "#F05C7E"),
    ("۱۳۹۶ تا امروز", "توسعه هوشمند فرش ایرانیان", "همان شهر، همان کار: ساختن سامانه‌ای که بدون سر و صدا، سال‌ها درست کار کند — این بار با کد و هوش مصنوعی.", "#1E9E7B"),
]

# آدرس‌های قدیمی وردپرس → جدید
REDIRECTS = [
    ("/noban/", "/products/noban/", 301), ("/farsh-plus/", "/products/farsh-plus/", 301),
    ("/roham/", "/products/roham/", 301), ("/cheleh/", "/products/chelleh/", 301),
    ("/danayar/", "/products/danayar/", 301), ("/dook/", "/products/", 301),
    ("/radman/", "/products/رادمان/", 301), ("/diaco/", "/products/diaco/", 301),
    ("/rayeshgar/", "/products/رایشگر/", 301), ("/manix/", "/products/manix/", 301),
    ("/courses/", "/courses/", 301), ("/دوره-های-آموزشی/", "/courses/", 301),
    ("/instructors/", "/courses/", 301), ("/instructor/", "/courses/", 301),
    ("/become_a_teacher/", "/start-project/", 301), ("/lp-profile/", "/accounts/dashboard/", 301),
    ("/my-account/", "/accounts/dashboard/", 301), ("/lp-checkout/", "/courses/", 301),
    ("/cart/", "/courses/", 301), ("/term_conditions/", "/p/terms/", 301),
    ("/category/content-production/", "/blog/?cat=content-production", 301),
    ("/category/artificial-intelligence/", "/blog/?cat=artificial-intelligence", 301),
    ("/category/carpet-industry/", "/blog/?cat=carpet-industry", 301),
    ("/category/office-automation/", "/blog/?cat=office-automation", 301),
    ("/portfolio/", "", 410), ("/home-base/", "", 410), ("/home-base-rtl/", "", 410),
    ("/wishlist/", "", 410), ("/compare/", "", 410),
]

PAGES = [
    ("درباره ما", "about", "<p>توسعه هوشمند فرش ایرانیان از سال ۱۳۹۶ در کاشان، نرم‌افزار اختصاصی برای کارخانه‌های ریسندگی، بافندگی و بازرگانی فرش می‌سازد. تیم ما ترکیبی از برنامه‌نویس‌ها و کسانی است که سال‌ها در خود کارخانه کار کرده‌اند.</p><p>این متن را از پنل مدیریت ← صفحات ویرایش کنید.</p>"),
    ("قوانین و شرایط", "terms", "<h2>شرایط استفاده از دوره‌ها</h2><p>دسترسی به دوره‌های خریداری‌شده دائمی است. محتوای دوره‌ها برای استفاده‌ی شخصی است و انتشار مجدد آن مجاز نیست.</p><h2>بازگشت وجه</h2><p>تا ۷ روز پس از خرید، در صورت مشاهده‌ی کمتر از ۲۰٪ دوره، وجه قابل بازگشت است.</p>"),
    ("حریم خصوصی", "privacy", "<p>شماره موبایل شما فقط برای ورود و اطلاع‌رسانی دوره‌ها استفاده می‌شود و در اختیار هیچ شخص ثالثی قرار نمی‌گیرد. آمار بازدید به‌صورت ناشناس و بدون ذخیره‌ی IP جمع‌آوری می‌شود.</p>"),
]


class Command(BaseCommand):
    help = "داده‌ی اولیه‌ی سایت"

    def handle(self, *args, **opts):
        SiteSettings.load()
        self.stdout.write("✓ تنظیمات سایت")

        if not NavLink.objects.exists():
            for i, (t, u) in enumerate(NAV):
                NavLink.objects.create(title=t, url=u, order=i)
            self.stdout.write("✓ منو")

        if not HomeSection.objects.exists():
            for i, (k, kick, t, sub) in enumerate(SECTIONS):
                HomeSection.objects.create(key=k, kicker=kick, title=t, subtitle=sub, order=i * 10,
                                           items_limit=SECTION_LIMITS.get(k, 8))
            self.stdout.write("✓ بخش‌های صفحه اصلی")

        if not TimelineEvent.objects.exists():
            for i, (era, t, txt, c) in enumerate(TIMELINE):
                TimelineEvent.objects.create(era=era, title=t, text=txt, color=c, order=i)
            self.stdout.write("✓ خط زمان کاشان")

        for t, s, b in PAGES:
            Page.objects.get_or_create(slug=s, defaults={"title": t, "body": b})
        self.stdout.write("✓ صفحات")

        from django.core.management import call_command
        call_command("seed_products", stdout=self.stdout)

        n = 0
        for old, new, code in REDIRECTS:
            _, created = Redirect.objects.update_or_create(old_path=old, defaults={"new_path": new, "status_code": code})
            n += created
        self.stdout.write(f"✓ {n} ریدایرکت جدید")
        self.stdout.write(self.style.SUCCESS("تمام. حالا: python manage.py seed_geo  و  python manage.py seed_courses"))

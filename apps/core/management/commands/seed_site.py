"""
داده‌ی اولیه‌ی سایت: تنظیمات، منو، بخش‌های صفحه اصلی، خط زمان کاشان، صفحات، محصولات،
ریدایرکت آدرس‌های قدیمی وردپرس. اجرا: python manage.py seed_site
"""
from django.core.management.base import BaseCommand

from apps.core.models import HomeSection, NavLink, Page, SiteSettings, TimelineEvent
from apps.products.models import Product, ProductFeature
from apps.seo.models import Redirect

NAV = [("محصولات", "/products/"), ("آکادمی", "/courses/"), ("از سیلک تا سرور", "/#kashan"),
       ("مقالات", "/blog/"), ("شروع پروژه", "/start-project/")]

SECTIONS = [
    ("products", "محصولات", "هشت نرم‌افزار، یک زنجیره", "هر کدام از دل یک توقف واقعی در خط تولید یا یک سفارش گم‌شده در بازار بیرون آمده است."),
    ("timeline", "از سیلک تا سرور", "کاشان، شهر مهندسان", "این فهرست تبلیغات نیست؛ سابقه‌ی فنی یک شهر است که ما نفر بعدی‌اش هستیم."),
    ("academy", "آکادمی", "آنچه در کارگاه یاد گرفتیم، درس می‌دهیم", "هیچ دوره‌ای اینجا نیست که از دل یک پروژه‌ی واقعی بیرون نیامده باشد."),
    ("blog", "مقالات", "از دفترچه‌ی فنی ما", ""),
    ("cta", "تماس", "مسئله‌تان را بگویید، معماری‌اش را می‌نویسیم", "جلسه‌ی اول رایگان است. اگر راهکار آماده‌ای داشته باشیم همان را پیشنهاد می‌دهیم؛ اگر نه، از صفر می‌سازیم."),
]

TIMELINE = [
    ("۵۵۰۰ پیش از میلاد", "تپه سیلک", "کهن‌ترین سکونتگاه شناخته‌شده‌ی فلات ایران. سفال نقش‌دار، خشت، و نخستین سازه‌ی پلکانی — هفت هزار سال پیش، همین‌جا.", "#D2623E"),
    ("هزاره‌ی اول پیش از میلاد", "قنات", "انتقال آب زیرزمینی با شیب کنترل‌شده در ده‌ها کیلومتر — یک سامانه‌ی توزیع، قرن‌ها پیش از لوله‌کشی.", "#F2A83B"),
    ("۹۹۴ خورشیدی", "باغ فین", "فواره‌های بدون پمپ، فقط با اختلاف ارتفاع. مهندسی هیدرولیک که چهارصد سال است کار می‌کند.", "#16A9C7"),
    ("دوره‌ی قاجار", "بادگیر و خانه‌های تاریخی", "خنک‌سازی غیرفعال در دل کویر — بروجردی‌ها و طباطبایی‌ها، پیش از آنکه کولر اختراع شود.", "#F05C7E"),
    ("۱۳۹۶ تا امروز", "توسعه هوشمند فرش ایرانیان", "همان شهر، همان کار: ساختن سامانه‌ای که بدون سر و صدا، سال‌ها درست کار کند — این بار با کد و هوش مصنوعی.", "#1E9E7B"),
]

PRODUCTS = [
    ("دوک", "doox", "پایش لحظه‌ای خط ریسندگی", "MES · IoT", "#1E9E7B", "memory",
     "ثبت خودکار توقفات، محاسبه راندمان و گزارش ضایعات به تفکیک شیفت و ماشین.",
     ["اتصال مستقیم به PLC و سنسورها", "داشبورد زنده‌ی راندمان (OEE)", "ثبت خودکار علت توقف", "گزارش ضایعات هر شیفت"]),
    ("دیاکو", "diaco", "برنامه‌ریزی تولید و تخصیص سفارش به ماشین", "ERP · PLANNING", "#16A9C7", "account_tree",
     "تخصیص سفارش به ماشین با احتساب موجودی نخ و زمان تعویض نقشه.",
     ["برنامه‌ریزی روزانه و هفتگی", "کنترل موجودی نخ و مواد", "پیگیری سفارش تا تحویل", "گزارش مدیریتی"]),
    ("رادمان", "radman", "نگهداری و تعمیرات", "CMMS", "#D2623E", "build",
     "تعریف دارایی، برنامه‌ی PM، درخواست کار، انبار قطعات و تاریخچه‌ی خرابی هر ماشین.",
     ["شناسنامه‌ی هر ماشین", "برنامه‌ی نگهداری پیشگیرانه", "درخواست کار و کارتابل تعمیرکار", "انبار قطعات یدکی"]),
    ("چله", "cheleh", "مدیریت تار و چله‌کشی", "WARP CALC", "#F2A83B", "straighten",
     "محاسبه‌ی مصرف نخ بر پایه‌ی شانه و تراکم، پیش از شروع بافت.",
     ["محاسبه‌ی دقیق مصرف نخ", "برنامه‌ی چله‌کشی", "ثبت مشخصات هر چله", "هشدار کمبود نخ"]),
    ("فرش‌پلاس", "farshplus", "بازار دیجیتال فرش", "MARKETPLACE", "#F05C7E", "storefront",
     "کاتالوگ، مدیریت نمایندگان، سفارش‌گیری و تسویه‌ی خودکار.",
     ["کاتالوگ آنلاین با فیلتر", "پنل نمایندگان و عاملان فروش", "سفارش‌گیری موبایلی", "تسویه و صورت‌حساب خودکار"]),
    ("نوبان", "noban", "اتوماسیون اداری برای شرکت‌های تولیدی", "AUTOMATION", "#1E9E7B", "mark_email_read",
     "دبیرخانه، گردش مکاتبات، کارتابل و امضای دیجیتال.",
     ["دبیرخانه و بایگانی", "کارتابل و گردش کار", "امضای دیجیتال", "جستجوی تمام‌متن"]),
    ("زال", "zaal", "تبدیل گفتار فارسی به متن", "ASR · AI", "#16A9C7", "mic",
     "مستندسازی جلسات فنی و تماس‌های فروش با دقت بالا.",
     ["تشخیص گفتار فارسی", "زمان‌بندی خودکار متن", "خروجی Word و PDF", "API برای اتصال به سامانه‌ها"]),
    ("دانایار", "danayar", "تحلیل داده‌ی تولید با هوش مصنوعی", "ML · VISION", "#F2A83B", "insights",
     "پیش‌بینی تقاضا و تشخیص الگوی عیوب بافت از روی تصویر.",
     ["پیش‌بینی تقاضا", "تشخیص عیب بافت از تصویر", "داشبورد تحلیلی", "هشدار هوشمند"]),
]

# آدرس‌های قدیمی وردپرس → جدید
REDIRECTS = [
    ("/noban/", "/products/noban/", 301), ("/farsh-plus/", "/products/farshplus/", 301),
    ("/roham/", "/products/", 301), ("/cheleh/", "/products/cheleh/", 301),
    ("/danayar/", "/products/danayar/", 301), ("/dook/", "/products/doox/", 301),
    ("/radman/", "/products/radman/", 301), ("/diaco/", "/products/diaco/", 301),
    ("/courses/", "/courses/", 301), ("/دوره-های-آموزشی/", "/courses/", 301),
    ("/instructors/", "/courses/", 301), ("/instructor/", "/courses/", 301),
    ("/become_a_teacher/", "/start-project/", 301), ("/lp-profile/", "/accounts/dashboard/", 301),
    ("/my-account/", "/accounts/dashboard/", 301), ("/lp-checkout/", "/courses/", 301),
    ("/cart/", "/courses/", 301), ("/term_conditions/", "/p/terms/", 301),
    ("/category/content-production/", "/blog/?cat=content-production", 301),
    ("/category/artificial-intelligence/", "/blog/?cat=artificial-intelligence", 301),
    ("/category/carpet-industry/", "/blog/?cat=carpet-industry", 301),
    ("/category/office-automation/", "/blog/?cat=office-automation", 301),
    ("/tarahi-site-farsh-kashan/", "/blog/tarahi-site-farsh-kashan/", 301),
    ("/narmafzar-mes-nassaji-risandegi/", "/blog/narmafzar-mes-nassaji-risandegi/", 301),
    ("/tabdil-sot-be-matn-farsi-zaal/", "/blog/tabdil-seda-be-matn-zaal/", 301),
    ("/narmafzar-tamirat-negahdari-kashan/", "/blog/narmafzar-tamirat-negahdari-kashan/", 301),
    ("/how-artificial-intelligence-is-transforming-the-carpet-industry/", "/blog/ai-carpet-industry/", 301),
    ("/۷-کاربرد-هوش-مصنوعی-در-صنعت-فرش-ایران/", "/blog/7-karbord-hoosh-masnooei-farsh/", 301),
    ("/فرش-پلاس؛-اکوسیستم-دیجیتال-نوآورانه-ص/", "/blog/farsh-plus-digital-ecosystem/", 301),
    ("/نرم‌افزار-اختصاصی-برای-کسب-و-کار/", "/blog/narmafzar-ekhtesasi-kasb-o-kar/", 301),
    ("/5-مزیت-رقابت-برندهای-فرش/", "/blog/5-mazit-raghabati-brand-farsh/", 301),
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
            for i, (k, kick, t, s) in enumerate(SECTIONS):
                HomeSection.objects.create(key=k, kicker=kick, title=t, subtitle=s, order=i)
            self.stdout.write("✓ بخش‌های صفحه اصلی")

        if not TimelineEvent.objects.exists():
            for i, (era, t, txt, c) in enumerate(TIMELINE):
                TimelineEvent.objects.create(era=era, title=t, text=txt, color=c, order=i)
            self.stdout.write("✓ خط زمان کاشان")

        for t, s, b in PAGES:
            Page.objects.get_or_create(slug=s, defaults={"title": t, "body": b})
        self.stdout.write("✓ صفحات")

        for i, (name, latin, tag, cat, color, icon, summary, feats) in enumerate(PRODUCTS):
            p, created = Product.objects.get_or_create(slug=latin, defaults={
                "name": name, "latin_name": latin, "tagline": tag, "category_label": cat,
                "color": color, "icon": icon, "summary": summary, "order": i,
                "description": f"<p>{summary}</p><p>شرح کامل محصول را از پنل مدیریت ← محصولات ویرایش کنید؛ می‌توانید تصویر، آموزش و کاتالوگ اضافه کنید.</p>",
            })
            if created:
                for j, f in enumerate(feats):
                    ProductFeature.objects.create(product=p, title=f, order=j)
        self.stdout.write("✓ محصولات")

        n = 0
        for old, new, code in REDIRECTS:
            _, created = Redirect.objects.get_or_create(old_path=old, defaults={"new_path": new, "status_code": code})
            n += created
        self.stdout.write(f"✓ {n} ریدایرکت جدید")
        self.stdout.write(self.style.SUCCESS("تمام. حالا: python manage.py seed_geo  و  python manage.py seed_courses"))

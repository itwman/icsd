# -*- coding: utf-8 -*-
# بانک ۳۴ سؤالی آزمون دوره‌ی جامع Word — هر نوبت ۲۰ سؤال تصادفی

QUIZ = {
    "course_slug": "word",
    "title": "آزمون پایانی آموزش جامع Microsoft Word",
    "pass_percent": 70,
    "time_limit_minutes": 30,
    "questions_per_attempt": 20,
    "questions": [
        # ── فصل ۱
        {
            "text": "تفاوت «راست‌چین کردن» (Align Right) با «راست‌به‌چپ کردن» (Right-to-Left) یک پاراگراف فارسی چیست؟",
            "explanation": "Align Right فقط تراز را عوض می‌کند؛ نقطه، پرانتز و ارقام در پاراگراف چپ‌به‌راست جای غلط می‌نشینند. جهت پاراگراف باید Right-to-Left باشد.",
            "choices": [
                {"text": "هیچ تفاوتی ندارند", "correct": False},
                {"text": "راست‌چین فقط تراز است؛ راست‌به‌چپ جهت منطقی متن را عوض می‌کند و علائم درست می‌نشینند", "correct": True},
                {"text": "راست‌به‌چپ فقط برای جدول کار می‌کند", "correct": False},
                {"text": "راست‌چین فونت را هم فارسی می‌کند", "correct": False},
            ],
        },
        {
            "text": "گزینه‌ی Numeral = Context در Options ← Advanced چه کاری انجام می‌دهد؟",
            "explanation": "Context ارقام را بر اساس متن اطراف نمایش می‌دهد؛ فقط نمایش را عوض می‌کند و کاراکتر ذخیره‌شده تغییر نمی‌کند.",
            "choices": [
                {"text": "همه‌ی ارقام را به‌طور دائمی به فارسی تبدیل می‌کند", "correct": False},
                {"text": "ارقام را بر اساس زبان متن اطراف نمایش می‌دهد، بدون تغییر کاراکتر ذخیره‌شده", "correct": True},
                {"text": "فقط ارقام داخل جدول را فارسی می‌کند", "correct": False},
                {"text": "ارقام را همیشه لاتین نشان می‌دهد", "correct": False},
            ],
        },
        {
            "text": "در پنجره‌ی Font، فونت متن فارسی را در کدام بخش باید انتخاب کرد؟",
            "explanation": "بخش Complex scripts مخصوص خط‌های فارسی/عربی است؛ بخش Latin text فقط حروف لاتین را تغییر می‌دهد.",
            "choices": [
                {"text": "Latin text", "correct": False},
                {"text": "Text Effects", "correct": False},
                {"text": "Complex scripts", "correct": True},
                {"text": "Character Spacing", "correct": False},
            ],
        },
        {
            "text": "کدام کلید نیم‌فاصله (ZWNJ) درج می‌کند؟",
            "explanation": "در Word میانبر Ctrl+Shift+2 و در کیبورد استاندارد فارسی Shift+Space نیم‌فاصله می‌زند.",
            "choices": [
                {"text": "Ctrl+Shift+Space", "correct": False},
                {"text": "Ctrl+Shift+2 یا Shift+Space (کیبورد استاندارد)", "correct": True},
                {"text": "Ctrl+-", "correct": False},
                {"text": "Alt+Space", "correct": False},
            ],
        },
        {
            "text": "برای این‌که «۲۵» و «کیلوگرم» هیچ‌وقت سر خط از هم جدا نشوند چه چیزی بین آن‌ها می‌گذاریم؟",
            "explanation": "فاصله‌ی نشکن با Ctrl+Shift+Space دو کلمه را در یک خط نگه می‌دارد.",
            "choices": [
                {"text": "دو فاصله‌ی معمولی", "correct": False},
                {"text": "Tab", "correct": False},
                {"text": "شکست خط (Shift+Enter)", "correct": False},
                {"text": "فاصله‌ی نشکن (Ctrl+Shift+Space)", "correct": True},
            ],
        },
        {
            "text": "Spike در Word چیست؟",
            "explanation": "Spike کلیپ‌بورد انباشتی است: با Ctrl+F3 متن‌ها بریده و جمع می‌شوند و با Ctrl+Shift+F3 همه یک‌جا چسبانده می‌شوند.",
            "choices": [
                {"text": "ابزاری برای کشیدن خطوط عمودی", "correct": False},
                {"text": "کلیپ‌بورد انباشتی که با Ctrl+F3 جمع و با Ctrl+Shift+F3 یک‌جا درج می‌کند", "correct": True},
                {"text": "نام دیگر Format Painter", "correct": False},
                {"text": "قابلیت جست‌وجوی سریع در Navigation Pane", "correct": False},
            ],
        },
        {
            "text": "چرا برای ارسال سند فارسی به دیگران توصیه می‌شود Embed fonts in the file فعال باشد یا PDF فرستاده شود؟",
            "explanation": "اگر فونت فارسی روی سیستم گیرنده نباشد، Word فونت دیگری جایگزین می‌کند و صفحه‌بندی به هم می‌ریزد.",
            "choices": [
                {"text": "چون حجم فایل کمتر می‌شود", "correct": False},
                {"text": "چون بدون فونت جاسازی‌شده، گیرنده فونت جایگزین می‌بیند و صفحه‌بندی به هم می‌ریزد", "correct": True},
                {"text": "چون Word بدون آن فایل را باز نمی‌کند", "correct": False},
                {"text": "چون Track Changes به آن نیاز دارد", "correct": False},
            ],
        },
        {
            "text": "Shift+F5 در Word چه می‌کند؟",
            "explanation": "Shift+F5 مکان‌نما را به آخرین جاهای ویرایش‌شده برمی‌گرداند، حتی بعد از باز کردن دوباره‌ی فایل.",
            "choices": [
                {"text": "سند را ذخیره می‌کند", "correct": False},
                {"text": "به آخرین جای ویرایش‌شده برمی‌گردد", "correct": True},
                {"text": "غلط‌یاب را اجرا می‌کند", "correct": False},
                {"text": "پنجره را دو نیم می‌کند", "correct": False},
            ],
        },
        # ── فصل ۲
        {
            "text": "مهم‌ترین مزیت استفاده از Heading Styles نسبت به بولد کردن دستی تیترها چیست؟",
            "explanation": "Heading به Word می‌گوید این متن تیتر است؛ فهرست مطالب، Navigation Pane، ارجاع، شماره‌گذاری فصل و بوک‌مارک PDF همه به آن وابسته‌اند.",
            "choices": [
                {"text": "فقط زیباتر است", "correct": False},
                {"text": "فهرست خودکار، Navigation Pane، ارجاع و شماره‌گذاری فصل را ممکن می‌کند و تغییر یک‌جا انجام می‌شود", "correct": True},
                {"text": "حجم فایل را کم می‌کند", "correct": False},
                {"text": "تیتر را از غلط‌یابی مستثنا می‌کند", "correct": False},
            ],
        },
        {
            "text": "میانبر Ctrl+Space و Ctrl+Q به ترتیب چه می‌کنند؟",
            "explanation": "Ctrl+Space قالب‌بندی کاراکتر و Ctrl+Q قالب‌بندی پاراگراف را پاک می‌کند و متن به تعریف Style برمی‌گردد.",
            "choices": [
                {"text": "پاک کردن قالب‌بندی مستقیم کاراکتر / پاک کردن قالب‌بندی مستقیم پاراگراف", "correct": True},
                {"text": "درج فاصله‌ی نشکن / خروج از Word", "correct": False},
                {"text": "انتخاب کلمه / انتخاب پاراگراف", "correct": False},
                {"text": "باز کردن پنل Styles / باز کردن Quick Parts", "correct": False},
            ],
        },
        {
            "text": "چرا نباید گزینه‌ی Automatically update در Modify Style فعال باشد؟",
            "explanation": "با این گزینه هر قالب‌بندی دستی روی یک پاراگراف، تعریف Style را عوض می‌کند و همه‌ی پاراگراف‌های هم‌Style تغییر می‌کنند.",
            "choices": [
                {"text": "چون Word کند می‌شود", "correct": False},
                {"text": "چون یک بولد تصادفی روی یک پاراگراف، همه‌ی پاراگراف‌های آن Style را عوض می‌کند", "correct": True},
                {"text": "چون فقط در فرمت .doc کار می‌کند", "correct": False},
                {"text": "چون فهرست مطالب را حذف می‌کند", "correct": False},
            ],
        },
        {
            "text": "برای این‌که تیتر فصل هیچ‌وقت تنها در پایین صفحه نماند، کدام تنظیم پاراگراف لازم است؟",
            "explanation": "Keep with next پاراگراف را با پاراگراف بعدی در یک صفحه نگه می‌دارد؛ Heading‌ها به‌طور پیش‌فرض آن را دارند.",
            "choices": [
                {"text": "Widow/Orphan control", "correct": False},
                {"text": "Page break before", "correct": False},
                {"text": "Keep with next", "correct": True},
                {"text": "Suppress line numbers", "correct": False},
            ],
        },
        {
            "text": "برای شماره‌گذاری خودکار «۱-۲-۳» تیترها که با جابه‌جایی فصل‌ها به‌روز شود چه باید کرد؟",
            "explanation": "Define New Multilevel List و پیوند هر سطح به Heading مربوط (Link level to style) شماره‌ها را خودکار و پویا می‌کند.",
            "choices": [
                {"text": "شماره‌ها را دستی ابتدای هر تیتر تایپ کنیم", "correct": False},
                {"text": "از Numbering ساده روی هر تیتر استفاده کنیم", "correct": False},
                {"text": "Multilevel List تعریف کنیم و هر سطح را به Heading 1/2/3 پیوند دهیم", "correct": True},
                {"text": "از فیلد PAGE استفاده کنیم", "correct": False},
            ],
        },
        # ── فصل ۳
        {
            "text": "برای این‌که فقط یک صفحه‌ی وسط سند Landscape باشد، بدون Section Break ممکن است؟",
            "explanation": "جهت کاغذ ویژگی Section است؛ با Apply to: Selected text، Word خودش قبل و بعد Section break می‌گذارد.",
            "choices": [
                {"text": "بله، با چرخاندن متن", "correct": False},
                {"text": "خیر؛ جهت کاغذ ویژگی Section است و به Section جداگانه نیاز دارد (Word با Apply to Selected text خودش می‌سازد)", "correct": True},
                {"text": "بله، با Page Break", "correct": False},
                {"text": "بله، با Column Break", "correct": False},
            ],
        },
        {
            "text": "شماره‌ی صفحه‌ی صفحات آغازین هم همراه با فصل اول عوض شد. علت رایج چیست؟",
            "explanation": "وقتی Link to Previous روشن است، سربرگ/پاورقی Section‌ها به هم وصل‌اند و تغییر یکی، بقیه را هم عوض می‌کند.",
            "choices": [
                {"text": "Link to Previous در پاورقی Section جدید روشن مانده", "correct": True},
                {"text": "فونت شماره‌ی صفحه فارسی نیست", "correct": False},
                {"text": "Track Changes روشن است", "correct": False},
                {"text": "فهرست مطالب به‌روز نشده", "correct": False},
            ],
        },
        {
            "text": "فیلد StyleRef با Style name = Heading 1 در سربرگ چه چیزی نشان می‌دهد؟",
            "explanation": "StyleRef متن آخرین پاراگراف با آن Style قبل از صفحه‌ی جاری را نمایش می‌دهد؛ یعنی عنوان فصل جاری، بدون نیاز به Section جداگانه.",
            "choices": [
                {"text": "شماره‌ی صفحه‌ی اول فصل", "correct": False},
                {"text": "عنوان فصل جاری (آخرین Heading 1 قبل از این صفحه)", "correct": True},
                {"text": "نام فایل", "correct": False},
                {"text": "تعداد فصل‌ها", "correct": False},
            ],
        },
        {
            "text": "برای درج سریع متن‌های تکراری (مثل امضای نامه) با تایپ نام و زدن F3 از کدام امکان استفاده می‌شود؟",
            "explanation": "AutoText (بخشی از Quick Parts / Building Blocks) با تایپ نام و F3 درج می‌شود.",
            "choices": [
                {"text": "Mail Merge", "correct": False},
                {"text": "Bookmark", "correct": False},
                {"text": "AutoText در Quick Parts", "correct": True},
                {"text": "Watermark", "correct": False},
            ],
        },
        {
            "text": "برای ساخت قالب شرکتی که هر بار سند جدیدی از آن ساخته شود و خودش دست‌نخورده بماند، فایل را با کدام فرمت ذخیره می‌کنیم؟",
            "explanation": "Word Template (.dotx) از File ← New ← Personal سند جدید می‌سازد؛ .dotm اگر ماکرو دارد.",
            "choices": [
                {"text": ".docx", "correct": False},
                {"text": ".dotx", "correct": True},
                {"text": ".pdf", "correct": False},
                {"text": ".rtf", "correct": False},
            ],
        },
        # ── فصل ۴
        {
            "text": "برای این‌که عنوان ستون‌های یک جدول چندصفحه‌ای در بالای هر صفحه تکرار شود چه می‌کنیم؟",
            "explanation": "ردیف اول را انتخاب و در تب Layout جدول Repeat Header Rows را فعال می‌کنیم.",
            "choices": [
                {"text": "ردیف اول را در هر صفحه کپی می‌کنیم", "correct": False},
                {"text": "Repeat Header Rows در تب Layout جدول", "correct": True},
                {"text": "جدول را به دو جدول تقسیم می‌کنیم", "correct": False},
                {"text": "از Header صفحه استفاده می‌کنیم", "correct": False},
            ],
        },
        {
            "text": "چرا در اسناد رسمی توصیه می‌شود تصاویر In Line with Text باشند؟",
            "explanation": "تصویر In Line مثل یک کاراکتر با متن حرکت می‌کند و «نمی‌پرد»؛ تصویر شناور به لنگر پاراگراف وابسته است.",
            "choices": [
                {"text": "چون کیفیت تصویر بهتر می‌شود", "correct": False},
                {"text": "چون با متن حرکت می‌کند و مثل تصویر شناور با جابه‌جایی لنگر نمی‌پرد", "correct": True},
                {"text": "چون فقط این حالت در PDF چاپ می‌شود", "correct": False},
                {"text": "چون تصویر شناور زیرنویس نمی‌گیرد", "correct": False},
            ],
        },
        {
            "text": "برای این‌که زیرنویس شکل به شکل «شکل ۲-۳» با شماره‌ی فصل باشد، کدام شرط لازم است؟",
            "explanation": "در Insert Caption ← Numbering ← Include chapter number؛ اما فقط وقتی کار می‌کند که Heading 1 با Multilevel List شماره‌دار باشد.",
            "choices": [
                {"text": "تصویر باید شناور باشد", "correct": False},
                {"text": "Heading 1 باید با Multilevel List پیوندی شماره‌گذاری شده باشد و Include chapter number فعال شود", "correct": True},
                {"text": "باید از Text Box استفاده شود", "correct": False},
                {"text": "باید Track Changes خاموش باشد", "correct": False},
            ],
        },
        {
            "text": "کدام میانبر همه‌ی فیلدهای بدنه‌ی سند را به‌روز می‌کند؟",
            "explanation": "Ctrl+A برای انتخاب همه و سپس F9 فیلدها را به‌روز می‌کند (سربرگ‌ها جداگانه).",
            "choices": [
                {"text": "Ctrl+A سپس F9", "correct": True},
                {"text": "Ctrl+F9", "correct": False},
                {"text": "Alt+F9", "correct": False},
                {"text": "Ctrl+Shift+F9", "correct": False},
            ],
        },
        # ── فصل ۵
        {
            "text": "برای تغییر ظاهر خطوط فهرست مطالب به‌طوری که با Update از بین نرود چه می‌کنیم؟",
            "explanation": "Style‌های TOC 1 تا TOC 9 ظاهر فهرست را کنترل می‌کنند؛ قالب‌بندی دستی داخل فهرست با Update entire table پاک می‌شود.",
            "choices": [
                {"text": "خطوط فهرست را دستی قالب‌بندی می‌کنیم", "correct": False},
                {"text": "Style‌های TOC 1، TOC 2 و … را Modify می‌کنیم", "correct": True},
                {"text": "فهرست را به تصویر تبدیل می‌کنیم", "correct": False},
                {"text": "فهرست را در Text Box می‌گذاریم", "correct": False},
            ],
        },
        {
            "text": "خط جداکننده‌ی بالای پاورقی‌ها فقط در کدام نما قابل ویرایش است؟",
            "explanation": "در نمای Draft با References ← Show Notes می‌توان Footnote Separator را ویرایش کرد.",
            "choices": [
                {"text": "Print Layout", "correct": False},
                {"text": "Read Mode", "correct": False},
                {"text": "Draft", "correct": True},
                {"text": "Web Layout", "correct": False},
            ],
        },
        {
            "text": "میانبر Ctrl+F9 در Word چه می‌کند؟",
            "explanation": "Ctrl+F9 یک جفت آکولاد فیلد خالی درج می‌کند تا کد فیلد را دستی بنویسید؛ تایپ آکولاد معمولی کار نمی‌کند.",
            "choices": [
                {"text": "همه‌ی فیلدها را به‌روز می‌کند", "correct": False},
                {"text": "یک فیلد خالی (جفت آکولاد ویژه) برای نوشتن کد درج می‌کند", "correct": True},
                {"text": "کد فیلدها را نمایش می‌دهد", "correct": False},
                {"text": "فیلد را به متن ثابت تبدیل می‌کند", "correct": False},
            ],
        },
        {
            "text": "در Source Manager تفاوت Master List و Current List چیست؟",
            "explanation": "Master List همه‌ی منابعی است که در هر سندی وارد کرده‌اید (فایل Sources.xml)؛ Current List منابع همین سند.",
            "choices": [
                {"text": "Master منابع فارسی، Current منابع انگلیسی", "correct": False},
                {"text": "Master همه‌ی منابع ذخیره‌شده‌ی شما در همه‌ی اسناد؛ Current منابع سند فعلی", "correct": True},
                {"text": "Master منابع چاپ‌شده، Current منابع وب", "correct": False},
                {"text": "تفاوتی ندارند", "correct": False},
            ],
        },
        # ── فصل ۶
        {
            "text": "نمای No Markup در Track Changes چه چیزی نشان می‌دهد و چه خطری دارد؟",
            "explanation": "No Markup نتیجه‌ی نهایی را نشان می‌دهد اما تغییرات هنوز در فایل هستند؛ گیرنده می‌تواند همه‌ی حذف‌شده‌ها را ببیند.",
            "choices": [
                {"text": "سند اصلی قبل از تغییرات را؛ خطری ندارد", "correct": False},
                {"text": "نتیجه‌ی نهایی را، اما تغییرات هنوز در فایل هستند و دیگران می‌بینند", "correct": True},
                {"text": "فقط نظرها را؛ تغییرات حذف می‌شوند", "correct": False},
                {"text": "تغییرات را می‌پذیرد و حذف می‌کند", "correct": False},
            ],
        },
        {
            "text": "دو نسخه از یک قرارداد دارید که همکار بدون Track Changes ویرایش کرده. با کدام ابزار تفاوت‌ها را می‌بینید؟",
            "explanation": "Review ← Compare دو سند را مقایسه و تفاوت‌ها را به شکل Track Changes در سند سوم نشان می‌دهد.",
            "choices": [
                {"text": "Review ← Compare", "correct": True},
                {"text": "Document Inspector", "correct": False},
                {"text": "Mail Merge", "correct": False},
                {"text": "Restrict Editing", "correct": False},
            ],
        },
        {
            "text": "پیش از ارسال سند مناقصه، کدام ابزار متادیتا، نظرها، متن پنهان و نام نویسنده را پیدا و حذف می‌کند؟",
            "explanation": "File ← Info ← Check for Issues ← Inspect Document (Document Inspector).",
            "choices": [
                {"text": "Accessibility Checker", "correct": False},
                {"text": "Compatibility Checker", "correct": False},
                {"text": "Document Inspector", "correct": True},
                {"text": "Mark as Final", "correct": False},
            ],
        },
        {
            "text": "در Mail Merge مبلغ از Excel به شکل 1250000 می‌آید. برای نمایش با جداکننده‌ی هزارگان چه می‌کنیم؟",
            "explanation": "به فیلد MERGEFIELD سوییچ قالب عدد اضافه می‌کنیم: `\\# \"#,##0\"` (با Alt+F9 کد فیلد را ویرایش کنید).",
            "choices": [
                {"text": "در Excel فرمت سلول را عوض می‌کنیم؛ Word خودکار می‌گیرد", "correct": False},
                {"text": "سوییچ قالب `\\# \"#,##0\"` را به فیلد MERGEFIELD اضافه می‌کنیم", "correct": True},
                {"text": "از Rules ← If…Then…Else استفاده می‌کنیم", "correct": False},
                {"text": "ممکن نیست؛ باید دستی تایپ شود", "correct": False},
            ],
        },
        # ── فصل ۷ و ۸
        {
            "text": "در Find & Replace با Use wildcards، الگوی `([0-9]{4})/([0-9]{2})/([0-9]{2})` با جایگزینی `\\3/\\2/\\1` چه می‌کند؟",
            "explanation": "گروه‌های پرانتزی با \\1 \\2 \\3 در Replace ارجاع داده می‌شوند؛ ترتیب اجزای تاریخ برعکس می‌شود (1405/06/25 → 25/06/1405).",
            "choices": [
                {"text": "تاریخ‌ها را حذف می‌کند", "correct": False},
                {"text": "ترتیب سال/ماه/روز را به روز/ماه/سال برمی‌گرداند", "correct": True},
                {"text": "ارقام را فارسی می‌کند", "correct": False},
                {"text": "خطا می‌دهد؛ wildcard گروه ندارد", "correct": False},
            ],
        },
        {
            "text": "برای تبدیل «ي» عربی به «ی» فارسی در کل سند با Find & Replace از کدام کدها استفاده می‌کنیم؟",
            "explanation": "کد ^u به‌همراه شماره‌ی یونیکد دهدهی: ^u1610 (ي) به ^u1740 (ی).",
            "choices": [
                {"text": "^p به ^l", "correct": False},
                {"text": "^u1610 به ^u1740", "correct": True},
                {"text": "^s به ^w", "correct": False},
                {"text": "^# به ^$", "correct": False},
            ],
        },
        {
            "text": "ماکروی ضبط‌شده در Normal.dotm را برای همکار می‌فرستید اما در فایل .docx نیست. چرا؟",
            "explanation": "ماکروی Normal.dotm فقط روی سیستم شماست؛ ماکروی داخل سند به فرمت .docm نیاز دارد و docx آن را دور می‌ریزد.",
            "choices": [
                {"text": "چون ماکرو در Normal.dotm ذخیره شده و docx ماکرو نگه نمی‌دارد؛ باید در سند و با فرمت .docm ذخیره شود", "correct": True},
                {"text": "چون ماکروها فقط با PDF منتقل می‌شوند", "correct": False},
                {"text": "چون همکار Track Changes روشن نکرده", "correct": False},
                {"text": "چون ماکرو باید در Building Blocks باشد", "correct": False},
            ],
        },
        {
            "text": "هنگام ذخیره به PDF، کدام گزینه باعث می‌شود پنل نشانک‌های PDF از تیترهای سند ساخته شود؟",
            "explanation": "در Options پنجره‌ی PDF، «Create bookmarks using: Headings» نشانک‌ها را از Heading‌ها می‌سازد.",
            "choices": [
                {"text": "PDF/A compliant", "correct": False},
                {"text": "Create bookmarks using: Headings", "correct": True},
                {"text": "Bitmap text when fonts may not be embedded", "correct": False},
                {"text": "Document properties", "correct": False},
            ],
        },
    ],
}

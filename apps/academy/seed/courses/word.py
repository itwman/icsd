# -*- coding: utf-8 -*-
# دوره‌ی جامع Microsoft Word — ۸ فصل، ۳۸ درس. متن‌ها r""" هستند تا بک‌اسلش‌های wildcard و فیلدها دست‌نخورده بمانند.

COURSE = {
    "slug": "word",
    "title": "آموزش جامع Microsoft Word",
    "category": "مهارت‌های اداری",
    "level": "intermediate",
    "summary": "از تنظیمات درست فارسی تا Styles، فیلدها، مرجع‌دهی، Track Changes، Mail Merge، ماکرو و ساخت قالب پایان‌نامه — با ده‌ها نکته‌ای که کمتر کسی می‌داند.",
    "description": (
        "<p>بیشتر ما سال‌هاست با Word کار می‌کنیم و هنوز از کمتر از ده درصد آن استفاده می‌کنیم: تیترها را دستی بولد "
        "می‌کنیم، فاصله‌ها را با Enter می‌سازیم، عکس‌ها «می‌پرند»، فهرست مطالب را با دست می‌نویسیم و شماره‌ی صفحه‌ها "
        "هیچ‌وقت درست درنمی‌آید. این دوره برای همین نوشته شده است.</p>"
        "<p>از صفر شروع می‌کنیم اما خیلی زود به لایه‌ای می‌رسیم که کاربران حرفه‌ای در آن کار می‌کنند: <strong>Styles</strong> "
        "به‌عنوان ستون فقرات سند، <strong>Section</strong>ها و سربرگ‌های هوشمند، <strong>فیلدها</strong> و ارجاع‌های خودکار، "
        "جدول و تصویر بدون دردسر، <strong>Track Changes</strong> و همکاری، <strong>Mail Merge</strong>، جست‌وجوی "
        "wildcard، AutoCorrect، ماکرو و در پایان ساخت یک قالب استاندارد گزارش/پایان‌نامه‌ی فارسی.</p>"
        "<p>هر درس با بخش «نکته‌هایی که کمتر کسی می‌داند» تمام می‌شود؛ ترفندهایی که سال‌ها وقت شما را ذخیره می‌کنند. "
        "پیش‌نیاز: هیچ. تمرکز روی Word 2019/2021/365 برای ویندوز است و تفاوت‌های نسخه‌ی وب و مک هرجا مهم باشد گفته می‌شود.</p>"
    ),
    "price": 0,
    "duration_minutes": 732,
    "tags": ["Word", "ورد", "مهارت‌های اداری", "مستندسازی", "پایان‌نامه", "Office"],
    "modules": [
        # ───────────────────────────── فصل ۱ ─────────────────────────────
        {
            "title": "فصل ۱: شروع درست — محیط Word و تنظیمات فارسی",
            "lessons": [
                {
                    "title": "نقشه‌ی Word: Ribbon، نماها و Navigation Pane",
                    "kind": "text",
                    "minutes": 18,
                    "is_preview": True,
                    "body": r"""<h2>جایی که همه‌چیز قرار دارد</h2>
<p>Word را می‌توان به سه لایه تقسیم کرد: <strong>Ribbon</strong> (نوار بالای صفحه با تب‌های Home، Insert، Design، Layout، References، Mailings، Review، View)، <strong>Backstage</strong> (منوی File برای ذخیره، چاپ، اشتراک و Options) و <strong>ناحیه‌ی سند</strong>. تب‌های «زمینه‌ای» مثل Table Design یا Picture Format فقط وقتی ظاهر می‌شوند که روی جدول یا تصویر کلیک کرده باشید؛ اگر ابزاری را پیدا نمی‌کنید اول ببینید چه چیزی انتخاب شده است.</p>
<p>در گوشه‌ی پایین راست هر گروه Ribbon یک فلش کوچک (Dialog Launcher) هست که پنجره‌ی کامل آن گروه را باز می‌کند — مثلاً فلش گروه Paragraph در تب Home همه‌ی تنظیمات پاراگراف را یک‌جا نشان می‌دهد. بسیاری از امکانات مهم فقط از همین پنجره‌ها در دسترس‌اند.</p>
<h3>نماهای سند (تب View)</h3>
<table><thead><tr><th>نما</th><th>کاربرد</th></tr></thead><tbody>
<tr><td>Print Layout</td><td>نمای پیش‌فرض؛ صفحه همان‌طور که چاپ می‌شود</td></tr>
<tr><td>Read Mode</td><td>خواندن بدون حواس‌پرتی؛ ویرایش غیرفعال است</td></tr>
<tr><td>Web Layout</td><td>بدون شکست صفحه؛ برای متن‌هایی که به وب می‌روند</td></tr>
<tr><td>Outline</td><td>ساختار تیترها؛ جابه‌جایی فصل‌ها با کشیدن</td></tr>
<tr><td>Draft</td><td>سریع و ساده؛ تنها جایی که جداکننده‌ی پاورقی و کدهای شکست را می‌توانید ویرایش کنید</td></tr>
</tbody></table>
<p><strong>Navigation Pane</strong> (Ctrl+F یا View ← Navigation Pane) در سمت صفحه باز می‌شود و سه تب دارد: Headings (فهرست زنده‌ی تیترها که با کشیدن جابه‌جا می‌شوند)، Pages (بندانگشتی صفحات) و Results (نتایج جست‌وجو). این پنل فقط وقتی مفید است که تیترها با Heading Styles نوشته شده باشند — موضوعی که فصل دوم را به آن اختصاص داده‌ایم.</p>
<p>نوار <strong>Quick Access Toolbar</strong> (بالای Ribbon یا زیر آن) جای دکمه‌هایی است که هر روز استفاده می‌کنید. روی هر دکمه‌ی Ribbon راست‌کلیک کنید و «Add to Quick Access Toolbar» را بزنید. اگر Alt را فشار دهید، روی هر دکمه یک حرف ظاهر می‌شود (KeyTips) و می‌توانید بدون ماوس هر فرمانی را اجرا کنید؛ دکمه‌های QAT با Alt+1، Alt+2 و… اجرا می‌شوند.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>کادر «Tell me what you want to do» (Alt+Q) هر فرمانی را با نامش پیدا و همان‌جا اجرا می‌کند؛ لازم نیست بدانید در کدام تب است.</li>
<li>Ctrl+F1 نوار Ribbon را جمع می‌کند و فضای بیشتری برای متن می‌دهد. دوبار کلیک روی نام یک تب هم همین کار را می‌کند.</li>
<li>در Outline و Navigation Pane با کشیدن یک تیتر، <em>همه‌ی متن زیر آن</em> جابه‌جا می‌شود — سریع‌ترین راه برای بازچینی فصل‌های یک گزارش.</li>
<li>View ← Split (یا Ctrl+Alt+S) سند را به دو نیمه‌ی مستقل تقسیم می‌کند تا هم‌زمان صفحه‌ی ۳ و صفحه‌ی ۴۰ را ببینید.</li>
<li>در نوار وضعیت پایین صفحه راست‌کلیک کنید: می‌توانید شمارنده‌ی کلمات، شماره‌ی Section، وضعیت Track Changes و Caps Lock را نمایش دهید.</li>
</ul>""",
                },
                {
                    "title": "تنظیمات حیاتی فارسی: زبان، جهت، ارقام و کیبورد استاندارد",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>پنج تنظیمی که باید یک بار برای همیشه انجام دهید</h2>
<p>بیشتر مشکلات «فارسی» در Word — ارقام انگلیسی وسط متن فارسی، پرانتزهای برعکس، «ی» عربی، فاصله‌های زشت — نتیجه‌ی تنظیم نشدن این چند گزینه است.</p>
<h3>۱. زبان ویرایش</h3>
<p>File ← Options ← Language. در بخش Office authoring languages، «Persian» را اضافه کنید. بدون این کار دکمه‌های راست‌به‌چپ، Kashida و گزینه‌های ارقام اصلاً در Ribbon ظاهر نمی‌شوند. زبان تصحیح املایی هر پاراگراف را هم Word از روی کیبورد فعال تشخیص می‌دهد؛ اگر اشتباه تشخیص داد، متن را انتخاب کنید و از Review ← Language ← Set Proofing Language زبان را فارسی کنید.</p>
<h3>۲. جهت پاراگراف</h3>
<p>در گروه Paragraph تب Home دو دکمه‌ی <strong>Left-to-Right</strong> و <strong>Right-to-Left</strong> هست (میانبر: Ctrl+Shift راست / Ctrl+Shift چپ). «راست‌چین کردن» (Align Right) با «راست‌به‌چپ کردن» فرق دارد: پاراگراف چپ‌به‌راستی که فقط راست‌چین شده، نقطه و پرانتز را سر جای غلط می‌گذارد و ارقام و کلمات لاتین را برعکس می‌چیند. همیشه جهت را درست کنید، نه تراز را.</p>
<h3>۳. ارقام فارسی</h3>
<p>File ← Options ← Advanced ← بخش Show document content ← <strong>Numeral</strong>. چهار حالت دارد:</p>
<table><thead><tr><th>گزینه</th><th>رفتار</th></tr></thead><tbody>
<tr><td>Arabic</td><td>همیشه ارقام لاتین (0123)</td></tr>
<tr><td>Hindi</td><td>همیشه ارقام فارسی/عربی (۰۱۲۳)</td></tr>
<tr><td>Context</td><td>بر اساس متن اطراف: داخل جمله‌ی فارسی، فارسی؛ داخل جمله‌ی لاتین، لاتین (پیشنهادی)</td></tr>
<tr><td>System</td><td>بر اساس تنظیمات ویندوز</td></tr>
</tbody></table>
<p>نکته‌ی مهم: این گزینه فقط <em>نمایش</em> را عوض می‌کند؛ رقم ذخیره‌شده همان کاراکتر تایپ‌شده است. اگر سند را به کسی بدهید که Numeral روی Arabic است، همه‌ی ارقام لاتین می‌شوند. برای اسناد رسمی (پایان‌نامه، قرارداد) بهتر است ارقام را واقعاً فارسی تایپ کنید (کیبورد استاندارد) یا در پایان با Find & Replace تبدیل کنید (فصل ۷).</p>
<h3>۴. کیبورد فارسی استاندارد (ISIRI 9147)</h3>
<p>کیبورد «Persian» قدیمی ویندوز، «ی» و «ک» را با کدهای عربی (ي و ك) تایپ می‌کند و نیم‌فاصله ندارد. کیبورد <strong>Persian (Standard)</strong> را از تنظیمات زبان ویندوز اضافه کنید. با آن:</p>
<ul>
<li>نیم‌فاصله: <strong>Shift+Space</strong> (در Word خود Word هم Ctrl+Shift+2 نیم‌فاصله می‌زند).</li>
<li>«ی» و «ک» فارسی درست تایپ می‌شوند و جست‌وجو و مرتب‌سازی به هم نمی‌ریزد.</li>
<li>گیومه‌ی فارسی «» با Shift+K و Shift+L؛ ویرگول فارسی با Shift+T؛ نقطه‌ویرگول با Shift+Y.</li>
</ul>
<h3>۵. فونت پیش‌فرض برای متن فارسی</h3>
<p>در پنجره‌ی Font (Ctrl+D) دو بخش هست: <strong>Latin text</strong> و <strong>Complex scripts</strong>. فونت فارسی را باید در بخش Complex scripts انتخاب کنید؛ وگرنه فقط حروف لاتین عوض می‌شوند و فارسی روی فونت پیش‌فرض (معمولاً Times New Roman یا Arial) می‌ماند. پس از انتخاب فونت (Vazirmatn، IRANSans، B Nazanin یا Sahel) دکمه‌ی <strong>Set As Default</strong> را بزنید و «All documents based on the Normal template» را انتخاب کنید تا هر سند جدیدی با همین فونت باز شود.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>می‌توانید برای متن فارسی فونت B Nazanin و برای متن لاتین همان سند Times New Roman داشته باشید؛ Word خودش هر کلمه را با فونت مناسب می‌چیند. این همان دو بخش پنجره‌ی Font است.</li>
<li>در Options ← Advanced، گزینه‌ی <strong>Use sequence checking</strong> اگر روشن باشد Word بعضی ترکیب‌های حروف را «نامعتبر» می‌داند و اجازه‌ی تایپ نمی‌دهد؛ برای فارسی خاموشش کنید.</li>
<li>Options ← Advanced ← <strong>Cursor movement: Logical</strong> باعث می‌شود فلش‌ها در متن دوزبانه به ترتیب کاراکترها حرکت کنند، نه به ترتیب بصری؛ برای ویرایش متن‌های ترکیبی بسیار راحت‌تر است.</li>
<li>در متن‌های فارسی به جای «فاصله + ویرگول» فقط «ویرگول + فاصله» بگذارید؛ Word با Kashida و Justify فاصله‌های اضافی را دوبرابر می‌کند.</li>
<li>اگر ارقام داخل جدول فارسی نمی‌شوند، جهت خود جدول (Table Properties ← Right-to-left) را هم بررسی کنید؛ Context numeral از جهت سلول تصمیم می‌گیرد.</li>
</ul>""",
                },
                {
                    "title": "کاراکترهای نامرئی: ¶، نیم‌فاصله، فاصله‌ی نشکن و انواع Enter",
                    "kind": "text",
                    "minutes": 18,
                    "is_preview": False,
                    "body": r"""<h2>چیزی که نمی‌بینید، سند را خراب می‌کند</h2>
<p>دکمه‌ی <strong>¶</strong> در تب Home (Ctrl+Shift+8) کاراکترهای «قالب‌بندی» را نشان می‌دهد: نقطه بین کلمات یعنی فاصله، فلش یعنی Tab، ¶ یعنی پایان پاراگراف، و ↵ یعنی شکست خط. کاربران حرفه‌ای این نمایش را دائم روشن دارند؛ چون بدون آن نمی‌توان فهمید چرا یک تیتر به صفحه‌ی بعد رفته یا چرا Justify فاصله‌های عجیب ساخته است.</p>
<table><thead><tr><th>کلید</th><th>کاراکتر</th><th>کِی استفاده کنیم</th></tr></thead><tbody>
<tr><td>Enter</td><td>پایان پاراگراف (¶)</td><td>فقط پایان پاراگراف واقعی. هرگز برای فاصله‌ی عمودی</td></tr>
<tr><td>Shift+Enter</td><td>شکست خط (↵)</td><td>رفتن به خط بعد در همان پاراگراف (آدرس، شعر)</td></tr>
<tr><td>Ctrl+Enter</td><td>شکست صفحه</td><td>شروع اجباری صفحه‌ی جدید</td></tr>
<tr><td>Ctrl+Shift+Space</td><td>فاصله‌ی نشکن</td><td>بین «۲۵» و «کیلوگرم» تا سر خط جدا نشوند</td></tr>
<tr><td>Ctrl+Shift+2 / Shift+Space</td><td>نیم‌فاصله (ZWNJ)</td><td>می‌رود، کتاب‌ها، بی‌نظیر</td></tr>
<tr><td>Ctrl+-</td><td>خط‌تیره‌ی اختیاری</td><td>اجازه‌ی شکستن کلمه‌ی لاتین بلند فقط در صورت نیاز</td></tr>
<tr><td>Ctrl+Shift+-</td><td>خط‌تیره‌ی نشکن</td><td>«COVID-19» سر خط جدا نشود</td></tr>
</tbody></table>
<h3>سه عادت اشتباه که باید ترک کنید</h3>
<p><strong>اول:</strong> چند بار Enter زدن برای رفتن به صفحه‌ی بعد. با یک ویرایش کوچک بالاتر، همه‌ی صفحه‌بندی به هم می‌ریزد. به‌جای آن Ctrl+Enter بزنید، یا بهتر: در Style تیتر فصل، «Page break before» را فعال کنید.</p>
<p><strong>دوم:</strong> Enter خالی برای فاصله بین پاراگراف‌ها. فاصله باید در تنظیمات پاراگراف (Spacing Before/After) باشد تا یکنواخت بماند و قابل تغییر یک‌جا باشد.</p>
<p><strong>سوم:</strong> فاصله یا Tab های پشت‌سرهم برای تراز کردن. برای تراز، Tab Stop تعریف کنید (کلیک روی خط‌کش) یا جدول بدون خط بکشید.</p>
<h3>نیم‌فاصله؛ کاراکتر شماره‌ی یک فارسی</h3>
<p>نیم‌فاصله (Zero-Width Non-Joiner) بین اجزای کلمه‌های مرکب می‌آید: «می‌شود» نه «می شود» و نه «میشود». Word آن را به‌عنوان یک کاراکتر واقعی ذخیره می‌کند، پس جست‌وجوی «می شود» آن را پیدا نمی‌کند. برای اصلاح کل سند از Find & Replace استفاده می‌کنیم (فصل ۷). وقتی ¶ روشن است نیم‌فاصله به شکل یک مستطیل کوچک نقطه‌چین دیده می‌شود.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>در پایان هر سلول جدول یک «¤» می‌بینید — نشانه‌ی پایان سلول. آخرین ¶ سند را نمی‌توانید حذف کنید؛ اگر یک صفحه‌ی خالی آخر سند دارید که پاک نمی‌شود، همان ¶ را انتخاب کنید و اندازه‌ی فونتش را روی ۱ بگذارید یا Hidden کنید.</li>
<li>Options ← Display به شما اجازه می‌دهد فقط بعضی کاراکترها (مثلاً فقط ¶ و Tab) همیشه نمایش داده شوند، بدون روشن کردن همه.</li>
<li>Ctrl+Shift+8 روی صفحه‌کلید عددی کار نمی‌کند؛ کلید 8 ردیف بالا را بزنید.</li>
<li>در Options ← Advanced ← Cut, copy and paste گزینه‌ی «Use smart cut and paste» وقتی کلمه‌ای را حذف می‌کنید فاصله‌ی اضافی را هم خودش پاک می‌کند.</li>
<li>متنی که از وب یا تلگرام کپی می‌کنید معمولاً پر از فاصله‌ی نشکن (U+00A0) و «ی» عربی است. با ¶ روشن، فاصله‌ی نشکن به شکل ° دیده می‌شود.</li>
</ul>""",
                },
                {
                    "title": "انتخاب، حرکت و کپی حرفه‌ای: Spike، Office Clipboard و انتخاب ستونی",
                    "kind": "text",
                    "minutes": 18,
                    "is_preview": False,
                    "body": r"""<h2>ماوس را کمتر بردارید</h2>
<p>سرعت کار با Word بیش از هر چیز به حرکت و انتخاب بستگی دارد. این جدول را چند روز کنار دست بگذارید؛ بعد از آن به عادت تبدیل می‌شود.</p>
<table><thead><tr><th>عمل</th><th>میانبر</th></tr></thead><tbody>
<tr><td>یک کلمه جلو/عقب</td><td>Ctrl + فلش چپ/راست</td></tr>
<tr><td>یک پاراگراف بالا/پایین</td><td>Ctrl + فلش بالا/پایین</td></tr>
<tr><td>ابتدا / انتهای سند</td><td>Ctrl+Home / Ctrl+End</td></tr>
<tr><td>برگشت به آخرین جای ویرایش‌شده</td><td><strong>Shift+F5</strong> (تا سه جای آخر؛ حتی بعد از باز کردن دوباره‌ی فایل)</td></tr>
<tr><td>انتخاب یک کلمه / یک جمله / یک پاراگراف</td><td>دوبار کلیک / Ctrl+کلیک / سه‌بار کلیک</td></tr>
<tr><td>حالت گسترش انتخاب</td><td>F8 (یک بار: روشن، دو بار: کلمه، سه بار: جمله، چهار بار: پاراگراف؛ Esc خاموش)</td></tr>
<tr><td>انتخاب ستونی (مستطیلی)</td><td>Alt + کشیدن ماوس یا Ctrl+Shift+F8</td></tr>
<tr><td>انتخاب همه‌ی متن‌های با قالب مشابه</td><td>راست‌کلیک ← Styles ← Select Text with Similar Formatting</td></tr>
<tr><td>تکرار آخرین عمل</td><td>F4 یا Ctrl+Y</td></tr>
<tr><td>جابه‌جایی پاراگراف بالا/پایین</td><td>Alt+Shift + فلش بالا/پایین (در جدول: جابه‌جایی ردیف)</td></tr>
</tbody></table>
<h3>Paste هوشمند</h3>
<p>بعد از Ctrl+V یک دکمه‌ی کوچک (Paste Options) ظاهر می‌شود با سه انتخاب: <strong>Keep Source Formatting</strong>، <strong>Merge Formatting</strong> و <strong>Keep Text Only</strong>. برای متنی که از وب یا از سند دیگری می‌آورید تقریباً همیشه «Keep Text Only» درست است؛ بعد Style سند خودتان را به آن می‌دهید. در Options ← Advanced ← Cut, copy and paste می‌توانید پیش‌فرض هر حالت (داخل همان سند، بین اسناد، از برنامه‌های دیگر) را تعیین کنید تا دیگر هر بار انتخاب نکنید. Ctrl+Alt+V پنجره‌ی Paste Special را باز می‌کند (Unformatted Text، Picture، لینک زنده به اکسل و…).</p>
<h3>Office Clipboard</h3>
<p>فلش کوچک گروه Clipboard در تب Home پنلی باز می‌کند که تا <strong>۲۴ مورد آخر</strong> کپی‌شده را نگه می‌دارد و می‌توانید هرکدام را جداگانه یا همه را یک‌جا بچسبانید. اگر دوبار پشت‌سرهم Ctrl+C بزنید این پنل باز می‌شود (در تنظیمات پنل فعال کنید).</p>
<h3>Spike: ابزار فراموش‌شده</h3>
<p>Spike یک کلیپ‌بورد «انباشتی» است: هر بار <strong>Ctrl+F3</strong> می‌زنید، متن انتخاب‌شده <em>بریده</em> و به انتهای Spike اضافه می‌شود. در پایان با <strong>Ctrl+Shift+F3</strong> همه را یک‌جا و به ترتیب می‌چسبانید. برای جمع کردن جمله‌های پراکنده‌ی یک سند در یک بخش «خلاصه» فوق‌العاده است. (اگر می‌خواهید کپی شود نه بریده، بلافاصله بعد از Ctrl+F3 یک Ctrl+Z بزنید؛ متن برمی‌گردد اما در Spike می‌ماند.)</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><strong>Ctrl+Shift+V</strong> در نسخه‌های جدید 365 مستقیماً «فقط متن» می‌چسباند.</li>
<li>Shift+Ctrl+F8 و سپس فلش‌ها، انتخاب ستونی را با کیبورد انجام می‌دهد؛ برای پاک کردن ستونی از شماره‌های ابتدای خطوط عالی است.</li>
<li>Ctrl+Shift+C و Ctrl+Shift+V (Format Painter صفحه‌کلیدی) فقط قالب را کپی و اعمال می‌کند. دوبار کلیک روی Format Painter آن را قفل می‌کند تا روی چند جا اعمال کنید.</li>
<li>Ctrl+Z تا ۱۰۰ مرحله برمی‌گردد. اما بستن سند تاریخچه را پاک می‌کند؛ Version History (فایل‌های OneDrive) به‌جای آن.</li>
<li>Alt+کشیدن روی یک جدول، ستون‌ها را بدون تغییر بقیه‌ی ستون‌ها تغییر اندازه می‌دهد و اندازه‌ی دقیق را روی خط‌کش نشان می‌دهد.</li>
</ul>""",
                },
                {
                    "title": "ذخیره‌سازی هوشمند: فرمت‌ها، AutoRecover، جاسازی فونت و کوچک کردن فایل",
                    "kind": "text",
                    "minutes": 17,
                    "is_preview": False,
                    "body": r"""<h2>فرمت درست برای هدف درست</h2>
<table><thead><tr><th>فرمت</th><th>چیست</th><th>کِی</th></tr></thead><tbody>
<tr><td>.docx</td><td>فرمت استاندارد (یک فایل ZIP از XML ها)</td><td>همیشه برای کار جاری</td></tr>
<tr><td>.docm</td><td>docx + ماکرو</td><td>وقتی سند ماکرو دارد (فصل ۷)</td></tr>
<tr><td>.dotx / .dotm</td><td>قالب (Template)</td><td>الگوی نامه، گزارش، پایان‌نامه</td></tr>
<tr><td>.doc</td><td>فرمت قدیمی 97-2003</td><td>فقط اگر گیرنده Word خیلی قدیمی دارد؛ بسیاری امکانات را از دست می‌دهید</td></tr>
<tr><td>.pdf</td><td>خروجی نهایی ثابت</td><td>ارسال، چاپ، آرشیو</td></tr>
<tr><td>.rtf / .odt / .txt</td><td>تبادل با نرم‌افزارهای دیگر</td><td>به ندرت</td></tr>
</tbody></table>
<p>وقتی سندی با فرمت قدیمی باز می‌کنید، در نوار عنوان «Compatibility Mode» می‌بینید و بعضی امکانات (مثل بعضی افکت‌های تصویر یا معادلات جدید) خاکستری می‌شوند. File ← Info ← <strong>Convert</strong> آن را به فرمت جدید تبدیل می‌کند.</p>
<h3>AutoRecover و بازیابی</h3>
<p>Options ← Save: «Save AutoRecover information every N minutes» را روی ۲ تا ۵ دقیقه بگذارید و گزینه‌ی «Keep the last AutoRecovered version if I close without saving» را روشن نگه دارید. اگر Word بسته شد یا برق رفت، File ← Info ← Manage Document ← <strong>Recover Unsaved Documents</strong> نسخه‌های خودکار را نشان می‌دهد. برای فایل خراب: File ← Open ← فایل را انتخاب کنید ← فلش کنار Open ← <strong>Open and Repair</strong>. اگر باز هم نشد، در پنجره‌ی Open نوع فایل را «Recover Text from Any File» بگذارید.</p>
<h3>جاسازی فونت — ضروری برای فارسی</h3>
<p>اگر فونت B Nazanin یا IRANSans روی سیستم گیرنده نباشد، Word فونت دیگری جایگزین می‌کند و صفحه‌بندی به هم می‌ریزد. Options ← Save ← <strong>Embed fonts in the file</strong> را روشن کنید («Embed only the characters used» حجم را کم می‌کند، ولی گیرنده نمی‌تواند با آن فونت متن جدید تایپ کند). بعضی فونت‌های تجاری اجازه‌ی جاسازی نمی‌دهند؛ Word پیام می‌دهد. برای ارسال نهایی، PDF تقریباً همیشه انتخاب امن‌تری است.</p>
<h3>چرا فایلم ۸۰ مگابایت شده؟</h3>
<ul>
<li>تصاویر بزرگ: روی یک تصویر کلیک کنید ← Picture Format ← <strong>Compress Pictures</strong> ← تیک «Apply only to this picture» را بردارید ← 150 ppi برای چاپ معمولی. همچنین Options ← Advanced ← «Do not compress images in file» باید خاموش باشد.</li>
<li>داده‌های برش‌خورده: Compress Pictures ← «Delete cropped areas of pictures».</li>
<li>Version History یا Track Changes قدیمی: تغییرات را Accept All کنید.</li>
<li>فونت‌های جاسازی‌شده: هر فونت چند مگابایت است.</li>
<li>ذخیره با Save As (نه Save) یک بار فایل را از نو می‌سازد و باقی‌مانده‌های داخلی را پاک می‌کند.</li>
</ul>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>فایل docx در واقع ZIP است: پسوند را به .zip تغییر دهید و باز کنید؛ پوشه‌ی word/media همه‌ی تصاویر اصلی را با کیفیت کامل دارد — سریع‌ترین راه برای بیرون کشیدن تصاویر یک سند.</li>
<li>F12 مستقیماً Save As را باز می‌کند؛ Ctrl+S ذخیره‌ی معمولی است.</li>
<li>File ← Info ← Properties ← Advanced Properties: عنوان، نویسنده و کلیدواژه‌ها را پر کنید؛ این‌ها با فیلد DOCPROPERTY داخل سند قابل استفاده‌اند و در PDF هم منتقل می‌شوند.</li>
<li>Options ← Save ← «Default local file location» را روی پوشه‌ی پروژه‌هایتان بگذارید تا هر بار مسیر را نگردید.</li>
<li>در فایل‌های OneDrive با AutoSave روشن، هر تغییری بلافاصله ذخیره می‌شود؛ اگر می‌خواهید «آزمایشی» چیزی را عوض کنید، اول File ← Save a Copy بزنید.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۲ ─────────────────────────────
        {
            "title": "فصل ۲: Styles — ستون فقرات هر سند حرفه‌ای",
            "lessons": [
                {
                    "title": "چرا قالب‌بندی مستقیم دشمن شماست؛ انواع Style و Style Inspector",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>دو راه برای ساختن یک تیتر</h2>
<p>راه اول: متن را انتخاب می‌کنید، بولد می‌زنید، اندازه را ۱۶ می‌کنید، رنگ می‌دهید. راه دوم: روی <strong>Heading 1</strong> کلیک می‌کنید. ظاهر هر دو یکی است، اما فقط راه دوم به Word می‌گوید «این یک تیتر است». همین تفاوت است که فهرست مطالب خودکار، Navigation Pane، ارجاع متقابل، شماره‌گذاری فصل‌ها، بوک‌مارک‌های PDF و تغییر یک‌جای ظاهر همه‌ی تیترها را ممکن می‌کند. راه اول را <em>قالب‌بندی مستقیم</em> (Direct Formatting) می‌نامند و در اسناد بلند، منبع اصلی آشفتگی است.</p>
<h3>پنج نوع Style</h3>
<table><thead><tr><th>نوع</th><th>روی چه چیزی</th><th>مثال</th></tr></thead><tbody>
<tr><td>Paragraph (¶)</td><td>کل پاراگراف: تراز، فاصله، تورفتگی + فونت پایه</td><td>Normal، Heading 1، Caption</td></tr>
<tr><td>Character (a)</td><td>فقط متن انتخاب‌شده</td><td>Strong، Emphasis، «کد داخل متن»</td></tr>
<tr><td>Linked (¶a)</td><td>هر دو؛ بسته به این‌که پاراگراف انتخاب شده یا بخشی از آن</td><td>Heading 1 در واقع Linked است</td></tr>
<tr><td>Table</td><td>خطوط، رنگ ردیف‌ها، سربرگ جدول</td><td>Grid Table 4</td></tr>
<tr><td>List</td><td>ساختار شماره‌گذاری چندسطحی</td><td>List Number</td></tr>
</tbody></table>
<p>پنل Styles با <strong>Ctrl+Alt+Shift+S</strong> باز می‌شود. در پایین آن سه دکمه هست: New Style، <strong>Style Inspector</strong> و Manage Styles. Style Inspector نشان می‌دهد متن زیر مکان‌نما دقیقاً چه Style‌ای دارد و چه قالب‌بندی مستقیمی روی آن اضافه شده — اولین ابزار عیب‌یابی وقتی «نمی‌دانم چرا این پاراگراف این شکلی است».</p>
<h3>پاک کردن قالب‌بندی مستقیم</h3>
<ul>
<li><strong>Ctrl+Space</strong>: قالب‌بندی کاراکتر را پاک می‌کند (متن به فونت Style برمی‌گردد).</li>
<li><strong>Ctrl+Q</strong>: قالب‌بندی پاراگراف را پاک می‌کند (تراز، فاصله، تورفتگی).</li>
<li><strong>Ctrl+Shift+N</strong>: Style را به Normal برمی‌گرداند.</li>
<li>دکمه‌ی Clear All Formatting در تب Home هر سه را با هم انجام می‌دهد.</li>
</ul>
<p>یک روش سریع برای پاک‌سازی سند به‌هم‌ریخته: Ctrl+A، Ctrl+Space، Ctrl+Q — و بعد Style‌های درست را به تیترها بدهید. تمام قالب‌بندی‌های تصادفی از بین می‌رود.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><strong>Shift+F1</strong> پنل Reveal Formatting را باز می‌کند؛ مثل «مشاهده‌ی کد» صفحه‌ی وب، همه‌ی ویژگی‌های فونت و پاراگراف را با لینک به پنجره‌ی مربوط نشان می‌دهد و می‌توانید دو قسمت متن را با هم مقایسه کنید (Compare to another selection).</li>
<li>در پنل Styles، گزینه‌ی <em>Options</em> را روی «All styles» بگذارید تا Style‌های پنهان مثل Caption، Footnote Text و TOC 1 را ببینید؛ به‌طور پیش‌فرض فقط «Recommended» نمایش داده می‌شوند.</li>
<li>در Options ← Advanced ← «Keep track of formatting» و «Mark formatting inconsistencies» را روشن کنید؛ Word زیر متنی که قالب‌بندی مستقیمِ مشابه یک Style دارد خط موج‌دار آبی می‌کشد و پیشنهاد می‌دهد به Style تبدیل شود.</li>
<li>Ctrl+Shift+S کادر «Apply Styles» را باز می‌کند؛ اسم Style را تایپ کنید و Enter بزنید — سریع‌تر از پیدا کردنش در گالری.</li>
<li>در نمای Draft می‌توانید «Style Area Pane» را فعال کنید (Options ← Advanced ← Style area pane width) تا اسم Style هر پاراگراف در حاشیه‌ی چپ دیده شود؛ برای بازبینی ساختار سند بی‌نظیر است.</li>
</ul>""",
                },
                {
                    "title": "Heading ها، Navigation Pane و نمای Outline: مدیریت سند بلند",
                    "kind": "text",
                    "minutes": 18,
                    "is_preview": False,
                    "body": r"""<h2>تیترها فقط ظاهر نیستند؛ ساختارند</h2>
<p>Word نه سطح Heading دارد (Heading 1 تا 9). به‌طور پیش‌فرض فقط سه تای اول در گالری دیده می‌شوند؛ به محض استفاده از Heading 3، Heading 4 ظاهر می‌شود. میانبرها: <strong>Ctrl+Alt+1</strong>، <strong>Ctrl+Alt+2</strong>، <strong>Ctrl+Alt+3</strong> برای سه سطح اول و <strong>Ctrl+Shift+N</strong> برای برگشت به Normal. با <strong>Alt+Shift+فلش چپ/راست</strong> یک تیتر را یک سطح بالا/پایین می‌برید (Promote/Demote)؛ در متن فارسی جهت فلش‌ها برعکس حس می‌شود، امتحان کنید.</p>
<h3>Navigation Pane به‌عنوان میز فرمان</h3>
<p>وقتی تیترها Heading باشند، Ctrl+F ← تب Headings یک نقشه‌ی زنده می‌دهد. روی هر تیتر راست‌کلیک کنید: Promote، Demote، New Heading Before/After، <strong>Select Heading and Content</strong>، <strong>Delete</strong> (کل بخش!) و Print Heading and Content. کشیدن یک تیتر در این پنل کل بخش را با زیرمجموعه‌هایش جابه‌جا می‌کند. فلش کنار هر تیتر آن را جمع می‌کند تا فقط ساختار کلی را ببینید.</p>
<h3>نمای Outline</h3>
<p>View ← Outline ساختار را بدون حواس‌پرتی ظاهر نشان می‌دهد. «Show Level» را روی Level 2 بگذارید تا فقط فصل‌ها و بخش‌ها دیده شوند؛ «Show First Line Only» خط اول هر پاراگراف را نشان می‌دهد. با دکمه‌های Move Up/Down (یا Alt+Shift+فلش بالا/پایین) بخش‌ها را مثل کارت جابه‌جا می‌کنید. کسانی که کتاب یا پایان‌نامه می‌نویسند، ساختار را در Outline طراحی می‌کنند و بعد متن را می‌نویسند.</p>
<h3>جمع کردن تیترها در نمای عادی</h3>
<p>وقتی ماوس را روی یک Heading می‌برید، مثلث کوچکی کنارش ظاهر می‌شود؛ کلیک روی آن، متن زیر تیتر را جمع می‌کند (Collapse). در Paragraph ← تنظیمات Heading می‌توانید «Collapsed by default» را روشن کنید تا سند مثل یک فهرست باز شود — برای اسناد مرجع و راهنما عالی است (فقط در docx کار می‌کند نه در چاپ).</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>می‌توانید به هر Style سطح Outline بدهید (Modify Style ← Format ← Paragraph ← Outline level) بدون این‌که اسمش Heading باشد؛ مثلاً Style «عنوان جدول» با سطح ۹ در Navigation Pane و TOC ظاهر می‌شود.</li>
<li>در Navigation Pane تایپ چند حرف، فقط تیترهایی را نشان می‌دهد که آن عبارت را دارند یا زیرمجموعه‌شان دارد.</li>
<li>Heading‌ها به‌طور پیش‌فرض «Keep with next» و «Keep lines together» دارند — به همین دلیل یک تیتر هیچ‌وقت تنها در پایین صفحه نمی‌ماند. اگر با Enter‌های خالی پاراگراف بعد را دور کنید این حفاظت بی‌اثر می‌شود.</li>
<li>عنوان اصلی سند را Heading 1 نکنید؛ Style <strong>Title</strong> برای همین است و در TOC نمی‌آید.</li>
<li>در Read Mode، Navigation Pane همچنان با تب Headings کار می‌کند؛ برای خواندن گزارش‌های بلند روی لپ‌تاپ راحت‌تر است.</li>
</ul>""",
                },
                {
                    "title": "ساخت و ویرایش Style: Based on، Next style، فونت Complex Script و کنترل صفحه‌بندی",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>پنجره‌ی Modify Style را خوب بشناسید</h2>
<p>روی یک Style راست‌کلیک ← <strong>Modify</strong>. بخش‌های این پنجره:</p>
<table><thead><tr><th>گزینه</th><th>معنی</th><th>توصیه</th></tr></thead><tbody>
<tr><td>Style based on</td><td>ویژگی‌های تعریف‌نشده از این Style به ارث می‌رسند</td><td>همه‌ی Style‌های متنی را بر پایه‌ی Normal بسازید؛ تغییر فونت Normal همه را عوض می‌کند</td></tr>
<tr><td>Style for following paragraph</td><td>بعد از Enter، پاراگراف بعد چه Style‌ای بگیرد</td><td>برای Heading‌ها: Normal (یا «متن اصلی»). برای «عنوان جدول»: خود جدول</td></tr>
<tr><td>Add to Styles gallery</td><td>در Ribbon نمایش داده شود</td><td>فقط Style‌های پرکاربرد</td></tr>
<tr><td>Automatically update</td><td>هر قالب‌بندی دستی روی یک پاراگراف، Style را عوض کند</td><td><strong>هرگز روشن نکنید</strong>؛ یک بولد تصادفی همه‌ی تیترها را عوض می‌کند</td></tr>
<tr><td>Only in this document / New documents based on this template</td><td>دامنه‌ی تغییر</td><td>گزینه‌ی دوم Normal.dotm را عوض می‌کند</td></tr>
</tbody></table>
<h3>Format ← Font: دو زبان، دو فونت</h3>
<p>در پنجره‌ی Font داخل Modify Style، بخش <strong>Complex scripts</strong> فونت، اندازه و ضخامت متن فارسی را جدا از لاتین تعیین می‌کند. عادت رایج و اشتباه: تغییر فقط بخش Latin و تعجب از این‌که فارسی عوض نشد. برای پایان‌نامه‌ی فارسی معمولاً: Complex = B Nazanin 14، Latin = Times New Roman 12. اندازه‌ی فارسی همیشه یک تا دو واحد بزرگ‌تر از لاتین انتخاب می‌شود تا هم‌قد به نظر برسند.</p>
<h3>Format ← Paragraph: تب Line and Page Breaks</h3>
<ul>
<li><strong>Widow/Orphan control</strong>: نمی‌گذارد یک خط تنها از پاراگراف در بالا یا پایین صفحه بماند.</li>
<li><strong>Keep with next</strong>: پاراگراف با پاراگراف بعدی در یک صفحه بماند (تیترها، عنوان بالای جدول، تصویر با زیرنویسش).</li>
<li><strong>Keep lines together</strong>: پاراگراف بین دو صفحه شکسته نشود.</li>
<li><strong>Page break before</strong>: هر Heading 1 (فصل) از صفحه‌ی جدید شروع شود — به‌جای Ctrl+Enter دستی.</li>
<li><strong>Suppress line numbers</strong> و <strong>Don't hyphenate</strong> برای موارد خاص.</li>
</ul>
<h3>ساخت Style جدید</h3>
<p>سریع‌ترین راه: یک پاراگراف را دقیقاً آن‌طور که می‌خواهید قالب‌بندی کنید، بعد در گالری Styles ← Create a Style ← نام بدهید ← Modify تا Based on و Next style را درست کنید. نام‌های فارسی مجازند («متن اصلی»، «عنوان شکل»، «نقل‌قول»). برای اعمال قالب‌بندی یک پاراگراف به Style موجود: پاراگراف را انتخاب کنید ← راست‌کلیک روی Style ← <strong>Update … to Match Selection</strong>.</p>
<h3>Line spacing درست برای فارسی</h3>
<p>فونت‌های فارسی نقطه‌ها و کشیدگی‌های بلندی دارند؛ Single معمولاً خطوط را به هم می‌چسباند. برای B Nazanin و IRANSans، <strong>Multiple 1.15</strong> یا <strong>Exactly</strong> با مقدار ۱٫۵ برابر اندازه‌ی فونت (مثلاً 21pt برای فونت 14) خوانایی و یکنواختی بهتری می‌دهد. مقدار Exactly این مزیت را دارد که خطوط صفحات روبه‌رو دقیقاً تراز می‌شوند.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>در پنجره‌ی Modify Style، دکمه‌ی Format ← <strong>Shortcut key</strong> اجازه می‌دهد به هر Style یک میانبر بدهید (مثلاً Alt+M برای «متن اصلی»).</li>
<li>اگر Style «Normal» را با Right-to-Left و فونت فارسی تنظیم کنید و «New documents based on this template» را بزنید، دیگر هیچ‌وقت لازم نیست تنظیمات فارسی را تکرار کنید.</li>
<li>در پنل Styles، Manage Styles ← تب <strong>Recommend</strong> ترتیب و نمایش Style‌ها در گالری را کنترل می‌کند؛ Style‌های بی‌فایده را Hide کنید تا همکاران‌تان اشتباه انتخاب نکنند.</li>
<li>Style‌های «Heading 1..9» و «TOC 1..9» و «Caption» اسم داخلی ثابت دارند؛ اگر اسم نمایششان را عوض کنید (مثلاً «عنوان فصل»)، Word هنوز آن‌ها را به‌عنوان Heading می‌شناسد. اسم مستعار با ویرگول اضافه می‌شود: «Heading 1,عنوان فصل».</li>
<li>Ctrl+Shift+Alt+S ← گزینه‌ی «Disable Linked Styles» در پایین پنل، مانع می‌شود که با انتخاب چند کلمه و زدن Heading 1 فقط همان کلمات تیتر شوند.</li>
</ul>""",
                },
                {
                    "title": "Themes و Style Sets، انتقال Style بین اسناد با Organizer",
                    "kind": "text",
                    "minutes": 15,
                    "is_preview": False,
                    "body": r"""<h2>ظاهر کل سند در یک کلیک</h2>
<p>تب <strong>Design</strong> سه لایه‌ی ظاهری را کنترل می‌کند که Style‌ها از آن‌ها ارث می‌برند:</p>
<ul>
<li><strong>Theme</strong>: مجموعه‌ای از رنگ‌ها (Colors)، فونت‌ها (Fonts) و افکت‌ها. وقتی در Style فونتی مثل «+Body» یا رنگی مثل «Accent 1» انتخاب می‌کنید، از Theme می‌آید و با تغییر Theme عوض می‌شود.</li>
<li><strong>Style Set</strong>: تعریف کامل Style‌های پایه (فاصله‌ها، اندازه‌ها). گالری Document Formatting همان Style Set هاست.</li>
<li><strong>Paragraph Spacing / Set as Default</strong>: فاصله‌های پیش‌فرض کل سند.</li>
</ul>
<p>برای برند شرکت: Design ← Colors ← Customize Colors ← رنگ‌های سازمانی را با کد HEX وارد کنید و با نام شرکت ذخیره کنید. Fonts ← Customize Fonts ← فونت تیتر و متن (توجه: پنجره‌ی Theme Fonts بخش Complex script ندارد؛ فونت فارسی را در Style تنظیم کنید). سپس Design ← Themes ← <strong>Save Current Theme</strong>. این Theme در Excel و PowerPoint هم قابل استفاده است تا گزارش، جدول و ارائه یک‌دست باشند.</p>
<h3>Organizer: کپی Style بین دو سند</h3>
<p>سند A را با Style‌های خوب دارید و می‌خواهید در سند B هم باشند. پنل Styles ← Manage Styles ← دکمه‌ی <strong>Import/Export</strong>. پنجره‌ی Organizer دو ستون دارد: چپ سند فعلی، راست Normal.dotm. با Close File / Open File هر فایلی را می‌توان در ستون راست باز کرد و Style‌ها را با دکمه‌ی Copy بین دو طرف جابه‌جا کرد. همین پنجره تب Macro Project Items هم دارد.</p>
<p>راه ساده‌تر برای یک سند: تب Developer ← Document Template ← <strong>Attach</strong> قالب جدید ← تیک <strong>Automatically update document styles</strong>. با این کار Style‌های هم‌نام از قالب جایگزین می‌شوند. (تیک را بعداً بردارید، وگرنه هر بار باز کردن سند دوباره به‌روز می‌شود.)</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>اگر Style‌ای در سند B هم‌نام ولی متفاوت است، وقتی متن را از A به B می‌چسبانید، Word تعریف B را اعمال می‌کند — به همین دلیل «Keep Source Formatting» گاهی نتیجه نمی‌دهد. اول Style را با Organizer منتقل کنید.</li>
<li>Design ← Set as Default همه‌ی تنظیمات Theme، Style Set و فاصله‌ها را در Normal.dotm ذخیره می‌کند.</li>
<li>برای دیدن این‌که یک رنگ «Theme color» است یا ثابت: در انتخاب رنگ، ردیف اول Theme Colors است و بخش Standard Colors ثابت. رنگ‌های ثابت با تغییر Theme عوض نمی‌شوند.</li>
<li>فایل Theme با پسوند .thmx در پوشه‌ی Document Themes کاربر ذخیره می‌شود و می‌توانید برای همکاران بفرستید.</li>
<li>Style‌ای که در Organizer حذف می‌کنید، متنی که آن را داشت به Normal برمی‌گردد؛ حذف Style‌های داخلی (Built-in) ممکن نیست، فقط Hide می‌شوند.</li>
</ul>""",
                },
                {
                    "title": "لیست‌ها و شماره‌گذاری چندسطحی: پیوند به Heading، ارقام فارسی و «الف)»",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>لیستی که خودش شماره می‌خورد</h2>
<p>سه دکمه در تب Home: Bullets، Numbering و <strong>Multilevel List</strong>. لیست ساده با Tab یک سطح پایین و Shift+Tab یک سطح بالا می‌رود. برای ادامه یا شروع مجدد شماره‌ها روی شماره راست‌کلیک کنید: <strong>Continue Numbering</strong>، <strong>Restart at 1</strong>، <strong>Set Numbering Value</strong>. اگر تایپ «1.» و فاصله خودبه‌خود لیست می‌سازد و نمی‌خواهید، Options ← Proofing ← AutoCorrect ← AutoFormat As You Type ← «Automatic numbered lists» را خاموش کنید.</p>
<h3>شماره‌گذاری فصل‌ها: 1، 1-1، 1-1-1</h3>
<p>راه درست، پیوند دادن Multilevel List به Heading Style هاست تا شماره‌ی فصل و بخش خودکار باشد و در ارجاع‌ها و زیرنویس شکل‌ها («شکل ۲-۳») قابل استفاده شود:</p>
<ol>
<li>مکان‌نما را روی یک Heading 1 بگذارید ← Multilevel List ← <strong>Define New Multilevel List</strong> ← دکمه‌ی More.</li>
<li>سطح 1: «Link level to style» = Heading 1؛ Number style = 1, 2, 3؛ در کادر «Enter formatting for number» فقط ۱ بماند (یا «فصل ۱»).</li>
<li>سطح 2: Link = Heading 2؛ در کادر قالب، ابتدا «Include level number from: Level 1» را انتخاب کنید و بین دو شماره خط تیره بگذارید تا «۱-۱» شود. سطح 3 مشابه با دو سطح قبلی.</li>
<li>Number alignment و Text indent را برای راست‌به‌چپ تنظیم کنید؛ «Follow number with» = Tab یا Space.</li>
</ol>
<p>اکنون هر Heading جدید خودش شماره می‌گیرد و با جابه‌جایی فصل‌ها همه‌ی شماره‌ها به‌روز می‌شوند.</p>
<h3>ارقام فارسی و «الف، ب، پ»</h3>
<p>در Define New Number Format، Number style فقط 1,2,3 و a,b,c و i,ii,iii و… دارد. برای ارقام فارسی دو راه هست: (۱) اگر Numeral در Options روی Context/Hindi باشد و پاراگراف راست‌به‌چپ، شماره‌ها فارسی نمایش داده می‌شوند؛ (۲) در نسخه‌هایی که زبان فارسی نصب است، Number style گزینه‌های «Arabic-Indic» و «Persian» هم دارد. برای «الف)» ، Number style را روی «alef, be, pe» (در همان فهرست، انتهای لیست) بگذارید و در قالب پرانتز اضافه کنید.</p>
<h3>Bullet های سفارشی</h3>
<p>Bullets ← Define New Bullet ← Symbol (مثلاً از فونت Wingdings) یا Picture. برای متن فارسی، Bullet را چپ‌چین می‌بینید؟ جهت پاراگراف را Right-to-Left کنید، نه تراز را.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>اگر لیست بین دو پاراگراف معمولی قطع شد و می‌خواهید بعد از توضیح ادامه پیدا کند، روی شماره‌ی جدید راست‌کلیک ← Continue Numbering؛ یا بهتر: پاراگراف میانی را با Style «List Continue» بنویسید.</li>
<li>برای پاراگراف‌های چندخطی داخل یک آیتم لیست، Shift+Enter بزنید؛ Enter آیتم جدید می‌سازد.</li>
<li>Ctrl+Shift+L لیست Bullet را روشن/خاموش می‌کند.</li>
<li>در Multilevel List ← Define New <strong>List Style</strong> (نه فقط Multilevel List) تعریف را به‌صورت Style ذخیره می‌کند تا با Organizer به اسناد دیگر ببرید — تعریف‌های معمولی قابل انتقال نیستند و منبع «شماره‌های به‌هم‌ریخته بعد از کپی» همین است.</li>
<li>در «Define New Multilevel List»، گزینه‌ی <em>Legal style numbering</em> همه‌ی سطوح را به عدد تبدیل می‌کند (مثلاً به جای «فصل ۲ - بخش الف»، «۲-۱»).</li>
<li>اگر شماره‌ی لیست‌ها بعد از کپی/پیست از جای دیگر «ادامه‌ی لیست قبلی» شد، Ctrl+Z یک بار معمولاً فقط شماره را جدا می‌کند و متن را نگه می‌دارد.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۳ ─────────────────────────────
        {
            "title": "فصل ۳: صفحه‌آرایی، Section‌ها و سربرگ‌های هوشمند",
            "lessons": [
                {
                    "title": "Page Setup کامل: حاشیه، Gutter، صفحات آینه‌ای و تنظیمات صحافی",
                    "kind": "text",
                    "minutes": 16,
                    "is_preview": False,
                    "body": r"""<h2>پنجره‌ای که سه تب دارد</h2>
<p>فلش کوچک گروه Page Setup در تب Layout (یا دوبار کلیک روی ناحیه‌ی خاکستری خط‌کش) پنجره‌ی کامل را باز می‌کند. سه تب دارد و بیشتر کاربران فقط تب اول را دیده‌اند.</p>
<h3>تب Margins</h3>
<ul>
<li><strong>Gutter</strong>: فضای اضافی برای صحافی که به حاشیه‌ی داخلی اضافه می‌شود. Gutter position برای سند فارسی «Right» است (چون صحافی سمت راست است). دانشگاه‌ها معمولاً حاشیه‌ی صحافی ۳٫۵ سانتی‌متر و بقیه ۲٫۵ می‌خواهند.</li>
<li><strong>Multiple pages ← Mirror margins</strong>: برای چاپ دورو، حاشیه‌ها به «Inside/Outside» تبدیل می‌شوند تا صفحات روبه‌رو قرینه باشند.</li>
<li><strong>Book fold</strong>: Word خودش صفحات را برای تا زدن کتابچه مرتب می‌کند (۴ صفحه روی یک برگ A4 دورو).</li>
<li><strong>2 pages per sheet</strong>: دو صفحه‌ی A5 روی یک A4.</li>
<li>Apply to: <em>Whole document</em> یا <em>This section</em> یا <em>This point forward</em> (که خودکار یک Section break می‌سازد).</li>
</ul>
<h3>تب Paper</h3>
<p>Paper size و منبع کاغذ چاپگر. Word گاهی با نصب اولیه روی Letter است؛ برای ایران A4 (21×29.7). اگر می‌خواهید همیشه A4 باشد، در همین پنجره Set As Default بزنید.</p>
<h3>تب Layout</h3>
<ul>
<li><strong>Section start</strong>: نوع شکست Section فعلی (بعداً مهم می‌شود).</li>
<li><strong>Headers and footers</strong>: «Different odd and even» و «Different first page» + فاصله‌ی سربرگ از لبه‌ی کاغذ.</li>
<li><strong>Vertical alignment</strong>: Center برای صفحه‌ی عنوان بدون استفاده از Enter‌های خالی؛ Justified برای پر کردن صفحه.</li>
<li><strong>Line Numbers</strong>: شماره‌ی خط در حاشیه (قراردادها، مقالات داوری).</li>
<li><strong>Borders</strong>: قاب دور صفحه (تب Design ← Page Borders هم همین است).</li>
</ul>
<h3>Ruler، واحدها و اندازه‌ی دقیق</h3>
<p>View ← Ruler را روشن کنید. واحد خط‌کش از Options ← Advanced ← Display ← Show measurements in units of (Centimeters) تغییر می‌کند. اگر هنگام کشیدن حاشیه یا Tab روی خط‌کش Alt را نگه دارید، اندازه‌ی دقیق نمایش داده می‌شود.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>Layout ← Margins ← Custom Margins ← Set As Default: حاشیه، اندازه‌ی کاغذ و جهت را برای همه‌ی اسناد آینده ذخیره می‌کند.</li>
<li>در نمای Print Layout اگر فاصله‌ی سفید بین صفحات ناپدید شد، بین دو صفحه دوبار کلیک کنید (Hide/Show White Space).</li>
<li>Options ← Advanced ← «Show text boundaries» خطوط نقطه‌چین حاشیه‌ها را نشان می‌دهد؛ برای صفحه‌آرایی دقیق مفید است.</li>
<li>برای صفحه‌ی عنوان پایان‌نامه، به جای Enter‌های متعدد، Vertical alignment = Center در یک Section مستقل استفاده کنید.</li>
<li>Landscape فقط برای یک صفحه: متن آن صفحه را انتخاب کنید ← Page Setup ← Orientation = Landscape ← Apply to: <strong>Selected text</strong>. Word خودش قبل و بعدش Section break می‌گذارد.</li>
</ul>""",
                },
                {
                    "title": "Break‌ها: Page، Column و انواع Section — قلب صفحه‌آرایی",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>Section چیست و چرا همه‌چیز به آن وابسته است</h2>
<p>یک سند Word از یک یا چند <strong>Section</strong> تشکیل شده. هر Section می‌تواند حاشیه، جهت کاغذ، تعداد ستون، سربرگ/پاورقی، شماره‌گذاری صفحه، پاورقی و حتی اندازه‌ی کاغذ مستقل داشته باشد. هر بار که می‌خواهید یکی از این‌ها «از یک جایی به بعد» عوض شود، به Section جدید نیاز دارید — نه به هیچ چیز دیگری.</p>
<p>Layout ← Breaks:</p>
<table><thead><tr><th>نوع</th><th>کار</th><th>کاربرد</th></tr></thead><tbody>
<tr><td>Page (Ctrl+Enter)</td><td>فقط صفحه‌ی جدید؛ Section عوض نمی‌شود</td><td>شروع فصل (بهتر: Page break before در Style)</td></tr>
<tr><td>Column</td><td>رفتن به ستون بعدی</td><td>متن چندستونی</td></tr>
<tr><td>Text Wrapping</td><td>ادامه‌ی متن زیر یک تصویر/جدول شناور</td><td>کنار زدن متن از کنار تصویر</td></tr>
<tr><td>Section: Next Page</td><td>Section جدید از صفحه‌ی بعد</td><td>فصل‌ها، تغییر شماره‌گذاری، Landscape</td></tr>
<tr><td>Section: Continuous</td><td>Section جدید در همان صفحه</td><td>چند ستون در وسط صفحه، تغییر حاشیه در همان صفحه</td></tr>
<tr><td>Section: Even / Odd Page</td><td>Section جدید از صفحه‌ی زوج/فرد بعدی</td><td>کتاب: هر فصل از صفحه‌ی فرد (راست) شروع شود</td></tr>
</tbody></table>
<h3>قوانین کار با Section</h3>
<ul>
<li>¶ را روشن کنید تا خط دوتایی «Section Break (Next Page)» را ببینید. کور کار نکنید.</li>
<li>تنظیمات هر Section <em>در Section break انتهای آن</em> ذخیره می‌شود. اگر Section break را حذف کنید، متن قبل، تنظیمات Section بعد را می‌گیرد — دلیل اصلی «همه‌چیز به هم ریخت».</li>
<li>در نوار وضعیت، شماره‌ی Section را نمایش دهید (راست‌کلیک روی نوار ← Section) تا بدانید کجا هستید.</li>
<li>برای پرش بین Section‌ها: Ctrl+G ← Section ← +1.</li>
</ul>
<h3>الگوی استاندارد پایان‌نامه</h3>
<ol>
<li>Section 1: صفحه‌ی عنوان و صفحات آغازین (بدون شماره یا با شماره‌ی «الف، ب، پ»).</li>
<li>Section 2: فهرست‌ها (شماره‌ی حروفی یا رومی).</li>
<li>Section 3 به بعد: فصل‌ها با شماره‌ی عددی از ۱.</li>
<li>Section پایانی: منابع و پیوست‌ها (شماره‌گذاری ادامه یا مستقل).</li>
</ol>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>در نمای <strong>Draft</strong> می‌توانید Section break را دقیقاً ببینید و با Delete حذف کنید؛ در Print Layout گاهی انتخابش سخت است.</li>
<li>قبل از حذف Section break، اول به Section بعد بروید و تنظیماتش را با Section قبلی یکسان کنید تا بعد از حذف چیزی تغییر نکند.</li>
<li>یک Section break «Continuous» که به‌دنبال آن Section break «Next Page» بیاید، معمولاً به «Next Page» تبدیل می‌شود؛ Word این تبدیل را بی‌صدا انجام می‌دهد.</li>
<li>در Find & Replace، «^b» به معنی Section break است؛ می‌توانید همه را یک‌جا پیدا (یا با احتیاط حذف) کنید.</li>
<li>برای این‌که متن چندستونی وسط صفحه به‌طور مساوی بین ستون‌ها تقسیم شود، انتهای آن یک Section break Continuous بگذارید.</li>
</ul>""",
                },
                {
                    "title": "سربرگ و پاورقی هوشمند: شماره‌ی صفحه‌ی فارسی، «صفحه X از Y»، StyleRef و Link to Previous",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>سربرگ فقط یک خط متن نیست</h2>
<p>دوبار کلیک روی بالای صفحه، ناحیه‌ی Header را باز می‌کند و تب <strong>Header & Footer</strong> ظاهر می‌شود. سه گزینه‌ی این تب تعیین می‌کنند چند سربرگ متفاوت دارید: <strong>Different First Page</strong> (صفحه‌ی اول هر Section)، <strong>Different Odd & Even Pages</strong> (کل سند) و برای هر Section، دکمه‌ی <strong>Link to Previous</strong>.</p>
<h3>Link to Previous؛ کلید همه‌ی مشکلات</h3>
<p>وقتی Section جدید می‌سازید، سربرگ و پاورقی‌اش به‌طور پیش‌فرض «به قبلی وصل» هستند؛ یعنی هرچه در Section 2 بنویسید در Section 1 هم ظاهر می‌شود. برای سربرگ مستقل، به Section جدید بروید و Link to Previous را <em>خاموش</em> کنید — جداگانه برای Header، Footer، First Page و Even Page! (چهار پیوند مستقل). ۹۰٪ موارد «شماره‌ی صفحه‌ی صفحات اول هم عوض شد» به همین برمی‌گردد.</p>
<h3>شماره‌ی صفحه</h3>
<p>Insert ← Page Number ← جای دلخواه. سپس <strong>Format Page Numbers</strong>:</p>
<ul>
<li>Number format: 1,2,3 / a,b,c / i,ii,iii / الف,ب,پ (وقتی زبان فارسی نصب است) / ۱,۲,۳ (Arabic-Indic یا Persian در فهرست).</li>
<li>Include chapter number: با Multilevel List فصل‌ها ترکیب می‌شود (۲-۱۵ یعنی صفحه‌ی ۱۵ فصل ۲).</li>
<li><strong>Start at</strong>: برای این‌که فصل اول از ۱ شروع شود، در Section فصل اول این گزینه را روی ۱ بگذارید و Link to Previous را خاموش کنید.</li>
</ul>
<h3>«صفحه ۳ از ۴۰»</h3>
<p>در پاورقی تایپ کنید «صفحه » ← Insert ← Quick Parts ← Field ← <strong>Page</strong> ← « از » ← Field ← <strong>NumPages</strong>. اگر صفحات آغازین را نمی‌خواهید بشمارید، به جای NumPages از <strong>SectionPages</strong> استفاده کنید (تعداد صفحات همین Section). یا سریع‌تر: Alt+Shift+P شماره‌ی صفحه را درج می‌کند.</p>
<h3>StyleRef: عنوان فصل در سربرگ به‌طور خودکار</h3>
<p>در کتاب‌ها بالای هر صفحه نام فصل جاری نوشته می‌شود. لازم نیست برای هر فصل Section جداگانه بسازید: در Header، Quick Parts ← Field ← <strong>StyleRef</strong> ← Style name = Heading 1. Word خودش آخرین Heading 1 قبل از این صفحه را نشان می‌دهد. با تیک «Insert paragraph number» شماره‌ی فصل را می‌دهد. برای سربرگ صفحات زوج Heading 1 و فرد Heading 2 بگذارید، دقیقاً مثل کتاب‌های چاپی.</p>
<h3>محتوای دیگر سربرگ</h3>
<p>لوگو (Insert ← Pictures، با wrap «Behind Text» اگر می‌خواهید پس‌زمینه باشد)، تاریخ خودکار (Insert ← Date & Time با تیک Update automatically — احتیاط: در سند رسمی تاریخ ثابت بهتر است)، نام فایل (Field ← FileName)، خط زیر سربرگ (Borders ← Bottom border روی پاراگراف سربرگ، نه Underline).</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>سربرگ سه Tab stop پیش‌فرض دارد: چپ، وسط، راست. با یک Tab متن به وسط و با دو Tab به انتهای دیگر می‌رود؛ لازم نیست فاصله بزنید.</li>
<li>برای شماره‌ی صفحه‌ی فارسی بدون تغییر Numeral کل سند، شماره‌ی صفحه را انتخاب کنید و در پنجره‌ی Font، بخش Complex script را روی فونت فارسی بگذارید و جهت پاراگراف پاورقی را RTL کنید.</li>
<li>اگر شماره‌ی صفحه‌ی صفحه‌ی اول نمی‌خواهید، فقط «Different First Page» را برای همان Section روشن کنید؛ سربرگ خالی می‌شود اما صفحه همچنان شمرده می‌شود.</li>
<li>در Options ← Display ← «Print hidden text» خاموش باشد، اما «Update fields before printing» روشن باشد تا NumPages همیشه درست چاپ شود.</li>
<li>Header & Footer ← Header from Top: اگر ۰٫۵ سانتی‌متر بگذارید و متن سربرگ زیاد باشد، حاشیه‌ی بالای متن خودکار بزرگ می‌شود؛ Word هیچ‌وقت سربرگ را روی متن نمی‌اندازد مگر با تصویر شناور.</li>
</ul>""",
                },
                {
                    "title": "ستون‌ها، Text Box، Cover Page، Watermark و Kashida برای متن فارسی",
                    "kind": "text",
                    "minutes": 16,
                    "is_preview": False,
                    "body": r"""<h2>ستون‌بندی</h2>
<p>Layout ← Columns ← More Columns. برای فارسی، تیک <strong>Right-to-left</strong> در همین پنجره باعث می‌شود ستون اول سمت راست باشد. «Line between» خط عمودی بین ستون‌ها می‌کشد. متن انتخاب‌شده را می‌توانید جداگانه ستونی کنید (Apply to: Selected text)؛ Word خودش Section break Continuous می‌گذارد. با Ctrl+Shift+Enter به ستون بعدی می‌پرید. اگر می‌خواهید ستون‌ها در انتها هم‌قد شوند، بعد از متن یک Section break Continuous بگذارید.</p>
<h3>Text Box و Shape با متن</h3>
<p>Insert ← Text Box برای متن شناور (کادر نقل‌قول کنار صفحه، برچسب روی تصویر). Text Box در واقع یک Shape است؛ راست‌کلیک ← Format Shape همه‌ی گزینه‌ها را دارد. Text Box‌ها می‌توانند به هم <strong>Link</strong> شوند (Shape Format ← Create Link) تا متنِ سرریز از اولی به دومی برود — همان چیزی که در روزنامه می‌بینید. برای فارسی: Text Direction را از Shape Format تنظیم کنید و جهت پاراگراف داخل کادر را RTL.</p>
<h3>Cover Page، Blank Page، Watermark</h3>
<ul>
<li>Insert ← <strong>Cover Page</strong>: صفحه‌ی عنوان آماده با فیلدهای Title و Author که از Document Properties پر می‌شوند. طرح خودتان را انتخاب کنید ← Save Selection to Cover Page Gallery تا در همه‌ی اسناد باشد.</li>
<li>Design ← <strong>Watermark</strong>: «محرمانه» یا «پیش‌نویس» کم‌رنگ پشت متن. Custom Watermark ← Text watermark ← زبان فارسی؛ فونت فارسی انتخاب کنید. Watermark در واقع یک WordArt داخل Header است؛ برای حذف، به Header بروید.</li>
<li>Design ← <strong>Page Color</strong> فقط روی صفحه دیده می‌شود؛ برای چاپ Options ← Display ← Print background colors and images.</li>
</ul>
<h3>Justify و Kashida برای فارسی</h3>
<p>Justify (Ctrl+J) در متن فارسی فاصله‌ی بین کلمات را باز می‌کند. Word با نصب زبان فارسی، دکمه‌ی <strong>Justify Low / Medium / High</strong> در گروه Paragraph دارد که به‌جای فاصله، کشیده (ـ) اضافه می‌کند. برای متن رسمی چاپی «Justify» معمولی با فاصله‌ی متعادل یا Justify Low طبیعی‌تر است؛ Kashida زیاد مخصوص متون سنتی و قرآنی است. حتماً در Options ← Advanced ← Layout options ← «Don't expand character spaces on a line that ends with SHIFT+RETURN» را روشن کنید تا خط آخر پاراگراف‌های Justify‌شده که با Shift+Enter تمام می‌شوند کشیده نشود.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>در Options ← Advanced ← Show document content ← «Diacritics» می‌توانید رنگ اِعراب فارسی/عربی را جدا از متن تنظیم کنید.</li>
<li>Insert ← <strong>Blank Page</strong> در واقع دو Page break می‌گذارد؛ اگر صفحه‌ی خالی ناخواسته دارید، ¶ را روشن کنید و Page break اضافه را پاک کنید.</li>
<li>برای متن عمودی در جدول یا Text Box: Layout ← Text Direction. برای متن فارسی عمودی، جهت RTL + چرخش ۹۰ درجه‌ی کادر نتیجه‌ی خواناتری می‌دهد.</li>
<li>Drop Cap (Insert ← Drop Cap) برای فارسی کار می‌کند اما حرف چسبان اول کلمه جدا می‌شود؛ فقط در متن ادبی استفاده کنید.</li>
<li>Insert ← Object ← Text from File متن یک فایل Word دیگر را همان‌جا درج می‌کند — بدون کپی/پیست و با حفظ Style ها.</li>
</ul>""",
                },
                {
                    "title": "قالب (Template)، Normal.dotm، Quick Parts، AutoText و Building Blocks",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>یک بار بسازید، هزار بار استفاده کنید</h2>
<p>هر سند Word بر پایه‌ی یک <strong>Template</strong> ساخته می‌شود. سند خالی از <strong>Normal.dotm</strong> می‌آید؛ همه‌ی Style‌ها، حاشیه‌ها، فونت پیش‌فرض و ماکروهای شخصی شما آن‌جا ذخیره می‌شوند. اگر Word رفتار عجیب پیدا کرد (کند شد، فونت پیش‌فرض عوض شد)، Word را ببندید، Normal.dotm را از پوشه‌ی Templates کاربر تغییر نام دهید؛ Word یک Normal تازه می‌سازد.</p>
<h3>ساخت قالب سازمانی</h3>
<ol>
<li>سند را با Style‌های درست (Normal فارسی RTL، Heading‌های شماره‌دار، «متن اصلی»، «عنوان جدول»…)، سربرگ با لوگو، پاورقی با شماره‌ی صفحه و حاشیه‌های استاندارد آماده کنید.</li>
<li>متن نمونه را حذف کنید و به‌جای آن راهنمای کوتاه بگذارید (مثلاً «[عنوان گزارش را این‌جا بنویسید]»).</li>
<li>File ← Save As ← نوع فایل <strong>Word Template (.dotx)</strong>. Word خودش به پوشه‌ی Custom Office Templates می‌رود. اگر ماکرو دارد .dotm.</li>
<li>از این به بعد: File ← New ← <strong>Personal</strong> ← قالب شما. سند جدیدی ساخته می‌شود و قالب دست‌نخورده می‌ماند.</li>
</ol>
<p>برای تیم، پوشه‌ی مشترک شبکه را در Options ← Advanced ← File Locations ← <strong>Workgroup templates</strong> تنظیم کنید؛ همه قالب‌های یکسان می‌بینند.</p>
<h3>Quick Parts و AutoText</h3>
<p>هر چیزی که مرتب تکرار می‌کنید — امضای نامه، جدول مشخصات پروژه، پاراگراف سلب مسئولیت، یک شکل با زیرنویس — را انتخاب کنید ← Insert ← Quick Parts ← <strong>Save Selection to Quick Part Gallery</strong>. نام بدهید، Gallery را AutoText بگذارید، در Save in قالب Normal یا قالب سازمانی را انتخاب کنید. برای درج: اسم را تایپ کنید و <strong>F3</strong> بزنید، یا از Insert ← Quick Parts ← AutoText. این‌ها «Building Block» هستند و در فایل Building Blocks.dotx ذخیره می‌شوند؛ Cover Page، Header، Footer، Table و Equation آماده‌ی Word هم همین‌ها هستند و همه با Building Blocks Organizer قابل مدیریت‌اند.</p>
<h3>Document Property ها</h3>
<p>Insert ← Quick Parts ← <strong>Document Property</strong> ← Title/Author/Company/… فیلدی درج می‌کند که هرجای سند تکرار شود با یک تغییر همه‌جا به‌روز می‌شود — نام مشتری در قرارداد، شماره‌ی پروژه در گزارش. مقدار را از File ← Info ← Properties عوض کنید، یا خود فیلد را در سند ویرایش کنید (همه‌ی نسخه‌ها هم‌زمان تغییر می‌کنند).</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>برای ویرایش خود قالب (نه ساخت سند از آن) از File ← Open مسیر قالب را باز کنید؛ دوبار کلیک روی .dotx همیشه سند جدید می‌سازد.</li>
<li>تب <strong>Developer</strong> (Options ← Customize Ribbon ← تیک Developer) ابزار Content Control دارد: کادر متنی، تاریخ، لیست کشویی و چک‌باکس واقعی برای ساخت فرم‌های پرکردنی. Design Mode برای ویرایش متن راهنما.</li>
<li>Developer ← Document Template نشان می‌دهد سند فعلی به کدام قالب وصل است و می‌توانید عوضش کنید.</li>
<li>AutoText با تایپ ۴ حرف اول اسم و دیدن راهنمای زردرنگ + Enter هم درج می‌شود (اگر «Show AutoComplete suggestions» روشن باشد).</li>
<li>Building Blocks Organizer: Insert ← Quick Parts ← Building Blocks Organizer. با «Edit Properties» می‌توانید دسته و توضیح بدهید و با Delete بلوک‌های آماده‌ی بی‌فایده (مثل Cover Page‌های پیش‌فرض) را حذف کنید.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۴ ─────────────────────────────
        {
            "title": "فصل ۴: جدول، تصویر و اشیای گرافیکی — بدون دردسر",
            "lessons": [
                {
                    "title": "جدول حرفه‌ای: جهت RTL، تکرار سربرگ، تبدیل متن به جدول، فرمول و مرتب‌سازی",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>سه راه ساخت جدول</h2>
<p>Insert ← Table: (۱) کشیدن روی شبکه، (۲) Insert Table با تعداد دقیق و گزینه‌ی AutoFit، (۳) <strong>Convert Text to Table</strong>: اگر داده‌ها با Tab یا ویرگول یا «؛» جدا شده‌اند (مثلاً خروجی یک نرم‌افزار یا کپی از سایت)، همه را انتخاب کنید و در همین پنجره جداکننده را مشخص کنید؛ ثانیه‌ای جدول می‌شود. عکس این عمل (Convert to Text) هم در تب Layout جدول هست. راه چهارم: Excel Spreadsheet برای وقتی محاسبه‌ی واقعی لازم دارید.</p>
<h3>تنظیمات فارسی جدول</h3>
<p>Table Properties (راست‌کلیک) ← تب Table ← <strong>Table direction: Right-to-left</strong>. ستون اول سمت راست می‌رود و Tab هم به ترتیب درست حرکت می‌کند. اگر جدول را قبل از RTL کردن پاراگراف ساخته‌اید، ترتیب ستون‌ها ممکن است برعکس باشد؛ همین گزینه درستش می‌کند. تراز جدول در صفحه (Alignment: Right/Center) و «Text wrapping: None» را برای جدول‌های داخل متن نگه دارید؛ جدول شناور (Around) همان دردسر تصویر شناور را دارد.</p>
<h3>ردیف سربرگ که تکرار می‌شود</h3>
<p>ردیف اول را انتخاب کنید ← تب Layout جدول ← <strong>Repeat Header Rows</strong>. در جدول‌های چندصفحه‌ای عنوان ستون‌ها بالای هر صفحه تکرار می‌شود. هم‌زمان: Table Properties ← Row ← تیک <strong>Allow row to break across pages</strong> را بردارید تا یک ردیف بین دو صفحه نصف نشود.</p>
<h3>ابزارهای تب Layout جدول</h3>
<table><thead><tr><th>ابزار</th><th>کار</th></tr></thead><tbody>
<tr><td>AutoFit ← Contents / Window / Fixed</td><td>عرض ستون‌ها بر اساس محتوا، عرض صفحه، یا ثابت</td></tr>
<tr><td>Distribute Rows / Columns</td><td>هم‌اندازه کردن</td></tr>
<tr><td>Merge / Split Cells، Split Table</td><td>ادغام و تقسیم (Ctrl+Shift+Enter جدول را دو تکه می‌کند)</td></tr>
<tr><td>Cell Margins</td><td>فاصله‌ی متن از خطوط سلول؛ برای جدول فارسی خوانا ۰٫۱۵ سانتی‌متر</td></tr>
<tr><td>Sort</td><td>مرتب‌سازی الفبایی/عددی/تاریخی روی یک تا سه ستون؛ فارسی را درست مرتب می‌کند اگر «ی» عربی نباشد</td></tr>
<tr><td>Formula</td><td>=SUM(ABOVE)، =AVERAGE(LEFT)، =A1*B1 با آدرس اکسلی؛ به‌روزرسانی با F9</td></tr>
<tr><td>Convert to Text</td><td>جدول به متن تب‌دار</td></tr>
</tbody></table>
<h3>Table Style</h3>
<p>تب Table Design ← گالری. Style‌های Grid/List با «Header Row»، «Banded Rows» و «First Column» ترکیب می‌شوند. Style سفارشی: New Table Style ← جداگانه برای Whole table، Header row، Banded rows تعریف کنید. برای گزارش فارسی: سربرگ با رنگ سبز سازمانی و متن سفید، ردیف‌های یک‌درمیان خاکستری ۵٪، بدون خطوط عمودی. Style ذخیره‌شده با Organizer قابل انتقال است.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>در سلول جدول، Tab به سلول بعد می‌رود؛ برای Tab واقعی داخل سلول <strong>Ctrl+Tab</strong>.</li>
<li>Tab در آخرین سلول ردیف آخر، ردیف جدید می‌سازد. برای درج ردیف بین دو ردیف، مکان‌نما را خارج از جدول انتهای ردیف بگذارید و Enter بزنید.</li>
<li>جدول اول سند که چسبیده به بالای صفحه است و نمی‌توانید بالایش بنویسید: مکان‌نما را در اولین سلول بگذارید و <strong>Ctrl+Shift+Enter</strong> بزنید؛ یک پاراگراف بالای جدول ایجاد می‌شود.</li>
<li>Alt+کشیدن خط ستون اندازه‌ی دقیق را روی خط‌کش نشان می‌دهد؛ Shift+کشیدن فقط همان ستون را تغییر می‌دهد و بقیه ثابت می‌مانند.</li>
<li>جدول تودرتو (جدول داخل سلول) مجاز است اما Sort و Formula را خراب می‌کند؛ برای صفحه‌آرایی پیچیده از Text Box استفاده کنید.</li>
<li>برای پیست یک محدوده از Excel به‌صورت <em>لینک زنده</em>: Paste Special ← Paste link ← Microsoft Excel Worksheet Object. هر تغییر در اکسل با F9 یا باز کردن سند به‌روز می‌شود.</li>
</ul>""",
                },
                {
                    "title": "تصویر بدون «پریدن»: Wrap، Anchor، Position، فشرده‌سازی و Selection Pane",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>چرا عکس‌ها جابه‌جا می‌شوند</h2>
<p>هر تصویر در Word یکی از دو حالت را دارد: <strong>In Line with Text</strong> (مثل یک حرف بزرگ داخل پاراگراف؛ با متن حرکت می‌کند، هیچ‌وقت نمی‌پرد) یا <strong>Floating</strong> (شناور با Wrap: Square، Tight، Through، Top and Bottom، Behind Text، In Front of Text). تصویر شناور به یک پاراگراف <strong>Anchor</strong> (لنگر) دارد و نسبت به آن جایگذاری می‌شود؛ هر وقت آن پاراگراف به صفحه‌ی بعد برود تصویر هم می‌رود — همین «پریدن» است.</p>
<p>قانون طلایی: در اسناد رسمی، پایان‌نامه و گزارش، همه‌ی تصاویر <strong>In Line</strong> باشند، در یک پاراگراف مستقل وسط‌چین، با زیرنویس زیرشان. فقط برای بروشور و طرح‌های تبلیغاتی سراغ Floating بروید. برای تغییر: کلیک روی تصویر ← دکمه‌ی Layout Options کنارش ← In Line with Text. Options ← Advanced ← Cut, copy, and paste ← <strong>Insert/paste pictures as: In line with text</strong> این را پیش‌فرض می‌کند.</p>
<h3>وقتی واقعاً شناور لازم دارید</h3>
<ul>
<li>¶ را روشن کنید تا لنگر (⚓) کنار پاراگراف دیده شود. لنگر را می‌توانید به پاراگراف دیگری بکشید.</li>
<li>Layout Options ← See more ← تب Position: «Lock anchor» تصویر را به همان پاراگراف قفل می‌کند؛ «Move object with text» را بردارید تا تصویر نسبت به <em>صفحه</em> ثابت شود (مثلاً لوگو در گوشه‌ی صفحه).</li>
<li>Position relative to Page/Margin/Column؛ برای فارسی «Right relative to margin».</li>
<li>Wrap ← Edit Wrap Points برای پیچاندن متن دور شکل نامنظم.</li>
<li>Layout ← <strong>Selection Pane</strong>: همه‌ی اشیای شناور را فهرست می‌کند؛ می‌توانید پنهان/انتخاب کنید و ترتیب لایه‌ها (Bring Forward) را عوض کنید. تصویری که «گم شده» را از این‌جا پیدا کنید.</li>
</ul>
<h3>ابزارهای تصویر (Picture Format)</h3>
<p><strong>Crop</strong> (کشیدن دستگیره‌های مشکی؛ Crop to Shape، Aspect Ratio)، <strong>Remove Background</strong> (حذف پس‌زمینه‌ی ساده)، Corrections/Color، Picture Styles (قاب و سایه)، <strong>Compress Pictures</strong>، <strong>Change Picture</strong> (جایگزینی با حفظ اندازه و موقعیت)، <strong>Reset Picture</strong> و <strong>Alt Text</strong> (متن جایگزین برای دسترس‌پذیری و PDF). Align/Distribute و Group وقتی چند شیء انتخاب شده (Shift+کلیک) فعال می‌شوند.</p>
<h3>تصویر و زیرنویس همیشه با هم</h3>
<p>پاراگراف تصویر را Keep with next بزنید (در Style مثلاً «تصویر»). یا تصویر و زیرنویس را داخل یک جدول یک‌سلولی بدون خط بگذارید؛ سلول هیچ‌وقت نصف نمی‌شود. با تصویر In Line، زیرنویس با Insert Caption زیرش می‌آید (درس بعد).</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>Insert ← Pictures ← فلش کنار Insert ← <strong>Link to File</strong> تصویر را جاسازی نمی‌کند و سند سبک می‌ماند (فایل تصویر باید کنار سند بماند). «Insert and Link» هر دو.</li>
<li>Ctrl+کشیدن یک تصویر آن را کپی می‌کند؛ Shift+کشیدن حرکت را افقی/عمودی نگه می‌دارد؛ Alt+کشیدن بدون چسبیدن به شبکه.</li>
<li>Insert ← Screenshot ← Screen Clipping قسمتی از هر پنجره‌ی باز را مستقیماً درج می‌کند.</li>
<li>راست‌کلیک روی تصویر ← Save as Picture تصویر اصلی را ذخیره می‌کند (حتی اگر Crop شده باشد، نسخه‌ی کامل).</li>
<li>Ctrl+Shift+G عکس گروهی می‌سازد؛ Ctrl+Shift+H جدا می‌کند. یک شیء داخل گروه با کلیک دوم جداگانه انتخاب می‌شود.</li>
<li>در Options ← Advanced ← «Show picture placeholders» تصاویر را با کادر خالی نشان می‌دهد تا کار با اسناد پرتصویر سریع شود.</li>
</ul>""",
                },
                {
                    "title": "Shape، SmartArt، نمودار، آیکون، Screenshot و معادلات ریاضی",
                    "kind": "text",
                    "minutes": 18,
                    "is_preview": False,
                    "body": r"""<h2>گرافیک بدون خروج از Word</h2>
<h3>Shapes و Drawing Canvas</h3>
<p>Insert ← Shapes: خط، پیکان، مستطیل، فلوچارت، Callout. با Shift کشیدن، دایره و مربع کامل می‌سازد. راست‌کلیک ← Add Text متن داخل شکل. وقتی چند شکل به هم مربوط‌اند (فلوچارت)، اول Insert ← Shapes ← <strong>New Drawing Canvas</strong> بسازید و شکل‌ها را داخل آن بکشید؛ همه با هم حرکت می‌کنند و پیکان‌های اتصال (Connectors) به شکل‌ها می‌چسبند و با جابه‌جایی کش می‌آیند. Shape Format ← Edit Shape ← Change Shape بدون از دست دادن متن نوع شکل را عوض می‌کند. راست‌کلیک ← <strong>Set as Default Shape</strong> ظاهر انتخابی را پیش‌فرض می‌کند.</p>
<h3>SmartArt</h3>
<p>Insert ← SmartArt: لیست، فرایند، چرخه، سلسله‌مراتب (چارت سازمانی)، رابطه، ماتریس، هرم. متن را در پنل Text (فلش کنار SmartArt) تایپ کنید؛ Tab سطح می‌سازد. SmartArt Design ← <strong>Right to Left</strong> جهت فلش‌ها و ترتیب را برای فارسی برمی‌گرداند. Change Colors و SmartArt Styles از Theme می‌گیرند. Convert ← to Shapes اگر خواستید کنترل کامل داشته باشید.</p>
<h3>نمودار</h3>
<p>Insert ← Chart ← نوع را انتخاب کنید؛ یک پنجره‌ی کوچک اکسل با داده‌ی نمونه باز می‌شود. داده را عوض کنید و ببندید. Chart Design ← <strong>Edit Data</strong> بعداً همان را باز می‌کند؛ Select Data برای تغییر محدوده. اگر نمودار در Excel آماده دارید: کپی از اکسل ← در Word Paste Options ← <strong>Use Destination Theme & Link Data</strong> تا نمودار با تغییر فایل اکسل به‌روز شود (Chart Design ← Refresh Data). عنوان و برچسب‌های فارسی نمودار: هر عنصر را انتخاب کنید و در Format، Text Direction را RTL کنید.</p>
<h3>آیکون‌ها، تصاویر سه‌بعدی و Screenshot</h3>
<p>Insert ← Icons (365) مجموعه‌ی آیکون‌های SVG که رنگ‌پذیرند و Convert to Shape می‌شوند. Insert ← Screenshot تصویر هر پنجره‌ی باز یا Screen Clipping بخشی از صفحه.</p>
<h3>معادلات (Equation)</h3>
<p><strong>Alt+=</strong> کادر معادله باز می‌کند. می‌توانید با <strong>UnicodeMath</strong> تایپ کنید: <code>x=(-b+-\sqrt(b^2-4ac))/2a</code> و Word خودش به فرمول زیبا تبدیل می‌کند؛ یا <strong>LaTeX</strong> را از تب Equation انتخاب کنید و <code>\frac{-b\pm\sqrt{b^2-4ac}}{2a}</code> بنویسید. Equation ← Ink Equation با ماوس/قلم بنویسید. برای شماره‌گذاری معادلات، معادله را در جدول سه‌ستونی بدون خط بگذارید (خالی | معادله | شماره با SEQ). متن فارسی داخل معادله: بخش متن را انتخاب و «Normal Text» بزنید تا حروف فارسی ایتالیک ریاضی نشوند.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>Insert ← Symbol ← More Symbols ← تب Special Characters فهرست میانبرهای کاراکترهای خاص (فاصله‌ی نشکن، خط‌تیره‌ی بلند و…) را نشان می‌دهد و می‌توانید برای هر نماد میانبر تعریف کنید.</li>
<li>هر کد یونیکد را تایپ کنید و <strong>Alt+X</strong> بزنید، به کاراکتر تبدیل می‌شود (200C سپس Alt+X = نیم‌فاصله). برعکس هم کار می‌کند: کاراکتر را انتخاب کنید و Alt+X کدش را نشان می‌دهد — برای تشخیص «ی» عربی از فارسی (064A در برابر 06CC).</li>
<li>Math AutoCorrect (Options ← Proofing ← AutoCorrect ← Math AutoCorrect) با تیک «Use Math AutoCorrect rules outside of math regions»، تایپ <code>\alpha</code> در متن عادی هم α می‌دهد.</li>
<li>راست‌کلیک روی نمودار ← Save as Template نمودار قالب می‌شود (Templates در Insert Chart).</li>
<li>Shape با Text: Shape Format ← Text Effects ← Transform برای متن منحنی (WordArt)؛ فونت فارسی پشتیبانی می‌شود.</li>
</ul>""",
                },
                {
                    "title": "زیرنویس (Caption)، فهرست شکل‌ها و جدول‌ها، ارجاع متقابل و فیلدهای SEQ",
                    "kind": "text",
                    "minutes": 22,
                    "is_preview": False,
                    "body": r"""<h2>«شکل ۲-۳» که خودش شماره می‌خورد</h2>
<p>روی تصویر یا جدول راست‌کلیک ← <strong>Insert Caption</strong> (یا References ← Insert Caption). Label را انتخاب کنید؛ برچسب‌های پیش‌فرض Figure/Table/Equation هستند؛ با <strong>New Label</strong> برچسب «شکل»، «جدول»، «نمودار» و «رابطه» بسازید (فقط یک بار؛ در Normal ذخیره می‌شوند). Position: زیر شکل، بالای جدول (استاندارد). <strong>Numbering</strong> ← تیک «Include chapter number» ← Chapter starts with style: Heading 1، Separator: خط تیره ← نتیجه: «شکل ۲-۳». این فقط وقتی کار می‌کند که Heading 1 با Multilevel List شماره‌دار باشد (فصل ۲).</p>
<p>پشت هر زیرنویس یک فیلد <strong>SEQ</strong> است: <code>{ SEQ شکل \* ARABIC \s 1 }</code>. Alt+F9 کدها را نشان می‌دهد. با کشیدن شکل‌ها به ترتیب جدید، شماره‌ها بعد از Ctrl+A و F9 درست می‌شوند. Style زیرنویس <strong>Caption</strong> است؛ آن را Modify کنید (فونت فارسی، اندازه ۱۲، وسط‌چین، Keep with next برای عنوان جدول).</p>
<h3>فهرست شکل‌ها و جدول‌ها</h3>
<p>References ← <strong>Insert Table of Figures</strong> ← Caption label: شکل. برای جدول‌ها یک بار دیگر با label جدول. Options ← می‌توانید به‌جای label از یک Style (مثلاً «عنوان نمودار») فهرست بسازید. به‌روزرسانی: راست‌کلیک ← Update Field ← Entire table. اگر جای فهرست اشتباه است، فیلد TOC با سوییچ \c را می‌توانید ببرید.</p>
<h3>ارجاع متقابل (Cross-reference)</h3>
<p>در متن می‌نویسید «همان‌طور که در » ← References ← <strong>Cross-reference</strong> ← Reference type: شکل ← Insert reference to: <strong>Only label and number</strong> ← انتخاب شکل ← Insert. حالا «شکل ۲-۳» یک فیلد REF است که با تغییر شماره‌ی شکل به‌روز می‌شود و در PDF لینک است (تیک Insert as hyperlink). برای Heading: Reference type: Heading ← «Heading text» یا «Page number» یا «Heading number». برای پاورقی، بوک‌مارک و معادله هم کار می‌کند. عبارت «بالا/پایین» (Include above/below) خودکار «در بالا» یا «در پایین» را اضافه می‌کند.</p>
<h3>به‌روزرسانی فیلدها — عادت ضروری</h3>
<ul>
<li>Ctrl+A سپس <strong>F9</strong> همه‌ی فیلدهای بدنه را به‌روز می‌کند (فیلدهای سربرگ و Text Box جدا هستند؛ آن‌ها را جداگانه انتخاب کنید).</li>
<li>Options ← Display ← <strong>Update fields before printing</strong> و Update linked data before printing را روشن کنید؛ هنگام PDF گرفتن هم به‌روز می‌شوند.</li>
<li>Options ← Advanced ← Field shading: <strong>Always</strong> تا فیلدها با پس‌زمینه‌ی خاکستری معلوم باشند و کسی دستی رویشان ننویسد (در چاپ نمی‌آید).</li>
</ul>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>Insert Caption ← <strong>AutoCaption</strong>: از این به بعد هر جدول یا تصویری که درج می‌کنید خودکار زیرنویس بگیرد.</li>
<li>اگر Caption روی تصویر شناور بزنید، Word آن را داخل یک Text Box می‌گذارد که در Table of Figures گاهی نمی‌آید. تصویر را In Line کنید.</li>
<li>ارجاعی که به «Error! Reference source not found» تبدیل شده یعنی هدفش حذف شده؛ با Ctrl+Z بعد از F9 می‌توانید ببینید کجا بوده، یا Find «Error!» بزنید.</li>
<li>برای شماره‌گذاری معادلات با «(۲-۱)» سمت چپ: جدول سه ستونی، ستون وسط معادله، ستون کنار Caption با برچسب «رابطه» و بدون نمایش برچسب (تیک Exclude label from caption).</li>
<li>فیلد SEQ را دستی هم می‌توانید بسازید: Ctrl+F9 ← داخل آکولاد بنویسید <code>SEQ گام</code> ← F9. شمارنده‌ی دلخواه برای «گام ۱، گام ۲…» در دستورالعمل‌ها.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۵ ─────────────────────────────
        {
            "title": "فصل ۵: فهرست‌ها، مرجع‌دهی، نمایه و فیلدها",
            "lessons": [
                {
                    "title": "فهرست مطالب پیشرفته: سطوح، Style سفارشی، سوییچ‌های فیلد TOC و چند فهرست در یک سند",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>فهرست مطالب فقط یک دکمه نیست</h2>
<p>References ← Table of Contents ← <strong>Custom Table of Contents</strong>. گزینه‌های مهم: Show page numbers، Right align page numbers، <strong>Tab leader</strong> (نقطه‌چین)، Formats (From template = از Style‌های TOC 1..9 سند شما)، <strong>Show levels</strong> (معمولاً ۳). دکمه‌ی <strong>Options</strong>: به هر Style سطح TOC می‌دهید؛ مثلاً «عنوان پیوست» را سطح ۱ و Heading 4 را حذف کنید. تیک «Outline levels» باعث می‌شود پاراگراف‌هایی که سطح Outline دارند هم بیایند.</p>
<h3>ظاهر فهرست: Style‌های TOC 1 تا TOC 9</h3>
<p>هیچ‌وقت خطوط فهرست را دستی قالب‌بندی نکنید؛ با Update پاک می‌شود. به‌جای آن Style‌های <strong>TOC 1</strong>، <strong>TOC 2</strong>… را Modify کنید (فونت فارسی در Complex script، تورفتگی راست برای سطوح پایین‌تر، Bold برای TOC 1). این Style‌ها در پنل Styles با Options ← All styles دیده می‌شوند. برای فارسی، جهت پاراگراف TOC ها را RTL و Tab stop شماره‌ی صفحه را Left با leader نقطه بگذارید.</p>
<h3>فیلد TOC و سوییچ‌هایش</h3>
<p>Alt+F9 نشان می‌دهد فهرست یک فیلد است: <code>{ TOC \o "1-3" \h \z \u }</code></p>
<table><thead><tr><th>سوییچ</th><th>معنی</th></tr></thead><tbody>
<tr><td>\o "1-3"</td><td>سطوح Heading 1 تا 3</td></tr>
<tr><td>\h</td><td>هر خط لینک باشد (Ctrl+کلیک؛ در PDF هم)</td></tr>
<tr><td>\z</td><td>در Web Layout شماره‌ی صفحه پنهان شود</td></tr>
<tr><td>\u</td><td>از سطح Outline پاراگراف‌ها استفاده کند</td></tr>
<tr><td>\t "عنوان پیوست,1,عنوان جدول,2"</td><td>Style‌های سفارشی با سطح</td></tr>
<tr><td>\b نام_بوک‌مارک</td><td>فقط داخل یک بوک‌مارک (فهرست جداگانه برای هر فصل)</td></tr>
<tr><td>\n "3-3"</td><td>سطح ۳ بدون شماره‌ی صفحه</td></tr>
<tr><td>\c "شکل"</td><td>فهرست شکل‌ها (همان Table of Figures)</td></tr>
</tbody></table>
<p>می‌توانید مستقیم کد را ویرایش کنید و F9 بزنید. برای دو فهرست (مثلاً فهرست کلی و فهرست جزئی هر فصل)، هر فصل را Bookmark کنید و یک TOC با \b در ابتدای آن بگذارید.</p>
<h3>به‌روزرسانی</h3>
<p>کلیک داخل فهرست ← F9 (یا References ← Update Table) ← «Update page numbers only» وقتی فقط صفحه‌ها جابه‌جا شده‌اند، «Update entire table» وقتی تیتری اضافه/حذف/ویرایش شده. قالب‌بندی دستی داخل فهرست با گزینه‌ی دوم از بین می‌رود — دلیل دیگری برای استفاده از Style‌های TOC.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>اگر یک تیتر در فهرست نمی‌آید، Style آن احتمالاً Heading نیست یا فقط بخشی از پاراگراف Heading است (Linked style روی چند کلمه). Ctrl+Shift+S روی آن نگاه کنید.</li>
<li>اگر متنی اضافی در فهرست می‌آید (مثلاً یک پاراگراف عادی)، احتمالاً سطح Outline دارد؛ در Paragraph ← Outline level ← Body Text.</li>
<li>فهرست مطالب را می‌توان با Ctrl+Shift+F9 به متن ثابت تبدیل کرد (برای ارسال به کسی که نباید فیلدها را ببیند) — بازگشت ندارد، روی کپی انجام دهید.</li>
<li>References ← Add Text سریع‌ترین راه برای دادن سطح TOC به یک پاراگراف بدون تغییر ظاهر آن است.</li>
<li>در PDF، فهرست با \h لینک می‌شود، اما بوک‌مارک‌های نوار کناری PDF از Heading‌ها ساخته می‌شوند (گزینه‌ی Create bookmarks using Headings هنگام ذخیره‌ی PDF).</li>
</ul>""",
                },
                {
                    "title": "پاورقی و پی‌نوشت: شماره‌ی فارسی، شروع مجدد هر صفحه/فصل، خط جداکننده و تبدیل",
                    "kind": "text",
                    "minutes": 16,
                    "is_preview": False,
                    "body": r"""<h2>Footnote و Endnote</h2>
<p><strong>Ctrl+Alt+F</strong> پاورقی (پایین همان صفحه) و <strong>Ctrl+Alt+D</strong> پی‌نوشت (انتهای سند یا Section) درج می‌کند. متن پاورقی را همان‌جا بنویسید؛ دوبار کلیک روی شماره بین متن و پاورقی می‌پرد. حذف پاورقی: شماره‌ی مرجع را <em>در متن</em> پاک کنید (نه متن پاورقی را)؛ بقیه خودکار بازشماری می‌شوند.</p>
<h3>پنجره‌ی Footnote and Endnote (فلش گروه Footnotes)</h3>
<ul>
<li><strong>Number format</strong>: 1,2,3 / a,b,c / i,ii,iii / ۱,۲,۳ / نمادهای *,†,‡ / الف,ب,پ.</li>
<li><strong>Numbering</strong>: Continuous، <strong>Restart each section</strong> (هر فصل از ۱)، <strong>Restart each page</strong> (رایج در کتاب‌های فارسی).</li>
<li><strong>Custom mark</strong>: علامت دلخواه به‌جای شماره (مثلاً ستاره برای پاورقی مترجم).</li>
<li><strong>Footnote layout ← Columns</strong>: پاورقی‌های چندستونی وقتی متن اصلی چندستونی است.</li>
<li>Apply changes to: This section / Whole document.</li>
</ul>
<h3>پاورقی برای معادل انگلیسی</h3>
<p>در متون فارسی، پاورقی معمولاً معادل لاتین اصطلاح است. پاراگراف پاورقی را LTR و چپ‌چین کنید (Style <strong>Footnote Text</strong> را Modify کنید: جهت LTR، فونت لاتین Times 10، فونت فارسی B Nazanin 11) تا نقطه و پرانتز درست بنشیند. شماره‌ی پاورقی در متن با Style <strong>Footnote Reference</strong> (بالانویس) کنترل می‌شود؛ اگر می‌خواهید در متن فارسی شماره فارسی باشد اما در خود پاورقی لاتین، Number format را روی 1,2,3 بگذارید و Numeral سند را Context.</p>
<h3>خط جداکننده و ادامه‌ی پاورقی</h3>
<p>خط کوتاه بالای پاورقی‌ها فقط در نمای <strong>Draft</strong> قابل ویرایش است: View ← Draft ← References ← Show Notes ← از منوی کشویی پنل، <strong>Footnote Separator</strong> را انتخاب کنید؛ می‌توانید خط را حذف، بلندتر یا راست‌چین کنید. <strong>Footnote Continuation Separator</strong> خطی است که وقتی پاورقی به صفحه‌ی بعد سرریز کند ظاهر می‌شود و <strong>Continuation Notice</strong> متنی مثل «ادامه در صفحه‌ی بعد».</p>
<h3>تبدیل و کنترل</h3>
<p>در همان پنجره دکمه‌ی <strong>Convert</strong>: همه‌ی پاورقی‌ها به پی‌نوشت یا برعکس یا جابه‌جایی. برای پی‌نوشت هر فصل در انتهای همان فصل: Endnotes ← Location: End of section و در Page Setup ← Layout ← <strong>Suppress endnotes</strong> را برای Section‌هایی که نمی‌خواهید خاموش نگه دارید.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>فاصله‌ی بین پاورقی‌ها را با Spacing After در Style «Footnote Text» تنظیم کنید نه با Enter.</li>
<li>اگر پاورقی به صفحه‌ی بعد می‌رود در حالی که جا هست، معمولاً پاراگراف متن اصلی «Keep lines together» دارد یا Line spacing «Exactly» با مقدار کم است.</li>
<li>برای ارجاع دوباره به همان پاورقی (بدون شماره‌ی جدید): Cross-reference ← Reference type: Footnote ← Footnote number (formatted).</li>
<li>در Find & Replace، «^f» پاورقی و «^e» پی‌نوشت را پیدا می‌کند؛ Go To (Ctrl+G) ← Footnote برای پرش.</li>
<li>یادداشت‌های داخل جدول: پاورقی جدول در Word وجود ندارد؛ برای «یادداشت‌های جدول» یک ردیف آخر ادغام‌شده با فونت کوچک بسازید یا Custom mark با ستاره بگذارید.</li>
</ul>""",
                },
                {
                    "title": "Citations & Bibliography: منابع، سبک‌های APA/IEEE، Source Manager و منابع فارسی",
                    "kind": "text",
                    "minutes": 18,
                    "is_preview": False,
                    "body": r"""<h2>مرجع‌دهی خودکار داخل Word</h2>
<p>References ← Style (APA، IEEE، Chicago، Harvard، MLA…) ← <strong>Insert Citation ← Add New Source</strong>. نوع منبع (کتاب، مقاله‌ی ژورنال، وب‌سایت، پایان‌نامه…) را انتخاب و فیلدها را پر کنید. تیک <strong>Show All Bibliography Fields</strong> فیلدهای بیشتر (DOI، ویرایش، مترجم) را می‌دهد. برای چند نویسنده دکمه‌ی Edit را بزنید و نام‌ها را جداگانه وارد کنید تا سبک‌ها «و همکاران» را درست بسازند. در متن، «(Smith, 2021)» یا «[1]» درج می‌شود؛ روی آن کلیک ← فلش ← <strong>Edit Citation</strong> برای افزودن شماره‌ی صفحه یا پنهان کردن سال/نویسنده.</p>
<h3>Source Manager</h3>
<p>References ← Manage Sources: دو فهرست دارد — <strong>Master List</strong> (همه‌ی منابعی که تا حالا در هر سندی وارد کرده‌اید؛ در فایل Sources.xml کاربر) و <strong>Current List</strong> (منابع این سند). با Copy بین دو فهرست منبع جابه‌جا می‌شود؛ منابع علامت‌خورده با ✓ در متن استفاده شده‌اند. Sources.xml را می‌توانید به همکار بدهید یا Browse کنید تا فهرست منابع مشترک تیم داشته باشید.</p>
<h3>فهرست منابع</h3>
<p>References ← <strong>Bibliography</strong> ← «Bibliography/References/Works Cited» یا Insert Bibliography (بدون عنوان). این یک فیلد است؛ با تغییر Style یا افزودن منبع، Update Field کنید. ظاهر با Style <strong>Bibliography</strong> کنترل می‌شود (RTL، فونت فارسی و لاتین). برای منابع فارسی: در Add New Source، زبان (Language) را Persian بگذارید تا نام‌ها به ترتیب فارسی مرتب شوند و «و» به جای «and» بیاید (بسته به سبک). سبک‌های Word فایل‌های XSL هستند؛ سبک‌های فارسی سفارشی (مثل شیوه‌ی دانشگاه) را می‌توان به پوشه‌ی Bibliography\Style اضافه کرد.</p>
<h3>Placeholder</h3>
<p>وسط نوشتن وقت پر کردن منبع ندارید؟ Insert Citation ← <strong>Add New Placeholder</strong> ← یک نام (مثل Ahmadi2020). بعداً از Source Manager (علامت ؟ کنارش) کاملش کنید.</p>
<h3>محدودیت‌ها و جایگزین‌ها</h3>
<p>ابزار داخلی برای مقاله و پایان‌نامه با چند ده منبع کافی است، اما جست‌وجوی خودکار منبع، PDF و همگام‌سازی ندارد. برای پژوهش سنگین، نرم‌افزارهای مدیریت مرجع مثل Zotero، Mendeley یا EndNote افزونه‌ی Word دارند و همان Cite While You Write را با ده‌ها هزار سبک انجام می‌دهند. اگر روزی مهاجرت کردید، ارجاع‌های داخلی Word را با Ctrl+Shift+F9 ثابت کنید و از نو با افزونه وارد کنید؛ دو سیستم را با هم مخلوط نکنید.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><strong>Table of Authorities</strong> (Mark Citation، Alt+Shift+I) برای متون حقوقی: نمایه‌ی مواد قانونی و پرونده‌های استنادشده با شماره‌ی صفحه.</li>
<li>Bibliography را می‌توان به متن ثابت تبدیل کرد (Convert bibliography to static text) تا دستی ویرایش شود — روی نسخه‌ی نهایی.</li>
<li>هر Citation یک فیلد CITATION است؛ Alt+F9 ساختارش را نشان می‌دهد و می‌توانید سوییچ \l (زبان) و \p (صفحه) را ببینید.</li>
<li>در سبک IEEE ترتیب شماره‌ها ترتیب اولین ظهور در متن است؛ اگر پاراگراف‌ها را جابه‌جا کنید، بعد از Update همه‌ی شماره‌ها درست می‌شوند.</li>
<li>برای ارجاع به منبع فارسی داخل متن انگلیسی (یا برعکس)، فیلد Citation را انتخاب و جهت پاراگراف را برای همان بخش با Ctrl+Shift تغییر دهید تا پرانتزها برعکس نشوند.</li>
</ul>""",
                },
                {
                    "title": "نمایه (Index): Mark Entry، زیرمدخل‌ها، فایل AutoMark و ساخت نمایه‌ی موضوعی فارسی",
                    "kind": "text",
                    "minutes": 14,
                    "is_preview": False,
                    "body": r"""<h2>نمایه‌ی انتهای کتاب</h2>
<p>نمایه (Index) فهرست الفبایی اصطلاحات با شماره‌ی صفحاتی است که در آن آمده‌اند. Word نمایه را از فیلدهای <strong>XE</strong> پنهان که در متن گذاشته‌اید می‌سازد.</p>
<h3>علامت‌گذاری مدخل</h3>
<p>کلمه را انتخاب کنید ← References ← <strong>Mark Entry</strong> (Alt+Shift+X). پنجره باز می‌ماند تا بین مدخل‌ها بروید. گزینه‌ها:</p>
<ul>
<li><strong>Main entry</strong> و <strong>Subentry</strong>: «پایگاه داده» و زیر آن «رابطه‌ای»، «NoSQL».</li>
<li><strong>Cross-reference</strong>: «See» → «نگاه کنید به: SQL».</li>
<li><strong>Page range</strong>: برای مبحثی که چند صفحه ادامه دارد، اول متن را Bookmark کنید و این‌جا انتخاب کنید (۱۲–۱۸).</li>
<li><strong>Mark</strong>: فقط این مورد؛ <strong>Mark All</strong>: همه‌ی تکرارهای این کلمه در سند (اولین تکرار در هر پاراگراف).</li>
</ul>
<p>Word کد <code>{ XE "پایگاه داده:رابطه‌ای" }</code> را به‌صورت متن پنهان درج می‌کند و ¶ را روشن می‌کند؛ کدها با Ctrl+Shift+8 پنهان می‌شوند. برای مرتب‌سازی فارسی، املای مدخل باید یکدست باشد («ی» فارسی، نیم‌فاصله).</p>
<h3>AutoMark: نمایه از روی فهرست</h3>
<p>یک سند دو ستونی (جدول) بسازید: ستون اول کلمه‌ای که در متن است، ستون دوم مدخل نمایه (با «:» برای زیرمدخل). References ← Insert Index ← <strong>AutoMark</strong> ← این فایل. Word همه‌ی موارد را یک‌جا علامت می‌زند. برای کتاب چند صد صفحه‌ای، این روش تنها راه عملی است.</p>
<h3>درج و به‌روزرسانی نمایه</h3>
<p>References ← <strong>Insert Index</strong>: نوع Indented/Run-in، تعداد ستون (۲ برای A4)، Right align page numbers، Tab leader، زبان (Persian برای ترتیب الفبای فارسی) و Formats. ظاهر با Style‌های <strong>Index 1..9</strong> و <strong>Index Heading</strong> (حروف الفبا) کنترل می‌شود. به‌روزرسانی: کلیک داخل نمایه ← F9. اگر مدخلی اشتباه است، فیلد XE آن را در متن ویرایش کنید نه خود نمایه را.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>برای بولد یا ایتالیک کردن شماره‌ی صفحه‌ی مدخل اصلی (مثلاً جایی که تعریف شده)، در پنجره‌ی Mark Entry تیک Bold/Italic را بزنید؛ در کد به‌صورت \b و \i می‌آید.</li>
<li>Find ← «^d XE» همه‌ی فیلدهای نمایه را پیدا می‌کند و با Replace خالی حذف می‌شوند (وقتی می‌خواهید از نو شروع کنید).</li>
<li>نمایه‌ی نام‌ها و نمایه‌ی موضوعی جداگانه: در XE از سوییچ \f "نام" استفاده کنید و در INDEX هم \f "نام"؛ دو نمایه‌ی مستقل می‌سازد.</li>
<li>مدخل‌های فارسی که با «آ» شروع می‌شوند در ترتیب الفبایی Word زیر «ا» می‌آیند؛ اگر نمی‌خواهید، مدخل را با \y "آ..." (sort key) تنظیم کنید.</li>
<li>در نمایه‌ی چند ستونی، اگر می‌خواهید هر حرف الفبا از ستون جدید شروع نشود، تیک «Column break» را در Index Heading برندارید؛ رفتار پیش‌فرض درست است.</li>
</ul>""",
                },
                {
                    "title": "فیلدها، بوک‌مارک و لینک: Ctrl+F9، Alt+F9، IF، DOCPROPERTY، DATE و قفل کردن فیلد",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>فیلد یعنی «Word این‌جا را خودش پر کن»</h2>
<p>شماره‌ی صفحه، فهرست مطالب، زیرنویس شکل، ارجاع، تاریخ خودکار، Citation — همه فیلد هستند. Insert ← Quick Parts ← <strong>Field</strong> فهرست کامل با گزینه‌های هرکدام را نشان می‌دهد. کاربران حرفه‌ای فیلد را دستی می‌نویسند:</p>
<ol>
<li><strong>Ctrl+F9</strong>: یک جفت آکولاد ویژه { } درج می‌کند (تایپ آکولاد معمولی کار نمی‌کند).</li>
<li>داخل آن کد را می‌نویسید: <code>{ DATE \@ "yyyy/MM/dd" }</code></li>
<li><strong>F9</strong>: نتیجه را نشان می‌دهد. <strong>Alt+F9</strong>: همه‌ی فیلدهای سند بین کد و نتیجه سوییچ می‌کند؛ <strong>Shift+F9</strong>: فقط همین فیلد.</li>
</ol>
<table><thead><tr><th>فیلد</th><th>کاربرد</th></tr></thead><tbody>
<tr><td>PAGE، NUMPAGES، SECTIONPAGES</td><td>شماره و تعداد صفحات</td></tr>
<tr><td>DATE، TIME، CREATEDATE، SAVEDATE، PRINTDATE</td><td>تاریخ‌های مختلف؛ \@ برای قالب. CREATEDATE ثابت می‌ماند، DATE هر بار عوض می‌شود</td></tr>
<tr><td>FILENAME \p</td><td>نام و مسیر فایل (در پاورقی اسناد کنترل‌شده)</td></tr>
<tr><td>DOCPROPERTY "Company"</td><td>خواندن ویژگی‌های سند و ویژگی‌های سفارشی</td></tr>
<tr><td>STYLEREF "Heading 1"</td><td>متن آخرین پاراگراف با آن Style (سربرگ زنده)</td></tr>
<tr><td>SEQ نام</td><td>شمارنده‌ی دلخواه (\r 1 برای شروع مجدد، \c برای تکرار آخرین عدد)</td></tr>
<tr><td>REF نام_بوک‌مارک</td><td>تکرار متن یک بوک‌مارک (نام مشتری یک بار تایپ، همه‌جا تکرار)</td></tr>
<tr><td>IF { REF مبلغ } &gt; 1000000 "نیاز به تأیید مدیر" ""</td><td>متن شرطی</td></tr>
<tr><td>= { REF a } * 1.09 \# "#,##0"</td><td>محاسبه (مثلاً مالیات) با قالب عدد</td></tr>
<tr><td>FILLIN "نام مشتری؟"</td><td>هنگام باز شدن قالب می‌پرسد</td></tr>
<tr><td>INCLUDETEXT "مسیر" بوک‌مارک</td><td>درج زنده‌ی بخشی از فایل دیگر</td></tr>
</tbody></table>
<h3>بوک‌مارک</h3>
<p>متن را انتخاب کنید ← Insert ← <strong>Bookmark</strong> ← نام (بدون فاصله، با حرف شروع شود). با Options ← Advanced ← Show bookmarks، کروشه‌های خاکستری دیده می‌شوند. کاربرد: هدف لینک داخلی، REF برای تکرار متن، محدوده برای TOC \b و Page range نمایه، Go To سریع (Ctrl+G ← Bookmark). بوک‌مارک‌های با «_» در ابتدا پنهان‌اند (Hidden bookmarks) و Word خودش برای Cross-reference‌ها می‌سازد؛ پاکشان نکنید.</p>
<h3>لینک (Ctrl+K)</h3>
<p>Insert ← Link: به وب‌سایت، به فایل، به ایمیل، یا <strong>Place in This Document</strong> (Heading ها و بوک‌مارک‌ها). ScreenTip متن راهنمای هاور را تعیین می‌کند. Style <strong>Hyperlink</strong> و <strong>FollowedHyperlink</strong> ظاهرش را کنترل می‌کند (برای چاپ، آبی و زیرخط را بردارید). Ctrl+Shift+F9 روی لینک، آن را به متن ساده تبدیل می‌کند. Options ← Advanced ← «Use CTRL + Click to follow hyperlink» را خاموش کنید اگر کلیک ساده می‌خواهید.</p>
<h3>قفل، جدا کردن، به‌روزرسانی</h3>
<ul>
<li><strong>Ctrl+F11</strong> فیلد را قفل می‌کند (دیگر با F9 به‌روز نمی‌شود — تاریخ ثابت روی نامه). Ctrl+Shift+F11 باز می‌کند.</li>
<li><strong>Ctrl+Shift+F9</strong> فیلد را به نتیجه‌ی ثابت تبدیل می‌کند (Unlink) — بازگشت‌ناپذیر.</li>
<li>F11 / Shift+F11: پرش به فیلد بعدی/قبلی.</li>
<li>Options ← Advanced ← Field shading: Always.</li>
</ul>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>فیلدها تودرتو می‌شوند: <code>{ IF { PAGE } = { NUMPAGES } "صفحه‌ی آخر" "ادامه دارد" }</code> در پاورقی؛ هر جفت آکولاد با Ctrl+F9 جداگانه.</li>
<li>قالب تاریخ شمسی: Word با تنظیم Calendar type در Insert Date & Time (وقتی زبان فارسی نصب است) تاریخ هجری شمسی می‌دهد؛ در کد فیلد به‌صورت <code>DATE \@ "yyyy/MM/dd" \h</code> (سوییچ \h تقویم هجری قمری و \s در بعضی نسخه‌ها شمسی).</li>
<li>سوییچ <code>\* MERGEFORMAT</code> قالب‌بندی دستی نتیجه را بعد از به‌روزرسانی نگه می‌دارد؛ <code>\* CHARFORMAT</code> قالب اولین کاراکتر کد را به کل نتیجه می‌دهد.</li>
<li><code>\* Upper</code>، <code>\* FirstCap</code>، <code>\* CardText</code> (عدد به حروف — فقط انگلیسی)، <code>\* Roman</code> برای قالب نتیجه.</li>
<li>ویژگی سفارشی سند (File ← Info ← Advanced Properties ← Custom) مثل «شماره قرارداد» را با DOCPROPERTY بخوانید؛ برای اسناد کنترل‌شده‌ی ISO ایده‌آل است.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۶ ─────────────────────────────
        {
            "title": "فصل ۶: بازبینی، همکاری، امنیت سند و Mail Merge",
            "lessons": [
                {
                    "title": "Track Changes حرفه‌ای: نماهای Markup، قفل با رمز، فیلتر بازبین‌ها و پذیرش گروهی",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>ویرایش قابل پیگیری</h2>
<p><strong>Ctrl+Shift+E</strong> یا Review ← Track Changes. از این لحظه هر درج، حذف، جابه‌جایی و تغییر قالب با نام شما و زمان ثبت می‌شود. نام شما از Options ← General ← User name می‌آید؛ تیک «Always use these values regardless of sign in» را بزنید تا در سیستم مشترک نام درست ثبت شود.</p>
<h3>چهار نمای نمایش (Display for Review)</h3>
<table><thead><tr><th>نما</th><th>چه می‌بینید</th></tr></thead><tbody>
<tr><td>Simple Markup</td><td>متن تمیز + یک خط قرمز در حاشیه؛ کلیک روی خط تغییرات را باز می‌کند</td></tr>
<tr><td>All Markup</td><td>همه‌ی تغییرات با رنگ (حذف با خط‌خورده، درج با زیرخط)</td></tr>
<tr><td>No Markup</td><td>نتیجه‌ی نهایی اگر همه پذیرفته شوند — تغییرات هنوز هست!</td></tr>
<tr><td>Original</td><td>سند قبل از تغییرات</td></tr>
</tbody></table>
<p>Show Markup ← Balloons: «Show Revisions in Balloons» تغییرات قالب و حذف‌ها را در حاشیه می‌برد؛ «Show All Revisions Inline» همه را داخل متن. برای فارسی، حالت Inline خواناتر است. Show Markup ← <strong>Specific People</strong>: فقط تغییرات یک بازبین را ببینید.</p>
<h3>Reviewing Pane</h3>
<p>Review ← Reviewing Pane (Vertical/Horizontal) فهرست همه‌ی تغییرات با شمارش (چند درج، چند حذف، چند نظر) — قبل از ارسال نهایی بررسی کنید که صفر باشد.</p>
<h3>پذیرش و رد</h3>
<p>Accept / Reject روی هر تغییر، یا فلش کنارشان: <strong>Accept All Changes</strong>، <strong>Accept All Changes Shown</strong> (فقط آن‌چه فیلتر شده — مثلاً فقط تغییرات یک نفر یا فقط تغییرات قالب‌بندی)، Accept and Move to Next. راست‌کلیک روی تغییر هم همین گزینه‌ها را دارد. ترفند: Show Markup ← فقط Formatting را روشن بگذارید ← Accept All Changes Shown؛ همه‌ی تغییرات بی‌اهمیت قالب پذیرفته می‌شوند و فقط محتوا برای بررسی می‌ماند.</p>
<h3>Lock Tracking</h3>
<p>Track Changes ← <strong>Lock Tracking</strong> ← رمز. بازبین نمی‌تواند Track Changes را خاموش کند یا تغییرات را بپذیرد؛ فقط می‌تواند ویرایش کند. برای قراردادهایی که برای مذاکره می‌فرستید ضروری است. (رمز قوی نیست؛ برای امنیت واقعی از Restrict Editing و رمز فایل استفاده کنید.)</p>
<h3>تنظیمات پیشرفته</h3>
<p>فلش گروه Tracking ← Advanced Options: رنگ هر نوع تغییر، نمایش <strong>Moves</strong> (جابه‌جایی به‌جای حذف+درج)، Track formatting را خاموش کنید تا سند شلوغ نشود، عرض Balloon و جهت حاشیه (برای فارسی: Left در نمای RTL معمولاً بهتر است).</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>«No Markup» را با «پذیرفته‌شده» اشتباه نگیرید؛ فایلی که با No Markup می‌فرستید هنوز همه‌ی تغییرات و حذف‌شده‌ها را دارد و گیرنده می‌بیند. همیشه Accept All و Document Inspector قبل از ارسال.</li>
<li>Ctrl+Shift+E روی متنی که در حال تایپ هستید، وسط جمله می‌تواند روشن/خاموش شود؛ دیگران فقط بخشی از تغییرات را می‌بینند. یک عادت خطرناک.</li>
<li>Options ← Trust Center ← Privacy Options ← «Warn before printing, saving or sending a file that contains tracked changes or comments» هشدار می‌دهد.</li>
<li>Options ← Advanced ← «Make hidden markup visible when opening or saving» را روشن نگه دارید تا هیچ‌وقت با نمای No Markup فریب نخورید.</li>
<li>برای مقایسه‌ی نسخه‌ی خودتان با متن ویرایش‌شده‌ای که بدون Track Changes برگشته: Review ← Compare (درس بعد) — همان نتیجه‌ی Track Changes را از دو فایل می‌سازد.</li>
</ul>""",
                },
                {
                    "title": "Comments مدرن، Compare و Combine: ادغام نظر چند بازبین",
                    "kind": "text",
                    "minutes": 16,
                    "is_preview": False,
                    "body": r"""<h2>نظر (Comment) به جای تغییر</h2>
<p><strong>Ctrl+Alt+M</strong> یا Review ← New Comment روی متن انتخاب‌شده. در Word 365 نظرها «modern» هستند: با <strong>@نام</strong> همکار را منشن کنید (در فایل‌های OneDrive/SharePoint برایش اعلان می‌رود)، <strong>Reply</strong> رشته‌ی گفت‌وگو می‌سازد و <strong>Resolve</strong> نظر را بایگانی می‌کند بدون حذف (Reopen ممکن است). Delete ← Delete All Comments in Document برای پاک‌سازی نهایی. Previous/Next برای پیمایش. نظرها هم در Reviewing Pane شمرده می‌شوند.</p>
<p>چاپ نظرها: File ← Print ← Print All Pages ← <strong>List of Markup</strong> فقط فهرست نظرها و تغییرات را چاپ می‌کند؛ «Print Markup» اگر تیک‌دار باشد نظرها روی سند چاپ می‌شوند — برای نسخه‌ی نهایی تیک را بردارید.</p>
<h3>Compare: چه چیزی عوض شده؟</h3>
<p>دو نسخه از یک فایل دارید (قبل و بعد از ویرایش همکار که Track Changes روشن نکرده). Review ← Compare ← <strong>Compare</strong>: Original و Revised را انتخاب کنید. Word سند سومی می‌سازد که تفاوت‌ها را به‌صورت Track Changes نشان می‌دهد؛ می‌توانید آن‌ها را یکی‌یکی بپذیرید یا رد کنید. دکمه‌ی More: چه چیزهایی مقایسه شوند (جدول، سربرگ، فیلد، قالب‌بندی، Moves) و نتیجه در سند جدید یا اصلی. به این نوع مقایسه در متون حقوقی «Legal blackline» می‌گویند.</p>
<h3>Combine: چند بازبین، یک سند</h3>
<p>سه نفر هر کدام نسخه‌ی خودشان را با Track Changes برگردانده‌اند. Review ← Compare ← <strong>Combine</strong> ← اصل + نسخه‌ی اول ← نتیجه را با نسخه‌ی دوم Combine کنید و همین‌طور ادامه دهید. حالا همه‌ی تغییرات با نام هر بازبین در یک سند است و Show Markup ← Specific People اجازه می‌دهد نظر هر فرد را جدا ببینید. Combine قالب‌بندی را فقط از یک سند نگه می‌دارد (می‌پرسد) — قبل از Combine مطمئن شوید نسخه‌ی اصلی قالب درست را دارد.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>نظر روی یک تصویر یا جدول هم می‌توان گذاشت؛ کل شیء را انتخاب کنید.</li>
<li>در Word 365، Review ← Comments ← Show Comments ← <strong>Contextual/List</strong>: حالت List همه‌ی نظرها را در پنل کناری فهرست می‌کند و فیلتر می‌کند (مثلاً فقط Unresolved).</li>
<li>متن نظرها با Find (Ctrl+H ← Special ← Comment) جست‌وجو می‌شود؛ «^a» هم نشانه‌ی Comment است.</li>
<li>Compare حتی PDF نمی‌خواند؛ اما اگر PDF را با Word باز کنید (Word آن را به docx تبدیل می‌کند) بعد می‌توانید مقایسه کنید — برای بررسی این‌که طرف مقابل در قرارداد PDF چه چیزی را عوض کرده.</li>
<li>در Compare ← More ← «Show changes at: Character level» تفاوت‌های یک حرفی (مثلاً تغییر یک رقم در مبلغ) را دقیق نشان می‌دهد؛ حالت Word level ممکن است کل کلمه را نشان دهد.</li>
</ul>""",
                },
                {
                    "title": "امنیت و پاک‌سازی: Restrict Editing، رمز، Mark as Final، Document Inspector و Accessibility Checker",
                    "kind": "text",
                    "minutes": 18,
                    "is_preview": False,
                    "body": r"""<h2>سطوح حفاظت</h2>
<table><thead><tr><th>ابزار</th><th>چه می‌کند</th><th>سطح واقعی امنیت</th></tr></thead><tbody>
<tr><td>Mark as Final</td><td>فقط یک هشدار «نهایی است»؛ با یک کلیک قابل ویرایش</td><td>هیچ — فقط اطلاع‌رسانی</td></tr>
<tr><td>Restrict Editing (Read only / Comments / Tracked changes / Filling in forms)</td><td>محدودیت با رمز؛ Exceptions بخش‌هایی را آزاد می‌گذارد</td><td>پایین — با ابزارهای ساده دور زدنی</td></tr>
<tr><td>Restrict Editing ← Formatting restrictions</td><td>فقط Style‌های مجاز؛ قالب‌بندی مستقیم ممنوع</td><td>برای حفظ قالب سازمانی عالی</td></tr>
<tr><td>Encrypt with Password (File ← Info ← Protect Document)</td><td>رمزنگاری AES کل فایل؛ بدون رمز باز نمی‌شود</td><td>بالا — رمز فراموش شود، فایل از دست رفته</td></tr>
<tr><td>Password to modify (Save As ← Tools ← General Options)</td><td>باز کردن آزاد، ذخیره روی همان فایل با رمز</td><td>پایین — Save As جدید ممکن است</td></tr>
<tr><td>Information Rights Management / Sensitivity labels</td><td>محدودیت سازمانی (چاپ، فوروارد، انقضا)</td><td>بالا — نیاز به زیرساخت Microsoft 365</td></tr>
</tbody></table>
<h3>Restrict Editing برای فرم</h3>
<p>Developer ← Content Control‌ها را بگذارید (متن، تاریخ، لیست کشویی، چک‌باکس) ← Review ← Restrict Editing ← «Allow only this type of editing: Filling in forms» ← Yes, Start Enforcing ← رمز. کاربر فقط می‌تواند کادرها را پر کند و بقیه‌ی سند دست‌نخورده می‌ماند. برای قرارداد: حالت «No changes (Read only)» + Exceptions ← بخشی که مشتری باید پر کند را انتخاب و برای Everyone آزاد کنید.</p>
<h3>Document Inspector — قبل از هر ارسال</h3>
<p>File ← Info ← Check for Issues ← <strong>Inspect Document</strong>. چیزهایی که پیدا می‌کند و اغلب فراموش می‌شوند: نظرها و Track Changes، نام نویسنده و نسخه‌های قبلی، <strong>متن پنهان</strong>، سربرگ‌ها، داده‌های XML سفارشی، مسیرهای فایل، و اطلاعات شخصی. «Remove All» روی Document Properties and Personal Information، نام نویسنده را از فایل حذف می‌کند و «Remove personal information from file properties on save» را روشن می‌کند. برای اسناد مناقصه، دادگاه و روزنامه‌نگاری این مرحله حیاتی است؛ رسوایی‌های زیادی از متادیتای Word شروع شده‌اند.</p>
<h3>Accessibility Checker</h3>
<p>Review ← <strong>Check Accessibility</strong>: تصاویر بدون Alt Text، جدول بدون Header Row، کنتراست کم، Heading‌های پرش‌دار (Heading 1 بعدش Heading 3) و متن لینک بی‌معنی («این‌جا کلیک کنید») را گزارش می‌کند. رفع این‌ها هم PDF بهتری می‌دهد، هم برای کاربران نابینا با صفحه‌خوان قابل استفاده می‌شود و هم برای موتورهای جست‌وجو. Options ← Ease of Access ← «Keep accessibility checker running while I work» یک نشانگر در نوار وضعیت می‌گذارد.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>متن پنهان (Font ← Hidden، یا Ctrl+Shift+H) در چاپ نمی‌آید ولی در فایل هست و Document Inspector آن را نشان می‌دهد. برای یادداشت‌های نویسنده مفید، برای ارسال خطرناک.</li>
<li>File ← Info ← Protect Document ← <strong>Add a Digital Signature</strong> با گواهی، سند را امضا می‌کند و هر تغییری امضا را باطل می‌کند. Insert ← Signature Line خط امضای رسمی می‌سازد.</li>
<li>هنگام ذخیره‌ی PDF، Options ← «Document properties» را بردارید تا نام نویسنده در PDF نرود؛ و «Document structure tags for accessibility» را بگذارید.</li>
<li>File ← Info ← Version History (OneDrive/SharePoint) نسخه‌های قبلی را نشان می‌دهد؛ اگر کسی سند مشترک را خراب کرد Restore کنید.</li>
<li>Options ← Trust Center ← Trusted Locations: فایل‌های این پوشه‌ها بدون Protected View باز می‌شوند؛ پوشه‌ی دانلود را هرگز Trusted نکنید.</li>
</ul>""",
                },
                {
                    "title": "هم‌نویسی در OneDrive/SharePoint، Editor و املای فارسی، ترجمه، Dictate و Read Aloud",
                    "kind": "text",
                    "minutes": 14,
                    "is_preview": False,
                    "body": r"""<h2>چند نفر، یک فایل، هم‌زمان</h2>
<p>وقتی فایل در <strong>OneDrive</strong> یا <strong>SharePoint</strong> ذخیره شده باشد (File ← Save As ← OneDrive)، دکمه‌ی <strong>Share</strong> در بالا-راست لینک با سطح دسترسی (View / Edit، با یا بدون انقضا و رمز) می‌دهد. با <strong>AutoSave</strong> روشن، همه هم‌زمان ویرایش می‌کنند و مکان‌نمای رنگی هرکس دیده می‌شود. اگر همکاری هم‌زمان قطع شد («Upload blocked»)، معمولاً یکی از افراد سند را با Word قدیمی یا با فرمت .doc باز کرده، یا ماکرو دارد. نسخه‌ی وب Word (Word for the web) همان فایل را بدون نصب باز می‌کند اما Style‌ها، فیلدها و Section‌ها را محدودتر پشتیبانی می‌کند؛ صفحه‌آرایی نهایی را همیشه در Word دسکتاپ انجام دهید.</p>
<h3>املا و دستور زبان فارسی</h3>
<p>Word با نصب زبان فارسی، غلط‌یاب املایی فارسی دارد (Review ← Spelling & Grammar، F7). Options ← Proofing: <strong>Custom Dictionaries</strong> ← New ← «واژگان شرکت.dic» با زبان Persian؛ نام محصولات و اصطلاحات را Add کنید تا خط قرمز نگیرند و بین همکاران قابل اشتراک باشد. اگر متن اصلاً بررسی نمی‌شود، متن را انتخاب کنید ← Language ← Set Proofing Language ← تیک «Do not check spelling or grammar» را بردارید (این تیک اغلب از متن کپی‌شده از وب می‌آید). Options ← Proofing ← «Check spelling as you type» را برای اسناد بلند خاموش کنید و در پایان F7 بزنید؛ سرعت بالا می‌رود.</p>
<h3>ترجمه، خواندن و دیکته</h3>
<ul>
<li>Review ← <strong>Translate</strong> ← Selection (پنل کناری، جایگزینی مستقیم) یا Document (کل سند در سند جدید). کیفیت ماشینی؛ برای فهم و پیش‌نویس.</li>
<li>Review ← <strong>Read Aloud</strong> (Ctrl+Alt+Space) متن را می‌خواند — بهترین راه برای پیدا کردن جمله‌های ناروان و کلمه‌های جاافتاده در متن خودتان. صدای فارسی باید در ویندوز نصب باشد.</li>
<li>Home ← <strong>Dictate</strong>: تایپ صوتی؛ فارسی در فهرست زبان‌های پشتیبانی‌شده هست و با میکروفون خوب دقت قابل قبولی دارد.</li>
<li>View ← <strong>Immersive Reader</strong>: فاصله‌ی متن، تمرکز خطی و رنگ صفحه برای خواندن طولانی.</li>
<li>View ← <strong>Focus</strong>: تمام‌صفحه بدون Ribbon.</li>
</ul>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>Options ← Proofing ← AutoCorrect ← تب AutoCorrect: «Correct TWo INitial CApitals» و «Capitalize first letter of sentences» را برای اسناد فارسی-انگلیسی خاموش کنید؛ باعث تغییرات ناخواسته در کدها و نام‌ها می‌شوند.</li>
<li>Review ← Language ← Language Preferences ← «Detect language automatically» را برای اسناد دوزبانه روشن نگه دارید.</li>
<li>Exclude dictionary: فایلی که کلمات <em>درست</em> اما ناخواسته را غلط علامت می‌زند (مثلاً «سایت» وقتی سازمان «وب‌گاه» می‌خواهد). در پوشه‌ی UProof با نام ExcludeDictionaryFA0429.lex.</li>
<li>Word Count (Ctrl+Shift+G) کلمات، کاراکترها و صفحات را می‌شمارد؛ در متن انتخاب‌شده فقط همان بخش را. تیک «Include textboxes, footnotes and endnotes».</li>
<li>Smart Lookup (راست‌کلیک ← Search) تعریف و جست‌وجوی وب را در پنل کناری می‌آورد بدون ترک Word.</li>
</ul>""",
                },
                {
                    "title": "Mail Merge کامل: نامه‌ی انبوه از Excel، قوانین IF، قالب اعداد و تاریخ، برچسب و ایمیل",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>یک نامه، هزار گیرنده</h2>
<p>Mail Merge سه جزء دارد: <strong>سند اصلی</strong> (نامه با جای‌خالی‌ها)، <strong>منبع داده</strong> (Excel، Outlook Contacts، Access یا فهرست داخل Word) و <strong>فیلدهای ادغام</strong>. نتیجه: هزار نامه‌ی شخصی‌سازی‌شده، برچسب پستی، پاکت یا ایمیل.</p>
<h3>گام به گام با Excel</h3>
<ol>
<li>فایل Excel: ردیف اول عنوان ستون‌ها (نام، نام‌خانوادگی، شرکت، مبلغ، تاریخ)، بدون ردیف خالی و بدون سلول ادغام‌شده. یک Sheet تمیز.</li>
<li>Mailings ← Start Mail Merge ← Letters (یا Labels/Envelopes/E-mail Messages/Directory).</li>
<li>Select Recipients ← Use an Existing List ← فایل Excel ← Sheet. <strong>Edit Recipient List</strong> برای فیلتر، مرتب‌سازی، حذف تکراری و تیک زدن گیرنده‌ها.</li>
<li>در متن، Insert Merge Field ← هر ستون در جای خودش. <strong>Address Block</strong> و <strong>Greeting Line</strong> بلوک‌های آماده‌اند؛ برای فارسی معمولاً فیلدها را دستی می‌چینیم. <strong>Match Fields</strong> اگر نام ستون‌ها با انتظار Word فرق دارد.</li>
<li><strong>Preview Results</strong> برای دیدن رکوردها یکی‌یکی. <strong>Check for Errors</strong>.</li>
<li><strong>Finish & Merge</strong> ← Edit Individual Documents (سند بزرگ با همه‌ی نامه‌ها، هر کدام در یک Section)، Print Documents، یا Send Email Messages (نیاز به Outlook؛ ستون ایمیل را انتخاب کنید؛ فرمت HTML).</li>
</ol>
<h3>قوانین (Rules)</h3>
<p>Mailings ← Rules ← <strong>If…Then…Else</strong>: اگر «جنسیت» = «زن» بنویس «سرکار خانم» وگرنه «جناب آقای». <strong>Skip Record If</strong>: رکوردهایی با مبلغ صفر رد شوند. <strong>Fill-in / Ask</strong>: هنگام ادغام بپرسد. <strong>Merge Record #</strong> شماره‌ی ترتیبی. <strong>Next Record</strong> برای چند رکورد در یک صفحه (برچسب‌ها و Directory).</p>
<h3>قالب عدد و تاریخ — دردسر اصلی</h3>
<p>Word اعداد اکسل را «خام» می‌آورد: 1250000 به‌جای ۱٬۲۵۰٬۰۰۰ و تاریخ به‌صورت 1/5/2026. راه حل، سوییچ قالب روی فیلد MERGEFIELD است. Alt+F9 بزنید و فیلد را ویرایش کنید:</p>
<ul>
<li><code>{ MERGEFIELD مبلغ \# "#,##0" }</code> → جداکننده‌ی هزارگان. <code>\# "#,##0 ریال"</code> واحد اضافه می‌کند.</li>
<li><code>{ MERGEFIELD تاریخ \@ "yyyy/MM/dd" }</code> → قالب تاریخ میلادی. برای تاریخ شمسی، ستون تاریخ در اکسل را <em>متن</em> نگه دارید (۱۴۰۵/۰۶/۲۵) تا Word دست نزند.</li>
<li>اگر اعشار عجیب می‌آید (0.10000000001)، در Options ← Advanced ← General ← <strong>Confirm file format conversion on open</strong> را روشن کنید و هنگام انتخاب منبع، «MS Excel Worksheets via DDE» را انتخاب کنید تا قالب اکسل عیناً منتقل شود (کندتر، اما دقیق).</li>
</ul>
<h3>برچسب و پاکت</h3>
<p>Start Mail Merge ← Labels ← Label vendor و شماره (یا New Label با ابعاد کاغذ برچسب ایرانی: عرض/ارتفاع هر برچسب، فاصله‌ها، تعداد در هر ردیف). Word یک جدول می‌سازد؛ فیلدها را در سلول اول بگذارید و <strong>Update Labels</strong> بزنید تا در همه تکرار شود (خودش Next Record می‌گذارد). برای فارسی، جهت جدول برچسب را RTL کنید.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>در Edit Recipient List ← Filter می‌توانید شرط‌های ترکیبی (استان = اصفهان و مبلغ &gt; ۰) بگذارید بدون تغییر اکسل.</li>
<li>Finish & Merge ← Edit Individual Documents و بعد ذخیره به PDF، همه‌ی نامه‌ها را در یک PDF می‌دهد؛ برای PDF جداگانه‌ی هر نفر ماکرو لازم است (فصل ۷) — یا سند را با Section break‌ها Split کنید.</li>
<li>سند اصلی Mail Merge وقتی باز می‌شود می‌پرسد «SQL command…»؛ Yes یعنی به اکسل وصل شود. برای قطع اتصال: Start Mail Merge ← Normal Word Document.</li>
<li>Directory (Catalog) نوعی ادغام است که همه‌ی رکوردها را پشت‌سرهم در یک صفحه می‌چیند — برای ساخت فهرست اعضا یا کاتالوگ قیمت از اکسل.</li>
<li>برای ایمیل انبوه با پیوست شخصی یا از حساب غیر از Outlook پیش‌فرض، Word به‌تنهایی کافی نیست؛ افزونه یا اسکریپت لازم است. Mail Merge ایمیلی از Outlook می‌گذرد و در Outbox می‌نشیند؛ Outlook باید باز باشد.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۷ ─────────────────────────────
        {
            "title": "فصل ۷: خودکارسازی و بهره‌وری — Find & Replace، AutoCorrect، میانبر و ماکرو",
            "lessons": [
                {
                    "title": "Find & Replace پیشرفته: کدهای ^، جست‌وجوی قالب و Wildcard برای اصلاح متن فارسی",
                    "kind": "text",
                    "minutes": 26,
                    "is_preview": False,
                    "body": r"""<h2>قوی‌ترین ابزار ویرایش Word</h2>
<p><strong>Ctrl+H</strong> پنجره‌ی Find and Replace را باز می‌کند؛ دکمه‌ی <strong>More</strong> گزینه‌های واقعی را نشان می‌دهد: Match case، Find whole words only، <strong>Use wildcards</strong>، Sounds like، Match prefix/suffix، Ignore punctuation/white-space characters، و دو منوی <strong>Format</strong> (جست‌وجو/جایگزینی بر اساس فونت، پاراگراف، Style، زبان، Highlight) و <strong>Special</strong> (کاراکترهای ویژه). کادر Find یا Replace می‌تواند خالی باشد و فقط قالب داشته باشد.</p>
<h3>کدهای ویژه (Special)</h3>
<table><thead><tr><th>کد</th><th>معنی</th><th>کد</th><th>معنی</th></tr></thead><tbody>
<tr><td>^p</td><td>پایان پاراگراف</td><td>^l</td><td>شکست خط (Shift+Enter)</td></tr>
<tr><td>^t</td><td>Tab</td><td>^m</td><td>شکست صفحه/Section (در جست‌وجو)</td></tr>
<tr><td>^s</td><td>فاصله‌ی نشکن</td><td>^w</td><td>هر نوع فاصله (یک یا چند)</td></tr>
<tr><td>^?</td><td>هر کاراکتر</td><td>^#</td><td>هر رقم</td></tr>
<tr><td>^$</td><td>هر حرف</td><td>^g</td><td>گرافیک (تصویر In Line)</td></tr>
<tr><td>^f / ^e</td><td>پاورقی / پی‌نوشت</td><td>^d</td><td>فیلد</td></tr>
<tr><td>^&amp;</td><td>در Replace: متن پیدا‌شده</td><td>^c</td><td>در Replace: محتوای Clipboard</td></tr>
<tr><td>^u8204</td><td>نیم‌فاصله (کد یونیکد دهدهی)</td><td>^u1740</td><td>«ی» فارسی (06CC)</td></tr>
</tbody></table>
<h3>پاک‌سازی‌های استاندارد متن فارسی (بدون wildcard)</h3>
<ol>
<li>«ي» عربی → «ی» فارسی: Find <code>^u1610</code> Replace <code>^u1740</code>. «ك» → «ک»: <code>^u1603</code> → <code>^u1705</code>.</li>
<li>چند فاصله‌ی پشت‌سرهم: Find <code>^w</code> (با تیک Use wildcards خاموش) Replace یک فاصله — یا با wildcard: Find <code>[ ]{2,}</code> Replace یک فاصله.</li>
<li>پاراگراف‌های خالی: Find <code>^p^p</code> Replace <code>^p</code> (چند بار تا صفر شدن نتایج).</li>
<li>«می شود» → «می‌شود»: Find <code>می </code> (می + فاصله) Replace <code>می^u8204</code> (احتیاط: «می» + فاصله در «رفتم می» هم هست؛ با Whole word بهتر).</li>
<li>فاصله قبل از نقطه و ویرگول: Find <code> .</code> Replace <code>.</code>؛ Find <code> ،</code> Replace <code>،</code>.</li>
<li>ارقام لاتین به فارسی: ده بار جایگزینی 0→۰ … 9→۹ (یا ماکرو در درس ۷-۴).</li>
</ol>
<h3>Wildcard: عبارت منظم مخصوص Word</h3>
<p>با تیک <strong>Use wildcards</strong>: <code>?</code> یک کاراکتر، <code>*</code> هر تعداد، <code>[آ-ی]</code> بازه، <code>[!0-9]</code> هرچیز جز رقم، <code>{2,}</code> تکرار، <code>&lt;</code> و <code>&gt;</code> ابتدا/انتهای کلمه، <code>@</code> یک یا بیشتر، <code>( )</code> گروه و در Replace با <code>\1</code>، <code>\2</code> به آن ارجاع می‌دهید. کاراکترهای ویژه را با <code>\</code> بگریزید (<code>\?</code>، <code>\(</code>).</p>
<table><thead><tr><th>کار</th><th>Find</th><th>Replace</th></tr></thead><tbody>
<tr><td>«نام‌خانوادگی، نام» → «نام نام‌خانوادگی»</td><td><code>([!،]@)، ([!^13]@)^13</code></td><td><code>\2 \1^p</code></td></tr>
<tr><td>حذف فاصله قبل از نیم‌فاصله</td><td><code> (^u8204)</code></td><td><code>\1</code></td></tr>
<tr><td>گذاشتن گیومه فارسی به جای " "</td><td><code>"(*)"</code></td><td><code>«\1»</code></td></tr>
<tr><td>شماره‌ی ابتدای خط «1- » را حذف کن</td><td><code>^13[0-9]{1,3}- </code></td><td><code>^p</code></td></tr>
<tr><td>دو کلمه‌ی تکراری پشت‌سرهم</td><td><code>(&lt;[آ-ی]@&gt;) \1</code></td><td><code>\1</code></td></tr>
<tr><td>تاریخ 1405/06/25 → 25/06/1405</td><td><code>([0-9]{4})/([0-9]{2})/([0-9]{2})</code></td><td><code>\3/\2/\1</code></td></tr>
</tbody></table>
<p>در حالت wildcard، پایان پاراگراف را با <code>^13</code> پیدا می‌کنید و در Replace همچنان <code>^p</code> می‌نویسید. Match case خودکار فعال است.</p>
<h3>جست‌وجوی قالب</h3>
<p>Find خالی + Format ← Font ← Bold + Replace خالی + Format ← Style ← Strong: همه‌ی بولدهای دستی به Style تبدیل می‌شوند. Find: Style «Heading 1» و Replace: Style «Title» یک‌جا همه‌ی تیترهای سطح ۱ را عوض می‌کند. Find ← Format ← Highlight همه‌ی هایلایت‌ها را پیدا می‌کند و Replace با «Not Highlight» پاک می‌کند.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>Find ← <strong>Reading Highlight ← Highlight All</strong> همه‌ی نتایج را رنگی می‌کند؛ بعد پنجره را ببندید، متن‌های رنگی هنوز انتخاب‌شده‌اند و می‌توانید یک‌جا قالب بدهید یا کپی کنید (روش کلاسیک برای استخراج همه‌ی اعداد یا همه‌ی کلمات داخل گیومه به یک فایل).</li>
<li><strong>Ctrl+G</strong> (Go To): «s3p2» = صفحه‌ی ۲ از Section 3؛ «+10» = ده صفحه جلوتر؛ «%50» = وسط سند؛ Go To ← Graphic/Table/Heading/Field برای پرش بین اشیا. Ctrl+PageDown بعد از Go To همان نوع بعدی را می‌رود (دکمه‌های دوتایی زیر نوار پیمایش).</li>
<li>Replace با <code>^c</code> محتوای Clipboard (حتی تصویر یا جدول قالب‌دار) را جایگزین می‌کند — برای جایگزین کردن یک کلمه با لوگو در کل سند.</li>
<li>Find در Navigation Pane (Ctrl+F) نتایج را با متن اطراف فهرست می‌کند و روی Headings/Pages نشان می‌دهد کجاها بیشتر است.</li>
<li>محدود کردن به یک بخش: اول متن را انتخاب کنید، بعد Ctrl+H؛ Replace All فقط داخل انتخاب کار می‌کند و سپس می‌پرسد بقیه‌ی سند هم بررسی شود.</li>
</ul>""",
                },
                {
                    "title": "AutoCorrect و AutoFormat: میان‌برهای متنی، گیومه‌ی فارسی و خاموش کردن اصلاح‌های مزاحم",
                    "kind": "text",
                    "minutes": 14,
                    "is_preview": False,
                    "body": r"""<h2>AutoCorrect: تایپ کم، متن زیاد</h2>
<p>Options ← Proofing ← <strong>AutoCorrect Options</strong>. تب AutoCorrect جدولی از «Replace → With» است. علاوه بر اصلاح غلط‌های رایج، می‌توانید <strong>میان‌بر متنی</strong> بسازید: «/شرکت» → «شرکت توسعه هوشمند فرش ایرانیان»، «/تلفن» → شماره‌ی کامل، «/سلام» → پاراگراف احوال‌پرسی رسمی. علامت «/» یا «؛؛» در ابتدا مانع می‌شود کلمه‌ی عادی تصادفاً جایگزین شود. تیک «Formatted text» متن قالب‌دار (لوگو، جدول) را هم ذخیره می‌کند — اما بهتر است برای محتوای بزرگ از AutoText (فصل ۳) استفاده کنید؛ AutoCorrect در همه‌ی برنامه‌های Office مشترک است و فایلش (.acl) حجیم می‌شود.</p>
<h3>خاموش کردن اصلاح‌های مزاحم</h3>
<ul>
<li>Capitalize first letter of sentences، Correct TWo INitial CApitals، Capitalize names of days: برای متن فارسی/فنی خاموش.</li>
<li>Replace text as you type: اگر «(c)» را © می‌کند یا «-->» را → ، مورد را از جدول حذف کنید نه کل گزینه را.</li>
<li>Exceptions: کلماتی که بعدشان جمله جدید نیست («مثلاً.» یا مخفف‌ها).</li>
</ul>
<h3>AutoFormat As You Type</h3>
<p>تب دوم. رفتارهای زنده هنگام تایپ:</p>
<table><thead><tr><th>گزینه</th><th>چه می‌کند</th><th>توصیه</th></tr></thead><tbody>
<tr><td>"Straight quotes" with "smart quotes"</td><td>" را به “ ” تبدیل می‌کند</td><td>برای فارسی خاموش و در AutoCorrect: <code>"</code> → <code>«</code> با ترفند جفت (پایین)</td></tr>
<tr><td>Hyphens (--) with dash (—)</td><td>دو خط‌تیره → خط‌تیره‌ی بلند</td><td>روشن؛ برای فارسی مفید</td></tr>
<tr><td>Internet and network paths with hyperlinks</td><td>آدرس‌ها لینک می‌شوند</td><td>خاموش برای اسناد چاپی</td></tr>
<tr><td>Automatic bulleted/numbered lists</td><td>تایپ «1.» لیست می‌سازد</td><td>سلیقه‌ای؛ اگر آزاردهنده است خاموش</td></tr>
<tr><td>Border lines</td><td>سه بار --- یا === خط می‌کشد</td><td>خاموش؛ حذفش سخت است (Borders ← No Border)</td></tr>
<tr><td>Tables</td><td>+---+---+ جدول می‌سازد</td><td>خاموش</td></tr>
<tr><td>Format beginning of list item like the one before it</td><td>بولد ابتدای آیتم‌ها را تکرار می‌کند</td><td>روشن</td></tr>
<tr><td>Set left- and first-indent with tabs and backspaces</td><td>Tab ابتدای پاراگراف تورفتگی می‌سازد</td><td>خاموش؛ تورفتگی در Style</td></tr>
</tbody></table>
<h3>گیومه‌ی فارسی خودکار</h3>
<p>در تب AutoCorrect دو مدخل بسازید: Replace <code>"«</code>... راه ساده‌تر: Replace <code>,,</code> With <code>«</code> و Replace <code>..</code> With <code>»</code>؟ خیر — «..» با پایان جمله تداخل دارد. عملی‌ترین روش: کیبورد استاندارد فارسی (Shift+K / Shift+L) و در پایان کار Find & Replace با wildcard <code>"(*)"</code> → <code>«\1»</code> برای متن‌هایی که با گیومه‌ی لاتین آمده‌اند.</p>
<h3>Math AutoCorrect</h3>
<p>تب سوم؛ تایپ <code>\alpha</code>، <code>\sum</code>، <code>\ne</code>، <code>\le</code>، <code>\rightarrow</code> → α ∑ ≠ ≤ →. با تیک «Use Math AutoCorrect rules outside of math regions» در متن عادی هم کار می‌کند — سریع‌ترین راه تایپ نمادهای فنی در گزارش مهندسی.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>بلافاصله بعد از یک اصلاح خودکار ناخواسته، <strong>Ctrl+Z</strong> فقط اصلاح را برمی‌گرداند و تایپ شما را نگه می‌دارد.</li>
<li>مدخل‌های AutoCorrect در فایل MSO####.acl (شماره = زبان) در پوشه‌ی AppData\Roaming\Microsoft\Office ذخیره می‌شوند؛ آن را به سیستم جدید کپی کنید تا همه‌ی میان‌برهایتان منتقل شود. مدخل‌های Formatted text در Normal.dotm هستند.</li>
<li>Options ← Proofing ← AutoCorrect ← تب <strong>Actions</strong>: منوی راست‌کلیک هوشمند روی تاریخ و آدرس.</li>
<li>تب <strong>AutoFormat</strong> (نه As You Type) فقط با دستور Format ← AutoFormat اجرا می‌شود که در Ribbon نیست؛ آن را به QAT اضافه کنید تا متن خام کپی‌شده را یک‌جا تمیز کند (لیست‌سازی، Style تیترها، حذف پاراگراف خالی).</li>
<li>در AutoCorrect می‌توانید مدخلی بسازید که یک کلمه‌ی غلط سازمانی («انظباط») را همیشه به درست («انضباط») تبدیل کند — و با اشتراک .acl، کل تیم یک‌دست می‌نویسند.</li>
</ul>""",
                },
                {
                    "title": "میانبرهای کیبورد، شخصی‌سازی Ribbon و QAT، و تعریف میانبر برای Style و نماد",
                    "kind": "text",
                    "minutes": 16,
                    "is_preview": False,
                    "body": r"""<h2>جدول مرجع میانبرها</h2>
<table><thead><tr><th>دسته</th><th>میانبر</th><th>کار</th></tr></thead><tbody>
<tr><td rowspan="6">قالب‌بندی</td><td>Ctrl+B / I / U</td><td>بولد / ایتالیک / زیرخط</td></tr>
<tr><td>Ctrl+Shift+&gt; / &lt;</td><td>بزرگ/کوچک کردن فونت پله‌ای؛ Ctrl+] و Ctrl+[ یک واحد</td></tr>
<tr><td>Ctrl+= / Ctrl+Shift+=</td><td>زیرنویس / بالانویس</td></tr>
<tr><td>Ctrl+L / E / R / J</td><td>چپ‌چین / وسط / راست‌چین / Justify</td></tr>
<tr><td>Ctrl+1 / 2 / 5</td><td>فاصله‌ی خط ۱ / ۲ / ۱٫۵</td></tr>
<tr><td>Ctrl+0 (صفر)</td><td>افزودن/حذف فاصله‌ی قبل از پاراگراف (۱۲pt)</td></tr>
<tr><td rowspan="5">Style و ساختار</td><td>Ctrl+Alt+1/2/3</td><td>Heading 1/2/3</td></tr>
<tr><td>Ctrl+Shift+N</td><td>Normal</td></tr>
<tr><td>Ctrl+Shift+S</td><td>کادر Apply Styles</td></tr>
<tr><td>Ctrl+Space / Ctrl+Q</td><td>پاک کردن قالب کاراکتر / پاراگراف</td></tr>
<tr><td>Alt+Shift+فلش</td><td>تغییر سطح تیتر / جابه‌جایی پاراگراف</td></tr>
<tr><td rowspan="6">درج</td><td>Ctrl+Enter</td><td>شکست صفحه</td></tr>
<tr><td>Ctrl+Alt+F / D</td><td>پاورقی / پی‌نوشت</td></tr>
<tr><td>Ctrl+K</td><td>لینک</td></tr>
<tr><td>Ctrl+Alt+M</td><td>نظر</td></tr>
<tr><td>Alt+=</td><td>معادله</td></tr>
<tr><td>Ctrl+F9 / F9 / Alt+F9</td><td>فیلد جدید / به‌روزرسانی / نمایش کد</td></tr>
<tr><td rowspan="5">پیمایش و بازبینی</td><td>Ctrl+F / H / G</td><td>جست‌وجو / جایگزینی / رفتن به</td></tr>
<tr><td>Shift+F5</td><td>آخرین جای ویرایش</td></tr>
<tr><td>Ctrl+Shift+E</td><td>Track Changes</td></tr>
<tr><td>F7 / Shift+F7</td><td>غلط‌یاب / واژه‌نامه (Thesaurus)</td></tr>
<tr><td>Ctrl+Shift+8</td><td>نمایش ¶</td></tr>
<tr><td rowspan="4">فایل و پنجره</td><td>Ctrl+N / O / S / F12</td><td>جدید / باز / ذخیره / Save As</td></tr>
<tr><td>Ctrl+P / Ctrl+F2</td><td>چاپ / پیش‌نمایش</td></tr>
<tr><td>Ctrl+W / Ctrl+F6</td><td>بستن سند / سوییچ بین اسناد باز</td></tr>
<tr><td>Ctrl+Alt+S</td><td>Split پنجره</td></tr>
</tbody></table>
<h3>Ribbon و QAT خودتان</h3>
<p>Options ← <strong>Customize Ribbon</strong>: تب و گروه جدید بسازید («ابزار من»: نیم‌فاصله، Insert Caption، Update Field، AutoFormat، Spike Paste، Compare). از منوی «Choose commands from ← Commands Not in the Ribbon» ابزارهای پنهان را پیدا کنید. Options ← <strong>Quick Access Toolbar</strong> برای دکمه‌های همیشه‌دیده‌شده؛ «Show below the Ribbon» جای بیشتری می‌دهد. دکمه‌ی <strong>Import/Export</strong> همه‌ی سفارشی‌سازی‌ها را در یک فایل .exportedUI ذخیره می‌کند تا روی سیستم دیگر یا برای همکاران بازیابی شود.</p>
<h3>میانبر برای هر چیزی</h3>
<p>Options ← Customize Ribbon ← پایین صفحه <strong>Keyboard shortcuts: Customize</strong>. Categories: All Commands، Styles، Macros، Fonts، Common Symbols. مثال‌ها: Styles ← «متن اصلی» → Alt+M؛ Common Symbols ← نیم‌فاصله (اگر در فهرست نبود از Insert ← Symbol ← Shortcut Key) → Ctrl+Shift+Space دیگر لازم نیست؛ All Commands ← InsertCaption → Alt+C؛ ToggleShowAll (¶) → F10. Save changes in: Normal.dotm تا همیشگی شود، یا قالب سازمانی. اگر میانبری تداخل داشت، همان‌جا «Currently assigned to» نشان می‌دهد.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><strong>Ctrl+Alt+Plus (روی صفحه‌کلید عددی)</strong>: نشانگر به شکل چهارپر می‌شود؛ روی هر دکمه‌ی Ribbon کلیک کنید تا مستقیم پنجره‌ی تعیین میانبر برای همان فرمان باز شود.</li>
<li>Ctrl+Alt+Minus (عددی) نشانگر خط‌دار می‌دهد: کلیک روی هر دکمه، آن را از منو حذف می‌کند (احتیاط! Esc برای لغو).</li>
<li>Alt و بعد حروف KeyTips روی هر دکمه‌ی سفارشی QAT عدد می‌گذارد؛ Alt+1 تا Alt+9 برای ۹ دکمه‌ی اول.</li>
<li>Ctrl+Shift+F9 روی کل سند (Ctrl+A) همه‌ی فیلدها و لینک‌ها را به متن ثابت تبدیل می‌کند؛ Ctrl+Shift+A حروف بزرگ؛ Shift+F3 چرخش حالت حروف لاتین (کوچک/بزرگ/اول بزرگ).</li>
<li>Options ← Advanced ← «Prompt to update style» وقتی قالب پاراگرافی را عوض کردید و دوباره Style را زدید، می‌پرسد Style را به‌روز کند یا قالب دستی را پاک کند — برای یادگیری رفتار Style بسیار آموزنده است.</li>
</ul>""",
                },
                {
                    "title": "ماکرو و VBA مقدماتی: ضبط ماکرو، ویرایش کد، ماکروی فارسی‌سازی ارقام و دکمه برای آن",
                    "kind": "text",
                    "minutes": 24,
                    "is_preview": False,
                    "body": r"""<h2>کاری که هر روز تکرار می‌کنید را به Word بسپارید</h2>
<p>ماکرو مجموعه‌ای از دستورها به زبان <strong>VBA</strong> است که Word اجرا می‌کند. راه اول ساختنش، <strong>ضبط</strong> است: View ← Macros ← <strong>Record Macro</strong> (یا دکمه‌ی ضبط در نوار وضعیت). نام (بدون فاصله)، Store macro in: Normal.dotm (همه‌ی اسناد) یا این سند، و اختیاری: Assign to Button یا Keyboard. سپس هر کاری که انجام می‌دهید ضبط می‌شود (کلیک ماوس داخل متن ضبط نمی‌شود؛ با کیبورد حرکت کنید). Stop Recording. اجرا: <strong>Alt+F8</strong> ← Run.</p>
<h3>ویرایش کد: Alt+F11</h3>
<p>ویرایشگر VBA باز می‌شود. ماکروی ضبط‌شده در Modules ← NewMacros است. کد ضبط‌شده معمولاً شلوغ است؛ با کمی خواندن می‌توانید ساده‌اش کنید. یک نمونه‌ی کاربردی که ضبط‌کردنی نیست و باید نوشت — تبدیل ارقام لاتین به فارسی در کل سند:</p>
<pre><code class="language-vba">Sub ArghamFarsi()
    Dim i As Integer
    Dim latin As String, farsi As String
    latin = "0123456789"
    farsi = ChrW(1776) &amp; ChrW(1777) &amp; ChrW(1778) &amp; ChrW(1779) &amp; ChrW(1780) &amp; _
            ChrW(1781) &amp; ChrW(1782) &amp; ChrW(1783) &amp; ChrW(1784) &amp; ChrW(1785)
    For i = 1 To 10
        With ActiveDocument.Content.Find
            .ClearFormatting
            .Replacement.ClearFormatting
            .Text = Mid(latin, i, 1)
            .Replacement.Text = Mid(farsi, i, 1)
            .Forward = True
            .Wrap = wdFindContinue
            .MatchWildcards = False
            .Execute Replace:=wdReplaceAll
        End With
    Next i
    MsgBox "ارقام فارسی شد."
End Sub</code></pre>
<p>و نمونه‌ی دوم: پاک‌سازی استاندارد متن فارسی (ی و ک عربی، فاصله‌های تکراری، فاصله قبل از نقطه):</p>
<pre><code class="language-vba">Sub PaksaziFarsi()
    Dim pairs, i
    pairs = Array(ChrW(1610), ChrW(1740), ChrW(1603), ChrW(1705), _
                  "  ", " ", " .", ".", " ،", "،", " :", ":")
    For i = 0 To UBound(pairs) Step 2
        With ActiveDocument.Content.Find
            .ClearFormatting: .Replacement.ClearFormatting
            .Text = pairs(i): .Replacement.Text = pairs(i + 1)
            .Wrap = wdFindContinue: .MatchWildcards = False
            .Execute Replace:=wdReplaceAll
        End With
    Next i
End Sub</code></pre>
<h3>دکمه و میانبر</h3>
<p>Options ← Quick Access Toolbar ← Choose commands from: <strong>Macros</strong> ← Add ← Modify برای آیکون و نام. یا Customize Ribbon ← گروه سفارشی. میانبر: Keyboard shortcuts ← Categories: Macros. حالا Ctrl+Shift+F (مثلاً) کل سند را فارسی‌سازی می‌کند.</p>
<h3>ذخیره و امنیت</h3>
<p>ماکروی ذخیره‌شده در Normal.dotm در همه‌ی اسناد شما هست ولی با فایل ارسال نمی‌شود. ماکروی داخل سند نیاز به فرمت <strong>.docm</strong> دارد؛ docx ماکرو را دور می‌ریزد (هشدار می‌دهد). گیرنده‌ی .docm نوار زرد «Enable Content» می‌بیند؛ به‌دلیل بدافزارهای ماکرویی، فایل‌های ماکرودار از اینترنت به‌طور پیش‌فرض مسدودند (Options ← Trust Center ← Macro Settings). برای تیم، ماکروها را در یک قالب مشترک (.dotm) در پوشه‌ی Startup بگذارید (File Locations ← Startup) تا به‌عنوان Global Template همیشه بارگذاری شوند.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>در VBA Editor با <strong>F8</strong> کد را خط‌به‌خط اجرا کنید و با <strong>Ctrl+G</strong> پنجره‌ی Immediate را باز کنید؛ <code>? ActiveDocument.Paragraphs.Count</code> بلافاصله جواب می‌دهد.</li>
<li><strong>Document_Open</strong> و <strong>AutoExec</strong> نام‌های ویژه‌اند: ماکرویی با این نام هنگام باز شدن سند/Word اجرا می‌شود (و به همین دلیل ابزار بدافزار بوده‌اند).</li>
<li>ماکروی ضبط‌شده شامل Selection است (روی متن انتخابی)؛ برای کل سند از ActiveDocument.Content یا حلقه روی Paragraphs استفاده کنید.</li>
<li>برای خروجی PDF جداگانه از هر Section (بعد از Mail Merge) چند خط VBA کافی است: حلقه روی ActiveDocument.Sections، Range.ExportAsFixedFormat.</li>
<li>Organizer (فصل ۲) تب Macro Project Items دارد؛ ماکروها را مثل Style بین قالب‌ها کپی کنید. با Export File در VBA Editor هم .bas می‌گیرید.</li>
</ul>""",
                },
                {
                    "title": "اسناد بلند و سنگین: راهبرد یک فایل، Master Document (و چرا نه)، عملکرد و بازیابی",
                    "kind": "text",
                    "minutes": 16,
                    "is_preview": False,
                    "body": r"""<h2>پایان‌نامه‌ی ۳۰۰ صفحه‌ای را چطور نگه داریم؟</h2>
<p>گزینه‌ی رسمی Word برای اسناد چندفایلی، <strong>Master Document</strong> (Outline ← Show Document ← Create/Insert Subdocument) است که فصل‌ها را فایل‌های جدا نگه می‌دارد و در یک سند اصلی جمع می‌کند. با وجود جذابیت، این ابزار سابقه‌ی طولانی در خراب کردن فایل‌ها دارد و اکثر متخصصان توصیه می‌کنند از آن استفاده نکنید. راهبرد امن:</p>
<ul>
<li><strong>یک فایل</strong> با Heading‌های درست، Section‌های حداقل و تصاویر فشرده. Word تا چند صد صفحه با هزاران فیلد راحت است.</li>
<li>اگر تیم روی فصل‌های جدا کار می‌کند: هر فصل یک فایل از <em>همان قالب</em>، و در پایان Insert ← Object ← Text from File برای ادغام (یا فیلد INCLUDETEXT برای ادغام زنده).</li>
<li>نسخه‌ها را با نام‌گذاری تاریخ‌دار یا Version History نگه دارید؛ نه با Track Changes ماه‌ها روشن.</li>
</ul>
<h3>سرعت</h3>
<ul>
<li>Options ← Advanced ← «Show picture placeholders» در اسناد پرتصویر.</li>
<li>Options ← Advanced ← Display ← «Disable hardware graphics acceleration» را امتحان کنید اگر اسکرول پرش دارد.</li>
<li>Options ← Proofing ← Check spelling/grammar as you type خاموش.</li>
<li>در نمای Draft کار کنید؛ صفحه‌بندی پس‌زمینه (Options ← Advanced ← Background repagination فقط در Draft قابل خاموش کردن) کندی را می‌گیرد.</li>
<li>فونت‌های جاسازی‌شده و Version History قدیمی را پاک کنید؛ Save As به نام جدید.</li>
<li>افزونه‌های Word (File ← Options ← Add-ins ← Manage COM Add-ins) اغلب علت کندی و کرش هستند؛ یکی‌یکی خاموش کنید.</li>
</ul>
<h3>وقتی فایل خراب شد</h3>
<ol>
<li>File ← Open ← فلش Open ← <strong>Open and Repair</strong>.</li>
<li>نوع فایل: <strong>Recover Text from Any File (*.*)</strong> — متن را نجات می‌دهد، قالب را نه.</li>
<li>پسوند را .zip کنید و word/document.xml را در یک ویرایشگر XML بررسی کنید؛ گاهی یک تگ ناقص است. تصاویر در word/media.</li>
<li>سند خالی جدید ← Insert ← Object ← Text from File ← فایل خراب؛ اغلب محتوا وارد می‌شود (بدون آخرین ¶ که معمولاً محل خرابی است).</li>
<li>File ← Info ← Manage Document ← Recover Unsaved Documents و پوشه‌ی AutoRecover (Options ← Save ← AutoRecover file location).</li>
</ol>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>در اسناد بلند، بیشترین خرابی از جدول‌های تودرتو، اشیای شناور روی Section break‌ها و کپی/پیست از مرورگر می‌آید. قبل از پیست، Keep Text Only.</li>
<li>Options ← Advanced ← «Allow background saves» را روشن نگه دارید و AutoRecover را ۳ دقیقه.</li>
<li>Ctrl+F6 بین اسناد باز سوییچ می‌کند؛ View ← View Side by Side و Synchronous Scrolling برای مقایسه‌ی دستی دو نسخه.</li>
<li>Word for the web برای اسناد سنگین کند است اما هیچ‌وقت کرش نمی‌کند و همیشه یک نسخه‌ی سالم در OneDrive دارید؛ به‌عنوان پشتیبان جانبی.</li>
<li>File ← Info ← «Check for Issues ← Check Compatibility» می‌گوید کدام ویژگی‌ها در نسخه‌های قدیمی Word خراب می‌شوند — قبل از ارسال به دانشگاه یا اداره‌ای که Word 2010 دارد.</li>
</ul>""",
                },
            ],
        },
        # ───────────────────────────── فصل ۸ ─────────────────────────────
        {
            "title": "فصل ۸: پروژه‌ی پایانی — قالب استاندارد گزارش و پایان‌نامه‌ی فارسی",
            "lessons": [
                {
                    "title": "آناتومی یک پایان‌نامه/گزارش استاندارد و چک‌لیست ساختار",
                    "kind": "text",
                    "minutes": 14,
                    "is_preview": False,
                    "body": r"""<h2>از صفحه‌ی عنوان تا پیوست</h2>
<p>پیش از ساختن قالب باید بدانیم چه چیزی می‌سازیم. ساختار رایج پایان‌نامه و گزارش فنی فارسی (شیوه‌نامه‌ی دانشگاه‌ها و سازمان‌ها جزئیات را تغییر می‌دهد، اسکلت ثابت است):</p>
<table><thead><tr><th>بخش</th><th>شماره‌گذاری صفحه</th><th>در فهرست؟</th><th>Section</th></tr></thead><tbody>
<tr><td>صفحه‌ی عنوان (فارسی)</td><td>بدون شماره (شمرده می‌شود)</td><td>خیر</td><td rowspan="2">1</td></tr>
<tr><td>بسم‌الله، تأییدیه‌ی هیئت داوران، تعهدنامه، تقدیم، سپاس‌گزاری</td><td>بدون شماره</td><td>خیر</td></tr>
<tr><td>چکیده‌ی فارسی</td><td rowspan="2">حروف ابجد یا الف، ب، پ… (یا رومی)</td><td>بله (سطح ۱ بدون شماره‌ی فصل)</td><td rowspan="2">2</td></tr>
<tr><td>فهرست مطالب، فهرست جدول‌ها، فهرست شکل‌ها، فهرست علائم</td><td>عنوان‌ها بله، خودشان نه</td></tr>
<tr><td>فصل ۱ … فصل n</td><td>۱، ۲، ۳ … از فصل ۱</td><td>بله (سه سطح)</td><td>3</td></tr>
<tr><td>منابع و مراجع</td><td rowspan="2">ادامه‌ی عددی</td><td>بله (بدون شماره‌ی فصل)</td><td rowspan="2">3 یا 4</td></tr>
<tr><td>پیوست‌ها (پیوست الف، ب…)؛ شکل‌ها با شماره‌ی «الف-۱»</td><td>بله</td></tr>
<tr><td>چکیده و صفحه‌ی عنوان انگلیسی (از انتها، LTR)</td><td>بدون شماره</td><td>خیر</td><td>آخر (LTR)</td></tr>
</tbody></table>
<h3>چک‌لیست تصمیم‌ها قبل از شروع</h3>
<ul>
<li>فونت فارسی و لاتین و اندازه‌ها برای: متن اصلی، تیتر فصل، تیتر بخش، زیرنویس شکل/جدول، پاورقی، متن جدول، منابع.</li>
<li>فاصله‌ی خطوط (۱٫۵ یا Exactly) و فاصله‌ی قبل/بعد پاراگراف؛ تورفتگی خط اول (معمولاً ۰٫۸ سانتی‌متر، جز پاراگراف اول هر بخش).</li>
<li>حاشیه‌ها (بالا ۳، پایین ۲٫۵، راست ۳٫۵ برای صحافی، چپ ۲٫۵ — نمونه) و جای شماره‌ی صفحه (پایین وسط یا پایین چپ).</li>
<li>قالب شماره‌گذاری: فصل «۱-۲-۳»، شکل «شکل ۲-۳»، جدول «جدول ۲-۱» بالای جدول، رابطه «(۲-۱)» سمت چپ.</li>
<li>شیوه‌ی مرجع‌دهی: عددی [۱] (IEEE) یا نویسنده-سال (APA).</li>
<li>هر فصل از صفحه‌ی فرد (راست) شروع شود؟ (چاپ دورو) یا فقط از صفحه‌ی جدید؟</li>
</ul>
<p>در سه درس بعد این تصمیم‌ها را به Style، Section، فیلد و در نهایت یک فایل .dotx تبدیل می‌کنیم که هر بار با آن شروع کنید.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>عنوان‌های «چکیده»، «منابع» و «پیوست الف» را با Heading 1 بنویسید اما شماره‌ی فصل نگیرند: یک Style جدید «عنوان بدون شماره» بر پایه‌ی Heading 1 با Numbering: None و Outline level 1 بسازید؛ در TOC مثل بقیه می‌آید.</li>
<li>برای شماره‌ی شکل در پیوست («الف-۱»)، در Style «عنوان پیوست» شماره‌گذاری حروفی تعریف کنید و در Caption ← Numbering ← Chapter starts with style = عنوان پیوست.</li>
<li>بخش انگلیسی انتهای پایان‌نامه یک Section مستقل با جهت LTR، حاشیه‌ی آینه‌ای برعکس و سربرگ جداست؛ Link to Previous خاموش.</li>
<li>بسیاری از دانشگاه‌ها قالب Word رسمی می‌دهند؛ حتی اگر ناقص باشد، Style‌های آن را نگه دارید و اصلاح کنید — داوران به نام Style‌ها اهمیتی نمی‌دهند، به ظاهر یکنواخت اهمیت می‌دهند.</li>
</ul>""",
                },
                {
                    "title": "ساخت قالب گام‌به‌گام: Style‌های فارسی، شماره‌گذاری پیوندی، Section‌ها و سربرگ",
                    "kind": "text",
                    "minutes": 30,
                    "is_preview": False,
                    "body": r"""<h2>گام ۱: سند خالی و تنظیمات پایه</h2>
<ol>
<li>Ctrl+N. Layout ← Page Setup: A4، حاشیه‌ها طبق چک‌لیست، Gutter 0 (حاشیه‌ی صحافی را در خود حاشیه‌ی راست گذاشتیم)، Mirror margins اگر دورو.</li>
<li>Options ← Advanced ← Numeral: Context. Options ← Language: Persian.</li>
<li>Style <strong>Normal</strong> را Modify کنید: Right-to-Left، Justify، Complex script = B Nazanin 14، Latin = Times New Roman 12، Line spacing Multiple 1.15 (یا Exactly 21pt)، Spacing After 6pt، First line indent 0.8cm. این پایه‌ی همه است.</li>
</ol>
<h2>گام ۲: Style‌های اصلی</h2>
<table><thead><tr><th>Style</th><th>Based on</th><th>ویژگی‌های کلیدی</th><th>Next</th></tr></thead><tbody>
<tr><td>Heading 1 (تیتر فصل)</td><td>Normal</td><td>B Titr 18، وسط‌چین، Page break before، Space after 24pt، Keep with next، بدون تورفتگی</td><td>متن اصلی</td></tr>
<tr><td>Heading 2 (تیتر بخش)</td><td>Normal</td><td>B Titr 14، راست‌چین، Space before 18 / after 6، Keep with next</td><td>متن اصلی</td></tr>
<tr><td>Heading 3</td><td>Normal</td><td>B Nazanin Bold 14، Space before 12</td><td>متن اصلی</td></tr>
<tr><td>متن اصلی</td><td>Normal</td><td>همان Normal (ممکن است صرفاً از Normal استفاده کنید)</td><td>خودش</td></tr>
<tr><td>پاراگراف اول</td><td>متن اصلی</td><td>First line indent 0 (بعد از تیتر)</td><td>متن اصلی</td></tr>
<tr><td>Caption (زیرنویس)</td><td>Normal</td><td>B Nazanin Bold 12، وسط‌چین، بدون تورفتگی، Space before 6 / after 12؛ برای عنوان جدول نسخه‌ای با Keep with next</td><td>متن اصلی</td></tr>
<tr><td>تصویر</td><td>Normal</td><td>وسط‌چین، بدون تورفتگی، Keep with next، Space before 12</td><td>Caption</td></tr>
<tr><td>متن جدول</td><td>Normal</td><td>B Nazanin 12، Single، Space 0، بدون تورفتگی</td><td>خودش</td></tr>
<tr><td>Footnote Text</td><td>Normal</td><td>LTR، چپ‌چین، Times 10 / B Nazanin 11، Single</td><td>خودش</td></tr>
<tr><td>Bibliography / منابع</td><td>Normal</td><td>Hanging indent 1cm، بدون تورفتگی خط اول، Space after 6</td><td>خودش</td></tr>
<tr><td>عنوان بدون شماره</td><td>Heading 1</td><td>Numbering: None</td><td>متن اصلی</td></tr>
<tr><td>TOC 1 / TOC 2 / TOC 3</td><td>Normal</td><td>RTL، بدون تورفتگی خط اول؛ TOC 1 بولد؛ TOC 2 و 3 تورفتگی راست 0.8 و 1.6cm؛ Tab stop شماره‌ی صفحه با leader نقطه</td><td>—</td></tr>
</tbody></table>
<h2>گام ۳: شماره‌گذاری پیوندی</h2>
<p>روی یک پاراگراف Heading 1 ← Multilevel List ← Define New Multilevel List ← More. سطح ۱: Link to Heading 1، قالب «فصل ۱» (متن «فصل » + شماره)، Number style: 1,2,3، Number alignment: Centered. سطح ۲: Link to Heading 2، Include level 1 + «-» + شماره → «۱-۱»؛ Follow number with: Space. سطح ۳ به همین ترتیب «۱-۱-۱». Legal style numbering خاموش. برای این‌که شماره‌ها فارسی نمایش داده شوند، Numeral = Context و پاراگراف RTL کافی است.</p>
<h2>گام ۴: Section‌ها و صفحات آغازین</h2>
<ol>
<li>صفحه‌ی عنوان را با Vertical alignment: Center بسازید (Page Setup ← Layout ← Apply to This section). Insert ← Quick Parts ← Document Property برای عنوان، نویسنده، استاد راهنما (Custom properties).</li>
<li>Layout ← Breaks ← Section Next Page. صفحات تأییدیه/تقدیم.</li>
<li>Section جدید: چکیده با Style «عنوان بدون شماره»؛ سپس فهرست مطالب (TOC سفارشی، سه سطح، Style‌های «عنوان بدون شماره» و «عنوان پیوست» در Options به سطح ۱)، فهرست جدول‌ها (Table of Figures ← جدول)، فهرست شکل‌ها. Page Number Format: الف، ب، پ… Start at الف.</li>
<li>Section جدید (Odd Page اگر دورو): فصل ۱. Page Number Format: 1,2,3، <strong>Start at 1</strong>، Link to Previous خاموش برای Header و Footer.</li>
<li>Section پایانی LTR برای چکیده‌ی انگلیسی.</li>
</ol>
<h2>گام ۵: سربرگ و پاورقی</h2>
<p>Footer فصل‌ها: شماره‌ی صفحه وسط (فیلد PAGE، فونت فارسی). Header فرد: <code>{ STYLEREF "Heading 1" }</code> راست‌چین؛ زوج: <code>{ STYLEREF "Heading 2" }</code>. Different First Page روشن تا صفحه‌ی اول هر فصل سربرگ نداشته باشد. صفحات آغازین Footer با شماره‌ی حروفی و بدون Header.</p>
<h2>گام ۶: Caption، ارجاع و منابع</h2>
<p>Insert Caption ← New Label «شکل» و «جدول» و «رابطه» ← Numbering ← Include chapter number با Heading 1 و جداکننده «-». چند شکل و جدول نمونه بگذارید و با Cross-reference به آن‌ها ارجاع دهید تا کاربر قالب الگو ببیند. References ← Style: IEEE یا APA و یک منبع نمونه + Bibliography با عنوان «منابع» (Style «عنوان بدون شماره»).</p>
<h2>گام ۷: ذخیره به‌عنوان قالب</h2>
<p>متن‌های نمونه را با راهنمای «[این‌جا بنویسید]» جایگزین کنید، Ctrl+A ← F9، File ← Save As ← Word Template (.dotx) با نام «قالب پایان‌نامه». از این پس File ← New ← Personal.</p>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>برای شماره‌های فارسی در Caption‌ها و TOC حتی روی سیستم‌هایی که Numeral روی Arabic است، فونت Complex script را روی فونتی بگذارید که ارقام لاتین را به شکل فارسی رسم می‌کند (خانواده‌ی «B» مثل B Nazanin این کار را می‌کند) — راه‌حل کلاسیک تایپیست‌ها.</li>
<li>Style Set و Theme را از تب Design با نام قالب ذخیره کنید تا در اکسل/پاورپوینت دفاعیه هم یکسان باشد.</li>
<li>در Style Heading 1، Page break before را بگذارید اما Section break نگذارید؛ برای هر فصل Section لازم نیست، StyleRef سربرگ را زنده نگه می‌دارد.</li>
<li>در قالب، Document Inspector را اجرا کنید تا اطلاعات نویسنده‌ی شما با قالب به دیگران نرود.</li>
<li>Restrict Editing ← Formatting restrictions ← فقط Style‌های قالب مجاز باشند: کاربران نمی‌توانند قالب‌بندی مستقیم بزنند و سند تا انتها تمیز می‌ماند (بدون رمز هم می‌شود؛ فقط بازدارنده است).</li>
</ul>""",
                },
                {
                    "title": "کلینیک مشکلات رایج: تصویر می‌پرد، فهرست به‌روز نمی‌شود، شماره اشتباه است، فونت عوض شد",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": r"""<h2>تشخیص و درمان</h2>
<table><thead><tr><th>علامت</th><th>علت رایج</th><th>درمان</th></tr></thead><tbody>
<tr><td>تصویر جای دیگری می‌رود یا روی متن می‌افتد</td><td>Wrap شناور با لنگر روی پاراگرافی که جابه‌جا شده</td><td>Layout Options ← In Line with Text؛ پاراگراف مستقل وسط‌چین (فصل ۴)</td></tr>
<tr><td>تیتر تنها در پایین صفحه مانده</td><td>Keep with next خاموش یا Enter خالی بعد از تیتر</td><td>Style تیتر ← Keep with next؛ پاراگراف‌های خالی را حذف</td></tr>
<tr><td>یک صفحه‌ی خالی وسط سند</td><td>Page break + Page break before در Style، یا Section break Next Page بعد از Page break، یا جدول تا انتهای صفحه + ¶ اجباری</td><td>¶ روشن؛ شکست اضافه را پاک؛ برای جدول انتهایی ¶ آخر را فونت ۱ یا Hidden</td></tr>
<tr><td>فهرست مطالب تیتر جدید را نشان نمی‌دهد</td><td>به‌روز نشده یا Style تیتر Heading نیست</td><td>F9 ← Update entire table؛ Style را بررسی</td></tr>
<tr><td>در فهرست، متن پاراگراف عادی آمده</td><td>پاراگراف Outline level دارد یا با Heading + قالب دستی نوشته شده</td><td>Paragraph ← Outline level: Body Text</td></tr>
<tr><td>شماره‌ی صفحه‌ی همه‌ی Section‌ها با هم عوض شد</td><td>Link to Previous روشن</td><td>در Section هدف Link to Previous را خاموش و Format Page Numbers ← Start at</td></tr>
<tr><td>شماره‌ی صفحه از ۱ شروع نمی‌شود</td><td>Continue from previous section</td><td>Format Page Numbers ← Start at 1</td></tr>
<tr><td>شماره‌ی شکل‌ها «شکل ۰-۱» است</td><td>Heading 1 شماره‌گذاری پیوندی ندارد</td><td>Multilevel List را به Heading 1 پیوند دهید</td></tr>
<tr><td>«Error! Reference source not found»</td><td>هدف ارجاع حذف شده</td><td>ارجاع را دوباره درج کنید؛ Find «Error!»</td></tr>
<tr><td>فونت‌ها در سیستم دیگر عوض شد</td><td>فونت نصب نیست</td><td>Embed fonts یا PDF بفرستید؛ Options ← Advanced ← Font Substitution نشان می‌دهد چه جایگزین شده</td></tr>
<tr><td>ارقام در سیستم دیگر لاتین شد</td><td>Numeral = Context فقط نمایشی است</td><td>ارقام را واقعاً فارسی تایپ/تبدیل کنید (ماکرو فصل ۷) یا PDF</td></tr>
<tr><td>فاصله‌های عجیب در خط آخر پاراگراف</td><td>Justify + Shift+Enter</td><td>Options ← Advanced ← Layout ← Don't expand character spaces on a line ending with Shift+Return</td></tr>
<tr><td>Heading با شماره اما شماره‌ها ترتیب ندارند (۱، ۱، ۱)</td><td>چند لیست مستقل؛ کپی از اسناد دیگر</td><td>روی شماره راست‌کلیک ← Continue Numbering؛ یا Multilevel List را دوباره اعمال</td></tr>
<tr><td>سند به‌شدت کند است</td><td>تصاویر بزرگ، Track Changes قدیمی، افزونه</td><td>Compress Pictures، Accept All، Add-ins خاموش، Save As جدید</td></tr>
<tr><td>پرانتز و نقطه در جای غلط</td><td>پاراگراف LTR که فقط راست‌چین شده، یا کاراکتر جهت‌دار در متن</td><td>Ctrl+Shift راست؛ متن را Keep Text Only دوباره پیست کنید</td></tr>
<tr><td>PDF فارسی حروف جدا یا مربع نشان می‌دهد</td><td>PDF با پرینتر مجازی قدیمی ساخته شده، یا فونت بدون جاسازی</td><td>File ← Save As ← PDF (موتور داخلی Word)؛ فونت استاندارد</td></tr>
<tr><td>Track Changes خودش روشن می‌شود</td><td>Lock Tracking یا قالب</td><td>Review ← Lock Tracking ← رمز؛ یا در Normal.dotm خاموش کنید</td></tr>
<tr><td>Word هنگام باز کردن فایل کرش می‌کند</td><td>Normal.dotm خراب یا افزونه</td><td>Word را با winword /safe اجرا؛ Normal.dotm را تغییر نام دهید</td></tr>
</tbody></table>
<h3>روش کلی عیب‌یابی</h3>
<ol>
<li>¶ را روشن کنید. ۸۰٪ مشکلات با دیدن کاراکترهای نامرئی معلوم می‌شود.</li>
<li>Style Inspector / Reveal Formatting (Shift+F1) روی متن مشکل‌دار.</li>
<li>Alt+F9 برای دیدن فیلدها؛ Ctrl+A ← F9.</li>
<li>نوار وضعیت: در کدام Section هستید؟</li>
<li>در بدترین حالت: کل متن را به یک سند جدید از قالب سالم منتقل کنید (Keep Text Only) و Style‌ها را دوباره بزنید — سریع‌تر از ساعت‌ها جست‌وجوی ایراد.</li>
</ol>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li><code>winword /a</code> Word را بدون هیچ افزونه و قالبی اجرا می‌کند؛ <code>winword /safe</code> حالت امن. در Run ویندوز تایپ کنید.</li>
<li>Options ← Advanced ← Compatibility options ← «Lay out this document as if created in» می‌تواند صفحه‌بندی فایل‌های قدیمی را دقیقاً حفظ کند یا به‌روز کند؛ اگر فایل قدیمی بعد از تبدیل صفحه‌بندی‌اش تغییر کرد، همین‌جاست.</li>
<li>Options ← Advanced ← Font Substitution ← Convert Permanently فونت جایگزین را دائمی می‌کند تا هر بار پیام ندهد.</li>
<li>اگر ارقام داخل جدول‌های کپی‌شده از اکسل فارسی نمی‌شوند، سلول‌ها را انتخاب و جهت پاراگراف را RTL کنید؛ اکسل پاراگراف‌ها را LTR می‌فرستد.</li>
<li>هنگام ارسال به دانشگاه، هم docx هم PDF بفرستید و در ایمیل بنویسید PDF مرجع است؛ داور روی docx با فونت ناقص قضاوت نمی‌کند.</li>
</ul>""",
                },
                {
                    "title": "خروجی نهایی: PDF/A با بوک‌مارک و لینک، چاپ کتابچه و دورو، و چک‌لیست تحویل",
                    "kind": "text",
                    "minutes": 16,
                    "is_preview": False,
                    "body": r"""<h2>PDF درست</h2>
<p>File ← Save As ← نوع فایل PDF (یا File ← Export ← Create PDF/XPS). دکمه‌ی <strong>Options</strong> مهم‌ترین بخش است:</p>
<ul>
<li><strong>Page range</strong>: همه، صفحه‌ی جاری، یا محدوده (برای فرستادن یک فصل).</li>
<li><strong>Publish what</strong>: Document (بدون Track Changes و نظر) در برابر Document showing markup.</li>
<li><strong>Create bookmarks using: Headings</strong> ← پنل نشانک‌های PDF از Heading‌ها ساخته می‌شود؛ خواننده در Acrobat فهرست کناری دارد.</li>
<li><strong>Document properties</strong>: عنوان و نویسنده به PDF می‌رود — برای ناشناس‌ماندن تیک را بردارید.</li>
<li><strong>Document structure tags for accessibility</strong>: روشن؛ PDF قابل خواندن با صفحه‌خوان و قابل جست‌وجو.</li>
<li><strong>PDF/A compliant</strong> (ISO 19005-1): برای آرشیو بلندمدت و بعضی سامانه‌های دانشگاهی؛ فونت‌ها کامل جاسازی می‌شوند، لینک‌ها و شفافیت محدود.</li>
<li><strong>Bitmap text when fonts may not be embedded</strong>: اگر فونتی اجازه‌ی جاسازی ندهد، متن به تصویر تبدیل می‌شود (حجیم، غیرقابل جست‌وجو) — فونت را عوض کنید.</li>
<li>Optimize for: <strong>Standard</strong> برای چاپ، Minimum size برای ایمیل.</li>
</ul>
<p>لینک‌های داخلی (TOC با \h، ارجاع‌ها با Insert as hyperlink، Ctrl+K) در PDF زنده می‌مانند. پیش از خروجی: Ctrl+A ← F9، Accept All، Document Inspector، Accessibility Checker، و «Update fields before printing» روشن.</p>
<h3>چاپ</h3>
<p>Ctrl+P. گزینه‌ها: Print One Sided / <strong>Print on Both Sides</strong> (Flip on long edge برای پرتره)، Collated، Pages: «s2-s4» (Section‌ها)، «p1s3-p5s3»، یا «1-5, 12, 20-» ؛ <strong>Pages per sheet</strong> (۲ صفحه در یک برگ برای پیش‌نویس)، Scale to paper size (A4 → A5). Print Markup را برای نسخه‌ی نهایی خاموش کنید. Page Setup ← Multiple pages: Book fold و بعد چاپ دورو، کتابچه‌ی آماده‌ی تا زدن می‌دهد. Print ← Printer Properties برای انتخاب سینی و کیفیت.</p>
<h3>دیگر خروجی‌ها</h3>
<ul>
<li><strong>docx برای ویرایش دیگران</strong>: فونت جاسازی‌شده؛ فیلدها را نگه دارید؛ Compatibility Checker.</li>
<li><strong>Plain text / Markdown</strong>: Save As ← Plain Text (UTF-8 را انتخاب کنید تا فارسی سالم بماند). برای HTML، «Web Page, Filtered» تمیزتر از «Web Page» است.</li>
<li><strong>تصویر از یک صفحه</strong>: Insert ← Screenshot در سند دیگر، یا PDF را در ابزار دیگر به PNG تبدیل کنید؛ Word خودش «Save as picture» برای صفحه ندارد.</li>
<li><strong>ارسال</strong>: File ← Share ← Email as attachment / PDF.</li>
</ul>
<h3>چک‌لیست تحویل نهایی</h3>
<ol>
<li>Track Changes: Accept All؛ نظرها حذف. Reviewing Pane = صفر.</li>
<li>Ctrl+A ← F9؛ سربرگ‌ها جداگانه F9؛ فهرست‌ها Update entire table.</li>
<li>Find «Error!» و Find «[» برای جای‌خالی‌های راهنما.</li>
<li>F7 غلط‌یاب فارسی و انگلیسی؛ Read Aloud برای بخش‌های مهم.</li>
<li>Accessibility Checker: Alt Text تصاویر، Header Row جدول‌ها.</li>
<li>Document Inspector ← Remove متادیتا (مگر لازم).</li>
<li>Print Preview صفحه به صفحه: تیتر تنها، جدول شکسته، صفحه‌ی خالی، شماره‌گذاری Section‌ها.</li>
<li>PDF با بوک‌مارک؛ باز کردن PDF در دو نمایشگر مختلف؛ بررسی فونت‌ها (File ← Properties ← Fonts در Acrobat؛ همه Embedded).</li>
<li>نام‌گذاری فایل: «پایان‌نامه_نام_۱۴۰۵-۰۶-۲۵_نهایی.pdf» — تاریخ در نام فایل از Version History ساده‌تر است.</li>
</ol>
<h3>نکته‌هایی که کمتر کسی می‌داند</h3>
<ul>
<li>File ← Print ← Print All Pages ← <strong>Document Info / Styles / AutoText / Key Assignments</strong>: چاپ مستندات Style‌ها و میانبرهای سند — برای مستندسازی قالب سازمانی.</li>
<li>Options ← Display ← <strong>Print pages in reverse order</strong> و «Use draft quality» برای چاپگرهایی که برعکس می‌چینند.</li>
<li>Options ← Advanced ← Print ← «Scale content for A4 or 8.5 x 11" paper sizes» خودکار Letter/A4 را تطبیق می‌دهد.</li>
<li>Microsoft Print to PDF (پرینتر مجازی) لینک و بوک‌مارک نمی‌سازد؛ همیشه Save As PDF داخلی Word را ترجیح دهید.</li>
<li>PDF/A اجازه‌ی لینک خارجی ندارد اما لینک داخلی و بوک‌مارک را نگه می‌دارد؛ اگر سامانه PDF/A می‌خواهد و لینک‌ها مهم‌اند، دو نسخه بدهید.</li>
</ul>""",
                },
            ],
        },
    ],
}

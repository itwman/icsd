# قالب فایل seed هر دوره

هر فایل یک ماژول پایتون است که فقط یک متغیر `COURSE` (dict) دارد. کدگذاری UTF-8.

```python
COURSE = {
    "slug": "python-basics",              # لاتین، یکتا
    "title": "آموزش پایتون",              # فارسی
    "category": "برنامه‌نویسی",           # یکی از: برنامه‌نویسی / دیتابیس / دواپس و زیرساخت / تحلیل داده / مهارت‌های اداری / مبانی
    "level": "beginner",                  # beginner | intermediate | advanced
    "summary": "یک جمله‌ی کوتاه معرفی",
    "description": "<p>چند پاراگراف HTML: این دوره برای چه کسی است، چه یاد می‌گیرید، پیش‌نیاز.</p>",
    "price": 0,                           # تومان؛ 0 یعنی رایگان
    "duration_minutes": 480,
    "tags": ["پایتون", "برنامه‌نویسی"],
    "modules": [
        {
            "title": "فصل اول: ...",
            "lessons": [
                {
                    "title": "عنوان درس",
                    "kind": "text",           # text | video
                    "minutes": 15,
                    "is_preview": True,       # فقط درس اول هر دوره True
                    "body": "<h2>...</h2><p>...</p><pre><code class=\"language-python\">...</code></pre>",
                },
            ],
        },
    ],
}
```

## قواعد محتوا
- `body` HTML معتبر؛ فقط این تگ‌ها: h2 h3 p ul ol li pre code strong em table thead tbody tr th td blockquote.
- متن فارسی روان و آموزشی (نه ترجمه‌ی ماشینی)، ۱۵۰ تا ۳۰۰ کلمه در هر درس + دست‌کم یک نمونه کد یا جدول جایی که معنا دارد.
- کد داخل `<pre><code class="language-xxx">` با escape کردن `<` `>` `&`.
- هر دوره: ۴ تا ۶ فصل، هر فصل ۳ تا ۵ درس. درس‌ها از ساده به پیچیده.
- اعداد داخل متن فارسی می‌توانند لاتین باشند (لایه‌ی نمایش تبدیل می‌کند).
- هیچ لینک بیرونی.

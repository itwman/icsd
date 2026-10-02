COURSE = {
    "slug": "docker",
    "title": "داکر",
    "category": "دواپس و زیرساخت",
    "level": "intermediate",
    "summary": "کانتینری‌سازی برنامه‌ها با داکر، از ساخت Dockerfile تا داکرایز کردن یک پروژه‌ی جنگو و دیپلوی",
    "description": """<p>این دوره برای توسعه‌دهندگانی است که پایه‌ی برنامه‌نویسی و کار با خط فرمان لینوکس را می‌دانند و می‌خواهند یاد بگیرند چطور برنامه‌های خود را در قالب کانتینر بسته‌بندی و اجرا کنند. داکر یکی از مهم‌ترین ابزارهای دنیای دواپس است که مشکل «روی سیستم من کار می‌کند!» را برای همیشه حل می‌کند.</p>
<p>در طول دوره با مفهوم image و container، نوشتن Dockerfile، مدیریت volume و network، و هماهنگ‌سازی چند سرویس با docker compose آشنا می‌شوید. بخش کاربردی دوره به داکرایز کردن یک پروژه‌ی واقعی جنگو به همراه پایگاه‌داده‌ی پستگرس اختصاص دارد و در پایان با رجیستری و روند اولیه‌ی دیپلوی کانتینرها روی سرور آشنا می‌شوید.</p>
<p>پیش‌نیاز این دوره، آشنایی مقدماتی با لینوکس و حداقل یک زبان برنامه‌نویسی (ترجیحاً پایتون) است. اگر دوره‌ی «لینوکس» یا «گیت و گیت‌هاب» را نگذرانده‌اید، پیشنهاد می‌شود ابتدا با آن‌ها آشنا شوید.</p>""",
    "price": 900000,
    "duration_minutes": 340,
    "tags": ["داکر", "کانتینر", "دواپس", "جنگو"],
    "modules": [
        {
            "title": "فصل اول: مفاهیم پایه‌ی کانتینر",
            "lessons": [
                {
                    "title": "چرا کانتینر؟ تفاوت با ماشین مجازی",
                    "kind": "text",
                    "minutes": 13,
                    "is_preview": True,
                    "body": """<h2>مشکل همیشگی: «روی سیستم من کار می‌کند»</h2>
<p>یکی از دردسرهای رایج در توسعه‌ی نرم‌افزار این است که برنامه‌ای روی سیستم یک توسعه‌دهنده به‌درستی اجرا می‌شود اما روی سرور یا سیستم همکار دیگر با خطا مواجه می‌شود؛ دلیل آن معمولاً تفاوت نسخه‌ی کتابخانه‌ها، تنظیمات سیستم‌عامل یا وابستگی‌های نصب‌نشده است. کانتینر (Container) دقیقاً همین مشکل را حل می‌کند: برنامه به همراه تمام وابستگی‌ها، کتابخانه‌ها و تنظیمات موردنیازش در یک بسته‌ی ایزوله و قابل‌حمل بسته‌بندی می‌شود.</p>
<h2>کانتینر در برابر ماشین مجازی</h2>
<p>ماشین مجازی (Virtual Machine) با شبیه‌سازی کامل سخت‌افزار، یک سیستم‌عامل کامل و مستقل اجرا می‌کند که حجم زیادی از منابع (چند گیگابایت) و زمان راه‌اندازی طولانی نیاز دارد. اما کانتینرها از هسته‌ی (kernel) سیستم‌عامل میزبان استفاده می‌کنند و فقط فضای کاربری (user space) خودشان را ایزوله نگه می‌دارند. نتیجه این است که کانتینرها بسیار سبک‌تر (چند مگابایت تا چند صد مگابایت)، سریع‌تر در راه‌اندازی (چند ثانیه در برابر چند دقیقه) و کارآمدتر در استفاده از منابع سرور هستند.</p>
<p>داکر (Docker) محبوب‌ترین پلتفرم کانتینرسازی است که ابزارهای ساخت، اجرا و مدیریت کانتینرها را در اختیار توسعه‌دهندگان قرار می‌دهد. با داکر می‌توانید یک برنامه را یک‌بار بسته‌بندی کنید و همان بسته را روی لپ‌تاپ شخصی، سرور تست و سرور تولید (production) بدون تغییر اجرا کنید. این قابلیت «یک‌بار بساز، همه‌جا اجرا کن» دلیل اصلی محبوبیت گسترده‌ی داکر در صنعت نرم‌افزار است.</p>""",
                },
                {
                    "title": "نصب داکر و دستورات ابتدایی",
                    "kind": "text",
                    "minutes": 12,
                    "is_preview": False,
                    "body": """<h2>نصب داکر روی لینوکس</h2>
<p>روی توزیع‌های مبتنی بر دبیان مانند اوبونتو، ساده‌ترین راه نصب استفاده از اسکریپت رسمی داکر است:</p>
<pre><code class="language-bash">curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER</code></pre>
<p>خط دوم کاربر فعلی را به گروه <code>docker</code> اضافه می‌کند تا نیازی به استفاده از <code>sudo</code> برای هر دستور داکر نباشد؛ پس از اجرای این دستور باید یک‌بار از سیستم خارج و دوباره وارد شوید. برای اطمینان از نصب موفق:</p>
<pre><code class="language-bash">docker --version
docker run hello-world</code></pre>
<p>دستور دوم یک کانتینر آزمایشی کوچک دانلود و اجرا می‌کند که پیام خوش‌آمدگویی چاپ می‌کند؛ اگر این پیام را دیدید، داکر به‌درستی نصب شده است.</p>
<h2>چند دستور پرکاربرد اولیه</h2>
<pre><code class="language-bash">docker ps
docker ps -a
docker images
docker rm &lt;container_id&gt;
docker rmi &lt;image_id&gt;</code></pre>
<p><code>docker ps</code> کانتینرهای در حال اجرا را نشان می‌دهد و <code>docker ps -a</code> همه‌ی کانتینرها را حتی متوقف‌شده‌ها. <code>docker images</code> فهرست ایمیج‌های دانلودشده روی سیستم را نمایش می‌دهد. برای اجرای یک کانتینر تعاملی و ورود به ترمینال داخل آن:</p>
<pre><code class="language-bash">docker run -it ubuntu bash</code></pre>
<p>فلگ <code>-it</code> ترمینال تعاملی می‌سازد. این دستورات پایه، ابزار روزمره‌ی کار با داکر هستند و در ادامه‌ی دوره بارها از آن‌ها استفاده می‌کنیم.</p>""",
                },
                {
                    "title": "تفاوت image و container",
                    "kind": "text",
                    "minutes": 12,
                    "is_preview": False,
                    "body": """<h2>image: قالب، container: نمونه‌ی در حال اجرا</h2>
<p>یکی از مفاهیم پایه‌ای که باید کاملاً روشن باشد، تفاوت بین <strong>image</strong> و <strong>container</strong> است. image یک بسته‌ی فقط-خواندنی (read-only) است که شامل کد برنامه، کتابخانه‌ها، تنظیمات و همه‌چیزهایی است که برنامه برای اجرا نیاز دارد. می‌توان image را مثل یک قالب یا الگو در نظر گرفت، شبیه به کلاس در برنامه‌نویسی شیءگرا.</p>
<p>container نمونه‌ی در حال اجرای یک image است، دقیقاً مثل نمونه (instance) ساخته‌شده از یک کلاس. از یک image می‌توان چندین container مستقل و همزمان ساخت که هرکدام حافظه، فایل‌سیستم موقت و شبکه‌ی جداگانه دارند اما همگی از همان قالب اولیه ساخته شده‌اند.</p>
<pre><code class="language-bash">docker run -d --name web1 nginx
docker run -d --name web2 nginx</code></pre>
<p>دستور بالا دو container مستقل به نام‌های <code>web1</code> و <code>web2</code> از روی یک image یکسان (<code>nginx</code>) می‌سازد. فلگ <code>-d</code> یعنی کانتینر در پس‌زمینه (detached) اجرا شود.</p>
<h2>چرخه‌ی حیات یک کانتینر</h2>
<p>یک کانتینر می‌تواند در حالت‌های در حال اجرا، متوقف یا حذف‌شده باشد:</p>
<pre><code class="language-bash">docker stop web1
docker start web1
docker restart web1
docker rm -f web2</code></pre>
<p>نکته‌ی مهم این است که وقتی یک کانتینر متوقف می‌شود، فایل‌سیستم آن از بین نمی‌رود و با <code>docker start</code> می‌توان دوباره آن را با همان داده‌ها اجرا کرد؛ اما با <code>docker rm</code> کانتینر و تمام تغییرات موقتش برای همیشه حذف می‌شود، مگر اینکه داده‌ها در یک volume ذخیره شده باشند که در فصل بعد بررسی می‌کنیم.</p>""",
                },
            ],
        },
        {
            "title": "فصل دوم: ساخت ایمیج با Dockerfile",
            "lessons": [
                {
                    "title": "دستورات پایه‌ی Dockerfile",
                    "kind": "text",
                    "minutes": 15,
                    "is_preview": False,
                    "body": """<h2>دستور ساخت به زبان داکر</h2>
<p>Dockerfile یک فایل متنی است که مرحله‌به‌مرحله توضیح می‌دهد یک image چگونه ساخته شود. هر خط آن یک دستور (instruction) است که یک لایه‌ی جدید به image اضافه می‌کند. یک Dockerfile ساده برای یک اسکریپت پایتون:</p>
<pre><code class="language-dockerfile">FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]</code></pre>
<p><code>FROM</code> ایمیج پایه را مشخص می‌کند؛ اینجا از یک نسخه‌ی سبک پایتون استفاده شده است. <code>WORKDIR</code> دایرکتوری کاری داخل کانتینر را تعیین می‌کند و دستورات بعدی نسبت به آن اجرا می‌شوند. <code>COPY</code> فایل‌ها را از سیستم میزبان به داخل image کپی می‌کند. <code>RUN</code> یک دستور را در زمان ساخت image اجرا می‌کند (مثل نصب پکیج). <code>CMD</code> دستوری است که هنگام اجرای container (نه ساخت image) اجرا می‌شود.</p>
<p>برای ساختن image از روی این فایل:</p>
<pre><code class="language-bash">docker build -t my-app:1.0 .
docker run my-app:1.0</code></pre>
<p>فلگ <code>-t</code> یک نام و تگ برای image تعیین می‌کند و نقطه‌ی پایانی مسیر context ساخت (معمولاً پوشه‌ی فعلی) است. توجه کنید که ترتیب COPY کردن <code>requirements.txt</code> پیش از بقیه‌ی کدها یک تکنیک بهینه‌سازی است که در لایه‌ی بعدی توضیح می‌دهیم.</p>""",
                },
                {
                    "title": "لایه‌ها و کش ساخت image",
                    "kind": "text",
                    "minutes": 13,
                    "is_preview": False,
                    "body": """<h2>هر دستور، یک لایه</h2>
<p>داکر هر image را از لایه‌های متعدد (layers) می‌سازد؛ هر دستور در Dockerfile معمولاً یک لایه‌ی جدید تولید می‌کند. این لایه‌ها روی هم قرار می‌گیرند و یک فایل‌سیستم واحد تشکیل می‌دهند. مزیت بزرگ این معماری، امکان اشتراک‌گذاری لایه‌ها بین ایمیج‌های مختلف و کش شدن آن‌هاست: اگر یک لایه تغییر نکرده باشد، داکر آن را دوباره نمی‌سازد و از کش استفاده می‌کند.</p>
<p>به همین دلیل، ترتیب دستورات در Dockerfile اهمیت زیادی دارد. لایه‌هایی که کمتر تغییر می‌کنند (مثل نصب وابستگی‌ها) باید زودتر بیایند و لایه‌هایی که زیاد تغییر می‌کنند (مثل کد خود برنامه) باید در انتها قرار بگیرند:</p>
<pre><code class="language-dockerfile"># درست: وابستگی‌ها قبل از کد
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .</code></pre>
<pre><code class="language-dockerfile"># نادرست: هر تغییر کد، نصب مجدد وابستگی‌ها را هم اجبار می‌کند
COPY . .
RUN pip install -r requirements.txt</code></pre>
<p>در حالت دوم، حتی یک تغییر کوچک در کد برنامه باعث می‌شود کش لایه‌ی <code>COPY . .</code> باطل شود و در نتیجه لایه‌ی <code>RUN pip install</code> هم دوباره از صفر اجرا شود، چون داکر لایه‌ها را به‌ترتیب و بر اساس تغییر لایه‌ی قبلی نامعتبر می‌کند. رعایت این ترتیب در پروژه‌های واقعی می‌تواند زمان ساخت image را از چند دقیقه به چند ثانیه کاهش دهد و فرایند توسعه را به‌طور محسوسی سریع‌تر کند.</p>""",
                },
                {
                    "title": "ساخت چندمرحله‌ای (multi-stage build)",
                    "kind": "text",
                    "minutes": 16,
                    "is_preview": False,
                    "body": """<h2>مشکل ایمیج‌های حجیم</h2>
<p>در زبان‌هایی مثل Go یا در پروژه‌های فرانت‌اند که نیاز به کامپایل یا build دارند، ابزارهای ساخت (کامپایلر، وابستگی‌های توسعه) خودشان حجم زیادی دارند اما در زمان اجرای نهایی برنامه به آن‌ها نیازی نیست. ساخت چندمرحله‌ای (Multi-stage Build) به شما اجازه می‌دهد از چند مرحله‌ی <code>FROM</code> در یک Dockerfile استفاده کنید تا فقط نتیجه‌ی نهایی وارد image آخر شود.</p>
<pre><code class="language-dockerfile">FROM node:20 AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html</code></pre>
<p>در این مثال، مرحله‌ی اول با نام <code>build</code> پروژه‌ی React یا Vue را با Node.js می‌سازد. مرحله‌ی دوم یک image بسیار سبک‌تر بر پایه‌ی nginx است که فقط فایل‌های خروجی build (پوشه‌ی <code>dist</code>) را از مرحله‌ی اول کپی می‌کند، بدون اینکه Node.js یا وابستگی‌های توسعه در image نهایی باقی بمانند.</p>
<h2>نتیجه: ایمیج‌های کوچک‌تر و امن‌تر</h2>
<p>نتیجه‌ی این روش، image نهایی بسیار کوچک‌تری است که فقط شامل چیزهای لازم برای اجرا (نه ساخت) برنامه است. این کار هم سرعت دانلود و دیپلوی image را افزایش می‌دهد و هم سطح حمله‌ی امنیتی (attack surface) را کاهش می‌دهد، چون ابزارهای توسعه که می‌توانند نقاط ضعف امنیتی داشته باشند، در image نهایی وجود ندارند. Multi-stage build یکی از مهم‌ترین تکنیک‌های حرفه‌ای در نوشتن Dockerfileهای production است.</p>""",
                },
                {
                    "title": "بهترین شیوه‌ها برای ایمیج‌های کوچک و امن",
                    "kind": "text",
                    "minutes": 14,
                    "is_preview": False,
                    "body": """<h2>چند اصل برای Dockerfileهای بهتر</h2>
<p>پس از یادگیری دستورات پایه، رعایت چند اصل باعث می‌شود ایمیج‌های شما سبک‌تر، امن‌تر و قابل‌نگهداری‌تر شوند. اول، همیشه از ایمیج‌های پایه‌ی سبک استفاده کنید؛ نسخه‌های <code>slim</code> یا <code>alpine</code> به‌جای نسخه‌ی کامل، حجم قابل‌توجهی کم می‌کنند:</p>
<pre><code class="language-dockerfile">FROM python:3.12-slim</code></pre>
<p>دوم، هرگز از تگ <code>latest</code> در محیط production استفاده نکنید؛ همیشه یک نسخه‌ی مشخص قفل کنید تا build شما در آینده به‌طور غیرمنتظره تغییر نکند. سوم، از کاربر غیر-root داخل کانتینر استفاده کنید:</p>
<pre><code class="language-dockerfile">RUN useradd --create-home appuser
USER appuser</code></pre>
<p>اجرای کانتینر با کاربر root ریسک امنیتی بالایی دارد؛ اگر مهاجمی از یک آسیب‌پذیری داخل برنامه سوءاستفاده کند، دسترسی root داخل کانتینر می‌تواند خطرناک‌تر باشد. چهارم، از فایل <strong>.dockerignore</strong> برای جلوگیری از کپی شدن فایل‌های غیرضروری (مثل <code>.git</code>، <code>__pycache__</code>، محیط مجازی) استفاده کنید، دقیقاً مشابه .gitignore:</p>
<pre><code class="language-text">.git
__pycache__/
*.pyc
venv/
.env</code></pre>
<p>پنجم، دستورات <code>RUN</code> مرتبط را با <code>&amp;&amp;</code> در یک خط ترکیب کنید تا لایه‌های کمتری ساخته شود و فضای اضافی پاک شود:</p>
<pre><code class="language-dockerfile">RUN apt-get update &amp;&amp; apt-get install -y curl &amp;&amp; rm -rf /var/lib/apt/lists/*</code></pre>
<p>رعایت این اصول تفاوت زیادی بین یک image آماتور و یک image آماده‌ی production ایجاد می‌کند.</p>""",
                },
            ],
        },
        {
            "title": "فصل سوم: ذخیره‌سازی و شبکه",
            "lessons": [
                {
                    "title": "Volume و ماندگاری داده",
                    "kind": "text",
                    "minutes": 13,
                    "is_preview": False,
                    "body": """<h2>مشکل داده‌های ناپدیدشونده</h2>
<p>فایل‌سیستم یک کانتینر به‌طور پیش‌فرض موقتی است؛ به محض حذف کانتینر با <code>docker rm</code>، تمام داده‌های نوشته‌شده داخل آن هم از بین می‌روند. این رفتار برای برنامه‌های بدون‌حالت (stateless) مشکلی ندارد، اما برای پایگاه‌داده یا هر برنامه‌ای که باید داده را نگه دارد، فاجعه‌بار است.</p>
<p><strong>Volume</strong> راه‌حل رسمی داکر برای ماندگاری داده است؛ یک فضای ذخیره‌سازی است که مستقل از چرخه‌ی حیات کانتینر مدیریت می‌شود و توسط خود داکر نگهداری می‌شود:</p>
<pre><code class="language-bash">docker volume create pgdata
docker run -d --name db -v pgdata:/var/lib/postgresql/data postgres:16</code></pre>
<p>در این دستور، پوشه‌ی <code>/var/lib/postgresql/data</code> داخل کانتینر به volume به نام <code>pgdata</code> متصل می‌شود. حتی اگر کانتینر <code>db</code> حذف شود، می‌توانید یک کانتینر جدید بسازید و همان volume را دوباره متصل کنید تا داده‌ها دست‌نخورده باقی بمانند.</p>
<h2>Bind Mount برای توسعه</h2>
<p>گزینه‌ی دیگر، Bind Mount است که یک پوشه‌ی مشخص از سیستم میزبان را مستقیماً به کانتینر متصل می‌کند؛ این روش برای توسعه بسیار مفید است چون تغییرات کد بلافاصله داخل کانتینر منعکس می‌شود:</p>
<pre><code class="language-bash">docker run -v $(pwd):/app -it my-app:1.0 bash</code></pre>
<p>فهرست volumeهای موجود را با <code>docker volume ls</code> و حذف یک volume بلااستفاده را با <code>docker volume rm pgdata</code> انجام می‌دهید. انتخاب درست بین Volume و Bind Mount، بسته به اینکه در حال توسعه هستید یا production، اهمیت زیادی در معماری کانتینری شما دارد.</p>""",
                },
                {
                    "title": "Network در داکر و ارتباط بین کانتینرها",
                    "kind": "text",
                    "minutes": 14,
                    "is_preview": False,
                    "body": """<h2>چرا کانتینرها باید با هم صحبت کنند؟</h2>
<p>در بیشتر برنامه‌های واقعی، چند کانتینر باید با هم ارتباط برقرار کنند؛ مثلاً یک برنامه‌ی وب باید بتواند به یک کانتینر پایگاه‌داده متصل شود. داکر برای این منظور مفهوم <strong>network</strong> را ارائه می‌دهد. ساده‌ترین راه، ساختن یک شبکه‌ی سفارشی از نوع bridge است:</p>
<pre><code class="language-bash">docker network create app-network
docker run -d --name db --network app-network postgres:16
docker run -d --name web --network app-network my-app:1.0</code></pre>
<p>مزیت کلیدی network سفارشی این است که کانتینرهای متصل به آن می‌توانند با استفاده از <strong>نام کانتینر</strong> به‌جای IP به یکدیگر متصل شوند؛ یعنی داخل کد برنامه‌ی <code>web</code> کافی است به آدرس <code>db</code> وصل شوید (مثلاً <code>db:5432</code> برای پستگرس) و داکر به‌طور خودکار این نام را به آدرس داخلی درست ترجمه می‌کند. این قابلیت به نام DNS داخلی داکر شناخته می‌شود.</p>
<h2>انواع دیگر network</h2>
<p>علاوه بر <code>bridge</code> که پیش‌فرض و رایج‌ترین است، داکر انواع دیگری مثل <code>host</code> (اشتراک مستقیم شبکه‌ی میزبان، بدون ایزوله‌سازی) و <code>none</code> (بدون هیچ دسترسی شبکه‌ای) را نیز پشتیبانی می‌کند. برای دیدن شبکه‌های موجود و جزئیات یک شبکه:</p>
<pre><code class="language-bash">docker network ls
docker network inspect app-network</code></pre>
<p>در عمل، معمولاً به‌جای ساختن دستی این شبکه‌ها، از docker compose استفاده می‌کنیم که این کار را به‌طور خودکار برای سرویس‌های تعریف‌شده انجام می‌دهد؛ موضوعی که در فصل بعد به آن می‌پردازیم.</p>""",
                },
                {
                    "title": "متغیرهای محیطی و مدیریت پیکربندی",
                    "kind": "text",
                    "minutes": 11,
                    "is_preview": False,
                    "body": """<h2>جدا کردن پیکربندی از کد</h2>
<p>یک اصل مهم در توسعه‌ی نرم‌افزار مدرن این است که تنظیمات حساس یا وابسته به محیط (مثل رمز پایگاه‌داده، کلید API، آدرس سرویس‌های خارجی) هرگز مستقیماً داخل کد یا Dockerfile نوشته نشوند. داکر برای این منظور از <strong>متغیرهای محیطی</strong> (Environment Variables) پشتیبانی می‌کند.</p>
<p>روش اول، تعیین مستقیم متغیر هنگام اجرا:</p>
<pre><code class="language-bash">docker run -e DATABASE_URL=postgres://user:pass@db:5432/mydb my-app:1.0</code></pre>
<p>روش دوم و رایج‌تر، استفاده از یک فایل <code>.env</code>:</p>
<pre><code class="language-text">DATABASE_URL=postgres://user:pass@db:5432/mydb
DEBUG=False
SECRET_KEY=change-this-in-production</code></pre>
<pre><code class="language-bash">docker run --env-file .env my-app:1.0</code></pre>
<p>فایل <code>.env</code> باید حتماً در <code>.gitignore</code> و <code>.dockerignore</code> قرار بگیرد تا هرگز وارد تاریخچه‌ی گیت یا داخل image نشود. در داخل کد پایتون یا جنگو، این مقادیر معمولاً با کتابخانه‌هایی مثل <code>os.environ.get()</code> یا <code>django-environ</code> خوانده می‌شوند.</p>
<p>یک نکته‌ی مهم امنیتی: متغیرهای محیطی که با <code>-e</code> یا <code>--env-file</code> ست می‌شوند، با دستور <code>docker inspect</code> قابل مشاهده هستند؛ برای اطلاعات بسیار حساس در محیط production، ابزارهای مدیریت رمز (Secret Management) مانند Docker Secrets یا Vault گزینه‌ی امن‌تری هستند که در دوره‌های پیشرفته‌تر بررسی می‌شوند.</p>""",
                },
            ],
        },
        {
            "title": "فصل چهارم: Docker Compose",
            "lessons": [
                {
                    "title": "آشنایی با docker-compose.yml",
                    "kind": "text",
                    "minutes": 14,
                    "is_preview": False,
                    "body": """<h2>مدیریت چند کانتینر با یک فایل</h2>
<p>وقتی برنامه‌ی شما از چند سرویس تشکیل شده (مثلاً وب‌سرور، پایگاه‌داده، کش)، اجرای دستی هر کدام با <code>docker run</code> و ساختن network و volume به‌صورت جداگانه خسته‌کننده و مستعد خطاست. <strong>Docker Compose</strong> ابزاری است که تعریف کل این سرویس‌ها را در یک فایل YAML واحد جمع می‌کند.</p>
<pre><code class="language-yaml">version: "3.9"

services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"

  cache:
    image: redis:7-alpine</code></pre>
<p>هر بلوک زیر <code>services</code> یک کانتینر را توصیف می‌کند. کلید <code>image</code> ایمیج موردنیاز را مشخص می‌کند و <code>ports</code> پورت میزبان را به پورت داخل کانتینر متصل می‌کند؛ در مثال بالا، پورت ۸۰۸۰ سیستم شما به پورت ۸۰ داخل کانتینر nginx وصل می‌شود.</p>
<h2>اجرا و مدیریت</h2>
<pre><code class="language-bash">docker compose up -d
docker compose ps
docker compose logs -f web
docker compose down</code></pre>
<p><code>docker compose up -d</code> همه‌ی سرویس‌های تعریف‌شده را در پس‌زمینه اجرا می‌کند و به‌طور خودکار یک network مشترک برای آن‌ها می‌سازد تا بتوانند با نام سرویس به هم متصل شوند. <code>docker compose down</code> همه‌ی کانتینرها و شبکه را متوقف و حذف می‌کند (ولی volumeها را نگه می‌دارد مگر با فلگ <code>-v</code>). این فایل واحد، مستندسازی زنده‌ای از معماری کل پروژه‌ی شماست.</p>""",
                },
                {
                    "title": "تعریف چند سرویس: وب و دیتابیس",
                    "kind": "text",
                    "minutes": 15,
                    "is_preview": False,
                    "body": """<h2>یک نمونه‌ی واقعی‌تر</h2>
<p>حالا یک docker-compose.yml کامل‌تر می‌سازیم که یک برنامه‌ی وب را به یک پایگاه‌داده‌ی پستگرس متصل می‌کند و از volume برای ماندگاری داده و متغیر محیطی برای پیکربندی استفاده می‌کند:</p>
<pre><code class="language-yaml">version: "3.9"

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgres://appuser:apppass@db:5432/appdb
    depends_on:
      - db

  db:
    image: postgres:16
    environment:
      - POSTGRES_USER=appuser
      - POSTGRES_PASSWORD=apppass
      - POSTGRES_DB=appdb
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:</code></pre>
<p>در سرویس <code>web</code>، به‌جای <code>image</code> از کلید <code>build: .</code> استفاده شده که یعنی داکر به‌جای دانلود یک image آماده، از Dockerfile موجود در همان پوشه، image بسازد. <code>depends_on</code> ترتیب راه‌اندازی را کنترل می‌کند تا سرویس <code>db</code> پیش از <code>web</code> شروع شود، هرچند نکته‌ی مهم این است که این تنها ترتیب راه‌اندازی کانتینر را تضمین می‌کند، نه آماده بودن کامل پایگاه‌داده برای پذیرش اتصال.</p>
<h2>بلوک volumes سطح بالا</h2>
<p>در انتهای فایل، بخش <code>volumes</code> در سطح بالا، volume نام‌گذاری‌شده‌ی <code>pgdata</code> را تعریف می‌کند که در سرویس db استفاده شده است. این ساختار به شما اجازه می‌دهد کل معماری چندسرویسی برنامه را با یک دستور <code>docker compose up</code> راه‌اندازی کنید.</p>""",
                },
                {
                    "title": "مدیریت چرخه‌ی حیات با compose up و down",
                    "kind": "text",
                    "minutes": 12,
                    "is_preview": False,
                    "body": """<h2>دستورات روزمره‌ی کار با Compose</h2>
<p>پس از نوشتن فایل docker-compose.yml، تعامل روزانه با آن از طریق چند دستور کلیدی انجام می‌شود. برای اجرای مجدد فقط یک سرویس خاص پس از تغییر کد:</p>
<pre><code class="language-bash">docker compose up -d --build web</code></pre>
<p>فلگ <code>--build</code> باعث می‌شود پیش از اجرا، image سرویس <code>web</code> دوباره ساخته شود؛ این کار وقتی لازم است که Dockerfile یا کد منبع تغییر کرده باشد. برای اجرای یک دستور یک‌باره داخل یکی از سرویس‌ها بدون تأثیر روی کانتینر اصلی:</p>
<pre><code class="language-bash">docker compose exec web python manage.py migrate
docker compose exec db psql -U appuser -d appdb</code></pre>
<p><code>exec</code> دستوری را داخل یک کانتینر <strong>در حال اجرا</strong> اجرا می‌کند؛ اگر کانتینر هنوز اجرا نشده، باید از <code>docker compose run</code> استفاده کنید که یک کانتینر موقت جدید می‌سازد.</p>
<h2>پاک‌سازی و توقف</h2>
<pre><code class="language-bash">docker compose stop
docker compose down
docker compose down -v</code></pre>
<p><code>stop</code> فقط کانتینرها را متوقف می‌کند بدون حذف آن‌ها، <code>down</code> کانتینرها و شبکه را کاملاً حذف می‌کند و <code>down -v</code> علاوه بر آن، volumeها را هم پاک می‌کند؛ از این فلگ آخر با احتیاط استفاده کنید چون داده‌های پایگاه‌داده هم از بین می‌روند. عادت به استفاده‌ی منظم از این دستورات، محیط توسعه‌ی شما را تمیز و قابل‌پیش‌بینی نگه می‌دارد.</p>""",
                },
            ],
        },
        {
            "title": "فصل پنجم: داکرایز کردن یک پروژه‌ی جنگو",
            "lessons": [
                {
                    "title": "نوشتن Dockerfile برای جنگو",
                    "kind": "text",
                    "minutes": 15,
                    "is_preview": False,
                    "body": """<h2>یک Dockerfile واقعی برای پروژه‌ی جنگو</h2>
<p>حالا آموخته‌های فصل‌های قبل را روی یک پروژه‌ی واقعی جنگو پیاده می‌کنیم. یک Dockerfile مناسب برای توسعه به این شکل است:</p>
<pre><code class="language-dockerfile">FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]</code></pre>
<p><code>PYTHONDONTWRITEBYTECODE</code> از ساخت فایل‌های <code>.pyc</code> غیرضروری جلوگیری می‌کند و <code>PYTHONUNBUFFERED</code> باعث می‌شود خروجی لاگ پایتون بلافاصله (بدون بافر) نمایش داده شود، که برای دیدن لاگ‌ها با <code>docker compose logs</code> ضروری است. توجه کنید که سرور توسعه‌ی جنگو باید روی <code>0.0.0.0</code> اجرا شود، نه <code>127.0.0.1</code>، وگرنه از بیرون کانتینر قابل دسترسی نخواهد بود.</p>
<h2>فایل requirements.txt</h2>
<p>مطمئن شوید فایل <code>requirements.txt</code> شامل تمام وابستگی‌های لازم است:</p>
<pre><code class="language-text">Django==5.0.6
psycopg2-binary==2.9.9
gunicorn==22.0.0
django-environ==0.11.2</code></pre>
<p><code>psycopg2-binary</code> برای اتصال جنگو به پستگرس و <code>gunicorn</code> برای اجرای production در فصل بعد لازم است. با این دو فایل آماده، پروژه‌ی جنگوی شما اکنون قابل بسته‌بندی در یک image مستقل است.</p>""",
                },
                {
                    "title": "افزودن پستگرس با docker compose",
                    "kind": "text",
                    "minutes": 16,
                    "is_preview": False,
                    "body": """<h2>اتصال جنگو به پستگرس در کانتینر</h2>
<p>در فصل قبل با docker compose آشنا شدیم؛ حالا آن را برای پروژه‌ی جنگوی خودمان کامل می‌کنیم. فایل docker-compose.yml:</p>
<pre><code class="language-yaml">services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    env_file: .env
    depends_on:
      - db

  db:
    image: postgres:16
    env_file: .env
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:</code></pre>
<p>فایل <code>.env</code> متغیرهای مشترک بین جنگو و پستگرس را نگه می‌دارد:</p>
<pre><code class="language-text">POSTGRES_DB=appdb
POSTGRES_USER=appuser
POSTGRES_PASSWORD=apppass
DATABASE_URL=postgres://appuser:apppass@db:5432/appdb</code></pre>
<p>در فایل <code>settings.py</code> جنگو، تنظیمات پایگاه‌داده باید این مقدار را از متغیر محیطی بخواند، معمولاً با کتابخانه‌ی <code>django-environ</code>:</p>
<pre><code class="language-python">import environ

env = environ.Env()
DATABASES = {
    "default": env.db("DATABASE_URL")
}</code></pre>
<p>پس از بالا آوردن سرویس‌ها با <code>docker compose up -d</code>، باید مایگریشن‌های جنگو را داخل کانتینر اجرا کنید:</p>
<pre><code class="language-bash">docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser</code></pre>
<p>از این پس، پروژه‌ی جنگوی شما و پایگاه‌داده‌اش کاملاً در کانتینر اجرا می‌شوند و هر همکار جدید فقط با <code>docker compose up</code> کل محیط توسعه را یکسان راه‌اندازی می‌کند.</p>""",
                },
                {
                    "title": "تنظیمات production: gunicorn و فایل‌های استاتیک",
                    "kind": "text",
                    "minutes": 16,
                    "is_preview": False,
                    "body": """<h2>سرور توسعه کافی نیست</h2>
<p>سرور داخلی جنگو (<code>runserver</code>) فقط برای توسعه طراحی شده و برای بار ترافیک واقعی مناسب نیست. در production باید از یک WSGI Server مثل <strong>gunicorn</strong> استفاده کنیم. Dockerfile برای production کمی متفاوت است و از multi-stage build نیز می‌توان بهره برد:</p>
<pre><code class="language-dockerfile">FROM python:3.12-slim

WORKDIR /code
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]</code></pre>
<p>دستور <code>collectstatic</code> تمام فایل‌های استاتیک (CSS، JS، تصاویر) پروژه را در یک پوشه‌ی واحد جمع می‌کند. در محیط production، معمولاً این فایل‌ها را به یک وب‌سرور سبک‌تر مثل nginx یا یک سرویس ابری می‌سپاریم، نه به خود جنگو، چون جنگو برای سرو فایل استاتیک بهینه نیست.</p>
<h2>ترکیب nginx و gunicorn با compose</h2>
<p>یک الگوی رایج، افزودن یک سرویس nginx به docker-compose.yml است که درخواست‌های استاتیک را مستقیم پاسخ می‌دهد و بقیه‌ی درخواست‌ها را به gunicorn هدایت می‌کند:</p>
<pre><code class="language-yaml">services:
  nginx:
    image: nginx:alpine
    volumes:
      - static_volume:/code/staticfiles
      - ./nginx.conf:/etc/nginx/conf.d/default.conf
    ports:
      - "80:80"
    depends_on:
      - web</code></pre>
<p>در این معماری، nginx به‌عنوان دروازه‌ی ورودی عمل می‌کند و بار سرو فایل‌های استاتیک را از دوش gunicorn برمی‌دارد و کارایی کلی سیستم را بهبود می‌بخشد.</p>""",
                },
            ],
        },
        {
            "title": "فصل ششم: رجیستری و دیپلوی",
            "lessons": [
                {
                    "title": "Docker Hub و رجیستری خصوصی",
                    "kind": "text",
                    "minutes": 11,
                    "is_preview": False,
                    "body": """<h2>ذخیره‌سازی و اشتراک‌گذاری ایمیج‌ها</h2>
<p><strong>رجیستری (Registry)</strong> سروری است که ایمیج‌های داکر را ذخیره و در دسترس قرار می‌دهد، دقیقاً مشابه نقشی که گیت‌هاب برای کد گیت دارد. <strong>Docker Hub</strong> بزرگ‌ترین و محبوب‌ترین رجیستری عمومی است که هزاران ایمیج رسمی (مانند <code>python</code>، <code>postgres</code>، <code>nginx</code>) را میزبانی می‌کند و همان جایی است که تا اینجای دوره ایمیج‌های پایه را از آن دانلود کرده‌ایم.</p>
<p>برای انتشار image خودتان روی Docker Hub، ابتدا باید وارد حساب کاربری شوید:</p>
<pre><code class="language-bash">docker login</code></pre>
<p>سازمان‌ها معمولاً به دلیل ملاحظات امنیتی یا حجم بالای ایمیج‌های داخلی، از یک <strong>رجیستری خصوصی</strong> استفاده می‌کنند؛ گزینه‌هایی مانند Amazon ECR، Google Artifact Registry، GitHub Container Registry، یا حتی راه‌اندازی یک رجیستری خودمیزبان با تصویر رسمی <code>registry:2</code>. مفهوم استفاده در همه‌ی این‌ها یکسان است: تگ زدن image با آدرس رجیستری و سپس push کردن.</p>
<p>برای رجیستری خودمیزبان، یک نمونه‌ی ساده این‌گونه اجرا می‌شود:</p>
<pre><code class="language-bash">docker run -d -p 5000:5000 --name registry registry:2</code></pre>
<p>این کار یک رجیستری محلی روی پورت ۵۰۰۰ راه‌اندازی می‌کند که برای تیم‌های کوچک یا محیط‌های آزمایشی گزینه‌ای سبک و رایگان است.</p>""",
                },
                {
                    "title": "تگ‌گذاری و push/pull ایمیج",
                    "kind": "text",
                    "minutes": 12,
                    "is_preview": False,
                    "body": """<h2>نام‌گذاری صحیح ایمیج‌ها</h2>
<p>پیش از push کردن یک image به رجیستری، باید آن را با فرمت مناسب تگ بزنید: <code>&lt;نام کاربری یا آدرس رجیستری&gt;/&lt;نام ایمیج&gt;:&lt;نسخه&gt;</code>. برای Docker Hub:</p>
<pre><code class="language-bash">docker build -t my-app:1.0 .
docker tag my-app:1.0 aliuser/my-app:1.0
docker push aliuser/my-app:1.0</code></pre>
<p>برای یک رجیستری خصوصی، آدرس سرور هم باید در تگ قید شود:</p>
<pre><code class="language-bash">docker tag my-app:1.0 registry.mycompany.com/my-app:1.0
docker push registry.mycompany.com/my-app:1.0</code></pre>
<p>برای دانلود یک image منتشرشده روی هر سرور دیگری:</p>
<pre><code class="language-bash">docker pull aliuser/my-app:1.0
docker run aliuser/my-app:1.0</code></pre>
<h2>اهمیت نسخه‌بندی درست تگ‌ها</h2>
<p>یک اشتباه رایج، اتکای همیشگی به تگ <code>latest</code> است. اگر image شما همیشه با تگ latest منتشر شود، سرور تولید ممکن است بدون اطلاع شما نسخه‌ی جدیدی را pull کند که هنوز کاملاً تست نشده است. بهترین شیوه این است که از نسخه‌بندی معنایی (semantic versioning) یا حتی شناسه‌ی commit گیت به‌عنوان تگ استفاده کنید تا هر image دقیقاً قابل ردیابی به یک نسخه‌ی مشخص از کد باشد؛ این کار هماهنگی بین گردش کار گیت و دیپلوی داکر را نیز برقرار می‌کند.</p>""",
                },
                {
                    "title": "مقدمه‌ای بر دیپلوی کانتینر روی سرور",
                    "kind": "text",
                    "minutes": 15,
                    "is_preview": False,
                    "body": """<h2>از لپ‌تاپ به سرور تولید</h2>
<p>پس از ساخت و push کردن image، مرحله‌ی نهایی اجرای آن روی یک سرور واقعی است. ساده‌ترین روش دیپلوی، اتصال به سرور از طریق SSH و اجرای docker compose در همان‌جا:</p>
<pre><code class="language-bash">ssh user@myserver.com
git clone https://github.com/username/my-project.git
cd my-project
docker compose pull
docker compose up -d</code></pre>
<p>در این الگو، به‌جای <code>build</code> روی سرور، معمولاً image از قبل در CI ساخته و به رجیستری push شده و سرور فقط آن را <code>pull</code> می‌کند؛ این کار سرعت دیپلوی را بالا می‌برد و از نیاز به ابزارهای ساخت روی سرور تولید بی‌نیاز می‌کند.</p>
<h2>یک گردش کار ساده‌ی CI/CD</h2>
<p>با ترکیب آموخته‌های این دوره و دوره‌ی گیت‌هاب، یک گردش کار معمول این‌گونه است: توسعه‌دهنده کد را push می‌کند، GitHub Actions تست‌ها را اجرا و در صورت موفقیت image را build و به رجیستری push می‌کند، سپس یک مرحله‌ی deploy از طریق SSH به سرور متصل شده و <code>docker compose pull &amp;&amp; docker compose up -d</code> را اجرا می‌کند.</p>
<p>برای پروژه‌های بزرگ‌تر با ده‌ها یا صدها کانتینر در چندین سرور، اجرای دستی این فرایند دیگر کافی نیست و به ابزارهای ارکستراسیون مانند Kubernetes یا Docker Swarm نیاز پیدا می‌کنید که هماهنگی، مقیاس‌پذیری خودکار و بازیابی از خطا را مدیریت می‌کنند. این موضوع پایه‌ای است که در دوره‌ی «معماری میکروسرویس» با جزئیات بیشتری بررسی می‌شود.</p>""",
                },
            ],
        },
    ],
}

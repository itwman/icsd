# -*- coding: utf-8 -*-

COURSE = {
    "slug": "laravel",
    "title": "لاراول",
    "category": "برنامه‌نویسی",
    "level": "intermediate",
    "summary": "ساخت وب‌اپلیکیشن حرفه‌ای با فریم‌ورک لاراول، از Routing تا استقرار.",
    "description": (
        "<p>لاراول محبوب‌ترین فریم‌ورک PHP برای ساخت وب‌اپلیکیشن‌های مدرن است که با فراهم کردن "
        "ابزارهای آماده برای routing، پایگاه داده، احراز هویت و بسیاری موارد دیگر، سرعت توسعه را "
        "به شکل چشمگیری افزایش می‌دهد. این دوره برای کسانی طراحی شده که PHP را می‌شناسند و می‌خواهند "
        "با یک فریم‌ورک حرفه‌ای و ساختاریافته کار کنند.</p>"
        "<p>در طول دوره با نصب و ساختار پروژه‌ی لاراول، Routing و Controller، قالب‌بندی Blade، کار با "
        "پایگاه داده از طریق Eloquent و Migration، فرم و Validation، احراز هویت، Middleware، ساخت API "
        "با Resource، پردازش صف و Job و در نهایت استقرار پروژه آشنا خواهید شد.</p>"
        "<p>پیش‌نیاز این دوره تسلط بر مبانی PHP (متغیر، آرایه، تابع، شیءگرایی مقدماتی) است.</p>"
    ),
    "price": 1500000,
    "duration_minutes": 540,
    "tags": ["Laravel", "PHP", "فریم‌ورک وب"],
    "modules": [
        {
            "title": "فصل اول: شروع کار با لاراول",
            "lessons": [
                {
                    "title": "نصب و ساختار پروژه",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": True,
                    "body": """<h2>لاراول چیست؟</h2>
<p>لاراول یک فریم‌ورک متن‌باز نوشته‌شده با PHP است که از الگوی معماری MVC (Model-View-Controller) پیروی می‌کند. این الگو کد برنامه را به سه بخش جدا تقسیم می‌کند: Model برای منطق داده، View برای نمایش و Controller برای هماهنگی بین این دو؛ نتیجه‌ی این جداسازی، کدی تمیزتر و قابل نگهداری‌تر است.</p>
<p>برای نصب لاراول باید ابتدا Composer را نصب داشته باشید، سپس با دستور زیر یک پروژه‌ی جدید بسازید:</p>
<pre><code class='language-bash'>composer create-project laravel/laravel blog
cd blog
php artisan serve</code></pre>
<p>پس از اجرای دستور آخر، پروژه روی آدرس localhost:8000 در دسترس خواهد بود. دستور artisan خط فرمان اصلی لاراول است که برای انجام بسیاری از کارهای تکراری مانند ساخت Controller، Model و Migration استفاده می‌شود.</p>
<p>ساختار پوشه‌های اصلی پروژه به این شکل است: پوشه‌ی app شامل Controllerها و Modelها، پوشه‌ی routes شامل تعریف مسیرها، پوشه‌ی resources/views شامل فایل‌های Blade، پوشه‌ی database شامل Migration و Seederها و فایل .env شامل تنظیمات محیطی مانند اطلاعات اتصال به دیتابیس است.</p>
<pre><code class='language-bash'>DB_CONNECTION=mysql
DB_DATABASE=blog
DB_USERNAME=root
DB_PASSWORD=secret</code></pre>
<p>آشنایی با این ساختار پایه‌ی کار با تمام بخش‌های آینده‌ی دوره است، چون هر ویژگی جدید لاراول در یکی از همین پوشه‌ها قرار می‌گیرد.</p>""",
                },
                {
                    "title": "Routing و Controller",
                    "kind": "text",
                    "minutes": 25,
                    "is_preview": False,
                    "body": """<h2>تعریف مسیرها و کنترلرها</h2>
<p>Routing در لاراول مشخص می‌کند که هر آدرس (URL) باید به چه کدی متصل شود. تمام مسیرهای وب در فایل routes/web.php تعریف می‌شوند. ساده‌ترین حالت یک مسیر، اجرای مستقیم یک Closure است:</p>
<pre><code class='language-php'>Route::get('/', function () {
    return view('welcome');
});

Route::get('/about', function () {
    return 'درباره‌ی ما';
});</code></pre>
<p>برای پروژه‌های واقعی معمولاً منطق را به Controller منتقل می‌کنیم. برای ساخت یک Controller از artisan استفاده می‌کنیم:</p>
<pre><code class='language-bash'>php artisan make:controller PostController</code></pre>
<p>سپس متدهای لازم را داخل آن می‌نویسیم:</p>
<pre><code class='language-php'>class PostController extends Controller
{
    public function index()
    {
        $posts = Post::all();
        return view('posts.index', compact('posts'));
    }

    public function show($id)
    {
        $post = Post::findOrFail($id);
        return view('posts.show', compact('post'));
    }
}</code></pre>
<p>و در فایل مسیرها، این متدها را به آدرس‌های مشخص وصل می‌کنیم:</p>
<pre><code class='language-php'>Route::get('/posts', [PostController::class, 'index']);
Route::get('/posts/{id}', [PostController::class, 'show']);</code></pre>
<p>پارامترهای داخل آکولاد در مسیر، مانند id}{، به‌صورت خودکار به آرگومان متد Controller ارسال می‌شوند. برای گروه‌بندی مسیرهای پرتکرار (مثل CRUD کامل) می‌توان از Route::resource استفاده کرد که در درس API با جزئیات بیشتری بررسی خواهد شد.</p>""",
                },
                {
                    "title": "قالب‌بندی با Blade",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": """<h2>موتور قالب Blade</h2>
<p>Blade موتور قالب‌بندی پیش‌فرض لاراول است که امکان نوشتن HTML همراه با منطق نمایشی ساده را با سینتکسی تمیز و خوانا فراهم می‌کند. فایل‌های Blade در پوشه‌ی resources/views قرار می‌گیرند و پسوند blade.php. دارند.</p>
<p>برای نمایش یک متغیر از دو آکولاد استفاده می‌شود که به‌صورت خودکار خروجی را escape می‌کند و از حملات XSS جلوگیری می‌کند:</p>
<pre><code class='language-blade'>&lt;h1&gt;{{ $post-&gt;title }}&lt;/h1&gt;
&lt;p&gt;{{ $post-&gt;body }}&lt;/p&gt;</code></pre>
<p>برای شرط و حلقه، Blade دستورات ساده‌ای دارد که با علامت @ شروع می‌شوند:</p>
<pre><code class='language-blade'>@if ($posts-&gt;count() &gt; 0)
    &lt;ul&gt;
    @foreach ($posts as $post)
        &lt;li&gt;{{ $post-&gt;title }}&lt;/li&gt;
    @endforeach
    &lt;/ul&gt;
@else
    &lt;p&gt;هیچ مطلبی یافت نشد.&lt;/p&gt;
@endif</code></pre>
<p>یکی از قابلیت‌های مهم Blade، ارث‌بری قالب (layout inheritance) است. با تعریف یک قالب پایه شامل @yield('content') و استفاده از @extends و @section در صفحات دیگر، می‌توانید هدر و فوتر مشترک را یک‌بار بنویسید و در تمام صفحات استفاده کنید:</p>
<pre><code class='language-blade'>@extends('layouts.app')

@section('content')
    &lt;h1&gt;صفحه‌ی اصلی&lt;/h1&gt;
@endsection</code></pre>
<p>این روش باعث می‌شود کد HTML تکراری در پروژه به حداقل برسد و مدیریت ظاهر کلی سایت بسیار ساده‌تر شود.</p>""",
                },
            ],
        },
        {
            "title": "فصل دوم: پایگاه داده با Eloquent",
            "lessons": [
                {
                    "title": "Migration و ساخت جدول",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": """<h2>مدیریت ساختار دیتابیس با Migration</h2>
<p>Migration در لاراول روشی برای تعریف و مدیریت نسخه‌دار ساختار جداول پایگاه داده با کد PHP است، به‌جای نوشتن دستی کوئری‌های SQL. این کار باعث می‌شود ساختار دیتابیس در کنترل نسخه (Git) قرار بگیرد و بین اعضای تیم و سرورهای مختلف به‌راحتی هماهنگ شود.</p>
<p>برای ساخت یک Migration جدید:</p>
<pre><code class='language-bash'>php artisan make:migration create_posts_table</code></pre>
<p>سپس ساختار جدول را در متد up تعریف می‌کنیم:</p>
<pre><code class='language-php'>public function up()
{
    Schema::create('posts', function (Blueprint $table) {
        $table-&gt;id();
        $table-&gt;string('title');
        $table-&gt;text('body');
        $table-&gt;foreignId('user_id')-&gt;constrained();
        $table-&gt;timestamps();
    });
}

public function down()
{
    Schema::dropIfExists('posts');
}</code></pre>
<p>متد id() یک ستون کلید اصلی خودافزا می‌سازد، foreignId با constrained() یک کلید خارجی به جدول users متصل می‌کند و timestamps() دو ستون created_at و updated_at را به‌صورت خودکار اضافه می‌کند. برای اجرای تمام Migrationهای در انتظار:</p>
<pre><code class='language-bash'>php artisan migrate</code></pre>
<p>اگر بخواهید آخرین Migration را برگردانید (rollback)، از دستور php artisan migrate:rollback استفاده کنید. متد down دقیقاً برای همین حالت نوشته می‌شود تا عملیات up را خنثی کند. تسلط بر Migration پیش‌نیاز کار درست با Eloquent در درس بعدی است.</p>""",
                },
                {
                    "title": "Eloquent ORM",
                    "kind": "text",
                    "minutes": 25,
                    "is_preview": False,
                    "body": """<h2>کار با داده از طریق مدل‌ها</h2>
<p>Eloquent، ORM (Object-Relational Mapping) پیش‌فرض لاراول است که به شما اجازه می‌دهد به‌جای نوشتن SQL خام، با ردیف‌های جدول به‌صورت شیء PHP کار کنید. هر جدول در دیتابیس معمولاً یک Model متناظر دارد؛ مثلاً جدول posts با مدل Post مدیریت می‌شود.</p>
<pre><code class='language-bash'>php artisan make:model Post</code></pre>
<p>عملیات پایه‌ی CRUD با Eloquent بسیار خوانا و ساده است:</p>
<pre><code class='language-php'>// ایجاد رکورد جدید
$post = Post::create([
    'title' =&gt; 'آموزش لاراول',
    'body'  =&gt; 'متن مقاله...',
    'user_id' =&gt; 1,
]);

// خواندن همه‌ی رکوردها
$posts = Post::all();

// جستجوی شرطی
$posts = Post::where('user_id', 1)-&gt;orderBy('created_at', 'desc')-&gt;get();

// به‌روزرسانی
$post = Post::find(1);
$post-&gt;title = 'عنوان جدید';
$post-&gt;save();

// حذف
Post::destroy(1);</code></pre>
<p>یکی از مزایای مهم Eloquent، متد findOrFail است که در صورت پیدا نشدن رکورد به‌جای بازگرداندن null، خطای 404 مناسب برمی‌گرداند؛ این ویژگی برای Controllerهایی که پاسخ به کاربر می‌دهند بسیار کاربردی است. Eloquent همچنین امکان تعریف روابط بین جداول (مانند یک‌به‌چند و چندبه‌چند) را فراهم می‌کند که موضوع درس بعدی است.</p>""",
                },
                {
                    "title": "روابط بین مدل‌ها",
                    "kind": "text",
                    "minutes": 25,
                    "is_preview": False,
                    "body": """<h2>تعریف رابطه‌های Eloquent</h2>
<p>در پایگاه داده‌های رابطه‌ای، جداول معمولاً با یکدیگر ارتباط دارند؛ مثلاً هر کاربر می‌تواند چند مقاله بنویسد و هر مقاله می‌تواند چند برچسب داشته باشد. Eloquent این روابط را با متدهای ساده‌ای در داخل مدل تعریف می‌کند.</p>
<p>رابطه‌ی یک‌به‌چند (hasMany / belongsTo)، رایج‌ترین نوع رابطه است:</p>
<pre><code class='language-php'>class User extends Model
{
    public function posts()
    {
        return $this-&gt;hasMany(Post::class);
    }
}

class Post extends Model
{
    public function user()
    {
        return $this-&gt;belongsTo(User::class);
    }
}</code></pre>
<p>پس از تعریف این رابطه، دسترسی به داده‌های مرتبط بسیار ساده می‌شود:</p>
<pre><code class='language-php'>$user = User::find(1);
foreach ($user-&gt;posts as $post) {
    echo $post-&gt;title;
}

$post = Post::find(1);
echo $post-&gt;user-&gt;name;</code></pre>
<p>برای رابطه‌ی چندبه‌چند (مثل مقاله و برچسب) از belongsToMany استفاده می‌شود که نیاز به یک جدول واسط دارد:</p>
<pre><code class='language-php'>class Post extends Model
{
    public function tags()
    {
        return $this-&gt;belongsToMany(Tag::class);
    }
}</code></pre>
<p>نکته‌ی مهم برای بهبود کارایی، استفاده از Eager Loading با متد with() است تا از مشکل معروف N+1 Query جلوگیری شود؛ یعنی به‌جای اجرای یک کوئری جداگانه برای هر رکورد، تمام داده‌های مرتبط در یک یا دو کوئری بارگذاری می‌شوند، برای مثال:</p>
<pre><code class='language-php'>$posts = Post::with('user')-&gt;get();</code></pre>""",
                },
            ],
        },
        {
            "title": "فصل سوم: فرم، اعتبارسنجی و احراز هویت",
            "lessons": [
                {
                    "title": "فرم و Validation",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": """<h2>اعتبارسنجی ورودی‌های کاربر</h2>
<p>یکی از قوی‌ترین بخش‌های لاراول سیستم Validation آن است که به‌سادگی امکان بررسی صحت داده‌های ارسالی از فرم را فراهم می‌کند، بدون نیاز به نوشتن شرط‌های دستی و تکراری. اعتبارسنجی معمولاً در داخل Controller و با متد validate روی شیء Request انجام می‌شود:</p>
<pre><code class='language-php'>public function store(Request $request)
{
    $validated = $request-&gt;validate([
        'title' =&gt; 'required|min:3|max:255',
        'body'  =&gt; 'required',
        'email' =&gt; 'required|email|unique:users,email',
    ]);

    Post::create($validated);

    return redirect('/posts')-&gt;with('success', 'مقاله ثبت شد');
}</code></pre>
<p>اگر داده‌ها معتبر نباشند، لاراول به‌طور خودکار کاربر را به صفحه‌ی قبلی برمی‌گرداند و پیام‌های خطا را در متغیر $errors در دسترس View قرار می‌دهد (@error در Blade این پیام‌ها را نمایش می‌دهد):</p>
<pre><code class='language-blade'>@error('title')
    &lt;span class="text-danger"&gt;{{ $message }}&lt;/span&gt;
@enderror</code></pre>
<p>برای فرم‌های پیچیده‌تر، لاراول امکان ساخت کلاس مجزای Form Request را نیز فراهم می‌کند که منطق اعتبارسنجی را از Controller جدا نگه می‌دارد:</p>
<pre><code class='language-bash'>php artisan make:request StorePostRequest</code></pre>
<p>قوانین رایج شامل required (اجباری بودن)، min و max (حداقل و حداکثر طول)، email (فرمت ایمیل معتبر) و unique (یکتا بودن مقدار در جدول) هستند. ترکیب این قوانین باعث می‌شود بدون نوشتن کد تکراری، داده‌های ورودی را قابل اعتماد نگه دارید.</p>""",
                },
                {
                    "title": "احراز هویت (Authentication)",
                    "kind": "text",
                    "minutes": 25,
                    "is_preview": False,
                    "body": """<h2>سیستم ورود و ثبت‌نام کاربران</h2>
<p>لاراول یک سیستم احراز هویت کامل و آماده برای ثبت‌نام، ورود، خروج و بازیابی رمز عبور دارد که پیاده‌سازی آن را از صفر بسیار سریع‌تر می‌کند. ابزارهای رسمی مانند Laravel Breeze یا Laravel Jetstream این قابلیت‌ها را همراه با View آماده نصب می‌کنند:</p>
<pre><code class='language-bash'>composer require laravel/breeze --dev
php artisan breeze:install
npm install &amp;&amp; npm run build
php artisan migrate</code></pre>
<p>پس از نصب، مسیرهای login، register و logout به‌طور خودکار در دسترس هستند. برای بررسی وضعیت ورود کاربر در کد خودتان می‌توانید از هلپر ()auth استفاده کنید:</p>
<pre><code class='language-php'>if (auth()-&gt;check()) {
    $user = auth()-&gt;user();
    echo "خوش آمدید " . $user-&gt;name;
} else {
    return redirect('/login');
}</code></pre>
<p>برای محدود کردن دسترسی به کل یک گروه از مسیرها به کاربران وارد‌شده، از میان‌افزار auth استفاده می‌شود که در درس بعدی با جزئیات آن آشنا می‌شوید:</p>
<pre><code class='language-php'>Route::middleware('auth')-&gt;group(function () {
    Route::get('/dashboard', [DashboardController::class, 'index']);
});</code></pre>
<p>رمزهای عبور در لاراول هرگز به‌صورت متن ساده ذخیره نمی‌شوند؛ سیستم به‌طور پیش‌فرض از الگوریتم bcrypt برای هش کردن رمز استفاده می‌کند و مقایسه‌ی رمز هنگام ورود نیز به‌صورت امن و خودکار انجام می‌شود.</p>""",
                },
                {
                    "title": "Middleware",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": """<h2>فیلتر کردن درخواست‌ها با Middleware</h2>
<p>Middleware لایه‌ای است که هر درخواست HTTP پیش از رسیدن به Controller از آن عبور می‌کند و امکان بررسی یا تغییر درخواست، یا حتی متوقف کردن آن را فراهم می‌سازد. کاربرد رایج آن بررسی ورود کاربر، بررسی نقش (role) یا لاگ کردن درخواست‌ها است.</p>
<p>لاراول چند Middleware آماده مانند auth دارد، اما ساخت یک Middleware اختصاصی نیز بسیار ساده است:</p>
<pre><code class='language-bash'>php artisan make:middleware CheckAdmin</code></pre>
<pre><code class='language-php'>class CheckAdmin
{
    public function handle($request, Closure $next)
    {
        if (! auth()-&gt;user() || ! auth()-&gt;user()-&gt;is_admin) {
            abort(403, 'دسترسی غیرمجاز');
        }

        return $next($request);
    }
}</code></pre>
<p>پس از ساخت، باید Middleware را در فایل app/Http/Kernel.php با یک نام کوتاه ثبت کنید تا بتوانید در مسیرها از آن استفاده کنید:</p>
<pre><code class='language-php'>protected $middlewareAliases = [
    'admin' =&gt; \\App\\Http\\Middleware\\CheckAdmin::class,
];</code></pre>
<p>سپس در فایل مسیرها:</p>
<pre><code class='language-php'>Route::middleware(['auth', 'admin'])-&gt;group(function () {
    Route::get('/admin/panel', [AdminController::class, 'index']);
});</code></pre>
<p>نکته‌ی کلیدی متد handle است: فراخوانی next($request) به معنای ادامه دادن زنجیره‌ی پردازش درخواست به سمت Controller است؛ اگر این خط اجرا نشود، درخواست همان‌جا متوقف می‌شود. می‌توان چند Middleware را به‌صورت زنجیره‌ای روی یک مسیر یا گروهی از مسیرها اعمال کرد.</p>""",
                },
            ],
        },
        {
            "title": "فصل چهارم: API، صف و استقرار",
            "lessons": [
                {
                    "title": "ساخت API با Resource",
                    "kind": "text",
                    "minutes": 25,
                    "is_preview": False,
                    "body": """<h2>ساخت وب‌سرویس RESTful</h2>
<p>لاراول ابزارهای قدرتمندی برای ساخت API دارد. اولین قدم، تعریف مسیرهای استاندارد CRUD در فایل routes/api.php با استفاده از Route::apiResource است که به‌طور خودکار هفت مسیر رایج (index، store، show، update، destroy و...) را می‌سازد:</p>
<pre><code class='language-php'>Route::apiResource('posts', PostController::class);</code></pre>
<p>مشکل رایج در بازگرداندن مستقیم Model به‌عنوان پاسخ JSON این است که ممکن است فیلدهای حساس یا غیرضروری (مانند رمز عبور هش‌شده) نیز فاش شوند. راه‌حل استاندارد لاراول برای این موضوع، استفاده از API Resource است:</p>
<pre><code class='language-bash'>php artisan make:resource PostResource</code></pre>
<pre><code class='language-php'>class PostResource extends JsonResource
{
    public function toArray($request)
    {
        return [
            'id'    =&gt; $this-&gt;id,
            'title' =&gt; $this-&gt;title,
            'author' =&gt; $this-&gt;user-&gt;name,
            'created_at' =&gt; $this-&gt;created_at-&gt;toDateString(),
        ];
    }
}</code></pre>
<p>سپس در Controller:</p>
<pre><code class='language-php'>public function index()
{
    return PostResource::collection(Post::with('user')-&gt;get());
}

public function show(Post $post)
{
    return new PostResource($post);
}</code></pre>
<p>این روش کنترل کاملی روی ساختار خروجی JSON به شما می‌دهد و باعث می‌شود تغییرات ساختار دیتابیس، مستقیماً روی قرارداد API تأثیر نگذارد. برای احراز هویت API معمولاً از پکیج Laravel Sanctum استفاده می‌شود که بر پایه‌ی توکن کار می‌کند.</p>""",
                },
                {
                    "title": "صف و Job",
                    "kind": "text",
                    "minutes": 20,
                    "is_preview": False,
                    "body": """<h2>پردازش وظایف سنگین با صف</h2>
<p>برخی عملیات مانند ارسال ایمیل، پردازش تصویر یا تولید گزارش ممکن است زمان زیادی طول بکشند. اگر این کارها را مستقیماً در طول یک درخواست HTTP اجرا کنید، کاربر باید منتظر بماند و تجربه‌ی کاربری بدی خواهد داشت. سیستم صف (Queue) لاراول این وظایف را به یک نوبت پردازش پس‌زمینه منتقل می‌کند تا پاسخ سریع به کاربر داده شود.</p>
<p>ابتدا باید یک درایور صف مانند database یا redis را در فایل .env تنظیم کنید:</p>
<pre><code class='language-bash'>QUEUE_CONNECTION=database
php artisan queue:table
php artisan migrate</code></pre>
<p>سپس یک Job می‌سازیم:</p>
<pre><code class='language-bash'>php artisan make:job SendWelcomeEmail</code></pre>
<pre><code class='language-php'>class SendWelcomeEmail implements ShouldQueue
{
    protected $user;

    public function __construct(User $user)
    {
        $this-&gt;user = $user;
    }

    public function handle()
    {
        Mail::to($this-&gt;user-&gt;email)-&gt;send(new WelcomeMail($this-&gt;user));
    }
}</code></pre>
<p>برای اضافه کردن این Job به صف به‌جای اجرای فوری آن:</p>
<pre><code class='language-php'>SendWelcomeEmail::dispatch($user);</code></pre>
<p>در نهایت باید یک Worker را اجرا کنید تا صف را پردازش کند:</p>
<pre><code class='language-bash'>php artisan queue:work</code></pre>
<p>در محیط عملیاتی (production) معمولاً از ابزاری مانند Supervisor برای اجرای دائمی و مانیتور شدن این Worker استفاده می‌شود تا در صورت خطا به‌طور خودکار مجدداً اجرا شود.</p>""",
                },
                {
                    "title": "استقرار پروژه لاراول",
                    "kind": "text",
                    "minutes": 25,
                    "is_preview": False,
                    "body": """<h2>آماده‌سازی و انتشار پروژه روی سرور</h2>
<p>پس از توسعه، پروژه‌ی لاراول باید روی یک سرور واقعی مستقر (deploy) شود. مراحل استقرار شامل انتقال کد، نصب وابستگی‌ها، تنظیم فایل محیطی و پیکربندی وب‌سرور است. ابتدا کد را روی سرور کلون کرده و وابستگی‌ها را برای محیط عملیاتی نصب می‌کنیم:</p>
<pre><code class='language-bash'>git clone https://example.com/repo.git
cd repo
composer install --optimize-autoloader --no-dev</code></pre>
<p>سپس فایل .env را با تنظیمات واقعی سرور (اطلاعات دیتابیس، آدرس سایت و کلید APP_KEY) پیکربندی می‌کنیم و مطمئن می‌شویم APP_DEBUG روی false تنظیم شده تا جزئیات فنی خطاها برای کاربران عادی نمایش داده نشود:</p>
<pre><code class='language-bash'>cp .env.example .env
php artisan key:generate
php artisan migrate --force</code></pre>
<p>برای بهبود کارایی در محیط عملیاتی، لاراول دستوراتی برای کش کردن تنظیمات، مسیرها و View فراهم می‌کند که باعث کاهش زمان پاسخ‌دهی می‌شود:</p>
<pre><code class='language-bash'>php artisan config:cache
php artisan route:cache
php artisan view:cache</code></pre>
<p>در نهایت باید Document Root وب‌سرور (Nginx یا Apache) به پوشه‌ی public پروژه اشاره کند، نه ریشه‌ی پروژه، تا فایل‌های حساس مانند .env در دسترس عمومی قرار نگیرند. تنظیم HTTPS با گواهی SSL و اجرای صف به‌صورت دائمی با Supervisor نیز از الزامات یک استقرار حرفه‌ای است.</p>""",
                },
            ],
        },
    ],
}

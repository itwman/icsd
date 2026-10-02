"""
تنظیمات پروژه‌ی ICSD
لوکال: SQLite بدون هیچ نصبی.  سرور: با تعریف POSTGRES_DB در .env به پستگرس سوییچ می‌کند.
"""
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


# ── .env ساده، بدون وابستگی ─────────────────────────────────────────
def _load_env(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


_load_env(BASE_DIR / ".env")


def env(key: str, default=None):
    return os.environ.get(key, default)


def env_bool(key: str, default=False) -> bool:
    return str(env(key, default)).lower() in ("1", "true", "yes", "on")


# ── پایه ────────────────────────────────────────────────────────────
SECRET_KEY = env("SECRET_KEY", "dev-only-change-me-in-production-9f3k2j1h")
DEBUG = env_bool("DEBUG", True)
ALLOWED_HOSTS = [h for h in env("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",") if h]
CSRF_TRUSTED_ORIGINS = [o for o in env("CSRF_TRUSTED_ORIGINS", "").split(",") if o]
# دامنه‌ی اصلی؛ بقیه‌ی دامنه‌های ALLOWED_HOSTS با ۳۰۱ به آن می‌روند (مثلاً icsd.ir)
CANONICAL_HOST = env("CANONICAL_HOST", "")

INSTALLED_APPS = [
    "unfold",
    "unfold.contrib.filters",
    "unfold.contrib.forms",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "django.contrib.syndication",
    "django.contrib.humanize",
    "django_ckeditor_5",
    # اپ‌های پروژه
    "apps.common",
    "apps.core",
    "apps.accounts",
    "apps.academy",
    "apps.products",
    "apps.blog",
    "apps.team",
    "apps.leads",
    "apps.payments",
    "apps.analytics",
    "apps.seo",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "apps.seo.middleware.CanonicalHostMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "apps.analytics.middleware.PageViewMiddleware",
    "apps.seo.middleware.RedirectMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "apps.core.context_processors.site",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# ── دیتابیس ─────────────────────────────────────────────────────────
if env("POSTGRES_DB"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": env("POSTGRES_DB"),
            "USER": env("POSTGRES_USER", "postgres"),
            "PASSWORD": env("POSTGRES_PASSWORD", ""),
            "HOST": env("POSTGRES_HOST", "127.0.0.1"),
            "PORT": env("POSTGRES_PORT", "5432"),
            "CONN_MAX_AGE": 60,
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ── کاربر و احراز هویت ──────────────────────────────────────────────
AUTH_USER_MODEL = "accounts.User"
AUTHENTICATION_BACKENDS = ["apps.accounts.backends.MobileOrEmailBackend"]
LOGIN_URL = "accounts:login"
LOGIN_REDIRECT_URL = "accounts:dashboard"
LOGOUT_REDIRECT_URL = "core:home"

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", "OPTIONS": {"min_length": 6}},
]

# ── زبان و زمان ─────────────────────────────────────────────────────
LANGUAGE_CODE = "fa"
TIME_ZONE = "Asia/Tehran"
USE_I18N = True
USE_TZ = True

# ── استاتیک و مدیا (همه محلی) ───────────────────────────────────────
WHITENOISE_MAX_AGE = 60 * 60 * 24 * 7  # یک هفته کش مرورگر برای css/js/فونت
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedStaticFilesStorage"},
}
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
DATA_UPLOAD_MAX_MEMORY_SIZE = 50 * 1024 * 1024
FILE_UPLOAD_MAX_MEMORY_SIZE = 50 * 1024 * 1024

# ── پیامک و پرداخت (مقادیر واقعی در .env یا تنظیمات سایت) ───────────
SMS_PROVIDER = env("SMS_PROVIDER", "console")          # console | kavenegar
KAVENEGAR_API_KEY = env("KAVENEGAR_API_KEY", "")
KAVENEGAR_SENDER = env("KAVENEGAR_SENDER", "")
OTP_TTL_SECONDS = 180

ZARINPAL_MERCHANT_ID = env("ZARINPAL_MERCHANT_ID", "")
ZARINPAL_SANDBOX = env_bool("ZARINPAL_SANDBOX", True)

# ── امنیت روی سرور ──────────────────────────────────────────────────
if not DEBUG:
    # تا وقتی گواهی SSL نگرفته‌اید HTTPS_ENABLED=False بماند؛ بعد از certbot روی True بگذارید.
    HTTPS = env_bool("HTTPS_ENABLED", False)
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SESSION_COOKIE_SECURE = HTTPS
    CSRF_COOKIE_SECURE = HTTPS
    SECURE_SSL_REDIRECT = HTTPS and env_bool("SECURE_SSL_REDIRECT", True)
    # HSTS پیش‌فرض خاموش؛ includeSubDomains روی دامنه‌ی اصلی می‌تواند زیردامنه‌های دیگرِ همین سرور را بشکند.
    SECURE_HSTS_SECONDS = int(env("HSTS_SECONDS", "0"))
    SECURE_HSTS_INCLUDE_SUBDOMAINS = env_bool("HSTS_INCLUDE_SUBDOMAINS", False)
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"
    X_FRAME_OPTIONS = "SAMEORIGIN"

# ── ویرایشگر متن (محلی، بدون CDN) ───────────────────────────────────
CKEDITOR_5_CUSTOM_CSS = "css/ckeditor-rtl.css"
CKEDITOR_5_FILE_UPLOAD_PERMISSION = "staff"
CKEDITOR_5_CONFIGS = {
    # ویرایشگر کامل، شبیه ویرایشگر کلاسیک وردپرس: تیتر، قالب‌بندی، لینک، تصویر با متن جایگزین و زیرنویس،
    # جدول، ویدیو (آپارات/یوتیوب با «کد HTML»)، کد، نقل‌قول، جست‌وجو و جایگزینی، شمارش کلمات و نمایش کد HTML.
    "default": {
        "language": {"ui": "fa", "content": "fa"},
        "toolbar": {
            "items": [
                "heading", "|", "bold", "italic", "underline", "strikethrough", "link", "highlight", "fontColor", "removeFormat", "|",
                "alignment", "bulletedList", "numberedList", "todoList", "outdent", "indent", "|",
                "insertImage", "insertTable", "mediaEmbed", "htmlEmbed", "blockQuote", "codeBlock", "horizontalLine", "specialCharacters", "|",
                "findAndReplace", "sourceEditing", "showBlocks", "undo", "redo",
            ],
            "shouldNotGroupWhenFull": True,
        },
        "heading": {
            "options": [
                {"model": "paragraph", "title": "پاراگراف", "class": "ck-heading_paragraph"},
                {"model": "heading2", "view": "h2", "title": "تیتر ۲ (بخش اصلی)", "class": "ck-heading_heading2"},
                {"model": "heading3", "view": "h3", "title": "تیتر ۳ (زیربخش)", "class": "ck-heading_heading3"},
                {"model": "heading4", "view": "h4", "title": "تیتر ۴", "class": "ck-heading_heading4"},
            ]
        },
        "image": {
            "toolbar": ["imageTextAlternative", "toggleImageCaption", "|", "imageStyle:inline", "imageStyle:alignRight",
                        "imageStyle:alignCenter", "imageStyle:alignLeft", "|", "resizeImage", "linkImage"],
            "resizeUnit": "%",
        },
        "table": {"contentToolbar": ["tableColumn", "tableRow", "mergeTableCells", "tableProperties", "tableCellProperties", "toggleTableCaption"]},
        "list": {"properties": {"styles": True, "startIndex": True, "reversed": True}},
        "link": {"addTargetToExternalLinks": True, "defaultProtocol": "https://",
                 "decorators": {"nofollow": {"mode": "manual", "label": "nofollow (لینک تبلیغاتی/غیرقابل اعتماد)", "attributes": {"rel": "nofollow"}}}},
        "mediaEmbed": {"previewsInData": True},
        "htmlEmbed": {"showPreviews": False},
        "wordCount": {"displayWords": True, "displayCharacters": False},
        "codeBlock": {
            "languages": [
                {"language": "python", "label": "Python"},
                {"language": "bash", "label": "Bash"},
                {"language": "powershell", "label": "PowerShell"},
                {"language": "sql", "label": "SQL"},
                {"language": "php", "label": "PHP"},
                {"language": "javascript", "label": "JavaScript"},
                {"language": "html", "label": "HTML"},
                {"language": "css", "label": "CSS"},
                {"language": "json", "label": "JSON"},
                {"language": "plaintext", "label": "متن ساده"},
            ]
        },
        "htmlSupport": {"allow": [{"name": "iframe", "attributes": True}, {"name": "/^(div|span|p|h[2-4]|a|img|figure|table|td|th)$/", "attributes": ["id", "dir", "lang"], "classes": True}]},
    }
}
CKEDITOR_5_UPLOAD_FILE_TYPES = ["jpeg", "jpg", "png", "gif", "webp"]
CKEDITOR_5_MAX_FILE_SIZE = 3  # مگابایت

# ── پنل مدیریت ──────────────────────────────────────────────────────
from config.unfold import UNFOLD  # noqa: E402,F401

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"
from django.contrib.messages import constants as _mc  # noqa: E402
MESSAGE_TAGS = {_mc.DEBUG: "secondary", _mc.INFO: "info", _mc.SUCCESS: "success", _mc.WARNING: "warning", _mc.ERROR: "danger"}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {"handlers": ["console"], "level": "INFO"},
}

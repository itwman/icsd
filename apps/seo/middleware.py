import re
from urllib.parse import unquote

from django.conf import settings
from django.db.models import F
from django.http import HttpResponseGone, HttpResponsePermanentRedirect, HttpResponseRedirect

# درخواست‌های بی‌ارزش ربات‌ها و اسکنرها در نمایشگر ۴۰۴ ثبت نمی‌شوند
JUNK = re.compile(r"(^/(static|media|admin|ckeditor5|api)/)|wp-(admin|login|includes|content/plugins)|xmlrpc|\.(php|env|asp|aspx|jsp|cgi|ini|bak|sql|git)\b|/\.|favicon|apple-touch", re.I)


class RedirectMiddleware:
    """روی ۴۰۴: اول جدول ریدایرکت (با و بدون / انتهایی، فارسیِ decode شده)، وگرنه ثبت در نمایشگر ۴۰۴."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code != 404:
            return response
        from .models import NotFoundLog, Redirect
        raw = request.path
        candidates = {raw, unquote(raw)}
        for p in list(candidates):
            candidates.add(p.rstrip("/") + "/" if not p.endswith("/") else p.rstrip("/") or "/")
        r = Redirect.objects.filter(old_path__in=candidates, is_active=True).first()
        if r:
            Redirect.objects.filter(pk=r.pk).update(hits=F("hits") + 1)
            if r.status_code == 410 or not r.new_path:
                return HttpResponseGone("این صفحه حذف شده است.")
            target = r.new_path
            if request.META.get("QUERY_STRING") and "?" not in target:
                target += "?" + request.META["QUERY_STRING"]
            return HttpResponseRedirect(target) if r.status_code == 302 else HttpResponsePermanentRedirect(target)

        path = unquote(raw)[:300]
        if request.method == "GET" and not JUNK.search(path):
            try:
                ref = request.META.get("HTTP_REFERER", "")[:300]
                updated = NotFoundLog.objects.filter(path=path).update(hits=F("hits") + 1, referrer=ref or F("referrer"))
                if not updated:
                    NotFoundLog.objects.create(path=path, referrer=ref)
            except Exception:
                pass
        return response


class CanonicalHostMiddleware:
    """همه‌ی دامنه‌های فرعی (www.icsd.ir، new.icsd.ir) با ۳۰۱ به دامنه‌ی اصلی می‌روند تا گوگل محتوای تکراری نبیند.
    دامنه‌ی اصلی از CANONICAL_HOST در .env خوانده می‌شود؛ خالی = غیرفعال."""

    def __init__(self, get_response):
        self.get_response = get_response
        self.host = (getattr(settings, "CANONICAL_HOST", "") or "").lower()

    def __call__(self, request):
        if self.host:
            host = request.get_host().split(":")[0].lower()
            if host != self.host and host not in ("127.0.0.1", "localhost"):
                scheme = "https" if request.is_secure() else "http"
                return HttpResponsePermanentRedirect(f"{scheme}://{self.host}{request.get_full_path()}")
        return self.get_response(request)

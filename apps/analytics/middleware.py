"""ثبت بازدید صفحات HTML — بدون ذخیره‌ی IP خام (فقط هش روزانه)."""
import hashlib
from datetime import date

from django.conf import settings

SKIP_PREFIXES = ("/admin", "/panel", "/static", "/media", "/api/", "/ckeditor5", "/sitemap", "/robots", "/favicon")
BOT_HINTS = ("bot", "crawl", "spider", "slurp", "curl", "wget", "python-requests", "headless")


class PageViewMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        try:
            self._record(request, response)
        except Exception:
            pass  # آمار هرگز نباید سایت را بیندازد
        return response

    def _record(self, request, response):
        if request.method != "GET" or response.status_code != 200:
            return
        if not response.get("Content-Type", "").startswith("text/html"):
            return
        path = request.path
        if path.startswith(SKIP_PREFIXES):
            return
        ua = request.META.get("HTTP_USER_AGENT", "")[:300]
        ua_l = ua.lower()
        if any(h in ua_l for h in BOT_HINTS):
            device = "bot"
        elif "mobile" in ua_l or "android" in ua_l or "iphone" in ua_l:
            device = "mobile"
        else:
            device = "desktop"

        ip = request.META.get("HTTP_X_FORWARDED_FOR", "").split(",")[0].strip() or request.META.get("REMOTE_ADDR", "")
        ip_hash = hashlib.sha256(f"{ip}|{date.today()}|{settings.SECRET_KEY[:8]}".encode()).hexdigest()[:32]

        if not request.session.session_key:
            request.session.save()

        from .models import PageView
        PageView.objects.create(
            path=path[:300],
            referrer=request.META.get("HTTP_REFERER", "")[:300],
            user_agent=ua, device=device, ip_hash=ip_hash,
            session_key=request.session.session_key or "",
            user=request.user if request.user.is_authenticated else None,
        )

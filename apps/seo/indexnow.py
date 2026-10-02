"""IndexNow — خبر دادن فوری انتشار/ویرایش صفحه به Bing، Yandex، Seznam و Naver.
(گوگل IndexNow را پشتیبانی نمی‌کند؛ برای گوگل sitemap.xml و سرچ‌کنسول کافی است.)
کلید در «تنظیمات سایت ← سئو» قرار می‌گیرد؛ فایل تأیید در /<کلید>.txt خودکار سرو می‌شود."""
import json
import logging
import threading
import urllib.request

log = logging.getLogger(__name__)


def ping(urls):
    from apps.core.models import SiteSettings
    site = SiteSettings.load()
    key = (site.indexnow_key or "").strip()
    if not key or not urls:
        return
    base = site.site_url.rstrip("/")
    host = base.split("://", 1)[-1].split("/", 1)[0]
    if host in ("", "localhost", "127.0.0.1") or host.startswith("127."):
        return
    payload = {"host": host, "key": key, "keyLocation": f"{base}/{key}.txt",
               "urlList": [u if u.startswith("http") else base + u for u in urls]}

    def _send():
        try:
            req = urllib.request.Request("https://api.indexnow.org/indexnow", data=json.dumps(payload).encode(),
                                         headers={"Content-Type": "application/json; charset=utf-8"})
            urllib.request.urlopen(req, timeout=8)
        except Exception as e:  # شبکه‌ی سرور ممکن است بسته باشد؛ مهم نیست
            log.info("IndexNow skipped: %s", e)

    threading.Thread(target=_send, daemon=True).start()

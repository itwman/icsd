"""ارسال پیامک — لوکال: چاپ در ترمینال. سرور: کاوه‌نگار (یا هر سرویسی که بعداً اضافه کنید)."""
import logging

import requests
from django.conf import settings

log = logging.getLogger(__name__)


def _cfg(name, fallback):
    """اول تنظیمات سایت (پنل)، بعد .env"""
    try:
        from apps.core.models import SiteSettings
        v = getattr(SiteSettings.load(), name, "")
        if v:
            return v
    except Exception:  # قبل از migrate
        pass
    return fallback


def send_otp(mobile: str, code: str) -> bool:
    provider = settings.SMS_PROVIDER
    api_key = _cfg("kavenegar_api_key", settings.KAVENEGAR_API_KEY)
    if provider == "kavenegar" and api_key:
        return _kavenegar(api_key, mobile, code)
    # حالت کنسول
    print(f"\n[SMS → {mobile}] کد ورود شما: {code}\n")
    log.info("OTP for %s: %s", mobile, code)
    return True


def _kavenegar(api_key: str, mobile: str, code: str) -> bool:
    """
    ارسال با «الگوی تأیید» کاوه‌نگار. الگویی به نام otp با متغیر token بسازید.
    """
    url = f"https://api.kavenegar.com/v1/{api_key}/verify/lookup.json"
    try:
        r = requests.get(url, params={"receptor": mobile, "token": code, "template": "otp"}, timeout=10)
        ok = r.status_code == 200 and r.json().get("return", {}).get("status") == 200
        if not ok:
            log.error("Kavenegar error: %s", r.text[:300])
        return ok
    except requests.RequestException as e:
        log.exception("Kavenegar request failed: %s", e)
        return False

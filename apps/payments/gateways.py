"""
لایه‌ی انتزاعی درگاه. برای افزودن درگاه جدید فقط یک کلاس با request/verify بنویسید
و در GATEWAYS ثبت کنید.
"""
import logging

import requests
from django.conf import settings

log = logging.getLogger(__name__)


class GatewayError(Exception):
    pass


def _site_cfg(name, fallback):
    try:
        from apps.core.models import SiteSettings
        v = getattr(SiteSettings.load(), name, None)
        if v not in (None, ""):
            return v
    except Exception:
        pass
    return fallback


class Zarinpal:
    name = "zarinpal"

    def __init__(self):
        self.merchant = _site_cfg("zarinpal_merchant_id", settings.ZARINPAL_MERCHANT_ID)
        self.sandbox = bool(_site_cfg("zarinpal_sandbox", settings.ZARINPAL_SANDBOX))
        base = "https://sandbox.zarinpal.com" if self.sandbox else "https://payment.zarinpal.com"
        self.api = f"{base}/pg/v4/payment"
        self.start_url = f"{base}/pg/StartPay/"

    def request(self, amount_toman: int, callback_url: str, description: str, mobile: str = "") -> str:
        """مبلغ به ریال ارسال می‌شود. خروجی: authority"""
        if not self.merchant:
            raise GatewayError("مرچنت زرین‌پال تنظیم نشده است (تنظیمات سایت یا .env).")
        payload = {
            "merchant_id": self.merchant,
            "amount": amount_toman * 10,
            "currency": "IRR",
            "callback_url": callback_url,
            "description": description[:250],
            "metadata": {"mobile": mobile},
        }
        try:
            r = requests.post(f"{self.api}/request.json", json=payload, timeout=15)
            data = r.json().get("data") or {}
            if data.get("code") == 100 and data.get("authority"):
                return data["authority"]
            raise GatewayError(f"زرین‌پال: {r.json().get('errors') or r.text[:200]}")
        except requests.RequestException as e:
            raise GatewayError(f"اتصال به درگاه برقرار نشد: {e}")

    def pay_url(self, authority: str) -> str:
        return self.start_url + authority

    def verify(self, amount_toman: int, authority: str) -> dict:
        """خروجی: {'ok': bool, 'ref_id': str, 'card_pan': str}"""
        payload = {"merchant_id": self.merchant, "amount": amount_toman * 10, "authority": authority}
        try:
            r = requests.post(f"{self.api}/verify.json", json=payload, timeout=15)
            data = r.json().get("data") or {}
            # 100 = موفق، 101 = قبلاً تأیید شده
            if data.get("code") in (100, 101):
                return {"ok": True, "ref_id": str(data.get("ref_id", "")), "card_pan": data.get("card_pan", "")}
            log.warning("Zarinpal verify failed: %s", r.text[:300])
            return {"ok": False, "ref_id": "", "card_pan": ""}
        except requests.RequestException as e:
            log.exception("Zarinpal verify error: %s", e)
            return {"ok": False, "ref_id": "", "card_pan": ""}


GATEWAYS = {"zarinpal": Zarinpal}


def get_gateway(name="zarinpal"):
    return GATEWAYS[name]()

#!/usr/bin/env bash
# بررسی فقط‌خواندنی سرور — هیچ چیزی را تغییر نمی‌دهد. خروجی را برای ما بفرستید.
#   bash check_server.sh new.icsd.ir
DOMAIN="${1:-new.icsd.ir}"
echo "=== سیستم ==="; lsb_release -ds 2>/dev/null; uname -r; nproc; free -h | head -2; df -h / | tail -1
echo "=== پنل میزبانی؟ ==="
for d in /usr/local/directadmin /usr/local/cpanel /www/server/panel /usr/local/psa /usr/local/CyberCP /usr/local/hestia /usr/local/vesta; do [ -d "$d" ] && echo "پیدا شد: $d"; done
echo "=== وب‌سرورها ==="
for s in nginx apache2 httpd litespeed lsws openresty; do printf "%-10s %s\n" "$s" "$(systemctl is-active $s 2>/dev/null)"; done
ss -ltnp 2>/dev/null | awk 'NR==1 || /:80 |:443 |:5432 |:3306 |:8000 |:8001 /'
echo "=== پیکربندی nginx ==="
ls -1 /etc/nginx/sites-enabled/ 2>/dev/null; ls -1 /etc/nginx/conf.d/ 2>/dev/null
echo "--- دامنه‌های icsd در nginx:"; grep -RHn "server_name" /etc/nginx/ 2>/dev/null | grep -i "icsd" || echo "(هیچ)"
echo "--- آیا $DOMAIN قبلاً تعریف شده؟"; grep -RHln "$DOMAIN" /etc/nginx/ /etc/apache2/ 2>/dev/null || echo "خیر"
echo "=== پایتون ==="; for p in python3 python3.10 python3.11 python3.12; do command -v $p >/dev/null && echo "$p: $($p --version 2>&1)"; done
apt-cache policy python3.11 2>/dev/null | head -3
echo "=== پستگرس ==="; command -v psql >/dev/null && psql --version || echo "نصب نیست"; systemctl is-active postgresql 2>/dev/null
echo "=== سرویس‌های جنگوی موجود (gunicorn/uwsgi) ==="; systemctl list-units --type=service --no-pager 2>/dev/null | grep -Ei "gunicorn|uwsgi|django|daphne|uvicorn" || echo "(هیچ)"
echo "=== certbot ==="; command -v certbot >/dev/null && certbot --version 2>&1 || echo "نصب نیست"
echo "=== DNS دامنه ==="; getent hosts "$DOMAIN" || echo "$DOMAIN هنوز به IPی اشاره نمی‌کند"; curl -s -m 5 ifconfig.me 2>/dev/null && echo " ← IP این سرور"
echo "=== دسترسی به گیت‌هاب و PyPI ==="
curl -s -m 8 -o /dev/null -w "github.com: %{http_code}\n" https://github.com
curl -s -m 8 -o /dev/null -w "pypi.org: %{http_code}\n" https://pypi.org/simple/django/
curl -s -m 8 -o /dev/null -w "mirror-pypi.runflare.com: %{http_code}\n" https://mirror-pypi.runflare.com/simple/django/
echo "=== تمام. هیچ تغییری ایجاد نشد. ==="

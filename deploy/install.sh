#!/usr/bin/env bash
# نصب ایزوله‌ی سایت ICSD روی سرور اشتراکی — به سایت‌های دیگر دست نمی‌زند.
#   sudo DOMAIN=new.icsd.ir DB_PASS='یک-رمز-قوی' bash install.sh
# کاربر جدا (icsd)، پوشه‌ی جدا (/srv/icsd)، پایتون/venv جدا، دیتابیس و کاربر پستگرس جدا،
# سرویس systemd جدا (icsd) با سوکت یونیکس (بدون اشغال پورت)، و یک فایل nginx جدا فقط برای همین دامنه.
set -euo pipefail
DOMAIN="${DOMAIN:?DOMAIN را بدهید، مثلاً DOMAIN=new.icsd.ir}"
DB_PASS="${DB_PASS:?DB_PASS را بدهید}"
REPO="${REPO:-https://github.com/itwman/icsd.git}"
BRANCH="${BRANCH:-main}"
APP_USER=icsd; BASE=/srv/icsd; APP=$BASE/app; VENV=$BASE/venv
PIP_INDEX="${PIP_INDEX_URL:-https://mirror-pypi.runflare.com/simple}"
say() { echo -e "\n\033[1;32m▶ $*\033[0m"; }
die() { echo -e "\033[1;31m✗ $*\033[0m"; exit 1; }

[ "$(id -u)" = 0 ] || die "با sudo اجرا کنید."
command -v nginx >/dev/null || die "nginx پیدا نشد. خروجی check_server.sh را بفرستید؛ این اسکریپت برای سرور با nginx است."
if grep -RqsE "server_name[^;]*\b${DOMAIN//./\\.}\b" /etc/nginx/ && [ ! -f /etc/nginx/sites-available/icsd ]; then
  die "دامنه‌ی $DOMAIN قبلاً در nginx تعریف شده. برای امنیت سایت فعلی متوقف شدم."
fi

say "۱. پایتون ۳.۱۱+ (کنار پایتون سیستم؛ پایتون سیستم عوض نمی‌شود)"
PY=""
for p in python3.12 python3.11; do command -v $p >/dev/null && { PY=$p; break; }; done
if [ -z "$PY" ]; then
  apt-get update -qq
  apt-get install -y -qq python3.11 python3.11-venv python3.11-dev && PY=python3.11
fi
$PY -c 'import sys; assert sys.version_info >= (3, 11)' || die "پایتون ۳.۱۱ نصب نشد."
$PY -m venv --help >/dev/null 2>&1 || apt-get install -y -qq "${PY}-venv"
apt-get install -y -qq git libpq5 >/dev/null

say "۲. کاربر و پوشه‌ی جدا"
id -u $APP_USER >/dev/null 2>&1 || useradd --system --create-home --home-dir $BASE --shell /usr/sbin/nologin $APP_USER
mkdir -p $BASE/media $BASE/logs; chown -R $APP_USER:$APP_USER $BASE; chmod 755 $BASE

say "۳. کد از گیت‌هاب"
if [ -d $APP/.git ]; then sudo -u $APP_USER git -C $APP pull --ff-only
else sudo -u $APP_USER git clone --branch "$BRANCH" "$REPO" $APP; fi

say "۴. محیط مجازی و کتابخانه‌ها"
[ -x $VENV/bin/python ] || sudo -u $APP_USER $PY -m venv $VENV
sudo -u $APP_USER $VENV/bin/pip install -q --upgrade pip -i "$PIP_INDEX" || sudo -u $APP_USER $VENV/bin/pip install -q --upgrade pip
sudo -u $APP_USER $VENV/bin/pip install -q -r $APP/requirements.txt -i "$PIP_INDEX" || sudo -u $APP_USER $VENV/bin/pip install -q -r $APP/requirements.txt

say "۵. پستگرس: کاربر و دیتابیس جدا (icsd)"
if ! command -v psql >/dev/null; then apt-get install -y -qq postgresql; fi
sudo -u postgres psql -tAc "SELECT 1 FROM pg_roles WHERE rolname='icsd'" | grep -q 1 || sudo -u postgres psql -qc "CREATE ROLE icsd LOGIN PASSWORD '$DB_PASS';"
sudo -u postgres psql -tAc "SELECT 1 FROM pg_database WHERE datname='icsd'" | grep -q 1 || sudo -u postgres psql -qc "CREATE DATABASE icsd OWNER icsd ENCODING 'UTF8' TEMPLATE template0;"

say "۶. فایل .env"
if [ ! -f $APP/.env ]; then
  SECRET=$($VENV/bin/python -c 'import secrets; print(secrets.token_urlsafe(50))')
  cat > $APP/.env <<ENV
SECRET_KEY=$SECRET
DEBUG=False
ALLOWED_HOSTS=$DOMAIN
CSRF_TRUSTED_ORIGINS=http://$DOMAIN,https://$DOMAIN
HTTPS_ENABLED=False
POSTGRES_DB=icsd
POSTGRES_USER=icsd
POSTGRES_PASSWORD=$DB_PASS
POSTGRES_HOST=127.0.0.1
POSTGRES_PORT=5432
SMS_PROVIDER=console
ZARINPAL_SANDBOX=True
ENV
  chown $APP_USER:$APP_USER $APP/.env; chmod 600 $APP/.env
fi
ln -sfn $BASE/media $APP/media; chmod 755 $APP; chgrp -R www-data $BASE/media; chmod 2775 $BASE/media

say "۷. دیتابیس، فایل‌های استاتیک و داده‌های اولیه"
M() { sudo -u $APP_USER bash -c "cd $APP && $VENV/bin/python manage.py $*"; }
M migrate --noinput
M collectstatic --noinput -v0
M seed_site; M seed_products; M seed_team; M import_wp_posts; M seed_geo; M seed_courses; M seed_quizzes; M setup_roles
M shell -c "\"from apps.core.models import SiteSettings as S; s=S.load(); s.site_url='http://$DOMAIN'; s.save()\""

say "۸. سرویس systemd (icsd) — فقط همین سرویس"
cp $APP/deploy/icsd.service /etc/systemd/system/icsd.service
systemctl daemon-reload; systemctl enable --now icsd; sleep 2
systemctl is-active --quiet icsd || { journalctl -u icsd -n 30 --no-pager; die "سرویس بالا نیامد."; }

say "۹. nginx — یک فایل جدا فقط برای $DOMAIN"
sed "s/__DOMAIN__/$DOMAIN/g" $APP/deploy/nginx-icsd.conf > /etc/nginx/sites-available/icsd
ln -sfn /etc/nginx/sites-available/icsd /etc/nginx/sites-enabled/icsd
if nginx -t 2>&1; then systemctl reload nginx
else rm -f /etc/nginx/sites-enabled/icsd; die "پیکربندی nginx خطا داشت؛ فایل icsd برداشته شد و سایت‌های دیگر دست نخوردند."; fi

say "تمام ✓  http://$DOMAIN  —  حالا مدیر بسازید:  sudo -u icsd $VENV/bin/python $APP/manage.py createsuperuser"
echo "برای SSL:  sudo certbot --nginx -d $DOMAIN   سپس در $APP/.env مقدار HTTPS_ENABLED=True و site_url را https کنید و: sudo systemctl restart icsd"

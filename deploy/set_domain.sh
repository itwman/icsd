#!/usr/bin/env bash
# انتقال سایت جنگو به دامنه‌ی اصلی (مثلاً icsd.ir) — دو بار اجرا می‌شود:
#   sudo DOMAIN=icsd.ir bash /srv/icsd/app/deploy/set_domain.sh
#   بار اول (DNS هنوز روی سرور قدیم): سایت برای icsd.ir آماده می‌شود و تصاویر وردپرس کپی می‌شوند.
#   بعد DNS را عوض کنید و همین دستور را دوباره بزنید: nginx + SSL + ریدایرکت www و new به دامنه‌ی اصلی.
# فقط فایل‌های خود icsd را تغییر می‌دهد؛ سایت‌های دیگر دست نمی‌خورند.
set -euo pipefail
export NEEDRESTART_MODE=l NEEDRESTART_SUSPEND=1 DEBIAN_FRONTEND=noninteractive
cd /tmp
DOMAIN="${DOMAIN:?DOMAIN را بدهید، مثلاً DOMAIN=icsd.ir}"
BASE=/srv/icsd; APP=$BASE/app; VENV=$BASE/venv; ENVF=$APP/.env
AV=/etc/nginx/sites-available; EN=/etc/nginx/sites-enabled
say() { echo -e "\n\033[1;32m▶ $*\033[0m"; }
die() { echo -e "\033[1;31m✗ $*\033[0m"; exit 1; }
[ "$(id -u)" = 0 ] || die "با sudo اجرا کنید."
[ -f $ENVF ] || die "$ENVF پیدا نشد؛ اول install.sh را اجرا کنید."

set_env() { if grep -q "^$1=" $ENVF; then sed -i "s|^$1=.*|$1=$2|" $ENVF; else echo "$1=$2" >> $ENVF; fi; }
M() { sudo -u icsd bash -c "cd $APP && $VENV/bin/python manage.py $*"; }
site_url() { M shell -c "\"from apps.core.models import SiteSettings as S; s=S.load(); s.site_url='$1'; s.save()\""; }

# همه‌ی نام‌ها: دامنه‌ی اصلی، www و دامنه‌های قبلی (مثل new.icsd.ir) تا به اصلی ریدایرکت شوند
OLD=$(grep -E '^ALLOWED_HOSTS=' $ENVF | cut -d= -f2 | tr ',' ' ')
NAMES=$(echo "$DOMAIN www.$DOMAIN $OLD" | tr ' ' '\n' | grep -vE '^(|127\.0\.0\.1|localhost)$' | awk '!s[$0]++' | tr '\n' ' ' | sed 's/ $//')
[ -n "$NAMES" ] || die "فهرست دامنه‌ها خالی است."
say "دامنه‌ها: $NAMES"
set_env ALLOWED_HOSTS "$(echo $NAMES | tr ' ' ',')"
set_env CSRF_TRUSTED_ORIGINS "$(for n in $NAMES; do printf 'https://%s,http://%s,' $n $n; done | sed 's/,$//')"

say "به‌روزرسانی کد"
sudo -u icsd git -C $APP pull --ff-only
M migrate --noinput; M collectstatic --noinput -v0

# دامنه نباید در فایل nginx سایت دیگری تعریف شده باشد
D_RE="${DOMAIN//./\\.}"
OTHER=$(grep -RlsE "server_name[^;]*(\s)(www\.)?$D_RE(\s|;)" /etc/nginx/sites-enabled/ /etc/nginx/conf.d/ 2>/dev/null | grep -vE '/icsd(-pre)?$' || true)
[ -z "$OTHER" ] || die "دامنه‌ی $DOMAIN در این فایل(ها)ی nginx هم تعریف شده: $OTHER — برای امنیت آن سایت متوقف شدم."

RES=$(getent ahostsv4 "$DOMAIN" | awk 'NR==1{print $1}')
if [ "${PHASE:-}" != 2 ] && ! hostname -I | tr ' ' '\n' | grep -qx "$RES"; then
  # ─── مرحله‌ی ۱: DNS هنوز روی سرور قدیم است ───
  say "۱. کپی تصاویر وردپرس از سایت فعلی ($RES)"
  mkdir -p $BASE/media/wp-uploads; chown icsd:www-data $BASE/media/wp-uploads
  sudo -u icsd $VENV/bin/python $APP/deploy/fetch_wp_uploads.py "https://$DOMAIN" $BASE/media/wp-uploads || echo "  (کپی تصاویر کامل نشد؛ با اجرای دوباره ادامه می‌دهد)"

  say "۲. آماده‌سازی nginx برای $DOMAIN (فایل موقت جدا؛ فایل فعلی new.icsd.ir دست نمی‌خورد)"
  sed "s/__DOMAIN__/$DOMAIN www.$DOMAIN/; s/icsd\.access\.log/icsd-pre.access.log/; s/icsd\.error\.log/icsd-pre.error.log/" $APP/deploy/nginx-icsd.conf > $AV/icsd-pre
  ln -sfn $AV/icsd-pre $EN/icsd-pre
  if nginx -t 2>&1; then systemctl reload nginx
  else rm -f $EN/icsd-pre $AV/icsd-pre; die "nginx خطا داشت؛ فایل موقت برداشته شد و چیزی تغییر نکرد."; fi
  systemctl restart icsd

  echo -e "\n\033[1;33mحالا در Cloudflare رکوردهای A برای icsd.ir و www را به $(hostname -I | awk '{print $1}') تغییر دهید (ابر خاکستری / DNS only)،"
  echo -e "یکی دو دقیقه صبر کنید و همین دستور را دوباره اجرا کنید تا SSL گرفته شود.\033[0m"
  exit 0
fi

# ─── مرحله‌ی ۲: DNS به این سرور اشاره می‌کند ───
say "۱. nginx با همه‌ی دامنه‌ها"
mkdir -p $BASE/backup; [ -f $AV/icsd ] && cp $AV/icsd $BASE/backup/nginx-icsd.$(date +%Y%m%d-%H%M%S)
sed "s/__DOMAIN__/$NAMES/" $APP/deploy/nginx-icsd.conf > $AV/icsd.new
mv $AV/icsd.new $AV/icsd; ln -sfn $AV/icsd $EN/icsd
rm -f $EN/icsd-pre
if nginx -t 2>&1; then systemctl reload nginx; rm -f $AV/icsd-pre
else
  cp "$(ls -t $BASE/backup/nginx-icsd.* | head -1)" $AV/icsd; [ -f $AV/icsd-pre ] && ln -sfn $AV/icsd-pre $EN/icsd-pre
  die "nginx خطا داشت؛ تنظیمات قبلی برگردانده شد."
fi

say "۲. گواهی SSL برای: $NAMES"
D=""; for n in $NAMES; do D="$D -d $n"; done
if certbot --nginx --non-interactive --agree-tos --redirect --expand --cert-name "$DOMAIN" $D; then
  set_env HTTPS_ENABLED True; set_env CANONICAL_HOST "$DOMAIN"
  site_url "https://$DOMAIN"
else
  echo "  SSL گرفته نشد. سایت روی http کار می‌کند. بعداً دستی:  sudo certbot --nginx$D"
  set_env HTTPS_ENABLED False; set_env CANONICAL_HOST "$DOMAIN"
  site_url "http://$DOMAIN"
fi
systemctl restart icsd; sleep 2
systemctl is-active --quiet icsd || { journalctl -u icsd -n 30 --no-pager; die "سرویس icsd بالا نیامد."; }
say "تمام ✓  https://$DOMAIN  (www و دامنه‌های قبلی با ۳۰۱ به آن می‌روند)"

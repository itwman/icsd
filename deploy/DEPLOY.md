# استقرار ICSD روی سرور اشتراکی (اوبونتو ۲۲)

اصل کار: **هیچ چیزِ سایت‌های دیگر تغییر نمی‌کند.** همه‌چیز جداست:

| چه چیزی | کجا |
|---|---|
| کاربر لینوکس | `icsd` (بدون sudo و بدون shell) |
| کد | `/srv/icsd/app` |
| پایتون | `python3.11` کنار پایتون سیستم + venv جدا در `/srv/icsd/venv` |
| دیتابیس | پستگرس، کاربر و دیتابیس جدا به نام `icsd` |
| اجرا | سرویس systemd جدا `icsd` روی سوکت یونیکس `/run/icsd/gunicorn.sock` (هیچ پورتی اشغال نمی‌شود)، با سقف رم و CPU |
| وب‌سرور | یک فایل nginx جدا `/etc/nginx/sites-available/icsd` فقط برای دامنه‌ی خودش؛ قبل از reload با `nginx -t` آزمایش می‌شود و اگر خطا داشت خودکار برداشته می‌شود |

سایت ابتدا روی **`new.icsd.ir`** بالا می‌آید تا وردپرس فعلی سر جایش بماند. بعد از تأیید، دامنه‌ی اصلی جابه‌جا می‌شود.

## قدم ۰ — DNS
در پنل دامنه یک رکورد **A** با نام `new` و مقدار IP سرور (`195.88.208.168`) بسازید.

## قدم ۱ — بررسی سرور (فقط خواندن، بدون تغییر)
```bash
ssh -p 2222 USER@195.88.208.168
curl -sSLo /tmp/check.sh https://raw.githubusercontent.com/itwman/icsd/main/deploy/check_server.sh
bash /tmp/check.sh new.icsd.ir
```
خروجی را بفرستید. اگر سرور پنل میزبانی (DirectAdmin، cPanel، aaPanel…) یا Apache داشته باشد، روش nginx فرق می‌کند و قبل از نصب هماهنگ می‌کنیم.
اگر مخزن خصوصی است، `raw.githubusercontent` کار نمی‌کند؛ محتوای فایل را دستی کپی کنید یا اول مخزن را clone کنید (قدم ۲).

## قدم ۲ — نصب
```bash
sudo DOMAIN=new.icsd.ir DB_PASS=YourStrongPass2026 bash -c "$(curl -fsSL https://raw.githubusercontent.com/itwman/icsd/main/deploy/install.sh)"
```
برای مخزن خصوصی: اول یک Deploy Key یا Personal Access Token در گیت‌هاب بسازید و `REPO=https://TOKEN@github.com/itwman/icsd.git` را هم به دستور اضافه کنید.

سپس مدیر سایت:
```bash
sudo -u icsd /srv/icsd/venv/bin/python /srv/icsd/app/manage.py createsuperuser
```

## قدم ۳ — SSL
```bash
sudo certbot --nginx -d new.icsd.ir
sudo sed -i 's/^HTTPS_ENABLED=.*/HTTPS_ENABLED=True/' /srv/icsd/app/.env
sudo systemctl restart icsd
```
در پنل ← تنظیمات سایت، «آدرس سایت» را `https://new.icsd.ir` کنید.

## به‌روزرسانی بعدی (بعد از هر push)
```bash
sudo bash /srv/icsd/app/deploy/update.sh
```

## جابه‌جایی icsd.ir از وردپرس به جنگو
DNS دامنه در Cloudflare است و وردپرس روی سرور دیگری (185.49.84.236) است؛ آن سرور دست نمی‌خورد و پشتیبان می‌ماند.
1. روی سرور جدید (DNS هنوز قدیمی):  `sudo DOMAIN=icsd.ir bash /srv/icsd/app/deploy/set_domain.sh`
   تصاویر وردپرس به `/srv/icsd/media/wp-uploads` کپی می‌شوند (آدرس‌های `/wp-content/uploads/...` زنده می‌مانند) و nginx برای icsd.ir آماده می‌شود.
2. در Cloudflare رکورد A برای `icsd.ir` و `www` را به 195.88.208.168 تغییر دهید (ابر خاکستری، DNS only). به `mail` و رکوردهای TXT دست نزنید.
3. یکی دو دقیقه بعد همان دستور مرحله‌ی ۱ را دوباره بزنید: SSL برای icsd.ir، www و new گرفته می‌شود و www و new با ۳۰۱ به icsd.ir می‌روند.
4. ریدایرکت همه‌ی ۳۸ آدرس sitemap وردپرس از قبل ساخته و آزمایش شده است. در پنل ← سئو ← «نمایشگر ۴۰۴» آدرس‌های جاافتاده را ببینید.
5. در سرچ‌کنسول (همان property قبلی icsd.ir) `https://icsd.ir/sitemap.xml` را ثبت کنید.

## عیب‌یابی
```bash
sudo systemctl status icsd
sudo journalctl -u icsd -n 80 --no-pager
sudo tail -n 50 /var/log/nginx/icsd.error.log
```

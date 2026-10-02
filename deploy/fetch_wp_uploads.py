"""کپی تصاویر وردپرس قدیمی (wp-content/uploads) به سرور جدید، پیش از تغییر DNS.

    python3 fetch_wp_uploads.py https://icsd.ir /srv/icsd/media/wp-uploads

فهرست فایل‌ها از REST API وردپرس (/wp-json/wp/v2/media) خوانده می‌شود، همراه همه‌ی اندازه‌های بریده‌شده.
فایل‌های موجود دوباره دانلود نمی‌شوند؛ پس اجرای دوباره بی‌خطر است.
"""
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

UA = {"User-Agent": "Mozilla/5.0 (ICSD migration)"}


def get(url, timeout=60):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout)


def main(site, dest):
    site = site.rstrip("/")
    dest = Path(dest)
    marker = "/wp-content/uploads/"
    urls, page, pages = set(), 1, 1
    while page <= pages:
        with get(f"{site}/wp-json/wp/v2/media?per_page=100&page={page}") as r:
            pages = int(r.headers.get("X-WP-TotalPages", "1"))
            for m in json.load(r):
                urls.add(m.get("source_url", ""))
                for s in (m.get("media_details") or {}).get("sizes", {}).values():
                    urls.add(s.get("source_url", ""))
        page += 1
    urls = sorted(u for u in urls if marker in u)
    ok = skip = fail = 0
    for u in urls:
        rel = urllib.parse.unquote(u.split(marker, 1)[1])
        if ".." in rel:
            continue
        target = dest / rel
        if target.exists() and target.stat().st_size:
            skip += 1
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        try:
            with get(urllib.parse.quote(u, safe=":/%?=&")) as r:
                target.write_bytes(r.read())
            ok += 1
        except Exception as e:  # noqa: BLE001
            fail += 1
            print("  ✗", rel, e)
    print(f"تصاویر وردپرس: {ok} دانلود، {skip} از قبل بود، {fail} خطا (از {len(urls)} فایل)")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

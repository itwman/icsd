#!/usr/bin/env bash
# به‌روزرسانی بعد از هر push به گیت‌هاب — فقط سرویس icsd ری‌استارت می‌شود.
#   sudo bash /srv/icsd/app/deploy/update.sh
set -euo pipefail
APP=/srv/icsd/app; VENV=/srv/icsd/venv; PIP_INDEX="${PIP_INDEX_URL:-https://mirror-pypi.runflare.com/simple}"
M() { sudo -u icsd bash -c "cd $APP && $VENV/bin/python manage.py $*"; }
sudo -u icsd git -C $APP pull --ff-only
sudo -u icsd $VENV/bin/pip install -q -r $APP/requirements.txt -i "$PIP_INDEX" || sudo -u icsd $VENV/bin/pip install -q -r $APP/requirements.txt
M migrate --noinput
M collectstatic --noinput -v0
systemctl restart icsd
sleep 2; systemctl is-active icsd && echo "✓ به‌روز شد"

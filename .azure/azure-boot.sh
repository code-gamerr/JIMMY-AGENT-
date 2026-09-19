#!/bin/sh
set -eu
export PATH="/opt/jimmy/.venv/bin:/opt/jimmy/bin:/command:/package/admin/s6/command:${PATH:-/usr/bin:/bin}"

echo "[azure-boot] start pwd=$(pwd) path=$PATH"
ls -la /opt 2>&1 | head -n 30 || true
ls -la /opt/jimmy 2>&1 | head -n 30 || true

SEED=/opt/jimmy/jimmy_cli/jimmy_seed_profiles.py
if [ -f "$SEED" ]; then
  echo "[azure-boot] patching seed api_mode"
  sed -i 's/"api_mode": "chat_completions"/"api_mode": "codex_responses"/g' "$SEED" || true
fi

if [ -f /mnt/maint/patch_astra_api_mode.py ]; then
  python /mnt/maint/patch_astra_api_mode.py || true
fi

if [ -x /opt/jimmy/docker/entrypoint-dispatch.sh ]; then
  echo "[azure-boot] exec entrypoint-dispatch"
  exec /opt/jimmy/docker/entrypoint-dispatch.sh
fi
if [ -x /init ]; then
  echo "[azure-boot] exec /init"
  exec /init
fi

echo "[azure-boot] fallback: seed + dashboard"
python -m jimmy_cli.jimmy_seed_profiles || true
python /mnt/maint/patch_astra_api_mode.py || true
exec jimmy dashboard --host 0.0.0.0 --port 9119 --no-open
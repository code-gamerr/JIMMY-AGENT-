#!/bin/sh
set -eu
export PATH="/opt/jimmy/.venv/bin:/opt/jimmy/bin:/command:/package/admin/s6/command:${PATH:-/usr/bin:/bin}"

# Keep HERMES_HOME on container-local /opt/data (from Container App env).
# Azure Files (/mnt/maint) is SMB and locks SQLite — do not point the live
# gateway home at it. /mnt/maint is only for boot scripts + durable logs.

echo "[azure-boot] start pwd=$(pwd) home=${HERMES_HOME:-unset} path=$PATH"

if [ -f /mnt/maint/hotpatch_models.py ]; then
  echo "[azure-boot] hotpatching azure foundry gpt-6 api_mode"
  python3 /mnt/maint/hotpatch_models.py || python /mnt/maint/hotpatch_models.py || true
fi

for SEED in \
  /opt/jimmy/jimmy_cli/jimmy_seed_profiles.py \
  /opt/jimmy/hermes_cli/jimmy_seed_profiles.py \
  /opt/jimmy/hermes_cli/hermes_seed_profiles.py
do
  if [ -f "$SEED" ]; then
    echo "[azure-boot] patching seed api_mode in $SEED"
    sed -i 's/"api_mode": "chat_completions"/"api_mode": "codex_responses"/g' "$SEED" || true
  fi
done

if [ -f /mnt/maint/patch_astra_api_mode.py ]; then
  echo "[azure-boot] patching profile configs"
  python3 /mnt/maint/patch_astra_api_mode.py || python /mnt/maint/patch_astra_api_mode.py || true
fi

# Full image path (s6 dispatcher) — not present on slim builds.
if [ -f /opt/jimmy/docker/entrypoint-dispatch.sh ]; then
  echo "[azure-boot] exec entrypoint-dispatch"
  chmod +x /opt/jimmy/docker/entrypoint-dispatch.sh 2>/dev/null || true
  exec /bin/sh /opt/jimmy/docker/entrypoint-dispatch.sh "$@"
fi
if [ -e /init ]; then
  echo "[azure-boot] exec /init"
  exec /init "$@"
fi

# Slim Azure image path: seed profiles (wires Telegram tokens), start the
# messaging gateway (Telegram), then keep the dashboard as PID 1.
echo "[azure-boot] slim path: seed profiles + gateway + dashboard"
python -m hermes_cli.jimmy_seed_profiles \
  || python -m jimmy_cli.jimmy_seed_profiles \
  || python /opt/jimmy/hermes_cli/jimmy_seed_profiles.py \
  || true

if [ -f /mnt/maint/patch_astra_api_mode.py ]; then
  python3 /mnt/maint/patch_astra_api_mode.py || python /mnt/maint/patch_astra_api_mode.py || true
fi

BIN=hermes
if command -v jimmy >/dev/null 2>&1; then
  BIN=jimmy
fi

mkdir -p /mnt/maint/logs /opt/data/logs
export PYTHONUNBUFFERED=1
# Gateway must run or Telegram stays silent (dashboard alone does not poll).
# Log to Azure Files so we can inspect without container exec.
echo "[azure-boot] starting $BIN gateway run --replace"
: >/mnt/maint/logs/gateway-boot.log 2>/dev/null || true
nohup "$BIN" gateway run --replace >>/mnt/maint/logs/gateway-boot.log 2>&1 &
echo "[azure-boot] gateway pid=$!"

# Give Telegram adapters a moment to claim getUpdates before dashboard starts.
sleep 5

echo "[azure-boot] starting $BIN dashboard on :9119"
exec "$BIN" dashboard --host 0.0.0.0 --port 9119 --no-open

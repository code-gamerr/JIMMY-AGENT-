#!/bin/sh
# Post-seed hotfix for Azure: gpt-6-astra needs Responses API for tools.
# Invoked from stage2 when present at /mnt/maint/post-seed.sh (image with hook),
# or run manually. Safe to call repeatedly.
set -e
if [ -f /mnt/maint/patch_astra_api_mode.py ]; then
  python /mnt/maint/patch_astra_api_mode.py || true
fi

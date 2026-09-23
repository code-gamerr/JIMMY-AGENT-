#!/bin/sh
set -eu
echo "===ENV==="
echo "DEPLOY=$AZURE_OPENAI_DEPLOYMENT"
echo "EP=$AZURE_OPENAI_ENDPOINT"
echo "KEYLEN=${#AZURE_OPENAI_API_KEY}"
echo "FOUNDRY_EP=$AZURE_FOUNDRY_BASE_URL"
echo "===CFG==="
for p in /opt/data /opt/data/profiles/jimmy1 /opt/data/profiles/jimmy2 /opt/data/profiles/jimmy3 /opt/data/profiles/jimmy4; do
  echo "---$p---"
  if [ -f "$p/config.yaml" ]; then
    sed -n '/^model:/,/^[a-z]/p' "$p/config.yaml" | head -30
    sed -n '/^agent:/,/^[a-z]/p' "$p/config.yaml" | head -20
  fi
done
echo "===RECENT LOG FILES==="
find /opt/data -name "*.log" -type f -mtime -2 2>/dev/null | head -30
echo "===GREP ERRORS==="
find /opt/data -name "*.log" -type f -mtime -2 2>/dev/null | while read -r f; do
  hits=$(grep -Ei "error|fail|401|403|404|429|api.?call|provider|DeploymentNotFound|astra|openai|retries|codex" "$f" 2>/dev/null | tail -20 || true)
  if [ -n "$hits" ]; then
    echo "==== $f ===="
    echo "$hits"
  fi
done

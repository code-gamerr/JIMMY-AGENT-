# Run AFTER closing Cursor / any terminals using this repo.
# Renames Documents\Codes\hermes-agent-main -> jimmy-agent-main
$parent = Split-Path $PSScriptRoot -Parent
if (-not (Test-Path (Join-Path $parent "jimmy_cli"))) {
  # Script may live under scripts/; parent is repo root
  $repo = $parent
} else {
  $repo = $parent
}
$codes = Split-Path $repo -Parent
$src = Join-Path $codes "hermes-agent-main"
$dst = Join-Path $codes "jimmy-agent-main"
Write-Host "src=$src"
Write-Host "dst=$dst"
if (-not (Test-Path $src)) {
  if (Test-Path $dst) { Write-Host "Already renamed to jimmy-agent-main"; exit 0 }
  Write-Host "Source not found"; exit 1
}
if (Test-Path $dst) { Write-Host "Destination already exists"; exit 1 }
Rename-Item -LiteralPath $src -NewName "jimmy-agent-main"
Write-Host "Done. Reopen Cursor on: $dst"

# Jimmy on Azure

Public Container App with **4 independent password logins** (`jimmy1`–`jimmy4`), shared Azure OpenAI, isolated profiles (sessions + Telegram).

## Live URL

https://ca-jimmy-yd6h7x5ni6ki4.braveriver-d2909cea.eastus.azurecontainerapps.io/chat

Login: https://ca-jimmy-yd6h7x5ni6ki4.braveriver-d2909cea.eastus.azurecontainerapps.io/login

## Maintenance (2026-09-03)

Planned ~42 hour window (ECC install + related work). Full Jimmy gateway is
offline; revision `ca-jimmy-yd6h7x5ni6ki4--maintbots` runs a lightweight
Telegram auto-replier + HTTP maintenance page instead.

- Any Telegram message (e.g. “hi”) to jimmy1/2/3 bots gets a cool maintenance reply.
- Script: `.azure/jimmy_maintenance_bots.py` (also on Azure Files share `jimmy-data`).
- Dashboard URL serves a short “polishing up” page on `:9119`.
- jimmy4: no Telegram bot token configured.

To bring full Jimmy back online: redeploy from `azure-build/` (preferred), or
clear the maintenance `command` override / remount and activate a normal
gateway revision. Do **not** leave `--maintbots` as the live command after
maintenance.

## Local CLI (Jimmy, not Jimmy)

After `pip install -e .` in this repo:

```powershell
jimmy --help
jimmy chat
jimmy dashboard
jimmy -p jimmy1 chat
```

`jimmy` still works as an alias; prefer `jimmy` for this project.
Do **not** run `jimmy gateway` locally while Azure is polling the same Telegram bots.

Resource group: `rg-jimmy-eastus`  
Portal: https://portal.azure.com/#@/resource/subscriptions/ef27ac90-4a8e-4d2d-8de0-22d1924f023e/resourceGroups/rg-jimmy-eastus

## Credentials

Passwords are in `.azure/jimmy-credentials.local.txt` (gitignored). Log in with:

| Username | Profile |
|----------|---------|
| jimmy1 | jimmy1 |
| jimmy2 | jimmy2 |
| jimmy3 | jimmy3 |
| jimmy4 | jimmy4 |

## Redeploy image

Build from `azure-build/` (includes dashboard + TUI + WhatsApp bridge):

```powershell
$tag = "whatsapp-" + (Get-Date -Format "yyyyMMddHHmmss")
az acr build --registry jimmyyd6h7x5ni6ki4 --image "jimmy:$tag" --file Dockerfile ./azure-build
az containerapp update -g rg-jimmy-eastus -n ca-jimmy-yd6h7x5ni6ki4 `
  --image "jimmyyd6h7x5ni6ki4.azurecr.io/jimmy:$tag"
```

## Isolation

- Auth session claims `profile`; middleware forces `?profile=` and returns 403 on mismatch.
- Profile switcher is locked for bound users.
- `gateway.multiplex_profiles` + per-profile `JIMMY_HOME/profiles/jimmyN`.

# OpenClaw → Jimmy capability merge

Goal: **Jimmy absorbs OpenClaw operator value** (migration + unique skills),
without replacing Jimmy’s gateway / `conversation_loop` with OpenClaw’s Gateway.

Vendored tree: `openclaw/` ([openclaw/openclaw](https://github.com/openclaw/openclaw), MIT).

## Architecture

| Layer | Role |
|---|---|
| Jimmy gateway + platforms | **Primary** messaging runtime |
| `jimmy claw migrate` | Import `~/.openclaw` → Jimmy home |
| `jimmy openclaw …` | Sidecar over `openclaw/openclaw.mjs` (isolated state dir) |
| `jimmy/adapters/openclaw.py` | Command-center worker |
| `optional-skills/openclaw/*` | Curated skill packs |
| Device nodes / companion apps / Control UI | **SIDECAR only** |

## Capability matrix

| OpenClaw capability | Jimmy status | Where |
|---|---|---|
| Agent Gateway as primary | **WONTFIX** | Keep Jimmy gateway |
| Telegram/Discord/Slack/WhatsApp/… | **EXISTS** (Jimmy often broader) | `plugins/platforms/*` |
| Exotic channels (Nostr, Twitch, Synology, …) | **SIDECAR** | `jimmy openclaw gateway` |
| Migration (SOUL/MEMORY/skills/MCP/…) | **EXISTS** | `jimmy claw migrate` |
| Skills / ClawHub | **PARTIAL** | curated `optional-skills/openclaw/` + migrate imports |
| Cron / plugins deep config | **PARTIAL** | archived on migrate; recreate in Jimmy |
| Device nodes + mobile/desktop apps | **SIDECAR** | `openclaw/apps/`, `src/node-host/` |
| Control UI (Lit) | **SIDECAR** | `jimmy openclaw dashboard` |
| Node-host computer-use / canvas / camera | **SIDECAR** | do not fork into core |

## Commands

```bash
# Migration (existing)
jimmy claw migrate --dry-run
jimmy claw migrate --yes

# Sidecar (new)
jimmy openclaw doctor
jimmy openclaw status
jimmy openclaw dashboard
jimmy openclaw agent --message "hello"
# gateway is explicit sidecar — Jimmy stays primary
jimmy openclaw gateway
```

Rebuild curated skills:

```bash
python scripts/port_openclaw_skills.py
```

## WONTFIX in Jimmy core

1. Replacing Jimmy gateway with OpenClaw Gateway  
2. Re-homing companion device nodes into Electron as a hard dependency  
3. Shipping Apple-only skills into core toolsets  

## Notices

See `THIRD_PARTY_NOTICES_OPENCLAW.md`. Preserve OpenClaw license notices.

## Manual checklist

- [ ] `jimmy openclaw doctor` finds `./openclaw/openclaw.mjs`
- [ ] `jimmy claw migrate --dry-run` still works
- [ ] Curated skills under `optional-skills/openclaw/`
- [ ] Sidecar uses isolated `OPENCLAW_STATE_DIR` by default

# ECC → Jimmy capability merge

Goal: **Jimmy gets useful ECC harness workflows**, without replacing Jimmy’s
custom agent loop with ECC’s multi-harness OS.

Vendored tree: `ECC/` ([affaan-m/ECC](https://github.com/affaan-m/ECC), MIT).

## Architecture

| Layer | Role |
|---|---|
| Jimmy `conversation_loop` | **Primary** agent runtime (keep) |
| `jimmy ecc …` | Sidecar CLI → `ECC/scripts/ecc.js` |
| `jimmy/adapters/ecc.py` | Command-center worker |
| `optional-skills/ecc/*` | Curated skill packs (ported) |
| Full ECC control-pane / hooks / 286 skills | **Sidecar only** |

## Capability matrix

| ECC capability | Jimmy status | Where |
|---|---|---|
| Agent conversation loop | **WONTFIX** (Jimmy stronger/different) | Jimmy core |
| Skills OS (286 packs) | **PARTIAL** — curated port | `optional-skills/ecc/` |
| Slash commands (94) | **PARTIAL** — use ECC/Cursor install or Jimmy commands | sidecar / `.cursor` |
| Agents / personas (68) | **SIDECAR** | `ECC/agents/` |
| Hooks | **SIDECAR** (cache-risk) | prefer `--no-hooks` |
| Memory Vault | **SIDECAR** | `jimmy ecc memory …` |
| Consult / catalog | **SIDECAR** | `jimmy ecc consult` |
| Doctor / repair / setup | **SIDECAR** | `jimmy ecc doctor\|setup` |
| Control pane | **SIDECAR** | `jimmy ecc control-pane` |
| Sessions / work-items SQLite | **SIDECAR** | ECC status DB |
| Multi-harness install | **EXISTS** via adapter + setup | `--target hermes` today |

## Commands

```bash
jimmy ecc doctor
jimmy ecc status
jimmy ecc consult "minimal Jimmy profile"
jimmy ecc memory --help
jimmy ecc setup          # minimal + hermes target + no-hooks
jimmy ecc control-pane
```

Rebuild curated skills from the vendored tree:

```bash
python scripts/port_ecc_skills.py
jimmy skills install official/ecc/delivery-gate
```

## Enable

```yaml
# Optional — Memory Vault / consult stay CLI-driven; no core config required.
```

## WONTFIX in Jimmy core

1. Replacing Jimmy’s loop with ECC orchestration  
2. Enabling ECC hooks by default (prompt-cache risk)  
3. Shipping all 286 skills into core toolsets  
4. Replacing Command Center with ECC control-pane  

## Notices

See `THIRD_PARTY_NOTICES_ECC.md`. Do not strip `ECC/LICENSE`.

## Manual checklist

- [ ] `jimmy ecc doctor` finds `./ECC` and `scripts/ecc.js`
- [ ] `jimmy ecc consult` returns a recommendation
- [ ] Curated skills exist under `optional-skills/ecc/`
- [ ] Command-center ECC adapter status ready (node + ecc.js)

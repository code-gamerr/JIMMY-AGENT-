# Project Instructions (Jimmy Agent)

Canonical AI guide: **`AGENTS.md`**. Full deep-dive: **`docs/DEVELOPMENT.md`**.

## Tech Stack

- **Language:** Python `>=3.11,<3.14` (package `jimmy-agent`, exact-pinned deps + `uv.lock`)
- **CLI entry:** `jimmy` → `jimmy_cli.main:main`
- **Agent core:** `run_agent.AIAgent`
- **UI edges:** Ink TUI (`ui-tui` + `tui_gateway`), Electron (`apps/desktop`), Vite dashboard (`web`)
- **Tests:** `scripts/run_tests.sh` (pytest) · JS: vitest under `tests-js` / package trees

## Sacred Rules

1. **Prompt caching** — never mutate past context, swap toolsets, or rebuild the system prompt mid-conversation (exception: context compression).
2. **Narrow core** — new capability via footprint ladder: extend → CLI+skill → service-gated tool → plugin → MCP → new core tool (last).
3. **Profiles** — always `get_jimmy_home()` / `display_jimmy_home()`; never hardcode `~/.jimmy`.
4. **Secrets vs settings** — `.env` secrets only; behavioral config in `config.yaml`.

## Structure (edit targets)

| Path | Role |
|------|------|
| `run_agent.py` | Conversation loop |
| `model_tools.py` / `toolsets.py` | Tools + toolsets |
| `agent/` | Providers, memory, compression |
| `tools/` | Auto-registered tools |
| `gateway/` | Messaging + `platforms/` |
| `jimmy_cli/` | Subcommands, config, plugins, skins |
| `plugins/` / `skills/` | Edges, not core |
| `tests/` | Behavior-contract tests (temp `JIMMY_HOME`) |

## Build & Test

```bash
source .venv/bin/activate   # or Windows venv
jimmy                       # chat
scripts/run_tests.sh        # CI-parity — do not call pytest directly
```

## Conventions

- Commits: conventional (`feat:`, `fix:`, `refactor:`, …)
- Message role alternation must stay strict (no same-role doubles; no synthetic user mid-loop)
- Gateway dual guards for approval/control commands
- Do not write change-detector / source-regex tests

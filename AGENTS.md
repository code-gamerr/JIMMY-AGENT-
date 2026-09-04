# Jimmy - Development Guide

Instructions for AI coding assistants working on the jimmy-agent codebase.
**Never give up on the right solution.**

Full contributor guide (architecture, plugins, skills, testing deep-dives):
`docs/DEVELOPMENT.md`. Prefer that file when you need detail; keep this one
small so it fits the system prompt without truncation.

## What Jimmy Is

Jimmy is a personal AI agent: same core across CLI, messaging gateway
(Telegram/Discord/Slack/…), TUI, and Electron desktop. It learns (memory +
skills), delegates to subagents, runs cron, and drives terminal + browser.
Extend via **plugins and skills**, not by growing the core.

Two load-bearing rules:

1. **Prompt caching is sacred.** Do not mutate past context, swap toolsets, or
   rebuild the system prompt mid-conversation (exception: context compression).
2. **Narrow core, capability at the edges.** Every core tool ships on every API
   call. Prefer: extend existing → CLI + skill → service-gated tool → plugin →
   MCP catalog → new core tool (last resort).

## Contribution Rubric (short)

**Want:** real bug fixes with line-level repro; edge growth (platforms,
providers, desktop/TUI); god-file extractions; behavior-contract tests; E2E
against a temp `JIMMY_HOME`; cache-/alternation-safe changes.

**Don't want:** speculative hooks; new `JIMMY_*` env vars for non-secrets
(use `config.yaml`; `.env` is secrets only); new core tools when terminal/file
suffice; change-detector tests; outbound telemetry without opt-in; third-party
product plugins in-tree (ship standalone under `~/.jimmy/plugins/`).

**Verify the premise** before “fixing” missing links — many omissions are
intentional isolation. Trace runtime; read `git log -p -S` for original intent.

### Footprint ladder

1. Extend existing code  
2. CLI command + skill  
3. Service-gated tool (`check_fn`)  
4. Plugin  
5. MCP server in catalog  
6. New core tool (last resort)

Session surface (desktop panes, reactions, Projects) comes from the **session**,
never from process env like `JIMMY_DESKTOP=1`.

## Layout (entry points)

```
run_agent.py      # AIAgent conversation loop
model_tools.py    # tool orchestration + discovery
toolsets.py       # TOOLSETS + _JIMMY_CORE_TOOLS
cli.py            # interactive CLI
jimmy_constants.py# get_jimmy_home() / display_jimmy_home()
agent/            # providers, memory, compression, prompts
tools/            # auto-discovered via tools/registry.py
gateway/          # messaging + platforms/
plugins/          # memory, model-providers, …
skills/           # bundled skills
optional-skills/  # install via jimmy skills install
tests/            # pytest — always via scripts/run_tests.sh
```

User config: `~/.jimmy/config.yaml` (settings), `~/.jimmy/.env` (secrets only).

## Profiles — path rules

```python
from jimmy_constants import get_jimmy_home, display_jimmy_home
# GOOD
path = get_jimmy_home() / "config.yaml"
print(f"Saved to {display_jimmy_home()}/config.yaml")
# BAD — breaks profiles
path = Path.home() / ".jimmy" / "config.yaml"
```

Under `gateway.multiplex_profiles`, never fall through to bare `os.environ` for
profile secrets/authz — use scoped secret helpers (fail closed).

## Tools & config

- Register in `tools/*.py` via `registry.register(...)`; expose by adding the
  name to a toolset in `toolsets.py`.
- Non-secret settings → `DEFAULT_CONFIG` in `jimmy_cli/config.py` + `config.yaml`.
- Secrets → `OPTIONAL_ENV_VARS` + `.env`.
- Slash commands → `COMMAND_REGISTRY` in `jimmy_cli/commands.py`, then CLI /
  gateway handlers.

## Policies that break production if ignored

- **No mid-conversation cache break** (skills/tools/memory slash cmds: defer
  unless `--now`).
- **Message role alternation** — never two same-role messages in a row; never
  inject a synthetic user mid-loop.
- **Gateway dual guards** — approval/control cmds must bypass both base-adapter
  queue and runner intercept.
- **Stream-is-the-message adapters** — draft frames prefix-stable; consumer
  owns final; interim sends need `_interim_send`; reconcile by edit not plain
  send.
- **Tests never write to real `~/.jimmy/`** — use the autouse temp `JIMMY_HOME`.
- **Don't fake `sys.platform`** — use `@pytest.mark.linux_only` /
  `macos_only` / `windows_only`.
- **Don't write change-detector or source-regex tests.**

## Testing

```bash
scripts/run_tests.sh                          # CI-parity (required)
scripts/run_tests.sh tests/gateway/ -k foo    # scoped
```

Do not call `pytest` directly. JS/TS assertions belong in vitest, not Python.

## Dev environment

```bash
source .venv/bin/activate   # or venv / ~/.jimmy/jimmy-agent/venv
```

Need more detail (TUI, desktop slash curation, curator, cron, kanban, skins,
plugin ABCs, skill authoring standards)? → `docs/DEVELOPMENT.md`.

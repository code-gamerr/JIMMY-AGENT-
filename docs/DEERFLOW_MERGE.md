# DeerFlow → Jimmy capability merge

Goal: **Jimmy gets what DeerFlow has**, without replacing Jimmy’s custom agent
loop with LangGraph.

Analysis source: `docs/comparisons/Jimmy_vs_DeerFlow_Deep_Comparison.xlsx`

## Capability matrix

| DeerFlow capability | Jimmy status | Where |
|---|---|---|
| Custom / personal multi-surface agent | **Jimmy stronger** | CLI, gateway, Electron, Ink TUI |
| LangGraph lead agent + middleware stack | **Not adopted** (by design) | Jimmy `run_agent` / `conversation_loop` |
| Progressive research skills | **Ported** | `optional-skills/deerflow/*` (21 packs) |
| Media gen skills (ppt/podcast/video/…) | **Ported** | same |
| Skill reviewer / SkillScan pack | **Ported** | `optional-skills/deerflow/skill-reviewer` |
| CRITICAL SkillScan at install | **Ported** | `tools/skillscan_static.py` + `jimmy_cli/skills_hub.py` |
| Per-run token budget warn + hard-stop | **Ported** | `agent/token_budget.py`, desktop gauge |
| Plan-mode premature-exit guard | **Ported** | `agent/plan_mode.py`, `agent.plan_mode` |
| `present_files` artifacts + UI chrome | **Ported** | tool + desktop `PresentFilesTool` |
| Clarification cards | **Already had** (+ polish) | `clarify-tool.tsx` waiting hint |
| Max recursion / iteration ceiling | **Ported** | `agent.max_recursion_limit` |
| GitHub Issues/PR agent channel | **Ported (recipe)** | `plugins/platforms/github/` |
| Langfuse / LangSmith | **Had / Ported** | `plugins/observability/*` |
| InfoQuest search | **Ported** | `plugins/web/infoquest/` |
| E2B sandbox | **Ported** | `tools/environments/e2b.py`, `TERMINAL_ENV=e2b` |
| AIO sandbox (browser+shell+files) | **EXISTS via Docker / SIDECAR** | Jimmy Docker env; full AIO in `deer-flow/` |
| Durable MCP long-running tasks | **Ported** | `tools/mcp_tasks.py` (`mcp_task` tool) |
| Channels without public IP | **Already had** (+ banner) | desktop Messaging page |
| Cron multi-instance fire leases | **Hardened** | `cron/lease_config.py`, `cron.multi_instance` |
| DeerFlow sidecar CLI | **Ported** | `jimmy deerflow {setup,up,down,doctor}` |
| Helm full-stack chart | **SIDECAR** | wrap `deer-flow/deploy/helm` via CLI |
| Next.js research workspace UI | **Not adopted** | sidecar only |
| Session goals / todos / MCP / cron | **Already had** | Jimmy core |

## Install DeerFlow skills

```bash
jimmy skills install official/deerflow/deep-research
jimmy skills install official/deerflow/ppt-generation
jimmy skills install official/deerflow/skill-reviewer
```

## Enable new ports

```yaml
# ~/.jimmy/config.yaml
agent:
  token_budget:
    enabled: true
    total: 200000
  plan_mode: true
  skill_scan:
    enabled: true
  max_recursion_limit: 1000

terminal:
  backend: e2b   # requires E2B_API_KEY

cron:
  multi_instance:
    enabled: true
    fire_claim_ttl_seconds: 300

web:
  search_backend: infoquest   # requires INFOQUEST_API_KEY
```

```bash
jimmy deerflow setup
jimmy deerflow up
jimmy deerflow doctor
jimmy deerflow down
```

## Sandbox story (social / AIO honesty)

| Claim | Jimmy |
|---|---|
| Own computer / shell+files | **EXISTS** — `terminal.backend: docker` (or local/ssh/modal/daytona) |
| E2B cloud sandbox | **PORTED** — `terminal.backend: e2b` |
| DeerFlow AIO (browser+shell+files+MCP+VSCode in one image) | **SIDECAR** — `jimmy deerflow up` or Docker image from deer-flow |

## Manual checklist (Phase D)

- [ ] `present_files` shows artifact cards in desktop chat
- [ ] Statusbar context panel shows run token budget when enabled
- [ ] `agent.plan_mode: true` blocks final answer with incomplete todos
- [ ] Clarify card shows waiting hint
- [ ] `TERMINAL_ENV=e2b` requirements check with `E2B_API_KEY`
- [ ] Skill install blocked on embedded private key (SkillScan)
- [ ] `mcp_task` submit/list/status/cancel
- [ ] Messaging page shows no-public-IP banner
- [ ] `jimmy deerflow doctor` resolves vendored tree
- [ ] Cron fire claim TTL reads `cron.multi_instance`

## Still optional in `deer-flow/`

LangGraph harness, Next.js workspace, K8s provisioner, full AIO image, Helm templates.

Do **not** strip `deer-flow/LICENSE` (MIT — ByteDance / DeerFlow Authors).
See `THIRD_PARTY_NOTICES_DEERFLOW.md`.

## What we will not merge into Jimmy core

1. Replacing `conversation_loop` with LangGraph
2. Making Next.js the primary Jimmy UI
3. Requiring Redis + nginx for basic chat

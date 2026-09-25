# Jimmy Command Center — Architecture

Jimmy is the orchestration layer **above** OpenClaw, Munder Difflin, and ECC.
Those three trees stay intact. Jimmy does not rewrite them; it routes work
into their real CLIs/workspaces and streams observed process state to the UI.

## A. Repository analysis

| Path | What it is today | Role under Jimmy |
|------|------------------|------------------|
| Repo root (Jimmy / `jimmy` CLI) | Same agent runtime; `jimmy` is a branded `jimmy` entry point (`jimmy_cli/product.py`) | **Jimmy Core**: planner, task engine, event bus, Command Center |
| `openclaw/` | Multi-channel AI gateway (Node, `openclaw.mjs`). Sessions, channels, Control UI | Worker: messaging / gateway / channel tasks |
| `munder-difflin/` | Electron office-floor harness. Real coding CLIs in PTYs (`claude`, Cursor, Codex, …) | Worker: repository coding / tests / file changes |
| `ECC/` | Agent harness OS (`ecc-universal`): skills, hooks, `scripts/ecc.js` | Worker: harness ops, consult, doctor, memory vault, skill install |

Jimmy previously had **no** cross-module orchestrator — only CLI branding and Azure profile seeding.

## B. Current architecture

```
jimmy CLI  ==  jimmy CLI  →  AIAgent / gateway / dashboard
                 │
                 ├── openclaw/     (nested git repo, unused by Jimmy)
                 ├── munder-difflin/ (nested git repo, unused by Jimmy)
                 └── ECC/          (nested git repo; skills copied into Cursor)
```

## C. Proposed Jimmy architecture

```
                 JIMMY CORE (this package)
        ┌────────────────────────────────────┐
        │ Planner / Router / Permissions     │
        │ Task Manager / Event bus / Memory  │
        └────────────────┬───────────────────┘
                         │ AgentAdapter
           ┌─────────────┼──────────────┐
           ▼             ▼              ▼
       OpenClaw      Munder-Difflin    ECC
       (cwd+CLI)     (cwd+coding CLI)  (ecc.js)
           └─────────────┬──────────────┘
                         ▼
              subprocess (real stdout/stderr/exit)
                         ▼
              SQLite events + SSE → Command Center UI
```

Loop: **Task → Plan → Execute → Observe → Evaluate → Store experience → Reuse**.
No model-weight updates.

## D. Integration points (do not fork the workers)

- **OpenClaw**: `node openclaw/openclaw.mjs <subcommand>` with `cwd=openclaw/`.
  Probe `gateway status` / launcher version. Agent turns use documented CLI
  when the local Node version satisfies OpenClaw’s gate; otherwise Jimmy
  records the **real** launcher stderr (not a fake success).
- **Munder Difflin**: execution workspace is `munder-difflin/`. Jimmy inspects
  with `git status` / `git diff`, then spawns the real coding CLI already on
  PATH or this repo’s `jimmy -z` oneshot in that cwd. File lists come from
  git, not invented paths.
- **ECC**: `node ECC/scripts/ecc.js` (`consult`, `status`, `doctor`, `memory`,
  …). Coding-in-ECC-tree uses the same oneshot pattern with `cwd=ECC/`.

Future agents (Zara, finance, deploy, …) register as additional adapters with
the same `AgentAdapter` surface.

## E. Task / event data model

See `jimmy/models.py`. Task states: `QUEUED PLANNING ROUTING RUNNING WAITING
FAILED COMPLETED CANCELLED`. Events include `task.*`, `command.*`, `file.changed`,
`test.*`. Command events always carry the actual argv, cwd, stdout/stderr
chunks, exit code, and duration measured from the process.

## F. API contracts

Local-only (`127.0.0.1`). Token in `JIMMY_HOME/jimmy/auth.json`.

- `POST /api/jimmy/tasks` `{ "user_request": "...", "agent": "auto"|"openclaw"|"munder"|"ecc" }`
- `GET /api/jimmy/tasks`, `GET /api/jimmy/tasks/{id}`
- `POST /api/jimmy/tasks/{id}/cancel`
- `GET /api/jimmy/agents`
- `GET /api/jimmy/experiences?q=`
- `GET /api/jimmy/events?task_id=` (SSE)
- `GET /api/jimmy/audit`

## G. UI structure

`jimmy/ui/command-center.html` — Active tasks, queue, live activity, agent
status, terminal stream, files changed, errors, result, history, experiences.

## H. Implementation plan

1. Core models, store, events, security, process runner.
2. Adapters that only spawn real commands in the three folders.
3. Engine + experience memory.
4. Loopback API + Command Center.
5. `jimmy command-center` / `jimmy task` CLI.

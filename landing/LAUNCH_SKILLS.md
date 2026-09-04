# Jimmy launch skills

Ranked picks for day-one Jimmy (orchestrate coding + messaging + harness). Prefer built-ins first; enable optionals only when that worker is in play. Every enabled skill competes for model attention — keep the launch set small.

## Must enable (built-in)

| Rank | Skill | Path | Why |
|------|-------|------|-----|
| 1 | `plan` | `skills/software-development/plan/` | Write the plan before routing — matches Jimmy’s Plan → Execute loop. |
| 2 | `jimmy-agent` | `skills/autonomous-ai-agents/jimmy-agent/` | Operate Jimmy/Jimmy itself: CLI, gateway, themes, multi-agent. |
| 3 | `test-driven-development` | `skills/software-development/test-driven-development/` | Keeps coding-agent runs RED→GREEN instead of spray-and-pray edits. |
| 4 | `systematic-debugging` | `skills/software-development/systematic-debugging/` | Root-cause first when a routed CLI fails mid-task. |
| 5 | `github-pr-workflow` | `skills/github/github-pr-workflow/` | Branch → PR → CI → merge for work that should leave the sandbox. |
| 6 | `requesting-code-review` | `skills/software-development/requesting-code-review/` | Pre-commit security/quality gate before Jimmy marks a task done. |
| 7 | `github-code-review` | `skills/github/github-code-review/` | Review inbound PRs when Jimmy is used as a review desk. |
| 8 | `claude-code` | `skills/autonomous-ai-agents/claude-code/` | Delegate heavy coding to Claude Code CLI (Munder-style workers). |
| 9 | `codex` | `skills/autonomous-ai-agents/codex/` | Second coding CLI on the Munder floor — features and PRs via Codex. |
| 10 | `session-librarian` | `skills/productivity/session-librarian/` | Keep long Command Center sessions findable and pruned. |

## Strong defaults (built-in, enable if bandwidth)

| Rank | Skill | Path | Why |
|------|-------|------|-----|
| 11 | `simplify-code` | `skills/software-development/simplify-code/` | Parallel cleanup pass after a feature lands. |
| 12 | `codebase-inspection` | `skills/github/codebase-inspection/` | Quick LOC/language map before routing a large repo task. |
| 13 | `grounded-citations` | `skills/research/grounded-citations/` | Cite sources when research or docs are part of the goal. |
| 14 | `sdlc-review` | `skills/devops/sdlc-review/` | Kanban handoff verification when board dispatch is live. |
| 15 | `opencode` | `skills/autonomous-ai-agents/opencode/` | Third coding CLI option when OpenCode is on PATH. |

## Enable at launch only if that worker ships

| Rank | Skill | Path | Why |
|------|-------|------|-----|
| A | `ecc` | `optional-skills/autonomous-ai-agents/ecc/` | Install/use ECC harness workflows — Jimmy’s harness adapter. |
| B | `subagent-driven-development` | `optional-skills/software-development/subagent-driven-development/` | Execute plans via `delegate_task` with two-stage review. |
| C | `openclaw-migration` | `optional-skills/migration/openclaw-migration/` | Import OpenClaw memories/skills when migrating into Jimmy. |
| D | `prime-agent` | `optional-skills/autonomous-ai-agents/prime-agent/` | Long-running autonomous coding/research when Prime is available. |

## Explicitly defer

- Finance / blockchain / gaming / health optionals — not launch-critical.
- Creative media packs — enable per campaign, not by default.
- Heavy MLOps optionals — only when a model-training worker is assigned.
- Extra coding CLIs beyond the floor you actually run (`antigravity-cli`, `openhands`, `grok`, …) — install when that engine is present.

## Install notes

- Built-ins under `skills/` load with the product; confirm via `jimmy skills` / `jimmy skills`.
- Optionals: `jimmy skills install official/<category>/<skill>` (or `jimmy skills install …`).
- Keep the launch set to the Must-enable table plus worker-gated optionals only.

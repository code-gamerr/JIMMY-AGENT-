# Jimmy Harness Optimizer (AutoAgent-style)

Executable, reversible harness optimizer for Jimmy. Zero model-tool
schema footprint — capability is a CLI command (`jimmy optimize`), not a
core tool.

## What it reuses (do not duplicate the agent)

| Concern | Real path |
|---|---|
| LLM request construction / loop | `agent/conversation_loop.py` → `run_conversation` |
| System prompt tiers | `agent/system_prompt.py` (`build_system_prompt_parts`) |
| Tool schemas + dispatch | `model_tools.py` / `tools/registry.py` |
| Stop / continue / max tokens | conversation loop finish_reason + `_ephemeral_max_output_tokens` |
| Prompt caching | stable system-prompt prefix; hooks inject into **user** message only |
| Trajectory / history | session DB + `run_conversation` message list |
| Skill index | prompt builder `<available_skills>` (measured via `jimmy_cli/prompt_size.py`) |
| Subagents | `tools/delegate_tool.py` (`subagent_start` / `subagent_stop` hooks) |
| Credentials | `jimmy_cli.runtime_provider.resolve_runtime_provider` (AgentRunner) |

Instrumentation rides the existing first-party lifecycle bus
(`jimmy_cli/lifecycle.py` → `jimmy_cli/observability`) plus the same
`post_api_request` / `post_tool_call` / `subagent_*` hooks plugins already see.
When the optimize observer is **disabled**, `handles_hook` returns false and
behavior is unchanged.

## Package layout

```
jimmy_cli/optimize/
  observer.py      # opt-in metrics sink (thread-safe)
  scoring.py       # 100*success + 0.1*useful - 5*extra_turns - 2*extra_tools
  tasks.py         # ≥20 deterministic tasks + behavioral verifiers
  runner.py        # FakeRunner + AgentRunner; single-thread run_benchmark lock
  simulation.py    # explicit named offline fixture profiles (not hidden magic)
  candidate.py     # reversible config.yaml overlays + fail-closed compare
  search.py        # built-in catalog search across configurable axes
  report.py        # OFFLINE FIXTURE before/after report writer
  context_cost.py  # "Summarize what is in this folder" first-turn diagnosis
  artifacts.py     # summary.json + events.jsonl + per-task trajectories
  cli.py           # command implementation
jimmy_cli/subcommands/optimize.py  # argparse
```

## Scoring

```
score = 100*success
      + 0.1 * useful_completion_tokens
      - 5   * unnecessary_llm_turns
      - 2   * unnecessary_tool_calls
```

`useful_completion_tokens = min(completion_tokens, task.max_useful, USEFUL_COMPLETION_CAP=500)`
so verbosity cannot dominate. Unnecessary turns/tools are `max(0, actual - expected_max_*)`.

Candidate comparison requires **identical task-id sets**; mismatched sets raise
`TaskSetMismatchError` (missing tasks are never silently scored as zero).

## Orchestration invariant

`run_benchmark` mutates process-global `JIMMY_HOME` (and AgentRunner may
`chdir` into the task workspace). It is **single-thread orchestration only**:
a non-blocking process lock rejects concurrent callers, and both `JIMMY_HOME`
and cwd are restored in `finally`.

## Offline simulations (explicit)

Default FakeRunner metrics ignore config overlays — a no-op overlay is
correctly rejected. To demonstrate a measured dry-run improvement, pass an
**explicit** named simulation (see `simulation.py`), e.g. `lean_tool_use`:

```bash
jimmy optimize candidate --dry-run --simulation lean_tool_use \
  --overlay '{"agent":{"max_turns":60}}'
```

## Local runs

Offline (no credentials) — recommended for CI / dry-run:

```bash
# from repo root, with venv active
jimmy optimize list-tasks
jimmy optimize diagnose-context
jimmy optimize benchmark --dry-run --out /tmp/jimmy-optimize
jimmy optimize candidate --dry-run \
  --overlay '{"display":{"tool_progress":"off"}}' \
  --out /tmp/jimmy-optimize
jimmy optimize search --dry-run --out /tmp/jimmy-optimize
jimmy optimize report-offline --out docs/optimizer/OFFLINE_FIXTURE_REPORT.md
```

Live (uses provider credentials via normal runtime resolution — never
`api_key=missing`):

```bash
jimmy optimize benchmark --out /tmp/jimmy-optimize-live --model <model>
```

Artifacts land under `<out>/artifacts/<run_id>/`:

- `summary.json` — scores, prompt breakdown, folder-summarize diagnosis
- `events.jsonl` — per-LLM-call + tool events (tokens, cache, finish_reason, attribution)
- `tasks/<id>.json` — per-task response, **messages trajectory**, request_metrics, events
  (secrets redacted; no raw API payloads)
- `comparison.json` / `kept_overlay.yaml` | `rejected_overlay.yaml` for candidate runs
- `search_report.json` for `optimize search`

## Candidate safety

Overlays merge into the **isolated** `JIMMY_HOME/config.yaml` only, inside a
context manager that always restores prior bytes. Core source is never
self-edited during a run. A candidate is marked kept only when aggregate
score improves (`candidate_total > baseline_total`).

`optimize search` evaluates a documented catalog of reversible overlays across
axes that are genuinely configurable (`context`, `skills`, `tool_schemas`,
`guidance`, `turn_policy`). It does **not** pretend non-configurable
prompt/tool code changes were tested.

## Tests

```bash
scripts/run_tests.sh tests/jimmy_cli/test_optimize_observer.py \
  tests/jimmy_cli/test_optimize_scoring.py \
  tests/jimmy_cli/test_optimize_workflow.py \
  tests/jimmy_cli/test_optimize_cli.py \
  tests/jimmy_cli/test_optimize_verifiers.py -q
```

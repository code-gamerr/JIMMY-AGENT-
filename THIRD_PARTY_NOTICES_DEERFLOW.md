# Third-party notice — DeerFlow

This tree vendors [DeerFlow](https://github.com/bytedance/deer-flow)
(ByteDance Ltd. and/or its affiliates; DeerFlow Authors) under the MIT License.
See `deer-flow/LICENSE`.

Jimmy integrates DeerFlow at the edges (see `docs/DEERFLOW_MERGE.md`):

- Optional skills under `optional-skills/deerflow/` (adapted SKILL.md packs)
- Token-budget controls inspired by DeerFlow's token budget middleware
  (`agent/token_budget.py`)
- Full DeerFlow source retained under `deer-flow/` for reference / optional
  sidecar use — Jimmy's agent loop remains the custom `run_agent` /
  `conversation_loop` runtime (not LangGraph)

Copyright notices from DeerFlow are preserved. Do not strip LICENSE files.

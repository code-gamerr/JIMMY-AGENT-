# Third-party notice — OpenClaw

This tree vendors [OpenClaw](https://github.com/openclaw/openclaw)
under the MIT License. See `openclaw/package.json` / `openclaw/THIRD_PARTY_NOTICES.md`
and upstream LICENSE.

Jimmy integrates OpenClaw at the edges (see `docs/OPENCLAW_MERGE.md`):

- Migration: `jimmy claw migrate` + `optional-skills/migration/openclaw-migration/`
- Optional curated skills under `optional-skills/openclaw/`
- Sidecar CLI `jimmy openclaw …` → `openclaw/openclaw.mjs`
- Command-center worker `jimmy/adapters/openclaw.py`
- Full OpenClaw source retained under `openclaw/` — Jimmy’s gateway and
  `conversation_loop` remain primary (OpenClaw Gateway is never the default)

Do not strip license / notice files.

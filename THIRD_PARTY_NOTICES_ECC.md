# Third-party notice — ECC

This tree vendors [ECC / Everything Claude Code](https://github.com/affaan-m/ECC)
(`ecc-universal`, Affaan Mustafa and contributors) under the MIT License.
See `ECC/LICENSE`.

Jimmy integrates ECC at the edges (see `docs/ECC_MERGE.md`):

- Optional curated skills under `optional-skills/ecc/`
- Sidecar CLI `jimmy ecc …` → `ECC/scripts/ecc.js`
- Command-center worker `jimmy/adapters/ecc.py`
- Full ECC source retained under `ECC/` — Jimmy’s agent loop remains
  `run_agent` / `conversation_loop` (not ECC orchestration)

Do not strip LICENSE files.

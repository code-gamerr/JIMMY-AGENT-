---
name: ecc
description: Install and use ECC harness workflows in Jimmy.
disable-model-invocation: true
version: 0.1.0
author: Arnav Singh, Jimmy
license: MIT
platforms: [linux, macos, windows]
metadata:
  jimmy:
    tags: [ECC, Agent Harness, Skills, Memory, Workflow]
    category: autonomous-ai-agents
    related_skills: [prime-agent]
    requires_toolsets: [terminal]
---

# ECC Skill

ECC ([Everything Claude Code](https://github.com/affaan-m/ECC)) is an agent
harness pack: skills, rules, commands, and optional memory/handoff tooling.
Install it into Jimmy/Jimmy; do not treat it as a second chat model loop.

## When to Use

- The user asks to install or update ECC.
- The user wants ECC workflows (context budget, delivery gate, repo scan,
  research-first development, cross-harness memory).
- Bridging Jimmy with Cursor/Codex-style ECC conventions.

## Prerequisites

- Node.js 18+
- Git
- Official sources only: https://github.com/affaan-m/ECC and `ecc-universal`

## How to Run

```bash
git clone --depth 1 https://github.com/affaan-m/ECC.git /tmp/ECC
cd /tmp/ECC
npm install --no-audit --no-fund
node scripts/install-apply.js --profile minimal --target jimmy --no-hooks
```

Optional Memory Vault:

```bash
npm install -g ecc-universal
ecc memory init --scope project --scope team
```

## Quick Reference

```text
node scripts/install-apply.js --profile minimal --target jimmy --no-hooks
node scripts/install-apply.js --profile minimal --target cursor --no-hooks
npx ecc-universal doctor --target jimmy
ecc memory search "<query>"
```

## Procedure

1. Install only from the official ECC GitHub repo or `ecc-universal`.
2. Prefer `--profile minimal` and `--no-hooks` on Jimmy hosts first.
3. Verify with `npx ecc-universal doctor --target jimmy` when available.
4. Keep Jimmy's lean toolsets; do not enable ECC MCP servers by default.
5. Use ECC skills for workflow quality; keep ordinary chat on Jimmy's loop.

## Pitfalls

- ECC is not a replacement model. Stacking another agent loop raises cost.
- Hooks can change shell/edit behavior; review before `--enable-hooks`.
- Azure Jimmy needs a redeploy or volume skill sync after local install.
- Do not store secrets in ECC Memory Vault.

## Verification

```bash
test -f ~/.jimmy/ecc-install-state.json || test -f "$LOCALAPPDATA/jimmy/ecc-install-state.json"
ls ~/.jimmy/skills/ecc-guide 2>/dev/null || ls "$LOCALAPPDATA/jimmy/skills/ecc-guide"
```

## References

- https://github.com/affaan-m/ECC
- https://github.com/affaan-m/ECC/blob/main/docs/HERMES-SETUP.md

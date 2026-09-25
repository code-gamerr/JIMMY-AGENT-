<p align="center">
  <img src="docs/assets/banner.png" alt="Jimmy" width="100%">
</p>

# Jimmy

**The self-improving personal AI agent.** Same core across CLI, messaging gateway (Telegram, Discord, Slack, and more), TUI, and Electron desktop. It learns across sessions (memory + skills), delegates to subagents, runs scheduled jobs, and drives a real terminal and browser.

<p align="center">
  <a href="https://github.com/code-gamerr/JIMMY-AGENT-/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License: MIT"></a>
  <a href="https://github.com/code-gamerr/JIMMY-AGENT-"><img src="https://img.shields.io/badge/GitHub-code--gamerr%2FJIMMY--AGENT--black?style=for-the-badge&logo=github" alt="GitHub"></a>
  <a href="README.zh-CN.md"><img src="https://img.shields.io/badge/Lang-中文-red?style=for-the-badge" alt="中文"></a>
  <a href="README.ur-pk.md"><img src="https://img.shields.io/badge/Lang-اردو-green?style=for-the-badge" alt="اردو"></a>
  <a href="README.es.md"><img src="https://img.shields.io/badge/Lang-Español-orange?style=for-the-badge" alt="Español"></a>
</p>

Use any model you want — Azure Foundry, OpenRouter, OpenAI, local endpoints, and many others. Switch with `jimmy model` — no code changes, no lock-in.

<table>
<tr><td><b>A real terminal interface</b></td><td>Full TUI with multiline editing, slash-command autocomplete, conversation history, interrupt-and-redirect, and streaming tool output.</td></tr>
<tr><td><b>Lives where you do</b></td><td>Telegram, Discord, Slack, WhatsApp, Signal, and CLI — all from a single gateway process. Voice memo transcription, cross-platform conversation continuity.</td></tr>
<tr><td><b>A closed learning loop</b></td><td>Agent-curated memory with periodic nudges. Autonomous skill creation after complex tasks. Skills self-improve during use. FTS5 session search for cross-session recall. Compatible with the <a href="https://agentskills.io">agentskills.io</a> open standard.</td></tr>
<tr><td><b>Scheduled automations</b></td><td>Built-in cron scheduler with delivery to any platform. Daily reports, nightly backups, weekly audits — in natural language, running unattended.</td></tr>
<tr><td><b>Delegates and parallelizes</b></td><td>Spawn isolated subagents for parallel workstreams. Write Python scripts that call tools via RPC, collapsing multi-step pipelines into zero-context-cost turns.</td></tr>
<tr><td><b>Runs anywhere</b></td><td>Local, Docker, SSH, Singularity, Modal, Daytona, and Vercel Sandbox backends. Run it on a $5 VPS or a GPU cluster.</td></tr>
</table>

---

## Quick Install

### From this repo (recommended)

```bash
git clone https://github.com/code-gamerr/JIMMY-AGENT-.git
cd JIMMY-AGENT-
./setup-jimmy.sh          # Linux / macOS / WSL2 / Termux
# or on Windows PowerShell:
#   .\scripts\install.ps1
```

### One-liner (scripts in-repo)

```bash
# Linux, macOS, WSL2, Termux
curl -fsSL https://raw.githubusercontent.com/code-gamerr/JIMMY-AGENT-/main/scripts/install.sh | bash
```

```powershell
# Windows (native PowerShell)
irm https://raw.githubusercontent.com/code-gamerr/JIMMY-AGENT-/main/scripts/install.ps1 | iex
```

After installation:

```bash
jimmy              # start chatting
jimmy model        # choose provider + model
jimmy setup        # full setup wizard
jimmy gateway      # Telegram / Discord / Slack / …
jimmy doctor       # diagnose issues
```

Config lives in `~/.jimmy/` (or `%LOCALAPPDATA%\jimmy` on native Windows). Secrets go in `.env`; everything else in `config.yaml`.

> Legacy installs that still use `HERMES_HOME` / `~/.hermes` keep working — Jimmy reads those as a compatibility fallback when `JIMMY_HOME` is unset.

---

## Getting Started

```bash
jimmy              # Interactive CLI
jimmy model        # Choose LLM provider and model
jimmy tools        # Configure enabled tools
jimmy config set   # Set individual config values
jimmy config get   # Print individual config values
jimmy gateway      # Messaging gateway
jimmy setup        # Full setup wizard
jimmy claw migrate # Migrate from OpenClaw
jimmy update       # Update to the latest version
jimmy doctor       # Diagnose issues
jimmy prompt-size  # Measure system-prompt + tool-schema token cost
```

---

## CLI vs Messaging Quick Reference

| Action                         | CLI                                           | Messaging platforms                                                              |
| ------------------------------ | --------------------------------------------- | -------------------------------------------------------------------------------- |
| Start chatting                 | `jimmy`                                      | Run `jimmy gateway setup` + `jimmy gateway start`, then send the bot a message |
| Start fresh conversation       | `/new` or `/reset`                            | `/new` or `/reset`                                                               |
| Change model                   | `/model [provider:model]`                     | `/model [provider:model]`                                                        |
| Set a personality              | `/personality [name]`                         | `/personality [name]`                                                            |
| Retry or undo the last turn    | `/retry`, `/undo`                             | `/retry`, `/undo`                                                                |
| Compress context / check usage | `/compress`, `/usage`, `/insights [--days N]` | `/compress`, `/usage`, `/insights [days]`                                        |
| Browse skills                  | `/skills` or `/<skill-name>`                  | `/<skill-name>`                                                                  |
| Interrupt current work         | `Ctrl+C` or send a new message                | `/stop` or send a new message                                                    |
| Platform-specific status       | `/platforms`                                  | `/status`, `/sethome`                                                            |

---

## Documentation

| Doc | What's covered |
| --- | -------------- |
| [AGENTS.md](AGENTS.md) | Short contributor guide for AI coding assistants (kept lean for prompt size) |
| [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) | Full development / architecture guide |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribution process |
| [website/](website/) | In-repo docs site source |
| [docs/optimizer/ARCHITECTURE.md](docs/optimizer/ARCHITECTURE.md) | Harness optimizer design |

---

## Migrating from OpenClaw

```bash
jimmy claw migrate              # Interactive migration (full preset)
jimmy claw migrate --dry-run    # Preview what would be migrated
jimmy claw migrate --preset user-data   # Migrate without secrets
jimmy claw migrate --overwrite  # Overwrite existing conflicts
```

What gets imported: `SOUL.md`, memories, user skills, command allowlist, messaging settings, allowlisted API keys, TTS assets, and optional workspace `AGENTS.md`.

See `jimmy claw migrate --help`, or use the `openclaw-migration` skill for an agent-guided migration.

---

## Contributing

```bash
git clone https://github.com/code-gamerr/JIMMY-AGENT-.git
cd JIMMY-AGENT-
./setup-jimmy.sh
# or:
#   uv venv ~/.jimmy/venvs/jimmy-dev --python 3.11
#   source ~/.jimmy/venvs/jimmy-dev/bin/activate
#   uv pip install -e ".[all,dev]"
scripts/run_tests.sh
```

Create the venv **outside** the cloned source tree when possible — a relative-path wipe against the checkout can destroy a venv living inside it.

See [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md).

---

## Community

- 🐛 [Issues](https://github.com/code-gamerr/JIMMY-AGENT-/issues)
- 📚 [Skills Hub](https://agentskills.io)
- 🔌 [computer-use-linux](https://github.com/avifenesh/computer-use-linux) — Linux desktop-control MCP server

---

## License

MIT — see [LICENSE](LICENSE). Vendored sidecars retain upstream MIT notices:

- DeerFlow — [THIRD_PARTY_NOTICES_DEERFLOW.md](THIRD_PARTY_NOTICES_DEERFLOW.md), [docs/DEERFLOW_MERGE.md](docs/DEERFLOW_MERGE.md)
- ECC — [THIRD_PARTY_NOTICES_ECC.md](THIRD_PARTY_NOTICES_ECC.md), [docs/ECC_MERGE.md](docs/ECC_MERGE.md)
- OpenClaw — [THIRD_PARTY_NOTICES_OPENCLAW.md](THIRD_PARTY_NOTICES_OPENCLAW.md), [docs/OPENCLAW_MERGE.md](docs/OPENCLAW_MERGE.md)

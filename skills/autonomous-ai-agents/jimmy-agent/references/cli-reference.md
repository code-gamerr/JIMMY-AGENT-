# Jimmy CLI Reference

Live sources when anything looks stale: `jimmy --help`, `jimmy <command> --help`,
https://jimmy-agent.jimmy-agent.com/docs/reference/cli-commands

### Global Flags

```
jimmy [flags] [command]        (no subcommand = interactive chat)

  --version, -V             Show version
  -z, --oneshot PROMPT      One-shot: print ONLY the final response (for scripts/pipes)
  -m MODEL  --provider P    Model/provider override for this invocation
  -t, --toolsets LIST       Comma-separated toolsets for this invocation
  --resume, -r SESSION      Resume session by ID or title
  --continue, -c [NAME]     Resume by name, or most recent session
  --worktree, -w            Isolated git worktree mode (parallel agents)
  --skills, -s SKILL        Preload skills (comma-separate or repeat)
  --profile, -p NAME        Use a named profile
  --yolo                    Skip dangerous command approval
  --tui / --cli             Force the Ink TUI / classic REPL
  --ignore-rules            Skip AGENTS.md/SOUL.md/memory/skill injection
  --safe-mode               Disable ALL customizations (troubleshooting)
  --pass-session-id         Include session ID in system prompt
```

### Chat

```
jimmy chat [flags]
  -q, --query TEXT          Single query, non-interactive
  --image PATH              Attach a local image to a single query
  -Q, --quiet               Suppress banner, spinner, tool previews
  --checkpoints             Enable filesystem checkpoints (/rollback)
  --max-turns N             Cap tool-calling iterations
  --source TAG              Session source tag (default: cli)
```
(plus the global flags above)

### Configuration

```
jimmy setup [section]      Wizard (model|tts|terminal|gateway|tools|agent)
jimmy model                Interactive model/provider picker
jimmy fallback [add|remove|list]  Fallback provider chain
jimmy config [show|edit|get|set|unset|path|env-path|check|migrate]
jimmy login / logout       OAuth sign-in / clear stored auth
jimmy doctor [--fix]       Check dependencies and config
jimmy status [--all]       Component status
```

### Tools & Skills

```
jimmy tools [list|enable NAME|disable NAME]   Per-platform toolsets (curses UI with no args)

jimmy skills list|browse|search QUERY|inspect ID
jimmy skills install ID    Hub identifier OR a direct https://…/SKILL.md URL
jimmy skills config        Enable/disable skills per platform
jimmy skills check|update|uninstall|publish PATH
jimmy skills tap add REPO  Add a GitHub repo as a skill source
jimmy bundles              Skill bundles (one /<name> alias loads several skills)
```

### MCP Servers

```
jimmy mcp add NAME (--url or --command) | remove | list | test NAME
jimmy mcp catalog | install NAME     Curated catalog install
jimmy mcp configure NAME             Toggle tool selection
jimmy mcp serve                      Run Jimmy as an MCP server
```
Details (transport, tool discovery, catalog): `references/native-mcp.md`.

### Gateway (Messaging Platforms)

```
jimmy gateway run|install|start|stop|restart|status|setup
```

20+ platforms: Telegram, Discord, Slack, WhatsApp (Baileys + Business Cloud API), iMessage (Photon — `jimmy photon setup`), Signal, Email, SMS, Matrix, Mattermost, Teams, LINE, SimpleX, ntfy, Google Chat, Home Assistant, DingTalk, Feishu, WeCom, Weixin, API Server, Webhooks. Open WebUI connects via the API Server adapter. Most adapters ship under `plugins/platforms/`.
Docs: https://jimmy-agent.jimmy-agent.com/docs/user-guide/messaging/

### Sessions

```
jimmy sessions list|browse|rename ID TITLE|delete ID|export OUT|prune|stats
```

### Cron / Webhooks

```
jimmy cron list|create SCHED|edit ID|pause|resume|run ID|remove|status
    Schedules: '30m', 'every 2h', '0 9 * * *', ISO timestamp
jimmy webhook subscribe NAME|list|remove NAME|test NAME
```
Webhook payloads/routes: `references/webhooks.md`.

### Profiles

```
jimmy profile list|create NAME (--clone|--clone-all|--clone-from)|use|show|delete
jimmy profile rename A B | alias NAME | export NAME | import FILE
```

### Credentials & Pools

```
jimmy auth                 Interactive credential manager
jimmy auth add [PROVIDER]  Add OAuth or API-key credential (nous, openai-codex, qwen-oauth, …)
jimmy auth list|remove P IDX|reset PROVIDER|status
```
Multiple credentials per provider form a pool that rotates automatically and skips exhausted keys.

### Other

```
jimmy desktop / gui        Native desktop app
jimmy dashboard            Web admin panel + embedded chat (--stop / --status)
jimmy proxy                OpenAI-compatible local proxy backed by an OAuth provider
jimmy portal               Quick setup / sign in via Nous Portal
jimmy kanban <verb>        Multi-agent work-queue board
jimmy project              Named multi-folder workspaces
jimmy skin list|use|set    Switch/tweak skins (see references/themes.md)
jimmy pets <verb>          Pet mascots (see references/petdex.md)
jimmy memory setup|status|off|reset   Memory provider
jimmy secrets bitwarden|onepassword   External secret stores
jimmy moa                  Mixture-of-Agents slots
jimmy hooks / security / backup / import / checkpoints / console
jimmy logs [-f] [errors]   View agent/error logs
jimmy send                 One-off message through a gateway platform
jimmy pairing / plugins / insights / journey / computer-use
jimmy acp                  ACP server (IDE integration)
jimmy completion bash|zsh|fish
jimmy update / uninstall / claw migrate
```

Plugin- and provider-supplied subcommands (e.g. `jimmy photon setup`) only appear once their plugin is installed/active.

### Where to Find Things

| Looking for... | Location |
|---|---|
| Config options | `jimmy config edit` · [Configuration docs](https://jimmy-agent.jimmy-agent.com/docs/user-guide/configuration) |
| Tools / toolsets | `jimmy tools list` · [Tools reference](https://jimmy-agent.jimmy-agent.com/docs/reference/tools-reference) |
| Skills catalog | `jimmy skills browse` · [Skills catalog](https://jimmy-agent.jimmy-agent.com/docs/reference/skills-catalog) |
| Provider setup | `jimmy model` · [Providers guide](https://jimmy-agent.jimmy-agent.com/docs/integrations/providers) |
| Env variables | `jimmy config env-path` · [Env vars reference](https://jimmy-agent.jimmy-agent.com/docs/reference/environment-variables) |
| Gateway logs | `~/.jimmy/logs/gateway.log` (or `jimmy logs`) |
| Sessions | `jimmy sessions browse` (reads state.db) |

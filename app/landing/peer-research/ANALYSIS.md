# Peer analysis — 60 AI sites (Playwright evidence)

Source: `JIMMY_AI_PEER_SCRAPE.xlsx` + `RECON/batch/all-sites.json`  
Method: Chromium headless, live navigation, DOM signal extract + 1440px screenshot each.  
**Result: 60/60 HTTP OK.** No invented rows.

## Counts that shaped Jimmy

| Signal | Count |
|--------|------:|
| Sites scraped | 60 |
| Dark shell (heuristic) | 60/60 |
| Product/demo/video/canvas hero signal | 39/60 |
| Homepage `<video>` | 24/60 |
| Homepage `<canvas>` | 8/60 (subset) |
| Top category | coding-agent (10) |

## Patterns to steal (not markup)

1. **Hero = product surface** (Cursor, Linear, Windsurf→Devin Desktop, v0, Bolt, Lovable).
2. **One sharp claim** + dual CTA (GitHub Copilot, Claude Code, OpenHands).
3. **Surface map** GUI/CLI/SDK (OpenHands, LangChain, Aider terminal-native).
4. **Use-case specificity** (Devin PR/migration/triage; Zapier Agents; CrewAI/AG2 multi-agent).
5. **Orchestration language** (LangGraph “agent orchestration”, Factory, Augment).
6. **Local/OSS honesty** when that’s the product (Aider, Continue→Cursor acquisition note, OpenHands).

## Explicitly not copied

- Proprietary demos, video assets, logos, testimonials, customer counts.
- Windsurf URL now resolves to Devin Desktop (recorded as scraped final URL).
- Adept homepage title was “Blog” at scrape time — still logged honestly.

## Jimmy apply

Rebuild `landing/` as **内容爆改**: peer DNA (dark cinematic, product-first hero, surfaces, concrete jobs) + only real Jimmy facts (adapters, SSE events, loopback, CLI).

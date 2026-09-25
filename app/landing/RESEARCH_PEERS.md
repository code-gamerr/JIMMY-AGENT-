# Peer landing research — Jimmy

Live passes (2026-09-04). Steal **patterns**, not markup. No fake metrics on Jimmy’s page.

## Sites studied

| # | Site | URL | Steal for Jimmy |
|---|------|-----|-----------------|
| 1 | Cursor | https://cursor.com/ | Product *is* the hero — live demo stage, engineer voice |
| 2 | Linear | https://linear.app/ | Sparse claim + dense product UI cinema; purpose-built copy |
| 3 | Devin | https://devin.ai/ | Concrete use-case jobs, not vague “AI agents” |
| 4 | OpenHands | https://www.openhands.dev/ | Explicit surfaces (GUI / CLI / SDK) — map to CC + CLI + API |
| 5 | Cognition | https://cognition.com/ | Short manifesto only if needed — don’t become a lab brochure |
| 6 | SaaS pattern reviews | aydesign / vezadigital / foundey (2026) | Live preview > stock; social proof only if real; section grammar |

## Patterns applied

1. Full-bleed Command Center stage in the first viewport (Cursor-class).
2. Proof strip = **real module names** (OpenClaw / Munder / ECC) — no Fortune logos.
3. Loop section uses the real engine loop from `jimmy/ARCHITECTURE.md`.
4. Workers + API paths match adapters and documented endpoints.
5. CTA = `jimmy command-center` + real `command-center.html` — local-first, no fake signup.
6. Motion: stage entrance, live pulse, event feed rows; paused off-screen; respects `prefers-reduced-motion`.

## Explicitly omitted (no fake data)

- User counts, ARR, “trusted by N companies”
- Testimonials / quote walls
- Third-party logo bars for companies that don’t use Jimmy
- Invented file paths or green checkmarks for failed probes

## Files

- `landing/index.html` · `styles.css` · `main.js`
- Serve from **repo root** so `../jimmy/ui/command-center.html` resolves:
  `python -m http.server 8766` → http://127.0.0.1:8766/landing/

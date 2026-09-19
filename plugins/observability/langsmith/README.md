# LangSmith observability (DeerFlow parity)

DeerFlow supports LangSmith / Langfuse / Monocle. Jimmy already has a deep
**Langfuse** plugin; this plugin adds LangSmith opt-in.

```bash
jimmy plugins enable observability/langsmith
# in ~/.jimmy/.env:
LANGSMITH_API_KEY=lsv2_...
LANGSMITH_PROJECT=jimmy
```

For richer Jimmy-native traces (tool spans, subagents, MoA), prefer:

```bash
jimmy plugins enable observability/langfuse
```

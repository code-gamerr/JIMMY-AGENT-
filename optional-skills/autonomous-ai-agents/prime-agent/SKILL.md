---
name: prime-agent
description: Run Prime Agent for persistent, long-running agent work.
disable-model-invocation: true
version: 0.1.0
author: Arnav Singh, Jimmy
license: MIT
platforms: [linux, macos]
metadata:
  jimmy:
    tags: [Prime Agent, RLM, Autonomous Agents, Long-Running Tasks, Subagents]
    category: autonomous-ai-agents
    related_skills: [opencode, codex]
    requires_toolsets: [terminal]
---

# Prime Agent Skill

Prime Agent is an external coding and research agent with a persistent Python
REPL, recursive subagents, daemon-backed sessions, goals, schedules, and
continual harness state. This skill teaches Jimmy how to use it as an optional
worker; it does not replace Jimmy's normal conversation loop or automatically
start a second agent for every message.

## When to Use

- The user explicitly asks to use Prime Agent.
- A task is long-running and should survive terminal disconnection.
- The task benefits from a persistent REPL, recursive subagents, or resumable
  autonomous work.
- The user wants Prime Agent's `/refine` or continual-harness workflow.

Do not use Prime Agent for short answers, small edits, simple lookups, or
tasks Jimmy can complete directly. Starting a second model loop for those
tasks increases latency, cost, and duplicate context.

## Prerequisites

- Prime Agent installed and authenticated on a supported Linux or macOS host.
- A trusted repository or disposable worktree. Prime Agent executes
  model-generated Python and shell commands with the current user's
  permissions; its worker processes are not a security sandbox.
- A configured provider/API key or subscription.

Check availability with the `terminal` tool:

```bash
prime-agent --help
prime-agent status
```

Install from the official project instructions only:
https://github.com/PrimeIntellect-ai/prime-agent

## How to Run

Start it from the repository it should operate on:

```bash
cd /path/to/repository
prime-agent
```

For work that must continue after disconnecting, use the daemon/session
commands provided by the installed version:

```bash
prime-agent agents
prime-agent status
prime-agent --resume
```

Use a fresh session for unrelated work. Resume an existing session when the
task is a continuation so Prime Agent does not reread and restate the entire
repository context.

## Quick Reference

```text
prime-agent                 Start an agent in the current repository
prime-agent agents          List active, idle, and saved sessions
prime-agent attach <agent>  Reattach to a running session
prime-agent --resume        Resume or select a previous session
prime-agent status          Inspect the background service
prime-agent doctor          Diagnose the background service
prime-agent shutdown        Stop Prime Agent workers and services
```

Inside a session, use:

```text
/goal        Keep a durable objective and progress
/heartbeat   Schedule periodic re-entry
/autonomous  Continue within explicit budgets and quality gates
/refine      Review the trajectory and persist a focused improvement
```

## Procedure

1. Decide whether the task genuinely needs a persistent or autonomous worker.
2. Check that `prime-agent` is installed and its background service is
   healthy.
3. Use a disposable worktree for untrusted repositories or generated code.
4. Give one concise prompt containing the goal, constraints, acceptance
   checks, and expected final artifact.
5. Reuse `--resume` for follow-up work instead of starting another session.
6. Set explicit time, turn, and token budgets when autonomous mode is used.
7. Require a real quality gate—tests, lint, build, or another measurable
   check—before accepting completion.
8. Ask for a compact result containing only changes, checks, failures, and
   remaining work.
9. Stop or shut down idle workers when the task is complete.

## Token-Efficient Operation

- Prefer Jimmy's native tools for ordinary requests.
- Do not launch Prime Agent automatically for every user turn.
- Keep the initial prompt short; point to files and acceptance checks instead
  of pasting repository contents.
- Resume sessions so their persistent REPL and harness state are reused.
- Delegate only independent workstreams; avoid nested Jimmy ↔ Prime Agent
  loops.
- Use bounded autonomous mode and compact progress updates.
- Use `/refine` only for a specific, evidence-backed improvement. Review
  persistent changes before relying on them in future work.

## Pitfalls

- Prime Agent is not a sandbox. Do not run it against untrusted code with
  access to secrets or production credentials.
- It currently targets Linux and macOS; do not assume native Windows support.
- A running Prime Agent process does not mean a task succeeded. Inspect the
  worktree and quality-gate output.
- A second agent loop does not inherently save tokens. Unnecessary delegation
  can cost more than completing the task directly.
- Do not let Prime Agent and Jimmy modify the same worktree concurrently
  unless the work is intentionally coordinated.
- Do not claim that Prime Agent has trained or modified Jimmy's underlying
  model. It persists session/harness state, not model weights.

## Verification

```bash
prime-agent status
prime-agent doctor
```

For a completed task, verify the repository with its actual test or build
command and inspect the final diff before reporting success.

## References

- Project: https://github.com/PrimeIntellect-ai/prime-agent
- Documentation: https://github.com/PrimeIntellect-ai/prime-agent#readme

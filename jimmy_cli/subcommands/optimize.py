"""``jimmy optimize`` subcommand parser."""

from __future__ import annotations

from typing import Callable


def build_optimize_parser(subparsers, *, cmd_optimize: Callable) -> None:
    """Attach the ``optimize`` subcommand tree to ``subparsers``."""
    optimize_parser = subparsers.add_parser(
        "optimize",
        help="AutoAgent-style harness optimizer (benchmark + reversible candidates)",
        description=(
            "Run isolated offline/live benchmarks, capture per-call token and "
            "tool metrics via an opt-in observer, and compare reversible "
            "config overlays. Zero model-tool schema footprint."
        ),
    )
    optimize_parser.set_defaults(func=cmd_optimize, optimize_command="benchmark")

    opt_sub = optimize_parser.add_subparsers(dest="optimize_command")

    bench = opt_sub.add_parser(
        "benchmark",
        help="Run the representative task suite and write JSON/JSONL artifacts",
    )
    _add_common_args(bench)
    bench.set_defaults(func=cmd_optimize)

    cand = opt_sub.add_parser(
        "candidate",
        help="Run baseline vs config-overlay candidate; keep only if score improves",
    )
    _add_common_args(cand)
    cand.add_argument(
        "--overlay",
        default="{}",
        help='JSON object merged into config.yaml for the candidate (default: "{}")',
    )
    cand.add_argument(
        "--overlay-file",
        default=None,
        help="Path to JSON/YAML overlay (overrides --overlay)",
    )
    cand.set_defaults(func=cmd_optimize)

    search = opt_sub.add_parser(
        "search",
        help=(
            "Evaluate a small catalog of reversible config overlays across "
            "configurable axes; rank and keep winner only if improved"
        ),
    )
    _add_common_args(search)
    search.set_defaults(func=cmd_optimize)

    diag = opt_sub.add_parser(
        "diagnose-context",
        help="Diagnose first-turn 'Summarize what is in this folder' context cost",
    )
    diag.add_argument("--platform", default="cli", help="Platform to simulate")
    diag.add_argument("--json", action="store_true", help="Emit JSON")
    diag.set_defaults(func=cmd_optimize)

    listing = opt_sub.add_parser("list-tasks", help="List built-in optimize tasks")
    listing.add_argument("--category", default=None, help="Filter by category")
    listing.add_argument("--tasks", default=None, help="Comma-separated task ids")
    listing.set_defaults(func=cmd_optimize)

    report = opt_sub.add_parser(
        "report-offline",
        help="Write OFFLINE FIXTURE before/after report (not live-model evidence)",
    )
    report.add_argument(
        "--out",
        default=None,
        help="Markdown output path (default: docs/optimizer/OFFLINE_FIXTURE_REPORT.md)",
    )
    report.set_defaults(func=cmd_optimize)


def _add_common_args(parser) -> None:
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Offline deterministic fake runner (no provider credentials)",
    )
    parser.add_argument(
        "--offline",
        action="store_true",
        help="Alias for --dry-run",
    )
    parser.add_argument("--platform", default="cli", help="Platform toolset profile")
    parser.add_argument("--model", default="", help="Model for live AgentRunner")
    parser.add_argument(
        "--api-key",
        default=None,
        help="Explicit API key (live only; omit to use normal runtime resolution)",
    )
    parser.add_argument(
        "--base-url",
        default=None,
        help="Explicit base URL (live only; omit to use normal runtime resolution)",
    )
    parser.add_argument(
        "--provider",
        default=None,
        help="Explicit provider id (live only; omit to use config/runtime)",
    )
    parser.add_argument(
        "--simulation",
        default=None,
        help="Named FakeRunner simulation profile (offline/dry-run)",
    )
    parser.add_argument("--category", default=None, help="Comma-separated categories")
    parser.add_argument("--tasks", default=None, help="Comma-separated task ids")
    parser.add_argument("--out", default=None, help="Output root directory")
    parser.add_argument("--workspace", default=None, help="Task workspace root")
    parser.add_argument("--jimmy-home", default=None, help="Isolated JIMMY_HOME")
    parser.add_argument("--artifact-dir", default=None, help="Artifacts directory")
    parser.add_argument("--run-id", default=None, help="Run id for benchmark artifacts")

"""``jimmy command-center`` argparse tree."""

from __future__ import annotations

from typing import Callable


def build_command_center_parser(subparsers, *, cmd_command_center: Callable) -> None:
    parser = subparsers.add_parser(
        "command-center",
        aliases=("cc", "orchestrate"),
        help="Jimmy Command Center: route tasks to OpenClaw, Munder-Difflin, and ECC",
        description=(
            "Local orchestration layer. Binds 127.0.0.1 only. Workers are the "
            "existing openclaw/, munder-difflin/, and ECC/ checkouts."
        ),
    )
    parser.set_defaults(func=cmd_command_center, cc_command="serve")
    cc = parser.add_subparsers(dest="cc_command")

    serve_p = cc.add_parser("serve", help="Start the local Command Center UI + API")
    serve_p.add_argument("--host", default="127.0.0.1")
    serve_p.add_argument("--port", type=int, default=8765)
    serve_p.add_argument("--no-browser", action="store_true")
    serve_p.set_defaults(func=cmd_command_center, cc_command="serve")

    submit = cc.add_parser("submit", help="Submit a natural-language task")
    submit.add_argument("message")
    submit.add_argument(
        "--agent",
        default="auto",
        choices=("auto", "openclaw", "munder", "ecc", "landing", "research"),
    )
    submit.add_argument("--telegram-chat", default=None, help="Edit one Telegram status message for this task")
    submit.add_argument("--wait", action="store_true")
    submit.add_argument("--timeout", type=int, default=1800)
    submit.set_defaults(func=cmd_command_center, cc_command="submit")

    listing = cc.add_parser("list", help="List tasks")
    listing.set_defaults(func=cmd_command_center, cc_command="list")

    show = cc.add_parser("show", help="Show a task and its events")
    show.add_argument("task_id")
    show.set_defaults(func=cmd_command_center, cc_command="show")

    cancel = cc.add_parser("cancel", help="Cancel a running task")
    cancel.add_argument("task_id")
    cancel.set_defaults(func=cmd_command_center, cc_command="cancel")

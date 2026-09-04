#!/usr/bin/env python3
"""Run the Kronos financial-candle forecasting model for Jimmy."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any


UPSTREAM_URL = "https://github.com/shiyu-coder/Kronos.git"
UPSTREAM_COMMIT = "67b630e67f6a18c9e9be918d9b4337c960db1e9a"
DEFAULT_MODEL = "NeoQuasar/Kronos-small"
DEFAULT_TOKENIZER = "NeoQuasar/Kronos-Tokenizer-base"


def _jimmy_home() -> Path:
    """Resolve persistent paths through Jimmy' active profile."""
    try:
        from jimmy_constants import get_jimmy_home

        return get_jimmy_home()
    except ImportError as exc:
        raise RuntimeError(
            "Run this script from an installed Jimmy/Jimmy environment "
            "with JIMMY_HOME configured."
        ) from exc


def _paths() -> dict[str, Path]:
    home = _jimmy_home()
    return {
        "root": home / "cache" / "kronos",
        "source": home / "cache" / "kronos" / "Kronos",
        "venv": home / "venvs" / "kronos",
        "hf": home / "cache" / "huggingface",
    }


def _venv_python(paths: dict[str, Path]) -> Path:
    name = "python.exe" if os.name == "nt" else "python"
    return paths["venv"] / ("Scripts" if os.name == "nt" else "bin") / name


def _maybe_reexec_in_venv() -> None:
    """Use the dedicated runtime after setup without changing Jimmy's venv."""
    paths = _paths()
    python = _venv_python(paths)
    if not python.is_file() or Path(sys.executable).resolve() == python.resolve():
        return
    os.execv(str(python), [str(python), str(Path(__file__).resolve()), *sys.argv[1:]])


def _run(command: list[str], *, cwd: Path | None = None) -> str:
    try:
        completed = subprocess.run(
            command,
            cwd=cwd,
            check=True,
            text=True,
            capture_output=True,
        )
    except FileNotFoundError as exc:
        raise RuntimeError(
            f"Required executable is missing: {command[0]!r}. "
            "Install it and retry."
        ) from exc
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or exc.stdout or "").strip()
        raise RuntimeError(
            f"Command failed ({exc.returncode}): {' '.join(command)}\n{detail}"
        ) from exc
    return completed.stdout.strip()


def _setup(*, install: bool) -> None:
    paths = _paths()
    paths["root"].mkdir(parents=True, exist_ok=True)
    source = paths["source"]

    if source.exists() and not (source / ".git").is_dir():
        raise RuntimeError(
            f"{source} exists but is not a Git checkout. Move it aside and retry."
        )
    if not source.exists():
        _run(["git", "clone", "--filter=blob:none", UPSTREAM_URL, str(source)])

    _run(["git", "fetch", "--depth", "1", "origin", UPSTREAM_COMMIT], cwd=source)
    _run(["git", "checkout", "--detach", UPSTREAM_COMMIT], cwd=source)

    python = _venv_python(paths)
    if install:
        paths["venv"].parent.mkdir(parents=True, exist_ok=True)
        if not python.is_file():
            _run([sys.executable, "-m", "venv", str(paths["venv"])])
        requirements = Path(__file__).resolve().parent / "requirements.txt"
        _run([str(python), "-m", "pip", "install", "--upgrade", "pip"])
        _run([str(python), "-m", "pip", "install", "-r", str(requirements)])

    paths["hf"].mkdir(parents=True, exist_ok=True)
    print(
        json.dumps(
            {
                "ok": True,
                "source": str(source),
                "commit": UPSTREAM_COMMIT,
                "runtime": str(python) if python.is_file() else sys.executable,
                "installed": install,
                "huggingface_cache": str(paths["hf"]),
            },
            indent=2,
        )
    )


def _doctor() -> None:
    paths = _paths()
    report: dict[str, Any] = {
        "source": str(paths["source"]),
        "source_present": paths["source"].is_dir(),
        "runtime": str(_venv_python(paths)),
        "runtime_present": _venv_python(paths).is_file(),
        "huggingface_cache": str(paths["hf"]),
    }
    try:
        import importlib.util

        report["packages"] = {
            name: importlib.util.find_spec(name) is not None
            for name in ("numpy", "pandas", "torch", "einops", "huggingface_hub")
        }
        if report["packages"]["torch"]:
            import torch

            report["torch"] = torch.__version__
            report["cuda_available"] = bool(torch.cuda.is_available())
            report["cuda_device_count"] = int(torch.cuda.device_count())
    except Exception as exc:  # Doctor should report, not hide, environment issues.
        report["error"] = str(exc)
    print(json.dumps(report, indent=2, default=str))


def _load_candles(path: str, pd: Any) -> tuple[Any, Any]:
    frame = pd.read_csv(sys.stdin if path == "-" else path)
    columns = {str(column).strip().lower(): column for column in frame.columns}
    timestamp_name = next(
        (columns[name] for name in ("timestamp", "timestamps", "datetime", "date", "time") if name in columns),
        None,
    )
    if timestamp_name is None:
        raise ValueError(
            "Input must contain a timestamp column named timestamp, timestamps, "
            "datetime, date, or time."
        )
    required = ["open", "high", "low", "close"]
    missing = [name for name in required if name not in columns]
    if missing:
        raise ValueError(f"Input is missing required OHLC columns: {', '.join(missing)}")

    rename = {columns[name]: name for name in required}
    rename[timestamp_name] = "timestamp"
    for optional in ("volume", "amount"):
        if optional in columns:
            rename[columns[optional]] = optional
    frame = frame.rename(columns=rename)
    frame["timestamp"] = pd.to_datetime(frame["timestamp"], errors="coerce")
    if frame["timestamp"].isna().any():
        raise ValueError("Input contains invalid timestamps.")
    frame = frame.sort_values("timestamp").drop_duplicates("timestamp").reset_index(drop=True)
    for name in (*required, "volume", "amount"):
        if name not in frame:
            frame[name] = 0.0
        frame[name] = pd.to_numeric(frame[name], errors="coerce")
    if frame[required].isna().any().any():
        raise ValueError("Input contains non-numeric or missing OHLC values.")
    return frame, frame["timestamp"]


def _forecast(args: argparse.Namespace) -> None:
    _maybe_reexec_in_venv()
    try:
        import pandas as pd
        import torch
    except ImportError as exc:
        raise RuntimeError(
            "Kronos dependencies are not installed. Run: "
            f"{Path(__file__).resolve()} setup --install"
        ) from exc

    paths = _paths()
    if not paths["source"].is_dir():
        raise RuntimeError(
            "Kronos is not set up. Run the script with `setup --install` first."
        )
    paths["hf"].mkdir(parents=True, exist_ok=True)
    os.environ.setdefault("HF_HOME", str(paths["hf"]))
    sys.path.insert(0, str(paths["source"]))
    try:
        from model import Kronos, KronosPredictor, KronosTokenizer
    except ImportError as exc:
        raise RuntimeError(
            f"Could not import Kronos from {paths['source']}: {exc}"
        ) from exc

    frame, timestamps = _load_candles(args.input, pd)
    if len(frame) < args.lookback:
        raise ValueError(
            f"Input has {len(frame)} rows but lookback requires {args.lookback}."
        )
    history = frame.tail(args.lookback).reset_index(drop=True)
    inferred = args.freq or pd.infer_freq(timestamps.tail(args.lookback))
    if not inferred:
        raise ValueError("Could not infer candle frequency; provide --freq.")
    offset = pd.tseries.frequencies.to_offset(inferred)
    future_timestamps = pd.Series(
        [history["timestamp"].iloc[-1] + offset * index for index in range(1, args.pred_len + 1)]
    )

    device = args.device
    if device == "auto":
        device = "cuda" if torch.cuda.is_available() else "cpu"
    tokenizer = KronosTokenizer.from_pretrained(args.tokenizer)
    model = Kronos.from_pretrained(args.model).to(device).eval()
    predictor = KronosPredictor(model, tokenizer, max_context=args.max_context)
    input_columns = ["open", "high", "low", "close", "volume", "amount"]
    predictions = predictor.predict(
        df=history[input_columns],
        x_timestamp=history["timestamp"],
        y_timestamp=future_timestamps,
        pred_len=args.pred_len,
        T=args.temperature,
        top_p=args.top_p,
        sample_count=args.sample_count,
        verbose=False,
    )
    predictions.index = future_timestamps
    predictions.index.name = "timestamp"
    records = json.loads(predictions.to_json(orient="records", date_format="iso"))
    payload = {
        "model": args.model,
        "tokenizer": args.tokenizer,
        "device": device,
        "lookback": args.lookback,
        "prediction_length": args.pred_len,
        "frequency": str(inferred),
        "forecast": records,
        "disclaimer": "Model output only; not investment advice.",
    }

    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        if output.suffix.lower() == ".csv":
            predictions.to_csv(output)
        else:
            output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({"ok": True, "output": str(output), **{k: payload[k] for k in ("model", "device", "prediction_length")}}, indent=2))
    else:
        print(json.dumps(payload, indent=2))


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    setup = subparsers.add_parser("setup", help="Clone Kronos and optionally install its runtime.")
    setup.add_argument("--install", action="store_true", help="Create the isolated venv and install dependencies.")
    subparsers.add_parser("doctor", help="Report setup and runtime availability.")
    forecast = subparsers.add_parser("forecast", help="Forecast future OHLCV candles from a CSV.")
    forecast.add_argument("--input", required=True, help="CSV path, or - to read CSV from stdin.")
    forecast.add_argument("--output", help="Write .csv or .json output; otherwise print JSON.")
    forecast.add_argument("--lookback", type=int, default=400)
    forecast.add_argument("--pred-len", type=int, default=24)
    forecast.add_argument("--freq", help="Pandas frequency such as 5min, 1h, or 1D.")
    forecast.add_argument("--model", default=DEFAULT_MODEL)
    forecast.add_argument("--tokenizer", default=DEFAULT_TOKENIZER)
    forecast.add_argument("--max-context", type=int, default=512)
    forecast.add_argument("--temperature", type=float, default=1.0)
    forecast.add_argument("--top-p", type=float, default=0.9)
    forecast.add_argument("--sample-count", type=int, default=1)
    forecast.add_argument("--device", choices=("auto", "cpu", "cuda"), default="auto")
    return parser


def main() -> None:
    args = _parser().parse_args()
    if args.command == "setup":
        _setup(install=args.install)
    elif args.command == "doctor":
        _maybe_reexec_in_venv()
        _doctor()
    else:
        _forecast(args)


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, ValueError) as exc:
        print(f"kronos: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc

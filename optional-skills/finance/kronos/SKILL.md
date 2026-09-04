---
name: kronos
description: Forecast OHLCV market candles with Kronos.
version: 0.1.0
author: Arnav Singh, Jimmy
license: MIT
platforms: [linux, macos, windows]
metadata:
  jimmy:
    tags: [Kronos, Finance, Forecasting, OHLCV, Candles, Quantitative Finance]
    category: finance
    related_skills: [stocks]
    requires_toolsets: [terminal]
---

# Kronos Forecasting Skill

Kronos forecasts future financial candles from historical OHLCV data. This
skill runs the open-source Kronos model locally and does not place orders,
connect to brokerage accounts, or turn predictions into trading advice.

## When to Use

- The user asks for a Kronos forecast.
- The user wants a short-horizon OHLCV forecast from a CSV.
- The user wants to compare forecast paths or save predicted candles.

## Prerequisites

- Python 3.10+ and `git`.
- A CSV containing `timestamp` (or `timestamps`) and `open`, `high`, `low`,
  `close` columns. `volume` and `amount` are optional.
- CPU works for small experiments but can be slow. CUDA is recommended for
  repeated or long forecasts.
- The first setup downloads the Kronos source and model weights from GitHub
  and Hugging Face. Do not use forecasts as investment advice.

## How to Run

Use the `terminal` tool with the bundled script:

```bash
python ~/.jimmy/skills/finance/kronos/scripts/kronos_forecast.py setup --install
python ~/.jimmy/skills/finance/kronos/scripts/kronos_forecast.py forecast \
  --input candles.csv --pred-len 24 --freq 1h --output forecast.csv
```

The setup command stores the pinned Kronos checkout, Python environment, and
Hugging Face cache under the active Jimmy home. It is safe to run again.

## Quick Reference

```bash
SCRIPT=~/.jimmy/skills/finance/kronos/scripts/kronos_forecast.py

# Install the pinned runtime and source checkout
python $SCRIPT setup --install

# Forecast the next 24 hourly candles
python $SCRIPT forecast --input candles.csv --pred-len 24 --freq 1h

# Use a larger context and multiple sampled paths
python $SCRIPT forecast --input candles.csv --lookback 400 \
  --pred-len 120 --sample-count 3 --device cuda

# Write CSV or JSON
python $SCRIPT forecast --input candles.csv --pred-len 24 --output forecast.csv
python $SCRIPT forecast --input candles.csv --pred-len 24 --output forecast.json
```

## Procedure

1. Confirm the input contains timestamped candles sorted oldest to newest.
2. Run `setup --install` once in the active Jimmy/Jimmy profile.
3. Choose `--lookback` no greater than the model context. Kronos-small and
   Kronos-base use a maximum context of 512; the runner defaults to 400.
4. Set `--freq` explicitly when timestamp frequency cannot be inferred.
5. Run the forecast and inspect the output timestamps and OHLC relationships.
6. Treat the output as a model forecast only. Validate it with walk-forward
   backtesting, transaction costs, slippage, and risk controls before any
   research or investment decision.

## Pitfalls

- Kronos is a time-series model, not a general-purpose language model. It
  cannot answer arbitrary finance questions.
- A forecast is not a signal or a guaranteed price path. Avoid claims of
  certainty or guaranteed returns.
- The model expects chronological, consistently sampled candles. Gaps,
  duplicate timestamps, and mixed intervals reduce reliability.
- The default Hugging Face model is `NeoQuasar/Kronos-small` with
  `NeoQuasar/Kronos-Tokenizer-base`. Override both only when the matching
  tokenizer/model pair is available.
- The upstream model repository is pinned by commit in the runner, but model
  weights are downloaded by Hugging Face and should be reviewed before use.
- HumanEval-style code execution is unrelated to this skill; no generated
  code is executed by the forecast runner.

## Verification

Run the built-in self-check:

```bash
python ~/.jimmy/skills/finance/kronos/scripts/kronos_forecast.py doctor
```

It reports the source checkout, model cache location, Python runtime, and
whether the required packages and CUDA runtime are available.

## References

- Upstream project: https://github.com/shiyu-coder/Kronos
- Paper: https://arxiv.org/abs/2508.02739
- Model card: https://huggingface.co/NeoQuasar/Kronos-small

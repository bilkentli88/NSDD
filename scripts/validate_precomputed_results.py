#!/usr/bin/env python3
"""Check the internal consistency and expected structure of included results."""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results" / "extended" / "reference"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)
    print(f"[PASS] {message}")


def main() -> None:
    noise = pd.read_csv(RESULTS / "noise_scaling.csv")
    noise_runs = pd.read_csv(RESULTS / "noise_scaling_runs.csv")
    solver = pd.read_csv(RESULTS / "solver_refinement.csv")
    extra = pd.read_csv(RESULTS / "extrapolation.csv")
    osc = pd.read_csv(RESULTS / "oscillator_summary.csv")
    payload = json.loads((RESULTS / "key_results.json").read_text(encoding="utf-8"))

    require(np.allclose(noise["noise_std"], [0.0, 0.0005, 0.001, 0.002, 0.005]),
            "five expected observation-noise levels are present")
    require(len(noise_runs) == 10, "two scalar replicates are present at each noise level")
    require(np.allclose(solver["dt"], [0.1, 0.05, 0.025, 0.0125]),
            "four solver-refinement step sizes are present")
    require(set(extra["region"]) == {"interpolation", "extrapolation"},
            "interpolation and extrapolation rows are present")
    require(set(osc["model"]) == {"full_observation", "partial_x1_only", "unrestricted_fixed_delay_0.38"},
            "three delayed-oscillator regimes are present")
    require(len(payload["noise_scaling"]) == len(noise),
            "JSON and CSV noise summaries have matching lengths")
    require(np.isfinite(noise["clean_test_mse"]).all() and np.isfinite(noise["delay_rmse"]).all(),
            "reported scalar errors are finite")
    print("\nIncluded result files passed all structural checks.")


if __name__ == "__main__":
    main()

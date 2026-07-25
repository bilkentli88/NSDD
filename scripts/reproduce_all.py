#!/usr/bin/env python3
"""Run the principal and extended experiment pipelines from the repository root."""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(command: list[str]) -> None:
    print("$", " ".join(command), flush=True)
    subprocess.run(command, cwd=ROOT, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mode",
        choices=("quick", "paper"),
        default="quick",
        help="quick runs the principal smoke configuration; paper runs the three-seed principal configuration",
    )
    args = parser.parse_args()
    principal_mode = "smoke" if args.mode == "quick" else "paper"
    run([sys.executable, "experiments/run_principal_scalar.py", "--mode", principal_mode])
    run([sys.executable, "experiments/run_extended_experiments.py", "--mode", "paper"])


if __name__ == "__main__":
    main()

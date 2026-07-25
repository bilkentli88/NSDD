# Identifiability and Certification of Learned State-Dependent Delays

This repository contains the CPU-scale implementation and controlled experiments supporting the manuscript **“Identifiability and Certification of Learned State-Dependent Delays in Neural Delay Differential Equations.”**

The code distinguishes three questions that should not be conflated:

1. whether a model predicts trajectories accurately;
2. whether a state-dependent delay is structurally identifiable in the declared model class;
3. whether the available noisy histories support a practical certificate at a queried state.

The experiments cover unrestricted delay--field compensation, projectively informative and centered-degenerate history designs, trajectory-only optimization, observation-noise scaling, solver refinement, state-domain extrapolation, and partial observation in a delayed oscillator.

## Scientific scope

The positive recovery mechanism is restricted to the scalar affine delayed-state model and the fixed matched-slope inverse problem. Profile minimizers provide data-derived delay anchors, not ground-truth labels. The vector oscillator is a qualitative limitation experiment rather than a vector identifiability theorem.

## Repository structure

```text
.
├── experiments/
│   ├── run_principal_scalar.py
│   └── run_extended_experiments.py
├── scripts/
│   ├── reproduce_all.py
│   └── validate_precomputed_results.py
├── tests/
│   └── test_core_invariants.py
├── results/
│   ├── principal_scalar/
│   └── extended/
├── figures/
│   ├── principal_scalar/
│   └── extended/
├── checkpoints/
│   ├── reference/
│   ├── principal_scalar/
│   └── extended/
└── docs/
```

See [`docs/experiment_mapping.md`](docs/experiment_mapping.md) for the mapping between scientific claims, entry points, and outputs.

## Installation

Python 3.13 and a CPU build of PyTorch were used for the validated package.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

A Conda specification is also provided:

```bash
conda env create -f environment.yml
conda activate neural-sddde-identifiability
```

## Validate the included results

```bash
python scripts/validate_precomputed_results.py
python -m unittest discover -s tests -v
```

## Quick pipeline check

```bash
python scripts/reproduce_all.py --mode quick
```

This runs the shortened principal configuration and the validated extended configuration. It verifies the complete workflow but does **not** reproduce the three-seed principal summary.

## Manuscript-scale reproduction

```bash
python scripts/reproduce_all.py --mode paper
```

Equivalent individual commands are:

```bash
python experiments/run_principal_scalar.py --mode paper
python experiments/run_extended_experiments.py --mode paper
```

The extended `paper` mode reruns the configuration used for the included extended result files. Regenerated artifacts are written to `generated/` subdirectories so the supplied references are not overwritten. A longer, non-reference sensitivity configuration is available through:

```bash
python experiments/run_extended_experiments.py --mode extended
```

## Main outputs

- `results/principal_scalar/generated/model_summary.csv`
- `results/principal_scalar/generated/certificate_results.csv`
- `results/extended/reference/noise_scaling.csv`
- `results/extended/reference/solver_refinement.csv`
- `results/extended/reference/extrapolation.csv`
- `results/extended/reference/oscillator_summary.csv`
- supplied reference figures under `figures/extended/reference/` and regenerated figures under `figures/**/generated/`
- supplied reference state dictionaries under `checkpoints/` and regenerated states under `checkpoints/**/generated/`

## Computational requirements

The supplied extended configuration is designed for one CPU thread and typically completes in tens of seconds in the validated environment. The three-seed principal configuration is more expensive. Runtime and final digits may vary across platforms and PyTorch builds.

## Citation

The `CITATION.cff` file currently contains anonymous placeholder authorship and a placeholder repository URL. Replace these fields before public archival or DOI creation.

## License

The code is released under the MIT License. Checkpoint files are supplied solely to reproduce the accompanying experiments.
# NSDD
Code and controlled experiments for identifiability and certification of learned state-dependent delays in Neural DDEs.

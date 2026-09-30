# Matched-State Identifiability and Certification of Learned State-Dependent Delays in Neural Delay Differential Equations

This repository contains the CPU-scale implementation and controlled experiments associated with the manuscript **“Matched-State Identifiability and Certification of Learned State-Dependent Delays in Neural Delay Differential Equations.”**

The work distinguishes three questions that should not be conflated:

1. whether a model predicts trajectories accurately;
2. whether a state-dependent delay is structurally identifiable in the declared model class;
3. whether the available noisy histories support a practical certificate at a queried state.

The experiments examine unrestricted delay--field compensation, projectively informative and centered-degenerate history designs, profile-informed delay anchors, trajectory-only optimization, fresh-noise replication, observation-noise scaling, solver refinement, state-domain extrapolation, and partial observation in a delayed oscillator.

## Scientific scope

The positive recovery theory is restricted to the scalar affine delayed-state model and the fixed matched-slope inverse problem. It is not an if-and-only-if characterization of the complete trajectory observation operator.

Profile minimizers provide data-derived delay anchors rather than ground-truth labels. In the reported experiments, the profile-derived anchors and the rollout loss are constructed from the same training trajectories. The anchors should therefore be interpreted as a geometry-aware re-expression of information already present in the training data, not as independent supervision or independent validation.

The vector oscillator experiment is a qualitative partial-observation stress test and is not covered by the scalar projective-identifiability theorem.

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

See [`docs/experiment_mapping.md`](docs/experiment_mapping.md) for the mapping between manuscript results, experiment entry points, and generated outputs.

## Installation

Python 3.13 and a CPU build of PyTorch were used for the validated package.

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt
```

A Conda specification is also provided:

```bash
conda env create -f environment.yml
conda activate neural-sddde-identifiability
```

## Validate the included results

The supplied reference outputs can be checked without rerunning all training experiments:

```bash
python scripts/validate_precomputed_results.py
python -m unittest discover -s tests -v
```

## Quick pipeline check

```bash
python scripts/reproduce_all.py --mode quick
```

This executes shortened configurations intended to verify the end-to-end computational workflow. It is not intended to reproduce the full manuscript-scale replication.

## Manuscript-scale reproduction

```bash
python scripts/reproduce_all.py --mode paper
```

Equivalent individual commands are:

```bash
python experiments/run_principal_scalar.py --mode paper
python experiments/run_extended_experiments.py --mode paper
```

The `paper` configuration reproduces the computational settings associated with the supplied manuscript results. Regenerated artifacts are written to `generated/` subdirectories so that the supplied reference outputs are not overwritten.

A longer, non-reference sensitivity configuration is also available:

```bash
python experiments/run_extended_experiments.py --mode extended
```

## Main outputs

Principal scalar outputs include:

- `results/principal_scalar/generated/model_summary.csv`
- `results/principal_scalar/generated/certificate_results.csv`

Extended outputs include:

- `results/extended/reference/noise_scaling.csv`
- `results/extended/reference/solver_refinement.csv`
- `results/extended/reference/extrapolation.csv`
- `results/extended/reference/oscillator_summary.csv`

Reference figures are supplied under `figures/extended/reference/`, while regenerated figures are written under `figures/**/generated/`.

Reference model states are supplied under `checkpoints/`, and regenerated states are written under the corresponding `generated/` directories.

## Experimental replication

The fresh-noise confirmation uses five independently generated noisy datasets with three paired optimization seeds nested within each dataset. The five datasets are the independent data replications; the three optimization seeds quantify optimization variability and should not be interpreted as additional independent datasets.

Prediction error, delay error, and certificate outcomes are reported separately.

## Code and data availability

All datasets used in the reported experiments are synthetically generated by the provided code. No external proprietary dataset is required to reproduce the reported results.

The repository contains the experiment scripts, validation utilities, supplied reference outputs, model checkpoints, and configuration files needed to reproduce or verify the computational analyses reported in the manuscript and Supplementary Material.

## Computational requirements

The supplied extended configuration is designed for execution on a single CPU thread and typically completes in tens of seconds in the validated environment. The principal replication is more computationally demanding.

Runtime and final numerical digits may vary across operating systems, processor architectures, Python versions, and PyTorch builds.

## Citation

Citation metadata are provided in [`CITATION.cff`](CITATION.cff). Please use the bibliographic information associated with the manuscript or its published version when citing this work.

## License

The code is released under the MIT License. Checkpoint files are supplied for reproducibility of the accompanying computational experiments.

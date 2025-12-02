# ml-recipes-py

Curated, well-documented **machine learning recipes** in Python.

Each recipe is a small, focused example (script or notebook) that shows one idea clearly, with simple, readable code.

## Goals

- Make ML examples **approachable** for beginners and useful for intermediates.
- Prefer **small, self-contained recipes** over big frameworks.
- Encourage contributions: new recipes, better docs, small utilities.

## Getting started

```bash
git clone https://github.com/cutewizzy11/ml-recipes-py.git
cd ml-recipes-py

python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell
# .venv\\Scripts\\Activate.ps1

pip install .
# Or, for development
pip install .[dev]
```

Run tests:

```bash
pytest
```

## Project structure

```text
src/ml_recipes/
  datasets/
  models/
  training/
examples/notebooks/
docs/
tests/
```

## Example recipes (initial)

- Linear regression with scikit-learn
- Iris classification with scikit-learn
- Linear regression from scratch (NumPy)

See `examples/notebooks/` for Jupyter notebooks.

## Contributing

- Read [`CONTRIBUTING.md`](CONTRIBUTING.md).
- Check issues labeled `good first issue` and `help wanted`.
- Popular ways to contribute:
  - New notebooks covering classic ML tasks
  - Improving explanations and plots
  - Adding small utility functions in `src/ml_recipes/`

## Code of Conduct

See [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

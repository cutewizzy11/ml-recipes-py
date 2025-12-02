# Contributing

Thank you for considering contributing!

## How to get started

1. **Fork** the repository and clone your fork.
2. Create a virtual environment and install in editable mode:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -e .[dev]
   ```

3. Create a new branch for your change:

   ```bash
   git checkout -b feature/my-awesome-change
   ```

## Development workflow

- Run tests:

  ```bash
  pytest
  ```

- Format and lint:

  ```bash
  black .
  ruff .
  ```

- Keep PRs small and focused.

## Types of contributions

- **Code**: new utilities or recipe helpers.
- **Notebooks**: new educational Jupyter notebooks.
- **Docs**: clarifying explanations, better examples.
- **Tests**: adding coverage and regression tests.

## Pull request checklist

- [ ] Tests added or updated if needed.
- [ ] Code formatted with `black`.
- [ ] No new lint errors.
- [ ] Updated docs or README if behaviour changed.

## Communication

- Use GitHub Issues for bugs/feature requests.
- Be respectful and follow the Code of Conduct.

# Development

This section describes the process of developing the NQRduck software. 

## Style

Linting is done using [ruff](https://astral.sh/ruff) with the following configuration specified in the `pyproject.toml` file:

```toml
[tool.ruff]
exclude = [
  "widget.py",
  "base_spectrometer_widget.py",
]

[tool.ruff.lint]
extend-select = [
  "UP",  # pyupgrade
  "D",   # pydocstyle
]

[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401"]

[tool.ruff.lint.pydocstyle]
convention = "google"
```

Run `ruff check` to lint the code, ideally in a pre-commit hook.

## Branching

The main branch is used for releases. Development is done on a development branch. Feature branches are created from the development branch and merged back into it. The development branch is merged into the main branch for releases. Releases are tagged with a version number starting with `v` (e.g. `v0.1.0`) and should follow [semantic versioning](https://semver.org/) (right now they don't).

## Testing

Testing is done using [pytest](https://docs.pytest.org/en/stable/). The tests are located in the `tests` directory and can be run using `pytest`.
Right now the tests are not very extensive, but they are a good starting point for further development.

## Deployment

- The software is deployed via [PyPI](https://pypi.org/). Different modules are distributed as separate packages. The Action is run on a tag push to the main branch starting with `v` (e.g. `v0.1.0`).

- For Cython modules, `aarch64` and `x86_64` wheels are built using GitHub Actions. The wheels are deployed alongside the source distribution to PyPI.
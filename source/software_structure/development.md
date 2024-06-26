# Development

This section describes the process of developing the NQRduck software.

## Development of NQRduck modules

Here, an exemplary workflow for the development of new NQRduck modules is given.

If one wants to develop a new module, a template is provided [here](https://github.com/nqrduck/nqrduck-module). This template can be used as a starting point for a new module.

For example, if one wants to develop a new module called *myduck*, one would first clone the repository.

The template repository has the following file structure:

```bash
nqrduck-module/
|-- .gitignore
|-- LICENCE
|-- README.md
|-- pyproject.toml
|-- src/
|   |-- nqrduck_module/
|   |   |-- __init__.py
|   |   |-- controller.py
|   |   |-- model.py
|   |   |-- module.py
|   |   |-- resources/
|   |   |    |-- module.ini
|   |   |    |-- module_widget.ui
|   |   |-- view.py
|   |   |-- widget.py
```

*File structure of the NQRDuck module Git repository.*

If one would now like to create a module with the example name *myduck*, the folder and file names would be modified in the following way:

```bash
nqrduck-myduck/
|-- .gitignore
|-- LICENCE
|-- README.md
|-- pyproject.toml
|-- src/
|   |-- nqrduck_myduck/
|   |   |-- __init__.py
|   |   |-- controller.py
|   |   |-- model.py
|   |   |-- myduck.py
|   |   |-- resources/
|   |   |    |-- module.ini
|   |   |    |-- myduck_widget.ui
|   |   |-- view.py
|   |   |-- widget.py

```

*File structure of the newly created *myduck* module.*

The class names inside the model, view, and controller classes should also be modified to have a more representative name (e.g., `MyDuckController`, `MyDuckView`, `MyDuckModel`). The object created in the `myduck` file should also be renamed:

```python
from nqrduck.module.module import Module
from .model import MyDuckModel
from .view import MyDuckView
from .controller import MyDuckController

MyDuck = Module(MyDuckModel, MyDuckView, MyDuckController)
```

Then the `.ini` file inside the resources folder should be modified to represent the *myduck* module.

```toml
[META]
name = nqrduck-myduck
category = MyOwnModules
toolbar_name = MyDuck
tooltip = Template for a new module
```

*Example for the modified .ini file. The category, toolbar name, and tooltip can be freely chosen.*

Additionally, the `pyproject.toml` has to be modified to represent the new module structure:

```toml
[project]
name = "nqrduck-myduck"
version = "0.0.1"
authors = [
  { name="YOUR NAME", email="your@e.mail" },
]

description = "Your description"

...

dependencies = [
    "nqrduck",
    "pyqt6",
    ...
]

[project.entry-points."nqrduck"]
"nqrduck-myduck" = "nqrduck_myduck.myduck:MyDuck"
```

Now functionality can be implemented. For example, the `myduck_widget.ui` could be modified using Qt Designer. The `widget.py` file can then be updated using `pyuic6`.

```bash
# Navigate to the repository directory
cd nqrduck-myduck

# Generate your widget.py
pyuic6 src/nqrduck_myduck/resources/myduck_widget.ui > src/nqrduck_myduck/widget.py
```

The module should be installed to test its functionality. Ideally, the module is installed with the `-e` argument of `pip` to install it in editable mode. This means changes in the source code of the project will be applied without reinstalling the module.

```bash
# Navigate to the repository directory
cd nqrduck-myduck

# Install the package and all dependencies
pip install -e .
```

## Example pyproject.toml

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "nqrduck-module"
version = "0.0.1"
authors = [
  { name="Author Name", email="author@e.mail" },
]

description = "A template for nqrduck modules."
readme = "README.md"
license = { file="LICENSE" }
requires-python = ">=3.8"

classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

dependencies = [
    "matplotlib",
    "pyqt6",
    "nqrduck",
]

[project.entry-points."nqrduck"]
"nqrduck-module" = "nqrduck_module.module:module"
```

## Style

Here the style guide for the NQRduck software is described.

### Linting

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

### Formatting

Formatting is done using [black](https://black.readthedocs.io/en/stable/).

### Typing

Use type hints for all functions and classes. The type hints should be as specific as possible.

## Documentation

Documentation is implemented with [Sphinx](https://www.sphinx-doc.org/en/master/) project. The documentation is located in `NQRduckumentation` repository.

For docstrings in the code, the [Google style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) is used.

## Branching

The main branch is used for releases. Development is done on a development branch. Feature branches are created from the development branch and merged back into it. The development branch is merged into the main branch for releases. Releases are tagged with a version number starting with `v` (e.g. `v0.1.0`) and should follow [semantic versioning](https://semver.org/) (right now they don't).

## Testing

Testing is done using [pytest](https://docs.pytest.org/en/stable/). The tests are located in the `tests` directory and can be run using `pytest`.
Right now the tests are not very extensive, but they are a good starting point for further development.

## Deployment

- The software is deployed via [PyPI](https://pypi.org/). Different modules are distributed as separate packages. The Action is run on a tag push to the main branch starting with `v` (e.g. `v0.1.0`).

- For Cython modules, `aarch64` and `x86_64` wheels are built using GitHub Actions. The wheels are deployed alongside the source distribution to PyPI.

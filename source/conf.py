# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "NQRduckumentation"
copyright = "2024, jupfi"
author = "jupfi"
release = "0.0.1"
version = ""

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_theme_options = {
    'navbar_title': 'NQRduckumentation',
}

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    'sphinx.ext.todo',
]
autosummary_generate = True

autodoc_default_options = {
    "members": True,
}

# This is required for readthedocs to work with PyQt6
autodoc_mock_imports = [
    "matplotlib",
    "PyQt6",
    "PyQt6.QtWidgets",
    "PyQt6.QtCore",
    "PyQt6.QtGui",
    "ModuleView",
    "ModuleController",
    "ModuleModel",
    "nqrduck.module.module",
    "nqrduck_spectrometer.base_spectrometer",
]

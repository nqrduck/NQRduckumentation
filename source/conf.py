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
html_title = "NQRduckumentation"

html_css_files = [
    'css/custom.css',
]


html_theme_options = {
    "icon_links": [
        {
            # Label for this link
            "name": "GitHub",
            # URL where the link will redirect
            "url": "https://github.com/nqrduck/",
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fa-brands fa-square-github",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        }
   ]
}


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    'sphinx.ext.todo',
    'myst_parser',
    'sphinx_design',
    'sphinxcontrib.bibtex'
]
myst_enable_extensions = ["colon_fence"]
autosummary_generate = True

bibtex_bibfiles = ['references.bib']
bibtex_default_style = 'plain'

autodoc_default_options = {
    "members": True,
}

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
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

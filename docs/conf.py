import os
import sys

sys.path.insert(0, os.path.abspath(".."))

# Project Information

project = "Raster Forge"
copyright = "2024, Afonso Oliveira"
author = "Afonso Oliveira"

# General Configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx_design",
    "sphinxawesome_theme.highlighting",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

nitpicky = True
default_role = "literal"

napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False

# HTML Output

html_theme = "sphinx_material"

html_title = "Raster Forge"

html_logo = "_static/logo-flat.svg"
html_favicon = "_static/logo-flat.svg"

html_theme_options = {
    "nav_title": "Raster Forge",
    "base_url": "https://afe-oliveira.github.io/raster-forge/",
    "color_primary": "yellow",
    "color_accent": "teal",
    "repo_type": "github",
    "repo_url": "https://github.com/afe-oliveira/raster-forge",
    "repo_name": "raster-forge",
    "globaltoc_depth": 5,
    "globaltoc_collapse": True,
    "globaltoc_includehidden": True,
}

html_last_updated_fmt = ""

html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

html_static_path = ["_static"]

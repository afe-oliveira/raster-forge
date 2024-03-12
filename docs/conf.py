import os
import sys

sys.path.insert(0, os.path.abspath('..'))

# Project Information

project = 'Raster Forge'
copyright = '2024, Afonso Oliveira'
author = 'Afonso Oliveira'

# General Configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinx.ext.viewcode",
    "sphinx_design",
    "sphinxawesome_theme.highlighting",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

nitpicky = True
default_role = "literal"

# HTML Output

html_theme = "sphinxawesome_theme"
extensions += ["sphinxawesome_theme.highlighting"]

html_title = 'Raster Forge'
html_last_updated_fmt = ""
html_logo = "_static/logo-flat.svg"
html_favicon = "_static/logo-flat.svg"

html_static_path = ['_static']

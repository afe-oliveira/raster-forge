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

html_theme = "pydata_sphinx_theme"

html_title = "Raster Forge"

html_favicon = "_static/logo-flat.svg"

html_last_updated_fmt = ""

html_theme_options = {
    "logo": {
        "alt_text": "Raster Forge",
        "image_light": "_static/logo-flat.svg",
        "image_dark": "_static/logo-flat-white.svg",
    },
    "navbar_align": "left",
    "show_prev_next": False,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/afe-oliveira/raster-forge",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
        }, {
            "name": "PyPi",
            "url": "https://pypi.org/project/raster-forge/",
            "icon": "fa-solid fa-box",
            "type": "fontawesome",
        }
   ]
}

html_static_path = ["_static"]
html_css_files = [
    'css/custom.css',
]

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme
from datetime import datetime

# -- Project information -----------------------------------------------------

project = 'HIP user documentation'
version = '2.0'
copyright = '2022-' + str(datetime.now().year) + ', The Human Intracerebral EEG Platform. Contact: support@thehip.app'
author = 'HIP documentation team'


# The full version, including alpha/beta/rc tags
#release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

html_extra_path = ['welcome.html']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_logo = '_static/HIP_LOGO_BASELINE_RVB_Blanc.png'

# Cloud
#html_theme = "cloud" # cloud
#html_theme_options = {
#'sidebar_localtoc_title': 'Table of Contents',
#'lighter_header_decor':'True',
#'shaded_decor':'True',
#'borderless_decor':'True',
#'default_layout_text_size':'90%'
#}

# Read the doc
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    'sticky_navigation': False,
    'style_nav_header_background': 'black',
    'logo_only': True,
    'prev_next_buttons_location': None
}

master_doc = 'user_doc'

# Material
#html_theme = "sphinx_material"
#html_theme_options = {
#'color_primary': 'blue',
#'nav_title':'HIP user documentation',
#'nav_links':[{'href':'a','title':'b','internal':'c'}],
#'globaltoc_depth':'1'
#}
#html_sidebars = {
#    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
#}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static'] #['_static'] []
html_css_files = ["custom.css"]

html_context = {
    "display_github": True, # Integrate GitHub
    "github_user": "HIP-infrastructure", # Username
    "github_repo": "HIP-infrastructure.github.io", # Repo name
    "github_version": "master", # Version
    "conf_py_path": "/docs/source/", # Path in the checkout to the docs root
}

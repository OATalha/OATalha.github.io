# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "OATalha's Doc Test"
copyright = '2022, Talha Ahmed'
author = 'Talha Ahmed'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os
import sys

sys.path.append(os.path.abspath('./'))

extensions = []

templates_path = ['_templates']
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx_affiliates',
]
exclude_patterns = []

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'arithmetics': ('https://oatalha.github.io/mymath.arithmetics', None),
    'trigonometry': ('https://oatalha.github.io/mymath.trigonometry', None),
}

affiliate_options = {'canonical_url': "https://oatalha.github.io/"}

sphinx_affiliates = [
    'https://oatalha.github.io/mymath.arithmetics/affiliate_searchindex.js',
    'https://oatalha.github.io/mymath.trigonometry/affiliate_searchindex.js'
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = './_static/One-Animation-Logo-Small.png'
html_favicon = './_static/favicon.ico'

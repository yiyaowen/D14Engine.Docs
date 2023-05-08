# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'D14Engine'
copyright = '2023, D14Studio'
author = 'yiyaowen'

version = 'developing'

# -- General configuration

extensions = ['myst_parser']

# -- Options for HTML output

html_theme = 'sphinx_book_theme'

# -- Options for translation

locale_dir = ["locales"]

gettext_uuid = True
gettext_compact = False

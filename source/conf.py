# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'D14Engine'
author = 'yiyaowen'
copyright = '2023, yiyaowen'
version = 'alpha && beta'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_tabs.tabs']

sphinx_tabs_disable_tab_closing = True

# -- Options for internationalization
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-internationalization

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_logo = 'https://raw.githubusercontent.com/yiyaowen/D14Engine.Docs.Img/main/logo.png'
html_favicon = 'https://raw.githubusercontent.com/yiyaowen/D14Engine.Docs.Img/main/favicon.png'

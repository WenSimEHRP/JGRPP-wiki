import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "OpenTTD JGRPP 中文百科"
author = "JGRennison and WenSim"
release = "0.1"
copyright = "2024 JGRennison 与 WenSim"
templates_path = ["_templates"]

language = "zh_CN"
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

'''
latex_engine = 'xelatex'
latex_elements = {
    'preamble': '\\usepackage[UTF8]{ctex}\n',
}
'''

html_theme = "sphinx_rtd_theme"
html_logo = "_static/logo.png"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.duration",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.autosectionlabel",
    "myst_parser",
]

myst_enable_extensions = [
    "deflist",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

# add custom css
html_static_path = ["_static"]
html_css_files = ["fonts.css"]

# conf.py

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# 项目信息
project = 'Your Project Name'
author = 'Your Name'
release = '0.1'

# Sphinx 扩展
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'myst_parser',  # 用于解析 Markdown 文件
]

# 模板路径
templates_path = ['_templates']

# 语言
language = 'zh_CN'

# 排除的文件和目录
exclude_patterns = []

# Markdown 设置
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# 主文档
master_doc = 'Home'

# Napoleon 设置 (用于 Google 和 NumPy 风格的 docstrings)
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
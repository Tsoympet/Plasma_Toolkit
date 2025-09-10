
import os, sys, datetime
sys.path.insert(0, os.path.abspath('..'))
project='Plasma Toolkit'; author='Your Name'; current_year=datetime.datetime.now().year
extensions=['sphinx.ext.autodoc','sphinx.ext.autosummary','sphinx.ext.napoleon','sphinx.ext.mathjax','sphinx.ext.viewcode']
autosummary_generate=True; napoleon_google_docstring=False; napoleon_numpy_docstring=True
templates_path=['_templates']; exclude_patterns=[]; html_theme='sphinx_rtd_theme'; html_static_path=['_static']

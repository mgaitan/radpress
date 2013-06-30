import datetime
import os
import sys

DOC_DIR = os.path.realpath(os.path.dirname(__file__))
PROJECT_DIR = os.path.join(DOC_DIR, '..', 'radpress')

sys.path.insert(0, PROJECT_DIR)

import radpress

#needs_sphinx = '1.0'
extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
#source_encoding = 'utf-8-sig'
master_doc = 'index'
project = u'radpress'
copyright = u'%s, Gokmen Gorgen' % datetime.date.today().year

version = radpress.get_version()
release = version
#language = None
#today = ''
#today_fmt = '%B %d, %Y'
exclude_patterns = ['_build']
#default_role = None
#add_function_parentheses = True
#add_module_names = True
#show_authors = False
pygments_style = 'sphinx'
#modindex_common_prefix = []
# html_theme = 'haiku'
#html_theme_options = {}
#html_theme_path = []
#html_title = None
#html_short_title = None
#html_logo = None
#html_favicon = None
html_static_path = ['_static']
#html_last_updated_fmt = '%b %d, %Y'
#html_use_smartypants = True
#html_sidebars = {}
#html_additional_pages = {}
#html_domain_indices = True
#html_use_index = True
#html_split_index = False
#html_show_sourcelink = True
#html_show_sphinx = True
#html_show_copyright = True
#html_use_opensearch = ''
#html_file_suffix = None
htmlhelp_basename = 'radpressdoc'

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #'preamble': '',
}

latex_documents = [
    ('index', 'radpress.tex', u'radpress Documentation', u'Gokmen Gorgen',
     'manual'),
]
#latex_logo = None
#latex_use_parts = False
#latex_show_pagerefs = False
#latex_show_urls = False
#latex_appendices = []
#latex_domain_indices = True

man_pages = [
    ('index', 'radpress', u'radpress Documentation', [u'Gokmen Gorgen'], 1)
]

#man_show_urls = False
texinfo_documents = [
    ('index', 'radpress', u'radpress Documentation', u'Gokmen Gorgen',
     'radpress', 'One line description of project.', 'Miscellaneous'),
]

#texinfo_appendices = []
#texinfo_domain_indices = True
#texinfo_show_urls = 'footnote'

"""
Copied and modified from django-rstify extension.
"""

from docutils.core import publish_parts
from docutils.writers import html4css1
from django.utils.encoding import force_unicode, smart_str
from radpress.settings import RST_SETTINGS
from radpress.rst_extensions import register_directives

# register radpress customized directives
register_directives()


def rstify(text):
    parts = get_parts(text)
    return force_unicode(parts['fragment'])


def get_parts(text):
    parts = publish_parts(
        source=smart_str(text),
        writer=html4css1.Writer(),
        settings_overrides=RST_SETTINGS)

    return parts

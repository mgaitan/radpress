import docutils
from docutils.core import publish_programmatically
from docutils.writers import html4css1
from django.utils.encoding import force_unicode, smart_str
from radpress.rst_extensions import register_directives
from radpress.settings import RST_SETTINGS
import re
try:
    from markdown import Markdown
except ImportError:
    Markdown = None  # NOQA

# register radpress customized directives
register_directives()


class Reader(object):
    """
    Thanks to pelican contributors.
    """
    enabled = False

    def __init__(self, source):
        self.source = smart_str(source)


class RstReader(Reader):
    """
    Radpress' default reader. It should be always enabled.
    """
    enabled = True

    def _parse_metadata(self, document):
        output = {
            'title': document.get('title'),
            'published': False
        }

        for docinfo in document.traverse(docutils.nodes.docinfo):
            for element in docinfo.children:
                if element.tagname != 'field':
                    continue

                name_elem, body_elem = element.children
                name = name_elem.astext().lower()
                value = body_elem.astext()

                if name == 'tags':
                    value = set([t.strip() for t in value.split(',')])

                elif name == 'published':
                    value = value == 'yes'

                output[name] = value

        return output

    def _get_publisher(self):
        output, pub = publish_programmatically(
            source=self.source,
            source_path=None,
            source_class=docutils.io.StringInput,
            destination_class=docutils.io.StringOutput,
            destination=None,
            destination_path=None,
            reader=None,
            reader_name='standalone',
            parser=None,
            parser_name='restructuredtext',
            writer=html4css1.Writer(),
            writer_name='pseudoxml',
            settings=None,
            settings_spec=None,
            settings_overrides=RST_SETTINGS,
            config_section=None,
            enable_exit_status=False)

        return pub

    def read(self):
        pub = self._get_publisher()
        metadata = self._parse_metadata(pub.document)
        content = force_unicode(pub.writer.parts.get('body'))

        return content, metadata


class MarkdownReader(Reader):
    enabled = bool(Markdown)

    def convertRSTmetaToMD(self):
        token = re.compile(r":(\w+:)")
        # http://stackoverflow.com/questions/2212933/python-regex-for-reading-csv-like-rows  # NOPEP8
        comma = re.compile(r'''
            \s*                # Any whitespace.
            (                  # Start capturing here.
              [^,"']+?         # Either a series of non-comma non-quote chars.
              |                # OR
              "(?:             # A double-quote followed by a string of chars.
                  [^"\\]|\\.   # That are either non-quotes or escaped...
               )*              # ...repeated any number of times.
              "                # Followed by a closing double-quote.
              |                # OR
              '(?:[^'\\]|\\.)*'# Same as above, for single quotes.
            )                  # Done capturing.
            \s*                # Allow arbitrary space before the comma.
            (?:,|$)            # Followed by a comma or the end of a string.
            ''', re.VERBOSE)
        pass1 = []
        pass2 = []

        # First, replace ":token:" with "token:"
        for line in self.source.split('\r\n'):
            if not line or line.isspace():
                break
            pass1.append(token.sub(r'\1', line))

        # Assume it's properly formatted markdown
        if pass1 == self.source.split('\r\n')[:len(pass1)]:
            return

        # Next, split up comma-seperated tags into newlines + indents
        for line in pass1:
            csv = comma.sub('\\1\n    ', line).strip()
            if csv != line:
                pass2.append(csv)
            else:
                pass2.append(line)

        # First line is a title
        pass2[0] = "title: " + pass2[0]
        # Every other line until the point where they're all the same char must
        # be the title line too, so we indent those.
        for i in xrange(1, len(pass2)):
            if pass2[i] and pass2[i] == len(pass2[i]) * pass2[i][0]:
                pass2 = pass2[:i] + pass2[i+1:]
                break
            else:
                pass2[i] = "   " + pass2[i]

        # Now, reconstruct the source: use our new tags + the remainder of the
        # source (+1 for the sake of the line of #'s).
        # Put the \r back because that's how django gave it to us, even though
        # it's stupid.
        self.source = "\r\n".join(pass2 +
                                  self.source.split("\r\n")[len(pass2)+1:])

    def _parse_metadata(self, meta):
        out = meta
        for key in out.iterkeys():
            if len(out[key]) == 1:
                out[key] = "".join(out[key])
            if key == "published":
                out[key] = out[key] == "yes"
            if key == "tags":
                out[key] = list(set(out[key]))

        return out

    def read(self):
        """Parse content and metadata of markdown files"""
        self.convertRSTmetaToMD()
        self._md = Markdown(extensions=['meta'])
        content = self._md.convert(self.source)
        metadata = self._parse_metadata(self._md.Meta)
        return content, metadata

from radpress.readers import MarkdownReader


def mdify(source):
    content, metadata = MarkdownReader(source).read()
    return content

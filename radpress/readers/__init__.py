import importlib
import os
from django.utils.encoding import smart_str

from radpress.settings import DEFAULT_READER


class BaseReader(object):
    """
    Thanks to pelican contributors.
    """
    enabled = False
    name = None

    def __init__(self, source):
        self.source = smart_str(source)


def get_reader(name=None):
    if name is None:
        name = DEFAULT_READER

    module_path = 'radpress.readers.%s_reader' % name
    reader = importlib.import_module(module_path).Reader
    return reader


def get_markup_choices():
    """
    Receives available markup options as list.
    """
    available_reader_list = []
    module_dir = os.path.realpath(os.path.dirname(__file__))
    module_names = filter(
        lambda x: x.endswith('_reader.py'), os.listdir(module_dir))

    for module_name in module_names:
        name = module_name.split('_')[0]
        reader = get_reader(name=name)

        if reader.enabled is True:
            available_reader_list.append((name, reader.name))

    return available_reader_list

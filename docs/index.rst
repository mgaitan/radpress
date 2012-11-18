.. radpress documentation master file, created by
   sphinx-quickstart on Fri May 25 15:23:49 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Radpress
========
Radpress is a simple blog application for Djangonauts. It doesn't use WYSIWYG
editor. The default markup syntax is `reStructuredText`_ and you can preview
your entry simply before published it.

Installation
------------
You can install Radpress with `pip` or `easy_install`::

    pip install radpress

It also installs it's dependencies, but you need some configuration after
package installation. In your django project, you should add `easy_thumbnails`
before `radpress`.

Python Imaging Library
----------------------
To use ImageFields in Django, you need to `Python Imaging Library`_. It doesn't
written as dependency to Radpress. Maybe you want to use Pillow_ instead of
PIL_.

Contents:

.. toctree::
   :maxdepth: 2

   configuration
   development



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _Python Imaging Library: http://docs.djangoproject.com/en/dev/ref/forms/fields/#imagefield
.. _Pillow: http://github.com/python-imaging/Pillow
.. _PIL: http://www.pythonware.com/products/pil/

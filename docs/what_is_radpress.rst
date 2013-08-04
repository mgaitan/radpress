What is Radpress?
=================
Radpress is a simple blog application for Djangonauts. It doesn't use WYSIWYG
editor. The default markup syntax is `reStructuredText`_ and you can preview
your entry simply before published it.

Features
--------
- Zen mode for writing articles
- Disqus support for comment and reactions
- Useful sidebar widgets; tag cloud, latest posts
- Adding page links in navigation bar
- Listing archives for date or tag
- Author information for articles
- Simple theme like as Octopress.

Requirements
------------
- Django >= 1.4
- docutils >= 0.9  `# for reStructuredText`
- Pygments >= 1.5  `# for highlighting code syntax`
- easy-thumbnails >= 1.0.3
- and Pillow or PIL

Installation
------------
You can install Radpress with `pip` or `easy_install`::

    pip install radpress

It also installs it's dependencies, but you need some configuration after
package installation. In your django project, you should add
``easy_thumbnails`` before ``radpress``.

Python Imaging Library
----------------------
We prefer Pillow_ in stage of development. But it's not added to ``setup.py``
as mandatory dependency. You want to continue to use PIL_ in your project.
This and ``easy-thumbnails`` is required to add image for articles, and
cropping and resizing images.

.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _Python Imaging Library: http://docs.djangoproject.com/en/dev/ref/forms/fields/#imagefield
.. _Pillow: http://github.com/python-imaging/Pillow
.. _PIL: http://www.pythonware.com/products/pil/

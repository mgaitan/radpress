Configuration
=============

RADPRESS_TITLE
--------------
Set your blog title.

**Default:** "Radpress"

RADPRESS_DESCRIPTION
--------------------
Set your blog description.

**Default:** "A blogging application for Djangonauts"

RADPRESS_LIMIT
--------------
Set blog entry count in a page.

**Default:** 5

RADPRESS_GA_CODE
----------------
Set Google Analytics code to enable support.

**Default:** None

RADPRESS_DISQUS
---------------
Set shortname if you want to enable Disqus comments support.

**Default:** None

RADPRESS_COVER_SIZE
-------------------
You can change default cover image size.

**Default:** '799x300'

RADPRESS_BOOTSTRAP_CSS
----------------------
`bootstrap.css` or `bootstrap.min.css` path.

**Default:** {{ STATIC_URL }}radpress/bootstrap/css/bootstrap.min.css

RADPRESS_BOOTSTRAP_RESPONSIVE_CSS
---------------------------------
`bootstrap-responsive.css` or `bootstrap.min.css` path.

**Default:** None, because it's included to custom bootstrap file.

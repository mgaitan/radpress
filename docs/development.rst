Development
===========
Thanks in advance for the contribution! Please start with installing
requirements for the development::

    $ pip install -r requirements/development.txt

Then, see the issues in Github: https://github.com/gkmngrgn/radpress/issues

If you want to send your changes to us, create your fork, open the branch about
your changes, commit them and send a pull request. That's all.

LESS Usage
----------
Do NOT try to edit ``main.css`` file directly. Learn LessCSS_ and edit less
files that you can find them it ``static/radpress_less`` directory. To compile
less files and convert to css::

    $ lessc --yui-compress radpress_less/main.less > radpress/css/main.css

JS Components
-------------
jquery.js
'''''''''
I am not a frontend developer, but jQuery seems very easy and some javascript
libraries need to jQuery.

http://jquery.com/

taboverride.min.js
''''''''''''''''''
It's required to override tab behaviour in zen mode textarea.

http://wjbryant.github.io/taboverride/


.. _LessCSS: http://lesscss.org/

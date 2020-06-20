strip-ansi
----------

    Strip ANSI escape sequences from a string


Installation
============

`strip-ansi` is available on `on PyPI <https://pypi.org/project/strip-ansi>`_:

.. code:: shell
   
   pip install strip_ansi

Usage
=====

.. WARNING::
   This package only supports python 3.6 and up. It may work on older versions (maybe even python 2)
   but I'm not sure.

.. code:: python

   >>> from strip_ansi import strip_ansi
   >>> strip_ansi("\033[38mLorem ipsum\033[0m")
   "Lorem ipsum"

dukpy
================

|unix_build| |windows_build| |coverage|

dukpy is a JavaScript runtime environment for Python (tested with python 2.7
and >= 3.4) using the `duktape <http://duktape.org/>`_ embeddable JavaScript
engine. With dukpy, you can run JavaScript in Python.

Example:

.. code-block:: python

    import dukpy

    ctx = dukpy.Context()
    ctx.eval('str = "Hello, World!";');

    # ctx.g to refers to the global object
    print(ctx.g.str)
    # ==> Hello, World!

    # Python functions can be called from JavaScript
    def add(x, y):
        return x + y

    ctx.g.add = add
    ctx.eval('result = add(10, 32);')
    print(ctx.g.result)
    # ==> 42

    # JavaScript functions can be called from Python
    ctx.eval('var sub = function (x, y) { return x - y; };')
    print(ctx.g.sub(52, 10))
    # ==> 42


.. |unix_build| image:: https://api.travis-ci.org/kovidgoyal/dukpy.svg
    :target: http://travis-ci.org/kovidgoyal/dukpy
    :alt: Build status of the master branch on Unix

.. |windows_build|  image:: https://ci.appveyor.com/api/projects/status/github/kovidgoyal/dukpy?svg=true
    :target: https://ci.appveyor.com/project/kovidgoyal/dukpy
    :alt: Build status of the master branch on Windows

.. |coverage| image:: https://coveralls.io/repos/kovidgoyal/dukpy/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/kovidgoyal/dukpy?branch=master
    :alt: Code coverage

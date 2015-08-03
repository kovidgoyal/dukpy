# Dukpy

[![Build Status](https://travis-ci.org/kovidgoyal/dukpy.svg?branch=master)](https://travis-ci.org/kovidgoyal/dukpy) [![Coverage Status](https://coveralls.io/repos/kovidgoyal/dukpy/badge.svg?branch=master)](https://coveralls.io/r/kovidgoyal/dukpy?branch=master)

Dukpy is a JavaScript runtime environment for Python using the
[duktape](http://duktape.org/) embeddable JavaScript engine. With
dukpy, you can run JavaScript in Python.

Example:
```python
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
```

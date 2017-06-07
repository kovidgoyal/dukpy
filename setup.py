#!/usr/bin/env python
import glob
import sys

from setuptools import Extension, setup

cflags = []
if not hasattr(sys, 'getwindowsversion'):
    cflags.append('-fvisibility=hidden')

sources = glob.glob('src/*.c') + glob.glob('src/duktape/*.c')

setup(
    name='dukpy',
    version='0.2',
    author='Kovid Goyal',
    author_email='kovid@kovidgoyal.net',
    description='JavaScript runtime environment for Python',
    url='https://github.com/kovidgoyal/dukpy',
    ext_modules=[
        Extension('dukpy', sources=sources, extra_compile_args=cflags),
    ],
    test_suite='tests',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: JavaScript',
    ], )

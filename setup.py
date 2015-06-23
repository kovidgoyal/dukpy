import os
from setuptools import setup, Extension


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='dukpy',
    version='0.1',
    author='Petri Lehtinen',
    author_email='petri@digip.org',
    description='JavaScript runtime environment for Python',
    url='https://github.com/akheron/dukpy',
    long_description=read('README.md'),
    ext_modules=[
        Extension('dukpy', sources=[
            'src/context.c',
            'src/conversions.c',
            'src/proxy.c',
            'src/module.c',
            'src/duktape/duktape.c',
        ]),
    ],
    test_suite='tests',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: JavaScript',
    ],
)

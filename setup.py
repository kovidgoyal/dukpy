from setuptools import setup, Extension


setup(
    name='dukpy',
    version='0.2',
    author='Kovid Goyal',
    author_email='kovid@kovidgoyal.net',
    description='JavaScript runtime environment for Python',
    url='https://github.com/kovidgoyal/dukpy',
    ext_modules=[
        Extension('dukpy', sources=[
            'src/errors.c',
            'src/context.c',
            'src/conversions.c',
            'src/proxy.c',
            'src/module.c',
            'src/duktape/duktape.c',
        ]),
    ],
    test_suite='tests',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: JavaScript',
    ],
)

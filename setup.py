#!/usr/bin/env python

import sys

from distutils.core import setup

if any(arg.startswith('bdist') for arg in sys.argv):
    import setuptools

version_ns = {}
with open('findjava.py') as f:
    for line in f:
        if line.startswith('__version__'):
            exec(line, version_ns)
            break

setup(
    name='findjava',
    version=version_ns['__version__'],
    py_modules=['findjava'],
    description="Find java to add it to the environment.",
    long_description="""
        Provides findjava.init() to add JAVA_HOME environment variable
    """,
    license="MIT",
    author="AbdealiJK",
    author_email="abdealikothari@gmail.com",
    url="https://github.com/AbdealiJK/findjava",
)

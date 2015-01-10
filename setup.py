#!/usr/bin/env python

# Copyright (c) 2012, Vadim "qnub" Lopatyuk
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import sys
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from django_boto import __version__

if sys.version_info <= (2, 4):
    error = "ERROR: boto requires Python Version 2.5 or above...exiting."
    print >> sys.stderr, error
    sys.exit(1)

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-boto',
    version=__version__,
    description='Wrapper of boto package for django',
    long_description=open("README.md").read(),
    author='Vadim Lopatyuk',
    author_email='qnub.ru@gmail.com',
    url='https://github.com/qnub/django-boto/',
    packages=["django_boto", "django_boto.s3"],
    install_requires=[
        "django>=1.3",
        "boto>=2.3.0",
        "python-dateutil>=2.4.0",
    ],
    license="MIT",
    platforms="Posix; MacOS X; Windows",
    classifiers=["Development Status :: 4 - Beta",
                 "Intended Audience :: Developers",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent",
                 "Topic :: Internet",
                 "Programming Language :: Python :: 2",
                 "Programming Language :: Python :: 2.5",
                 "Programming Language :: Python :: 2.6",
                 "Programming Language :: Python :: 2.7",
                 "Framework :: Django", ],
)

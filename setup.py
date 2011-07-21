#!/usr/bin/env python
from distutils.core import setup
import os


# meola settings
PACKAGE_NAME = 'PythonGit'
DESCRIPTION = 'Python interface to Git.'
LICENSE = 'Unlicence'
URL = 'http://github.com/adamnfish/PythonGit'
AUTHOR = "adamnfish"
AUTHOR_EMAIL = "adamnfish@gmail.com"

# VERSION
# attempt to read the version tuple out of the package to dynamically
# get the version.
try:
    # Dynamically calculate the version based on the VERSION-tuple
    execfile('meola/version.py')
    VERSION = ".".join([str(v) for v in VERSION])
except IOError:
    VERSION = ""

setup(
    packages = ['git'],
    name = PACKAGE_NAME,
    description = DESCRIPTION,
    version = VERSION,
    license = LICENSE,
    url = URL,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    classifiers = [
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
)

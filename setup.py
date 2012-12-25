#!/usr/bin/env python

import os.path
from distutils.core import setup

README = open(os.path.join(os.path.dirname(__file__), "README.rst")).read()

CLASSIFIERS = [
	"Development Status :: 2 - Pre-Alpha",
	"Intended Audience :: Developers",
	"License :: OSI Approved :: MIT License",
	"Programming Language :: Python",
	"Topic :: Software Development :: Libraries",
]

import omdb
VERSION = omdb.__version__

setup(
	name = "python-omdb",
	py_modules = ["omdb"],
	author = "Jerome Leclanche",
	author_email = "jerome.leclanche+omdb@gmail.com",
	classifiers = CLASSIFIERS,
	description = "Python bindings for the omdbapi.com service",
	download_url = "http://github.com/Adys/python-omdb/tarball/master",
	long_description = README,
	url = "http://github.com/Adys/python-omdb",
	version = VERSION,
)

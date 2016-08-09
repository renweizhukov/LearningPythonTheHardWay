#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Project for ex48',
    'author': 'Wei Ren',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'renwei@smartconn.cc',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'ex48'
}

setup(**config)

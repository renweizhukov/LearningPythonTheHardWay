#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My First Project',
    'author': 'Wei Ren',
    'url': 'https://github.com/renweizhukov/LearningPythonTheHardWay',
    'download_url': 'TBD',
    'author_email': 'renwei@smartconn.cc',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['myfirstproject'],
    'scripts': [],
    'name': 'myfirstproject'
}

setup(**config)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import *
import myfirstproject

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"

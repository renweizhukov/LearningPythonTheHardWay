#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import *
from ex48 import parser

def test_subverbobj():
    sentence = parser.parse_sentence([('noun', 'bear'), ('verb', 'eat'), ('noun', 'honey')])
    assert_equal(sentence.subject, 'bear')
    assert_equal(sentence.verb, 'eat')
    assert_equal(sentence.object, 'honey')

def test_verbobj():
    sentence = parser.parse_sentence([('verb', 'eat'), ('noun', 'honey')])
    assert_equal(sentence.subject, 'player')
    assert_equal(sentence.verb, 'eat')
    assert_equal(sentence.object, 'honey')

def test_stopsubverbobj():
    sentence = parser.parse_sentence([('stop', 'the'), ('noun', 'bear'), ('verb', 'eat'), ('noun', 'honey')])
    assert_equal(sentence.subject, 'bear')
    assert_equal(sentence.verb, 'eat')
    assert_equal(sentence.object, 'honey')

def test_verb(): 
    assert_raises(parser.ParserError, parser.parse_sentence, [('verb', 'eat')])

# -*- coding: utf-8 -*-

from nose.tools import *
from ex49 import parser

a = 'go north'
b = 'kill the princess'
c = 'eat the bear'
d = 'open the door'
def test_subjects():
    assert_equal(parser.parse_sentence(a).subject, 'player')
    assert_equal(parser.parse_sentence(b).subject, 'player')
    assert_equal(parser.parse_sentence(c).subject, 'player')
    # assert_equal(parser.parse_sentence(d).subject, 'player')
    assert_raises(parser.ParserError, parser.parse_sentence, d)

def test_verb():
    assert_equal(parser.parse_sentence(a).verb, 'go')
    assert_equal(parser.parse_sentence(b).verb, 'kill')
    assert_equal(parser.parse_sentence(c).verb, 'eat')
    assert_raises(parser.ParserError, parser.parse_sentence, d)
def test_objects():
    assert_equal(parser.parse_sentence(a).object, 'north')
    assert_equal(parser.parse_sentence(b).object, 'princess')
    assert_equal(parser.parse_sentence(c).object, 'bear')
    assert_raises(parser.ParserError, parser.parse_sentence, d)

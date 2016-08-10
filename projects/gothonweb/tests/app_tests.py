#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_index():
    # check that we get a 303 on the / URL
    resp = app.request("/")
    assert_response(resp, status="303")

    # test our first GET request to /game
    resp = app.request("/game")
    assert_response(resp)

    # test that we will die if we choose the wrong direction
    data = {'action': 'Shoot!'}
    resp = app.request("/game", method="POST", data=data)
    assert_response(resp, status="303")
    resp = app.request("/game")
    assert_response(resp, contains="You Died!")

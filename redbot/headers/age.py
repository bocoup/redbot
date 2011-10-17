#!/usr/bin/env python

__author__ = "Mark Nottingham <mnot@mnot.net>"
__copyright__ = """\
Copyright (c) 2008-2011 Mark Nottingham

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from cgi import escape as e

import redbot.speak as rs
import redbot.headers as rh
import redbot.http_syntax as syntax


@rh.GenericHeaderSyntax
@rh.SingleFieldValue
@rh.CheckFieldSyntax(syntax.DIGITS, rh.rfc2616 % "sec-14.6")
def parse(name, values, red):
    try:
        age = int(values[-1])
    except ValueError:
        red.set_message(name, rs.AGE_NOT_INT)
        return None
    if age < 0:
        red.set_message(name, rs.AGE_NEGATIVE)
        return None
    return age
    
    
class AgeTest(rh.HeaderTest):
    name = 'Age'
    inputs = ['10']
    expected_out = (10)
    expected_err = []

class MultipleAgeTest(rh.HeaderTest):
    name = 'Age'
    inputs = ['20', '10']
    expected_out = (10)
    expected_err = [rs.SINGLE_HEADER_REPEAT]

class CharAgeTest(rh.HeaderTest):
    name = 'Age'
    inputs = ['foo']
    expected_out = (None)
    expected_err = [rs.BAD_SYNTAX]

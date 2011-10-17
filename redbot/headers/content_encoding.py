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
@rh.CheckFieldSyntax(syntax.TOKEN, rh.rfc2616 % "sec-14.11")
def parse(name, values, red):
    values = [v.lower() for v in values]
    for value in values:
        # check to see if there are any non-gzip encodings, because
        # that's the only one we ask for.
        if value != 'gzip':
            red.set_message(name, rs.ENCODING_UNWANTED, encoding=e(value))
            break
    return values
    
class ContentEncodingTest(rh.HeaderTest):
    name = 'Content-Encoding'
    inputs = ['gzip']
    expected_out = ['gzip']
    expected_err = []

class ContentEncodingCaseTest(rh.HeaderTest):
    name = 'Content-Encoding'
    inputs = ['GZip']
    expected_out = ['gzip']
    expected_err = []

class UnwantedContentEncodingTest(rh.HeaderTest):
    name = 'Content-Encoding'
    inputs = ['gzip', 'foo']
    expected_out = ['gzip', 'foo']
    expected_err = [rs.ENCODING_UNWANTED]


#!/usr/bin/env python

###
# Copyright (c) 2002, Jeremiah Fincher
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
###

from test import *

import Alias


class FunctionsTest(unittest.TestCase):
    def testFindString(self):
        L = []
        self.assertEqual(0, Alias.findString('foo', L))
        L.append('bar')
        self.assertEqual(0, Alias.findString('foo', L))
        L.append('foo')
        self.assertEqual(1, Alias.findString('foo', L))
        L.append([])
        self.assertEqual(1, Alias.findString('foo', L))
        L.append(['bar'])
        self.assertEqual(1, Alias.findString('foo', L))
        L.append(['foo'])
        self.assertEqual(2, Alias.findString('foo', L))
        L.append(['bar', 'foo'])
        self.assertEqual(3, Alias.findString('foo', L))
        L.append(['foo', 'foo', 'foo'])
        self.assertEqual(6, Alias.findString('foo', L))

    def testFindDollars(self):
        L = []
        self.assertEqual([], Alias.findDollars(L))
        L.append('foo')
        self.assertEqual([], Alias.findDollars(L))
        L.append('$1')
        self.assertEqual([([1], '$1')], Alias.findDollars(L))
        L.append('$1 foo bar')
        self.assertEqual([([1], '$1')], Alias.findDollars(L))
        L.append('$2')
        self.assertEqual([([1], '$1'), ([3], '$2')], Alias.findDollars(L))
        L.append(['foo'])
        self.assertEqual([([1], '$1'), ([3], '$2')], Alias.findDollars(L))
        L.append(['foo', 'bar', '$1'])
        self.assertEqual([([1], '$1'), ([3], '$2'), ([5, 2], '$1')],
                         Alias.findDollars(L))
        L.append([[[['$3']]]])

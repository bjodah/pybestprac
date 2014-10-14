#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from future.builtins import *

import argh

from pybestprac import euclidean_norm


def calc_norms(data="1,2,3;4,5;7", silent=False):
    def _splt(s, delim):
        "Slightly modified version of str.split"
        l = s.split(delim)
        if l == ['']:
            return []
        return l

    result = euclidean_norm(map(int, _splt(x, ',')) for x in _splt(data, ';'))
    if not silent:
        return result

if __name__ == '__main__':
    argh.dispatch_command(calc_norms)

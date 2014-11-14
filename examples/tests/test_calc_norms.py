# -*- coding: utf-8 -*-

import os
import subprocess

import pytest

from calc_norms import calc_norms
from pybestprac.util.testing import assert_allclose, veryslow


def test_calc_norms():
    assert_allclose(calc_norms('3,4;4,3'), [5, 5])
    assert_allclose(calc_norms('1,1,1,1;2,2,2,2;3,3,3,3'), [2, 4, 6])

    with pytest.raises(RuntimeError):
        calc_norms('1,1,1,1;;2,2')


# This test isn't "veryslow" but for demonstration:
@veryslow
def test_cmdline():
    p = subprocess.Popen(['python', 'calc_norms.py', '-d 3,3;4,4', '--silent'],
                         cwd=os.path.dirname(__file__), stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    exit_status = p.wait()
    assert exit_status == os.EX_OK

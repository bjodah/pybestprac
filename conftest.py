# -*- coding: utf-8 -*-

# This file is used by py.test and defines two markers:
# - slow (>~ 50 ms)
# - veryslow (>~ 1 s)
# mark tests by importing the respecitve markers:
#
# >>> from .util.testing import veryslow
#
# By using these markers the tests run by e.g. the pre-commit hook
# can e.g. be chosen to be only the quick tests and leave the heavy
# liften to the CI servers.


from __future__ import (
    print_function, division, absolute_import, unicode_literals
)

import pytest

collect_ignore = ['setup.py', 'docs/conf.py', 'conda-recipe/run_test.py']


def pytest_addoption(parser):
    parser.addoption("--slow", dest="runslow", action="store_true",
                     help="allow slow tests to run")
    parser.addoption("--veryslow", dest="runveryslow", action="store_true",
                     help="allow very slow tests to run")


def pytest_configure(config):
    # register an additional marker
    config.addinivalue_line("markers", "slow: slow test")
    config.addinivalue_line("markers", "veryslow: very slow test")


def pytest_runtest_setup(item):
    if not isinstance(item, pytest.Function):
        return
    if not item.config.getvalue("runslow") and hasattr(item.obj, 'slow'):
        pytest.skip("slow test: pass --slow to run")
    if not item.config.getvalue("runveryslow") and hasattr(
            item.obj, 'veryslow'):
        pytest.skip("very slow test: pass --veryslow to run")

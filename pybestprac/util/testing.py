import pytest

slow = pytest.mark.slow  # call time >~ 100 ms
veryslow = pytest.mark.veryslow  # call time > a few seconds


def allclose(a, b, rtol=1e-8, atol=1e-8):
    if len(a) != len(b):
        raise ValueError("Incomaptible lengths")
    for idx, (x, y) in enumerate(zip(a, b)):
        if abs(x-y) > atol+rtol*abs(y):
            return idx
    return -1


def assert_allclose(*args, **kwargs):
    idx = allclose(*args, **kwargs)
    if idx != -1:
        raise AssertionError("Items at index %d differ." % idx)

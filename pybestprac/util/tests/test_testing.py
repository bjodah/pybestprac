import pytest

from pybestprac.util.testing import allclose, assert_allclose

a, b = [1.0, 1000.0], [1.0+5e-9, 1000.0+5e-7]


def test_allclose():
    assert allclose(a, b, rtol=1e-09, atol=1e-8) == -1
    assert allclose(a, b, rtol=1e-09, atol=1e-9) == 0
    assert allclose(a, b, rtol=1e-10, atol=1e-8) == 1


def test_assert_allclose():
    with pytest.raises(AssertionError):
        assert_allclose(a, b, rtol=1e-10, atol=1e-8)

import pytest

from pybestprac.norms import euclidean_norm, taxicab_norm
from pybestprac.util.testing import assert_allclose, slow


def test_euclidean_norm():
    assert_allclose(
        euclidean_norm([(1, 1, 1, 1), (2, 2, 2, 2), (3, 3, 3, 3)]),
        [2, 4, 6]
    )
    euclidean_norm([(), ()], allow_empty=True)
    with pytest.raises(RuntimeError):
        euclidean_norm([(), ()])

# This test isn't "slow" but for demonstration:


@slow
def test_taxicab_norm():
    assert_allclose(
        taxicab_norm([(1, 1, 1, 1), (2, 2, 2, 2), (3, 3, 3, 3)]),
        [4, 8, 12]
    )
    taxicab_norm([(), ()], allow_empty=True)
    with pytest.raises(TypeError):
        taxicab_norm([(), ()])

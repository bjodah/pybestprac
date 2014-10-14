"""
here you will find all norms implemented.

Example:

>>> from pybestprac.norms import taxicab_norm
>>> taxicab_norm([(1,1),(2,2)])
[2.0, 4.0]

"""

from operator import add

from ._euclid import euclidean_norm as _euclidean_norm


def euclidean_norm(vectors, allow_empty=False):
    """
    Calculates the euclidean norms of vectors of integers through the formula:

    .. math::

        \|\boldsymbol{x}\| := \sqrt{x_1^2 + \cdots + x_n^2}


    Parameters
    ----------
    vectors: iterable of iterables containing integers
        The vectors to compute the norm for. If the vectors does not contain
        integers, the values will be rounded prior to evaluation.
    allow_empty: bool
        Allow length 0 iterables in vectors by replacing them with
        a zero (default: False).

    Examples
    --------
    >>> euclidean_norm([(1, 1, 1, 1), (2, 2, 2, 2), (3, 3, 3, 3)])
    [2.0, 4.0, 6.0]

    Returns
    -------
    List of norms (floating point numbers)

    Raises
    ------
    RuntimeError
        If ``allow_empty`` not set to True and an empty iterable is
        passed in vectors.

    Notes
    -----
    .. versionadded:: 0.0.1

    The core algorithm is implemented in fastest possible way (for single
    node computations) using OpenMP reduction directive but the wrappers
    may slow things down. If optimal performance is critical: consider
    calling the Fortran subroutine directly.

    """
    if allow_empty:
        _vectors = []
        for v in vectors:
            if len(v) > 0:
                _vectors.append(v)
            else:
                _vectors.append((0,))
        vectors = _vectors
    return _euclidean_norm(vectors)


def taxicab_norm(vectors):
    # TODO: write a proper docstring
    return [reduce(add, map(abs, v)) for v in vectors]

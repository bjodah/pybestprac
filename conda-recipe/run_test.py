import pybestprac
# note that this is not the full test suite.
assert abs(pybestprac.euclidean_norm([(1,)])[0] - 1) < 1e-15

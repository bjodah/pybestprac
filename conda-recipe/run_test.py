import sys
import traceback

print("Importing pybestprac...")
try:
    import pybestprac
except ImportError:
    print("Importing pybestprac failed")
    traceback.print_exc(file=sys.stdout)

print("Running tests...")
try:
    # note that this is not the full test suite.
    assert abs(pybestprac.euclidean_norm([(1,)])[0] - 1) < 1e-15
except AssertionError:
    print("Assertion failed:")
    traceback.print_exc(file=sys.stdout)
else:
    print("Other error:")
    traceback.print_exc(file=sys.stdout)

import sys
import traceback

print("Importing pybestprac...")
try:
    import pybestprac
except ImportError as e:
    print("Importing pybestprac failed")
    print(e)
    traceback.print_exc(file=sys.stdout)
    raise e

print("Running tests...")
try:
    # note that this is not the full test suite.
    assert abs(pybestprac.euclidean_norm([(1,)])[0] - 1) < 1e-15
except AssertionError as e:
    print("Assertion failed:")
    print(e)
    traceback.print_exc(file=sys.stdout)
    raise e
except Exception as e:
    print("Other error:")
    traceback.print_exc(file=sys.stdout)
    raise e

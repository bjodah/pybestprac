import os
import sys
import traceback
from subprocess import Popen

pkg_name = 'pybestprac'

print("Importing %s..." % pkg_name)
try:
    import pybestprac
except ImportError as e:
    print("Importing %s failed" % pkg_name)
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

# Run the full test suite
p = Popen(['py.test', '--pyargs', pkg_name]) # need conftest.py for: '--slow', '--veryslow'
assert p.wait() == os.EX_OK

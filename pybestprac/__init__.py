"""
pybestprac is a humble attempt of creating
a demo package of some best practices for Python packages with
native extension modules. It shows how one can use unit tests,
continuous integration services (like Travis-CI) and a "conda recipe"
in a way that enables cooperative development on github.
"""

from .release import __version__
__url__ = "https://github.com/bjodah/pybestprac"

from .norms import euclidean_norm, taxicab_norm

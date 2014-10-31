Overview
========


Version control
---------------
By using a (distributed) version control system (DVCS) you get several
important benefits:

- Reproducibility (you know exactly what version is being used)
- History (if a change later turns out to have made things worse it may be undone)
- Collaboration (several people can work independently and their versions merged later on)

you should basically choose between two modern systems:

- git (read more at `http://git-scm.com/`_)
- hg (mercury, read more at `http://hg-scm.com/`_)

personally I use the former.

To fully benefit from your DVCS you can put your code repository
online. There are several service providers, I would recommend:

- github.com
- bitbucket.org

personally I use the former.

Dependencies
------------
In order not having to reinvent the wheel perpetually it is
common practice to let your package rely on other packages.

``pybestprac`` uses the following packages:

- `pytest <https://pypi.python.org/pypi/pytest>`_ - simple powerful testing with Python
- `future <https://pypi.python.org/pypi/future>`_ - Clean single-source support for Python 3 and 2
- `argh <https://pypi.python.org/pypi/argh>`_ - An unobtrusive argparse wrapper with natural syntax

to manage the dependencies you may rely on Python (since v3.4 built-in) ``pip`` tool or
an external package manager such as ``conda``.

These packages (and eventually also including your own) are usually hosted at:

-`PyPI <https://pypi.python.org>`_
-`Binstar <https://binstar.org>`_

where the latter hosts ``conda`` packages and also allow pre-compiled binary packages
(this is a HUGE plus when your build process gets involved).


Interfacing C/C++/Fortran
-------------------------

See `fortran90.org`_ for best practices for Fortran.

- `cython <https://pypi.python.org/pypi/cython>`_ - 

Host python wheels (binary distribution) for several platforms:

- `binstar <https://binstar.org>`_ - provided for free by Continuum Analytics.

Documentation
-------------

- sphinx - RestructuredText
- numpydoc - docstrings
- sphinx_rtd_theme - ReadTheDocs theme (unable to build the docs at readthedocs.org without extensive mocking of
  extension module). Hence the actual docs are hosted in the ``gh-pages`` branch of the repo.

Debugging
---------

- pudb
- pdb


Editor
------
Even though it does not quite fall under best practices a word on editors may
still be good. Saying what editor is the best is like saying car brand X is 
better than car brand Y, but some popular choices are:

- Emacs
- Vim
- PyCharm

where I personally use the former. For some python specific tips for emacs
you may have a look at https://github.com/jhamrick/emacs and for a beginners
guide on Emacs you may want to look at http://www.jesshamrick.com/2012/09/10/absolute-beginners-guide-to-emacs/.


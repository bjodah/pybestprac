==========
pybestprac
==========

.. image:: https://travis-ci.org/bjodah/pybestprac.png?branch=master
   :target: https://travis-ci.org/bjodah/pybestprac
   :alt: Build status
.. image:: https://readthedocs.org/projects/pybestprac/badge/?version=latest
   :target: http://pybestprac.readthedocs.org/
   :alt: Documentation Status
.. image:: https://coveralls.io/repos/bjodah/pybestprac/badge.png?branch=master
   :target: https://coveralls.io/r/bjodah/pybestprac?branch=master
   :alt: Test coverage

pybestprac tries to be an example of showing "best practices" for developing
an open source python package using github and external serives.

It is made quite intricate (Fortran 90 implementation called from C++
which in turn is wrapped using Cython to allow use from Python). 

Documentation
=============

the documentation is hostad at

- http://bjodah.github.io/pybestprac/docs/

Installation
============
.. install-start

Below you will find instructions for installation. You may also
look in ``scripts/`` folder for automated install scripts used
in continuous integration.

Prerequisites
-------------

- C++ compiler with C++11 support (e.g. GCC >= 4.8)
- Fortran compiler with ISO_C_BINDING support (Fortran 2003 standard) (e.g. gfortran)
- Python (2.7 or >=3.4)
    
In addition to python, the following python packages are required
(versions indicate what is tested):

- argh>=0.25.0
- numpy>=1.9.0
- cython>=0.21.0
- future>=0.14.1
- pycompilation>=0.3.6
- pycodeexport>=0.0.5

For rendering the documentation you also need:

- `Sphinx <http://sphinx-doc.org/>`_
- `numpydoc <https://pypi.python.org/pypi/numpydoc>`_
- `sphinx_rtd_theme <https://pypi.python.org/pypi/sphinx_rtd_theme>`_

Building and installing
-----------------------
Once non-python prerequisites are in installed, you may procede e.g. as:

::

    $ git clone https://bitbucket.org/bjodah/pybestprac.git
    $ cd pybestprac
    $ pip install --user --upgrade -r requirements.txt
    $ python setup.py install --user
    $ py.test


the above procedure works on Ubuntu 14.04 for example. See the `Python
docs <https://docs.python.org/2/install/index.html#install-index>`_
for more information on how to install e.g. system wide. 


Tests
-----
Run ``py.test``, possibly with explicit ``PYTHONPATH`` (e.g. if ``build_ext --inplace`` was used)

::

    $ PYTHONPATH=`pwd`:$PYTHONPATH py.test

All tests should pass (or xfail). If they don't, please `file an issue
<https://github.com/bjodah/pybestprac/issues>`_. 

.. install-end


Continuous integration
======================

.. ci-start

In order to minimize the risk of (re)introducing bugs into the code
base, it is continuously built on two CI services:

- `travis-ci.org <https://travis-ci.org/bjodah/pybestprac>`_

.. image:: https://travis-ci.org/bjodah/pybestprac.png?branch=master
   :target: https://travis-ci.org/bjodah/pybestprac

above you can find the build status shield for travis-ci (Py 2.7, Py
3.4, runs coveralls, builds docs and pushes them to the gh-pages branch).

Passing builds of the master branch are published on binstar and have
their docs built and deployed. 

.. ci-end


License
=======
Open Source. Released under the very permissive "simplified
(2-clause) BSD license". See ``LICENSE.txt`` for further details.

Author
======
Björn Dahlgren, contact:
 - gmail adress: bjodah
 - kth.se adress: bda

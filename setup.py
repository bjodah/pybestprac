#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This setup.py is to compile and link a
# Fortran 90/C++11/Cython extension module.
# To do this it uses "pycompilation"

import os
import sys

from distutils.core import setup, Command


pkg_name = 'pybestprac'

# read __version__ and __doc__ attributes:
exec(open('pybestprac/release.py').read())
try:
    major, minor, micro = map(int, __version__.split('.'))
except ValueError:
    IS_RELEASE=False
else:
    IS_RELEASE=True

with open('pybestprac/__init__.py') as f:
    long_description = f.read().split('"""')[1]

CONDA_BUILD = os.environ.get('CONDA_BUILD', '0') == '1'
ON_RTD = os.environ.get('READTHEDOCS', None) == 'True'
ON_DRONE = os.environ.get('DRONE', 'false') == 'true'
ON_TRAVIS = os.environ.get('TRAVIS', 'flse') == 'true'

if CONDA_BUILD:
    open('__conda_version__.txt', 'w').write(__version__)

if ON_DRONE or ON_TRAVIS:
    # 'fast' implies march=native which fails on current version of docker.
    options = ['pic', 'warn']
else:
    options = ['pic', 'warn', 'fast']

IDEMPOTENT_INVOCATION = False
if len(sys.argv) > 1:
    if '--help' in sys.argv[1:] or sys.argv[1] in (
            '--help-commands', 'egg_info', 'clean', '--version'):
        IDEMPOTENT_INVOCATION = True
elif len(sys.argv) == 1:
    IDEMPOTENT_INVOCATION = True

cmdclass = {}
if ON_RTD or IDEMPOTENT_INVOCATION:
    # Enbale pip to import setup.py before all requirements are installed
    ext_modules = []
else:
    sources = [
        'src/euclid_enorm.f90',
        'src/euclid.cpp',
        'pybestprac/_euclid.pyx',
    ]

    # The rest of this `else` clause relies on pycodeexport/pycompilation
    from pycompilation.dist import pc_build_ext, PCExtension
    cmdclass['build_ext'] = pc_build_ext

    ext_modules = [
        PCExtension(
            "pybestprac._euclid",
            sources=sources,
            pycompilation_compile_kwargs={
                'per_file_kwargs': {
                    'src/euclid.cpp': {
                        'std': 'c++11',
                        'options': options,
                    },
                },
                'options': options + ['openmp'],
            },
            pycompilation_link_kwargs={
                'options': ['openmp'],
                'std': 'c++11',
            },
            include_dirs=['src/'],
            logger=True,
        )
    ]

modules = [
    'pybestprac.util'
]

tests = [
    'pybestprac.tests',
    'pybestprac.util.tests',
]


classifiers = [
    "Development Status :: 3 - Alpha",
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Mathematics',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
]

setup_kwargs = {
    'name': pkg_name,
    'version': __version__,
    'description': ('Demo package for "best practices" python'
                    ' extension module github repo'),
    'long_description': long_description,
    'author': 'Björn Dahlgren',
    'author_email': 'bjodah@DELETEMEgmail.com',
    'license': 'BSD',
    'keywords': ("demo",),
    'url': 'https://github.com/bjodah/' + pkg_name,
    'packages': [pkg_name] + modules + tests,
    'cmdclass': cmdclass,
    'ext_modules': ext_modules,
    'classifiers': classifiers,
}

if IS_RELEASE:
    tmplt = 'https://github.com/bjodah/%s/archive/v%s.tar.gz'
    setup_kwargs['download_url'] = tmplt % (pkg_name, __version__)

if __name__ == '__main__':
    setup(**setup_kwargs)

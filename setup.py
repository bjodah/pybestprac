#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This setup.py is to compile and link a
# Fortran 90/C++11/Cython extension module.
# To do this it uses "pycodeexport"

import os
import sys

from distutils.core import setup, Command


pkg_name = 'pybestprac'
__version__ = '0.0.1'

IS_RELEASE = os.environ.get("IS_RELEASE", '0') == '1'
CONDA_BUILD = os.environ.get('CONDA_BUILD', '0') == '1'
ON_RTD = os.environ.get('READTHEDOCS', None) == 'True'
ON_DRONE = os.environ.get('DRONE', 'false') == 'true'
ON_TRAVIS = os.environ.get('TRAVIS', 'flse') == 'true'

if not IS_RELEASE:
    __version__ += '.dev'  # PEP386

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
    from pycodeexport.dist import pce_build_ext, PCEExtension
    cmdclass['build_ext'] = pce_build_ext

    ext_modules = [
        PCEExtension(
            "pybestprac._euclid",
            sources=sources,
            pycompilation_compile_kwargs={
                'per_file_kwargs': {
                    'src/euclid.cpp': {
                        'std': 'c++11',
                        # 'fast' doesn't work on drone.io
                        'options': options + ['openmp'],
                    },
                },
                'options': options,
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

long_description = '''pybestprac is a humble attempt of creating
a demo package of some best practices for Python packages with
native extension modules. It shows how one can use unit tests,
continuous integration and a "conda recipe" in a way that enables
cooperative development on github.'''

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
    'packages': [pkg_name] + modules,
    'cmdclass': cmdclass,
    'ext_modules': ext_modules,
    'classifiers': classifiers,
}

if IS_RELEASE:
    tmplt = 'https://github.com/bjodah/%s/archive/v%s.tar.gz'
    setup_kwargs['download_url'] = tmplt % (pkg_name, __version__)

if __name__ == '__main__':
    setup(**setup_kwargs)

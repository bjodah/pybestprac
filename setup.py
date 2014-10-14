#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This setup.py is to compile and link a
# Fortran 90/C++11/Cython extension module.
# To do this it uses "pycodeexport"

import os
import sys

from distutils.core import setup, Command

name_ = 'pybestprac'
version_ = '0.0.1'
cmdclass_ = {}

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
on_drone = os.environ.get('DRONE', 'false') == 'true'
on_travis = os.environ.get('TRAVIS', 'flse') == 'true'

if on_drone or on_travis:
    # 'fast' implies march=native which fails on current version of docker.
    options = ['pic', 'warn']
else:
    options = ['pic', 'warn', 'fast']


if on_rtd or '--help' in sys.argv[1:] or sys.argv[1] in (
        '--help-commands', 'egg_info', 'clean', '--version'):
    # Enbale pip to import setup.py before all requirements are installed
    ext_modules_ = []
else:
    from pycodeexport.dist import pce_build_ext, PCEExtension
    cmdclass_['build_ext'] = pce_build_ext
    sources = [
        'src/euclid_enorm.f90',
        'src/euclid.cpp',
        'pybestprac/_euclid.pyx',
    ]

    ext_modules_ = [
        PCEExtension(
            "pybestprac._euclid",
            sources=sources,
            pycompilation_compile_kwargs={
                'per_file_kwargs': {
                    'src/euclid.cpp': {
                        'std': 'c++0x',
                        # 'fast' doesn't work on drone.io
                        'options': options + ['openmp'],
                    },
                },
                'options': options,
            },
            pycompilation_link_kwargs={
                'options': ['openmp'],
                'std': 'c++0x',
            },
            include_dirs=['src/'],
            logger=True,
        )
    ]

setup(
    name=name_,
    version=version_,
    description=('Demo package for "best practices" python'
                 ' extension module github repo'),
    author='Björn Dahlgren',
    author_email='bjodah@DELETEMEgmail.com',
    url='https://github.com/bjodah/' + name_,
    packages=[name_, name_ + '.util'],
    cmdclass=cmdclass_,
    ext_modules=ext_modules_,
)

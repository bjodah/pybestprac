#!/bin/bash -x -e

PY_VERSION=$1
ENV_NAME=$2

conda create --quiet -n $ENV_NAME python=${PY_VERSION} cython=0.21 pip sphinx pytest numpydoc future
source activate $ENV_NAME
pip install --quiet pycompilation pycodeexport argh pytest-pep8 pytest-cov python-coveralls sphinx_rtd_theme https://github.com/sympy/sympy/archive/master.zip

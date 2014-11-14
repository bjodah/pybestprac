#!/bin/bash
# this script assumes conda is in $PATH

export PYTHON_VERSION=$1
export CONDA_PY=$2
export ENV_NAME=$3
export CONDA_PATH=$(conda info --system | grep sys.prefix | cut -d: -f2 | sed -e 's/^ *//')
source ./scripts/setup_conda_testenv.sh $PYTHON_VERSION $ENV_NAME
conda info
python --version
python setup.py --version
export DISTUTILS_DEBUG=1
conda build conda-recipe
conda install --quiet pybestprac --use-local
LIBRARY_PATH=$CONDA_PATH/envs/$ENV_NAME/lib:$LIBRARY_PATH ./scripts/run_tests.sh

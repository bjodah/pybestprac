#!/bin/bash
export PYTHON_VERSION=$1
export CONDA_PY=$2
export ENV_NAME=$3

source ./scripts/setup_conda_testenv.sh $PYTHON_VERSION $ENV_NAME
conda info
python --version
python setup.py --version
export DISTUTILS_DEBUG=1
conda build conda-recipe
conda install --quiet pybestprac --use-local
LIBRARY_PATH=$MINICONDA_PATH/envs/$ENV_NAME/lib:$LIBRARY_PATH TEST_INSTALL=1 bash -x -e ./scripts/run_tests.sh

#!/bin/bash
# Usage, e.g.:
# ./scripts/run_tests.sh --ignore examples/
if python -c "import pybestprac"; then
    python setup.py build_ext --inplace
fi
if [[ $TEST_INSTALL != "1" ]]; then
    # Extract absolute path of script, from:
    # http://unix.stackexchange.com/a/9546
    absolute_repo_path_x="$(readlink -fn -- "$(dirname $0)/.."; echo x)"
    absolute_repo_path="${absolute_repo_path_x%x}"
    export PYTHONPATH=$absolute_repo_path:$PYTHONPATH
fi
py.test --slow --veryslow --pep8 --doctest-modules --cov pybestprac --cov-report html --ignore setup.py --ignore scripts/move-conda-package.py $@

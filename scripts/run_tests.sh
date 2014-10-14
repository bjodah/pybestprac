#!/bin/bash
# Usage, e.g.:
# ./scripts/run_tests.sh --ignore examples/

# Extract absolute path of script, from:
# http://unix.stackexchange.com/a/9546
absolute_repo_path_x="$(readlink -fn -- "$(dirname $0)/.."; echo x)"
absolute_repo_path="${absolute_repo_path_x%x}"
export PYTHONPATH=$absolute_repo_path:$PYTHONPATH
py.test --slow --veryslow --pep8 --doctest-modules --cov pybestprac --cov-report html --ignore setup.py $@

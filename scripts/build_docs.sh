#!/bin/bash

# Extract absolute path of script, from:
# http://unix.stackexchange.com/a/9546
# Note: we are assuming this script is inside a subdirectory of the repo root
absolute_repo_path_x="$(readlink -fn -- "$(dirname $0)/.."; echo x)"
absolute_repo_path="${absolute_repo_path_x%x}"
export PYTHONPATH=$absolute_repo_path:$absolute_repo_path/examples:$PYTHONPATH

# You use sphinx-apidoc to generate a base structure
#sphinx-apidoc --output-dir docs/ --full --doc-author="Bjoern Dahlgren" --doc-version "v0.0.1" pybestprac

cd docs/
make $@ html >_build.log
cp _build.log _build/html/

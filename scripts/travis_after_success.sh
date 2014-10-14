#!/bin/bash
set -x # Verbose
MINICONDA_HOME=$1
ENV_NAME=$2

GH_USER=bjodah
GH_REPO=pybestprac
BINSTAR_USER=$GH_USER
WORKDIR=`pwd`
if [ "$TRAVIS_REPO_SLUG" == "${GH_USER}/${GH_REPO}" ] && [ "$TRAVIS_PULL_REQUEST" == "false" ] && [ "$TRAVIS_BRANCH" == "master" ]; then

    # Push wheel to binstar.org (for all Python versions)
    set +x # Silent
    source deactivate
    conda install conda-build
    source activate $ENV_NAME
    set -x # Verbose
    conda config --add channels http://conda.binstar.org/$BINSTAR_USER
    conda install binstar
    conda build conda-recipe/
    set +x # Silent
    echo "Uploading to binstar..."
    binstar -t ${BINSTAR_TOKEN} upload --force $MINICONDA_HOME/conda-bld/linux-64/*.tar.bz2 # bash -x workaround
    if [ "$TRAVIS_PYTHON_VERSION" == "3.4" ]; then
        # Build the documentation
        # =======================
        # Github pages
        # ------------
        echo -e "Building docs...\n"
        set -x # Verbose
        ./scripts/build_docs.sh

        # ReadTheDocs
        # -----------
        # echo -e "Triggering readthedocs webhook...\n"
        # curl -X POST http://readthedocs.org/build/$GH_REPO

        echo -e "Publishing docs...\n"
        cd $HOME
        git config --global user.email "travis@travis-ci.org"
        git config --global user.name "travis-ci"
        set +x # Silent
        echo "Cloning github repo: ${TRAVIS_REPO_SLUG}"
        git clone --quiet https://${GH_TOKEN}@github.com/${TRAVIS_REPO_SLUG} ${GH_REPO} > /dev/null
        set -x # Verbose
        cd ${GH_REPO}
        git branch -D gh-pages
        git checkout --orphan gh-pages
        git rm -rf . > /dev/null
        cp -R ${WORKDIR}/gh-pages-skeleton/* .
        cp ${WORKDIR}/gh-pages-skeleton/.* .
        cp -R ${WORKDIR}/docs/_build/html ./docs
        cp -R ${WORKDIR}/htmlcov .
        git add -f . > /dev/null
        git commit -m "Lastest docs on successful travis build $TRAVIS_BUILD_NUMBER auto-pushed to gh-pages"
        git push -f origin gh-pages
        echo -e "Published docs to gh-pages.\n"
    fi
fi

#!/bin/bash -x

if [ "$TRAVIS_REPO_SLUG" == "${GITHUB_USER}/${GITHUB_REPO}" ] && [ "$TRAVIS_PULL_REQUEST" == "false" ] && [ "$TRAVIS_BRANCH" == "master" ] && [ "$BUILD_DOCS" == "1" ]; then
    # Build the documentation
    # =======================

    # ReadTheDocs
    # -----------
    ## Currently not used since we have a compiled extension module
    ##    which would require a ton of mocking...
    ## echo -e "Triggering readthedocs webhook...\n"
    ## curl -X POST http://readthedocs.org/build/$GITHUB_REPO

    # Github pages
    # ------------
    echo -e "Building docs...\n"
    set -x # Verbose
    ./scripts/build_docs.sh

    echo -e "Publishing docs in gh-pages branch...\n"
    WORKDIR=`pwd`
    cd $HOME
    git config --global user.email "travis@travis-ci.org"
    git config --global user.name "travis-ci"
    set +x # Silent (protect token in Travis log)
    echo "Cloning github repo: ${TRAVIS_REPO_SLUG}"
    git clone --quiet https://${GH_TOKEN}@github.com/${TRAVIS_REPO_SLUG} ${GITHUB_REPO} > /dev/null
    set -x # Verbose
    cd ${GITHUB_REPO}
    git branch -D gh-pages
    git checkout --orphan gh-pages
    git rm -rf . > /dev/null
    cp -R ${WORKDIR}/gh-pages-skeleton/* .
    cp ${WORKDIR}/gh-pages-skeleton/.* .
    cp -R ${WORKDIR}/docs/_build/html ./docs
    cp -R ${WORKDIR}/htmlcov .
    git add -f . > /dev/null
    git commit -m "Lastest docs from successful travis build $TRAVIS_BUILD_NUMBER"
    git push -f origin gh-pages
fi

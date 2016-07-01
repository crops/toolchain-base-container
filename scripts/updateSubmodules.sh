#!/bin/bash

if [ ! -d .git ]; then
    echo "Must be run from top of tree"
    exit 1
fi

git submodule update --init --recursive
git submodule foreach git checkout master
git submodule foreach git pull origin master
git submodule foreach git status
git submodule foreach git log -1

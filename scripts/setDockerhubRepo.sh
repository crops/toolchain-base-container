#!/bin/bash

TRAVIS_USER=`echo $TRAVIS_REPO_SLUG | cut -d '/' -f1`
if [ "`cat ./scripts/repoMapping.txt | grep -v "#" | grep $TRAVIS_USER`" != "" ]; then
    DOCKERHUB_REPO=`cat ./scripts/repoMapping.txt | grep -v "#" | grep $TRAVIS_USER| awk '{print $2}'`
    echo "OVERRIDE, DOCKERHUB_REPO set to $DOCKERHUB_REPO"
else
    DOCKERHUB_REPO=$TRAVIS_USER
    echo "DOCKERHUB_REPO set to $DOCKERHUB_REPO"
fi
export DOCKERHUB_REPO

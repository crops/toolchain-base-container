#!/bin/bash

TRAVIS_USER=`echo $TRAVIS_REPO_SLUG | cut -d '/' -f1`
while read line; do
    echo $line
    if [ "`echo $line | grep -v "#" | awk '{print $1}' |grep $TRAVIS_USER`" != "" ]; then
	DOCKERHUB_REPO=`echo $line | grep -v "#" | grep $TRAVIS_USER| awk '{print $2}'`
	echo "OVERRIDE, DOCKERHUB_REPO set to $DOCKERHUB_REPO"
	DOCKERHUB_USER=`echo $line | grep -v "#" | grep $TRAVIS_USER| awk '{print $3}'`
	echo "OVERRIDE, DOCKERHUB_USER set to $DOCKERHUB_USER"
	exit 0
    fi
done < repoMapping.txt


DOCKERHUB_REPO=$TRAVIS_USER
DOCKERHUB_USER=$TRAVIS_USER
echo "DOCKERHUB_REPO defaulting to $DOCKERHUB_REPO"
echo "DOCKERHUB_USER defaulting to $DOCKERHUB_USER"

export DOCKERHUB_REPO
export DOCKERHUB_USER

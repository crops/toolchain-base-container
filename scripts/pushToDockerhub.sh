#!/bin/bash

# for final PR make sure to also check TRAVIS_BRANCH to make sure it is master and also
# check our slug TRAVIS_REPO_SLUG to make sure we are crops/ and not bavery/ or todor/
echo "TRAVIS_REPO_SLUG=$TRAVIS_REPO_SLUG"
echo "DOCKERHUB_REPO set to $DOCKERHUB_REPO"

# these are travis encrypted in the env section
# there is a cmplexity here
# DOCKER_EMAIL_bavery is encrypted against the bavery/crops-base-container fork
# DOCKER_EMAIL_crops is encrypted against the crops/crops-base-container origin
# we choose based on DOCKERHUB_REPO
# ${!FOO} is a bashism for an indirect reference
TMP_EMAIL="DOCKER_EMAIL_$DOCKERHUB_REPO"
TMP_PASS="DOCKER_PASS_$DOCKERHUB_REPO"

DOCKER_EMAIL=${!TMP_EMAIL}
DOCKER_PASS=${!TMP_PASS}

echo "DOCKER_EMAI=$DOCKER_EMAIL"
if [ "$DOCKER_EMAIL" = "" ]; then
    echo "DOCKER_EMAIL empty"
    exit 0
fi
if [ "$DOCKER_PASS" = "" ]; then
    echo "DOCKER_PASS empty"
    exit 0
fi

docker login -e $DOCKER_EMAIL -u $DOCKERHUB_REPO -p $DOCKER_PASS

docker images | grep ${DOCKERHUB_REPO}\/ | grep -v deps | grep -v \<none\> | awk '{print $1 ":" $2}'
if [ "$TRAVIS_PULL_REQUEST" = "false" ]; then
    # l8r also check $TRAVIS_REPO_SLUG so we only push to dockerhub on master
    for i in `docker images | grep ${DOCKERHUB_REPO}\/ | grep -v deps | grep -v \<none\> | awk '{print $1 ":" $2}'`; do
	echo Pushing $i
	docker push $i
    done
else
    print "No Pushy, TRAVIS_PULL_REQUEST=$TRAVIS_PULL_REQUEST"

fi

#!/bin/bash

IFS=$'\n';
for l in `grep '='  .travis.yml | egrep -v secure| egrep -v sudo| sed s/-//`; do
    echo "LINE<$l>";VAR=`echo $l | cut -d '=' -f1|xargs`;VAL=`echo $l | cut -d '=' -f2|xargs` ;
    echo "VAR=<$VAR> VAL=<$VAL>";
    export $VAR="$VAL";
done

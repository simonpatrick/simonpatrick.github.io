#!/bin/bash
MESSAGE=$1
echo "$MESSAGE"

git add .
git commit -m "$MESSAGE"
git push coding master
git push origin master

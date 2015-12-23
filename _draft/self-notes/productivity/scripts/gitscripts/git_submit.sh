#! /bin/bash

comment=$1

if [ ! -n "$comment" ]; then
 echo "your comment is empty"
 comment="make your changes"
fi

echo "your comments is $comment"

echo "start add changes"
git add .
echo "start commit changes"
git commit -m "$comment"

echo "start push changes"
git push

echo "Done.........."

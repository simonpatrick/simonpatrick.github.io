# /bin/bash

remote_url= $1
echo $remote_url
comments=$2
echo $comments

git remote add origin git@github.com:simonpatrick/$remote_url.git 
git add .
git commit . -m "$comments"
git push -u origin master

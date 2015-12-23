#! /bin/bash
# push gh-pages
git checkout master
git add .
git commit . -m "commit new changes"
gitbook build .
git checkout gh-pages
cp -rf _book/* . 
rm -rf _book

git add .
git commit . -m "publish new changes"
git push origin gh-pages
git checkout master

rm -rf _book
# push master
git push origin master


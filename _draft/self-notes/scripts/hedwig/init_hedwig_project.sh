#!/bin/bast init
git init
# setting email
git config user.name "testless"
git config user.email "patrickwuke@163.com"
# commit readme.md
touch README.md
echo "this is first commit for README" >>README.md
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:testless/hedwig-activiti-samples.git
git push -u origin master




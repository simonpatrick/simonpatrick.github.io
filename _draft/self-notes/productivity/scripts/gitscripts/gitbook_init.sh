#!/bin/bash
touch README.md
git init
git add README.md
git commit -m "first commit"
#git remote add origin https://github.com/simonpatrick/usinggithub.git
git remote add origin git@github.com:simonpatrick/usinggithub.git 
git push -u origin master

#git remote add origin https://github.com/simonpatrick/usinggithub.git
#git push -u origin master

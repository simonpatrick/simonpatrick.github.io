#!/bin/bash
cd ~/workspace/blog/simonpatrick.github.io/blogs
hexo generate
cp -rf public/* ../
git add .
git commit . -m "make daily changes for new blog"
git push

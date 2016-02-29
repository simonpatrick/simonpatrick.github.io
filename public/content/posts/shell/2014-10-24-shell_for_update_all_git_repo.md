---
layout: post
title: "Shell Script for updating all git repo"
modified:
categories: [shell]
excerpt:
tags: [shell]
image:
  feature:
date: 2014-10-24T10:31:11+08:00
---

# 更新一个目录下所有的git repository的shell 脚本

最近感觉需要了解一些shell脚本的使用，刚好本地上面的一个文件夹中有一些github上面的代码仓库，所以刚好学着用shell来更新各个代码仓库

```bash
#! /bin/bash

for file in ./*
do
  if test -d $file
  then  
    echo $file is directory 
    cd $file
    a=$(pwd)
    echo $a
    git pull
    cd ..
    b=$(pwd)
    echo $b
  fi

done

```



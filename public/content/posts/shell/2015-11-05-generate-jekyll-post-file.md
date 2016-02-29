---
layout: post
title: "shell来自动生成Jekyll post文件"
modified:
categories: [shell]
excerpt:
tags: [shell]
date: 2015-11-05T18:31:42
---

通过以下代码可以生成jekyll 的post 文件

```sh
#! /bin/bash

CAT=$1
TITLE=$2
echo "current location: $PWD"
echo "category: $CAT"
echo "file_name: $TITLE"

FilePrefix=`date "+%Y-%m-%d-"`
FILE_NAME="$FilePrefix$TITLE.md"
echo "target file name is $FILE_NAME"
echo "generate file......."

POST_LOCATION=_posts/$CAT
FILE_LOCATION=$POST_LOCATION/$FILE_NAME
if [ -d $POST_LOCATION ]
then
    cp template.md $FILE_LOCATION
else
    echo "create folder $CAT"
    mkdir -p $POST_LOCATION
    cp template.md $FILE_LOCATION
fi

cd $POST_LOCATION
echo "current location: $PWD"
TODAY=`date "+%Y-%m-%d-%H:%M:%S"`
echo "today:$TODAY"
# replace keyword in template
sed -i '' "s/_TITLE/$TITLE/g" $FILE_NAME
sed -i '' "s/_CAT/$CAT/g" $FILE_NAME
sed -i '' "s/_TAG/$CAT/g" $FILE_NAME
sed -i '' "s/_DATE/$TODAY/g" $FILE_NAME

```

以上脚本中使用到了shell中的如下命令：

- date 获取时间
- sed 替换文本内容

## shell - date 使用

格式化date 可以使用如下方法：


```sh
  date "+%Y-%m-%d-%H:%M:%S"
```

+ 后面是date 的格式，通过```man date```可以查找更详细的格式

## 将shell的返回值再赋值

以上实例中使用了:

```sh
TODAY=`date "+%Y-%m-%d-%H:%M:%S"`
```
将shell的返回值再赋值,

```sh
  ``
```  
在shell中是用来将返回值赋值

## 使用sed 替换文本

以下是MAC中sed的用法，－i后面额外多了‘’参数

```sh
sed -i '' "s/_TITLE/$TITLE/g" $FILE_NAME
```

解释```s/_TITLE/$TITLE/g```：

- s: replace
- _TITLE: 旧值
- $TITLE: 新值
- g: 全部替换(global)

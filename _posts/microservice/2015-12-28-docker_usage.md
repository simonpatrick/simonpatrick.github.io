---
layout: post
title: "docker usage: images"
modified:
categories: [microservice]
excerpt:
tags: [microservice]
date: 2015-12-28-21:49:22
---

Some Basic Command usage for docker

## images

大部分的命令就是如下的思路：

```
# install image
docker pull image_name
# search image
docker search <image_name>
# get images
docker images
# run images as a container
docker -it <image_name> <command>
# example:
docker run -t -i ubuntu:12.04 /bin/bash
# commit changes
docker commit -m="added what" -a="author_name" <image_id> <new_image_name>

```

## Dockerfile
Dockerfile是申明docker container的一个文件，通过此文件来描述今镜像（image）的属性.

Dockerfile的每一个指令：
```
INSTRUCTION statement
```

docker build:
我们使用 docker build 命令并指定 -t 标识(flag)来标示属于 ouruser ，镜像名称为 sinatra,标签是 v2。

```
docker build -t ouruser/sinatra:v2 .
```

run as container:

```
 docker run -t -i ouruser/sinatra:v2 /bin/bash
 ```

## remove image

```
docker rmi <image_name>
```

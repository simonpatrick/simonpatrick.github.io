---
layout: post
title: "docker usage: container"
modified:
categories: [microservice]
image: 17.jpg
tags: [microservice]
date: 2015-12-28T22:08:39
---

Docker container 的常用命令。

## Docker information

```sh
docker info
```

如果docker没有安装，则下载docker tools,如果权限不过就使用如下方法：

```sh
# 如果还没有docker group就添加一个：
$ sudo groupadd docker
# 将用户加入该group内。然后退出并重新登录即可生效。
$ sudo gpasswd -a ${USER} docker
# 重启docker
$ sudo service docker restart
```

## working with docker

``` sh
# Usage:  [sudo] docker [flags] [command] [arguments] ..
# Example:
$ docker run -i -t ubuntu /bin/bash
```

## 运行交互shell

``` sh
sudo docker run -i -t ubuntu /bin/bash
```

## 绑定Docker到另外的主机/端口或者Unix socket

```
$ sudo docker -H 0.0.0.0:5555 -d &
sudo docker -H :5555 pull ubuntu
# 进程模式下运行docker
$ sudo <path to>/docker -H tcp://127.0.0.1:2375 -H unix:///var/run/docker.sock -d &
# 使用默认的unix socker来下载ubuntu镜像
$ sudo docker pull ubuntu
# 或者使用TCP端口
$ sudo docker -H tcp://127.0.0.1:2375 pull ubuntu
```

## 开始一个长时间运行的工作进程

```
# 开始一个非常有用的长时间运行的进程
$ JOB=$(sudo docker run -d ubuntu /bin/sh -c "while true; do echo Hello world; sleep 1; done")

# 到目前为止收集的输出工作
$ sudo docker logs $JOB

# 关闭这项进程
$ sudo docker kill $JOB

```

## 列出容器

```
$ sudo docker ps # Lists only running containers
$ sudo docker ps -a # Lists all containers
$ sudo docker ps -l # List the last running container
```

## 控制容器

```
# 开始一个新的容器
$ JOB=$(sudo docker run -d ubuntu /bin/sh -c "while true; do echo Hello world; sleep 1; done")

# 停止容器
$ docker stop $JOB

# 开始容器
$ docker start $JOB

# 重启容器
$ docker restart $JOB

# 杀死一个工作
$ docker kill $JOB

# 删除一个容器
$ docker stop $JOB # Container must be stopped to remove it
$ docker rm $JOB
```

## 绑定服务到TCP端口

```
#让容器绑定4444端口，并通知netcat监听它。
$ JOB=$(sudo docker run -d -p 4444 ubuntu:12.10 /bin/nc -l 4444)

# 查看容器转发的公共端口
$ PORT=$(sudo docker port $JOB 4444 | awk -F: '{ print $2 }')

# 连接这个公共端口
$ echo hello world | nc 127.0.0.1 $PORT

# 确认网络连接工作
$ echo "Daemon received: $(sudo docker logs $JOB)"
```
## Delete Docker images

```
# 停止所有容器
$ docker stop $(docker ps -a -q)

# 删除指定镜像
$ docker rmi $image

# 删除无标示镜像，即id为<None>的镜像
$ docker rmi $(docker images | grep "^<none>" | awk "{print $3}")

# 删除所有镜像
$ docker rmi $(docker images -q)
```

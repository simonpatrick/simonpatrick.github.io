---
layout: post
title: "Python virtualenv in Mac"
modified:
categories: [python]
excerpt:
tags: [python]
image:
  feature:
date: 2014-11-24T10:31:11+08:00
---

virtualenv是一个创建python虚拟环境的工具,主要的解决的问题是,让在一个干净的Python环境中开发,不需要被不同的python
安装包烦恼,python3中实际已经内置了venv的,可以不使用virtualenv,以下是简要说明以下安装使用方法:

ps: 关于Python3和Python2很有可能在同一台机器上都有安装,所以注意python命令对应的是那个版本.have fun :)
## Python3 in Mac

```bash
python3 -m venv todo_mvc
```
Done ..........

## Python2 in Mac
### Install virtualenv in Mac

``` bash
	sudo pip install virtualenv
```

此前确认pip已经安装了

### Install virtualenvwapper in Mac

```bash
 sudo pip install virtualenvwapper
```

### 创建python开发环境

#### 直接使用virtualevn

1. 创建目录

``` bash
	mkdir python_test
	virtualenv python_test
```

2. 使用创建好的目录作为开发环境

```bash
	source /bin/activate
```

启动开发环境之后，可以使用pip安装需要的python依赖库，如selenium

```bash
pip install selenium
```

如果安装好了virtualenvwapper的话，可以使用如下命令使用开发环境：

```sh
mkvirtualenv python_test
```

退出：

```sh
deactivate
```

切换：

```sh
	workon python-test
```

删除

```sh
rm virtualenv python-test
```

---
layout: post
title: "Python PIP mirror设置"
modified:
categories: [python]
excerpt:
tags: [python]
image:
  feature:
date: 2014-11-24T10:31:11+08:00
---

使用默认的pip mirror速度实在太慢了，所以使用douban的pypi镜像.如何使用呢？很简单，以下几步：
- 修改~/.pip/pip.conf 文件，将index_url改成douban镜像地址:```http://pypi.douban.com/simple```

```python
[global]
index-url=http://pypi.douban.com/simple
timeout = 30
require-virtualenv = false
download-cache = /tmp
```

当然记得把require-virtualenv 值改为false

- 关闭终端，重新使用pip命令就可以使用douban镜像了，速度超快

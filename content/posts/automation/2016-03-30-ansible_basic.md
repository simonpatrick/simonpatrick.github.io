---
layout: post
title: "Ansible简单介绍"
modified:
categories: [automation]
image: ansible.png
tags: [automation]
date: 2016-03-30T13:15:11+08:00
---

# Ansible 介绍

Ansible 目前都是使用在python2上面.

## installation

在MAC 上面安装ansible有两种方式：
* pip

```shell
pip install ansible
```

* brew

```shell
brew install ansible
```

## ansible playbook 的简单使用

ansible 大概的一个框架图如下：
![img](ansible.png)


下面简单介绍一个使用ansible的例子：

- 配置hosts文件
  在当前目录创建一个hosts文件：

  ```shell
    [jenkins]
    192.168.3.50
  ```
- 配置ansible yml playbook文件
  配置当前一个yml文件:

  ```shell
  - hosts: jenkins
    user: root
    accelerate:true
    tasks:
      - name: restart_nginx
        shell: sh /root/auto_publish_qadoc.sh
  ```

- 运行命令

  ```shell
    ansible-playbook playbook.yml -i hosts -vv
  ```

  就可以运行这些命令了,最简单的ansible就是这样上手非常容易.
  不过仔细看看他的帮助文档的话，其实对于python不熟的人还是会有一定难度，不过如果写过程序的人，写过python东西的人来说，其实
  过一下这个document估计也就是1天时间就可以上手干活了.

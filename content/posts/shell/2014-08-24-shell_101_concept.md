---
layout: post
title: "Shell Learning - Concept"
modified:
categories: [shell]
excerpt:
tags: [shell]
image: 11.jpg
date: 2014-08-24T10:31:11+08:00
---

摘自：[http://wklken.me/posts/2014/01/12/shell-script-base.html](http://wklken.me/posts/2014/01/12/shell-script-base.html)

### 标准IO

    文件描述符
    0 标准输入 默认键盘
    1 标准输出 默认终端
    2 标准错误 默认终端


### 重定向

    > 输出重定向
    >> 追加到输出重定向
    < 输入重定向
    << 追加到输入重定向

    ls -l > /tmp/a

    cmd >/dev/null #输出到垃圾桶

dev是设备(device)的英文缩写。/dev这个目录对所有的用户都十分重要。因为在这个目录中包含了所有Linux系统中使用的外部设备。但是这里并不是放的外部设备的驱动程序，这一点和windows,dos操作系统不一样。它实际上是一个访问这些外部设备的端口。我们可以非常方便地去访问这些外部设备，和访问一个文件，一个目录没有任何区别。

/dev/null 它是空设备，也称为位桶（bit bucket）或者黑洞(black hole)。你可以向它输入任何数据，但任何写入它的数据都会被抛弃。通常用于处理不需要的输出流。（当然，它也可以作为空的输入流

dev/zero 该设备无穷尽地提供空字符（ASCII NUL, 0x00），可以使用任何你需要的数目。它通常用于向设备或文件写入字符串0，用于初始化数据存储。（当然，也可作为输出流的接受容器）

### 管道

前后连接两个命令

    ls -l | grep test

### 引号

    双引号：可以除了字符$`\外地任何字符或字符串
    单引号：忽略任何引用值，将引号里的所有字符作为一个字符串 $var 不能被解析
    反引号：设置系统命令输出到变量

### 命令执行

shell脚本识别三种基本命令：内建命令，shell函数和外部命令

基本的命令查找:shell会沿着查找路径$PATH来寻找命令

    echo $PATH

可以在.profile文件中修改

    export PATH=$PATH:$HOME/bin

and/or

    expression1 && expression2 && expression3
    只有前面一条命令执行成功，才执行下一条
    expression1执行成功，才执行expression2
    串联的

    expression1 || expression2 || expression3
    执行命令，直到有一条成功为止


# Linux运维常用工具
- Cobbler
- sshd
- iptables
- sysctl
- puppet agent
- limits
- ntp
- Ganglia
- Cacti
- Nagios
- Zabbix
- PlayBanch Watch
- Scribe Hadoop
- ScatterQ
- Yum Repository
- package
- Configuration/Change/Service/Custom

## Puppet中服务配置

- Systemg
- sshd
- iptables
- sysctrl
- ntp
- nginx
- zabbix
- scribe

---
layout: post
title: "zabbix 基础"
modified:
categories: [python]
excerpt:
tags: [python]
date: 2016-02-26T16:48:54
---

抽空花了1个小时看了一下Zabbix的界面和简单的手册，了解了一下Zabbix的基础知识，下面是一个小小的记录,后面就写一些Python的脚本来直接调用Zabbix的API在进行一些自动化的操作.


# Zabbix 基础
Zabbix 是一个开源的监控系统，由于需要帮助运维写一些调用ZABBIX API的代码，所以就开始了解一下ZABBIX的一些基本概念. 简单的看了一下Zabbix的一个手册，大致了解Zabbix监控的一些概念，以下是Zabbix中比较重要的概念或者可以认为一些抽象的实体资源:

* Configuration
  - HOST
  - HOST GROUP
  - Templates

* Monitor
  - Application
  - Items: keys
  - Triggers
  - Graphs

## Configuration:HOST
HOST 就是Zabbix监控的对象，创建HOST可以通过一些预先定义好的模版来实现.
以Linux Group来说的话，HOST可能还有以下的一些属性：

- Agent Interface
- SNMP Interface
- JMX Interface
- IPMI Interface
- Monitory proxy
- Status

## Configuration: HOST GROUP
创建HOST的同时可以创建一个HOST GROUP，HOST GROUP实际上就是不同的HOST组合起来成一组.

## Configuration: Templates
Templates 就是一些HOST的模版，相似的HOST可以通过模版继承，组合的方式创建

## Monitor
从监控的层级来看，监控HOST的层级逻辑是：

- HOSTGROUP: HOST GROUP是可以认为不同HOST的容器
- HOST: 监控的实体,监控的实体实际上有不同的监控模版组合而成

以下的APPLICATION，ITEM,TRIGGER,Graph 其实都是继承了模版的：

- APPLICATION,可以认为是一组监控的内容
- ITEM: item就是监控的具体的一个数值,比如```cl Loaded Class Count```他的key是```jmx["java.lang:type=ClassLoading",LoadedClassCount]```
这个ITEM就是具体监控LoadedClass数目的一项，那么多个项目就可以组合成一个Application，ITEM 其实可以认为是采样数据的一个项

一个Template可以通过多个Application来组合而成，一个Application可以由Items来组合而成，一个HOST包含有多个监控的Template，一个HOST Group可以有多个HOST.

关于TEMPLATE的继承关系是： HOST 继承HOST GROUP的TEMPLATE

- Graph： 图表
- Trigger： 触发器
这两个可以设置到模版级别的


## Monitor: Application
Application 可以认为是监控的一个大的项目，里面可能包括了不同的采样项目(item)
create Application，可以参考一下API文档就可以

## Monitor: Item

Item创建首先需要创建一个key(在创建KEY之前可以先创建一个TEMPLATE)，key 相当于需要监控什么，如何设置？
- 监控客户端设置, 在zabbix_agentd.conf中需要添加UserParameter

```shell
  grep -v '#' /etc/zabbix/zabbix_agentd.conf|grep -v "^$"
  export UserParameter=<key_name>,<shell_command> >>  <configure_file_location>
```
- ITEM的设置，可以设置ITEM的类型，同时使用一些表达是来完成需要的采样内容的设置


## Graphs

graph 就是图标，那么很明显，一个graph有x,y 轴，x轴一般总是时间序列，另外一个轴对应不同的item（采样项目），同时又一些graph的类型选择，以及图表大小的设置

## Triggers

Trigger 就是一个触发器，对于单独的一个item来说，如果设置了一些阀值,那么如果超过这个阀值，那么就会报警了.

这是Zabbix的一些基本概念，其他还有如：
- Action, 遇到问题进行的操作
- Screens: 多个Graph就组合成一个Screen
- Slideshow: 多个Screen可以轮播
- Map: 网络路径图
- Discovery Rule: 发现安装Zabbix Agent的机器的规则
- 其他：如一些各种interface的设置，大致有个了结，可能在后续中会使用

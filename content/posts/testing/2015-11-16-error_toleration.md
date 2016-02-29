---
layout: post
title: "软件容错"
modified:
categories: [testing]
excerpt:
tags: [testing]
date: 2015-11-16T23:24:33
---

软件的世界已经变的及其复杂，在互联网的世界中一个个知道不知道的API将世界连接起来，如蜘蛛网一般,一个看的到的功能可能依赖了好几个看不到的API,所以中间出点错误实在不能说是个意外了。但是出错归出错，出错了软件也是一样要处理这些问题，下面就讲讲我学到遇到的一点容错的小知识。

## 容错的目标

降低或者最小化对系统可用性，可靠性的影响，举个例子来说就是单点故障，如果一个地方出现错误
而把整个系统网络都拖垮了，这个显然是不能接受的。可以用一下几个来形容错误：

- fault(缺陷) 一些bug
- error(错误) 一些业务无法正常执行
- failure(故障) 业务较长时间无法正常执行

## 容错的方法

- 硬件容错：多备份,系统冗余，主备
- 软件容错：避免严重业务错误，降级，异常处理,侦测，监控，重启......
- 系统容错

## 常见机遇鲁棒性
- Process Pairs
- Graceful Degradation:降级
- Selective Retry
- state handling
- Linking Process
- Rejuvenation: 不可重现问题
- Checkpoint
- update lost
- application state scrubbing
- process pools
- recovery block
- micro reboot
- state correction

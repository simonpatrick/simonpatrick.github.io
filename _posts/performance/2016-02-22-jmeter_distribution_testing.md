---
layout: post
title: "JMETER 分布式测试"
modified:
categories: [performance]
excerpt:
tags: [performance]
date: 2016-02-22-09:33:59
---

# JMETER DISTRIBUTION TESTING

JMETER有时进行压力测试时，生成压力的机器性能不够，不能产生足够的压力，不过JMETER可以使用多个系统进行JMETER的压力测试，来解决这个问题. 使用多系统测试时需要注意：

- 关闭防火墙
- client in the same subnet
- 服务器在同一个字网
- Jmeter可以访问服务器
- JMeter是同一版本的

## JMETER Distribution Setting

- Master Setup
  config remote address:
  jmeter.properties: remote_host=ip1,ip2,ip3.....
- salve setup
  - running jmeter-server.bat/.sh 文件
  - modify jmeter-server file to change the rmiregistry location
- start TESTING

## Additional Resources

[JMETER FAQ](http://wiki.apache.org/jmeter/JMeterFAQ#How_to_do_remote_testing_the_.27proper_way.27.3F) [REMOTE-TEST](http://jmeter.apache.org/usermanual/remote-test.html)

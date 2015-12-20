---
layout: post
title: "jvm-monitoring-with-jmc"
modified:
categories: [java]
excerpt:
tags: [java]
date: 2015-12-04-21:52:29
---


## Running JVM with following options

```
-Dcom.sun.management.jmxremote.authenticate=false
-Dcom.sun.management.jmxremote.ssl=false
-Dcom.sun.management.jmxremote.port=7777
# 如果是Linux，下面这一行必须添加，以指定目标JVM的地址
-Djava.rmi.server.hostname=192.168.0.232
-Dcom.sun.management.jmxremote
-XX:+UnlockCommercialFeatures
-XX:+FlightRecorder
```

```
for /f "tokens=1-3 delims=/ " %%a in ('date /t') do (set md=%%a-%%b-%%c)
for /f "tokens=1-3 delims=/:." %%a in ("%TIME%") do (set mt=%%a%%b%%c)
set CUR_TIME=%md%-%mt%

rem 启用黑匣子默认记录行为。官方文档注明dumponexitpath支持目录，但我在7u71版本下测试失败
set JAVA_OPTS=%JAVA_OPTS% -XX:FlightRecorderOptions=defaultrecording=true,disk=true,dumponexit=true,dumponexitpath=%LOG_DIR%\jfr\dump-on-exit-%CUR_TIME%.jfr,maxage=3600s,settings=%JRE_HOME%\lib\jfr\profile.jfc
```

```
命令	说明
JFR.start
启动一个JFR（黑匣子记录）实例，参数：
name 本次记录的名称
settings 服务器上的设置模板
defaultrecording 是否启动默认录制
delay 录制延迟时间，默认0s
duration 录制持续时间，默认0s，表示无限
filename 录制文件的名称
compress 是否使用GZip压缩结果，默认否
maxage 数据最大生命周期，默认0s，表示无限制
maxsize 数据最大字节数，默认0，表示无限制
JFR.check
显示运行中的JFR的状态，参数：
name 记录名称
recording 记录标识符
verbose 打印冗余信息，默认否
JFR.stop
停止运行中的JFR，参数：
name 记录名称
recording 记录标识符
discard 是否丢弃录制数据
filename 拷贝录制数据到文件
JFR.dump
将录制中的JFR保存到文件，参数：
name 记录名称
recording 记录标识符
filename 拷贝录制数据到文件
```

https://blog.gmem.cc/jvm-monitoring-with-oracle-jmc

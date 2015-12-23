# Gatling quick start
## Introduction 介绍
这章主要介绍如何使用Gatling 进行压力测试，以及如何使用Gatling基础的DSL用法

## 获取Gatling bundle
- Bundle 下载地址
[下载地址](https://repo1.maven.org/maven2/io/gatling/highcharts/gatling-charts-highcharts-bundle/2.1.7/gatling-charts-highcharts-bundle-2.1.7-bundle.zip)

- Maven 设置
```xml
<dependency>
    <groupId>io.gatling.highcharts</groupId>
    <artifactId>gatling-charts-highcharts</artifactId>
    <version>2.1.7</version>
</dependency>
```
- SBT
```scala
libraryDependencies += "io.gatling.highcharts" % "gatling-charts-highcharts" % "2.1.7"
```

## 安装Gatling
解压bundle文件，gatling需要JDK7u6 以上.

## Encoding
Gatling的默认编码格式是UTF-8,在使用Recorder的时候需要设置合适的编码格式，
编码格式在gatling.conf 文件中配置

## Scala
Gatling使用Scala语言编写测试场景，如果你不了解Scala，也不用担心，因为Gatling的DSL写的
足够出色，你可以很方便的编写测试场景.
了解Scale你可以从以下网站开始[twitter scala school cn](http://twitter.github.io/scala_school/zh_cn/index.html)

## 终于开始测试了
在一通可能吓到你的介绍之后，终于开始测试了.不过不要被前面的内容吓到，耐心看到下面内容，你
就又满血复活了.

### 确定被测系统
我们以下面一个系统为例：http://computer-database.gatling.io

### 测试场景编制
一个应用的性能测试，我们需要创建一个测试场景来代表我们实际访问过的请求。下例是我们认为的一个
真实用户操作：
- 用户访问应用主页
- 用户查询macbook
- 用户打开一个相关的型号
- 用户返回主页
- 用户通过好几个页面创建一个新型号

### 使用Gatling基础
#### 录制请求
Gatling提供了录制请求的工具，此工具可以录制你访问页面的实际请求，那么如何使用录制工具呢：
* Linux/Unix
```sh
$GATLING_HOME/bin/recorder.sh
```
* Windows
```sh
%GATLING_HOME%\bin\recorder.bat
```

录制设置：
- computerdatabase package
- BasicSimulation name
- Follow Redirects? checked
- Automatic Referers? checked
- Black list first filter strategy selected
- ```.\*.css,.*\.js and .*\.ico in the black list filters

设置完毕，启动录制器的代理

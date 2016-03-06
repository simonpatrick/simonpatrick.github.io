---
layout: post
title: "Python完成简单的SVN Reviewboard Precommit的客户端"
modified:
categories: [python]
excerpt:
tags: [python]
image: 22.jpg
date: 2015-05-16T10:31:11+08:00
---


最近公司需要使用review board进行代码pre-commit review(pre-commit:正式提交前review)，而公司的现状是：
1. 使用SVN作为代码版本管理工具
2. 开发工具有eclipse，idea
3. MAC 和windows 机器居多

考虑到开发eclipse和idea插件，连接review board我一个人无法完成，同时能力也不够来开发这两种插件，
所以就准备python写一个命令行工具，期间研究了一下taobao review board的插件，感觉有点复杂，这个也是
使用python来些命令行工具的一个理由,也考虑过使用node-webkit来写个客户端，不过由于时间上的限制也就先放弃了

## 实现

实现过程中，使用到主要的包和工具是：

1. RBTools,review board 自带的工具，但是支持中文能力让人有点困惑
2. python，cmd 包(python自带)，requests包使用 pip install requests 安装
3. ConEmuPack(windows CMD的替代),主要为了支持window系统
4. SVN

最后实现了如下功能
- 选择更改的文件，提交Review Board 作为pre-commit review
- 根据review request id 提交代码到SVN
- python直接操作svn命令,可以通过简单的命令就提交代码(由于使用习惯的问题,个人觉得命令行比UI效率更高)
  svn命令有个问题就是如果操作delete或者add这种的话,如果文件没有直接放到svn work copy的话,提交需要两步操作,
  而这个工具也解决了这个问题


## Review Board 功能介绍
review board 是进行代码review的一个工具，目前公司主要用来做pre-commit的review，在review board针对pre-主要有如下概念：

- review request draft, draft里面包含了differ文件，描述，review的人等等
- review request，在这个review request上面review
- review完毕，才可以提交代码

## 安装和配置

### 1.安装Python 和Requests包

- 下载安装最新版本的Python，确保在命令行中可以执行Python命令，如果打开命令行工具，执行python -v 失败，需要在环境变量中设置Python的执行路径
- 安装Python完成之后，在命令行中执行

```sh
pip install requests
```

安装requests包到全局。MAC可能需要使用:

```sh
sudo pip install requests
```

### 2. 安装RBTools

下载安装RBTool,RBTool有不同操作系统对应的版本，根据自身操作系统下载并安装，MAC和windows都是可执行文件，一路next就可以
安装完毕，在命令行检查是否安装成功:

 ```sh
 rbt -v
 ```

 检查版本，如果有版本显示则成功

### 3. 配置SVN

配置SVN，MAC自带了SVN，Windows需要将SVN，配置到环境变量里面，具体方法如下,命令行中执行

```sh
	svn --version
```

如果返回版本信息，则忽略下面步骤:

    下载SVN BIN文件，将BIN目录配置到环境变量PATH下面，命令行中执行svn --version如果返回版本信息则成功

### 4. Windows 下载ComEmuPack

ComEmuPack是Windows Cmd的替代工具，主要为了解决中文输入和显示问题，Window上使用，如果MAC上使用终端工具就可以terminal或者iterm都可以

## 运行客户端

复制svnrbclient.py 到你本地SVN的目录下面，这个目录需要和Review Board上面的配置相对应，具体如下例说明：
1.review board配置某个repository是https://scm.******.com:8443/svn/Test/automation
2.repository的名字是：******-automation,假设你使用

```sh
svn checkout https://scm.******.com:8443/svn/******-automation
```

检出代码到******-automation目录，那么你需要将svnrbclient.py复制到你本地的******-automation下面.

打开命令行工具，运行

```sh
python svnrbclient.py
```

就可以，第一次使用会让你配置你的review board设置，如果嫌麻烦，可以创建如下内容的文件
到.reviewboardrc，不过复制之前需要修改，具体修改参考一下注释.

```
// 不需要修改
REVIEWBOARD_URL = "192.168.3.180"
// 一般修改至你动作的目录名
REPOSITORY = "******-automation"
// 工号
USERNAME=110863
//review board密码，和LDAP密码一样
PASSWORD="*******"
// 默认代码审查人的工号，可以是****，****格式，,间隔表示多人
TARGET_PEOPLE=****
```

## 使用客户端

在运行客户端之后，可以看到如下内容：

```sh
        ****** Review Board Client, ? for help, and the total command lists:
        1. setup:setup review board setting
        2. pre:precommit your changes to review board
        3. upre:update your precommit
        4. ss:svn status,find svn status for the working copies
        5. sa:svn add,add files to local svn
        6. sd:svn delete,delete svn file
        7. ci:svn commit,commit the changes by review request id
        8. sre: revert changes
        9. sdiff: generate differ file
        10.sci: commit the selected files directly
        11.exit: exit the client
       (****** RB Client)
```

以上就是这个客户端的所有功能，重点是如下几个功能：
1. pre: 创建review request
2. upre： 更新review request
3. ci: review通过之后，提交代码到SVN中央仓库，这个是根据review request id来作的提交
  也就是你提交review request修改了什么文件，使用ci命令就帮你提交此review request修改过的文件
一般执行方法是：在(****** RB Client)后面输入你需要的命令如：pre,然后按照提示一步一步操作就可以了.以下是输入的日志：

以下是使用pre commit的一个完全的shell场景:

* 输入命令pre

```
****** RB Client)pre
// 得到输出，需要选择此次修改的文件：
pre-commit the changes
svn status:
Changed Files Status:
ID |FILE SVN Status|File Name/File Path
0 | ? | .git
1 | ? | .idea
2 | ? | .ignorerc
3 | A | .reviewboardrc
4 | ? | automation-common/automation-common.iml
5 | M | automation-common/src/main/java/com/******/automation/ITestProcessor.java
6 | ? | automation-common/target
7 | A | automation-demo/automation-demo.iml
8 | ? | automation-demo/target
9 | A | differ_temp
10 | A | differ_temp/105
11 | A | differ_temp/105/diff_105_latest.txt
12 | A | differ_temp/105/differ_1432611692.92.txt
13 | A | differ_temp/105/differ_1432612400.93.txt
14 | A | differ_temp/105/notes.txt
15 | A | differ_temp/113
16 | A | differ_temp/113/diff_113_latest.txt
17 | A | differ_temp/113/differ_1432620381.6.txt
18 | A | differ_temp/113/differ_1432620573.37.txt
19 | A | differ_temp/113/notes.txt
20 | A | differ_temp/114
21 | A | differ_temp/114/diff_114_latest.txt
22 | A | differ_temp/114/differ_1432621517.49.txt
23 | A | differ_temp/114/differ_1432621894.64.txt
24 | ? | differ_temp/114/differ_1432622051.84.txt
25 | A | differ_temp/114/notes.txt
26 | ? | differ_temp/115
27 | ? | differ_temp/116
28 | ? | differ_temp/125
29 | ? | differ_temp/132
30 | ? | ******-automation.iml
31 | A | rbtools_requests.py
32 | M | svnrbtclient.py
33 | A | +
34 |  | >
35 | Summary | of
36 |  | Tree
```

* 输入文件的ID， 可以是5,32，或者是5-32，34-90 表示5-32,34-90的文件

```
Please select the files IDs which your want to commit,eg. 0,1,2,3, or Enter for All Files
<5,32


automation-common/src/main/java/com/******/automation/ITestProcessor.java svnrbtclient.py is ready to post to review board......
Please input your reviewer ID,Entry for default Reviewer>
reviewer ID:
Please input summary for your changes,it is nice to provide your Bug No:>修改svnrbclient
<Response [201]>
None
update draft timeout but it doesn't matter
draft request review id :133

//到这里review request 提交完毕
```

* 审核通过之后，输入ci命令，提交review request

```
(****** RB Client)ci

last 5 review requests status:
Request Review Id |Summary  | Status | Changed File List
133 | 修改svnrbclient
 | pending | automation-common/src/main/java/com/******/automation/ITestProcessor.java svnrbtclient.py

132 | 测试很多文件
 | pending | README.md automation-common/src/main/java/com/******/automation/Environment.java automation-common/src/main/java/com/******/automation/ITestProcessor.java automation-common/src/main/java/com/******/automation/drivers/DriverFactory.java automation-common/src/main/java/com/******/automation/helpers/webdriver/WebDriverHelper.java automation-common/src/main/java/com/******/automation/listener/testng/SimpleWebDriverScreenShotTestListener.java automation-common/src/main/java/com/******/automation/testscaffold/BaseWebCurrencyTest.java automation-common/src/main/java/com/******/automation/testscaffold/BaseWebTest.java automation-common/src/main/java/com/******/automation/testscaffold/webtest/WebTestContext.java automation-common/src/main/java/com/******/automation/testscaffold/webtest/webUI/elementloader/locator/CustomerElementLocatorFactory.java automation-common/src/main/java/com/******/automation/testscaffold/webtest/webUI/htmlelements/HtmlElement.java automation-common/src/test/java/com/******/automation/drivers/DriverFactoryTest2.java automation-common/src/test/java/com/******/automation/drivers/DriverFactoryTest_Concurrency.java automation-common/src/test/java/com/******/automation/drivers/testng-test1.xml automation-common/src/test/java/com/******/automation/helpers/webdriver/WebDriverHelperTest.java

115 | 更新readme
 | pending | ******rbclient_en.py README.md

116 | 测试测试
 | pending | ******rbclient.py

125 | 修改中文注释
 | pending | automation-common/src/main/java/com/******/automation/Environment.java automation-common/src/main/java/com/******/automation/ITestProcessor.java

//输入你要需要提交的 review request id号：  //提交结束
(****** RB Client)

```

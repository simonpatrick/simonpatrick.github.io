---
layout: post
title: "Ruby Dependency Management"
modified:
categories: [ruby]
image: 11.jpg
tags: [ruby]
date: 2015-11-03T10:31:11+08:00
---

在接触了一些语言之后,一般每一个语言都有工具来管理第三方包
的安装和管理. 比如:
- Java Maven/Gradle
- Python pip
- NodeJS NPM

而Ruby则用Bundler来做类似的事情. 以下是介绍一下Bundler的基本用法

## 安装Bundler

一句话安装 bundler

```bash
gem install bundler

```

## 开始使用Bundler 管理项目

首先初始化一个Bundler管理的项目:

```bash
  bundle init
```
运行以上命令之后,项目中会生成一个Gemfile文件.


## 安装第一个包
将rspec写入Gemfile

```bash
echo 'gem "rspec"' >> Gemfile
bundle install
```

至此一个简单的使用bundler 管理的项目就已经可以使用了.

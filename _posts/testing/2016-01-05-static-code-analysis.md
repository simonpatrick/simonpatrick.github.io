---
layout: post
title: "静态代码检查"
modified:
categories: [testing]
excerpt:
tags: [testing]
date: 2016-01-05-23:00:55
---

静态代码检查有利于提高代码质量，同时也可以快速的发现一些问题. 常用的静态代码检查有一下几种，
checkstyle，pmd，findbugs. 刚好公司需要做一个mybatis SQL注入的检查，所以收集了一下关于这三个工具使用的介绍

## checkstyle,PMD,findbugs 的是使用介绍

- **checkstyle** enforce coding conventions and standards in code, missing/improper javadoc, naming conventions, placement of braces and parentheses, whitespace, line length, etc
- **PMD** detect bad practices,PMD 支持不同语言，如JAVA，Ruby，XML等
- **findbugs** really find potential bugs,比如NPE，equals，hashcode等的用法


参考文章：
[checkstyle vs pmd vs findbugs](http://tirthalpatel.blogspot.com/2014/01/static-code-analyzers-checkstyle-pmd-findbugs.html)
[sonar security](http://www.sonarqube.org/sonar-to-identify-security-vulnerabilities/)
[checkstyle vs pmd vs findbugs 2](https://www.sparkred.com/blog/open-source-java-static-code-analyzers/)

---
layout: post
title: "Refactoring-8-remove God Class"
modified:
categories: [refactoring]
image: 8.jpg
tags: [refactoring]
date: 2015-11-03T10:31:11+08:00
---

God Class 就是一个类里面有一大堆不相干的方法放在一起,一般
情况下很多的工具类，或者manager有可能会有这样的情况.不是说不能有
工具类或者manager类，这个的关键是不相干的放在一个类里面。

不相干就违反了Single Responsibility的原则.

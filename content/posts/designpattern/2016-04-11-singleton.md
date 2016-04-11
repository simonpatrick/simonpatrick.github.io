---
layout: post
title: Java Singleton ENUM as instance HOLDER
modified: null
categories:
  - designpattern
  - java
image: singleton.jpg
tags:
  - designpattern
  - java
date: 2016-04-11T23:35:45.000Z
---

# Singleton 单例设计模式

单例模式是产生一个类的唯一实例。

## Java Singleton

Java 的Singleton实际上有很多种写法的，下面一个是使用枚举方式写的：

```Java
public class InitializingOnDemandHolderIdiom implements Serializable {

    private static final long serialVersionUID = 1L;

    private static class HelperHolder {
        public static final InitializingOnDemandHolderIdiom INSTANCE = new InitializingOnDemandHolderIdiom();
    }

    public static InitializingOnDemandHolderIdiom getInstance() {
        return HelperHolder.INSTANCE;
    }

    private InitializingOnDemandHolderIdiom() {
    }

    protected Object readResolve() {
        return getInstance();
    }

}
```

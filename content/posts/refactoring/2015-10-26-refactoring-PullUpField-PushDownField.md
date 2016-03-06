---
layout: post
title: "Refactoring-4-Push Down Method and Pull Up and Posh Down Field"
modified:
categories: [refactoring]
image: 5.jpg
tags: [refactoring]
date: 2015-10-26T10:31:11+08:00
---

Push down method 和Pull Up method刚好相反.
有时会遇到公用的父类方法在某个子类中不需要了,如果这样的情况可以考虑将功用
方法放到具体的实现中

## Push Down Method实例

重构前：

```java
public abstract class Animal {
    public void bark(){
        System.out.println("testing");   
    }
}

class Dog extends Animal{

}

class Cat extends Animal{

}
```

重构后:

```java

public abstract class Animal {

}

class Dog extends Animal{
  public void bark(){
      System.out.println("testing");   
  }

}

class Cat extends Animal{

}
```

## Pull Up and Posh Down Field

Pull Up and Posh Down Field 表达了Pull up 和 Push Down method
基本上一样的意思，只不过一个是方法，一个是成员变量

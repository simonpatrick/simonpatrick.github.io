---
layout: post
title: "Singleton 的不同写法"
modified:
categories: [java]
excerpt:
tags: [java]
date: 2015-12-02-12:42:18
---

Singleton是JAVA的一个非常常见的方式，不过不同写的方式会有不同的想法，下面就介绍一下这个模式

## Singleton 懒汉式模式，线程不安全

一个基本的写法如下:

```java
private static LazySingleton instance;
  private LazySingleton(){}

  public static LazySingleton getInstance(){
      if(instance==null){
          instance=new LazySingleton();
      }

      return instance;
  }
```

这个的一个问题是线程不安全，就是当instance是null的时候，可能有两个线程同时满足，这样就是两个实例产生

那么一个改进就是,加入synchronized

```java
public static LazySingleton getInstance(){
        if(instance==null){
            synchronized (LazySingleton.class){
                instance=new LazySingleton();
            }
        }

        return instance;
    }
```
来自网上的解释说这个也是有问题的:

```
这段代码看起来很完美，很可惜，它是有问题。主要在于instance = new Singleton()这句，这并非是一个原子操作，事实上在 JVM 中这句话大概做了下面 3 件事情。

给 instance 分配内存
调用 Singleton 的构造函数来初始化成员变量
将instance对象指向分配的内存空间（执行完这步 instance 就为非 null 了）
但是在 JVM 的即时编译器中存在指令重排序的优化。也就是说上面的第二步和第三步的顺序是不能保证的，最终的执行顺序可能是 1-2-3 也可能是 1-3-2。如果是后者，则在 3 执行完毕、2 未执行之前，被线程二抢占了，这时 instance 已经是非 null 了（但却没有初始化），所以线程二会直接返回 instance，然后使用，然后顺理成章地报错。
```

那么将instace定义为:

```java
private volatile static Singleton instance; //声明成 volatile
```

使用 volatile 的原因是可见性，也就是可以保证线程在本地不会存有instance 的副本，每次都是去主内存中读取。但其实是不对的。使用 volatile 的主要原因是其另一个特性：禁止指令重排序优化
读操作不会被重排序到内存屏障之前,从「先行发生原则」的角度理解的话，就是对于一个 volatile 变量的写操作都先行发生于后面对这个变量的读操作（这里的“后面”是时间上的先后顺序.

## Singleton 饿汉式 static final field

```java
private static final HungarySingleton instance = new HungarySingleton();

  private HungarySingleton() {
  }

  public static HungarySingleton getInstance() {
      return instance;
  }
```

## 内部静态类

内部静态类实现的方式：

```java

public class SingletonHolderModel {
    private static class SingletonHolder {
        private static final SingletonHolderModel INSTANCE = new SingletonHolderModel();
    }

    private SingletonHolderModel() {
    }

    public static final SingletonHolderModel getInstance() {
        return SingletonHolderModel.SingletonHolder.INSTANCE;
    }
}

```

## 枚举

我们可以通过EasySingleton.INSTANCE来访问实例，这比调用getInstance()方法简单多了。创建枚举默认就是线程安全的.

```java
public enum EasySingleton{
    INSTANCE;
}
```

---
layout: post
title: "Java 并发死锁实践－1"
modified:
categories: [java]
excerpt:
tags: [java]
date: 2015-11-18-08:57:44
---

 写点学习Java 并发死锁实践的来记录一下学习JAVA 并发的经历.

 ## 什么是JAVA的死锁(dead lock)
 死锁就是两个线程一直相互等待.
![img](http://www.importnew.com/10661.html/deadlock_flat_reentrant_locks)

实例代码如下:

```java
public class ThreadDeadlock {

    public static void main(String[] args) throws InterruptedException {
        Object obj1 = new Object();
        Object obj2 = new Object();
        Thread t1 = new Thread(new SyncThread(obj1, obj2), "t1");
        Thread t2 = new Thread(new SyncThread(obj2, obj1), "t2");
        t1.start();
        Thread.sleep(1000);
        t2.start();
    }
}

public class SyncThread implements Runnable{
    private Object obj1;
    private Object obj2;

    public SyncThread(Object o1, Object o2){
        this.obj1=o1;
        this.obj2=o2;
    }
    @Override
    public void run() {
        String name = Thread.currentThread().getName();
        System.out.println(name + " acquiring lock on object 1"+obj1);
        synchronized (obj1) {
         System.out.println(name + " acquired lock on object 1"+obj1);
         work();
         System.out.println(name + " acquiring lock on object 2"+obj2);
         synchronized (obj2) {
            System.out.println(name + " acquired lock on  object 2"+obj2);
            work();
        }
         System.out.println(name + " released lock on object 2"+obj2);
        }
        System.out.println(name + " released lock on object 1"+obj1);
        System.out.println(name + " finished execution.");
    }

    private void work() {
        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
```

running result:

```
t1 acquiring lock on java.lang.Object@370cd189
t1 acquired lock on java.lang.Object@370cd189  -- lock object1
t2 acquiring lock on java.lang.Object@509afc84
t2 acquired lock on java.lang.Object@509afc84 -- lock object2
t1 acquiring lock on java.lang.Object@509afc84  -- try to lock object 2 waiting object 2 released
t2 acquiring lock on java.lang.Object@3165be7c -- try to lock object1  waiting object 1 released

```

Thread1 lock object1 waiting object2 released to release object1
Thread2 lock object2 waiting object1 released to release object2

Thread1->Thread2->Thread1  所以死循环了，所以这就是死锁了。出现死锁后，线程就停止在那里一致等待了。
容器里面可能就有一只无法释放的线程堆积

使用JVisualVM可以看到如下的ThreadDump:

```
Found one Java-level deadlock:
=============================
"t2":
  waiting to lock monitor 0x00007ff1288332a8 (object 0x000000074001d9a8, a java.lang.Object),
  which is held by "t1"
"t1":
  waiting to lock monitor 0x00007ff128830758 (object 0x000000074001d9b8, a java.lang.Object),
  which is held by "t2"

Java stack information for the threads listed above:
===================================================
"t2":
	at com.hedwig.concurrence.deadlocksample.SyncThread.run(SyncThread.java:20)
	- waiting to lock <0x000000074001d9a8> (a java.lang.Object)
	- locked <0x000000074001d9b8> (a java.lang.Object)
	at java.lang.Thread.run(Thread.java:745)
"t1":
	at com.hedwig.concurrence.deadlocksample.SyncThread.run(SyncThread.java:20)
	- waiting to lock <0x000000074001d9b8> (a java.lang.Object)
	- locked <0x000000074001d9a8> (a java.lang.Object)
	at java.lang.Thread.run(Thread.java:745)

Found 1 deadlock.
```


## 避免死锁

- 避免嵌套封锁, 在这个例子中可以之对一个object加锁
- 只对有请求的进行封锁
- 避免无限期的等待

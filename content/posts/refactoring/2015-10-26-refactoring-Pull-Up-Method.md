---
layout: post
title: "Refactoring-3-Pull Up Method"
modified:
categories: [refactoring]
image: 6.jpg
tags: [refactoring]
date: 2015-10-26T10:31:11+08:00
---

Pull Up Method 顾名思义,就是把方法向上拉,向上拉是个什么意思呢?在面向
对象中向上就是向父类，或者接口拉,是不是很形象？


## Pull Up Method实例

假设这样一个场景,目前有:
- 抽象类－Vehicle
- 继承了Vehicle的离散类－ Car
- 继承了Vehicle的离散类－ Motorcycle

而turn方法目前只有在Car中有，那么我们把turn方法防盗Vehicle中
这样Motocyle也可以公用turn方法，这就是Pull Up Method.是不是很简单。。。。

以下是代码实例:

```java
public abstract class Vehicle {

    public class Car extends Vehicle {
        public void turn(Direction d){
            System.out.println("turing to "+d);
        }
    }

    public class Motorcycle extends Vehicle{
      public void turn(Direction d){
          System.out.println("turing to "+d);
      }
    }

    public enum Direction {
        Left,Right
    }
}
```

使用IDE refactor的pull up member 重构后再稍作修改后，代码如下：

```java
public abstract class VehicleRefactor {

    public void turn(Direction d) {
        System.out.println("turing to " + d);
    }

    public class Car extends VehicleRefactor {
    }

    public class Motorcycle extends VehicleRefactor {
    }

    public enum Direction {
        Left, Right
    }
}
```

这样一个pull up method就完成了.是不是高大上的名次变成了现实的easy模式了。

Dirty your hand,then you may know the truth.

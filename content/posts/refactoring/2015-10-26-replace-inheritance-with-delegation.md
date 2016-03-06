---
layout: post
title: "Refactoring-6-Replace Inheritance with Delegation"
modified:
categories: [refactoring]
image: 10.jpg
tags: [refactoring]
date: 2015-10-26T10:31:11+08:00
---

Replace Inheritance with Delegation, 这种重构方式主要是继承有时
看起来不是那么合理，同时继承可能让程序的扩展性不好，所以可以改用委托
或者组合的形式重构。

## 代码实例

- Refactor前:

```java
public class Sanitation {

    public String washHands(){
        return "Cleaned!";
    }
}

class Child extends Sanitation{
    public static void main(String[] args) {
        System.out.println(new Child().washHands());
    }
}
```

- Refactor之后:

把继承关系拿掉，才有委托的方式:

```java
class ChildRefactor{
    Sanitation s;
    public ChildRefactor() {
        s = new Sanitation();
    }

    public String washHands(){
        return s.washHands();
    }
}
```

## 好处的思考

- 逻辑上Sanitation(公共卫生)和Child没有那种继承关系,修改之后表达更加准确
- Child的washHand方法实际更加灵活了
- 更加容易通过使用Dependency Injection注入

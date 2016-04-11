---
layout: post
title: Prototype Pattern
modified: null
categories:
  - designpattern
  - java
  - python
image: prototype.png
tags:
  - designpattern
  - java
  - python
date: 2016-04-11T23:35:45.000Z
---

prototype pattern 实际上是通过clone的方式创建出同一个类的不同对象.

# Java Prototype

一般Prototype模式中，又一个prototype的抽象类：

```java

public abstract class Prototype implements Cloneable{
    @Override
    protected abstract Object clone() throws CloneNotSupportedException;
}
```

这个抽象类的不同子类：

```java
public abstract class Beast extends Prototype {

    @Override
    public abstract Beast clone() throws CloneNotSupportedException;

}
public class ElfBeast extends Beast {

    public ElfBeast() {
    }

    public ElfBeast(ElfBeast beast) {
    }

    @Override
    public Beast clone() throws CloneNotSupportedException {
        return new ElfBeast(this);
    }

    @Override
    public String toString() {
        return "Elven eagle";
    }

}

public abstract class Adams extends Prototype {

    @Override
    public abstract Adams clone() throws CloneNotSupportedException;

}

public class ElfAdams extends Adams {

    public ElfAdams() {
    }

    public ElfAdams(ElfAdams warlord) {
    }

    @Override
    public Adams clone() throws CloneNotSupportedException {
        return new ElfAdams(this);
    }

    @Override
    public String toString() {
        return "Elven Adams";
    }

}

public abstract class Sam extends Prototype {

    @Override
    public abstract Sam clone() throws CloneNotSupportedException;

}
```

通过工厂方法来创建不同的prototype的实例：

```java
public interface Factory {
    Sam createSame();
    Adams createAdams();
    Beast createBeast();
}

public class FactoryImpl implements Factory {
    private Sam sam;
    private Beast beast;
    private Adams adams;

    public FactoryImpl(Sam sam, Beast beast, Adams adams) {
        this.sam = sam;
        this.beast = beast;
        this.adams = adams;
    }

    @Override
    public Sam createSame() {
        try {
            return sam.clone();
        } catch (CloneNotSupportedException e) {
            return null;
        }
    }

    @Override
    public Adams createAdams() {
        try {
            return adams.clone();
        } catch (CloneNotSupportedException e) {
            return null;
        }
    }

    @Override
    public Beast createBeast() {
        try {
            return beast.clone();
        } catch (CloneNotSupportedException e) {
            return null;
        }
    }
}
```

客户端的调用：

```java


public class App {
    public static void main(String[] args) {




        Factory f=new FactoryImpl(new ElfSam(),
                new ElfBeast(),
                new ElfAdams());
        Sam sam = f.createSame();
        Adams adams = f.createAdams();
        Beast beast = f.createBeast();

        System.out.println(sam);
        System.out.println(adams);
        System.out.println(beast);
    }
}
```

# python prototype

以下是python中关于prototype的一个实现，代码量明显要比java少，不过起到了差不多的作用：

- Prototype 类，可以注册需要做prototype的类
- 通过clone方法来复制和修改实例的属性

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy


class Prototype:

    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]

    def clone(self, name, **attr):
        """Clone a registered object and update inner attributes dictionary"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class A:
    def __init__(self):
        self.x = 3
        self.y = 8
        self.z = 15
        self.garbage = [38, 11, 19]

    def __str__(self):
        return '{} {} {} {}'.format(self.x, self.y, self.z, self.garbage)


def main():
    a = A()
    prototype = Prototype()
    prototype.register_object('objecta', a)
    b = prototype.clone('objecta')
    c = prototype.clone('objecta', x=1, y=2, garbage=[88, 1])
    print([str(i) for i in (a, b, c)])

if __name__ == '__main__':
  main()
```

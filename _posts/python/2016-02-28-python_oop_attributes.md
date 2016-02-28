---
layout: post
title: "Python 面向对象，以及访问对象属性基础"
modified:
categories: [python]
excerpt:
tags: [python]
date: 2016-02-28-14:57:44
---

在前面的Zabbix API调用中我们看到了python的```__getattr__```的妙用，下面就探索一下这里面的道理,所以就聊聊python面向对象的基础知识.

## Python 面向对象

说到面向对象，就会说到类(class)，对象(object),那么什么是Class，Object呢？

- Object：
  Objects have states and behaviors. Example: A dog has states - color, name, breed as well as behaviors -wagging, barking, eating. An object is an instance of a class.
- Class:
  A class can be defined as a template/blue print that describes the behaviors/states that object of its type support.

那么综合起来，class就是用来描述一系列对象的一个模版，抽象出了共同的东西(class)，object就是具体的某种情况下的一个例子(instance)

面向对象有如下基础概念：

- Polymorphism
- Inheritance
- Encapsulation
- Abstraction
- Classes
- Objects
- Instance
- Method
- Message Parsing

## Python Class and Object 的使用

看下例：
- ```class Dog``` 定义了一个类
- ```__init__``` 构造这个类的方法，就是创建出一个Dog的对象是通过这个方法
- ```name```, 类的一个属性;```eat()```,也可以看成是类的一个属性，实际上它是一个dog的一个行为(behavior)
- ``` dog = Dog()``` 是创建了一个Dog(class)的新的的对象(object), 按照我们上面说的，dog是类Dog(class)的一个实例(instance)

```python
  class Dog:
    def __init__(self):
      self.name='dog'

    def eat():
      print('eating......')

  dog = Dog()
  print(dog.name)
```

## Python 对象的创建

参考上例，分别来说明对象的创建，访问.

- 对象的访问

```python
  dog = Dog()
```

Dog() 实际上创建了一个Dog的实例(object),那么他具体是通过Dog类的那个东西去实现的呢？是```__init__``` 方法实现的，可以通过下面的例子还看看：

我们修改代码，就class Dog 中的```__init__```方法去掉，然后运行代码看看

```python
AttributeError: 'Dog' object has no attribute 'name'
```

这是运行后的一个错误，也就是说```name```没有被初始化，远来的例子中name是通过```__init__``` 方法去初始化的，这也说明了实例的创建是通过```__init__```来创建的.

把```__init__``` 的修改还原，同时修改原有代码：

```python
def __init__(self):
    self.name='dog'
    print('Dog is created .....')
```

运行代码，发现Dog is created......输出了，所以使用```__init__```的猜测是正确的.
不过我们进一步做一个尝试，去掉```__init__```的代码，我们发现其实dog实例也是可以创建的，那么要问，没有```__init__```也可以创建呀，那么如果类都是通过```__init__```实例化的，那么这个时候怎么实例化的呢？

```python
print(Dog.__base__)
print(Dog.__bases__)
```

使用如上的代码可以知道Dog的base class是object，也就是使用object的```__init__```来实例话自己的.
到这里就简单的介绍了一下Python实例的创建.

## Python 类实例的创建－ 继承

面向对象就逃不过继承，下面看看在继承的情况下，如何创建对象的.
好，那么久先创建继承一个Dog的一个类： CrazyDog():

```python

class CrazyDog(Dog):

    def why_crazy(self):
        print('I am sick.......')

crazy_dog = CrazyDog()
crazy_dog.eat()
print(crazy_dog.name)
crazy_dog.why_crazy()

```

以下是一个创建了一个CrazyDog的类，继承了Dog，python中继承就是在类声明语句的()中加入需要继承的类.运行上面的程序，可以看到：

```python
Dog is created .....
eating .....
dog
I am sick.......
```

这里就更加清楚的看到了子类在没有定义```__init__```的情况下，去使用了父类的```__init__```方法.接下来我们尝试用自己的```__init__``` 方法：

```python
class CrazyDog(Dog):
  def __init__(self):
      super().__init__()
  def why_crazy(self):
      print('I am sick.......')
```

注意使用super的写法哦，他需要调用__init__方法的哦.重写后实际上我们是显性调用了父类的```__init__```方法，同时可以完成自己写自己的```__init__```方法:

```python
class CrazyDog(Dog):
    def __init__(self):
        self.is_crazy=True

    def why_crazy(self):
        print('I am sick.......')
```

运行，报错，name不存在,```AttributeError: 'CrazyDog' object has no attribute 'name'```, 哦，远来要使用父类的属性，是需要显性初始化父类的,修改成如下代码，一切就OK了.

```python
class CrazyDog(Dog):
    def __init__(self):
        super().__init__()
        self.is_crazy=True

    def why_crazy(self):
        print('I am sick.......')
```

## Python 访问对象中的属性

上面例子中其实已经有如何访问对象的属性或者方法了，如：

```python
crazy_dog = CrazyDog()
crazy_dog.eat()
print(crazy_dog.name)
crazy_dog.why_crazy()
```

这些都非常容易理解，同时这里也可以看到，python的对象里面没有java的：```public,private,protected```等定义来确定访问的范围.

## Python 访问对象的属性： __getattr__,__setattr__

继续再聊聊python的访问对象的属性，做个试验：

```python
class CrazyDog(Dog):
    def __init__(self):
        super().__init__()
        self.is_crazy = True

    def why_crazy(self):
        print('I am sick.......')

    def __getattr__(self, item):
        print('getting attribute', item)
        return (item, 'getattr_created')
crazy_dog = CrazyDog()
crazy_dog.eat()
print(crazy_dog.name)
crazy_dog.why_crazy()
print(crazy_dog.name1)
```

得到如下结果：

```python
Dog is created .....
eating .....
dog
I am sick.......
getting attribute name1
('name1', 'getattr_created')
```

这个例子表明，如果访问没有定义变量名的时候，python是通过__getattr__来访问的，未定义属性的赋值呢？

```python
class CrazyDog(Dog):
  def __init__(self):
      super().__init__()
      self.is_crazy = True

  def why_crazy(self):
      print('I am sick.......')

  def __getattr__(self, item):
      print('getting attribute', item)
      return (item, 'getattr_created')

  def __setattr__(self, key, value):
      print('using setattr set value')
      print(key, value)
      super().__setattr__(key, value)

```

访问：

```python
crazy_dog = CrazyDog()
crazy_dog.eat()
print(crazy_dog.name)
crazy_dog.why_crazy()
crazy_dog.name2 = 'test_set_attr'
print(crazy_dog.name1)
print(crazy_dog.name2)
```

结果```crazy_dog.name2```是test_set_attr, 这个例子清楚的表明，没有定义的属性变量是通过```__setattr__```去访问的，如果我们修改原有的代码：

```python
# super().__setattr__(key, value) 修改到如下的代码：
setattr(self,key,value)
```
运行，我们会发现递归深度不够的错误，所以这个地方我们需要使用```super().__setattr__(k,v)```来处理, 那么为什么呢？
我自己推测是setattr(self,k,v)是使用了self的__setattr__,那么很明显这个就是死循环了，因为他具体到了self这个实例，如果改为：

```python
setattr(Dog,key,value)
setattr(CrazyDog,key,value)
```

都可以成功，相信这里面python语言再lookup method的时候有一套自己的方法.

回顾一下这个__getattr__,_setattr__ 两个方法，可以动态创建属性，这个机制会减少不少的代码量.和java比起来会减少很多的反射的代码.

这块内容需要继续学习和挖掘！

---
layout: page
title: "Python 基础-语法"
modified:
categories: [python]
excerpt:
tags: [python]
image: 11.jpg
date: 2013-11-24T10:31:11+08:00
---



学习一门语言，就当多一门手艺。虽然是个测试，被人唾弃，但是相信自己比什么都重要。
卷起袖子，dirty your hand。以下是学习https://github.com/qiwsir/StarterLearningPython的笔记.

## python 运行
以下是python运行命令，同时带了两个不同的参数：

```python
	python <filename>.py # pyc 文件生成
	python <filename>.py # pyo 文件生成，优化了的python字节码
```

## 数字，变量，计算

1. python里面的数字主要又以下几种：
	- 整数， 如2
	- 浮点数，如2.22
	- 长整数，如2.222222222222L
	- 其他如：十进制，还有二进制、八进制、十六进制

2. python 变量

对象有类型，变量无类型， 如何理解 x=5, x 没有赋值时没有类型，当=5时就是int了，如果x='str'时，就是String了

3. 四则运算
运算符号：
```
#- +,-,*,/#
```

看一下例子就可以了解基本的运算和类型了：

```python
a=4+2
b=4.0+2
#自动处理整数溢出
x= 123456789870987654321122343445567678890098876*1233455667789990099876543332387665443345566999999999999

print a,b,x
print(type(a))
print(type(b))
print(type(x))


print a/b
print a/2
#不管是被除数还是除数，只要有一个数是浮点数，结果就是浮点数
print a/2.0
print x/0
```

以上预算的结果,出错信息也显而易见

```python

6 6.0 152278477193527562870044352587576277277562451818822315203216690188373592848234522837124321109901124
<type 'int'>
<type 'float'>
<type 'long'>

1.0
3
3.0

ZeroDivisionError: long division or modulo by zero

```

对于数值计算来说,以下内容供参考
>
对于需要非常精确的情况，可以使用 decimal 模块，它实现的十进制运算适合会计方面的应用和高精度要求的应用。另外 fractions 模块支持另外一种形式的运算，它实现的运算基于有理数（因此像1/3这样的数字可以精确地表示）。最高要求则可是使用由 SciPy提供的 Numerical Python 包和其它用于数学和统计学的包。列出这些东西，仅仅是让看官能明白，解决问题的方式很多，后面会用这些中的某些方式解决上述问题。
[浮点数算法：争议和限制](https://docs.python.org/2/tutorial/floatingpoint.html#tut-fp-issues)

## 使用计算模块 ```division```

使用python的模块来作除法：```from __future__ import division``` 所有的除法就都是浮点数了:

```python
	from __future__ import division
	print 5/2  # 2.5 如果不用division，则为2
```
整除方法：

```python
print divmod(5,2) # 返回元组（2，1）
print divmod(10,3)[0],divmod(10,3)[1],divmod(10,3)
# 结果是：
3 1 (3, 1)
```

## 四舍五入 ```round```

四舍五入取位数：

```python
print round(1.2345567, 2)
print round(1.23456677, 3)
print round(10.0 / 3, 4)
```

结果是：

```
1.23
1.235
3.3333
```

以下结果不要惊慌,这是正常的！！！！

```python
round(1.2345,3)
1.234               #应该是：1.235
round(2.235,2)
2.23                #应该是：2.24

```

## Math 模块小试

以下代码小试以下Math模块：

```python
print math.pi
functions = dir(math)
print pow(4, 2)
for x in functions:
    print x
    print help(x)
```
## 优先级

以下是优先级从低到高的顺序：

|运算符|描述|
|------|----|
|lambda|Lambda表达式|
|or|布尔“或”|
|and|布尔“与”|
|not x|布尔“非”|
|in，not in|成员测试|
|is，is not|同一性测试|
|<，<=，>，>=，!=，==|比较|
|\|按位或|
|^|按位异或|
|&|按位与|
|<<，>>|移位|
|+，-|加法与减法|
|*，/，%|乘法、除法与取余|
|+x，-x|正负号|
|~x|按位翻转|
|**|指数|
|x.attribute|属性参考|
|x[index]|下标|
|x[index:index]|寻址段|
|f(arguments...)|函数调用|
|(experession,...)|绑定或元组显示|
|[expression,...]|列表显示|
|{key:datum,...}|字典显示|
|'expression,...'|字符串转换|

### 1.Python基础常识

1. 安装python（windows基本就是下载后安装，linux和mac自带
2. 添加python到windows 的path中
3. 执行python文件： ```python <file>```
4. python 文件 encoding

```python
    '#_*_coding:utf-8_*_'
```

5. 注释

```python
""" docs """
```

### 2.Python 注释和#号

- # A comment

### 3.数字和数字计算

```
- +，-，/,*,%,<,>,<=,>=
```

### 4. 变量<variable>和命名

1. car = 100
2. space_in_a_car = 4.0
3. 和java的常用规范还是有点不同，python不用驼峰

### 5. 打印更多的变量
1. 格式化打印

```python
print "this is for %s", %test
```

### 6.字符串和文本

1. 可以带格式参数赋值

```python
 x= "%s,%s" % (s1,s2)
```
2. %r-用来debug raw data会打印,%s

### 7. 转义字符
### 8. raw_input("XXXXX")
### 9. 参数，解包，变量

```python
 from sys import argv
    script,first, second, third = argv
```

### 10. IO

1. close–关闭文件。跟你编辑器的文件->保存..一个意思
2. read – 读取文件内容。你可以把结果赋给一个变量
3. readline–读取文本文件中的一行
4. truncate–清空文件,请小心使用该命令
5. write(stuff) – 将 stuff 写入文件
6. open("",a/w/r), read, write, append

### 11. Function and Variants

```python
def functionName() :
```

### 12. return of Function

```python
def function1():
    return 1;
```

###13.逻辑关系
###14.布尔表达式
###15.if, if-else,if-elif-else
###16.循环，列表
###17. 列表

1. 定义 ：[]
2. append： element.append()
3. 访问index x[0]....

###18. 关键字

• and
• del
• from • not
• while • as
• elif
• global
• or
• with
• assert
• else
• if
• pass
• yield
• break
• except
• import
• print
• class
• exec
• in
• raise
• continue • finally • is
• return
• def
• for
• lambda/try

###19. 数据类型

• True
• False
• None
• strings • numbers • floats • lists

###20. list and dictionary

1. list : []
2. dictionary :{"key" :"value"}

###21. module,class,object

1. module: 不是类，里面可以定义函数，变量，大体可以看做一个静态类或者一个单例类
2. class：和JAVA里面的类相似

```python
    __author__ = 'simon'
    # _*_ coding:utf-8 _*_

    # 定义类
    class MyStuff(object):
        def __init__(self):  # 初始化类，构造器
            self.target = "Andriod"
    # self 就是 this
        def apple(self):
            print self.target
            print "test apple"

    # 实例化
    myStuff = MyStuff()
    myStuff.apple()
```

###22. is-a/has-a
###23. 继承(Inheritance)VS合成(composition)

1. 隐身继承

```python
#隐身继承
    class Parent(object):
        def implicit(self):
         print("implicit class!")

    class Child(Parent):
        pass
```

2. 显示继承

```python
    ##显示继承
    class Test(object):
        def override(self):
            print "parent override"

    class TestChild(Test):
        def override(self):
            print "child override"
```

3. super（）
4. 多重继承（multiple inheritance）
5. composition组合

```python
    # _*_ coding=utf-8 _*_
    __author__ = 'patrick'

    class Other(object):
        def overrider(self):
            print "override"

        def altered(self):
            print "other alter!"

    class Child(object):
        def __init__(self):
            self.other =Other()

        def override(self):
            self.other.overrider()

        def altered(self):
            self.other.altered()

    child = Child()
    child.altered()
    child.override()
```

###24.Python风格

1.类名:camel case/method 名字： underscore format
2.class name（object）
3.注释说为什么这样子做，而不是怎么做

以下是学习python guide时候的一些笔记，同时应该是满足所有的编程语言的。

## 1. Writing Great Code

- structuring your project
- code style
- reading great codes
- documentation
- testing your codes
- logging
- common gotchas

### 1.1 structuring your project

不要小看了这个项目结构，好的结构可以让项目一目了然。好的项目结构可能就回答了以下几个问题：
- which function should go into which modules
- how does the data flow through the project
- which functions and features can be grouped together and isolated

以下是一些不好的设计：
- 不同的内容放在一起而相互影响
- 隐含的依赖，hidden coupling
- 全部变量和状态的滥用
- spaghetti code and ravioli code

对于python来说，处理这些组织代码的事情可以使用modules，package(__init__.py),还有一些重用的方法如：
- decorators

```python
def foo():
  # do something
def decorator(func):
  # do something
  return func

# manually decorator
foo = decorator(foo)

@decorator
def bar():
  # Do something

# bar is decorated
```

- dynamic typing

变量可以不是固定类型，Variables are not a segment of the computer’s memory where some value is written, they are ‘tags’ or ‘names’ pointing to objects.

- mutable and immutable types

mutable: list, dict
immutable: int

```python
my_list = [1,2,3,4]
my_list[0]=4
print my_list  # the same list

x = 6
x=x+1 # the next x is another object
```

```python
foo = 'foo'
bar = 'bar'
foobar = '%s%s' % (foo, bar) # It is OK
foobar = '{0}{1}'.format(foo, bar) # It is better
foobar = '{foo}{bar}'.format(foo=foo, bar=bar) # It is best

```
## 1.2 code style

- Explicit code

```python
# Bad
￼def make_complex(*args):
  x, y = args
  return dict(**locals())

# good
def make_complex(x,y):
  return {'x':x,‘y’：y}
```

- function arguments
* positonal arguments

```python
send(message, recipient)
```

* keywords arguments

```python
send(message, to, cc=None, bcc=None)
```
* arbitrary argument list

```python
send(message, *args)
```

* arbitrary keyword argument dictionary

```python
send(message, **args)
```

- Avoid the magical wand/all responsible users
The main convention for private properties and implementation details is to prefix all “internals” with an underscore.
- return values
raising exception or return None/False
- Idioms
* unpacking

```python
for index,item in enumerate(some_list):
  # do something

a,b=b,a
a,(b,c)=1,(2,3)

# python3
a,*rest=[1,2,3]
b,*middle,c=[1,2,3,4,5]
```

- create an ignored Variables

```python
￼filename = 'foobar.txt'
basename, __, ext = filename.rpar
```

- PEP8

```sh
pep8 optparse.py
```
- convertions

```python
# don't use has_key in dictionary
d ={'hello':'world'}
print d.get('hello',default_value)
if 'hello' in d:
  print d['hello']
```

- short ways to manipulate lists

```python
# bad
a = [3, 4, 5]
b = []
for i in a:
  if i > 4: b.append(i)

# good
a = [3, 4, 5]
b = [i for i in a if i > 4]
# Or:
b = filter(lambda x: x > 4, a)

a = [3, 4, 5]
a = [i + 3 for i in a]
# Or:
a = map(lambda i: i + 3, a)

a = [3, 4, 5]
for i, item in enumerate(a):
  print i, item
```

- read from a file

```python
￼with open('file.txt') as f:
  for line in f:
      print line
```

- line continuations

```python
# bad
my_very_big_string = """For a long time I used to go to bed early. Sometimes, \
    when I had put out my candle, my eyes would close so quickly that I had not even \
    time to say “I’m going to sleep.”"""
from some.deep.module.inside.a.module import a_nice_function, another_nice_function,  yet_another_nice_function

# good
my_very_big_string = (
"For a long time I used to go to bed early. Sometimes, "
"when I had put out my candle, my eyes would close so quickly " "that I had not even time to say “I’m going to sleep.”"
)

```

## 1.3 read great codes

- Howdoi Howdoi is a code search tool, written in Python.
- Flask Flask is a microframework for Python based on Werkzeug and Jinja2. It’s intended for getting started very
quickly and was developed with best intentions in mind.
- Werkzeug Werkzeug started as simple collection of various utilities for WSGI applications and has become one of the most advanced WSGI utility modules. It includes a powerful debugger, full-featured request and response objects, HTTP utilities to handle entity tags, cache control headers, HTTP dates, cookie handling, file uploads, a powerful URL routing system and a bunch of community-contributed addon modules.
- Requests Requests is an Apache2 Licensed HTTP library, written in Python, for human beings.
- Tablib Tablib is a format-agnostic tabular dataset library, written in Python.

## 1.4 ducomentation

- readme
- project documentation
- api reference
- tutorial
- reStructuredText documentation
- code documentation advice

```python
￼def square_and_rooter(x):
"""Returns the square root of self times self."""
  # do something
```
Do not use triple-quote strings to comment code. This is not a good practice.
PEP 257


## 1.5 Testing your codes

- unittest/unittest2
- doctest

The doctest module searches for pieces of text that look like interactive Python sessions in docstrings, and then executes those sessions to verify that they work exactly as shown.
Doctests have a different use case than proper unit tests: they are usually less detailed and don’t catch special cases or obscure regression bugs. They are useful as an expressive documentation of the main use cases of a module and its components. However, doctests should run automatically each time the full test suite runs.

- pytest
- nose
- tox
- mock

## 1.6 logging

- diagnositic logging
- audit logging

## 1.7 common gotchas

- mutable  default arguments
default argumant is mutable, python的方法每次被访问时不是重新建立，所以一定要小心，除非你是exploit(user as intended)

```python
def append_to(element,to=[]):
  to.append(element)
  return to

# what you expected to happen
my_list=append_to(12)
print my_list
my_list=append_to(42)
print my_list

# your expected result:
[12]
[42]

# but actual result:
[12]
[12,42]

# so

def append_to(element,to=None):
  to.append(element)
  return to
```

- late binding closure

```python
def create_mulipliers():
  return [lambda x : i * x for i in range(5)]

for n in create_mulipliers():
      print n(2)  
```

Python’s closures are late binding. This means that the values of variables used in closures are looked up at the time
the inner function is called.

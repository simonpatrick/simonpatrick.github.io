---
layout: post
title: "Python 基础-字符串处理"
modified:
categories: [python]
excerpt:
tags: [python]
image:
  feature:
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
#- +,-,*,/#

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
```
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








# Python String learning notes

字符串是任何一门语言中常用的一个类型，python中也是，以下是关于python string一个学习的记录

## 字符串简单操作

python中用双引号，或者单引号来表示字符串

```python
print "print hello world-------"
print 'print hello world!!!!'
```

## 字符串连接

```python

	>>> print "py"+"thon"
	python

```

## 字符串编码

python2的编码比较繁琐，使用中文比较头疼，以下是一个简单的例子，一个基本的原则是：
1. 输入中文马上encode成Unicode,utf-8格式
2. 使用utf-8 解码

```python
print "中国".encode('utf-8')
print "中国".encode(sys.getfilesystemencoding())
print "中国".encode('acii'').decode('utf-8')

```

## 字符串函数操作

数字转换成字符串：

```python
	print str(1234543)
	print type(str(1234456))
	print type(repr(1234543))
```

这里面str和repr函数的区别会在后续中提到，下面使用一个下例子说明以下区别：str是个人看的，repr是给python看的，这是网友一个天才的解释

```python
 print str("hello world \n")
 print repr("hello world\n")
```

## 连接字符串-更好可读性

- 使用占位符

```python
print '%s %s'%('hello','world')
print '%d %s'%(1,'world')
nameAge={"zhang":10,"wang":11,"li":32} "wang's age is %(wang)d" % nameAge 
"{0},{2},{1},{str}".format(one,2,3,str="string") 
```
以下这个方式更又可读性：
```python
s.format(*args,*kwargs) 
```

- 使用dict

```python
print ''
```

## 字符串功能函数

```python
print ‘hello world'.upper()
print ‘hello world'.lower()
print ‘hello world'.capitalize()
print ‘hello world'.istitle()
print ‘hello world'.islower()
'hello world'.strip()
'hello world'.lstrip()
'hello world'.rstrip()

···




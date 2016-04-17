---
layout: post
title: Python Tricky-01
modified: null
categories:
  - python
image: 10.jpg
tags:
  - python
date: 2016-04-17T10:41:15.000Z
---

# Python Tricky-2

## max split

```python

"""split a string max times"""
string = "a_b_c_d_e"
print(string.split("_", 2))


"""use maxsplit with  arbitrary whitespace"""

s = "foo    bar        foobar foo"

print(s.split(None, maxsplit=1))
```

## min and max index

获取最大值，最小值的index

```python

"""
Find Index of Min/Max Element.
"""

lst = [40, 10, 20, 30]


def minIndex(lst):
    return min(range(len(lst)), key=lst.__getitem__)  # use xrange if < 2.7


def maxIndex(lst):
    return max(range(len(lst)), key=lst.__getitem__)  # use xrange if < 2.7


print(minIndex(lst))
print(maxIndex(lst))
```

## nested function

python 支持函数作为参数传递：

```python


"""nested functions"""
def addBy(val):
    print(val)
    def func(inc):
        print(inc)
        return val + inc
    return func

addFive = addBy(5)
print(addFive(4))

addThree = addBy(3)
print(addThree(7))
```

## obj get attribute

通过getattr获取python的属性，可以是类级别的，也可以实例级别的，但是如果属性没有实例级别是先通过`__getattribute__`获取

```python


class obj():
    attr = 1

    def __getattribute__(self, item):
        print('get attribute')
        return "123"

    def __get__(self, instance, owner):
        print("get")

    def __getattr__(self, item):
        print("get attribute1")


foo = "attr"
a = obj()
print(a.test)
print(getattr(obj, foo))
print(getattr(a, "attr1"))
```

## remove duplicated values

这里面需要理解清楚的是：

- list，可以重复
- set,没有重复

```python
"""remove duplicate items from list. note: does not preserve the original list order"""

items = [2, 2, 3, 3, 1]

newitems2 = list(set(items))
print(newitems2)

"""remove dups and keep order"""

from collections import OrderedDict

items = ["foo", "bar", "bar", "foo"]

print(list(OrderedDict.fromkeys(items).keys()))
```

## reverse list/string

```python
"""reversing list with special case of slice step param"""
a = [5, 4, 3, 2, 1]
print(a[::-1])

"""iterating over list contents in reverse efficiently."""
for ele in reversed(a):
    print(ele)
```

```python
"""reversing string with special case of slice step param"""

a = 'abcdefghijklmnopqrstuvwxyz'
print(a[::-1])


"""iterating over string contents in reverse efficiently."""

for char in reversed(a):
    print(char)

"""reversing an integer through type conversion and slicing."""

num = 123456789
print(int(str(num)[::-1]))
```

## set operators 集合操作

```python
"""Python provides usual set operator"""
a = set(['a', 'b', 'c', 'd'])
b = set(['c', 'd', 'e', 'f'])
c = set(['a', 'c'])

# Intersection
print(a & b)

# Subset
print(c < a)

# Difference
print(a - b)

# Symmetric Difference
print(a ^ b)

# Union
print(a | b)

"""using methods instead of operators which take any iterable as a second arg"""

a = {'a', 'b', 'c', 'd'}
b = {'c', 'd', 'e', 'f'}
c = {'a', 'c'}

print(a.intersection(["b"]))

print(a.difference(["foo"]))

print(a.symmetric_difference(["a", "b", "e"]))

print(a.issuperset(["b", "c"]))

print(a.issubset(["a", "b", "c", "d", "e", "f"]))

print(a.isdisjoint(["y", 'z']))

print(a.union(["foo", "bar"]))

a.intersection_update(["a", "c", "z"])
print(a)
```

## set global variables

python 的全局变量也可以更新：

```python
"""set global variables from dict"""

d = {'a': 1, 'b': 'var2', 'c': [1, 2, 3]}
globals().update(d)
print(globals())
print('a' in globals().keys())
```

## socket msg handling

```python

import socket
import functools

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn = s.connect(('localhost', 1080))
msgs = []

# normal way
# while True:
#    msg = coon.recv(1024)
#    if recv:
#        msgs.append(msg)
# else:  # when no msg come, break
#         break

# hack way with iter and functools.partial
# this circle will auto break when msg is empty ''
for msg in iter(functools.partial(conn.recv, 1024), b''):
    msgs.append(msg)
```

## sort list keeping indices

- enumerate 使用
- zip 使用

```python

"""Sort a list and store previous indices of values"""

"""
# enumerate is a great but little-known tool for writing nice code
"""

l = [4, 2, 3, 5, 1] print("original list: ", l)

values, indices = zip(*sorted((a, b) for (b, a) in enumerate(l)))

"""
# now values contains the sorted list and indices contains

# the indices of the corresponding value in the original list
"""

print("sorted list: ", values) print("original indices: ", indices)

"""
# note that this returns tuples, but if necessary they can

# be converted to lists using list()
"""
```

## step slice

python stepwise slicing of arrays

```python
"""stepwise slicing of arrays"""
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[::3])
```

## swap keys and values

key,value 交换，只要是通过 `v：k for k,v in dict.items()｝` 这个方式就可以了

```python
"""Swaps keys and values in a dict"""

_dict = {"one": 1, "two": 2}
# make sure all of dict's values are unique
assert len(_dict) == len(set(_dict.values()))
reversed_dict = {v: k for k, v in _dict.items()}
print(reversed_dict)
```

## zip 使用

```python

"""transpose 2d array [[a,b], [c,d], [e,f]] -> [[a,c,e], [b,d,f]]"""

original = [['a', 'b'], ['c', 'd'], ['e', 'f']]
transposed = zip(*original)
print(list(transposed))
```

## tree 使用

```python

"""
See description here
https://gist.github.com/hrldcpr/2012250
"""

from collections import defaultdict

tree = lambda: defaultdict(tree)


users = tree()
users['harold']['username'] = 'chopper'
users['matt']['password'] = 'hunter2'
```

## try else

```python
""" You can have an 'else' clause with try/except.
    It gets excecuted if no exception is raised.
    This allows you to put less happy-path code in the 'try' block so you can be
    more sure of where a caught exception came from."""

try:
    1 + 1
except TypeError:
    print("Oh no! An exception was raised.")
else:
    print("Oh good, no exceptions were raised.")
```

also while else:

```python
i = 5

while i > 1:
    print("Whil-ing away!")
    i -= 1
    if i == 3:
        break
else:
    print("Finished up!")
```

## unique by attr

```python
"""
    If we have some sequence of objects and want to remove items with the same attribute value
    Python creates a dict, where keys are value if attribute (bar in our case), values are object of the sequence.
    After that the dict is transformed back to list

    Note: in result we save the last from repeating elements (item2 in our case)!
"""


class Foo:
    def __init__(self, value):
        self.bar = value

item1 = Foo(15)
item2 = Foo(15)
item3 = Foo(5)

lst = [item1, item2, item3]

unique_lst = list({getattr(obj, 'bar'): obj for obj in lst}.values())

print(unique_lst)  # [item2, item3]
```

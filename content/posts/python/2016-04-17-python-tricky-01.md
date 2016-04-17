---
layout: post
title: Python Tricky-01
modified: null
categories:
  - python
image: 18.jpg
tags:
  - python
date: 2016-04-17T10:41:15.000Z
---

# Python Tricky

python tricky 是记录一些Python使用过程中一些神奇的小技巧.

## Argument Unpacking

一个argument unpacking的例子：

```python
def product(a, b):
    print("a is %d" % a)
    print("b is %d" % b)
    return a * b


argument_tuple = (1, 2)
argument_dict = {'a': 1, 'b': 2}
argument_list = [1,2]
# interesting for unpacking
print(product(*argument_list))
print(product(*argument_tuple))
print(product(**argument_dict))
```

python unpacking 这里指的是调用python函数的参数可以自动匹配：

- list: 顺序匹配函数参数，变量调用时以*开始
- tuple：顺序匹配函数参数，变量调用时以*开始
- dict: 根据key值来匹配，变量调用时以**开始

下面是一个可扩展unpacking的方式： `*`其实表示一个list

```python
"""allows collecting not explicitly assigned values into
a placeholder variable"""

a, *b, c = range(10)
print(a, b, c)

"""advanced example"""

[(c, *d, [*e]), f, *g] = [[1, 2, 3, 4, [5, 5, 5]], 6, 7, 8]
print(c, d, e, f, g)
```

## bool

python 中的bool有True or False，python2中的True 或者False都可以改变对应的值：

python中的True or False可以参加数学运算：

```python
a = 5
print(isinstance(a,int)+(a<10))
# interesting writing
print(["is odd","is even"][a % 2 ==0])
print("is even" if a % 2 ==0 else "is odd")
```

python中循环如果使用True会比使用1来的慢，不过一般肯定是使用True or False来做循环的：

```python
from timeit import timeit


def test_true():
    count = 100
    while True:  # Here is True
        if count < 0:
            break
        count = -1


def test_1():
    count = 100
    while 1:
        break
    count -= 1


print('use True: %s' %timeit(test_true, number=1000000))
print('use 1: %s' % timeit(test_1, number=1000000))
```

结果：

```
use True: 0.21380468501592986
use 1: 0.1610587630129885
```

## Property Cache

python 的property可以通过`__get__`来获取，同时可以在运行时添加，改变属性的值

```python
class PropertyCache:
    """ a decorator to cache property
    """

    def __init__(self, func):
        self.func = func

    def __get__(self, obj, cls):
        if not obj:
            return self
        value = self.func(obj)
        # Magic Here, there is property_to_be_cached property there
        setattr(obj, self.func.__name__, value)
        return value


class Foo:
    def __init__(self):
        self._property_to_be_cached = 'result'

    @PropertyCache
    def property_to_be_cached(self):
        print('compute')
        return self._property_to_be_cached

test = Foo()

print(test.property_to_be_cached)
print(test.property_to_be_cached)
print(Foo().property_to_be_cached)
```

这里通过一个装饰器：PropertyCache 来装饰property_to_be_cached，在调用property_to_be_cached时，其实是通过PropertyCache的__get__来获取，那么：

- value = self.func(obj) 就是通过调用Foo中的property_to_be_cached函数，value就是property_to_be_cached的返回值
- setattr(obj, self.func.**name**, value)： 就是将value付给了属性：property_to_be_cached，self.func.__name__ 其实就是property_to_be_cached

这是一个挺有意思的例子来说明了动态语言的一些magic的方法

## calculator

这里例子可以看出，python的函数的一些使用方法，函数也可以作为一种参数，活着变量

```python
import operator
ops = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul
}

x = input("Enter an operator [OPTIONS: +, -, *, /]: ")
y = int(input("Enter number: "))
z = int(input("Enter number: "))

# interesting to use function
print (ops[x](y, z))
```

## chained comparsion

```python
a = 10
print(1 < a < 50)
print(10 == a < 20)
```

## compile

python 可以通过`exec`可以直接运行组装起来的字符串，当然其实很多语言都可以的......

```python

import math  # using sin, cos and sqrt for example

''' Takes a code string and returns a ready-to-use function '''


def compile_(s):
    code = """def f(x):\n  return {}""".format(s)  # wrap the string as a function f(x)
    scope = {"sin": math.sin, "cos": math.cos, "sqrt": math.sqrt}  # define the scope for the code to use
    exec(code, scope)  # execute code inside the given scope
    # f(x) gets defined inside %vis%
    return scope["f"]  # now we only have to extract it and return


f = compile_("x**2 + 2*sin(x)")
print(f(10))
```

```python
"""exec can be used to execute Python code during runtime
variables can be handed over as a dict
"""
exec("print('Hello ' + s)", {'s': 'World'})
```

## sequence

sequence 其实是个list，如果遍历这个list，遍历时需要进行一些调用的话，那么下面例子提供了两个不同的方法.

```python
import operator


class Foo():
    def bar(self, *args, **kwargs):
        print('method bar works')


sequence = [Foo() for i in range(5)]

# in python3 map returns iterator so we must ask python to process elements by list()
# in python2 map(operator.methodcaller('bar'), sequence) works perfectly
list(map(operator.methodcaller('bar'), sequence))

# there is another way more understandable
[f.bar() for f in sequence]
```

## Conditional assignment

python 的if else的另外一种写法：

```python

b = True print(True if b else False)
b = None or False print(b)

"""calling different functions with same arguments based on condition"""
def product(a, b):     
  return a * b

def subtract(a, b):
  return a - b

b = True print((product if b else subtract)(1, 1))
```

## context manager

with 通过context manager来控制上下问，同时释放资源运行finally的内容

```python
"""Context managers are useful for automatically releasing resources once you are done with them."""

# common context manager that will close
# a file when it has been read
with open('README.md') as f:
    contents = f.read()

# make your own context manager
import contextlib


@contextlib.contextmanager
def unlock(resource):
    resource = "unlocked"
    try:
        yield resource
    finally:
        resource = "locked"


# a resource that is locked
resource = "locked"

# test that it is indeed locked
print(resource)

# call your 'unlock' context manager with your resource
with unlock(resource) as unlocked:
    print(unlocked)  # check that it is unlocked

# ensure it was re-locked when it left the 'unlock' context
print(resource)
```

## controll the whitespace

```python
"""control the whitespaces in string"""

s = 'The Little Price'

# justify string to be at least width wide
# by adding whitespaces
width = 20
s1 = s.ljust(width)
s2 = s.rjust(width)
s3 = s.center(width)
print(s1)   # 'The Little Price    '
print(s2)   # '    The Little Price'
print(s3)   # '  The Little Price  '

# strip whitespaces in two sides of string
print(s3.lstrip())  # 'The Little Price  '
print(s3.rstrip())  # '  The Little Price'
print(s3.strip())   # 'The Little Price'
```

## copy list

python 的copy 和deep copy，list 的copy python3中也可以copy嵌套的list内容

```python

a = [1, 2, 3, 4, 5]
print(a[:])

"""using the list.copy() method (python3 only)"""

a = [1, 2, 3, 4, 5]

print(a.copy())


"""copy nested lists using copy.deepcopy"""

from copy import deepcopy

l = [[1, 2], [3, 4]]

l2 = deepcopy(l)
print(l2)
```

## class as list

下面个例子有个一些很好玩的地方：

- namedtuple
- 两个列表正交产生集合

```python
self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
```

- `__getitem__` 在list的使用

例子：

```python
""" How to use dunder methods to add behavior to objects.
Here it's an example of how implement a french deck that can be used as a list"""

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class Deck:

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

card_a = Card('A', 'spades')
print(card_a)

deck = Deck()
len(deck)

print(deck[0])
print(deck[-1])
for card in deck:
    print(card)
```

## default value

python set default value for a dict

```python

""" builtin dict """
d = {}
d.setdefault('a', []).append(1)
d['b'] = d.get('b', 0) + 1

print(d)


""" with collections.defaultdict """
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)

print(d)
```

python get value with a default value

```python

d = {'a': 1, 'b': 2}

print(d.get('c', 3))
```

## sort dict

sort dictionary by its values

```python

""" Sort a dictionary by its values with the built-in sorted() function and a 'key' argument. """

d = {'apple': 10, 'orange': 20, 'banana': 5, 'rotten tomato': 1}
print(sorted(d.items(), key=lambda x: x[1]))


""" Sort using operator.itemgetter as the sort key instead of a lambda"""


from operator import itemgetter


print(sorted(d.items(), key=itemgetter(1)))


"""Sort dict keys by value"""


print(sorted(d, key=d.get))
```

## easy formating

python 字符串的formating，以下是python的几种方法,主要的思路其实就是：

- 字符串模版
- 外部变量使用dict的方式来填充相应的模版

```python

"""easy string formatting using dicts"""

d = {'name': 'Jeff', 'age': 24}
print("My name is %(name)s and I'm %(age)i years old." % d)

"""for .format, use this method"""

d = {'name': 'Jeff', 'age': 24}
print("My name is {name} and I'm {age} years old.".format(**d))

"""alternate .format method"""
print("My name is {} and I'm {} years old.".format('Jeff','24'))

"""dict string formatting"""
c = {'email': 'jeff@usr.com', 'phone': '919-123-4567'}
print('My name is {0[name]}, my email is {1[email]} and my phone number is {1[phone]}'.format(d, c))
```

## flatten a list

flatten a list 就是将有嵌套的list转化为一个扁平没有嵌套的list

```python

"""
Deep flattens a nested list

Examples:
    >>> list(flatten_list([1, 2, [3, 4], [5, 6, [7]]]))
    [1, 2, 3, 4, 5, 6, 7]
    >>> list(flatten_list(['apple', 'banana', ['orange', 'lemon']]))
    ['apple', 'banana', 'orange', 'lemon']
"""


def flatten_list(L):
    for item in L:
        if isinstance(item, list):
            yield from flatten_list(item)
        else:
            yield item

"""In Python 2
# from compiler.ast import flatten
# flatten(L)


# Flatten list of lists

a = [[1, 2], [3, 4]]

# Solutions:
"""
print([x for _list in a for x in _list])

import itertools
print(list(itertools.chain(*a)))

print(list(itertools.chain.from_iterable(a)))

"""
# In Python 2
# print(reduce(lambda x, y: x+y, a))
"""

print(sum(a, []))
```

## for else

```python

"""else gets called when for loop does not reach break statement"""
a = [1, 2, 3, 4, 5]
for el in a:
    print(el)
    if el == 0:
        break
else:
    print('did not break out of for loop')
```

## key default dict

key default dict, if there is not key existing, the default key would be the return of the default_factory

```python

"""
keydefaultdict with where the function receives the key.
"""
from collections import defaultdict


class keydefaultdict(defaultdict):
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        else:
            ret = self[key] = self.default_factory(key)
            return ret


def pow2(n):
    return 1 << n

d = keydefaultdict(pow2)
print(d[1])
print(d[3])
print(d[10])
print(d)
```

## switch alternatives

如何不写switch，下面是一个小小的参考：

```python

"""lightweight switch statement"""
a = {
    True: 1,
    False: -1,
    None: 0
}
print(a.get(False, 0))

"""works with functions as well"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


b = {
    '+': add,
    '-': subtract
}

print(b['+'](1, 1))
```

## join for the list

```python
"""converts list to comma separated string"""

items = ['foo', 'bar', 'xyz']

print (','.join(items))

"""list of numbers to comma separated"""
numbers = [2, 3, 5, 10]

print (','.join(map(str, numbers)))

"""list of mix  data"""
data = [2, 'hello', 3, 3.4]

print (','.join(map(str, data)))
```

## loop overlapping keys

python使用& 或者｜ 可以获取列表的交集或者合集

```python

"""loop over dicts that share (some) keys in Python2"""

dctA = {'a': 1, 'b': 2, 'c': 3}
dctB = {'b': 4, 'c': 3, 'd': 6}

for ky in set(dctA) & set(dctB):
    print(ky)

"""loop over dicts that share (some) keys in Python3"""
for ky in dctA.keys() & dctB.keys():
    print(ky)

"""loop over dicts that share (some) keys and values in Python3"""
for item in dctA.items() & dctB.items():
    print(item

"""
the all keys(without duplication) in two dicts
"""
print(dctA.keys() | dctB.keys())
```

metatable: 例子实际上就是一个defaultkeydict

```python
# -*- coding: utf-8 -*-
"""
metatable with where the function receives the dictionary and key.
"""
from collections import defaultdict


class metatable(defaultdict):
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        else:
            ret = self[key] = self.default_factory(self, key)
            return ret


def fib(d, n):
    if n == 0 or n == 1:
        return n
    return d[n - 1] + d[n - 2]


d = metatable(fib)
print(d[1])
print(d[3])
print(d[10])
print(d)
```

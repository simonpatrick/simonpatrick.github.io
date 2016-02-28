---
layout: post
title: "Simple Sorting in Python And Ruby"
modified:
categories: [python,ruby]
excerpt:
tags: [python,ruby]
image:
  feature:
date: 2014-08-24T10:31:11+08:00
---
不同语言的排序

## Python

```python
a=[5,3,2,2,90,12]
sorted(a)
sorted(a,reverse=True)
a.sort()
a.sort(reserve=True)

f = ['abcd','CCCC']
sorted(c,key=len)
sorted(c,key=str.lower)
sorted(c,key=lastchar)

f = [{'name':'abc','age':20},{'name':'def','age':30}]
def age(s):
  return s['age']

ff=sorted(f,key=age)
f2=sorted(f,key=lambda x:x['age'])
```

## Ruby

```ruby
a = [ "d", "a", "e", "c", "b" ]
a.sort                    #=> ["a", "b", "c", "d", "e"]
a.sort { |x,y| y <=> x }  #=> ["e", "d", "c", "b", "a"]
a.sort { |x,y| x <=> Y }  #=> ["a", "b", "c", "d", "e"]

a = [ "d", "a", "e", "c", "b" ]
a.sort!                    #=> ["a", "b", "c", "d", "e"]
a.sort! { |x,y| y <=> x }  #=> ["e", "d", "c", "b", "a"]
```

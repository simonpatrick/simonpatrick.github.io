---
layout: post
title: "python-borg-design-pattern"
modified:
categories: [designpattern,python]
image: 17.jpg
tags: [designpattern,python]
date: 2016-01-11T23:05:26
---

Python Design Pattern: Borg

## Borg
Borg 模式实际上就是一个类的多个实例共享一个相同的状态.
简单的代码实现如下：

```python
__author__ = 'patrick'


class Borg:
    _share_state = {}

    def __init__(self):
        self.__dict__ = self._share_state
        self.state = 'Init'

    def __str__(self):
        return self.state


class YourBorg(Borg):
    pass


if __name__ == '__main__':
    rm1 = Borg()
    rm2 = Borg()
    rm1.state = 'Idle'
    rm2.state = 'Running'

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))

    rm2.state = 'Zombie'

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))

    print('rm1 id: {0}'.format(id(rm1)))
    print('rm2 id: {0}'.format(id(rm2)))

    rm3 = YourBorg()

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))
    print('rm3: {0}'.format(rm3))

```

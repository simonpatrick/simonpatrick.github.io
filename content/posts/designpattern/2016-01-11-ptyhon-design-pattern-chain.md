---
layout: post
title: "ptyhon design pattern: chain of responsibility"
modified:
categories: [designpattern,python]
image: 16.jpg
tags: [designpattern,python]
date: 2016-01-11T23:35:45
---

python 的责任链模式.

***方法链：***

上代码吧： 其实就死return 了一个self，java里面可能是this

``` python

class Person(object):
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def do_action(self):
        print(self.name, self.action.name, end=' ')
        return self.action


class Action(object):
    def __init__(self, name):
        self.name = name

    def amount(self, val):
        print(val, end=' ')
        return self

    def stop(self):
        print('then stop')


if __name__ == '__main__':
    move = Action('move')
    person=Person('Jack',move)
    person.do_action().amount('5m').stop
```

***责任链:***

这是一个责任链的模式，一个handler叠加，下例中：
ConcreteHandler1->ConcreteHandler3->ConcreteHandler2->DefaultHandler,
那么如果第一个request满足了ConcreteHandler1的条件，就结束了，如果没有怎尝试ConcreteHandler3，知道满足了就退出.
这样就把一大批if else 转化成不同的handler了.

```python
class Handler:
    def __init__(self, successor):
        self._successor = successor;

    def handle(self, request):
        i = self._handle(request)
        if not i:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError('Must provide implementation in subclass.')


class ConcreteHandler1(Handler):
    def _handle(self, request):
        if 0 < request <= 10:
            print('request {} handled in handler 1'.format(request))
            return True


class ConcreteHandler2(Handler):
    def _handle(self, request):
        if 10 < request <= 20:
            print('request {} handled in handler 2'.format(request))
            return True


class ConcreteHandler3(Handler):
    def _handle(self, request):
        if 20 < request <= 30:
            print('request {} handled in handler 3'.format(request))
            return True


class DefaultHandler(Handler):
    def _handle(self, request):
        print('end of chain, no handler for {}'.format(request))
        return True


class Client:
    def __init__(self):
        self.handler = ConcreteHandler1(ConcreteHandler3(ConcreteHandler2(DefaultHandler(None))))

    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)


if __name__ == "__main__":
    client = Client()
    requests = [2, 5, 14, 22, 18, 3, 35, 27, 20]
    client.delegate(requests)
```

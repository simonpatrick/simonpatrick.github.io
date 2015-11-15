---
layout: post
title: "Python 中String的格式化"
modified:
categories: [python]
excerpt:
tags: [python]
date: 2015-11-15-15:12:56
---

python中对于string有些挺有意思操作,现在把他记录如下：

```python
output = 'Hello {0}!'.format('World!')
output1 = 'Hello {0} {1} !'.format('Mr.','World!')
output2 = 'Hello {name} !'.format(name='World')


print(output)
print(output1)
print(output2)
```

以上可读性最好的，个人认为是:

```python
output2 = 'Hello {name} !'.format(name='World')
```

## 时间，urlparser的一起使用

```python
print('It\'s {0:%H:%M}'.format(datetime.today()))
url = urlparse('http://pocoo.org/')
print('{0.netloc} [{0.scheme}]'.format(url))
```

结果：

```python
It's 15:16
pocoo.org [http]
```

是不是很方便的.

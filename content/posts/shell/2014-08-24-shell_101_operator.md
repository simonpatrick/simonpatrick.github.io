---
layout: post
title: "Shell Learning - 操作符号"
modified:
categories: [shell]
excerpt:
tags: [shell]
image: 14.jpg
date: 2014-08-24T10:31:11+08:00
---

摘自：[http://wklken.me/posts/2014/01/12/shell-script-base.html](http://wklken.me/posts/2014/01/12/shell-script-base.html)

### 计算

```bash
#!/bin/bash
no_1=4
no_2=5
let result=no_1+no_2

let result--
echo $result
let result++
echo $result

# expr(漏洞之源？？)

result=`expr 3+4`
echo $result
result=`expr $no_1+345`
echo $result
result=$[ no_1 + no_2 ]
echo $result
result=$[ $no_1 + 5 ]

echo $result
result=$(( no_1 + 5 ))
echo $result

# result:
8
9
3+4
4+345
9
9
9
```

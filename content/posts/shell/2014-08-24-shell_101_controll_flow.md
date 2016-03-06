---
layout: post
title: "Shell Learning - Control Flow"
modified:
categories: [shell]
excerpt:
tags: [shell]
image: 12.jpg
date: 2014-08-24T10:31:11+08:00
---

### if/test 条件测试

```bash
#!/bin/bash

a=34
if test $a = 4
then
  echo true
else
  echo false
fi

if [ $a -eq 34 ]
then
  echo true
else
  echo false
fi

#Result:
h controll_flow.sh
false
true
```

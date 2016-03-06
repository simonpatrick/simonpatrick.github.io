---
layout: post
title: "Shell Learning - Variant 变量"
modified:
categories: [shell]
excerpt:
tags: [shell]
image: 16.jpg
date: 2014-08-24T10:31:11+08:00
---

摘自：[http://wklken.me/posts/2014/01/12/shell-script-base.html](http://wklken.me/posts/2014/01/12/shell-script-base.html)

### 变量赋值

```bash
#!/bin/bash
var=value
echo $var
var='the value'
echo $var
var="the $PARAM"
echo $var
echo $var
echo `pwd`
echo $(pwd)

#result:
╰─[:)] % sh shell_variant.sh
value
the value
the
the
/Users/patrick/workspace/works/shell_learning
/Users/patrick/workspace/works/shell_learning
```

### 变量分类
四种变量：环境变量、本地变量、位置变量、特定变量参数

    * 环境变量可作用于所有子进程
    * 本地变量在用户现在的shell 生命期的脚本中使用，仅存在于当前进程
    * 位置变量：作为程序参数
    * 特定变量：特殊作用

### 环境变量

```bash
    设置
    MYVAR="test"
    expirt MYVAR
    or
    export MYVAR="test"

    只读
    MYVAR="test"
    readonly MYVAR
    or
    readonly MYVAR="test"

    显示
    export -p
    env #查看所有环境变量
    $MYVAR #获取

    消除
    unset MYVAR
```
### 本地变量

```bash
设置
LOCAL_VAR="test"
or
LOCAL_VAR="test"
readonly LOCAL_VAR #设置只读

还可以使用declare命令定义
```

### 位置变量

- $0 脚本名称
- $# 传递到脚本参数个数
- $$ shell脚本运行当前进程ID
- $? 退出状态
- $N N>=1，第n个参数

```bash
#!/bin/bash

echo $#
echo $0
echo $1 $2
echo $$

# result:
2
read_parameter.sh
1 2
24171
```

### 字符串处理

- ``` ${#VARIABLE_NAME}``` 可以给出字符串的长度

``` bash

echo $#
echo $0
echo $1 $2
echo $$

p=$2
echo $p

if [ ${#p} != 2 ]
then
  echo "wrong input"
fi

# Result

h read_parameter.sh 1 2
2
read_parameter.sh
1 2
24217
2
wrong input
```

### 拼接字符串
```bash
echo "$x$y"
```

### 字符串切片

${变量名:起始:长度}得到子字符串

```bash
$ test='I love china'
$ echo ${test:5}
e china
$ echo ${test:5:10}
e china

str="hello world"
echo ${str:6}  # ${var:offset:length}
```

### 字符串替换

${变量/查找/替换值}

一个“/”表示替换第一个，”//”表示替换所有,当查找中出现了：”/”请加转义符”\/”表示

```bash
echo ${str/foo/bar} #首个
echo ${str//foo/bar} #所有
```

### 正则匹配

```bash
if [[ $str =~ [0-9]+\.[0-9]+ ]]
```

### 数值处理

自增

``` bash
a=1
a=`expr a + 1`

or

a=1
let a++
let a+=2
let

no1=4
no2=5
let result=no1+no2
expr

result=`expr 3 + 4`
result=$(expr $no1 + 5)
```

### 其他

```bash
result=$[ no1 + no2 ]
result=$[ $no + 5 ]

result=$(( no1 + 5 ))
浮点数

echo "4 * 0.56" | bc
设定精度
echo "scale=2;3/8" | bc
进制转换
echo "obase=2;100" | bc
平方
echo "sqrt(100)" | bc
数组和map
```

---
layout: post
title: "Shell Learning - Scripting"
modified:
categories: [shell]
excerpt:
tags: [shell]
image:
  feature:
date: 2014-08-24T10:31:11+08:00
---


## Shell Script sample

``` bash
    #!/bin/bash
    # do somthing
```

## Run Shell Script

``` bash
sh script.sh
chmod a+x script.sh
./script.sh
```

```bash
cmd1;cmd2
# or
cmd1
cmd2
```
## echo

```bash
echo "welcome to bash"
ehco welcome to bash
```
不对单引号求值：
```bash
╰─[:)] % echo '$test'
$test
```
换行：
```bash
╰─[:)] % echo "test\ntest"
test
test
```
打印颜色：

    文字颜色码
        重置0
        黑色30
        红色31
        绿色32
        黄色33
        蓝色34
        洋红35
        青色36
        白色37

    echo -e "\e[1;31m This is red test \e[0m"

    背景颜色码
        重置0
        黑色40
        红色41
        绿色42
        黄色43
        蓝色44
        洋红45
        青色46
        白色47

    echo -e "\e[1;42m Green Background \e[0m"

### printf

```bash
printf "hello world"
printf "%-5s %-10s %-4.2f\n" 3 Jeff 77.564
3     Jeff       77.56
```

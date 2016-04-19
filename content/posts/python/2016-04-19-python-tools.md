---
layout: post
title: 'Python Tools- unittest,pip,pylint'
modified: null
categories:
  - python
image: 21.jpg
tags:
  - python
date: 2016-04-19T10:41:15.000Z
---

# Python Tools

以下内容是Writing Solid Python Code-91 suggestions to improve your python program的 读书笔记。下面是关于第七章，使用工具辅助项目开发的笔记，这里提到了如下工具：

- pip/yolk
- setuptools
- paster
- nose
- flask-pypi-proxy
- pylint
- pyreverse

## PIP

pip 是用来安装python第三方包，管理python第三包的工具。pip常用的方法有：

```shell
Usage:
  pip <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  list                        List installed packages.
  show                        Show information about installed packages.
  search                      Search PyPI for packages.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion
  help                        Show help for commands.

General Options:
  -h, --help                  Show help.
  --isolated                  Run pip in an isolated mode, ignoring
                              environment variables and user configuration.
  -v, --verbose               Give more output. Option is additive, and can
                              be used up to 3 times.
  -V, --version               Show version and exit.
  -q, --quiet                 Give less output.
  --log <path>                Path to a verbose appending log.
  --proxy <proxy>             Specify a proxy in the form
                              [user:passwd@]proxy.server:port.
  --retries <retries>         Maximum number of retries each connection
                              should attempt (default 5 times).
  --timeout <sec>             Set the socket timeout (default 60.0
                              seconds).
  --exists-action <action>    Default action when a path already exists:
                              (s)witch, (i)gnore, (w)ipe, (b)ackup.
  --trusted-host <hostname>   Mark this host as trusted, even though it
                              does not have valid or any HTTPS.
  --cert <path>               Path to alternate CA bundle.
  --client-cert <path>        Path to SSL client certificate, a single file
                              containing the private key and the
                              certificate in PEM format.
  --cache-dir <dir>           Store the cache data in <dir>.
  --no-cache-dir              Disable the cache.
  --disable-pip-version-check
                              Don't periodically check PyPI to determine
                              whether a new version of pip is available for
                              download. Implied with --no-index.
```

这里其实已经非常清楚的表示了pip的用法，比如安装：

```shell
pip install requests
```

比如卸载：

```shell
pip uninstall requests
```

比如生成requirement 文件

```shell
pip freeze -requirements.txt
```

如果想获得每一个命令的的详细帮助，则：

```shell
pip freeze -h
```

## python 单元测试和nose

单元测试的目的：

- 提高代码质量，减少潜在bug
- 减少修复成本
- 集成测试保证

有效的单元测试：(只是读书笔记)

- 测试先行
- 编写用例，准备数据
- 测试脚本
- 编写被测代码
- 修改代码，通过单元测试

单元测试基本原则：

- 一致性
- 原子性
- 单一职责：基于场景
- 隔离性

单元测试相关概念：

- 测试固件(test fixture)
- 测试用例(test case)
- 测试用例集(test suite)
- 测试运行器(test runner)

以下是一个python的单元测试例子：一个add函数

```python
# 单元测试
class TestCalculator(TestCase):

    def setUp(self):
        self.calculator=Calculator()

    def test_add(self):
        result = self.calculator.add(1,2)
        self.assertEqual(result,3)

    def test_add_string(self):
        result= self.calculator.add('1','sd')
        self.assertEqual(result,'1sd')

    def test_add_list_exception(self):
        with self.assertRaises(TypeError) as context:
            result=self.calculator.add(['12','2'],'dd')
        print(context)
        self.assertEqual(TypeError,type(context.exception))
```

补上add实现：

```python
class Calculator(object):
    def __init__(self):
        pass

    def add(self, a, b):
        return a+b
```

这样一个简单的单元测试例子就完成了，当然实际使用要比这个负责的多的多.

## pylint

pylint 主要是用来进行代码风格的检查：

- 代码风格审查
- 代码错误检查
- 重复或者设计不合理代码

pylint中集成了pyreverser，可以生成uml图，pylint的安装如下：

```python
pip install pylint
```

使用pylint：

```shell
pylint sample.py
```

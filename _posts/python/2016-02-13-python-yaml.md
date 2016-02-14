---
layout: post
title: "python yaml 使用介绍"
modified:
categories: [python]
excerpt:
tags: [python]
date: 2016-02-13-18:38:43
---

# Python YAML 应用

YAML由于其可读性，越来越多的地方用它来做配置文件了来代替XML文件.下面就是用来介绍如何使用PYTHON来进行YAML的操作.
读取yaml或者写yaml，主要是用的是两个方法：

- load 读
- dump 写

## Read YAML to List

以下是读YAML 内容到python的list

```PYTHON
import yaml
def load_list():
    content = """
        - config
        - domain
        - repository
    """
    return yaml.load(content)
```

## Read YAML TO DICT

load yaml to dict or a nest dict:

```python
import yaml

def load_dict():
  content = """
      hello1: test
      hello2: test2
  """
  return yaml.load(content)


def load_all_dict():
  contents = """
    hero:
      hp: 34
      sp: 8
      level: 4
    orc:
      hp: 12
      sp: 0
      level: 2
  """
  return yaml.load(contents)

print(load_dict())
print(load_all_dict())
```

## Read YAML: auto type conversation

yaml 对于格式要求比较严格的，： 后面注意加空格，同时python的原始类型通过load函数可以自动转化的.

```python
import yaml

def load_with_type():
    contents = """
        none: [~,null]
        bool: [true,false,on,off]
        int: 42
        float: 3.1415
        list: [test1,test2,test3]
        dict: {name: simon,sp: 5}
    """

    return yaml.load(contents)

print(load_with_type())

## result:
{'dict': {'name': 'simon', 'sp': 5}, 'none': [None, None], 'int': 42, 'bool': [True, False, True, False], 'list': ['test1', 'test2', 'test3'], 'float': 3.1415}
```

## Dump YAML: write contents to a yml file

使用dump函数直接可以将dict 内容写入到yml文件，这里有两个参数：
- default_flow_style: 设为false之后就```first_name: simon``` 这种格式了
- default_style: 设为‘“’, first_name 就会加上“”

```python
def dump_file():
    contents = {
        'name': 'test',
        'first_name': 'simon',
        'last_name': 'kevin'
    }
    # return yaml.dump(contents)
    with open('document.yaml', 'w') as f:
        return yaml.dump(contents, f, default_flow_style=False, default_style='"')

# file result:
"first_name": "simon"
"last_name": "kevin"
"name": "test"

```

## 复杂一点的YAML格式

下面一个yaml文件表示了一个JAVA maven项目里面主要的一些目录

```java
      main:
        - config
        - domain
        - repository
        - service
        - rest:
          - controller
          - dto
          - exception
        - exceptions
        - utils
      resources:
        - config
      test:
        - config
        - domain
        - repository
        - service
        - rest:
          - controller
          - dto
          - exception
        - exceptions
        - utils
```

读取此文件的python代码：

```python

def read_yaml_file():
    with open('springboot-folders.yml', 'r') as f:
        result = yaml.load(f)

    return result
folders = read_yaml_file()
print(folders['main'])
print(folders['test'])
print(folders['resources'])

# result:
['config', 'domain', 'repository', 'service', {'rest': ['controller', 'dto', 'exception']}, 'exceptions', 'utils']
['config', 'domain', 'repository', 'service', {'rest': ['controller', 'dto', 'exception']}, 'exceptions', 'utils']
['config']

```

以上已经非常清楚的表示了如何读取yml文件了， 至此简单的yml的使用介绍就到此为止. 更加详细的介绍请参考：
[python yaml](http://pyyaml.org/wiki/PyYAMLDocumentation)

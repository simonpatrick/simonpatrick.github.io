---
layout: post
title: "简单面试题：统计字符串中的相同字符数量"
modified:
categories: [interview]
excerpt:
tags: [interview]
date: 2016-02-28-10:41:15
---

有时测试的面试题中会考点编程的内容，比如统计字符串中的相同字符数量，具体题目如下：

- 给定一个字符串，如MIssissippi
- 计算字符串中每一个不同字符出现的数量

## Python 的解法

```python
letter_count={}
for letter in 'MIssissippi':
  letter[letter]=letter_count.get(letter,0)+1
print(letter_count)
```

运行结果：

```
{'s': 4, 'M': 1, 'i': 3, 'I': 1, 'p': 2}
```

## Java 的解法

JAVA 8 中给Map加入了getOrDefault的方法，下面就分别介绍一下JAVA8之前和使用JAVA8的方法：

- JAVA8 之前：

```java
public Map<String,Integer> countCharacters(String source){
       char[] chars = source.toCharArray();
       Map<String,Integer> result = new HashMap<>();

       for (char aChar : chars) {
           Integer existing_counter = result.get(String.valueOf(aChar));
           int counter =  existing_counter==null?0:existing_counter;
           result.put(String.valueOf(aChar),counter+1);
       }
       return result;
   }
```

- JAVA8

```java
public Map<String,Integer> countCharacters_JAVA8(String source){
    char[] chars = source.toCharArray();
    Map<String,Integer> result = new HashMap<>();
    for (char aChar : chars) {
        result.put(String.valueOf(aChar),result.getOrDefault(String.valueOf(aChar),0)+1);
    }
    return result;
}
```

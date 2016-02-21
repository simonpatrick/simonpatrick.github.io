---
layout: post
title: "Python 面试题"
modified:
categories: [python,java,interview]
excerpt:
tags: [python,java,interview]
image:
  feature:
date: 2015-10-22T10:31:11+08:00
---

测试有的时候出去会遇到一些编程面试题,以下是用python来解决两个简单面试题.

## 倒转字符串中的单词的排列
给定字符串“Hello World!”,经过一段程序运行之后,得到输出结果“World! Hello”,也就是以单词
为单位,倒转输入“Hello World!”

- python解法: 不考虑编码格式

```python
words = "Hello World!"
print(" ".join(reversed(words)))
print(" ".join(words.split(" ")[::-1]))
```
- Java 解法

```java
public class ReverseWords {

    public static String reverseWords(String input){
        String[] words = input.split(" ");
        StringBuilder sb = new StringBuilder();
        for (int i = words.length-1; i >=0 ; i--) {
            sb.append(words[i]);
            sb.append(" ");
        }

        return sb.toString().trim();
    }

    public static void main(String[] args) {
        System.out.println(reverseWords("Hello World!"));
    }
}
```

## 输出斐波那契数列

根据给定的值,输出相同数目的斐波那契列， 如如果给定是1， 则输出1;给定2,输出1,1;
给定3，输出1,1,2, 依次类推。

- python 解法

```python
def f(n):
    if n <= 0:
        return 0
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    nums = [1, 1]
    temp1 = 1
    temp2 = 1
    for i in range(n - 2):
        append_num = temp1 + temp2
        nums.append(append_num)
        temp1,temp2=temp2,append_num

    return nums

print(f(3))
print(f(5))
print(f(10))
```

- java 解法

```java
public static String getFibListByNum(int n){
    if (n<=0) throw new RuntimeException("invalid input");
    if(n==1) return "1";
    if(n==2) return "1,1";
    int temp1=1;
    int temp2=1;
    String result = "1,1";
    for (int i = 3; i <=n ; i++) {
        int appendNum = temp1+temp2;
        temp1=temp2;
        temp2=appendNum;
        result=result+","+appendNum;
    }

    return result;
}
```

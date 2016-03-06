---
layout: post
title: "Refactoring-1-Encapsulate Collection"
modified:
categories: [refactoring]
image: 2.jpg
tags: [refactoring]
date: 2015-10-26T10:31:11+08:00
---

关于重构的第一篇，后续会在这个话题继续讨论

## What is Encapsulate Collection

```
In certain scenarios it is beneficial to not expose a full collection to consumers of a class. Some of these circumstances is when there is additional logic associated with adding/removing items from a collection. Because of this reason, it is a good idea to only expose the collection as something you can iterate over without modifying the collection. Let’s take a look at some code
```

这种重构方式主要是将直接操纵集合类的操作直接暴露出简单的函数，同时修改函数名到
更有意义的名字

## Code Sample

```java
public class Order {
  private List<Item> itemList = Lists.newArrayList();

  public void addItem(Item item){
      itemList.add(item);
  }

  public void removeItem(final Item item){
      itemList.remove(item);
  }

  public void removeItems(List<Item> items){
      itemList.removeAll(items);
  }

  public int total(){
      return itemList.size();
  }

  public int distinctItemCount(){
      int result=0;
      List<String> itemNames=Lists.newArrayList();
      Set<String> names = Sets.newHashSet();
      itemList.stream().forEach(element ->
              names.add(element.getName()));
      return names.size();
  }
}  
```

## 关于有什么好处的思考

考虑一下如上的写法有哪些好处呢？个人觉得：

－ 将一些集合操作整合成函数，减少每个人不同写法出错
－ 将集合操作编程有意义的业务函数，提高了代码业务层的可读性

---
layout: post
title: "True Stories: 有趣的函数"
modified:
categories: [truestories]
excerpt:
tags: [truestories]
image: 26.jpg
date: 2015-10-24T10:31:11+08:00
---

## 有趣的函数

下面是一些有趣而真实的函数，自己的感受是：

- 此刻的想法是复杂的
- 不敢想象
- 这是认真的吗?
- 为什么会这样?
- 如果4个key－value对是不是还要再写函数？
- 这样的代码放在Controller层？你是认真的吗？

测试有时真的很难改变什么,这样的代码其实已经无力吐槽了.

```java
    //    json方法
    public String json(Map<String,Object> map){
        JsonString jsonString = new JsonString();
        Set<String> set = map.keySet();
        for (String key : set) {
            //spring内置的对象去掉
            if (key.contains("org.springframework")) {
                continue;
            }
            jsonString.put(key, map.get(key));
        }
        return jsonString.toString();
    }

    public String json(Model model){
        return json(model.asMap());
    }

    public String json(String key, Object value){
        return new JsonString().put(key, value).toString();
    }

    public String json(String key, Object value,String key2, Object value2){
        return new JsonString().put(key, value).put(key2,value2).toString();
    }

    public String json(String key, Object value,String key2, Object value2,String key3, Object value3){
        return new JsonString().put(key, value).put(key2,value2).put(key3, value3).toString();
    }

```

## 自己的思考

- JOSN转换方法不应该放到Controller层
- 这几个json的函数其实没有必要,完全可以通过
- 使用了keySet,再使用map.get(key) 有点浪费，应该直接使用Map.Entry
- Map 转Json应该直接使用第三方库
- 不理解org.springframework的东西怎么会到Map里面？

```java
new JsonString().put(key,value).put(key,value).toString();
```
来获得，完全没有必要写这些函数，这些函数基本上和上面代码没有区别.

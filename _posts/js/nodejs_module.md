---
layout: post
title: "NodeJS - Module"
modified:
categories: [js]
excerpt:
tags: [js]
image:
  feature:
date: 2012-09-24T10:31:11+08:00
---

NodeJS Module 简单使用

## require
require 是用来加载模块

```Javascript
var foo1= require('./foo')
```

## exports
当前模块的导出对象
```js
 exports.hello=function(){
    console.log('Hello world!');
 }
```

调用导出对象的方法：

``Javascript
var hello = require('./hello');
hello.hello();
```

从调用的方法来看，module的使用是不是很像java的工厂模式？

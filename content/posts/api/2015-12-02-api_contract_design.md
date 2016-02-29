---
layout: post
title: "True Stories: 从API的URL定义想到的"
modified:
categories: [truestories]
excerpt:
tags: [truestories]
date: 2015-12-02T13:26:07
---

关于REST API接口的设计没有了解太多，不过实际的测试中看到一些这样设计的接口资源路径URL，自己感觉就是怪怪的，
感觉这样的接口URL总是哪里不太对劲，所以自己就分析了一下：

```
http://domain.org/api/v4/＊＊/coursePassed/{appCode}/{courseId}/{userCode}
```

自己的思考是感觉这个东西不是很理想，无法通过一个路径了解大概是个什么事情，自己的感觉或许这样会更清楚一点

```
http://domain.org/api/v4/app/{appCode}/user/course/{courseId}
```

感觉这样的URL说清楚了：

－ 哪个APP
－ 是用户的course的状态
－ usercode可能不需要，应为已经使用了oAuth认证了

通过这样的命名的话，如果想获取一个用户所有的course的状态，或许就是：

```
http://domain.org/api/v4/app/{appCode}/user/course/
```
而我加上user的目的是表示这个是用户的课程考核状态，而不是course本身的状态。

原来的URL里面coursePassed上太具体了，可能本来这个接口其实是获取course的考核状态，如果写上这个coursePassed的话，或许只能返回true or false了，是不是有点太具体了，实际的实现和扩展非常有可能和这个有区别，而且如果有时需要一个接口提供的知识course考核的状态，那么难道再写一个API的接口来给状态，如果不是，那么coursePassed叫法就是值得商量的.

然后自己查了一下关于REST API设计原则的文章:

- [rest api](http://www.ruanyifeng.com/blog/2014/05/restful_api.html)

虽然没有直接说明如何设计，但是看完之后我自己觉得我的想法没有太大错误.感觉好的原则就是应该合乎一个常理的，通顺的，有上下文逻辑的.

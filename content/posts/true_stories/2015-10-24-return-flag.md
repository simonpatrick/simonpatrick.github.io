---
layout: post
title: "True Stories: About Return Flag"
modified:
categories: [truestories]
excerpt:
tags: [truestories]
image: 27.jpg
date: 2015-10-24T10:31:11+08:00
---

## Return Flag

真实的一段代码片段：

```java

public boolean update(Inquiry inquiry) {
    boolean bUpdBaseInf = super.update(inquiry);
    solrService.syncUpdate(new SolrInquiry(inquiry.getInquiryId()));
    return bUpdBaseInfo;
}

```

自己的思考：

- 这个返回的状态值没有完全体现整个函数的状态
- 如果solrService是个异步还可以理解这个返回值，但是名字是syncUpdate
  直接是不是应该怀疑这是个异步更新？
- solr的更新真的需要同步吗？solr的更新可能直接影响到整个业务的处理了......
- 这里也许是留了点坑关于这个flag的
- 这个flag的命名是不是有点那个啥?


## 代码REVIEW 流程的思考

这样的代码,个人觉得代码REVIEW是需要检查出来的。也许这样的代码永远也不会出现问题，但是他的味道就是不好。
就算我是一个测试，也看出这里面不严谨的地方了,很多时候我们总是讲流程,流程，流程，但是有了流程又怎么样呢？

一个好的技术团队是有他自己的品味的.呆过技术很好的公司,也呆过技术比较一般的公司,比较不同类别公司的开发，
很好的公司的开发更加注重这些细节,你可能觉得他们其实都在写差不多的代码,但是这种细节的常年累积,一个产品是否好维护就会出现很明显的差距了.
不容易维护的产品,有时可能已经资不抵债了.

如果想的更远一点的话,关于开发经常说到的工作无聊没有挑战的话题，
好公司的开发说的工作无聊和一般公司一些开发说的工作无聊可能是两个不同层次的无聊。
有些知道确实没有挑战而有些只是不知道其实自己写的代码挺烂的而已。我无意攻击任何人只是说说我真实的想法。

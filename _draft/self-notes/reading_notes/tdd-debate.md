# 关于TDD的讨论

## Reading Sources
- [TDD并不是看上去的那么美](http://coolshell.cn/articles/3649.html)
- []

## Essense of TDD

用例即规范(Specification By Example), TDD 强调用例来表达需求，对外接口的设计,或者是内部的某个功能描述内容.

![img](http://images.cnblogs.com/cnblogs_com/weidagang2046/feedback_cycle.jpg)

## TDD的争论

关于TDD的争论，更多的是在讨论方法论上面，但是无论如何，现在我们都不能忽略他的一个本质，就是测试是重要的，他不是一个
在产品之外的东西，他是一个保证产品不走样，保证产品他本身就是产品的一部分的东西.

个人认为软件开发的一个最核心的观点就是Don't Repeat Yourself, 如果使用人工调试来确认问题的话，他就是一种反Don't
repeat yourself的原则，相信他是一个不好的实践.

开发一个新产品只是软件开发中的一小部分时间，更多的时候是如何维护一个产品. 那么如何有效率的维护一个产品呢？个人的见解就是：
- 累积你的发现和所做过的事情，累积分两类
  * 你的作品，这个就是你的代码
  * 你做过的实验，你做过的测试，验证，这是你的单元测试，集成测试代码

# TDD  概念

TDD,Test Driven Testing,测试驱动开发，他描述的是软件开发的一种方法。无论TDD是否可以在实际项目中使用，他都强调了测试的重要性。
对于一个测试人员来说，这种方式实际上时可以了解了解的。在现实中很多被项目进度压的抬不起头的开发，一听到单元测试就直摇头
觉得根本没有时间做，而TDD去说，我们应该让测试先开始，很显然TDD落地实际上非常困难的。那么TDD说的是什么呢？

## TDD

- 测试驱动，测试－编码－重构
- ATDD, Accept Test Driven Development 验收测试
- TDD tools-xUnit,ATDD integration Testing framework,CI/CD

## TDD 概念和模式

- 测试驱动基本原则
- 测试夹具
- 测试替身，mock，stub
- 机遇状态和交互
- 设计模式提高可测性,composition over inheritance, less static methods, singleton,DI
- Unit Testing: assertion,fixture,test pattern


## Different TDD Solution
- TDD in WEB MVC,JAVA Servlet
- TDD in Database: Spring JDBC Template,Hibernate TDD
- TDD in unpredicatable functionality: TIME, LOGGING
- TDD in Multiple Threads
- TDD in MVP


## ATDD
- Fitness
- ColumnFixture
- RowFixture
- ActionFixture
- SetupFixture


## 关于单元测试的想法

单元测试对于提高系统的可维护性还是有不错的作用的，至少可以在较短的时间内知道自己的改动是否有明显的破坏了其他代码。
单元测试就想功能一样都是累积的作用，就想银行的复利一样，短期内你看着没效果，长期看可能不得了.

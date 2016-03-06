---
layout: post
title: "TestNG 报告定制最简单的原理"
modified:
categories: [automation]
excerpt:
tags: [automation]
image: 5.jpg
date: 2015-09-24T10:31:11+08:00
---

如果需要定制TestNG的测试报告,可以先想一下首先需要什么的数据,其实最简单的数据就是测试用例成功失败的数据,
那么实际上TestNG提供了ITestListener的接口可以让你获取这些测试数据.
同时IReporter 接口可以让用户在调用最后自己生成测试报告.

所以其实只要用一个类实现ITestListener,IReporter就可以了.

## ITestListener,IReporter实现
一下是我一个最简单的实现, 实际上TestNG开放出来的这些监听器,主要是让你可以获取TestNG 测试容器中运行测试的数据,上下文.
关于代码里面的ITestResult, xmlSuites,suites 可以自行查找

```java
public class TestNGSimpleReport implements ITestListener, IReporter {
    private List<String> testPassed = Lists.newArrayList();
    private List<String> testFailed = Lists.newArrayList();
    private List<String> testSkipped = Lists.newArrayList();

    @Override
    public void generateReport(List<XmlSuite> xmlSuites, List<ISuite> suites,
                               String outputDirectory) {
        System.out.println("Passed Case: " + testPassed.size());
        System.out.println("testFailed Case: " + testFailed.size());
        System.out.println("testSkipped Case: " + testSkipped.size());

        for (String passed : testPassed) {
            System.out.println("passed case:" + passed);
        }
        for (String passed : testFailed) {
            System.out.println("failed case:" + passed);
        }

        for (String passed : testSkipped) {
            System.out.println("skipped case:" + passed);
        }

    }

    @Override
    public void onTestStart(ITestResult result) {

    }

    @Override
    public void onTestSuccess(ITestResult result) {
        testPassed.add(result.getMethod().getMethodName());
    }

    @Override
    public void onTestFailure(ITestResult result) {
        testFailed.add(result.getMethod().getMethodName());
    }

    @Override
    public void onTestSkipped(ITestResult result) {
        testSkipped.add(result.getMethod().getMethodName());
    }

    @Override
    public void onTestFailedButWithinSuccessPercentage(ITestResult result) {

    }

    @Override
    public void onStart(ITestContext context) {

    }

    @Override
    public void onFinish(ITestContext context) {

    }
}

```

## 编写TestNG的测试
```java
public class TestNGTest {

    @Test
    public void test_pass(){
        System.out.println("passed_case");
    }

    @Test
    public void test_failed(){
        Assert.assertTrue(false);
    }

    @Test
    public void test_pass_2(){
        System.out.println("passed_case_2");
    }
}
```

## 将监听器放入Testng.xml文件

```xml
   <suite name="SimpleReport">
       <listeners>
           <listener class-name="com.hedwig.testng.TestNGSimpleReport"/>
       </listeners>
       <test verbose="1" name="simple test" >
           <classes>
               <class name="com.hedwig.testng.TestNGTest"/>
           </classes>
       </test>

   </suite>
```

## 运行Testng.xml文件,查看结果
结果如下,是不是很简单? 如果想做的cool一点,可以将这些数据写到一个html模版,写入文件就可以了

```java
===============================================
SimpleReport
Total tests run: 3, Failures: 1, Skips: 0
===============================================

Passed Case: 2
testFailed Case: 1
testSkipped Case: 0
passed case:test_pass
passed case:test_pass_2
failed case:test_failed
```

---
layout: post
title: "Refactoring-7-Extract-Interface,Method,Sub Class,Supper Class"
modified:
categories: [refactoring]
image: 3.jpg
tags: [refactoring]
date: 2015-10-26T10:31:11+08:00
---

Extract-Interface,Method,Sub Class,Supper Class

以上重构的方式主要是通过提起接口,方法,为了让代码有更好的可读性,可测性.

## 开始:实例代码

以下是一个需要重构的实例代码：

```java
public class Receipt {

    private List<Double> discounts= Lists.newArrayList();
    private List<Double> itemTotals=Lists.newArrayList();

    public double calculateGradTotal(){
        double subTotal =0;
        for (Double itemTotal : itemTotals) {
            subTotal+=itemTotal;
        }

        if(discounts.size()>0){
            for (Double discount : discounts) {
                subTotal-=discount;
            }
        }

        double tax=subTotal*0.065;
        subTotal+=tax;
        return subTotal;
    }
}
```

## 抽取方法

阅读代码,根据计算方法的步骤,可以通过如下尝试抽取方法:
- calculateSubTotal
- calculateDiscounts
- calculateTax

最后calculateGrandTotal 调用着三个方法. 由于实例代码比较简单,所以还看不出有多少优点.
但是如果想像calculateGrandTotal这个方法是很长的话，那么通过这种方式重构可以让计算calculateGrandTotal
的逻辑更加清晰.

```java
    public double calculateGrandTotal(){
        double subTotal=calculateSubTotal();
        subTotal=calculateDiscounts(subTotal);
        subTotal=calculateTax(subTotal);
        return subTotal;
    }

    public double calculateTax(double subTotal){
        double tax=subTotal*0.065;
        subTotal+=tax;
        return subTotal;
    }

    public double calculateDiscounts(double subTotal){
        if(discounts.size()>0){
            for (Double discount : discounts) {
                subTotal-=discount;
            }
        }

        return subTotal;
    }

    public double calculateSubTotal(){
        double subTotal=0;
        for (Double itemTotal : itemTotals) {
            subTotal+=itemTotal;
        }

        return subTotal;
    }
```

## 抽取接口
接口的好处想来大家都不叫清楚，所以有时有不同的实现出现时，抽取一个接口定义来也是一个不错的重构
时间。

- 假设ClassRegistration 如下:

```java

public class ClassRegistration {
  private double total;

  public void create(){
      System.out.println("create");
  }

  public void transfer(){
      System.out.println("transfer");
  }

```

- 有一个新的ClassRegistration，所以抽取接口

```java
public interface IClassRegistration {
    void create();
    double transfer();
}
```

然后修改ClassRegistration 使他实现IClassRegistration

- 客户端代码在增加一个实现之后实际上不需要修改了,或者只需要修改方法签名就可以

```java
public class RegistrationProcessor {
    public double processRegistration(IClassRegistration registration){
        registration.create();
        return registration.total();
    }
}
```

## Extract SubClass SupperClass

这两个实际上就是合并子类，或者分解类.将方法，属性放到更合适的位置。

## 一些小结

通过移动方法，分解方法，合并子类，分离大类，个人认为实际上完成了一些目的:

- 将大方法分解到小方法，更好的维护
- 分解不必要的依赖，可以通过新的实现来完成而不需要修改客户端代码
- 大方法分解之后,方法负责的任务更加小，更加清楚
- 小方法实际有更好的复用

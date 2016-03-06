---
layout: post
title: "Refactoring-10-introduce method object, replace conditions with polymorphism"
modified:
categories: [refactoring]
image: 9.jpg
tags: [refactoring]
date: 2015-11-03T10:31:11
---

## 将方法参数转化为类

有时一个方法的传入参数太多，就需要考虑是否需要引入新的类来解决的。

```java
public class Registration {
    public void create(double amount,String name,
                       double credits){
        //do work
    }

}
```

重构后:

```java
//instroduce new Class
public class RegistrationContext {

    double amount;
    String name;
    double credits;
}

//modify the method
public void createRefactored(RegistrationContext context){
    //do work
}

```

## 多态替代条件判断

有时通过If...Else来判断不同的类型进行不同的处理，代码可读性不是很强，通过多态来替代这些
条件判断，同时抽取方法后，代码就会更加的具有可读性.

```java
public class OrderProcessor {
    public double processOrder(Customer cu,List<Product> products){
        double orderTotal = products.parallelStream().mapToDouble(Product::getPrice).sum();
        if(cu instanceof Employee){
            orderTotal-=orderTotal*0.15;
        }

        if (cu instanceof NonEmployee){
            orderTotal-=orderTotal*0.10;
        }

        return orderTotal;
    }

}

public abstract class Customer {
}


public class Employee extends Customer {
}


public class NonEmployee extends Customer {
}
```

重构后:是不是代码更清楚了

```java

public abstract class Customer {
    abstract double tax();
}


public class Employee extends Customer {
    @Override
    double tax() {
        return 0.15;
    }
}


public class NonEmployee extends Customer {
    @Override
    double tax() {
        return 0.10;
    }
}



public double processOrderRefactor(Customer cu,List<Product> products){
    double orderTotal = products.parallelStream().mapToDouble(Product::getPrice).sum();

    orderTotal-=orderTotal*cu.tax();
    return orderTotal;
}
```

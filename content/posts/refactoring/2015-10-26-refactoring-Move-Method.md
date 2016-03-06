---
layout: post
title: "Refactoring-2-Move Method"
modified:
categories: [refactoring]
image: 4.jpg
tags: [refactoring]
date: 2015-10-26T10:31:11+08:00
---

Move Method 重构实际上比较简单，一个简单的描述就是:
- 如果有一个方法在一个类里面出现的频率很高，但他不在这个类里面
- 那么Move Method就是把这个方法移动到出现频率高的这个类里面

## Before Move Method

```java
public class BankAccountOrigin {

    private int accountAge;
    private int creditScore;
    private AccountInterestOrigin accountInterest;

    public double calculateInterestRate(){
        if(creditScore>800){
            return 0.02;
        }
        if(accountAge>10){
            return 0.03;
        }
        return 0.05;
    }
    ..... getter/setter
}

public class AccountInterestOrigin {
    private BankAccountOrigin ba;

    private double interestRate =ba.calculateInterestRate();
    private boolean introductorRate;

    public AccountInterestOrigin(BankAccountOrigin ba) {
        this.ba = ba;
    }
    public boolean isIntroductorRate() {
        return ba.calculateInterestRate()<0.05;
    }

    public void setIntroductorRate(boolean introductorRate) {
        this.introductorRate = introductorRate;
    }
}  

```

## After Move Method

```java
public class AccountInterestRefactored {
    private BankAccountRefactored ba;

    private double interestRate =calculateInterestRate();
    private boolean introductorRate;

    public AccountInterestRefactored(BankAccountRefactored ba) {
        this.ba = ba;
    }

    public boolean isIntroductorRate() {
        return calculateInterestRate()<0.05;
    }

    private double calculateInterestRate(){
        if(ba.getCreditScore()>800){
            return 0.02;
        }
        if(ba.getAccountAge()>10){
            return 0.03;
        }
        return 0.05;
    }
}
```

## 关于有什么好处的思考

Move Method just move method to different location.
本身其实很难说有多少好处.经常整理自己抽屉的孩子，也不会把床搞得太乱.可能就是
这个道理。

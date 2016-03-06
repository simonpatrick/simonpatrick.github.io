---
layout: post
title: "Refactoring-9-ArrowHead AntiPattern and Remove Double Negative"
modified:
categories: [refactoring]
image: 1.jpg
tags: [refactoring]
date: 2015-11-03T10:31:11
---

## Arrowhead AntiPattern

一下代码有一系列的if 判断，我们可以重新思考判断逻辑,合并一些逻辑判断
来让代码更可读:

```java
public boolean hasAccess(User user, Permission permission,
                        List<Permission> exemptions) {
      boolean hasPermission = false;
      if (user != null) {
          if (permission != null) {
              if (exemptions.Count() == 0) {
                  if (SecurityChecker.CheckPermission(user,permission) ||
                  exemptions.Contains(permission)) {
                      hasPermission = true;
                  }
              }
              return hasPermission;
          }

```

重构后:

```java
       if (user == null || permission == null)
           return false;
       if (exemptions.Contains(permission))
           return true;
       return SecurityChecker.CheckPermission(user, permission);
```

## Remove Double Negative

remove double negative 实际上非常简单,代码如下:

```java
public void checkout(){
       if(!isNotNull()){
           System.out.println("checking ....");
       }
   }

   private boolean isNotNull(){
       return true;
   }

```

重构后：

```java
private boolean isNull(){
    return true;
}

public void checkoutRefactored(){
    if(isNull()){
        System.out.println("checking ....");
    }
}
```

改动虽小，是不是让你阅读代码更爽一点......

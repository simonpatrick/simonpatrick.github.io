---
layout: post
title: "sql injection, sql 注入"
modified:
categories: [testing]
excerpt:
tags: [testing]
date: 2016-01-05-23:37:49
---

SQL注入的问题由来以久,主要是针对于一些系统时通过拼接SQL的方式来处理程序.以下是关于JAVA WEB的一些SQL注入的介绍.

[来源OWASP](https://www.owasp.org/index.php/Preventing_SQL_Injection_in_Java)

## 什么是SQL注入

SQL injection vulnerabilities allow an attacker to inject (or execute) SQL commands within an application.
大意就是攻击者可以通过修改页面请求来执行sql达到自己的目的，比如拉数据，或者恶意的修改数据等等.

## SQL 注入例子

一下例子是有SQL注入漏洞的一段程序：

```JAVA
conn = pool.getConnection( );
String sql = "select * from user where username='" + username +"' and password='" + password + "'";
stmt = conn.createStatement();
rs = stmt.executeQuery(sql);
if (rs.next()) {
loggedIn = true;
	out.println("Successfully logged in");
} else {
	out.println("Username and/or password not recognized");
}
```

由于SQL是拼接的，所有如果用户直接食用username，或者password中 使用了如:

```JAVA
admin' OR '1'='1
```

最后执行的SQL就是：

```JAVA
select * from user where username='admin' OR '1'='1' and password=' '
```

明显，这样就会把所有的用户信息拿到了

## 防范措施 Defense Strategy

prevent SQL injection:
- All queries should be parametrized.
- All dynamic data should be explicitly bound to parametrized queries.
- String concatenation should never be used to create dynamic SQL.

## Parameterized Queries／Stored Procedures

参数化SQL，使用prepareStatement

```JAVA
String selectStatement = "SELECT * FROM User WHERE userId = ? ";
PreparedStatement prepStmt = con.prepareStatement(selectStatement);
prepStmt.setString(1, userId);
ResultSet rs = prepStmt.executeQuery();
```

存储过程基本上能够防止SQL注入

## Hibernate/MyBatis

不要以为使用了ORM框架就没有SQL注入，其实不当使用也会有的.比如:

- Hibernate native SQL
- order by 没法使用绑定变量
- 动态表名也无法使用
  

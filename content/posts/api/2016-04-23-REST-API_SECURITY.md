---
layout: post
title: Rest API Security
modified: null
categories:
  - rest api
image: 2.jpg
tags:
  - rest api
date: 2016-04-12T13:26:07.000Z
---

# REST API

REST: Representational State Transfer REST 提倡无需Session，每次请求都带上身份认证，同样 REST基于HTTP的也是无状态的.不过REST API的安全性都需要自己实现.REST WEB SERVICE 的核心是RESOURCE(资源).资源可以使用URI来表示，一般REST风格的请求对应关系如下：

HTTP 方法 | 行为         | 实例
------- | ---------- | --------------------------------------
GET     | 获取资源信息     | <http://example.com/api/v1/orders>
GET     | 获取某个特定资源信息 | <http://example.com/api/v1/orders/123>
POST    | 创建新资源      | <http://example.com/api/v1/orders>
PUT     | 更新资源       | <http://example.com/api/v1/orders/123>
DELTE   | 删除资源       | <http://example.com/api/v1/orders/123>

对于请求数据一般用jSON或者XMl来表示，一般使用JSON

## 身份认证

- HTTP Basic
- HTTP Digest
- API Key
- oAuth
- JWK

## HTTP Basic

HTTP Basic 其实就看下面例子就可以了:

```
base64编码前:Basic admin:admin
base64编码后:Basic YWRtaW46YWRtaW4=
放到Header中:Authorization: Basic YWRtaW46YWRtaW4=
```

## API Key

API Key 是用户通过身份认证之后服务端给客户端分配一个API Key

- Oauth1.0
- Oauth2

## JWT: JSON Web Token

JWT 是JSON Web Token,用于发送可通过数字签名和认证的东西,它包含一个紧凑的,URL安全的 JSON对象,服务端可通过解析该值来验证是否有操作权限,是否过期等安全性检查。由于其紧凑的特点, 可放在url中或者 HTTP Authorization头中,具体的算法就如下图 ![img](/images/JWT.jpg)

## 授权

身份认证之后就是授权，不同的用户，授予不同的访问权限，如Admin，Normal，Auditor 等.

## HTTPS SSL

重要数据需要通过HTTPS来传输.

## 速率限制

根据用户判断某段时间的请求次数，存在内存数据库(redis,memcached),达到最大数即不接受用户的请求。

- X-Rate-Limit-Rest

## 错误处理

- 登陆，注册等统一进行记录管理
- 统一处理如401，403这样的错误
- 非法参数统一处理

## 重要的ID不透明处理

如/user/123,如果id是个重要的信息，可以通过对id进行url62,uuid处理


class: center, middle

# Cookie &  Session & CSRF

---
# Cookie
类似key/value的东东：
![描述](/img/cookie-show.png)

---
# Cookie相关的RFC文档
- [RFC 2019](https://tools.ietf.org/html/rfc2019)
- [RFC 2965](https://tools.ietf.org/html/rfc2965)
- [RFC 6265](https://tools.ietf.org/html/rfc6265)


最新的Http1.1标准，[RFC 7230](https://tools.ietf.org/html/rfc7230) 指明了RFC 6265是最新的Cookie的标准。

---
# Cookie Http Header
cookie通过http header在浏览器与服务器之间传输。

##Request Header

```bash
Cookie: JSESSIONID=DA0AD8BE014362258DD2395D292092F2.c36;
VUID=94AE1C949F2B435E852D366D48D8F18F; NAGENTID=0;
CNZZDATA3538029=cnzz_eid%3D639656208-1406786546-%26ntime%3D1406786546;
route=e6a4eb0dfea7a6b8067b7a0edaeabc56; __utma=1.48147676.1406786569.1406786569.1406786569.1;
 __utmb=1.1.10.1406786569; __utmc=1; __utmz=1.1406786569.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)
```
##Response Header
```bash
Set-Cookie: JSESSIONID=DA0AD8BE014362258DD2395D292092F2.c36; Path=/; HttpOnly
Set-Cookie: route=abda2a3bb80025b6a3e51983891b8ca7;Path=/
```

---
# Cookie Http Header
![描述](/img/cookie-header.png)



---
# Cookie支持的字符
RFC 6265
```xml
 cookie-value      = *cookie-octet / ( DQUOTE *cookie-octet DQUOTE )
 cookie-octet      = %x21 / %x23-2B / %x2D-3A / %x3C-5B / %x5D-7E
                       ; US-ASCII characters excluding CTLs,
                       ; whitespace DQUOTE, comma, semicolon,
                       ; and backslash

```
 US-ASCII字符集中，除去控制字符，空白字符，双引号，逗号，分号，反斜杠。

 RFC 6265的建议是用BASE64编码。

---
# Cookie支持的字符

## javascript
 javascript里没有标准的Base64的函数可用。实际上encodeURIComponent可能用的比较多。

## java
```java
/**
The name must conform to RFC 2109.
That means it can contain only ASCII alphanumeric characters and cannot contain commas,
semicolons, or white space or begin with a $ character.
The cookie's name cannot be changed after creation.
 **/
		Cookie cookie = new Cookie("abc", "xyz=sdlfkj");
		response.addCookie(cookie);

```
只能包含ASCII字母数字字符，并且不能包含逗号，分号或空格或以$开头的字符。

---
# Cookie的六个属性
```
- Expires  过期时间
- Max-Age  因为Expires不能准确表示浏览器接收到后多长时间过期，但IE不支持Max-Age
- Domain   域名范围
- Path     Cookie在特定的path才生效
- Secure   只有https时，才传输
- HttpOnly 浏览器的JS API不能访问到
```

- Path 实际上没什么用处，也没有人使用


---
# 设置Cookie过期时间
因为IE不支持Max-Age，所以只讨论Expires。

**当服务器的时间和浏览器的时间不一致会怎样？**

服务器时间是2014年，客户端时间设置为2015年

--

Chrome浏览器会自动据Date头来转换时间：
```bash
Date: Wed, 16 Jul 2014 15:19:30 GMT
Set-Cookie: UserNick=xxx; Domain=.csdn.net; Expires=Wed, 23-Jul-2014 15:19:30 GMT; Path=/
```

真正的cookie的expires转换为：
```bash
Thu, 23 Jul 2015 15:21:31 GMT
```

---
## 如何删除Cookie？
标准里没有说明，实际上服务器也没有什么办法可以删除。

服务器可以通过重新设置一个cookie值，并设置expires为1970年，让cookie失效。

---
# Cookie Domain
cookie的domain通常有下面的几种形式：
```bash
 example.com
 .example.com
 www.example.com
 test.example.com
 ```
 前面有一个 "." 是什么意思？

---
# Cookie Domain

 当访问 http://www.test.com 时
* 不设置Domain
```java
		Cookie cookie = new Cookie("abc", "xyz=sdlfkj");
		response.addCookie(cookie);
```
结果：
Domain   www.test.com
* 显式设置Domain
```java
		Cookie cookie = new Cookie("abc", "xyz=sdlfkj");
		cookie.setDomain("www.test.com");
		response.addCookie(cookie);
```
Domain   .www.test.com

RFC中规定了是如此。RFC 2965 3.2.2

If an explicitly specified value does not start with a dot, the user agent supplies a leading dot.


---
# Cookie Domain
* 如果Cookie的Domain是 test.com，访问 a.test.com 会不会发送cookie？

--

IE会发送，非IE浏览器不会发送。

[IE官方Blog](http://blogs.msdn.com/b/ieinternals/archive/2009/08/20/wininet-ie-cookie-internals-faq.aspx)

[测试网站](http://debugtheweb.com/test/cookieinherit.aspx)

据RFC6265 4.1.2.3，IE的做法是对的。

  The Domain attribute specifies those hosts to which the cookie will
   be sent.  For example, if the value of the Domain attribute is
   "example.com", the user agent will include the cookie in the Cookie
   header when making HTTP requests to example.com, www.example.com, and
   www.corp.example.com.

---
# Cookie Domain

* 如果设置Domain为.com , com.cn 会怎样？
```java
		Cookie cookie = new Cookie("abc", "xyz=sdlfkj");
		cookie.setDomain("com.cn");
		response.addCookie(cookie);
```
--
* 设置为*.168.66.239？

--

实际上是比较混乱的，可以简单认为，domain里至少要有一个" ."，以及还有一些顶级域名不能设置cookie。

---
# Cookie Domain

* 为什么推荐用www.test.com，而不要用test.com?
* 如果a.test.com 用JS设置了一个 test.com的cookie？

--

以 weibo.com 为例， **新浪微博主站的安全性等同于子域名网站的安全性**
* 子域名的服务器可以拿到微博的cookie
* 子域名可以随意覆盖父域名的cookie，导致用户登陆丢失

**a公司使用了b公司的子域名，如何保证a公司不会窃取b公司的用户的cookie？**

比如 fora.b.com 给a公司使用，如何保证a公司不会窃取 b.com 的cookie？

--

**b公司可以通过iframe，form嵌套，引入a公司的网页。**

用户在访问fora.b.com/ppppp?xxx=yyy 时返回的网页是：
```html
<form method="POST" action="http://test.a.com/ppppp?xxx=yyy" id="login_form"
target="post_iframe"></form>
<iframe width="100%" height="100%" frameborder="0"  name="post_iframe"></iframe>
```

---
# Cookie溢出攻击
```javascript
for (i = 0; i < 10000; i++) {
    document.cookie = "cookie" + i + "=chocolate-chips; Path=/;
    Domain=.google.com.hk; Expires=Thu, 01-Jan-2100 00:00:01 GMT;"
}
```
--
浏览器为每个域名设置的Cookie的容量是有限的

即使设置了Secure/HttpOnly也会被攻击

后面设置的cookie会把前面的cookie冲掉

另外，设置了太多cookie会导致请求可能被拒绝，需要清除cookie才可以正常使用。

---
# Cookie溢出攻击
####测试网页
在google code上的一个测试项目，项目地址：
```
https://code.google.com/p/test-cookie/
测试网页地址：
http://test-cookie.googlecode.com/git/test.html
```
IE打开时，会卡很久，因为设置1000个cookie，IE也是会丢弃前面的cookie，只保留最后的约50个cookie：

chrome浏览器打开时，会发现set-cookie失败。chrome浏览器会保护好自己google的域名，但有一些其它公司域名不会保护（因为不能）。
对于一个子域名设置父域名cookie的情况，都不起作用了。

**所以要把域名分开，不能让用户的raw文件和google code使用同一域名。**
```xml
code.google.com
googlecode.com
```

[github把raw.github.com的域名移到 githubusercontent.com](https://developer.github.com/changes/2014-04-25-user-content-security/)


---
# 子域名的好处
* cookie安全性的原因

* cookie分离，减少流量

* 浏览器的并发加载

* CDN缓存方便

--

###为什么要控制cookie的个数和大小？

---
# Path, Secure, HttpOnly

Domain是最重要的cookie的属性，另外还有下面三个属性：

* Path意义不大，因为JavaScript代码可以随意发起请求

* Secure  必要

* HttpOnly 必要，xss的攻击成本大大提高

 **并非设置HttpOnly cookie就安全了，还有其它的一些攻击方法。**
 flash, IE漏洞，web服务器漏洞等

还要注意一点：

- cookie是没有端口概念的

---
#cookie如何保存加密信息？
* md5 加密被破解的例子

[Codeigniter 利用加密Key（密钥）的对象注入漏洞](http://drops.wooyun.org/papers/1449)

对称加密，强度要足够

推荐AES256位


---
#多次set cookie？
```java
		Cookie cookie = new Cookie("abc", "xyz=sdlfkj");
		response.addCookie(cookie);
		response.addCookie(cookie);
		response.addCookie(cookie);
		response.addCookie(cookie);
		response.addCookie(cookie);
		response.addCookie(cookie);
```
--

![multi-setcookie](/img/multi-setcookie.png)

**因为cookie实际上是用数组来存储的，并非map。**

---
# Session
## Session的本质是什么？

--
  标识用户，维持上下文


---

# Web Session的实现的三种方式

* url重写

 典型看Tomcat的 /manager页面，http://localhost:8080/manager 。

 url带sessionid的安全性问题：

 http://www.inbreak.net/archives/171

* 基于Cookie

  WebServer返回一个强度足够的随机数/随机字符串

Tomcat的JSESSIONID就是用SecureRandom生成随机数：

[ManagerBase.java](https://github.com/apache/tomcat/blob/TOMCAT_7_0_42/java/org/apache/catalina/session/ManagerBase.java)

  [SessionIdGenerator.java](https://github.com/apache/tomcat/blob/TOMCAT_7_0_42/java/org/apache/catalina/util/SessionIdGenerator.java)


* 基于form表单，插入一个隐藏的input标签

---

# Cookie 与 Session的关系


* Cookie是一种客户端/浏览器的存储机制。


* Cookie可以用来维持浏览器和Web Server之间的Session。

---
# 什么情况下请求会带cookie？

* XMLHttpRequest 请求会不会带cookie?

* jspnp请求会不会带cookie？

* 向一个其它域名的网站提交一个form，会不会带cookie？

--

* XMLHttpRequest：

同域情况下会，不同域情况下不会。如果服务器设置Access-Control-Allow-Credentials: true ，也是可以跨域带Cookie的。

--

* jspnp请求

会。

--

* form提交

会。

---
# CSRF

* CSRF请求是如何发起的
* 相当多的开发人员不能正确理解CSRF

--

* CSRF利用了浏览器的Cookie机制，从而达到了非法访问
* **理解什么时候请求会带上Cookie，对于理解CSRF相当关键**

---
# 防御CSRF
**为什么判断referer不是很好的办法？**
* referer 为空
  - https跳转http没有referer
  - https跳转不同的域名的https没有referer
  - 通过特殊构造的POST请求没有referer
  - 一些proxy会把referer去掉

* 判断的逻辑复杂（用正则匹配？）
* 友站中招，殃及池鱼
* 可以作为过渡方案，非长久之计
--

* 不要使用正则，要正确地处理URL。

**是否处理了这种情况site.com，site.com.attacker.com？**
* 构造空referer请求的一些参考资料

[Stripping Referrer for fun and profit](http://blog.kotowicz.net/2011/10/stripping-referrer-for-fun-and-profit.html)

[Stripping the Referer in a Cross Domain POST request](http://webstersprodigy.net/2013/02/01/stripping-the-referer-in-a-cross-domain-post-request/)

---
# 防御CSRF

## Tomcat的做法

### CsrfPreventionFilter

 CsrfPreventionFilter的思想是只记录最近的几次（默认5次）的请求参数，
 每个请求都会生成一个新的参数，并放到LRU Cache里。
 并把这个LRU Cache放到Session里。这样的话Tomcat就可以处理那种回退的操作。

```java
            LruCache<String> nonceCache = (session == null) ? null
                    : (LruCache<String>) session.getAttribute(
                            Constants.CSRF_NONCE_SESSION_ATTR_NAME);
```

---
# 防御CSRF

**Spring mvc的做法**

 org.springframework.security.web.csrf.CsrfFilter

CsrfToken默认保存到session里

 request的session里拿到CsrfToken，然后再把相关的变量request.setAttribute到request里

 在jsp页面上，在head标签插入
```html
  <head>
    <meta name="_csrf" content="${_csrf.token}"/>
    <!-- default header name is X-CSRF-TOKEN -->
    <meta name="_csrf_header" content="${_csrf.headerName}"/>
  </head>
```

在form表单，插入一个隐藏的input标签
```html
	<form action="csrfpost" method="post">
		<p>/csrfpost, with sec:csrfInput</p>
		<sec:csrfInput />
		<input type="submit" value="Submit" />
	</form>
```

---
# 防御CSRF

**Spring mvc的做法**

对于AJAX请求，增加一个_csrf_header:
```javascript
$(function () {
var token = $("meta[name='_csrf']").attr("content");
var header = $("meta[name='_csrf_header']").attr("content");
$(document).ajaxSend(function(e, xhr, options) {
	xhr.setRequestHeader(header, token);
});
});
```
也可以在请求的url里带上csrfToken：
```html
<form action="./upload?${_csrf.parameterName}=${_csrf.token}" method="post" enctype="multipart/form-data">
```

---
# 防御CSRF

**Django的做法**

- csrftoken保存到cookie里，csrftoken设置为一个随机的值

- 在请求的表单或者header里带上csrftoken，和springmvc类似

https://docs.djangoproject.com/en/dev/ref/csrf/

因为同源策略，其它网站的页面是不可能读取到cookie里的csrftoken，那么它发起的请求也只能带上Cookie，而不能带上parameter参数

https://github.com/django/django/blob/master/django/middleware/csrf.py

---
# 防御CSRF
**csrf token放到cookien里的优缺点**

优点：
* 服务器的判断逻辑简单，取cookie和header/parameter对比即可

缺点：
* 每个请求都会带上这个cookie，原本是不必要的，比如图片

---
# 防御CSRF
**意想不到的泄露csrf token**

在页面上输出csrf token有一定的危险性
* 在页面上输出了csrf token
* 攻击者通过社会工程学，让用户把网页保存下来发送给攻击者
* 攻击者分析网页，拿到csrf token
* 攻击者让用户访问恶意网站，在脚本时构造带上csrf token参数的请求

---
# 防御CSRF
**尽量避免在url中使用csrf token**

因为比较容易泄露csrf token
* 在浏览器的历史里
* 在web服务器的log里
* 在其它网站request的referer可能会获取到

**更多的参考**

https://www.owasp.org/index.php/Cross-Site_Request_Forgery_(CSRF)_Prevention_Cheat_Sheet


---
#sticky session

为什么需要sticky session？

假定一个网站，后面有三台tomcat服务器，前端用nginx做负载均衡。

```xml
          DNS Round Robin
                |
         Load Balancer
          /     |     \
         /      |      \
    Tomcat1   Tomcat2  Tomcat3
```
如果nginx是随机，或者轮循策略，则会有下面这些问题：

- session 共享/分布式的问题
  通常web服务器的session实现都是本进程内存中的

- 日志不连续

--

ip_hash 也不理想

- 某些服务器负载过重
- 用户切换IP的问题

---

# sticky session的实现

###tomcat jvmroute + apache mod_jk

http://tomcat.apache.org/tomcat-7.0-doc/cluster-howto.html

原理：

 - 在tomcat里配置上jvmroute，如m15
 - 生成的JSESSIONID后面会加上jvmroute做后缀
 - apache据cookie的后缀把请求发到对应的tomcat

```
JSESSIONID	358F9DF41E610F10B3266B77C94F4B51.m15
```

---

# sticky session的实现

###nginx-sticky-module
https://code.google.com/p/nginx-sticky-module/

原理：
据upstream生成一个 md5 的cookie，后面的请求据这个cookie转发到对应的服务器上
```
(client)                             (nginx)                      (upstream servers)
    >-- GET /URI1 HTTP/1.0 -----------> |
                                        | *** nginx choose one upstream by RR ***
                                        | >----- GET /URI1 HTTP/1.0   ----> |
                                        | <------- HTTP/1.0 200 OK -------< |
    <-- HTTP/1.0 200 OK --------------< |
        Set-Cookie: route=md5(upstream) |
                                        |
    >-- GET /URI2 HTTP/1.0 -----------> |
        Cookies: route                  |
                                        | *** nginx redirect to "route" ***
                                        | >----- internal fetch /URI2 ----> |
                                        | <--- internal response /URI2 ---< |
    <-- HTTP/1.0 200 OK --------------< |
```

---

# sticky session的实现

###tengine-upstream-session-sticky

http://tengine.taobao.org/document_cn/http_upstream_session_sticky_cn.html

原理同nginx-sticky-module，功能更丰富。


---

# 分布式session的实现

完全分布式session（没有sticky session）实现的代价很高：

- 版本问题
- 数据一致性问题
- 锁？

**sticky session + 集中式session存储是个比较好的选择**

---
# 分布式session的实现
###细节是魔鬼
- 兼容javax.servlet.http.HttpSession接口
 是否要实现 java.io.Serializable ？

- session内部用什么来做存储？

 org.apache.catalina.session.StandardSession
 ```java
 /**
 * The collection of user data attributes associated with this Session.
 */
protected Map<String, Object> attributes = new ConcurrentHashMap<String, Object>();
```
- 通过Filter拦截请求，包装自己的Session实现类

 ```java
HttpSession
HttpServletRequestWrapper
HttpServletResponseWrapper
```
- memcached/redis?
 以单个key存储都个session？

 以单个key存储Session里的一个attribute？

- 合并修改？还是每修改一次session，提交修改到缓存服务器？

---
# 分布式session的实现
###细节是魔鬼

- 什么时候flush到cache？

标准里的接口，没有合适的地方可以注入。

黑科技：
```java
public interface ServletResponse {
    public ServletOutputStream getOutputStream() throws IOException;
    public PrintWriter getWriter() throws IOException;
}
```
数据在返回给浏览器前，一定会调用到上面两个函数，所以重载之后，在里面flush到cache中。

- 是否要提供接口，可以手动flush？提供异步API？

---
# 分布式session的实现
###细节是魔鬼

- 是否要实现数据补偿？

 当发现cache里的数据，比当前内存里的数据要新，是否要合并？

- 是否要考虑session存储在cookie里的情况？


---
# 分布式session的实现

一些开源项目：
- [tomcat cluster](http://tomcat.apache.org/tomcat-7.0-doc/cluster-howto.html#Configuration_Example)

  结点之间用Multicast互相发现，结点之间用TCP来通讯。当NodeA修改了Session，把Session的通知写到物理TCP中，再返回Response给用户。
- [memcached-session-manager](https://code.google.com/p/memcached-session-manager/)

  多年开源项目，代码很复杂

- [tomcat-redis-session-manager](https://github.com/jcoleman/tomcat-redis-session-manager)

  强依赖tomcat，继承ManagerBase，实现自己的session的处理函数，原理/代码比较简单

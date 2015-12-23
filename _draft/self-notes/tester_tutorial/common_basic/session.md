# HTTP Session
session在web开发中是一个非常重要的概念，这个概念很抽象，很难定义，也是最让人迷惑的一个名词，
也是最多被滥用的名字之一，在不同的场合，session一次的含义也很不相同。这里只探讨HTTP Session.

## Java 中的HttpSession
在Java中，HTTP的Session对象用javax.servlet.http.HttpSession来表示.
- 1、概念：Session代表服务器与浏览器的一次会话过程，这个过程是连续的，也可以时断时续的。
在Servlet中，session指的是HttpSession类的对象.
- Session创建的时间
一个常见的误解是以为session在有客户端访问时就被创建，然而事实是直到某server端程序调用 HttpServletRequest.getSession(true)这样的语句时才被创建.
注意如果JSP没有显示的使用 <% @page session="false"%> 关闭session，则JSP文件在编译成Servlet时将会自动加上这样一条语句 HttpSession session = HttpServletRequest.getSession(true);这也是JSP中隐含的 session对象的来历。
由于session会消耗内存资源，因此，如果不打算使用session，应该在所有的JSP中关闭它。

引申：
- 访问*.html的静态资源因为不会被编译为Servlet，也就不涉及session的问题。
- 当JSP页面没有显式禁止session的时候，在打开浏览器第一次请求该jsp的时候，服务器会自动为其创建一个session，并赋予其一个sessionID，
:JSESSIONID=客户端第一次拿到的session ID---搞不懂这个，就永远不明白session的原理
- Session删除的时间是：
  1）Session超时：超时指的是连续一定时间服务器没有收到该Session所对应客户端的请求，并且这个时间超过了服务器设置的Session超时的最大时间。
  2）程序调用HttpSession.invalidate()
  3）服务器关闭或服务停止
- session存放在哪里：服务器端的内存中。不过session可以通过特殊的方式做持久化管理
- session的id是从哪里来的，sessionID是如何使用的？
当客户端第一次请求session对象时候，服务器会为客户端创建一个session，并将通过特殊算法算出一个session的ID，用来标识该session对象，
当浏览器下次（session继续有效时）请求别的资源的时候，浏览器会偷偷地将sessionID放置到请求头中，服务器接收到请求后就得到该请求的sessionID，
服务器找到该id的session返还给请求者（Servlet）使用。一个会话只能有一个session对象，对session来说是只认id不认人。
- session会因为浏览器的关闭而删除吗？
不会，session只会通过上面提到的方式去关闭。
- 同一客户端机器多次请求同一个资源，session一样吗？
一般来说，每次请求都会新创建一个session。
- session是一个容器，可以存放会话过程中的任何对象。
- session因为请求（request对象）而产生，同一个会话中多个request共享了一session对象，可以直接从请求中获取到session对象。
- 其实，session的创建和使用总在服务端，而浏览器从来都没得到过session对象。但浏览器可以请求Servlet（jsp也是Servlet）来获取session的信息。
客户端浏览器真正紧紧拿到的是session ID，而这个对于浏览器操作的人来说，是不可见的，并且用户也无需关心自己处于哪个会话过程中

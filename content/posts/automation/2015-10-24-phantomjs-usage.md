---
layout: post
title: "Phantomjs Tutorial"
modified:
categories: [automation]
excerpt:
tags: [automation]
image: 6.jpg
date: 2015-10-24T10:31:11+08:00
---

自己学习Phatomjs的教程,分享之.

## Quick Start
首先phantomjs是个什么? 以下是官方网站的解释:

```
PhantomJS is a headless WebKit scriptable with a JavaScript API.
It has fast and native support for various web standards:
DOM handling, CSS selector, JSON, Canvas, and SVG.
```

phantomjs可以用来做什么?

- [HEADLESS WEBSITETESTING](http://phantomjs.org/headless-testing.html)
- [SCREENSHOT](http://phantomjs.org/screen-capture.html)
- [PAGE AUTOMATION](http://phantomjs.org/page-automation.html)
- [NETWORK MONITORING](http://phantomjs.org/network-monitoring.html)
- ...... depends on your imagination

这里主要来介绍一下PhantomJS的基础用法,包括了:

- 基础语法
- HEADLESS WEB TESTING
- SCREEN Capture
- Network Monitoring
- Page Automation


安装PhantomJS请参考: [http://phantomjs.org/download.html](http://phantomjs.org/download.html)

### 基础语法

- Hello World

```javascript
console.log('Hello World!');
phantom.exit();
```

result:

```sh
phantomjs hello_world.js
Hello World!
```

- Page Loading
一下代码是访问百度首页,计算页面加载时间并且截屏的例子:

```javascript
var page = require('webpage').create();
var url = 'http://www.baidu.com';
t = Date.now();
page.open(url, function (status) {
    console.log("Status:" + status);
    if (status !== 'success') {
        console.log('FAIL to load the address');
    } else {
        t = Date.now() - t;
        console.log('Loading ' + url);
        console.log('Loading time ' + t + ' msec');
        page.render('baidu.png'); //capture the screenshot
    }

    phantom.exit();
})
```

运行结果：

```bash
●✚  phantomjs pageload.js                              [10:43:41]
Status:success
Loading http://www.baidu.com
Loading time 699 msec
```

是不是很简单，只要几行代码就可以实现了,这里主要使用了:```webpage``` 这个模块

- Code Evaluation

通过evaluate 方法可以在当前页面运行js程序，但是也仅限于当前页面的范围

```javascript
var page = require('webpage').create();
page.onConsoleMessage = function(msg) {
    console.log('Page title is ' + msg);
};
page.open("http://www.baidu.com", function(status) {
    page.evaluate(function() {
        console.log(document.title);
        var element = document.getElementById('kw');
        console.log(element.getAttribute('name'));
    });
    phantom.exit();
});
```

运行结果：

```sh
phantomjs code_evaluation.js                       [10:51:55]
Page title is 一张网页，要经历怎样的过程，才能抵达用户面前？
一位新人，要经历怎样的成长，才能站在技术之巅？
探寻这里的秘密；
体验这里的挑战；
成为这里的主人；
加入百度，加入网页搜索，你，可以影响世界。

Page title is 请将简历发送至 %c ps_recruiter@baidu.com（ 邮件标题请以“姓名-应聘XX职位-来自console”命名） color:red
Page title is 职位介绍：http://dwz.cn/hr2013
Page title is 百度一下，你就知道
Page title is wd

```

- On request and Response

通过phantomjs 监听request和response，代码：

```javascript
var page = require('webpage').create();
var url="http://www.baidu.com"
page.onResourceRequested = function(request) {
    console.log('Request ' + JSON.stringify(request, undefined, 4));
};
page.onResourceReceived = function(response) {
    console.log('Receive ' + JSON.stringify(response, undefined, 4));
};
page.open(url,function(){
    console.log("success");
    phantom.exit()
});
```

 运行结果：

 ```sh
 ...............
}
],
"id": 18,
"redirectURL": null,
"stage": "end",
"status": 200,
"statusText": "OK",
"time": "2015-10-24T04:05:39.086Z",
"url": "https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su?wd=&json=1&p=3&sid=17521_1455_17619_13245_17640_17001_17470_17072_15640_11634_17051&req=2&csor=0&cb=jQuery110209065551124513149_1445659538702&_=1445659538703"
}
success
 ```

## HEADLESS WEB TESTING

please refer here:http://phantomjs.org/headless-testing.html

## SCREENSHOT

screen capture is quite simple,just use:

```javascript
var page = require('webpage').create();
var url = 'http://www.baidu.com';
t = Date.now();
page.open(url, function (status) {
    console.log("Status:" + status);
    if (status !== 'success') {
        console.log('FAIL to load the address');
    } else {
        t = Date.now() - t;
        console.log('Loading ' + url);
        console.log('Loading time ' + t + ' msec');
        page.render('baidu.png'); //capture the screenshot
    }

    phantom.exit();
})
```

also actual use ```page.render('baidu.pdf')``` to generate a PDF file

## page-automation

操作

```javascript
var page = require('webpage').create();
var url ="http://www.baidu.com";
var cdn_url= 'http://cdn.staticfile.org/jquery/2.1.1-rc2/jquery.min.js';

page.open(url, function() {
    page.includeJs(cdn_url, function() {
        page.evaluate(function() {

            $("button").click();
        });
        phantom.exit()
    });
    page.render('baidu.png');
});
```

## Related Projects

相关的项目请参考：
[projects](http://phantomjs.org/related-projects.html)

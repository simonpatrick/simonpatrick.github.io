---
layout: post
title: "How JavaScript MV* Works"
description: ""
category-substitution: 原创
tags: [Backbone, MVC, JavaScript, Web]

link-d: /bak/mvc.html
---
{% include JB/setup %}


## 参考资料

* [Rich JavaScript Applications – the Seven Frameworks](http://blog.stevensanderson.com/2012/08/01/rich-javascript-applications-the-seven-frameworks-throne-of-js-2012/)
  * [\[翻译\] JavaScript宝座：七大框架论剑](http://www.ituring.com.cn/article/8108)
  * AngularJS、Backbone、Batman、CanJS、Ember、Meteor、Knockout、Spine
* [Backbone.js vs Spine.js](http://stackoverflow.com/questions/6530444/backbone-js-vs-spine-js)
* [Model View Controller, Model View Presenter, and Model View ViewModel Design Patterns](http://www.codeproject.com/Articles/42830/Model-View-Controller-Model-View-Presenter-and-Mod)
* [MVC, MVP and MVVM: A Comparison of Architectural Patterns](http://channel9.msdn.com/Events/TechEd/NorthAmerica/2011/DPR305)
* [MVC vs. MVP vs. MVVM](http://nirajrules.wordpress.com/2009/07/18/mvc-vs-mvp-vs-mvvm/)
* [MVVM vs MVP vs MVC: The differences explained](http://joel.inpointform.net/software-development/mvvm-vs-mvp-vs-mvc-the-differences-explained/)
* [MVVM vs MVP vs MVC  The concise explanation](http://joel.inpointform.net/software-development/mvvm-vs-mvp-vs-mvc/)
* [MVP(SC),MVP(PV),PM,MVVM 和 MVC 表现模式架构对比](http://wenku.baidu.com/view/16decd4e852458fb770b560f.html)
* [Understanding Basics of UI Design Pattern MVC, MVP and MVVM](http://www.codeproject.com/Articles/228214/Understanding-Basics-of-UI-Design-Pattern-MVC-MVP)
* [MVC系列之一:图解MVC MVP MVVM区别](http://www.cnblogs.com/piaopiao7891/archive/2012/09/04/2670390.html)
* [wiki MVC](http://en.wikipedia.org/wiki/Model-view-controller)
* [MVP, MVC, MVVM, 傻傻分不清楚~](http://www.dotblogs.com.tw/regionbbs/archive/2011/09/29/compare.to.mvp.mvc.mvvm.aspx)
* [Model-View-ViewModel (MVVM) Explained](http://csharperimage.jeremylikness.com/2010/04/model-view-viewmodel-mvvm-explained.html)
* [知乎 MVC、MVP、MVVM](http://www.zhihu.com/question/20148405)
* [百科 MVVM](http://baike.baidu.com/view/3507915.htm)
* [白汀 Backbone Application](http://feliving.github.com/developing-backbone-applications/)
* [MODELS - VIEWS - CONTROLLERS](http://heim.ifi.uio.no/~trygver/1979/mvc-2/1979-12-MVC.pdf)
  * [\[翻译\] MODELS - VIEWS – CONTROLLERS](http://www.cnblogs.com/winter-cn/archive/2012/06/13/2547662.html)
  * [为何选择MVVM而非MVC](http://www.cnblogs.com/winter-cn/archive/2012/09/16/2687184.html)
* [Clarification :MVC,MVP,MVVM](http://stackoverflow.com/questions/4751633/clarification-mvc-mvp-mvvm)
* [MVVM Compared To MVC and MVP](http://geekswithblogs.net/dlussier/archive/2009/11/21/136454.aspx)
* [Building Enterprise Applications with Windows Presentation Foundation and the MVVM Model View ViewModel Pattern](http://books.google.com.hk/books?id=6WJ5oQT0dcUC&hl=zh-CN)
* [GitHub Buttons](http://ghbtns.com/)


## 参考框架&库

* [Backbone] {% assign fullname = "documentcloud/backbone" %}{% include custom/ghbtns %}
  * Backbone supplies structure to JavaScript-heavy applications by providing models key-value binding and custom events, collections with a rich API of enumerable functions, views with declarative event handling, and connects it all to your existing application over a RESTful JSON interface.
* [Meteor] {% assign fullname = "meteor/meteor" %}{% include custom/ghbtns %}
  * Meteor is an ultra-simple environment for building modern web applications.
  * With Meteor you write apps:
    * in pure Javascript
    * that send data over the wire, rather than HTML
    * using your choice of popular open-source libraries
* [Ember.js] {% assign fullname = "emberjs/ember.js" %}{% include custom/ghbtns %}
  * Ember.js is a JavaScript framework that does all of the heavy lifting that you'd normally have to do by hand. There are tasks that are common to every web app; Ember.js does those things for you, so you can focus on building killer features and UI.
  * These are the three features that make Ember.js a joy to use:
    * Bindings
    * Computed properties
    * Auto-updating templates
* [AngularJS] {% assign fullname = "janl/mustache.js" %}{% include custom/ghbtns %}
  * AngularJS lets you write client-side web applications as if you had a smarter browser. It lets you use good old HTML (or HAML, Jade and friends!) as your template language and lets you extend HTML’s syntax to express your application’s components clearly and succinctly. It automatically synchronizes data from your UI (view) with your JavaScript objects (model) through 2-way data binding. To help you structure your application better and make it easy to test, AngularJS teaches the browser how to do dependency injection and inversion of control. Oh yeah and it also helps with server-side communication, taming async callbacks with promises and deferreds; and make client-side navigation and deeplinking with hashbang urls or HTML5 pushState a piece of cake. The best of all: it makes development fun!
* [Knockout] {% assign fullname = "SteveSanderson/knockout" %}{% include custom/ghbtns %}
  * Knockout is a JavaScript MVVM (a modern variant of MVC) library that makes it easier to create rich, desktop-like user interfaces with JavaScript and HTML. It uses observers to make your UI automatically stay in sync with an underlying data model, along with a powerful and extensible set of declarative bindings to enable productive development.
* [Spine] {% assign fullname = "spine/spine" %}{% include custom/ghbtns %}
  * Spine is a lightweight framework for building JavaScript web applications. Spine gives you an MVC structure and then gets out of your way, allowing you to concentrate on the fun stuff, building awesome web applications.
* [batman.js] {% assign fullname = "Shopify/batman" %}{% include custom/ghbtns %}
  * batman.js is a framework for building rich single-page browser applications. It is written in CoffeeScript and its API is developed with CoffeeScript in mind, but of course you can use plain old JavaScript too.
* [CanJS] {% assign fullname = "bitovi/canjs" %}{% include custom/ghbtns %}
  * CanJS is a MIT-licensed, client-side, JavaScript framework that makes building rich web applications easy. Use it because it’s: Smaller, Faster, Safer, Easier, Library-er.
* [TodoMVC] {% assign fullname = "addyosmani/todomvc" %}{% include custom/ghbtns %}
  * Helping you select an MV* framework - Todo apps for Backbone.js, Ember.js, AngularJS, Spine and many more

[TodoMVC]:      https://github.com/addyosmani/todomvc
[AngularJS]:    https://github.com/angular/angular.js
[Backbone]:     https://github.com/documentcloud/backbone
[batman.js]:    https://github.com/Shopify/batman
[CanJS]:        https://github.com/bitovi/canjs
[Ember.js]:     https://github.com/emberjs/ember.js
[Meteor]:       https://github.com/meteor/meteor
[Knockout]:     https://github.com/SteveSanderson/knockout
[Spine]:        https://github.com/spine/spine


## 前言开光 - 框架>=本质

先起个头谈谈对框架认识和学习吧。

优秀的框架是对某一类问题的本质认知、对关键特征的精确把握，需要深厚的软件功底和大量应用开发经验，是设计模式在某一领域的最佳实践，以及对诸多因素的平衡。

学习框架就是在学习某一类问题的本质和关键特征，学习作者对理论、实现、应用、市场的平衡理念。

通过这个系列我希望达到以下目的：

* MVC 提出了什么问题（或希望解决什么问题）
* 学习 Backbone 是如何解决的（或作者是如何理解 JSMVC 的）
* 学习 Backbone 的实现技巧
* 学习 Backbone 涉及的基础知识
* 以及前端开发的方向
* 最终接近作者的专业水平

附：《Backbone 源码分析系列》依然是以源码分析为主，目前会把时间放在这个系列上，入门和应用开发会另开两个系列《Backbone 入门》和《精通 Backbone》，视时间而定。

## MVC 模型

### 代码混乱

前端攻城师是个新兴的职业，一直以来前端开发面临着以下的问题：

* 数据模型、业务模型不清晰
* 代码复用率低，很多时候是 Ctrl-C/V
* 代码可读性和可维护性低
* 难以满足需求的变化，特别是前端需求的频繁变化

jQuery 在很大程度上改善了这种状态，解决了原生 JS 代码写起来繁琐的问题；jQuery 的革命性特征可以总结为：

* 良好的浏览器兼容
* 独特的链式语法
* 高效 CSS 选择器
* 丰富的插件
* 以及更好的贯彻 HTML、CSS、JS 的分工。

不过，总体感觉 jQuery 是定位于 DOM 查找和操作为主的基础库，这样的定位使得 jQuery 的大型前端项目中只能作为底层支持库使用。应用代码依然是杂乱无章，从而不得不依赖于攻城师的技术水准和职业素养。

MVC 模型则通过细分模型、视图、控制器的职责，可以解耦合、提高代码复用、简化重构、适应变化、易扩展、易读、较少维护代码、提高可维护性。同时，因为是分层结构化、模块化开发，还可以实现代码自动生成。但是MVC也会导致复杂度上升、运行效率下降。

MVC 的核心目标是：分离显示逻辑和业务逻辑，即减弱业务逻辑接口与数据逻辑接口之间的耦合，以及让视图层更富于变化。

MVC 的优点可以概括为：可扩展性、可复用性、可维护性、有利于软件工程管理。

Backbone 的优点集中体现在：提供 MVC 模型基础实现、面向对象、导航。

导航使系统的脉络更加清晰，通过一个配置文件，即可把握整个系统各部分之间联系，便于维护。

MVC 特别适用于事件驱动的场景，通过约定开发方式，还可以使代码开发和代码管理变得有章可循。JS 应用程序运行的的本质是基于事件驱动，这与 MVC 不谋而合。并且，MVC 在大部分语言的框架中都有实现，随着前端和 JS 越来越被认可和重视，JSMVC 框架的出现成为必然。

Backbone 正是 MVC 开发模型在浏览器环境中的实践，从目前看也是一款优秀的 JSMVC 框架。

### 传说中的单页面应用程序 SPA（或一站式应用程序）

SPA Sigle-page Application，也称为 OPOA One Page One Application、SPI Sigle-page Interface。

SPA 的优势相当诱人，可以共享框、库、数据，减少 HTTP 请求和流量，缩短加载时间、降低成本；不必重新加载整个页面，不会出现界面调整时的空白页面，加上合理的加载提示动画，可以实现不间断的用户体验。

但是 SPA 也带来了更多的挑战，比如：

* 所有的 HTML、CSS、JS 都在一个页面中加载和销毁，需要安全、可靠、开发简单的内存管理，尤其是IE臭名昭著的内存泄漏。
* 事件管理会更加复杂，jQuery 提供的事件缓存不能完全满足这种需求。
* 浏览器历史管理。
* 还有诸多难题，都会导致开发方式和成本的增加。

SPA 传统的实现方式是使用分帧（frameset + frame + iframe），但 URL 不会发生变化，这导致浏览器历史的前进、后退和收藏功能失效，因此在过去，SPA 仅局限于对 URL 不敏感的场合，比如 MIS 系统。    

站在攻城师的角度，这种复杂性和局限性不是我们所乐意看到的，谁愿意受无谓的虐待呢？

即使对 Ajax 的发掘也没有让 SPA 真正变得可行，虽然 Ajax 拯救了曾经半死不活的 JavaScript。Ajax 可以实现无刷新加载界面（即动态加载），但同样不能修改 URL，只能通过延迟加载、异步加载等技巧，来减少 HTTP 流量、加速网页打开速度、优化用户体验。

直到对 URL hash（即 location.hash）的挖掘，SPA 才变得切实可行。location.hash 是一个可读写的字符串，指定了当前 URL 中的锚部分，包括前导散列符 #。URL hash 虽然不会在请求时传给服务器，但是在浏览器中，改变 URL hash 却可以支持前进、后退、收藏（在低版本的 IE 中需要通过 iframe 实现）。

hash 驱动正是 Backbone 事件驱动模型中一种，在某些应用中甚至是最重要的一种，此外 Backbone 还有模型事件驱动和视图事件驱动。

### 结构化的 Web 应用程序

个人认为 SPA 最能体现 MVC 设计思想，当然，MVC 也适合应用在由多个页面组成的 Web 应用程序中，以 Backbone 为例，每个页面分别基于 Backbone 的 Model 和 View 进行设计和开发，同样可以增加可复用性、可扩展性、可维护性。

### 还不够完美

模块化、模块依赖、动态载入、模板等概念、库、框架需要去研究和学习，虽然这些已算不得什么新鲜事务，但是如何将各种专注的库、工具、框架无缝集成，变成完整、可靠、稳定、可以高效开发、可以成熟应用的系统解决方案，是目前前端领域需要继续研究和实践的课题。这方面推荐 [@玉伯](http://weibo.com/lifesinger) 领导的 [Arale](http://aralejs.org/) 项目。

更少的代码、更短的开发周期、更少的 BUG、易读、易维护、易扩展，才是优秀攻城师的追求。

回到本文的主题 MVC，模型与视图的关系在实际应用中的关系可能更加复杂，视图不仅要引用模型，负责渲染、交互，还会涉及模板引擎、数据解析、数据适配等等。

为了更清晰的探讨和分析 JSMVC 的实现，非常必要对 MVC 在 JS 中的职责做一番梳理。

## JSMVC

### JSMVC 职责划分

* M 模型（数据和业务）

  * 业务模型：业务逻辑、流程、状态、规则
  * 数据模型（核心）：业务数据、数据校验、增删改查（Ajax、RESTful）

*  V 视图（UI）

  * 视图（核心）：定义、管理、配置
  * 模板：定义、配置、管理
  * 组件：定义、配置、管理
  * 交互事件（核心）：配置、管理
  * 输入：校验、配置、管理
  * 输出：更新

* C 控制器/分发器

  * 事件分发（核心）、模型分发、视图分发
  * 不做数据处理和业务处理，即业务无关
  * 扩展：权限控制、异常处理等
  * C 是 JSMVC 框架的核心，实现集中式配置和管理，并且可以有多个控制器

* 工具库

  * 主要是异步请求、DOM 操作，可以依赖于 jQuery 等库

### JSMVC 实现探讨

MVC 的模型 Model、视图 View、控制器 Control 相互独立又相互联系，C 则是作为其中联系的桥梁。

MVC 作为由来已久的成熟开发模型，已有大量经典的实现可供参考，在浏览器和 JS 这个新的特定应用场景中，我们权做如下探索：

* **M** 模型是自包含的，可以嵌套包含，不会主动引用视图和控制器；可以是简单的 JSON 对象/数组，也可以用组合模式 Composite 实现嵌套包含。
* **V** 视图是嵌套包含的，可以用组合 Composite 实现；视图需要引用模型（M-V），一个视图可以引用一个或多个模型，视图会收到模型的通知并自动更新，可以用观察者模式 Observer 实现；视图需要响应用户的交互，可以使用浏览器事件模型实现。
* **C** 控制器作为 MVC 框架关注的核心，采取集中配置的策略（V-C）；可以有多个控制器（C + C），用策略模式 Strategy 实现；hash 事件驱动则需要用到浏览器的事件模型。

M 模型和 C 控制器之间（M-C）一般我认为是不需要关联的；但是在有的框架中实现了 M 模型和 C 控制器的关联（例如一淘在用的 [Magix](https://github.com/limu/magix)），也是一类值得参考和启发的实践。

### 事件驱动

前面的小节中，我们形而上学的从理论上分析了模型 M、视图 V、控制器 C 在 JS 中的职责定位以及它们之间的引用关系，并尝试着用设计模式来探索和诠释 JSMVC 框架的实现思路。

此外，在学习 JSMVC 的过程中，还要认识到 JSMVC 的运行方式是基于事件驱动，这一点非常之重要，本节对在浏览器中可能用到的事件做简练的说明。

在浏览器中，JSMVC 会用到三类事件，分别对应着三种事件驱动方式：

1.  hash 事件，即 popstate/hashchange 事件，绑定在 window 对象上，用来驱动控制器。hash 变化触发 popstate/hashchange 事件之后，控制器根据配置找到相应的回调函数并执行；配置是指存有 hash 与回调函数的映射关系的 Map 对象。

    这个过程称为“hash驱动控制器”，在 Backbone 中由 Router 和 History 共同实现。

2.  DOM 事件，即我们熟知的 click、focus 等浏览器事件，用来响应用户操作、实现交互。DOM 事件被绑定在视图 View上，特别的是 Backbone 提倡采用集中配置的方式，例如下面的代码：

        events: {
            "click .check"              : "toggleDone",
            "dblclick div.todo-text"    : "edit",
            "click span.todo-destroy"   : "clear",
            "keypress .todo-input"      : "updateOnEnter"
        }

    这个过程称为“DOM 事件驱动视图“，在 Backbone 中由 View 实现，其中事件的绑定、触发、销毁则依赖于 jQuery 等第三方库。

3.  模型事件，包括业务模型事件和数据模型事件，用来驱动模型以及模型集合，实现模型和视图之间的观察者模式。
    这个过程称之为”模型驱动“，在 Backbone 中由 Model、Collection、Event 共同实现。

### 应该关注什么

框架最应该关注的是控制器 C，部分视图 V。

框架用户则主要关注模型 M 和视图 V，即业务、数据以及展示，并关注模型 M 的复用和视图 V 的变化。

## Backbone

### Backbone 架构

![](/project/mvc/Backbone.png)

#### 参考资料

* 基于 [Backbone 0.9.1](https://github.com/documentcloud/backbone/tree/0.9.1)
* [官方文档](http://documentcloud.github.com/backbone/)
* [中文翻译](http://www.csser.com/tools/backbone/backbone.js.html)

#### 官网介绍

Backbone 通过提供模型 Model、集合 Collection、视图 View 赋予了 Web 应用程序分层结构。

通过以下方式实现分层结构：

* 模型 Model 绑定键值数据和自定义事件。
* 集合 Colection 是模型的有序或无序集合，带有丰富的可枚举 API。
* 视图 View 声明事件监听函数。
* 将模型、集合、视图与服务端的 RESTful JSON 接口连接。

#### 自调用匿名函数

整个 Backbone 的源码用一个自调用匿名函数包裹，通过闭包特性引用变量（例如 previousBackbone、slice、splice 等），同时避免污染全局命名空间。

整体结构如下，还是很清晰的：

    (function() {
        Backbone.Events     // 自定义事件
        Backbone.Model      // 模型构造函数和原型扩展
        Backbone.Collection // 集合构造函数和原型扩展
        Backbone.Router     // 路由配置器构造函数和原型扩展
        Backbone.History    // 路由器构造函数和原型扩展
        Backbone.View       // 视图构造函数和原型扩展
        Backbone.sync       // 异步请求工具方法
        var extend = function (protoProps, classProps) { ... } // 自扩展函数
        Backbone.Model.extend = Backbone.Collection.extend = Backbone.Router.extend = Backbone.View.extend = extend; // 自扩展方法
    }).call(this);

#### 依赖库

Backbone 必须依赖于 Underscore.js，DOM 操作和 Ajax 请求依赖于第三方 jQuery/Zepto/ender 之一，也可以通过方法 `Backbone.setDomLibrary( lib )` 设置其他的第三方库。

#### 自定义事件模块 Backbone.Events

可以和任意对象合体（将方法赋值到其他对象或原型上），合体后的对象支持自定义事件，提供了三个方法来绑定、移除、触发自定义事件：

    on(events, callback, context)   // 绑定一个或多个事件回调函数
    off(events, callback, context)  // 移除一个或多个事件回调函数
    triggle(events)                 // 触发一个或多个事件回调函数

方法功能和调用关系如下图所示：

![](/project/mvc/Backbone.Events.png)


#### 模型 Backbone.Model

模型是 JavaScript 应用程序的核心，包含了业务数据以及对业务数据的读写和持久化，模型的主要方法包括读写和持久化：

    // 初始化
    initialize()                // 执行构造函数时会被自动调用     

    // 读写
    _validate(attrs, options)   // 验证属性集
    hasChanged(attr)            // 判断模块是否改变
    change(options)             // 手动触发一个change事件
    get(id)                     // 返回一个属性的值
    escape(attr)                // 获取一个属性的HTML转义后的值
    has(attr)                   // 是否含有某个属性（有效值）
    set(key, value, options)    // 设置或删除模块属性散列表
    unset(attr, options)        // 删除一个属性
    clear(options)              // 清除模块的所有属性

    // 持久化
    url()                       // 模块在服务端对应的URL
    fetch(options)              // 从服务器获取模块
    save(key, value, options)   // 将模块同步到服务器，create or update
    destroy(options)            // 在服务器上销毁这个模块

支持的事件包括：

    change:attr
    chage
    sync
    destory
    error

方法功能和调用关系如下图所示：

![](/project/mvc/Backbone.Model.png)

#### 集合 Backbone.Collection

集合是模型的有序集合，可以在集合上绑定 "change" 事件，当集合中的任意模型发生变化时将收到通知，集合也可以监听 "add" 和 “remove" 事件，从服务器获取数据，并能使用 Underscore.js 提供的全套方法。为了方便，在集合中的模型上触发的任何事件都会在集合上直接触发。这样就可以监听集合中模型的指定属性的变化。 例如：Documents.on("change:selected", ...)。

集合的主要方法包括读写、维护和持久化：

    // 初始化
    initialize() // 执行构造函数时会被自动调用

    // 读写、维护
    add(models, options)    // 添加一个一组模型对象到集合中
    remove(models, options) // 从集合中移除一个或一组模型对象
    get(id)                 // 通过id获取模型对象
    getByCid(cid)           // 通过客户端id返回模型对象
    sort(options)           // 强制集合排序
    reset(models, options)  // 重置整个集合
    _reset(options)         // 重置所有状态
    _prepareModel(model, options) // 创建一个模型，用以添加到这个集合中
    _removeReference(model) // 移除模块与集合的关系
    _onModelEvent(ev, model, collection, options) // 集合中的元素每次触发事件时内部调用的方法

    // 持久化
    fetch(options)          // 获取集合的默认模块对象集合
    create(model, options)  // 在集合中创意一个新模型实例
    parse(resp, xhr)        // 将响应转换为模型对象列表
    // 其他借用 Underscore 的工具方法，借鸡生蛋

支持的事件包括：

    add
    remove
    reset
    sync
    error
    (change:attr, chage, sync, destory)

方法功能和调用关系如下图所示：

![](/project/mvc/Backbone.Collection.png)

#### 路由配置器 Backbone.Router

Web 应用程序通常需要为重要页面提供可链接、收藏、可分享的 URL。直到最近， 锚文片段（hash #page）可以被用来提供这种固定链接；同时随着 History API 的到来，锚文现在可以用于处理标准 URLs（/page）。

Backbone.Router 为客户端页面路由提供了许多方法，并能连接到指定的动作（actions）和事件（events）。

对于不支持 History API 的旧浏览器（IE6、IE7），路由器提供了优雅的回调函数并可以透明的进行 URL 片段的转换。

页面加载期间，当应用程序已经创建了所有的路由表，需要调用 Backbone.history.start() 或 Backbone.history.start({pushState : true}) 来确保路由初始 URL。

提供了的主要方法有：

    initialize()                 // 初始化，执行构造函数时会被自动调用。
    route(route, name, callback) // 手动绑定一个路由 到 一个回调函数
    navigate(fragment, options)  // 手动到达应用程序中的某个位置
    _bindRoutes()                // 绑定所有定义的映射关系给Backbone.history
    _routeToRegExp(route)        // 将虚拟URL转换为正则表达式，用于与当前路径的hash部分匹配
    _extractParameters: function(route, fragment) // 正则匹配URL片段fragment，取出其中的参数部分

支持的事件包括：

    route:name
    route

#### 路由器 Backbone.History

作为全局路由器，用于处理 hashchange 或 pushState 事件，匹配适合的路由表，并触发回调函数。

如果使用带有路由表的路由器，会自动创建一个 History 对象，此时，不要再创建一个 History 对象，而是直接使用 Backbone.history。

Backbone 会自动判断浏览器对 pushState 的支持，以做内部的选择。不支持 pushState 的浏览器将会继续使用基于锚点的 URL 片段。

提供的主要方法有：

    start(options)              // 开始监听hash变化（绑定popstate事件 或 绑定hashchange事件 或 通过定时器监听hash变化）
    stop()                      // 临时性的停止Backbone.history
    route(route, callback)      // 添加映射关系
    checkUrl(e)                 // 检查当前URL是否已改变，如果已改变，调用loadUrl
    loadUrl(fragmentOverride)   // 检查是否有路由匹配
    navigate(fragment, options) // 保存URL片段到锚文历史（history.replaceState 或 history.pushState 或 location.replace 或 location.hash）
    _updateHash(location, fragment, replace) // 更新锚文路径（location.replace 或 location.hash）

方法功能和调用关系如下图所示：

![](/project/mvc/Backbone.Router+History.png)

#### 视图 Backbone.View

视图的使用相当方便，不需要判断任何 HTML、CSS，可以和任意 JavaScript 模板引擎集成。

通用的做法是，将界面组织成基于模型的逻辑视图，当模型改变时视图立即更新，而不需要重画整个页面。

不再需要纠结于 JSON 对象、查找 DOM 元素、手动更新 HTML，只需把视图 render 方法绑定到模型的 change 事件，模型数据会立即更新到界面上。

方法功能和调用关系如下图所示：

![](/project/mvc/Backbone.View.png)

#### 扩展方法 extend

模型、集合、视图、路由器都含有一个 extend(protoProps, classProps) 方法，用于扩展原型属性和静态属性，创建自定义的视图、集合、视图、路由器类。


### 事件 Event - 最佳基友

> TODO 概述、使用、流程、事件、源码

### 模型 Model - 自娱自乐

> TODO

### 集合 Collection - 不是一个人在战斗

> TODO

### 视图 View - 能者多劳

> TODO

### 控制器 Route + History - ？

> TODO

### Backbone 插件

* [Backbone.Subviews](https://github.com/rotundasoftware/backbone.subviews)
  * A minimalist view mixin for creating and managing named subviews (views within views) in your Backbone.js applications.
* [Backbone.Courier](https://github.com/rotundasoftware/backbone.courier)
  * Easily bubble events ("messages") up your view hierarchy in your Backbone.js applications.

### 可以学习的编码技巧 - 上士闻道

1. 字符串用单引号包裹，提高编码效率（高效）。
2. 将对象包装成数组，统一处理，砍掉对象，什么都是数组的编程思想（多功能）。
3. 总是预留一个选项对象，函数根据选项中的属性执行不同的逻辑（可扩展，增加策略）。
4. 复制选项对象，避免在执行过程中改变选项对象中的属性，影响外围函数的执行逻辑（高内聚）。
5. 等待策略：决定是立即在浏览器中生效，还是等到服务器响应根据响应结果决定是否生效（便于测试）。
6. 细致的事件类型：应用开发虽然用不到，但是利于插件或基于 Backbone 开发。
7. 设计模式：MVC模式、观察者模式。


### 可以改进或扩展的地方 - 三省她身

1. 对其他库的依赖：jQuery/Zepto/Ender，Underscore，最讨厌库依赖！
2. 深受 Rails 的影响，与 MVC 的理解和实现必然有其局限性，不过是一家之言。
3. 仅仅是对 JSMVC 框架的探索，没有实现诸如嵌套模型、嵌套集合、嵌套视图的管理，虽然有诸多插件，但这又造成更多的依赖，诸多原因局限了它在实际项目中的应用，处于探索不成熟阶段。
4. 代码行数不多且容易理解，是学习 JSMVC 的很好示例，但是会导致更多的工程师学习并创造自己的 MVC 框架（比如我、我所在的团队），一个不是革命性的框架导致的诸多模仿者，会让 MVC 框架更加泛滥（看看其他语言的发展历史，总是在重复）。


### 待分类

1. 使用了大量有副作用的表达式、语句，比如
    布尔表达式
    在 if 中调用设置方法
2. 所有的方法都预留一个 options 对象参数，用于存放可以改变方法行为的参数。
3. 将工具函数underscore和backbone分离，underscore负责提供基础工具函数，backbone则负责实现MVC框架；这种分离有利于两个库的复用。可以集成第三方库。
4. 关于回调函数和触发事件的二选一，如果设置回调函数则不触发事件，未设置回调函数才会触发事件；这样会减少重复响应，在框架这一级避免出现这样的bug，更健壮，不会让新手遇到莫名其妙的问题。

### Backbone 发布记录

* [Backbone Change Log](http://backbonejs.org/#changelog)
* [Backbone Tags](https://github.com/documentcloud/backbone/tags)

## AngularJS

## Knockout

## Meteor

## Ember.js


## 何谈理解

在很多文章中会提到，学习开源框架最重要的学习它的思想、架构，这应该是最终的目标，也是最初的动机，但这两个境界截然不同。

姑且分为一、二、三层境界，第一层为了解思想架构，第二层为熟读源码细节，深刻体会思想架构；第三层将思想架构融入自己的体系和实践，收为己有运用自如。

大部分源码分析的文章和书籍局限于第一层，可以帮助写出更好的应用。

一小部分工程师会细致的钻研每一行源码，他们更接近框架的本质，学习实现的技巧，抄袭然后美名自创一套。

第三层已经跳出学习既有框架的范畴，本人高度不足没有体会，不想它。

大部分的熟练工停留在第一层，大部分的高手停留在第二层，可怕的不是无知，可怕的意识不到。在你走到更高的层次之前，你不会有更高的觉悟。而这个过程，没有捷径。

不深入何谈理解，引以为戒，与君共勉。


## Backbone 过时了吗？

不是潮流不一定就是过时。


## 修订记录

版本、日期、编制人、说明、行为、备注

**nuysoft 2012-02-18 0.01**

* 文档结构，前言、技巧

**nuysoft 2013-01-31 0.02**

* 转换为 Markdown 格式

**nuysoft 2013-03-07 0.03**

* 增加代码块
* 美化图片

**nuysoft 2013-03-21 0.04**

* 校对已有内容

**nuysoft 2013-03-22 0.05**

* 增加参考资料、参考库&框架

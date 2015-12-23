# Angular.js Basic
## Angular.js几个重要的核心的概念
- Data-bind : automatic bind view and model component
- Scope: A glue between controller and view
- Controller: javascript bind to a particular scope
- Services: singleton object which are instantiated only once in app
- Filters: filter to get subset of items
- Directives: markers on DOM, create customer tags
 default bind: ngBind,ngModel
- Tempaltes: 模板，HTML片段
- Routing: switching views
- Model View Whatever: MVVM: Model-View-ViewModle
- Deep Linking: restore application state
- Dependency Injection: 依赖注入，可以方便的创建实例，测试

## Anglular.js模块
- Data Binding
- Scope
- DI
- Filters
- Services
- Factories
- Expressions
- Providers
- Validators
- Directives
- Controllers
- Modules

## AngularJS Directives
- ng-app: app in HTML
- ng-model: data to HTML input tag
- ng-bind : data to tag

## Hello Angular.js
- ng-app 申明了一个angular app 作用域
- {{ }} agular model 表达式
- 数据双向绑定 model in js

``` html
   <div class="container">
        <div class="row">
            <input type="text" ng-model="yourname" placeholder=”angular“ />
            <p>Hello {{ yourname }}  World!!!</p>
        </div>
    </div>
```

如果改动input 里面的内容，下面文字跟着以前改变

## Angular 创建
- app module binding
- View binding
- Controller binding

创建Angular.js html文件如何被加载：
1. 浏览器下载HTML文件
2. js 文件被加载
3. controller文件被加载
4. 获取views,并且联系view和controller
5. 执行controller函数
6. 渲染views,填入数据

## Angular MVC
- Model - It is the lowest level of the pattern responsible for maintaining data.
- View - It is responsible for displaying all or a portion of the data to the user.
- Controller - It is a software Code that controls the interactions between the
Model and View.

## Angular js Directives

- ng-app
- ng-init
- ng-model
- ng-repeat
- ng-bind

### Expression
- {{ }}
- 可以是单独的字段，可以是list，可以是用JSON表示的key-value 对

### Controller
可以定义数据模型，可以定义转换函数，可以实现页面数据逻辑
### Filter
- pipeline “|” 可以认为是一个后置函数，filter函数
- uppercase/lowercase
- filter:filter => filter:subjectName
- Orderby Filter => orderBy:whichOne

### Table
- ng-repeat for draw table with data

### HTML DOM
- ng-disabled
- ng-show
- ng-hide
- ng-click

## Modules
- application Module
- controller Module

### forms
```
- ng-click
- ng-dbl-click
- ng-mousedown 
- ng-mouseup
- ng-mouseenter 
- ng-mouseleave 
- ng-mousemove 
- ng-mouseover 
- ng-keydown
- ng-keyup
- ng-keypress
- ng-change
```

### Includes
### Ajax
- $http controller

### Views
- ng-view
- ng-template

## Sample 

ng-model and expression {{}} => data binding
ng-model/ng-app => directive

```html
<!DOCTYPE html>
<html ng-app>
<head lang="en">
    <meta charset="UTF-8">
    <title>angular_101</title>
    <link rperformanceel="stylesheet" href="../css/bootstrap.min.css"/>
    <link rel="stylesheet" href="../css/bootstrap-theme.min.css"/>
</head>
<body>
<div class="container">
    Name:<input type="text" ng-model="name">
    {{name}}
</div>
<script src="../js/angular.min.js"></script>
</body>
</html>
```

# Vue.js 入门
[Vue.js](http://cn.vuejs.org/guide/)是用于创建web交互界面的库。它专注于MVVM的ViewModel
层，通过双向数据绑定(two way data binding)将view和model层连接起来,而实际的DOM封装和输出格式都被抽象
为Directives,Filter.

概念综述：
[!img](http://cn.vuejs.org/images/mvvm.png)

## ViewModel
一个同步的Model和View对象，在Vue.js,每个Vue实例都是一个ViewModel。通过构造函数：
```js
  var vm = new Vue({/*options*/});
```

## View
被Vue实例管理的DOM节点：

```js
  vm.$el
```
## Model
```js
vm.$data
```
数据对象属性都转换为ES5的getter／setter属性，一旦一个对象被观察```{a:1}```,那么```vm.$data.a```
和```vm.a```将返回相同值，修改则会修改```vm.$data```
值得提醒的是，一旦数据被观察，Vue.js 就不会再侦测到新加入或删除的属性了。
作为弥补，我们会为被观察的对象增加 ```$add```,``` $set```和 ```$delete ``` 方法。

Vue.js数据观测机制：
[!img](http://cn.vuejs.org/images/data.png)

## Directives
带特殊前缀的 HTML 特性，可以让 Vue.js 对一个 DOM 元素做各种处理。
```HTML
<div v-text="message"></div>
```
Directives 可以封装任何 DOM 操作。比如 v-attr 会操作一个元素的特性；
v-repeat 会基于数组来复制一个元素；v-on 会绑定事件等。
个指令的本质是模板中出现的特殊标记，让处理模板的库知道需要对这里的 DOM 元素进行一些对应的处理。

```html
<element
  prefix-directiveId="[argument:] expression [| filters...]">
</element>
```
### Directives-Simple example

```html
  <div v-text="message"></div>
```
这里的前缀是默认的 v-。指令的 ID 是 text，表达式是 message。这个指令告诉 Vue.js， 当 Vue 实例的 message 属性改变时，更新该 div 元素的 textContent。

### Directives-inline expression
```html
<div v-text="'hello ' + user.firstName + ' ' + user.lastName"></div>
```
这里我们使用了一个计算表达式 (computed expression)，而不仅仅是简单的属性名。Vue.js 会自动跟踪表达式中依赖的属性并在这些依赖发生变化的时候触发指令更新。
同时，因为有异步批处理更新机制，哪怕多个依赖同时变化，表达式也只会触发一次。
如果需要绑定更复杂的操作，请使用计算属性

### Directives-parameters
```html
<div v-on="click : clickHandler"></div>
```
绑定了click事件，方法是clickHandler

### Directives-filters
一个 Vue.js 的过滤器本质上是一个函数，这个函数会接收一个值，将其处理并返回,可以认为一个流式操作。
过滤器在指令中由一个管道符 (|) 标记，并可以跟随一个或多个参数：

```html
<element directive="expression | filterId [args...]"></element>
```

1. function:
```html
<span v-text="message | capitalize"></span>
<span>{{message | uppercase}}</span>
<span>{{message | lowercase | reverse}}</span>
```
2. parameters:
```html
<span>{{order | pluralize 'st' 'nd' 'rd' 'th'}}</span>
<input v-on="keyup: submitForm | key 'enter'">
```
### Directives-multiple commands
多个事件绑定：
```html
<div v-on="
  click   : onClick,
  keyup   : onKeyup,
  keydown : onKeydown
">
</div>
```

### Directives-literal
```html
<my-component v-ref="some-string-id"></my-component>
```
### Directives- empty command

```html
<div v-pre>
<!-- 内部模板将不会被编译 -->
</div
```


## Mustache 风格绑定
```html
<div id="person-{{id}}">Hello {{name}}!</div>
```
escape html代码：

```html
{{{ safeHTMLString }}}
```

onlyOnce:
```js
{{* onlyOnce }}
```

## Filters
过滤器是用于在更新视图之前处理原始值的函数。它们通过一个“管道”在指令或绑定中进行处理

```html
 <div>{{message | capitalize}}</div>
```

## Components
[!img](http://cn.vuejs.org/images/components.png)
在 Vue.js，每个组件都是一个简单的 Vue 实例。一个树形嵌套的各种组件就代表了你的应用程序的各种接口。通过 Vue.extend 返回的自定义构造函数可以把这些组件实例化，不过更推荐的声明式的用法是通过 Vue.component(id, constructor) 注册这些组件。一旦组件被注册，它们就可以在 Vue 实例的模板中以自定义元素形式使用了。

```html
<my-component>
  <!-- internals handled by my-component -->
</my-component>
```

## simple-demo

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Simple Vue.js Guide</title>
</head>
<body>
<div id="demo">
    <h1>{{title | uppercase }}</h1>
    <ul>
        <li v-repeat="todos"
            v-on="click: done=!done"
            class="{{done? 'done':''}}">
            {{content}}
        </li>
    </ul>
</div>

<script src="../../bower_components/vue/dist/vue.min.js"></script>
<script>
    var demo=new Vue({
       el: '#demo',
        data:{
            title: "Vue.js guide",
            todos:[
                {
                    done:true,
                    content: "first one"
                },
                {
                    done:false,
                    content:"second one"
                }
            ]
        }
    });
</script>
</body>

</html>
```

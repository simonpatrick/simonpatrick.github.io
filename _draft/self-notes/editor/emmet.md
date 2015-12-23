# EMMET

## 自动补全

### 没有特殊字符
输入：
``` html
 title
```
tab补全：
```html
<title></title>
```

### {} text

```html
	title{hello}
```

```html
	<title>hello</title>
```

### ```#``` id

```html
	title#hello
```

```html
	<title id="hello"></title>
```

### ```.``` class
```html
title.hello
```

```html
<title class="test"></title>
```

### ```*``` plus

```html
title.test$*3
```
```html
<title class="test1"></title>
<title class="test2"></title>
<title class="test3"></title>
```

### ```[]``` attribute
```html
title[href='a.html']
```

```html
<title href="a.html"></title>
```

### ```+```平级

```html
        dl>dt{title;}+dd>input[type="text" size="30" name="title"] 
```

```html
<dl>
            <dt>title;</dt>
            <dd><input size="30" name="title" type="text"/></dd>
        </dl>
```
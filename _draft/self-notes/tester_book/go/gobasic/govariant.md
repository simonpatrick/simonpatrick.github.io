# Go:Variant
## Variant 简介
Go 定义变量不是 int a， 而是a int. 而赋值是 ```:=```或者```=```来实现.

## Variant实例
- example1: a 初始化默认值是0，s 默认是""
```go
var a int
var b bool
var s string
a = 15
b = false
```
- example2: 声明和赋值同时完成
```go
a:=15
b:=false
```

- example3:多个变量声明和赋值
```go
var {
    x int
    y bool
}
```

```go
var x,y int
x,y : 20,16
```

## Variant 特别提示
- ```_``` 变量的值都会被丢弃
- 未使用的变量会报错

```go
package main

func main() {
	var i int
}

```
error 提示：
```
./variant_error.go:4: i declared and not use
```




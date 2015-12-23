# Go:ControlFlow

go 里面没有do/while循环，只有for；switch 和if还是存在.

## if-else

``` go
if x>0 {  //{是强制的 并且必须和if同行
    return y
}else{
    return x
}
```

## goto

大小写敏感

```go

func func1() {
	i := 1
Here:
	fmt.Printf("%d", i)
	i++
	if i > 10 {
		return
	}

	goto Here
}
```

## for
for 的三种形式:
- for init;condition;post{}
- for condition {} -- while
- for {}

## break and continue
almost same as other languages，嵌套循环break需要指定是那个循环

## range

range是个迭代器

## switch
更加灵活，可以支持表达式




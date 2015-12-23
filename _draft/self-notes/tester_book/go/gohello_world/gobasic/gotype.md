# Go:Type

## bool
true or false

## number (todo: need to confirm if it named as number type)
- int8,int16,int64,int32
- byte,unit8,unit16,unit32,unit64

## 常量 constant
只能是数字，字符串或者布尔值
``` go
const x = 10
```
## 字符串 string

UTF-8的双引号""表示字符串，单引号表示一个字符(UTF-8）
```go
s:="Hello World"

```
## rune

rune是int32的别名，循环每个字节的时候会使用到

## 复数
complex128(64位虚数部分)，使用```re+imi```表示

## 错误 error

## Type实例

- 混合类型编译出错

```go
package main

func main() {
	var a int
	var b int32
	a = 15
	b = a + a  //error raised
	b = b + 5  //error raised
}
```

- 常量定义

```go
const {
    a = iota //a=0
    b //b=1
}

const {
    a =0
    b string ="0"
}
```

- 多行输入

```go
package main

import (
	"fmt"
)

func main() {

	s := "hello world"
	c := []rune(s)
	c[0] = 'c'
	s2 := string(c)
	fmt.Printf("%s\n", s2)

	//multiple line input
	s3 := "Line1" +
		"Line2"
	fmt.Printf("%s\n", s3)

	s4 := "Line1"
	+"Line2" //error here
	fmt.Printf("%s\n", s4)
}

```

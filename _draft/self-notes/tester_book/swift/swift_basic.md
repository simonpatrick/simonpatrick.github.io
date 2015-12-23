# SWIFT BASIC

## Introduction
- 简单值（simple Value）
swift变量的常用使用：

```swift
print("hello world")
// 常量，不能改变
let myVariable = 42
// 变量，可以改变
var myVariable = 11
myVariable =12
//类型自动推断
let implicityInteger = 70
let implicityDouble=70.0
let explictityDouble:Double = 70

//类型转换
var test_message_1=1
println("this is for testing message \(test_message_1)")

//数组和字典使用[]
var shoppingList=["catfish","water","tulips","blue paint"]
println(shoppingList[0])

var occupations=["Malcolm":"Captain","Kaylee":"Mechanic"]
println(occupations["Malcolm"])

//空数组或者字典
let emptyArray=[String]()
let emptyDict=[Stirng:Float]
//类型推断
let emptyDict=[:]

```
- 控制流
  * if/switch 进行条件操作
  * for-in,for,while,do-while 进行循环

```swift

```

- 函数和闭包
- 对象和类
- 枚举和结构体
- 协议和扩展
- 泛型

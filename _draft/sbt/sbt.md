# Scala SBT

## Install

```sh
    brew install scala
    brew install sbt

```

安装结束后的目录一般是在：

## SBT目录机构

类似于MAVEN

```
src/
  main/
    resources/
       <files to include in main jar here>
    scala/
       <main Scala sources>
    java/
       <main Java sources>
  test/
    resources
       <files to include in test jar here>
    scala/
       <test Scala sources>
    java/
       <test Java sources>
```
## SBT  构建定义文件

build.sbt

构建产品

构建出来的文件（编译的 classes，打包的 jars，托管文件，caches 和文档）默认写在 target 目录中。

配置版本管理

你的 .gitignore 文件（或者其他版本控制系统等同的文件）应该包含：

target/
注意：这里后面需要跟一个 / （只匹配目录）且前面不能有 / （除了匹配普通的 target/ 还匹配 project/target/ ）

## 交互方式

命令:
- sbt
- compile
- sbt clean compile "testOnly TestA TestB"
- ~ compile

clean	删除所有生成的文件 （在 target 目录下）。
compile	编译源文件（在 src/main/scala 和 src/main/java 目录下）。
test	编译和运行所有测试。
console	进入到一个包含所有编译的文件和所有依赖的 classpath 的 Scala 解析器。输入 :quit， Ctrl+D （Unix），或者 Ctrl+Z （Windows） 返回到 sbt。
run <参数>*	在和 sbt 所处的同一个虚拟机上执行项目的 main class。
package	将 src/main/resources 下的文件和 src/main/scala 以及 src/main/java 中编译出来的 class 文件打包成一个 jar 文件。
help <命令>	显示指定的命令的详细帮助信息。如果没有指定命令，会显示所有命令的简介。
reload	重新加载构建定义（build.sbt， project/*.scala， project/*.sbt 这些文件中定义的内容)。在修改了构建定义文件之后需要重新加载。

!	显示历史记录命令帮助。
!!	重新执行前一条命令。
!:	显示所有之前的命令。
!:n	显示之前的最后 n 条命令。
!n	执行 !: 命令显示的结果中下标为 n 的命令。
!-n	执行从该命令往前数第 n 条命令。
!string	执行最近执行过的以 string 打头的命令。
!?string	执行最近执行过的包含 string 的命令。

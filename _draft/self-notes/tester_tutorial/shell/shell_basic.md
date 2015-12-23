# SHELL Basic
## 传递参数
- $1 表示参数1，$2表示参数2
- $# 表示参数的个数
- $* 表示获取全部参数
- $@: 获取全部参数

```shell
p=$1
echo p
echo $p
echo "$p"
echo "{$p}"
echo "\%p"
```
运行此脚本传递参数为test，猜猜结果是什么？？

```shell
p
test
test
{test}
$p
```
根据结果，看官您能得出什么结论呢？
- $ 什么作用？
- 转义如何做？



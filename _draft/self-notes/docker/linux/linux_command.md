# Linux Command
## netstat
- netstat -an |grep 5000

## lsof
lsof :list open files

- lsof -i:5000

|table|description|
|-------|-----------|
|command|进程名称|
|pid|进程id|
|user|进程拥有者|
|fd|文件描述符|
|type|文件类型|
|device|磁盘名称|
|size|文件大小|
|node|索引节点|
|name|文件确切名字|
|txt|类型的文件|

## nmap
nmap -sT -O localhost

## ps

ps -aux |grep <port_no>

## port

```shell
lsof -i |grep java
```

## Mac flush dns

```shell
dscacheutil -flushcache
```
# 一个测试的好奇心日记-1 代码review-SQL REVIEW发现的性能小问题

## 引子
由于需要了解日常的业务知识，但是苦于没有文档可以阅读，所以只能从代码走读开始.
代码走读我一般从分如下几个步骤：
- controller开始
- 到service层
- 熟悉数据库表结构
- 查看开发代码的SQL语句

## 发现
今天偶然的阅读开发的mybastis的xml文件时发现了如下的SQL：
```sql
select o.ID as id,o.orgName as orgName
from ***.***.***ganization o with(nolock)
WHERE o.orgType='**' AND EXISTS (select 1 from ***.***.***ganization vo
where vo.id in (?) and o.code like vo.code + '%')
order by orgName;
```

不知道什么原因总觉得哪里不太对，感觉有些诡异，于是就自己改了一段尝试了一下:
```sql
select o.ID as id,o.orgName as orgName from ***.***.***ganization o with(nolock),   
(select vo.orgLongcode from ***.**.***ganization vo where vo.id in (?)) parent 
WHERE o.orgType='分行' and o.code like parent.code+'%' order by orgName;
```

## 验证

上下的比较
 SQL Server 执行时间:
   CPU 时间 = 0 毫秒，占用时间 = 1 毫秒。

 SQL Server 执行时间:
   CPU 时间 = 16 毫秒，占用时间 = 19 毫秒。

## 结果说明
修改后的效果会好很多. 

# Postgre SQL

## Extension
tablefunc,dict_xsync,fuzzystrmatch,pg_trgm,cube

## command

### Create Database
```SQL
 createdb book
```

### execution

```SQL
psql book -c "select '1' ::cube "
```
### index

```SQL
create index
```

### Primary Key

```SQL
create Table countries(
  country_code char(2) PRIMARY Key,
  country_name text unique
)
```

### Insert

```SQL
insert into countries ()
values()
```

### Select

```SQL
select * from table_name
```

### Delete


### 复合主键

```SQL
create Table cities(
  
)
```

## CRUD

## 关系数据库 元组关系演算

- where
- select (投影)
- join(笛卡尔卷积)

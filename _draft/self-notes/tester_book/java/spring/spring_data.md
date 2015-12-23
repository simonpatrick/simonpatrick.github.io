# Spring Data 介绍
spring data的目的是减少大量的访问数据层的代码，
这些代码可以访问不同的数据库，所以spring data 是一个访问数据的抽象层

## Core concept
spring data最核心的是一个Repository的概念，Repository使用id来管理领域对象类.CRUDReposity 提供了更加具体的Repository功能，具体的接口如下：

```java
public interface CrudRepository<T, ID extends Serializable>
    extends Repository<T, ID> {

    <S extends T> S save(S entity); 

    T findOne(ID primaryKey);       

    Iterable<T> findAll();          

    Long count();                   

    void delete(T entity);          

    boolean exists(ID primaryKey);  

    // … more functionality omitted.
}
```

而JpaRepository，MongoRespository则针对特定的持久化功能，而PagingAndSortingRepository则增加了额外分页功能

```java
public interface PagingAndSortingRepository<T, ID extends Serializable>
  extends CrudRepository<T, ID> {

  Iterable<T> findAll(Sort sort);

  Page<T> findAll(Pageable pageable);
}
```

```java
PagingAndSortingRepository<User, Long> repository = // … get access to a bean
Page<User> users = repository.findAll(new PageRequest(1, 20));
```
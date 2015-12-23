# JAVA Functional Try

## JAVA8 Map 用法

map 个人理解就是相当于给集合类里面的每一个元素都做一次指定的操作。
```java
      System.out.println(friends.stream().mapToInt(name->name.length()).sum());

```

而reduce相当于给集合类做了一次过滤
```java
        final Optional<String> aLongName = friends.stream().reduce((name1,name2)->
                name1.length()>=name2.length()?name1:name2);
        aLongName.ifPresent(name-> System.out.println(String.format("longest name: %s",name)));
        final String steveOrLonger = friends.stream().
                reduce("Steve",(name1,name2)->name1.length()>=name2.length()?name1:name2);
        System.out.println(steveOrLonger);
```
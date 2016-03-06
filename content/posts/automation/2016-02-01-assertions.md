---
layout: post
title: "assertions"
modified:
categories: [automation]
image: 11.jpg
tags: [automation]
date: 2016-02-01T23:48:35
---

由于一直都在进行测试的工作，所以会关注Assertion的工具，发现两个不错的Assertion 第三方包，准备在实践中使用. 这两个分别是：
- Google Truth(http://google.github.io/truth/usage/)
- [assertj](http://joel-costigliola.github.io/assertj/)

这个里面有很多自己想实现的比较的功能。一下是一些简单的试用的代码。

## Google Truth

基础的验证：

```java
@Test
  public void test_basic_truth(){
       Set<String> foo = Sets.newHashSet();
       assertThat(foo).isEmpty();
       assertThat(foo).isNotNull();
       assertThat(5).isEqualTo(5L);
       assertThat(5L).isEqualTo(5);
       assert_().that(50).isEqualTo(50);
       assertThat("test").isEqualTo("test");
       assertThat("test").contains("te");
   }
```

Collections/Maps的验证:

```java
@Test
   public void test_basic_truth_maps_collections(){
       Set<String> foo = Sets.newHashSet();
       assertThat(foo).isEmpty();
       assertThat(foo).isNotNull();
       foo.add("test");
       foo.add("test1");
       foo.add("test2");
       assertThat(foo).contains("test");
       assertThat(foo).containsAllOf("test", "test1");
       assertThat(foo).containsExactly("test2", "test", "test1");
       assertThat(foo).containsNoneOf("test889", "test10");

       Map<String,String> maps = Maps.newHashMap();
       maps.put("test", "test1");
       maps.put("test1", "test2");
       maps.put("test2", "test3");
       assertThat(maps).containsKey("test1");
       assertThat(maps).containsEntry("test1", "test2");
       assertThat(maps).doesNotContainEntry("test0", "test0");
   }
```

## assertj

基础的验证：

```java
@Test
 public void test_contains(){
     assertThat("aaa").contains("aa");
 }

 @Test
 public void test_list_contains(){
     List<String> result = Lists.newArrayList("abcd","ddds","ttest");
     assertThat(result).contains("ddds");
 }
 @Test
 public void test_list_contains_onlyonce(){
     List<String> result = Lists.newArrayList("abcd","ddds","ttest");
     assertThat(result).containsOnlyOnce("ddds");
 }

 @Test
     public void test_list_contains_ELementOf(){
     List<String> result = Lists.newArrayList("abcd","ddds","ttest");
     assertThat(result).containsExactlyElementsOf(Lists.newArrayList("abcd", "ddds", "ttest"));
 }
```

Guava 的验证：

```java
@Test
   public void MultiMap_assertions() {
       Multimap<String, String> actual = ArrayListMultimap.create();
       actual.putAll("Lakers", newArrayList("Kobe Bryant", "Magic Johnson", "Kareem Abdul Jabbar"));
       actual.putAll("Spurs", newArrayList("Tony Parker", "Tim Duncan", "Manu Ginobili"));

       assertThat(actual).containsKeys("Lakers", "Spurs");
       assertThat(actual).contains(entry("Lakers", "Kobe Bryant"),
               entry("Spurs", "Tim Duncan"));
   }

   @Test
   public void multiple_set_assertions() {
       Multimap<String, String> listMultimap = ArrayListMultimap.create();
       listMultimap.putAll("Spurs", newArrayList("Tony Parker", "Tim Duncan", "Manu Ginobili"));
       listMultimap.putAll("Bulls", newArrayList("Michael Jordan", "Scottie Pippen", "Derrick Rose"));

       Multimap<String, String> setMultimap = TreeMultimap.create();
       setMultimap.putAll("Spurs", newHashSet("Tony Parker", "Tim Duncan", "Manu Ginobili"));
       setMultimap.putAll("Bulls", newHashSet("Michael Jordan", "Scottie Pippen", "Derrick Rose"));

// assertion will pass as listMultimap and setMultimap have the same content
       assertThat(listMultimap).hasSameEntriesAs(setMultimap);

// this assertion FAILS even though both multimaps have the same content
       assertThat(listMultimap).isEqualTo(setMultimap);
   }


   @Test
   public void range_assertions() {
       Range<Integer> range = Range.closed(10, 12);
       assertThat(range).isNotEmpty()
               .contains(10, 11, 12)
               .hasClosedLowerBound()
               .hasLowerEndpointEqualTo(10)
               .hasUpperEndpointEqualTo(12);
   }

   @Test
   public void table_assertion() {
       // Table assertions
       Table<Integer, String, String> bestMovies = HashBasedTable.create();

       bestMovies.put(1970, "Palme d'Or", "M.A.S.H");
       bestMovies.put(1994, "Palme d'Or", "Pulp Fiction");
       bestMovies.put(2008, "Palme d'Or", "Entre les murs");
       bestMovies.put(2000, "Best picture Oscar", "American Beauty");
       bestMovies.put(2011, "Goldene Bär", "A Separation");

       assertThat(bestMovies).hasRowCount(5).hasColumnCount(3).hasSize(5)
               .containsValues("American Beauty", "A Separation", "Pulp Fiction")
               .containsCell(1994, "Palme d'Or", "Pulp Fiction")
               .containsColumns("Palme d'Or", "Best picture Oscar", "Goldene Bär")
               .containsRows(1970, 1994, 2000, 2008, 2011);
   }

   @Test
   public void test_opotions() {
       // Optional assertions
       Optional<String> optional = Optional.of("Test");
       assertThat(optional).isPresent().contains("Test");

       Optional<Long> optionalNum = Optional.of(12L);
       assertThat(optionalNum).extractingValue()
               .isInstanceOf(Long.class)
               .isEqualTo(12L);

        optional = Optional.of("Bill");
// extractingCharSequence allows to chain String specific assertion
       assertThat(optional).extractingCharSequence()
               .startsWith("Bi");

   }
```

日期的验证：

```java
@Test
   public void date_before(){

       DateTime dateTime = new DateTime();
       DateTime firstDateTime = new DateTime();
       firstDateTime.plus(10000L);
       assertThat(dateTime).isBefore(firstDateTime);
       assertThat(dateTime).isAfter("2004-12-13T21:39:45.618-08:00");
       assertThat(dateTime).isAfter("2004-12-13T21:39:00");
       assertThat(dateTime).isAfter("2004-12-13T21:39:00");

   }

   @Test
   public void joda_datetime_compare(){

       DateTime utcTime = new DateTime(2013, 6, 10, 0, 0, DateTimeZone.UTC);
       DateTime cestTime = new DateTime(2013, 6, 10, 2, 0, DateTimeZone.forID("Europe/Berlin"));

       assertThat(utcTime).as("in UTC time").isEqualTo(cestTime);
   }
```

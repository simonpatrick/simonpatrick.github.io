# TestNG 基础应用


## ```@Test```的使用
TestNG是个集成测试框架，所以如何用来做测试，是最关注的用法。和JUNIT一样，TestNG可以使用注解来标注测试类和方法。
```@Test``` 可以使用在Method，Class，Constructor上面。以下是三个例子来说明：

- Method level

```java

public class TestNgQuickStart {

    @Test
    public void allReadyCorrect(){
        assertTrue(true,"always true");
    }
}
```

- Class level

```java
@Test
public class TestNgQuickStartClassLevel {


    public void allReadyCorrect(){
        assertTrue(true,"always true");
    }

    public void allReadyCorrect_01(){
        assertTrue(true,"always true");
    }
}
```

- Constructor

在构造函数上面加@Test，很少会用到，同时似乎加了也没有什么影响

## 常用TestNg的Annotation的使用
常用的Annotation有BeforeClass，BeforeSuite，AfterClass，AfterSuite，DataProvider等。以下一个例子让你明白这些注解的执行顺序:

```java

    @BeforeClass
    public void beforeClass(){
        System.out.println("Before Class");
    }

    @BeforeSuite
    public void beforeSuite(){
        System.out.println("Before Suite");
    }

    @BeforeTest
    public void beforeTest(){
        System.out.println("Before Test");
    }
    @BeforeMethod
    public void beforeMethod(){
        System.out.println("Before Method");
    }
    @AfterClass
    public void afterClass(){
        System.out.println("After Class");
    }

    @AfterTest
    public void afterTest(){
        System.out.println("after test");
    }
    @AfterMethod
    public void afterMethod(){
        System.out.println("after method");
    }
    @AfterSuite
    public void AfterSuite(){
        System.out.println("After Suite");
    }

    @Test
    public void allReadyCorrect(){
        System.out.println("start testing");
        assertTrue(true,"always true");
    }
```

结果是不是可能和想的不太一样，不过这样子一试也就知道了大概的执行顺序:

```shell
Before Suite
Before Test
Before Class
Before Method
start testing
after method
After Class
after test
After Suite
```

## annotation 说明列表

<table>
<thead>
<tr>
<th></th>
<th>TestNG 类的配置信息</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>@BeforeSuite</strong></td>
<td>
<strong>@BeforeSuite</strong>: 被注解的方法，会在当前<code>suite</code>中所有测试方法之 前 被调用。</td>
</tr>
<tr>
<td><strong>@AfterSuite</strong></td>
<td>
<strong>@AfterSuite</strong>: 被注解的方法，会在当前suite中所有测试方法之 后 被调用。</td>
</tr>
<tr>
<td><strong>@BeforeTest</strong></td>
<td>
<strong>@BeforeTest</strong>: 被注解的方法，会在测试（原文就是测试，不是测试方法）运行 前 被调用</td>
</tr>
<tr>
<td><strong>@AfterTest</strong></td>
<td>
<strong>@AfterTest</strong>: 被注解的方法，会在测试（原文就是测试，不是测试方法）运行后 被调用</td>
</tr>
<tr>
<td><strong>@BeforeGroups</strong></td>
<td>
<strong>@BeforeGroups</strong>: 被注解的方法会在组列表中之前被调用。这个方法会在每个组中第一个测试方法被调用之前被调用</td>
</tr>
<tr>
<td><strong>@AfterGroups</strong></td>
<td>
<strong>@AfterGroups</strong>: 被注解的方法会在组列表中之后被调用。这个方法会在每个组中最后一个测试方法被调用之后被调用</td>
</tr>
<tr>
<td><strong>@BeforeClass</strong></td>
<td>
<strong>@BeforeClass</strong>: 被注解的方法，会在当前类第一个测试方法运行前被调用</td>
</tr>
<tr>
<td><strong>@AfterClass</strong></td>
<td>
<strong>@AfterClass</strong>: 被注解的方法，会在当前类所有测试方法运行后被调用</td>
</tr>
<tr>
<td><strong>@BeforeMethod</strong></td>
<td>
<strong>@BeforeMethod</strong>: 被注解的方法，会在运行每个测试方法之前调用</td>
</tr>
<tr>
<td><strong>@AfterMethod</strong></td>
<td>
<strong>@AfterMethod</strong>: 被注解的方法，会在每个测试方法运行之后被调用</td>
</tr>
<tr>
<td><em>alwaysRun</em></td>
<td>对于在方法之前的调用(<em>beforeSuite, beforeTest, beforeTestClass 和 beforeTestMethod, 除了beforeGroups</em>): 若为<code>true</code>，这个配置方法无视其所属的组而运行.对于在方法之后的调用(<em>afterSuite, afterClass</em>, ...): 若为<code>true</code>， 这个配置方法会运行，即使其之前一个或者多个被调用的方法失败或者被跳过。</td>
</tr>
<tr>
<td>dependsOnGroups</td>
<td>方法所依赖的一组<code>group</code>列表</td>
</tr>
<tr>
<td>dependsOnMethods</td>
<td>方法所依赖的一组<code>method</code>列表</td>
</tr>
<tr>
<td>enabled</td>
<td>在当前<code>class/method</code>中被此<code>annotation</code>标记的方法是否参与测试（不启用则不在测试中运行）</td>
</tr>
<tr>
<td>groups</td>
<td>一组<code>group</code>列表，指明了这个<code>class/method</code>的所属。</td>
</tr>
<tr>
<td>inheritGroups</td>
<td>如果是true，则此方法会从属于在类级由<code>@Test</code>注解中所指定的组</td>
</tr>
<tr>
<td><strong>@DataProvider</strong></td>
<td><strong>把此方法标记为为测试方法提供数据的方法。被此注释标记的方法必须返回<code>Object[][]</code>，其中的每个Object[]可以被分配给测试方法列表中的方法当做参数。那些需要从DataProvider接受数据的<code>@Test</code>方法，需要使用一个<code>dataprovider</code>名字，此名称必须与这个注解中的名字相同。</strong></td>
</tr>
<tr>
<td>name</td>
<td>DataProvider的名字</td>
</tr>
<tr>
<td><strong>@Factory</strong></td>
<td><strong>把一个方法标记为工厂方法，并且必须返回被TestNG测试类所使用的对象们。 此方法必须返回 Object[]。</strong></td>
</tr>
<tr>
<td><strong>@Parameters</strong></td>
<td>说明如何给一个<code>@Test</code>方法传参。</td>
</tr>
<tr>
<td>value</td>
<td>方法参数变量的列表</td>
</tr>
<tr>
<td><strong>@Test</strong></td>
<td><strong>把一个类或者方法标记为测试的一部分。</strong></td>
</tr>
<tr>
<td>alwaysRun</td>
<td>如果为<code>true</code>，则这个测试方法即使在其所以来的方法为失败时也总会被运行。</td>
</tr>
<tr>
<td>dataProvider</td>
<td>这个测试方法的<code>dataProvider</code>
</td>
</tr>
<tr>
<td>dataProviderClass</td>
<td>指明去那里找<code>data provider</code>类。如果不指定，那么就当前测试方法所在的类或者它个一个基类中去找。如果指定了，那么<code>data provider</code>方法必须是指定的类中的静态方法。</td>
</tr>
<tr>
<td>ependsOnGroups</td>
<td>方法所依赖的一组<code>grou</code>p列表</td>
</tr>
<tr>
<td>dependsOnMethods</td>
<td>方法所以来的一组<code>method</code>列表</td>
</tr>
<tr>
<td>description</td>
<td>方法的说明</td>
</tr>
<tr>
<td>enabled</td>
<td>在当前<code>class/method</code>中被此<code>annotation</code>标记的方法是否参与测试（不启用则不在测试中运行）</td>
</tr>
<tr>
<td>expectedExceptions</td>
<td>此方法会抛出的异常列表。如果没有异常或者一个不在列表中的异常被抛出，则测试被标记为失败。</td>
</tr>
<tr>
<td>groups</td>
<td>一组<code>group</code>列表，指明了这个<code>class/method</code>的所属。</td>
</tr>
<tr>
<td>invocationCount</td>
<td>方法被调用的次数。</td>
</tr>
<tr>
<td>invocationTimeOut</td>
<td>当前测试中所有调用累计时间的最大毫秒数。如果<code>invocationCount</code>属性没有指定，那么此属性会被忽略。</td>
</tr>
<tr>
<td>successPercentage</td>
<td>当前方法执行所期望的<code>success</code>的百分比</td>
</tr>
<tr>
<td>sequential</td>
<td>如果是<code>true</code>，那么测试类中所有的方法都是按照其定义顺序执行，即使是当前的测试使用<code>parallel="methods"</code>。此属性只能用在类级别，如果用在方法级，就会被忽略。</td>
</tr>
<tr>
<td>timeOut</td>
<td>当前测试所能运行的最大毫秒数</td>
</tr>
<tr>
<td>threadPoolSize</td>
<td>此方法线程池的大小。 此方法会根据制定的<code>invocationCount</code>值，以多个线程进行调用。<em>注意：如果没有指定<code>invocationCount</code>属性，那么此属性就会被忽略</em>
</td>
</tr>
</tbody>
</table>


## Annotation 使用补充
以下例子包含了和test相关的几种常用例子：

- 测试依赖关系
- 测试异常
- 多线程测试

```java
public class TestNgAnnotaionAdvanced {

    @Test
    public void allReadyCorrect(){
        assertTrue(true,"always true");
    }

    @Test(dependsOnMethods ={"allReadyCorrect"} )
    public void allReadyCorrect_01(){
        System.out.println("waiting allReadyCorrect running");
        assertTrue(true,"always true");
    }

    @Test(expectedExceptions = RuntimeException.class,expectedExceptionsMessageRegExp = "throw")
    public void allReadyCorrect_expectedException(){
        assertTrue(true,"always true");
        throw new RuntimeException("throw");
    }

    @Test(invocationCount = 20,threadPoolSize = 10)
    public void allReadyCorrect_multipleThreads(){
        System.out.println(Thread.currentThread().getId());
        assertTrue(true,"always true");
    }
}
```

## testng xml配置

以下是testng xml 配置实例一个例子，大体上testng 测试可以分为五层：

- Suite
- test
- package
- Class
- method

一般情况下用的比较多的就是类级别了

```xml
<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd" >

<suite name="Suite1" verbose="1" >
  <test name="Nopackage" >
    <classes>
       <class name="NoPackageTest" />
    </classes>
  </test>

  <test name="Regression1">
    <classes>
      <class name="test.sample.ParameterSample"/>
      <class name="test.sample.ParameterTest"/>
    </classes>
  </test>
</suite>
```

另外通过xml还可以配置分组运行，那些运行，那些不运行，如以下例子,什么意思，相信一看就知道了

```xml
<test name="Regression1">
  <groups>
    <run>
      <exclude name="brokenTests"  />
      <include name="checkinTests"  />
    </run>
  </groups>

  <classes>
    <class name="test.IndividualMethodsTest">
      <methods>
        <include name="testMethod" />
      </methods>
    </class>
  </classes>
</test>
```

同时可以在xml中调用不同的testng 文件：

```xml
<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd" >

<suite name="Testng-03" verbose="1" >
    <suite-files>
        <suite-file path="testng-1.xml"></suite-file>
        <suite-file path="testng-2.xml"></suite-file>
    </suite-files>
</suite>
```

使用group配置来确定那些跑，那些不跑：

```java

public class TestNgAnnotaionAdvanced {

    @Test(groups = {"P1","P2"})
    public void allReadyCorrect(){
        assertTrue(true,"always true");
    }

    @Test(dependsOnMethods ={"allReadyCorrect"} ,groups = {"P1","P2","P3"})
    public void allReadyCorrect_01(){
        System.out.println("waiting allReadyCorrect running");
        assertTrue(true,"always true");
    }

    @Test(expectedExceptions = RuntimeException.class,expectedExceptionsMessageRegExp = "throw",groups = {"P4"})
    public void allReadyCorrect_expectedException(){
        assertTrue(true,"always true");
        throw new RuntimeException("throw");
    }

    @Test(invocationCount = 20,threadPoolSize = 10,groups = {"P5"})
    public void allReadyCorrect_multipleThreads(){
        System.out.println(Thread.currentThread().getId());
        assertTrue(true,"always true");
    }
}
```
```xml
<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd" >

<suite name="Testng-02" verbose="1" >

    <test name="02" preserve-order="false" >
        <classes>
            <class name="com.testngdemo.quickstart.TestNgAnnotaionAdvanced" />
        </classes>
        <groups>
            <run>
                <exclude name="P1"></exclude>
                <exclude name="P2"></exclude>
                <exclude name="P5"></exclude>

            </run>
        </groups>
    </test>

</suite>
```
一个小问题，以上例子最终运行那些测试呀？


关于如何使用通过maven调用testng的测试，会在后续再将。


## ```dataprovider``` 使用

一个简单的例子：

``` java
//这个方法会服务于任何把它（测试方法）的数据提供者的名字为"test1"方法
@DataProvider(name = "test1")
public Object[][] createData1() {
 return new Object[][] {
   { "Cedric", new Integer(36) },
   { "Anne", new Integer(37)},
 };
}

//这个测试方法，声明其数据提供者的名字为“test1”
@Test(dataProvider = "test1")
public void verifyData1(String n1, Integer n2) {
 System.out.println(n1 + " " + n2);
}
```

dataprovider 返回的是Object[][]或者Iterator<Object[]> 本质上市一样的东西，在数据驱动测试中经常使用。

## ```dataprovider``` 高级应用

后续会在补上

## testng 高级应用
后续会在补上

## 程序化运行TestNG

```java
   public static void main(String[] args) {
        TestListenerAdapter tla = new TestListenerAdapter();
        TestNG testng = new TestNG();
        testng.setTestClasses(new Class[] { TestNgQuickStart.class,
                TestNgAnnotaionAdvanced.class,
                TestngAnnotationDemo.class,TestNgQuickStartClassLevel.class });
        testng.addListener(tla);
        testng.run();
    }
```

其实运行testng的xml跑测试，就是用以上代码来跑的，原理是一样的，只不过xml里面的配置信息对应到JAVA里面就可以，如以下代码和XML：

```java
XmlSuite suite = new XmlSuite();
suite.setName("TmpSuite");

XmlTest test = new XmlTest(suite);
test.setName("TmpTest");
List<XmlClass> classes = new ArrayList<XmlClass>();
classes.add(new XmlClass("test.failures.Child"));
test.setXmlClasses(classes) 
```

```xml
<suite name="TmpSuite" >
  <test name="TmpTest" >
    <classes>
      <class name="test.failures.Child"  />
    <classes>
    </test>
</suite>
```
```



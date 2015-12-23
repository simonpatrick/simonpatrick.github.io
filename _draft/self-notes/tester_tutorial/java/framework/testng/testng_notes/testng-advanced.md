# TestNG advanced 

## 注解转换器

以下是注解转换器的作用，注解转换器其实就是在运行时改变了某个注解的属性，如下面这个例子：

- @Test的属性中其实没有去定义多线程参数
- 通过transform 监听器，就可以在运行时修改，从而实现了多线程测试

```java
public class TestngAnnotationTransform {
    @Test
    public void test_transferm1(){
        System.out.println("test1");
    }

    public static void main(String[] args) {
        TestNG ng = new TestNG();
        ng.addListener(new Transform1());
        ng.setTestClasses(new Class[]{TestngAnnotationTransform.class});
        ng.run();
    }

    public static  class Transform1 implements IAnnotationTransformer {

        @Override
        public void transform(ITestAnnotation annotation, Class testClass, Constructor testConstructor, Method testMethod) {
            annotation.setAlwaysRun(true);
            annotation.setInvocationCount(20);
            annotation.setThreadPoolSize(20);
            annotation.setDescription("test_annotaion");
            System.out.println(annotation.getSuiteName());
        }
    }
 }
 ```

 retry功能监听器的实现其实就是通过AnnotationTransformer方式转变的


## 方法拦截器

方法拦截器可以在调用方法前进行一些特殊如理，如下面一个例子，可以过滤掉所有函数方法不含有test的方法，这些方法不会被执行，而这些方法不仅仅是@test注解的方法，是全部的方法：

```java
public class TestngAnnotationTransform {

    @BeforeTest
    public void before(){
        System.out.println("before test");
    }
    @Test
    public void test_transferm1(){
        System.out.println("test1");
    }

    @Test
    public void filtedByMethodInterceptor(){
        System.out.println("I am method interceptor testing");
    }

    public static void main(String[] args) {
        TestNG ng = new TestNG();
        ng.addListener(new Transform1());
        ng.addListener(new MethodInterceptor());
        ng.setTestClasses(new Class[]{TestngAnnotationTransform.class});
        ng.run();
    }

    public static class MethodInterceptor implements IMethodInterceptor{

        @Override
        public List<IMethodInstance> intercept(List<IMethodInstance> methods, ITestContext context) {
            System.out.println("running before testing running");
            List<IMethodInstance> result = Lists.newArrayList();
            for (IMethodInstance method : methods) {
                if(method.getMethod().getMethodName().contains("test")){
                    result.add(method);
                }
            }
            return result;
        }
    }
}
```
可以看到IMethodInterceptor接口中返回的是个所有要执行的method的实例，所以在调用之前，基本上可以做想做的任何事情，从而改变测试的执行

## Listeners

- IAnnotationTransformer：上面已经提过
- IReporter ：生成测试报告的监听器，定制测试报告可以实现这个
- ITestListener ：测试的监听器，如果实时的报告可以考虑实现这个
- IMethodInterceptor ：上面已经提过
- IInvokedMethodListener： 和MethodInterceptor类似，不过是方法调用前和调用后或被调用

ITestListener实例：
```java

public class SimpleTestListener implements ITestListener{
    @Override
    public void onTestStart(ITestResult result) {
        System.out.println("test is started");
    }

    @Override
    public void onTestSuccess(ITestResult result) {
        System.out.println("test is passed");
    }

    @Override
    public void onTestFailure(ITestResult result) {
        System.out.println("test is failed");
    }

    @Override
    public void onTestSkipped(ITestResult result) {
        System.out.println("test is skipped");
    }

    @Override
    public void onTestFailedButWithinSuccessPercentage(ITestResult result) {
        System.out.println("test is passed with acceptable percentage!");
    }

    @Override
    public void onStart(ITestContext context) {
        System.out.println("suite is started");
    }

    @Override
    public void onFinish(ITestContext context) {
        System.out.println("suite is finished");
    }
}
```
xml 配置：

```xml
<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd" >

<suite name="Testng-01" verbose="1" >
    <listeners>
        <listener class-name="com.testngdemo.advanced.SimpleTestListener"/>
    </listeners>
    <test name="Nopackage" >
        <classes>
            <class name="com.testngdemo.quickstart.TestNgQuickStart" />
        </classes>
    </test>

</suite>
```

结果可以看到：

```bash
suite is started
test is started
test is passed
suite is finished
```

如果把xml配置改为：

```xml
<suite name="Testng-01" verbose="1" >
    <listeners>
        <listener class-name="com.testngdemo.advanced.SimpleTestListener"/>
    </listeners>
    <test name="Nopackage" >
        <classes>
            <class name="com.testngdemo.quickstart.TestNgQuickStart" />
            <class name="com.testngdemo.quickstart.TestNgQuickStartClassLevel" />
        </classes>
    </test>

</suit>
```

结果为：
```bash

suite is started
test is started
test is passed
test is started
test is passed
test is started
test is passed
suite is finished
```

那么如果使用suite-files这种形式时结果会是怎么样呢？

## 本地依赖注入

TestNG 允许你在自己的方法中声明额外的参数。这时，TestNG会自动使用正确的值填充这些参数。依赖注入就使用在这种地方：

任何@Before或@Test方法可以声明一个类型为 ITestContext的参数。
任何@After都可以声明一个类型为ITestResult的单数，它代表了刚刚运行的测试方法。
任何@Before和@After方法都能够声明类型为XmlTest 的参数，它包含了当前的<test>参数。
任何@BeforeMethod可以声明一个类型为 java.lang.reflect.Method的参数。这个参数会接收 @BeforeMethod完成调用的时候马上就被调用的那个测试方法当做它的值。
任何@BeforeMethod可以声明一个类型为Object[]的参数。这个参数会包含要被填充到下一个测试方法中的参数的列表，它既可以由 TestNG 注入，例如java.lang.reflect.Method或者来自@DataProvider。
任何@DataProvider可以声明一个类型为ITestContext 或java.lang.reflect.Method的参数。后一种类型的参数，会收到即将调用的方法作为它的值。


这个又什么用处呢？其实还是挺大的，至少可以拿到testng的上下文,比如说listener的信息：

```java
public class TestngGetTestContext {

    @BeforeSuite
    public void init(ITestContext context){
        System.out.println(context.getSuite().getName());
        System.out.println(context.getSuite().getXmlSuite().getListeners());
        System.out.println(((TestRunner)context).getTestListeners());
        System.out.println(context);
    }

    @Test
    public void test_01(){
        System.out.println("test_01");
    }
}
```

可以得到listener的好处是什么呢？

- 可以实现testng的listener的同时，也实现webdrivereventlistener，这样可以让testng的测试和webdriver的web点击时间联系起来
- 可以根据method，做一些特殊如理


## IHookable 接口

TestNG的允许你覆盖和跳过测试方法的调用,只要实现IHookable接口，实现此接口之后，test其实是由run方法来执行的

```java
public class MyHookable implements IHookable {
    @Override
    public void run(IHookCallBack callBack, ITestResult testResult) {
        System.out.println("hookable is running");
        callBack.runTestMethod(testResult);
        System.out.println("hookable is finished");
    }

    @Test
    public void test_01(){
        System.out.println("test_01");
    }

    @Test
    public void test_02(){
        System.out.println("test_02");
    }

    @AfterMethod(alwaysRun = true)
    public void test_after(){
        System.out.println("after test_01");
    }
}
```


# 重试失败的用例 Retry Failed Cases

## Steps
- 实现IRetryAnalyzer
- 实现新的Listener，在Test里面加入Retry的Listener
- 添加新的Listener到testng.xml

### 实现IRetryAnalyzer

代码:
```java
public class RetrySample implements IRetryAnalyzer {
    private int retryCount = 0;
    private int maxRetryCount = 2;
    @Override
    public boolean retry(ITestResult result) {
        if(retryCount<maxRetryCount){
            System.out.println("retrying testing"+result.getName()+" result "
                    +getResultStatusName(result.getStatus()));
            retryCount++;
            return true;
        }

        return false;
    }

    public String getResultStatusName(int status){
        String resultName = null;
        if(status==1)
            resultName = "SUCCESS";
        if(status==2)
            resultName = "FAILURE";
        if(status==3)
            resultName = "SKIP";
        return resultName;
    }
}

```

### 实现Test 的annotation tranform

代码：
``` java

public class RetryListener implements IAnnotationTransformer{
    @Override
    public void transform(ITestAnnotation annotation, Class testClass, Constructor testConstructor, Method testMethod) {
        IRetryAnalyzer retry = annotation.getRetryAnalyzer();
        if(retry==null){
            annotation.setRetryAnalyzer(RetrySample.class);
        }
    }
}

```
### 添加retry listener到textng.xml
```xml
<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd" >
<suite name="Suite1" verbose="1" >
    <listeners>
        <listener class-name="com.hedwig.stepbystep.javatutorial.testng.listener.RetryListener"></listener>
    </listeners>
    <test name ="suite1">
        <classes>
            <class name="com.hedwig.stepbystep.javatutorial.guava.joinersamples.JoinerBasicTestByTestNG">

            </class>
        </classes>
    </test>
</suite>

```
### 分析
- 好处
- 影响
- 为什么这样做可以？

#### 源码分析



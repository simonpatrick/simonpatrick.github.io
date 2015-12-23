# 反射在自动化测试中的应用

## Java 反射
Java 反射应用非常广泛，几乎所有的框架都是在反射基础上实现。Java 的反射更多的用来操作java对象本身和java对象反映的实际业务关系没有太多关联。

一个反射的实例：

如何不通过Java bean的get方法得到某个类的某个属性值？
``` java

public static Object getFieldValue(final Object object,final Field field) throws IllegalAccessException {
		field.setAccessible(true);
		return field.get(object);

	}
```

### Java 反射常用的工具
- Apache Common BeanUtils
- 很多其他开源框架都提过了一些自己的反射工具

### Java 反射在自动化测试中的应用

#### Page Factory 模式
Selenium 官方Wiki上面提供了关于Page Factory的一个[实例](https://code.google.com/p/selenium/wiki/PageFactory).

#### 一个关于百度例子：

- 构建Page Object

```java

public class BaiduHomePage {

    @FindBy(id="kw")
    private WebElement keyword;

    @FindBy(id="su")
    private WebElement submit;

    @FindBy(className = "ipt_rec")
    private WebElement voiceRec;
    。。。。。。。省略get/set 方法
}
```

- 进行测试

```java
public class BaiduHomePageFactoryTest extends BaseWebTest {

    @Test
    public void testBaiduPageFactory(){
        driver.get("http://www.baidu.com");
        BaiduHomePage page =  PageFactory.initElements(super.driver, BaiduHomePage.class);
        page.getKeyword().sendKeys("test");
        page.getSubmit().click();
        assertNotNull(super.driver.getTitle());
    }

}
```

这样写的好处：
- 不用每次都去手动实例化每个页面元素，在实例化页面的时候可以自动实例化
- 页面和测试用例其实已经分离了，如果想修改页面元素的定位，其实不需要去改测试用例了

还有其他好处吗？。。。。。

看一下Selenium实现的[源码](https://github.com/SeleniumHQ/selenium.git)，其实这个就是使用了反射来达到这个目的的.

```java
public static void initElements(FieldDecorator decorator, Object page) {
    Class<?> proxyIn = page.getClass();
    while (proxyIn != Object.class) {
      proxyFields(decorator, page, proxyIn);
      proxyIn = proxyIn.getSuperclass();
    }
  }

  private static void proxyFields(FieldDecorator decorator, Object page, Class<?> proxyIn) {
    Field[] fields = proxyIn.getDeclaredFields();
    for (Field field : fields) {
      Object value = decorator.decorate(page.getClass().getClassLoader(), field);
      if (value != null) {
        try {
          field.setAccessible(true);
          field.set(page, value);
        } catch (IllegalAccessException e) {
          throw new RuntimeException(e);
        }
      }
    }
```

所以其实反射作用还是挺大的

### 可以使用反射的地方

看一下如下代码片段：

```java
    inquirySources = getNodeValue(xmlPath,"inquirySources");
    inquiryTypes = getNodeValue(xmlPath,"inquiryTypes");
    inquiryState = getNodeValue(xmlPath,"inquiryState");
    payTypes = getNodeValue(xmlPath,"payTypes");
    propertyUsage = getNodeValue(xmlPath,"propertyUsage");
    inquiryInfoText = getNodeValue(xmlPath,"inquiryInfoText");
    areaText = getNodeValue(xmlPath,"areaText");
    priceText = getNodeValue(xmlPath,"priceText");
    countF = getNodeValue(xmlPath,"countF");
    countF_num = getNodeValue(xmlPath,"countF_num");
```

其实我们在这里是不是也可以使用反射的，为什么：
 - 使用了同样的方法去getNodeValue
 - 都是在赋值计算

这个其实和PageFactory很像了，我们可以理解为：
 - 有一个类，里面有属性inquirySources，。。。。
 - 从XML文件通过某个属性获取某个值
 - 将XML获取的这个值赋给inquirySources。。。。。

使用反射来改写一些这端代码：

- 构建一个页面描述的类
```java
public class PageDescription {
    private String keyword;
    private String submit;

    @Override
    public String toString() {
        return MoreObjects.toStringHelper(this)
                .add("keyword", keyword)
                .add("submit", submit)
                .toString();
    }
}
```

- 构建xml文件

```java
<?xml version="1.0" encoding="utf-8" ?>
<root>
    <keyword desc="keyword">id="kw"</keyword>
    <submit desc="submit">id="su"</submit>
    <voiceRec desc="voice rec">.ipt_rec</voiceRec>
</root>
```

- 编写测试类

```java
 @Test
    public void testPageDescription(){

        // k:v = field name/ field description
       Map<String,String> map= XMLHelper.build("pages/BaiDuHomePageResource.xml")
               .getNameAndTextForAllElements();
        PageDescription pd = new PageDescription();
        for (Map.Entry<String,String> entry: map.entrySet()) {
           try {
               ReflectionHelper.setFieldValue(pd, entry.getKey(), entry.getValue());
           }catch (Exception e){
               logger.error(e);
           }
        }

        System.out.println(pd);
    }
```

如果在转化过程中不想完全一样的把值赋值呢，中间有点变化呢？

```java
 @Test
    public void testPageDescriotion_2(){
        // k:v = field name/ field description
        Map<String,String> map= XMLHelper.build("pages/BaiDuHomePageResource.xml")
                .getNameAndTextForAllElements();
        PageDescription pd = new PageDescription();
        for (Map.Entry<String,String> entry: map.entrySet()) {
            try {
                Function function = new Function() {
                    @Override
                    public Object apply(Object input) {
                        return input+"test";
                    }
                };
                //add field decorator here then transfer entry.getValue to defined value
                ReflectionHelper.setFieldValue(pd, entry.getKey(), function.apply(entry.getValue()));
            }catch (Exception e){
                logger.error(e);
            }
        }

        System.out.println(pd);
    }
```

如果在转化的过程中，赋值的规则是变化的呢？

```java
  @Test
    public void testPage2(){
        PageDescription pd = new PageDescription();
        Map<String,String> map= XMLHelper.build("pages/BaiDuHomePageResource.xml")
                .getNameAndTextForAllElements();

        convertTo(map, pd, new Function<String, String>() {
            @Override
            public String apply(String input) {
                return input.toLowerCase()+" converted";
            }
        });
        logger.info(pd);
    }

    private <T,I,R> void  convertTo(Map<String,String> map,T instance,Function<I,R> function){
        for (Map.Entry<String,String> entry: map.entrySet()) {
            try {
                //add field decorator here then transfer entry.getValue to defined value
                ReflectionHelper.setFieldValue(instance, entry.getKey(), function.apply((I)entry.getValue()));
            }catch (Exception e){
                logger.error(e);
            }
        }
    }

```

## 总结一下
赋值其实：将某个地方的值赋给另外一个地方。他有两个思路：

- 思路1：

```
在地方1，找到坑1里面的东西，填给地方2里面的坑1
。
。
。
在地方1，找到坑m里面的东西，填给地方2里面的坑n
```

- 思路2：

```
给地方1，建个模型，给地方2也建个模型
寻找地方1 和地方2 的规律
根据规律去搬东西填坑
```

貌似和没反射什么关系？稍微还是有点，反射就是填坑的动作，就是不需要知道哪个坑号，给我什么我填什么。

那么规律是什么呢？
- 名字
- 转换







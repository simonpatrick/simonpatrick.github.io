# Selenium Page Factory 模式分析
本文主要用来分析Page Factory实现的原理以及一些扩展的可能性。

## Page Factory 的例子
[Selenium Page Factory Wiki](https://code.google.com/p/selenium/wiki/PageFactory)

首先解释一下这个例子：

- 使用注解描述元素定位
- 使用 ```PageFactory.initElements(driver, page);```

```java
public class GoogleSearchPage {
    // The element is now looked up using the name attribute
    @FindBy(how = How.NAME, using = "q")
    private WebElement searchBox;

    public void searchFor(String text) {
        // We continue using the element just as before
        searchBox.sendKeys(text);
        searchBox.submit();
    }

    public void searchFor(String text) {
    GoogleSearchPage page＝ PageFactory.initElements(new ChromeDriver(), GoogleSearchPage.class);
    }
}
```
以上一个显而易见的好处就是减少了查找元素的代码量，比如类似于一下的代码：
```java
  driver.findElement(By.id("q"))
```

但是只有这样的好处吗？我们先从分析Selenium Page Factory实现的原理说起

##Page Factory 实现的原理

PageFactory 是使用反射(Reflection)和动态代理(dynamic proxies)的方式来创建页面的每
每个元素:

- PageFactory: initElements and proxyFields
```java
public static void initElements(FieldDecorator decorator, Object page) {
    for(Class proxyIn = page.getClass(); proxyIn != Object.class; proxyIn = proxyIn.getSuperclass()) {
        proxyFields(decorator, page, proxyIn);
    }

}

private static void proxyFields(FieldDecorator decorator, Object page, Class<?> proxyIn) {
    Field[] fields = proxyIn.getDeclaredFields();
    Field[] arr$ = fields;
    int len$ = fields.length;

    for(int i$ = 0; i$ < len$; ++i$) {
        Field field = arr$[i$];
        Object value = decorator.decorate(page.getClass().getClassLoader(), field);
        if(value != null) {
            try {
                field.setAccessible(true);
                field.set(page, value);
            } catch (IllegalAccessException var10) {
                throw new RuntimeException(var10);
            }
        }
    }

}
```
- FieldDecorator：DefaultFieldDecorator 源码
从DefaultFieldDecorator的源码看:
1. 实现decorate方法,WebElement 和List<WebElement> 都是通过proxy的方式创建的
2. 每个Proxy的方式都有一个对应的invocationHandler处理
   Selenium的源码有两个invocationHandler：
   - LocatingElementHandler
   - LocatingElementListHandler

```java
public Object decorate(ClassLoader loader, Field field) {
        if(!WebElement.class.isAssignableFrom(field.getType()) && !this.isDecoratableList(field)) {
            return null;
        } else {
            ElementLocator locator = this.factory.createLocator(field);
            return locator == null?null:(WebElement.class.isAssignableFrom(field.getType())?this.proxyForLocator(loader, locator):(List.class.isAssignableFrom(field.getType())?this.proxyForListLocator(loader, locator):null));
        }
    }

    private boolean isDecoratableList(Field field) {
        if(!List.class.isAssignableFrom(field.getType())) {
            return false;
        } else {
            Type genericType = field.getGenericType();
            if(!(genericType instanceof ParameterizedType)) {
                return false;
            } else {
                Type listType = ((ParameterizedType)genericType).getActualTypeArguments()[0];
                return !WebElement.class.equals(listType)?false:field.getAnnotation(FindBy.class) != null || field.getAnnotation(FindBys.class) != null || field.getAnnotation(FindAll.class) != null;
            }
        }
    }

    protected WebElement proxyForLocator(ClassLoader loader, ElementLocator locator) {
        LocatingElementHandler handler = new LocatingElementHandler(locator);
        WebElement proxy = (WebElement)Proxy.newProxyInstance(loader, new Class[]{WebElement.class, WrapsElement.class, Locatable.class}, handler);
        return proxy;
    }

    protected List<WebElement> proxyForListLocator(ClassLoader loader, ElementLocator locator) {
        LocatingElementListHandler handler = new LocatingElementListHandler(locator);
        List proxy = (List)Proxy.newProxyInstance(loader, new Class[]{List.class}, handler);
        return proxy;
    }
```

我们再看一下LocatingElementHandler,可以看到实际在待用PageFactory创建的元素时候
都是通过这个掉用LocatingElementHandler
```java
public class LocatingElementHandler implements InvocationHandler {
    private final ElementLocator locator;

    public LocatingElementHandler(ElementLocator locator) {
        this.locator = locator;
    }

    public Object invoke(Object object, Method method, Object[] objects) throws Throwable {
        WebElement element;
        try {
            element = this.locator.findElement();
        } catch (NoSuchElementException var7) {
            if("toString".equals(method.getName())) {
                return "Proxy element for: " + this.locator.toString();
            }

            throw var7;
        }

        if("getWrappedElement".equals(method.getName())) {
            return element;
        } else {
            try {
                return method.invoke(element, objects);
            } catch (InvocationTargetException var6) {
                throw var6.getCause();
            }
        }
    }
}
```

以上Selenium PageFactory大致的实现，从过程来看：
PageFaction-> initElements-> proxyFields

## Page Factory 有什么好处

个人理解的好处:

* 可以通过修改InvocationHandler里面的处理,比如
  ```java
  element = this.locator.findElement();
  ```
  如果都使用wait().util的方式,这样可以使所有查找的元素更加稳定
*  使用了proxy的方式,在实例化WebElement的时候，实际上不管WebElement存在不存在都可以创建
   而实际findElement都会延迟到真的调用这个元素时执行,这带来一个好处就是如果WebElement的实例创建后
   页面DOM刷新后,需要重新查找WebElement,否则可能抛出StaleElementReferenceException,而Proxy之后每次都会自动
   查找,这样就减少了代码处理
* 工厂的设计模式同时也带了了灵活程度,在创建页面或者页面元素的时候,可以开始添加统一的前置或者后置的处理

但是可惜的是Selenium并没有提供开发的接口来让用户定制,所以如果自己定制PageFactory模式,则需要自己去实现Selenium这
一套方法,同时加入自己特殊的实现

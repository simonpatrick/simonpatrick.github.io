# Spring

## Spring Context

```java
XmlBeanFactory factory = new XmlBeanFactory(new ClassPathResource("beans.xml"));//这样来加载配置文件  

XmlBeanFactory factory = new XmlBeanFactory(new ClassPathResource("beans.xml"));//这样来加载配置文件  

XmlWebApplicationContext context = new XmlWebApplicationContext();  
context.setConfigLocations(new String[] {"aaa.xml" , "bb.xml"});  
MockServletContext msc = new MockServletContext();  
context.setServletContext(msc);  
context.refresh();  
msc.setAttribute(WebApplicationContext.ROOT_WEB_APPLICATION_CONTEXT_ATTRIBUTE, context);

```

## Spring Test
- mock.env -> Enviroment
- mock.jndi -> JNDI mock
- mock.web -> servelet API
- General testing utilities -> ReflectionTestUtils
- AopTestUtils
- AopProxyUtils

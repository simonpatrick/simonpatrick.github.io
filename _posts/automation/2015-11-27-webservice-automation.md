---
layout: post
title: "自动化测试－接口测试"
modified:
categories: [automation]
excerpt:
tags: [automation]
date: 2015-11-27-11:10:00
---

在敏捷开发交付的流程中，自动化测试实际上被放在一个看起来挺重要的位置，而自动化测试中，接口测试是一个投入产出比比较高的
一种自动化测试的形式，而我自己也做了一个这样的脚手架一样的东西可以方便进行自动化测试，关键是在一些现有第三包的基础上做实现，其实一个脚手架不需要几个JAVA类就可以完成了，至少我自己的这个在10个文件以内.要论行数估计也没有多少代码量，主要时间其实都是在想怎么更方便的写自动化测试，怎么使用以后的开源代码了。

下面介绍一下我自己如何完成这个自动化接口测试
脚手架设计和实现的，以及我自己实现过程中的种种发现。主要从以下几个方面来讲：

- 如何构建接口自动化测试的脚手架
- 关于接口测试参考的一些资源
- 关于接口测试的后续的一些想法

## 如何构建接口自动化测试的脚手架

接口测试本文中主要是指HTTP的请求，构建接口自动化测试脚手架的时候，首先先看看平常接口测试，测试人员时如何做的，我了解主要是以下几种方式：

- 通过操作页面/APP来触发接口调用
- 使用诸如SOAPYUI/JMETER/POSTMAN 或者其他的客户端工具来进行接口测试

我自己都使用过SOAPUI/JMETER/POSTMAN,不能说使用的多么深入，但是常用的功能也都有用过，比如SOAPUI构建一个项目完整的接口自动化测试用例，大概有200+以上的用例，可以支持不同的测试环境，检查点中可以检查数据库,使用XPATH/XQUERY来检查／获取指定的值，进行不同API的数据传递等等，这些工具(指功能测试方面)大体的逻辑我觉得是类似的,基本上都有:

- 发起请求的客户端,需要测试人员构建，也有通过WSDL/WADL自己生成的，不过数据都是需要测试人员输入的
- 根据表达式进行取值的Resolver,就是可以根据XPATH/XQUERY语法，或者其他的语法来获取指定的值，
  就是用来传递上下文数据的一种方式
- 外部可以参数话数据，比如环境配置
- 可以查看测试结果，这个其实可以理解为某种测试框架的一个功能，不如JUNIT，TESTNG，他们

总体上我自己的总结是如下图:

![img](../assets/images/pics/api_testing.png)

### 接口自动化测试脚手架的构建

根据以上的分析如果自己需要实现的话，最主要需要实现一下其实就是请求的构建，请求构建包括了:
- 发起请求的客户端
- 请求数据的构建

对于发起请求的客户端就直接使用了Spring RestTemplate,考虑的主要原因如下:

- 使用相对比较方便,模块化比较清晰
- 可以使用HTTPClient的实现
- Spring RestTemplate所在的包还有其他一些接口的支持，以后如果使用其他接口可以不需要换包也可以做

在实际的使用过程中，其实也遇到了一些问题，比如如下的内容:
- HTTPS的访问
- 开发接口定义不够准确的问题,造成使用RestTemplate时候出现了一些不在开始预期范中的问题

如何解决这些问题,在后面再详细介绍，这里说明一下使用RestTemplate的一个主要流程：
- 1. 构建请求，设置请求的Header，URL，Accept，ContextType，Token等等
- 2. 调用请求获取返回的Response，
  这个ResponseRestTemplate中实际上封装了一个ResponseEntity的类，里面包括了请求状态，Body之类
  RestTemplate 有个好处就是如果给RestTemplate设定了MessageConverter的话，他可以自动把请求的返回类型直接转换，比如你发起请求的时候设置了JOSN的Message Converter，他可以帮你把类，或者字符串自己转化为JSON来发送，同样如果是返回值是JSON的话，也可以帮你自己将JSON转换成你指定类型的JAVA BEAN

说完这个流程，我们就说说如何通过RestTemplate构建一个简单的HTTP请求:

```java
  Map<String,String> urlVariable = new Map<String,String> ();
  urlVariable.put("q","test");
  JavaBean javaBean = restTemplate.getForObject("http://www.baidu.com",JavaBean.class,urlVariable);
  JavaBean javaBean1 = restTemplate.postForObject("http://www.baidu.com",JavaBean.class,urlVariable);
  ResponseEntity e =  restTemplate.getForEntity("http://www.baidu.com",JavaBean.class,urlVariable);
```

实际上使用RestTemplate还是挺简单的，不过为了让使测试更为方便一点，然后每个人的代码更统一点，自己重新封装了一下RestTemplate的使用，主要分为三个概念:

- Service 的描述
- 测试数据
- 客户端调用

### 接口服务描述

Service的描述实际上就是一个JSON文件，只不过自己规定了一下，格式类似于,这个文件描述了API的定义，当然API的body没有在这个里面，不过为了不把事情搞复杂，就暂时不放在这个里面.

```
{
  "apiDomainName": "applicationName",
  "contentType": "application/x-www-form-urlencoded",
  "headers": {
    "Accept": "application/json, text/javascript, */*"
  },
  "method": "POST",
  "pathParameters": [],
  "queryParameters": [
    "username",
  ],
  "resourceURL": "/application/subdomain"
}
```

测试数据类：

```java
 private Map<String, String> queryParameters = Maps.newHashMap();
 private Map<String, String> pathParameters = Maps.newHashMap();
 private Map<String, String> headers = Maps.newHashMap();
 private T body;
```

而如何调用客户端就变成,而且其实每一个API的访问其实都可以这样子来做，

```java
  ResponseEntity response = RestTemplateHelper.build(serviceDescriptionPath,requestData).call();
```
说明一下的是：
- serviceDescriptionPath就是接口的描述
- requestData就是需要进行测试的数据

然后实际上接口的描述是开发还没有开发好的时候就已经定了的，所以这里的变量就变成如何构建requestData了

### 构建RequestData

构建requestData实际上就是设计测试用例，那么这里也是使用Excel的方式，将不同的值填写到excel里面，不过为了减少set值这样的操作，这个脚手架就提供了一些工具，可以直接将数据设置到RequestData实例，具体的操作如下:

Excel是如下格式的：

|变量名|测试用例1|测试用例2|
|--- |---|----|
|data.queryParameters(username)|1|1|
|data.queryParameters(year)|2015|2014|
|data.queryParameters(month)|10|11|

说明一下，通过反射的方式，可以直接生成一个requestData的实例,同时queryParameters中值已经设置好了，这样调用代码中就不需要写类似于：

```java
  RequestData data = new RequestData();
  data.queryParameters.put("username","1");
  data.queryParameters.put("year","2015");
```

这里有兴趣的同学可以参考这个包:里面其实已经有很方便的通过反射去赋值了,

```xml
<dependency>
    <groupId>org.jodd</groupId>
    <artifactId>jodd-bean</artifactId>
    <version>3.6.6</version>
</dependency>
```

### 使用TestNG的DataProvider
刚才讲述了如何发生生成数据，那么通过Excel的方式提供不同的数据，就可以通过TestNG的DataProvider了
所以测试数据通过，TestNG data provider的实现在这里就不多少了，网上其实有很多内容了.

### 接口测试的代码看起来就是这个样子了

```java
@DataProvider(name = "data")
  public Iterator<Object[]> getAPITestData(Method m) throws Exception {
      Map<String, Class> clazz = new HashMap<String, Class>();
      clazz.put("RequestData", RequestData.class);
      Iterator<Object[]> y = TestData.provider("testcase/api1.xls", m, clazzMap);

      return y;
  }

  @Test(dataProvider = "data")
  public void testAPITest(RequestData data) {
    ResponseEntity response = RestTemplateHelper.build(serviceDescriptionPath,requestData).call();
    Assert.assertEqual(response.getStatus,200); // response 的期望值实际可以通过dataprovider传入
  }
```
而且几乎所有的代码都差不多成这个样子了，那么获取可以写个代码生成的东西,当然最后通过了JsonPath写了一些获取JSON值的工具，这个暂时也就不说了.

### 那么代码生成吧

当封装好这些东西之后，发现所有的接口都类似了，然后就做了代码生成的工具了,代码生成器的入口实际上个就是那个服务描述文件开始的，
所以代码生成器的参数就是服务描述文件，在实际的使用的过程中，接口描述这个文件也可以自动生成，目前总共支持以下几种:
- 手动编写描述文件
- 抓取开发API规格网站接口的描述，自动生成描述文件
- 解析HAR文件自动生成描述文件，解析HAR其实不难，就是繁琐一点字段有点多

后续想打通和POSTMAN的连接，可以接收POSTMAN的导出文件，然后也可以导出POSTMANT的，以后开BUG就什么也不说，直接放一个POSTMAN文件其实也挺帅的

至此一个接口测试的脚手架就大致完成了.总结起来就是:
- 封装了RestTemplate，让他接受一个接口的描述文件，一个请求的数据
- 通过Excel传数据给请求的数据进行数据驱动
- 相同类似的代码进行代码生成

最后其实这样子使用下来,接口构建几个简单一点的自动化测试用例，其实也就是几分钟的事情.

### 一些细节

在实现过程中，实际上还有一些特殊情况，比如说需要token，认证信息，这些通过一个公用函数的方式就可以解决，然后在代码生成的时候
直接讲这个放在实际测试的接口前面调用. 后有就是上面说到的的:

- HTTPS的访问
- 开发接口定义不够准确的问题,造成使用RestTemplate时候出现了一些不在开始预期范中的问题

HTTPS的访问是通过如下代码解决的,创建一个略SSL的httpclient就可以了

```java
public static RestTemplateClientHelper getHttpClientImplInstance(){
       RestTemplateClientHelper client = new RestTemplateClientHelper();
       HttpClient httpClient = getIgnoreSSLHttpClient();
       client.setTemplate(new RestTemplate(new HttpComponentsClientHttpRequestFactory(httpClient)));
       return client;
   }

   /**
    * 获取忽略SSL的httpclient，支持https的请求
    * @return
    */
   private static HttpClient getIgnoreSSLHttpClient() {
       CloseableHttpClient httpClient = null;
       try {

           httpClient = HttpClients.custom().
                   setHostnameVerifier(new AllowAllHostnameVerifier()).
                   setSslcontext(new SSLContextBuilder().loadTrustMaterial(null, new TrustStrategy() {
                       public boolean isTrusted(X509Certificate[] arg0, String arg1) throws CertificateException {
                           return true;
                       }
                   }).build()).build();
       } catch (NoSuchAlgorithmException | KeyManagementException | KeyStoreException e) {
           logger.error(e);
       }
       return httpClient;
   }
```

还有一个就是有时开发的接口返回类型(accept type)不能让RestTemplate处理，那么其实添加自己定义个MessageConverter就好了:
下面是一个修改阿里自己的FastJSON的MessageConverter的例子,
其实也没改什么，就是捕捉了一个异常，主要是不知道什么原因调用时候readInternal就抛出和编码格式有关系的异常，然后就捕捉了一下异常反正也就把那个问题就没有了，不过这个改法应该也是有问题的.

```java
public class ModifiedFastJsonHttpMessageConverter extends AbstractHttpMessageConverter<Object> {
   ........
    public ModifiedFastJsonHttpMessageConverter() {
        super(new MediaType("application", "json", UTF8), new MediaType("application", "*+json", UTF8));
        this.charset = UTF8;
        this.features = new SerializerFeature[0];
    }

    ............

    protected Object readInternal(Class<?> clazz, HttpInputMessage inputMessage) throws IOException, HttpMessageNotReadableException {
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        InputStream in = inputMessage.getBody();
        byte[] buf = new byte[1024];

        while(true) {
            int bytes = in.read(buf);
            if(bytes == -1) {
                byte[] bytes1 = baos.toByteArray();
                try {
                    return JSON.parseObject(bytes1, 0, bytes1.length, this.charset.newDecoder(), clazz);
                }catch (Exception e){
                    return baos.toString("UTF-8");
                }
            }

            if(bytes > 0) {
                baos.write(buf, 0, bytes);
            }
        }
    }
      ........
  }  
```

## 后续的一些想法

后续希望在这个基础上再做点其他的一些事情:
- 增加POSTMAN的代码生成的支持
- 探索能不能通过API接口描述直接生成JMETER的JMX文件，可以讲基础的JMETER性能测试的基础代码也生成好
- 整理一下放到GITHUB上面，其实整个脚手架自己也就是几个文件而已，:)
- 建立一个MOCK SERVER，方便模拟一些API调用的方式
- 做一个简单点获取JSON中指定字段，然后传递给下一个API使用的工具

## 一些资源

- [unitest](http://unirest.io)
- [json-placeholder](http://jsonplaceholder.typicode.com)
- [wiremock](http://wiremock.org/)
- [mockbin](https://github.com/Mashape/mockbin.git)

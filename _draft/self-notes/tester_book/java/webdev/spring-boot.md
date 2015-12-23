# Spring Boot 
## Spring Boot Quick Start
- install maven
- or install gradle
- install spring boot cli

```shell
gvm ls springboot
spring --version
```
or in Mac
``` shell
brew tap pivotal/tap
brew install springboot
brew update
```

## Quick start spring cli example

简单的groovy脚本
``` groovy
@RestController
class ThisWillActuallyRun {
 @RequestMapping("/")
 String home() {
 "Hello World!"
 }
}
```

然后运行如下命令：
```shell
spring run app.groovy
```

### 开始第一个Hello World代码

代码：
``` java
@RestController
@EnableAutoConfiguration
public class QuickStart {

    @RequestMapping("/helloworld")
    public String home(){
        return "hello world!";
    }

    public static void main(String[] args) {
        SpringApplication.run(QuickStart.class,args);
    }
}
```
运行curl命令：

```shell
curl http://127.0.0.1:8080/helloworld
hello world!%

```
### annotation 说明
- @RestController
* 这是个Controller
* 所以会用他处理请求

- @RequestMapping
* 路由信息

- @EnableAutoConfiguration
* Tell Spring how to configure the application
* 使用Spring默认的配置

### Running the Application
- Run the main method 
- ```mvn spring-boot:run```

### 创建可运行的jar

```mvn clean package``` 可以创建一个jar在target目录

## Use Spring-Boot
### Maven
- compile setting 
- UTF-8 source encoding or all encoding
- resource filtering
- exec plugin,surefire,git commit id,shade

### Gradle

``` groovy
buildscript {
    repositories { mavenCentral() }
    dependencies {
classpath("org.springframework.boot:spring-boot-gradle-plugin:1.2.1.RELEASE") }
}
apply plugin: 'java'
apply plugin: 'spring-boot'
repositories { mavenCentral() }
dependencies {
compile("org.springframework.boot:spring-boot-starter-web")
testCompile("org.springframework.boot:spring-boot-starter-test") }

```

### Quick start Tomcat

```shell
export MAVEN_OPTS=-Xmx1024m -XX:MaxPermSize=128M -Djava.security.egd=file:/dev/./urandom
```

## Spring-Boot Features

### 启动
- SpringApplication
- Fluent Style: SpringApplicationBuiler

### Banner
### Fluent Builder API
build application context 层级关系
### Application Events and Listener
```java 
SpringApplication.addListeners()
```

- ApplicationStartedEvent
- ApplicationEnviromentPrepareEvent
- ApplicationPrepareEvent
- ApplicationFailedEvent

## Spring Annotation 说明

- @RestController ： 说明是个WebController，spring会进行web request/response的处理,RestController 实际上包含了Controller和ResponseBody
- @EnableAutoConfiguration：将configuration交给Spring
- @ComponentScan ：Spring 扫描文件入口
- @Configuration: Spring 配置文件
- @ImportSource
- 
## 进行打包

```shell
mvn package
jar tvf target/myproject-0.0.1-SNAPSHOT.jar
java -jar target/myproject-0.0.1-SNAPSHOT.jar
```

## Spring Boot 配置文件
- application.properties
- value annotation
- configuration in Configuration Annotation
- profile


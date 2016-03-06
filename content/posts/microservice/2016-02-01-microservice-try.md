---
layout: post
title: "01-微服务框架－Springboot/Flask,Hello World"
modified:
categories: [microservice]
image: 19.jpg
tags: [microservice]
date: 2016-02-01T23:57:29
---

现在有很多的微服务框架，这里试用一下Java Springboot和Python的Flask.
本文分别试用SpringBoot和Flask完成了一个简单的Hello World服务来展示如何使用Springboot和Flask构建
一个简单的服务. 同时用AB进行了一个简单的压力测试。

## SpringBoot Hello World Web Application

- Create a SpringBoot Application entry point
- add Beans into springboot startup life cycle

  ```
  利用command-line runner的这个特性，再配合依赖注入，可以在应用程序启动时后首先引入一些依赖bean，例如data source、rpc服务或者其他模块等等，这些对象的初始化可以放在run方法中。不过，需要注意的是，在run方法中执行初始化动作的时候一旦遇到任何异常，都会使得应用程序停止运行，因此最好利用try/catch语句处理可能遇到的异常。
  ```
- create HelloWorld Service

## All Codes for the simple ***hello world*** Service

以下代码的一些说明：
- Web 应用的执行入口： main方法，里面的SpringApplication.run
- StartupRunner 可以在SpringBoot Application启动过程中一些事情
- RestController注解表示了这个类是个Rest 风格的Controller

pom.xml 中的唯一依赖，请指定版本或者parent指定为        ```<artifactId>spring-boot-starter-parent</artifactId>```

```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
</dependencies>
```

```java
@SpringBootApplication
@RestController
public class HelloWorldEndPoint {

    public static void main(String[] args) {
        SpringApplication.run(HelloWorldEndPoint.class,args);
    }

    public static class StartupRunner implements CommandLineRunner{
        protected final Logger logger = LoggerFactory.getLogger(StartupRunner.class);

        @Override
        public void run(String... strings) throws Exception {
            logger.info("startup command is running ........");
        }
    }
    //inject into spring start lifecycle
    @Bean
    @Order(value = 1)
    public StartupRunner runner(){
        return new StartupRunner();
    }

    @Bean
    @Order(value = 2)
    public StartupRunner runner2(){
        return new StartupRunner(){

            @Override
            public void run(String... strings) throws Exception {
                System.out.println("start up 2 command is running......");
            }
        };
    }

    @RequestMapping("/")
    @ResponseBody
    public String home(){
        return "hello world!";
    }

}

```

## 启动springboot 应用

运行如下命令：

```sh
mvn spring-boot:run
```

就可以启动springboot的应用，默认是tomcat的容器，如果又需要修改tomcat的配置，再后面文章中说明。

## curl测试

使用curl简单测试一下，可以访问，是不是简单呀......

```sh
$ curl http://localhost:8080/                                                            
hello world!%
```

# HelloWorld In Flask

构建Flask的Micro Service 系列的第一篇，Hello World Service

## Flask 环境设置

- 安装Python3
- 创建干净的web 应用的python3 环境,python3 可以不用virtualevn，直接用一下命令就可以了
  ```sh
    python3 -m venv <your_application_name>
  ```

## Flask HelloWorld Service

```python
from flask import Flask

hello_world=Flask(__name__)

@hello_world.rooter('/')
def hello_world():
    return 'hello world!'


if __name__ == '__main__':
    hello_world.run()
```

## 运行Flask HelloWorld Service

直接运行次文件就可以了

## 使用AB 进行简单的性能测试

AB的脚本如下： -n 表述总数，－c 表述并发

```sh
# $1 is a parameter for java or python to record different performance result
ab -n 3000 -c 30 http://127.0.0.1:8080/ > $1-3K-30C.txt
ab -n 6000 -c 50 http://127.0.0.1:8080/ > $1-6K-50C.txt
ab -n 12000 -c 100 http://127.0.0.1:8080/ > $1-12K-100C.txt
```

最后的结果：

30 Currents:

SpringBoot:

```
Concurrency Level:      30
Time taken for tests:   5.828 seconds
Complete requests:      3000
Failed requests:        0
Total transferred:      522000 bytes
HTML transferred:       36000 bytes
Requests per second:    514.71 [#/sec] (mean)
Time per request:       58.285 [ms] (mean)
Time per request:       1.943 [ms] (mean, across all concurrent requests)
Transfer rate:          87.46 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0   42 443.0      2    5092
Processing:     0    4   2.7      4      19
Waiting:        0    3   2.4      3      19
Total:          1   46 442.9      6    5100

Percentage of the requests served within a certain time (ms)
  50%      6
  66%      7
  75%      8
  80%      9
  90%     12
  95%     15
  98%     19
  99%     30
 100%   5100 (longest request)


 Concurrency Level:      50
Time taken for tests:   1.161 seconds
Complete requests:      6000
Failed requests:        0
Total transferred:      1044000 bytes
HTML transferred:       72000 bytes
Requests per second:    5166.09 [#/sec] (mean)
Time per request:       9.678 [ms] (mean)
Time per request:       0.194 [ms] (mean, across all concurrent requests)
Transfer rate:          877.83 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    3   2.4      3      18
Processing:     1    6   3.3      6      32
Waiting:        0    5   3.0      4      30
Total:          3   10   4.0      8      33

Percentage of the requests served within a certain time (ms)
  50%      8
  66%      9
  75%     11
  80%     11
  90%     14
  95%     17
  98%     24
  99%     27
 100%     33 (longest request)

```

Flask: Current Level 100的时候没有timeout出现，不过springboot有而不能完成实验.
在100个并发前，SpringBoot比Flask略快，但是不知道什么原因springboot在100个并发的时候不能完成，这个会在后续使用中再做分析

```
Concurrency Level:      30
Time taken for tests:   2.598 seconds
Complete requests:      3000
Failed requests:        0
Total transferred:      498000 bytes
HTML transferred:       36000 bytes
Requests per second:    1154.77 [#/sec] (mean)
Time per request:       25.979 [ms] (mean)
Time per request:       0.866 [ms] (mean, across all concurrent requests)
Transfer rate:          187.20 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       3
Processing:     1   26   5.8     24      67
Waiting:        1   26   5.7     24      67
Total:          2   26   5.8     24      67

Percentage of the requests served within a certain time (ms)
  50%     24
  66%     25
  75%     25
  80%     27
  90%     32
  95%     37
  98%     45
  99%     52
 100%     67 (longest request)

 Concurrency Level:      50
 Time taken for tests:   4.731 seconds
 Complete requests:      6000
 Failed requests:        0
 Total transferred:      996000 bytes
 HTML transferred:       72000 bytes
 Requests per second:    1268.30 [#/sec] (mean)
 Time per request:       39.423 [ms] (mean)
 Time per request:       0.788 [ms] (mean, across all concurrent requests)
 Transfer rate:          205.60 [Kbytes/sec] received

 Connection Times (ms)
               min  mean[+/-sd] median   max
 Connect:        0    0   0.2      0       3
 Processing:     2   39   3.2     39      50
 Waiting:        2   39   3.2     39      50
 Total:          5   39   3.1     39      50

 Percentage of the requests served within a certain time (ms)
   50%     39
   66%     40
   75%     40
   80%     40
   90%     41
   95%     46
   98%     48
   99%     49
  100%     50 (longest request)

  Concurrency Level:      100
  Time taken for tests:   32.135 seconds
  Complete requests:      12000
  Failed requests:        0
  Total transferred:      1992000 bytes
  HTML transferred:       144000 bytes
  Requests per second:    373.43 [#/sec] (mean)
  Time per request:       267.790 [ms] (mean)
  Time per request:       2.678 [ms] (mean, across all concurrent requests)
  Transfer rate:          60.54 [Kbytes/sec] received

  Connection Times (ms)
                min  mean[+/-sd] median   max
  Connect:        0  167 1816.4      0   20069
  Processing:     1  101 149.1     74    1559
  Waiting:        1  100 149.0     74    1559
  Total:          1  267 1816.7     75   20070

  Percentage of the requests served within a certain time (ms)
    50%     75
    66%     79
    75%     81
    80%     86
    90%     98
    95%    180
    98%    720
    99%   1543
   100%  20070 (longest request)

```

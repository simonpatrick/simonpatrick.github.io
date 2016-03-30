---
layout: post
title: "Jenkins API的简单介绍"
modified:
categories: [automation]
image: jenkins.png
tags: [automation]
date: 2016-03-30T13:15:11+08:00
---

# Jenkins 介绍

Jenkins是一个非常有用的持续集成的工具，可以通过它完成代码的build，测试，发布等一系列的事情.

From Jenkins Home Page

```
Jenkins is an automation engine with an unparalleled plugin ecosystem to support all of your favorite tools in your delivery pipelines, whether your goal is continuous integration, automated testing, or continuous delivery.
```


## Jenkins 使用

关于Jenkins的基本使用网上有很多的教程，基本使用其事没有太多说的，它是个平台，可以集成很多不同的工具，脚本等等.
总结下来这些东西包括：

- jenkins parameter setting, string, choice, ......
- JAVA 的maven, ant, gradle 等打包工具，其他语言也有类似的build，deploy，依赖管理的工具
- 定制化的脚本，可以在一个Jenkins的build步骤中运行这些脚本如shell命令，python脚本
- 定制插件来完成自己的特殊的目的

这些内容非常庞大，自己也不可能完全都知道，如果遇到实际的一些问题需要解决的话,
大体的逻辑就是，如果遇到一些特殊需求，那么先去找插件看能不能完成，如果没有插件就再想shell，python脚本等不同的事情，或者自己开发插件.

## Jenkins 的实践问题

随着Jenkins里面的任务越来越多，管理的环境越来越多，变更越来愈多，手工管理就会遇到一些问题：

- 比如为了改一个IP地址，可能需要没一个任务都去改具体的配置，比如部署同一个war到不同的测试环境，就需要给不同的job改IP
- 为了不同的环境配置不同的任务，需要很多的人工的配置修改等等
- 如果需要迁移一个多应用的测试环境，那么需要很多的复制，修改工作

那么为了解决这些问题，个人觉得可以改善的地方是：
- 定义一些类型项目的模版，抽象一些参数出来给Jenkins里面的Job做参数话，当然有时需要修改的是默认值
- 在定义了一些模版之后，就可以通过操作Jenkins API的方式来操作
- 在尝试了一些Jenkins API之后，感觉纯粹通过API的方式去操作，不一定比复制Jenkins 任务，然后修改来的快，但是通过Jenkins API的方式
  来操作Jenkins 的好处是，如果这些东西融入到运维的流程中，那么它会提高生产率

一些体会是，可能代码方式的操作单个单个来看不一定会提高多少生产率(参数一样要设)，但是如果放在一个流程的角度看，那么他的效率是高的，比如你如果需要运维帮你建环境，那么你需要提供一些信息，而这些信息就可以直接建立Jenkins的Job了，那么作为用户你只提供一次信息，就可以完成你需要的所有事情，这样效率就高了.

我对于自动化一切的看法是，也许对于单个任务来说，通过写代码的方式不一定是最优方式，但是如果放在一个流程中来看，那么一定是.所以平常可以积累点不同类型的脚本，代码，然后在某个时间点，也许连接你的这些脚本，代码，就可以流水线化一些你的工作了，不要以为这不会带来，我觉得这一天一定会有的。

## Jenkins API 的使用

对于Jenkins API来说，我使用过Java和Python的，总结下来大同小异，逻辑上可以分为几个层次：

- Job: 不同类型的Job
  * 添加，修改，删除Job
  * Job的详细信息
  * 可以通过Job的config.xml文件来修改配置
  * Job创建属于哪个父类和Jenkins的URL有关系
- View
  基本功能和Job类似

### Jenkins API - JAVA

我自己使用的是这个Jenkins的这个API client.

```xml
    <dependency>
        <groupId>com.offbytwo.jenkins</groupId>
        <artifactId>jenkins-client</artifactId>
        <version>0.3.3</version>
    </dependency>
```

 这个包中最主要的两个类是：

- JenkinsServer: JenkinsServer 可以认为是一个JenkinsHttpClient的一个Wrapper，封装了一些常用的方法，如getJob，getJobXml等等，具体可以参考他[github](https://github.com/RisingOak/jenkins-client)
- JenkinsHttpClient：可以通过这个HttpClient组装URL和参数来达到完成调用其他API的方法，提供的一些方法主要包括了:
  - post
  - post_xml: 主要用来修改job的config.xml

大体的东西就是这些，那么通过这个Jenkins的API client，完成了一些一些功能：

- 复制Job,根据参数修改复制出来的Job
- 复制View，根据参数修改复制出来的View，同时包括了所有的子Job
- 查询到使用了某个shell 命令或者某个配置的任务

一些实例代码如下：

复制任务：

```java
public class JenkinsReplicator {
  private final String COPY_FROM_VIEW_URL = "/view/%s/createItem?";
  private final String DEFAULT_VIEW = "All";
  private JenkinsInstance instance;
  private JenkinsHttpClient client;

  public JenkinsReplicator(JenkinsInstance instance) {
      this.instance = instance;
      this.client = instance.getJenkinsHttpClient();
  }

  /**
   * @param fromName: copied from issue
   * @param toName:   new Name
   * @param parentName: to View name
   */
  public void copyItem(String fromName, String toName, String parentName) {
      Map<String, String> formData = new HashMap<>();
      formData.put("name", toName);
      formData.put("mode", "copy");
      formData.put("from", fromName);
      formData.put("json", String.format("{\"name\": \"%s\", \"mode\": \"copy\", \"from\": \"%s\"}", toName, fromName));
      formData.put("Submit", "OK");
      try {
          this.client.post_form(String.format(COPY_FROM_VIEW_URL, parentName), formData, false);
      } catch (IOException e) {
          throw new JenkinsBaseException("copy item "+ fromName+ "to " + toName+" in view " + parentName + " failed", e);
      }
  }
}
```

update config file:

```java
String configXml = jobDescription.jobConfigXml();
this.getJenkins().updateJob(jobDescription.getJobName(),configXml,false);
```

复制整个view下面同时包括了不同的子Job:

```java
@Override
   public View copy(String fromName, String toName, String parentNameOrNull) {
       View fromView = getByName(fromName);
       if (fromView == null) throw new JenkinsViewException(fromName + "view is not found,can't copy from it!");
       View toView = getOrCreate(toName, fromName, parentNameOrNull);
       Map<String, Job> viewJobs = jobController.getJobsByViewName(fromName);
       for (Map.Entry<String, Job> entry : viewJobs.entrySet()) {
           jobController.copy(entry.getKey(), toName + "_" + entry.getKey(), toView.getName());
       }

       return getByName(toName);
   }

```

## Python API 使用

Python的Jenkins API client 可以通过以下命令安装：

```sh
  pip install jenkinsapi
```

基本的python jenkins api client 和JAVA的概念比较类似，不过python 的这个jenkinsapi很明显要比java的这个客户端功能要丰富的多的多，后面会详细介绍这个python client api的使用.

## 代码

[GITHUB](https://github.com/testless/jenkins-controller.git)

---
layout: post
title: "tomcat-jmx-monitoring"
modified:
categories: [java]
image: 21.jpg
tags: [java]
date: 2015-11-15T16:56:08
---

Tomcat JMX Monitoring

- Access Data Via JMX "MBeans"
- Read/Write Bean Attributes
- Invoke Operations
- Receive Notifications
- JVM Exposes certain status
- Tomcat Exposes certain status

## Monitoring JVM

- Head status
- Total,Free Used Memory
- GC(Garbage Collection)
- GC Pause Time

## Monitoring Tomcat

- Status of Connector
- Status of request-processor thread pool
- Status of data sources
- Request performance

## JMX Tools

- jconsole (jdk)
- VisualVM (jdk)
- Most Profiles (Yourkit,etc.)
- Custom tools using javax.management

## Monitoring Your Application

- Monitor Application Processes
- Performance Metrics
- On-the-fly re-configuration
- Write An MBean
  - Create an Interface
  - Create an Implementation
  - Create an XML MBean descriptor
- Deploy package to Tomcat
  - Publish the MBean to the MBean server
- Query/invokes as neccessary


## Example MBean
  ttern
- Servlet Filter that captures total request processing time
  - Timestamp prior to request
  - Timestamp after request
  - Add the delta to a JMX-accessible counter: RequestStats


## Automated Monitoring

- Remote Access
- Large Scale
- Constant
- Tools:
  - Nagios
    - Simple
    - Flexible
    - Well-deployed
    - No-cost community version
    - Plug-in architecture
    - Freely-avaiable JMX Plug-in: check_JMX
    - JMXProxyServlet
    - Tracking Values over time
    - Detecting OutOfMemory
      - Heap exhaustion
      - PermGen exhaustion
      - Hit thread limit
      - Hit file descriptor limit
      - Two types of Heap OutOfMemory
        - One Thread generates lots of local reference
        - All Threads collaborate to generate global reachable objects
      - Former is recoverable,latter is not
      - Memory Pool Threshold
        - Polling using check_JMX
        - Register a notification listener
        - Use -XX:OnOutOfMememoryError on first OOME

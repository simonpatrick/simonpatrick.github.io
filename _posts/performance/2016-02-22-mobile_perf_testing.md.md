---
layout: post
title: "mobile_perf_testing.md"
modified:
categories: [performance]
excerpt:
tags: [performance]
date: 2016-02-22-09:40:07
---

# 移动端性能测试的一些关键点

阅读了一些人的PPT，再这里记录一些移动端性能测试的一些关键点，每个关键点会在后续润色，细化.

## 移动端性能测试的方方面面

### Android
- Monkey
- Memory Usage:
  ```
    /system/build.prop
    dalvik.vm.heapstartsize=8m
    # 堆分配的初始大小
    dalvik.vm.heapgrowthlimit=64m
  ```  
- adb shell procrank
- DDMS
- adb shell top
- 启动性能(首次，多次)
- 流量
- 应用占用量，cachesize，datasize，codesize
- 电量
- CPU: active, idel
- memory leak, hprof, ddms dump hprof
- GPU 过度绘制
  1.蓝色1x过度绘制
  2.绿色2x过度绘制
  3.淡红色3x过度绘制
  4.红色超过4x过度绘制
- gfxinfo
- systrace
- traceview
- tracer for OpenGL ES


### IOS

- instruments
- api
- business flow/scenario

## Performance Baseline
- comparison
- 颗粒度
- Business flow
- Automation supporting
- poor network condition

## Security
- 混淆
- 加固
- 权限
- 本地数据库安全
- ContentProvider共享
- Activity注入风险

## Tools
- Fiddler
- Charles
- Burpsuites
- Anyproxy
- lint
- findbugs
- PMD
- oclint
- scan-build
- pro-guarded

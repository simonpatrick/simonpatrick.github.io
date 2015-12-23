# Selenium Grid 
selenium grid让并行跑测试用例变为可能

## 启动 Selenium Grid

启动selenium server/grid hub:

```sh
java -jar selenium-server-standalone-2.25.0.jar -port 4444 -role hub
-nodeTimeout 600
```

增加node:

```sh
java -jar selenium-server-standalone-2.25.0.jar -role webdriver
       -browser "browserName=internet explorer,version=8,maxinstance=1,pl
       atform=WINDOWS" -hubHost localhost –port 8989
```

使用configuration json 添加node:

```json
{
"class": "org.openqa.grid.common.RegistrationRequest",
"capabilities": [
{
} ],
"seleniumProtocol": "WebDriver",
"browserName": "internet explorer",
"version": "8",
"maxInstances": 1,
"platform" : "WINDOWS"},
configuration:{
"port":8989,
"register": true,
"host": "192.168.1.100",
"proxy": "org.openqa.grid.selenium.proxy.
   DefaultRemoteProxy",
"maxSession": 2,
"hubHost": "192.168.1.100",
"role": "webdriver",
"registerCycle": 5000,
"hub": "http://192.168.1.100:4444/grid/register",
"hubPort": 4444,
"remoteHost": "http://192.168.1.101:8989"}
}
```
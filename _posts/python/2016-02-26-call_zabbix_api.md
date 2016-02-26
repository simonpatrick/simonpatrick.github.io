---
layout: post
title: "访问Zabbix API"
modified:
categories: [python]
excerpt:
tags: [python]
date: 2016-02-26-16:51:20
---

## Zabbix API 访问

准备使用Python来访问一下Zabbix，首先当然阅读一下Zabbix的[API Manual](https://www.zabbix.com/documentation/2.4/),抛开什么json rpc这样的问题之外，zabbix的API的分类还是很工整的，所以看起来比较舒服，在一定了解了zabbix基础之后，基本上就可以上手来写了，网上查了一下，找个一个python zabbix的调用的一个客户段代码，感觉不错，就开始行动了。

## Zabbix API 客户端代码的实现
Zabbix API的主要的两个参数其实是method，params，params基本上就可以看作一些可变的参数，其实就是一个json或者map， 对于method来说，一般就是 resource.action 这种方式，所以python客户端使用重写了一个__getattr__来做,返回一个可以访问不同资源名称的客户端,具体的代码如下：

```python
class ZabbixClient:
    """
    Generic Zabbix API Client
    - login
    - get auth
    """
    globale_header = {
        "Content-Type": "application/json-rpc"
    }

    def __init__(self, session=None, timeout=None):
        self.user_name, self.default_user_name = '1', '1'
        self.password, self.default_password = '123456', '123456'
        self.zabbix_api_url = 'http://{0}/api_jsonrpc.php'.format('abcd.http')
        if session:
            self.session = session
        else:
            self.session = requests.session()

        self.session.headers.update({
            'Content-Type': 'application/json-rpc',
            'User-Agent': 'python-zabbix-client',
            'Cache-Control': 'no-cache'
        })

        self.auth = ''
        self.id = 0
        self.timeout = timeout
        logger.info('JSON-RPC Server EndPoint: %s', self.zabbix_api_url)

    def login_in(self, user_name=None, password=None):
        """
        login with given user_name and password, if None, use default user
        :param user_name:
        :param password:
        :return: result,auth key
        """
        if user_name:
            self.user_name = user_name

        if password:
            self.password = password

        self.auth = self.user.login(user=self.user_name, password=self.password)

    def api_version(self):
        return self.apiinfo.version()

    # def confimport(self, format='', source='', rules=''):
    #     """Alias for configuration.import because it clashes with
    #        Python's import reserved keyword"""
    #
    #     return self.do_request(
    #         method="configuration.import",
    #         params={"format": format, "source": source, "rules": rules}
    #     )['result']

    def do_request(self, method, params=None):
        request_json = {
            'jsonrpc': '2.0',
            'method': method,
            'params': params or {},
            'id': self.id,
        }

        if method != 'apiinfo.version' and self.auth:
            request_json['auth'] = self.auth

        logger.debug("sending: %s", json.dumps(request_json, indent=4, separators=(',', ':')))
        response = self.session.post(
            self.zabbix_api_url,
            data=json.dumps(request_json),
            timeout=self.timeout
        )
        logger.debug("Response Code : %s", str(response.status_code))

        response.raise_for_status()

        if not len(response.text):
            raise ZabbixAPIException("没有返回值")

        try:
            response_json = json.loads(response.text)
        except ValueError:
            raise ZabbixAPIException("不能解析JSON %s" % response.text)

        logger.debug("sending: %s", json.dumps(request_json, indent=4, separators=(',', ':')))

        self.id += 1

        if 'error' in response_json:
            if 'data' not in response_json['error']:
                response_json['error']['data'] = 'No Data'
            msg = "Error {code}: {message},{data}".format(
                code=response_json['error']['code'],
                message=response_json['error']['message'],
                data=response_json['error']['data']
            )
            raise ZabbixAPIException(msg, response_json['error']['code'])

        return response_json

    def __getattr__(self, item):
        """
        auto create Zabbix API Client
        :param item:
        :return:
        """
        return ZabbixAPIObjectClass(item, self)


class ZabbixAPIObjectClass(object):
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent

    def __getattr__(self, item):

        """
        dynamic create a method (get,create,update,delete)
        :param item:
        :return:
        """

        def fn(*args, **kwargs):
            if args and kwargs:
                raise TypeError('Found Both args and kwargs')

            return self.parent.do_request('{0}.{1}'.format(self.name, item),
                                          args or kwargs)['result']

        return fn

```

基本上一个文件就搞定了，不过这个基本上参考了网上的一个代码实现的，这里使用__getattr__这种方式可以非常简洁的处理了这种请求非常类似的情况，这也是python的魅力吧.

## 访问Zabbix API

访问API比较简单(如何参数不多的话，哈哈)，实例代码取Template的一些信息如下:

```python
class TestZabbixTemplateClient(unittest.TestCase):

    def setUp(self):
        self.zapi = ZabbixClient()
        self.zapi.login_in()

    def test_get_template(self):
        templates = self.zapi.template.get()
        print(templates)

    def test_get_template(self):
        templates = self.zapi.template.get(
            filter={
                "host": ["Template OS Linux"]
            })
        print(templates[0]["id"])

    def test_create_template(self):
        template = self.zapi.template.create()
```

补充一句，就是其实可以看到：
- ZabbixClient这个类没有定义template，可是他去可以使用？写了JAVA人是不是感觉有点惊喜的感觉
- template也没有create这个方法呀，他是怎么做到的？？

这个例子很好的说明了使用__getattr__可以做一些魔法的事情

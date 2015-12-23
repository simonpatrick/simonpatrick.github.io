# Restful API
- What is Restful API
	* Rest = REpresentation State Transfer
	* Rest VS Soap
	* XML VS JSON

- Rest/JSON is first choice to use

REF:
[SIIDES](http://www.slideshare.net/rmaclean/json-and-rest )
[Beautiful REST +JSON APIs](http://www.youtube.com/watch?v=hdSrT4yjS1g)


## CURL 

```shell
curl -v http://httpbin.org/get
curl http://httpbin.org/get
```

python urllib2,please don't use it

## Requests(Python)

Simple Beautiful,Pythonic

### requests
- simple get sample

```python
url = "http://www.xueqiu.com/p/ZH176890"
headers ={"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36",\
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
        }

r = requests.get(url,headers=headers)
print r.text
```

- post sample

```shell
curl -X post -d '{"public":true}' https://httpbin.org/post

```

```python
url = "http://www.xueqiu.com/p/ZH176890"
headers ={"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36",\
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
        }

json.dumps({'public':'true'})
r=requests.post(url,headers=headers)
print r.status_code
```

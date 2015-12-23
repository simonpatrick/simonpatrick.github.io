# Nginx 基础 
Notes from [nginx zero](http://oilbeater.com/nginx/2014/12/29/nginx-conf-from-zero.html)

Nginx 最常的用途是提供反向代理服务，以下是Nginx的基础原理：
![img](http://oilbeater.qiniudn.com/reverseproxy.png)

代理服务器作为客户端的中介接受请求，隐藏掉真实的客户，向服务器获取资源。如果代理服务器在长城外的话还能顺便帮助我们实现翻越长城的目的。而反向代理顾名思义就是反过来代理服务器作为服务器的中介，隐藏掉真实提供服务的服务器，原理大致如下图：

[!img](http://oilbeater.qiniudn.com/proxy.png)

## install

```sh
sudo apt-get install nginx
sudo service nginx start
curl http://localhost:80
```

## configuration

nginx 默认配置文件位置： ```/etc/nginx/nginx.conf```

配置文件中，外部配置文件的加载：

```sh
include /etc/nginx/site-enabled/*
```

外部配置实例：
```sh
server {
    server_name localhost;
    listen 80 default_server;
    listen [::]:80 default_server ipv6only=on;

    root /usr/share/nginx/html;
    index index.html index.htm;

    location / {
    try_files $uri $uri/ =404;
    }
}
```
## 虚拟主机

主站下面有子站，可以配置不同的server，servername

## proxypass 负载均衡

```sh
location / {
    proxy_pass 123.34.56.67:8080;
}
```

添加upstream 模块 实现负载均衡：

```sh
upstream backend {
    ip_hash;    
    server backend1.example.com;
    server backend2.example.com;
    server backend3.example.com;
    server backend4.example.com;
}
location / {
    proxy_pass http://backend;
}

```

## nginx reload

```sh
sudo service nginx reload
```

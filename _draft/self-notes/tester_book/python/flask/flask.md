# Flask 
## Install Flask

```shell
 pip install flask
```

## Quick Start
### 最小应用

```python
	from flask import Flask
	app = Flask(__name__)

	@app.route('/')
	def hello_world():
	    return 'Hello World!'

	if __name__ == '__main__':
	    app.run()
```

### 外部可见服务器配置

```python
	app.run(host='0.0.0.0:5000')
```

### 调试模式

```python
	app.debug = True
	app.run(debug=True)
```

### Route

route() 装饰器

```python
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'
```

### 变量规则

<variable_name>或者<converter:variable_name>
转换器:
|转换器|描述|
|-----|----|
|int|整数|
|float|浮点数|
|path|和默认相同，接受/|

```python
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
```

```python

@app.route('/projects/') # mapping /projects && /projects/
def projects():
    return 'The project page'

@app.route('/about') #mapping /about
def about():
    return 'The about page'
```

### HTTP 方法

```python

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()

```

### 静态文件

默认是static目录

```python
url_for('static', filename='style.css')
```

### render 模板

flask 从templates文件内寻找模板

```python
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```

### 模板中访问request，session,g
### 操作请求数据
使用全局对象request请求信息，但是如何保持线程安全？

#### 内部信息
本地对象的代理
设想现在处于处理线程的环境中。一个请求进来了，服务器决定生成一个新线程（或者 叫其他什么名称的东西，这个下层的东西能够处理包括线程在内的并发系统）。当 Flask 开始其内部请求处理时会把当前线程作为活动环境，并把当前应用和 WSGI 环境 绑定到这个环境（线程）。它以一种聪明的方式使得一个应用可以在不中断的情况下 调用另一个应用。


### 文件上传

header：
```enctype="multipart/form-data"```

```python
from flask import request
from werkzeug import secure_filename

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))
    ...
```

### Cookie

```python
from flask import make_response

@app.route('/')
def index():
    resp = make_response(render_template('hello.html','patrick'))
    resp.set_cookie('username', 'patrick')
    return resp
```

### 重定向和错误

```python
	from flask import abort, redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()
```

### 会话
### Logging
```python
	app.logger.debug('debug information')
	app.logger.warning('warning message')
	app.logger.error('error message')
```

Python 标准类 [logging](http://docs.python.org/library/logging.html)

### 集成WSGI中间件

```python
from werkzeug.contrib.fixers import LighttpdCGIRootFix
app.wsgi_app = LighttpdCGIRootFix(app.wsgi_app)
```

### Deployment
[link](http://dormousehole.readthedocs.org/en/latest/deploying/index.html#deployment)
# Advance of Flask

## Statement management
flask三个主要的状态：
- Setup State
- Application Context Bound
- Request Context Bound

flask的关于状态的用法：
- flask.current_app => applicaton-context
- flask.g => applicaton-context (as of 0.10)
- flask.request => request-context
- flask.session => request-context
- Application contexts are fast to create and destroy
- pushing request context push new Application context
- bind resources to application context

## Resource management
主要功能：
- Create/destroy application context => task
- Bind resources task wise
- Resources: claimed database connections,caches

### Teardown Illustrated -- todo need more learning

```python
@app.test_request_context
def call_on_teardown(error=None):
    print('tearing down, error:', error)
```

### Response Object Passing
- One request object: read only
- Potentially many response objects ,passed down a stack
- ... can be implicitly created
- ... can be replaced by other resopnse objects
- there is no flask.response

### implicitly Response Creation

```python
@app.route('/')
def index():
  return render_template('index.html')
```

### Explicit Creation
```python
from flask import make_response
@app.route('/')
def index():
    body = render_template('index.html')
    response = make_response(body)
    response.headers['X-Powered-By'] = 'Not-PHP/1.0'
    return response
```

### Customized Creation

```python
from flask import Flask, jsonify
class CustomFlask(Flask):
    def make_response(self, rv):
        if hasattr(rv, 'tojson'):
            return jsonify(rv.tojson())
        return Flask.make_response(self, rv)
```

customized flask example:
```python
class User(object):
    def __init__(self, id, username):
        self.id = id
        self.username = username
    def tojson(self):
        return {
            'id': self.id,
            'username': self.username
        }
app = CustomFlask(__name__)
@app.route('/')
def index():
    return User(42, 'john')
```

### Server Send Event
Basic Overview
- Open Socket
- Send "data: <data>\r\n\r\n</data>" packets
- Good idea for gevent/eventlet,bad idea for kernel level concurrency

Subscribing

```python
from redis import Redis
from flask import Response, stream_with_context
redis = Redis()
@app.route('/streams/interesting')
def stream():
    def generate():
        pubsub = redis.pubsub()
        pubsub.subscribe('interesting-channel')
        for event in pubsub.listen():
            if event['type'] == 'message':
                yield 'data: %s\r\n\r\n' % event['data']
    return Response(stream_with_context(generate()),
                    direct_passthrough=True,
                    mimetype='text/event-stream')
```

Publishing

```python
from flask import json, redirect, url_for
@app.route('/create-something', methods=['POST'])
def create_something():
    create_that_thing()
    redis.publish('interesting-channel', json.dumps({
        'event': 'created',
        'kind': 'something'
    }))
    return redirect(url_for('index'))
```

### Don't be afraid of Proxy
- gunicorn/uwsgi blocking for main app
- gunicorn gevent for SSE
- nginx for unification


## Worker Separation
supervisor config:
```sh
[program:worker-blocking]
command=gunicorn -w 4 yourapplication:app -b 0.0.0.0:8000
[program:worker-nonblocking]
command=gunicorn -k gevent -w 4 yourapplication:app -b 0.0.0.0:8001
```
ngix config:

```sh
server {
    listen 80;
    server_name example.com;
    location /streams {
        proxy_set_header Host $http_host;
        proxy_pass http://localhost:8001/streams;
}
    location / {
        proxy_set_header Host $http_host;
        proxy_pass http://localhost:8000/;
}
 }

```

## Signing Stuff
Basic Overview:
- Use itsdangerous for signing information that roundtrips
- Saves you from storing infomration in a database
- Especially useful for samll pieces of information that need to stary
around for long(any form of token etc.)

User Activation Example:
```python
from flask import abort
import itsdangerous
serializer = itsdangerous .URLSafeSerializer(secret_key=app.config['SECRET_KEY'])
ACTIVATION_SALT = '\x7f\xfb\xc2(;\r\xa8O\x16{'
def get_activation_link(user):
    return url_for('activate', code=serializer.dumps(user.user_id, salt=ACTIVATION_SALT))
@app.route('/activate/<code>')
def activate(code):
    try:
        user_id = serializer.loads(code, salt=ACTIVATION_SALT)
    except itsdangerous.BadSignature:
        abort(404)
    activate_the_user_with_id(user_id)
```

## Customization
Simple Cache Busting:
```python
from hashlib import md5
import pkg_resources
ASSET_REVISION = md5(str(pkg_resources.get_distribution(
    'Package-Name').version)).hexdigest())[:14]
@app.url_defaults
def static_cache_buster(endpoint, values):
    if endpoint == 'static':
        values['_v'] = ASSET_REVISION
```

Disable Parsing:

```python
from flask import Flask, Request
class SimpleRequest(Request):
    want_form_data_parsed = False
    data = None
app = Flask(__name__)
app.request_class = SimpleRequest

```

## Secure Redirects
Redirect Back:
```python
from urlparse import urlparse, urljoin
def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc
def is_different_url(url):
    this_parts = urlparse(request.url)
    other_parts = urlparse(url)
    return this_parts[:4] != other_parts[:4] and \
        url_decode(this_parts.query) != url_decode(other_parts.query)
def redirect_back(fallback):
    next = request.args.get('next') or request.referrer
    if next and is_safe_url(next) and is_different_url(next):
        return redirect(next)
    return redirect(fallback)
```

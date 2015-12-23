# Flask Basic

这章主要学习Flask的以下几个知识点：
- Setup virtualenv
- basic configuration of Flask
- Class-based configuration
- organized static files
- Being depoyment specific with instance folders
- Composition of views，controllers and models
- creating modular web app with blueprint
- making a flask app installable using pip or setup tools

## Setup virtualenv
### install pip
### install Flask

```shell
pip instal Flask
```
### install virtualenv
```shell
pip install virtualenv
virtualenv basic # create an clean python environment for development
cd basic && source bin/activate # activate the environment
pip install flask -U  # install flask only into the development environment
```
### install virtualenvwrapper
```shell
pip install virtualenvwrapper
export WORK_ON=~/workspace
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv flask
pip install flask
```

### deactivate 
```shell
deactivate
```
### workon a virtualenv
```python
workon flask
```

## Flask Basic Configurations
- debug options
```python
app.run(debug=True)
# or
app.configure['debug']=True
```
- fetch configuration from a *.cfg file
```python
app.config.from_pyfile('myconfig.cfg')
```
- fetch configuration from a object
```python
app.config.from_object('myapplication.default_setting')
```

- fetch configuration from envrionment variable
```python
app.config.from_envvar('PATH_TO_CONFIG_FILE')
```

- use convension
```python
DEBUG = True
TESTING = True
app.config.from_object(__name__)
app.config.from_pyfile('path/to/config/file')
```

## Class based setting

class based setting for different deployment modes

```python

class BaseConfig(object):
    'Base Config class'
    SECURTY_KEY='A random secret key'
    DEBUG = True
    TESTING = False
    NEW_CONFIG_VARIABLE ='my value'


class ProductionConfig(object):
    'Production kConfig class'
    SECURTY_KEY=open('/path/to/secret/file')
    DEBUG = False
    TESTING = False
    NEW_CONFIG_VARIABLE ='my value'

class StagingConfig(object):
    DEBUG = True

class DevelopmentConfig(object):
    DEBUG = True

 `loading configuration from object`
 app.config.from_object('config.DevelopmentConfig')
```

## Organization of static files
```python
app = Flask(__name__,static_folder='paht_to_static_file')
'or '
app = Flask(
    __name__,static_url_path ='/differntstatic',
    static_folder ='path_to_static_file'
)
```

## deployment specific deployment parts
默认情况下，instance目录在应用启动时会被扫描并且被加载，不过也可自定义这个值
```python
app = Flask(__name__,instance_folder='path_to_instance_folder')
'config file is also in instance folder use instance_relative_config =True'
app = Flask(__name__,instance_folder='path_to_instance_folder',
        instance_relative_config=True)
app.config.from_pyfile('config.cfg',silent=True)
```

## Compositon of views ,models, controllers
- model -- data sturcture
- view or controllers  : a route to different view
- app.py or run.py or __init___.py in different package 

## User blueprint for modular web app  

## Setuptools/requirement
learning different install methods for following tools:
- Setuptools
- pip 



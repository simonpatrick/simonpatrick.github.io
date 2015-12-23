# Virtualenv 
virtualenv 是用来构建一个隔离的python环境

## Install and Simple Usage
```shell
    pip install virtualenv
    virtualenv env
    cd env
    source bin/activate
    deactivate

```

## Install Flask

```shell
	pip install flask
```

## User virtualenvwrapper

```shell
$ pip install virtualenvwrapper
...
$ export WORKON_HOME=~/Envs
$ mkdir -p $WORKON_HOME
$ source /usr/local/bin/virtualenvwrapper.sh
$ mkvirtualenv env1
```

## pip usage
- install/uninstall/update

```shell
pip install junit-xml #latest version
pip install junix-xml =1.2 # specific version
pip uninstall junix-xml
pip install ---upgrade junix-xml
```

- pip generate package list

``` shell
pip lis
pip freeze > requirement.txt
pip install -r requirement.txt
```

- install local packages from mirror

``` shell
pip install --index-url <url>

```

## write a setup.py

setup and runnable script after installation


```python
from distutils.core import setup
setup(name="hello",
version='0.0.1',scripts=['hello.py'],
py_mpdule=['hello'],)
```

```shell
python setup.py sdict
pip isntall dist/hello.0.0.1.zip
find ~/env |grep hello
hello.py
```






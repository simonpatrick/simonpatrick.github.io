# Bower 介绍
Bower是一个客户端技术的软件包管理器，
它可用于搜索、安装和卸载如JavaScript、HTML、CSS之类的网络资源。
其他一些建立在Bower基础之上的开发工具，如Yeoman和Grunt.

## Bower的好处
- 方便安装开发中需要的第三方依赖，不用再去往常查找
- 脱机工具，下载下来的第三发依赖会存放在本地，类似于JAVA MAVEN的本地仓库(Local Repository)
- 方便的定义依赖关系
- 升级更加简单，只需要改变依赖包版本就可以了

## Bower的使用
下面介绍Bower的使用，首先需要安装Bower,bower需要安装node/npm(如何安装就不介绍了)，然后使用npm安装就可以了


```sh
# -g 表示全局安装
npm install -g bower
```

使用bower help:

```sh
bower help
usage:

    bower <command> [<args>] [<options>]
Commands:

    cache                   Manage bower cache
    help                    Display help information about Bower
    home                    Opens a package homepage into your favorite browser
    info                    Info of a particular package
    init                    Interactively create a bower.json file
    install                 Install a package locally
    link                    Symlink a package folder
    list                    List local packages - and possible updates
    login                   Authenticate with GitHub and store credentials
    lookup                  Look up a package URL by name
    prune                   Removes local extraneous packages
    register                Register a package
    search                  Search for a package by name
    update                  Update a local package
    uninstall               Remove a local package
    unregister              Remove a package from the registry
    version                 Bump a package version
Options:

    -f, --force             Makes various commands more forceful
    -j, --json              Output consumable JSON
    -l, --log-level         What level of logs to report
    -o, --offline           Do not hit the network
    -q, --quiet             Only output important information
    -s, --silent            Do not output anything, besides errors
    -V, --verbose           Makes output more verbose
    --allow-root            Allows running commands as root
    --version               Output Bower version
    --no-color              Disable colors
See 'bower help <command>' for more information on a specific command.

```

### Bower 安装第三方依赖
使用bower 安装第三方依赖很方便：

```sh
bower install bootstrap 
```

bootstrap 就安装好了，默认情况下，bower会把第三方包放在当前目录相面的bower_components的目录

### 查看bower安装的包

使用如下命令：
```sh
bower lsit
```

### 搜索bower 安装包

```sh
bower search angular
```

### 查看bower 包信息

```sh
bower info bootstrap
```

### 卸载bower包

```sh
bower uninstall bootstrap
```

### bower.json文件的使用

bower.json的作用是记录下个所有安装的包的记录，类似于JAVA MAVEN的pom文件
每次使用bower install/uninstall 命令都会相应的更新此文件




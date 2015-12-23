# GIT 
git是个分布式版本控制系统，所谓分布式版本控制就是任何一个在自己其实上就可以进行版本控制管理而无需连接中央服务器，这样提交代码就无需收到联网的限制。同时GIT提供了更好的branch等功能，也是目前最流行的工具.

## Git 配置

全局变量设置：

```sh
git config --global user.name "Your name"
git config --global user.email "emailname@example.com"
```

## 创建版本库

```sh
//不是必须在空目录中使用git init命令
git init

```
建立成功之后，当前目录会多一个.git目录，有些代码库很大，其实大的就是这个.git文件夹


## 提交改动

```sh
git add .
git commit . -m "add new changes"

```

## 查看当前仓库状态

查看当前仓库状态的命令：

```sh
git status
```

## 查看git 日志

```sh
git log
git log --pretty=oneline
```

## 回滚git的提交

```sh
git rest --hard
git rest --hard XXXXX-changeId
```

## git workspace，stage，head
git里面又工作区，版本库（stage），head，git add命令将改动放到stage，最后提交则提交到head

## git checkout

```sh
git checkout --file
git checkout
```

## 远程仓库

创建远程仓库，以github为例，一般步骤是：
1. github注册用户
2. github创建一个仓库

```sh
ssh-keygen -t rsa -C "emailaddrss"
git remote add origin <github addrss>
git push -u origin master //关联远程仓库和本地仓库
```
多人合作模式，一般的工作流程如下：
1. clone git Repository
2. 创建本地分支
3. 提交改动到远程相对应的分支
4. 解决冲突
5. 建立分支关系(如果出现 no tracking information就需要此步骤)

以下是对应的命令：

```sh
git clone <branch-path>
git checkout -b branch_name
git push origin branch-name
git branch --set-upstream branch-name origin/branch-name
```

## 分支管理
分支的实际作用，假设需要开发一个新的版本，需要两周完成，那么中间可能会提交不工作的代码，为了避免影响其他人，所以就开一个分支.
不过现在有些公司提倡主干开发，直接在主干上开发，通过单元测试等等保证功能不会出现大问题。

创建分支，创建分支时，也就是将当前head指向了新分支
```sh
//-b 就是创建一个新分支
git checkout -b dev
//创建分支但是不checkout
git branch dev
//查看branch 列表
git branch
```

合并分支

```sh
//切换到主干
git checkout master
//合并分支
git merge dev
//删除dev 分支
git branch -d dev
```

## 解决冲突

提交时发生冲突，需要手动修正

```sh
git log -graph  //查看分支合并图
```

## 合并分支- 不使用fastforward

```sh
git merge --no-ff -m "merge with no-ff"
```

bug 分支,可能某时需要紧急修改一个bug，但是当前又有没有测试胆码
这是可以使用git stash 保存当前工作情况
```sh
git stash
```

当修改完毕之后，恢复保存的内容,丢弃之前的内容都可以以下命令做到：

```sh
git stash list
git stash pop
git stash apply stash@{0}
git stash drop
```

## Git Tag标签管理

```sh
git tag v1.0
git tag
git tag v0.6 change_id
git show v0.6
git tag -s v0.2 //采用PGP签名
```

## Git 配置

```sh
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
```

# git scripts
ssh-keygen -t rsa -C "{email}"

# eval ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa

#copy to clipboard
pbcopy < ~/.ssh/id_rsa.pub

## git init command
git init
git add .
git commit . -m "init project"

## git pull
git branch --set-upstream-to=origin/master

## create new repository
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/simonpatrick/stepbystep-js.git
git push -u origin master

## remote add repository
git remote add origin https://github.com/simonpatrick/stepbystep-js.git
git push -u origin master
## remote add ssh
git remote add origin git@github.com:simonpatrick/stepbystep-js.git


全局设置:
git config --global user.name 'simonpatrick'
git config --global user.email 'simonpatrick@163.com'
2接下来:
您可以在本地创建新的 Git 仓库
mkdir testerplayground
cd testerplayground
git init
touch README.md
git add README.md
git commit -m 'first commit'
git remote add origin 'git@gitcafe.com:simonpatrick/testerplayground.git'
git push -u origin master
或者提交在本地已有 Git 仓库
cd existing_git_repo
git remote add origin 'git@gitcafe.com:simonpatrick/testerplayground.git'
git push -u origin master



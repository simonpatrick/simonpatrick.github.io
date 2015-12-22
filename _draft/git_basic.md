# Git Branch

```sh
  git checkout -b dev
  # do some changes
  # checkout master
  git checkout master
  # merge change without Fast Forward, fast Forward used, delete the branch might be lost branch information
  git merge --no-ff -m "merge with no-ff" dev
```

```
git branch
git branch <name>
git checkout <name>
git checkout -b <name>
git merge <name>
git branch -d <name>

```

# Review Board Code Review
## APIs
- updateRepositoryData 更新数据
- validCredentials 更新注册信息
- getReviewRequests 获取review Request
- getReviewRequestDraft
- isReviewRequestDraft
- getReviews
- publishReviewRequest
- updateReviewRequest
- updateReviewRequestFilterNoValue
- newReviewRequest
- uploadDiff


## RBTools
- .reviewboardrc

### RBTools
命令
### rbt setup-repo
* REPOSITORY
* REVIEWBOARD_URL
* TRACKING_BRANCH
* BRANCH
* ENABLE_PROXY
* ```svn propset reviewboard:url http://reviewboard.example.com .```

### rbt post
post is default for pre-commit review

- post a new file ```//path/to/file```
- post files ```//path/to/dir```
- post ```//path/to/file[@#]rev,[@#]rev```
- post ```//path/to/dir @#]rev,[@#]rev```
- ```rbt post -r 42``` post a new review request
- ```rbt post -I src/foo.c -I data/bar.png``` post uncommited file to reviewboard
- ```rbt post STARTREV STOPREV``` or ```rbt post STOPREV```
- ```rbt post --diff-filename=mycode.diff``` post will generate diff file
- Auto-Setting Summary and Description 
- auto post for post commit review using svn hook

### rbt diff
- start with ```rbt diff```
- ```revision-range``` <r1:r2>
- ```-I <filename>,--include <filename>```
- ```-X <pattern>,--exclude <pattern>```
- ```--diff-filename```
- ```--repository```
- ```--repository-url <url>```
- ```--repository-type```
- ```--svn-username --svn-password```
- ```--svn-changelist <id>```

### rbt land
rbt land 是为了提交一个已经审核通过的提交
- ```rbt land [option] <branch-name>```

### rbt patch

- ```rbt patch <rr_id>```

### rbt api-get

- ```rbt api-get <path> -- --query_k=query_v```
- ``` rbt attach --filename -d```
- ```rbt clear-cache```
- ```rbt close <rr-id>```
- ```rbt login```
- ```rbt logout```
- ```rbt publish <rr-id>```
- ```rbt status```
- ```rbt stamp``` lookup a review request matching the latest commit 
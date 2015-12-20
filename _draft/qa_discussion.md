# Testing Without QA

最近在看一些关于需要不需要QA的文章,以下是一些关于这些讨论的文章。

- [testing-without-qa](https://www.madetech.com/blog/testing-without-qa)
-[quality-assurance-in-small-developer-teams](http://stackoverflow.com/questions/2657479/quality-assurance-in-small-developer-teams)
## 观点
- We don't make use of a dedicated QA or test role
* challenges
  - decrease in development quality
  有了测试之后质量反而下降,潜意识会放松
  - increased cycle time

｜Where a defect is rectified｜	Cost｜
｜In development｜	£0.10｜
｜In test｜	£1.00｜
｜In production｜£10.00｜

  - Externalised Testing
  some externalisation issues and add overhead if QA is not involved in the implementation cycle

  solutions:
  - Continuous Integration
  - Pull requests
  - Peer review
  - Pair programing

- works for official QAs:
Automated unit tests
Automated builds - as frequent as you can manage
Coverage measurement of tests
Peer code reviews of checkins
Accepted coding conventions and standards
Personal branches
Frequent merges
Eat your own dog food
Regular code reviews/buddy checks for new code before checking it in.
Running static analysis tools like lint.
Leaving the ego at the door.
Enforcing coding standards.
Checking in the test code used for developing the feature/fix. The test team uses this as PART of their regression tests

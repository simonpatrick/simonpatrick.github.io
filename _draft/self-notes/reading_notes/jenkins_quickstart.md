# Jenkins Quick Start

## Installation
- Install Jenkins
- Create a new user group for Jenkins

## Setting up
- Jenkins Home Directory: .jenkins folder in your home Directory
  Write up your initialization script like this :
  ```sh
  export JENKINS_BASE=/usr/local/jenkins
  export JENKINS_HOME=/var/jenkins-data
  java -jar ${JENKINS_BASE}/jenkins.war
```
- Running Jenkins as Standard Alone Application
- Running Jenkins Behind Apache Server
- Running Jenkins Behind Nginx
- Configuration Of Memory
```sh
export JAVA_OPTS=-Djava.awt.headless=true -Xmx512m -DJENKINS_HOME=/data/jenkins
export MAVEN_OPTS="-Xmx512m -XX:MaxPermSize=256m"
export ANT_OPTS="-Xmx512m -XX:MaxPermSize=256m"
```
- Running jenkins as Windows Service - JNLP file

## Jenkins Docker
## Jenkins Scalable

## Distribution Testing

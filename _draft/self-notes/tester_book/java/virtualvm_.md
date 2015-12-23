# VirtualVM 

## Remote connect to TOMCAT

Add following script into tomcat setenv.sh file

```shell
export JAVA_OPTS="-Dcom.sun.management.jmxremote=true \
                  -Dcom.sun.management.jmxremote.port=9090 \
                  -Dcom.sun.management.jmxremote.ssl=false \
                  -Dcom.sun.management.jmxremote.authenticate=false \
                  -Djava.rmi.server.hostname=10.8.205.72 \
                  -  -XX:+HeapDumpOnOutOfMemoryError
```

other commands:

```shell
export JAVA_OPTS="-XX:MaxPermSize=512m -Xms512m -Xmx1024m  -XX:+HeapDumpOnOutOfMemoryError"
export GRADLE_OPTS="-XX:MaxPermSize=512m"
export SONAR_RUNNER_OPTS="-Xmx512m -XX:MaxPermSize=512m"
echo alias docs="source /Users/patrick/workspace/works/python_virtualenvs/automation-docs/bin/activate \
&& cd /Users/patrick/workspace/works/python_virtualenvs/automation-docs/dooioo-automation-docs \
&& mkdocs serve" >>~/.zshrc

echo alias de-docs="cd /Users/patrick/workspace/works/python_virtualenvs/automation-docs/bin/ \
&& deactivate" >>~/.zshrc

```shell
jmap -dump:live,format=b,file=heapdump.hprof -F 8152
export JAVA_OPTS="-Dfile.encoding=UTF-8 -Xms128m -Xmx1024m -XX:PermSize=64m -XX:MaxPermSize=256m"
JAVA_OPTS="-Djava.awt.headless=true -Dfile.encoding=UTF-8 
-server -Xms1536m -Xmx1536m
-XX:NewSize=256m -XX:MaxNewSize=256m -XX:PermSize=256m 
-XX:MaxPermSize=256m -XX:+DisableExplicitGC"

jinfo -flag MaxPermSize 18435
scp filename XXX@XX.XX.XX.XX:~/path
```
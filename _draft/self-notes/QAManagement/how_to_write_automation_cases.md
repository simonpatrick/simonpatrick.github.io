# Design
- Page
- Data
- Flow
- Flow binding to data not page
- Page -> Template
- Data -> Database Model or Data Model

## Test Design
- Input
Hight Level : Different scenarios
- What to Input  -> Data Model
- Where to Input -> Page
- What the sequence of Input -> Flow
- Expectation -> CheckPoint


Perf_Common_Settings
GC log settings:

Edit in run.conf file:

timestamp=$( date +%Y-%m-%d_%H%M%S )
…
-XX:+PrintGCDetails -XX:+PrintGCDateStamps -Xloggc:/opt/jboss/server/default/log/gc-$timestamp.log
C3p0 common settings:

c3p0.acquireIncrement=5
c3p0.minPoolSize=15
c3p0.maxPoolSize=200
c3p0.maxStatementsPerConnection=100
c3p0.maxIdleTime=7200
c3p0.preferredTestQuery=select 1 from dual
c3p0.idleConnectionTestPeriod=30
c3p0.testConnectionOnCheckin=true
c3p0.unreturnedConnectionTimeout=60
c3p0.checkoutTimeout=60000
G1 GC Collector Settings(JDK7_55):

-XX:+UseG1GC
-Xms6144m
-Xmx6144m
-XX:MaxPermSize=256m
-XX:InitiatingHeapOccupancyPercent=55
-XX:MaxGCPauseMillis=200
-XX:+ParallelRefProcEnabled

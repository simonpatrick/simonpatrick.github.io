# Software Change management 
## Problems
1. changes
2. system upgrade
3. refactoring
4. user growth
5. performance issues
## Performance
measurement driver -- data : how to get the data??
## Goals and Objects
1. reduce risk
2. reliability
3. maintainability
4. impact
## Example 
### UAT enviroment is different with PROD
1. REFRESH DATA
2. SWITCH between prod and UAT
### understand system
1. compoment diagrams
2. sequence diagrams
3. data flow diagrams
4. good naming for DSL
5. collecting, analyse data
6. real science is repeatable
### commons in performance
1. thread profile for waiting threads
2. database query slowness
3. network latency
4. soap or restful api slowness
5. poor througthput for RMI Service
6. Authentication/Authorization system overwhelmed

solution maybe like 
1. add more database server -- but how to sync with all different databases
2. caching things
3. batching update

os level common issues:
1. disk read
2. disk write
3. context switch

solution:
1. SSD
2. in-memory cache
3. batch writh
4. locking strategies
5. moving contending processes (?? what's this)

JVM level:
1. collect GC logs
2. MXBeans

```
-Xloggc:<pathtofile>!
Path to the log output, make sure you've got disk space!!
!
-XX:+PrintGCDetails! Minimum information for tools to help! Replace -verbose:gc with this!
!
-XX:+PrintTenuringDistribution! Premature promotion information
!
-XX:+PrintGCTimestamps! Capture the timestamp of GC events
```

3. tools
```
• HP JMeter (Google it)
– Free, reasonably solid, but no longer supported / enhanced !
• GCViewer (http://www.tagtraum.com/gcviewer.html)
– Free, OSS, but ugly & somewhat limited
!
• GarbageCat (http://code.google.com/a/eclipselabs.org/p/garbagecat/) – Best name, but not very active project
!
• IBM GCMV (http://www.ibm.com/developerworks/java/jdk/tools/gcmv/) – Only choice for IBM J9 support
!
• jClarity Censum (http://www.jclarity.com/products/censum)
– Best in class
```
4. application code profile
virtual vm/hprof/jprofiler

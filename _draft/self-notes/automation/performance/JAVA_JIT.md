# JAVA Performance

## Profiling Tools
- YourKit
- Flight Recorder
- JMH

## Points
- Algorithmic Complexity
- Allocation/GC overhead
- Latency/blocking in IO and System Call

## Inside
- Source .java file
- ByteCode binary version of the program that JVM loads and execute
- Native code: CPU can execute directly
- Heap: JVM- controlled area of memory where java objects live
- JIT: Just In Time that turns one program form into a lower program form
- AOT: compilation that occurs before runtime
- Inlining: inserting the code of a called method into the caller,avoiding overhead of the call and optimizing the two together
- Optimization: doing the least amount of work needed
- 

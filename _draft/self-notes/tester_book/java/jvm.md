# JAVA JVM 
## Tunning
- Memory tuning
- CPU usage tuning
- Lock contention tuning
- I/O tuning

## Latency
Latency contributors:

- biggest one is GC
- in-process locking, thread-scheduling
- I/O
- application algorithmic ineffeciencies

## Memory Tuning
- Memory footprint tuning
- Allocation rate tuning
- Garbage collection tuning

### Memory footprint tuning
Out of memory sample:
- maybe you just too much data
	* Run with -verbosegc
	* Bigger JVM memory
	* All data in JVM? how about LRU cache
- maybe your data represenstation is fat
- memory leak



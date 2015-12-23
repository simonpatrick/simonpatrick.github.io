# Java Threads
## Threads
* Thread sample

```java
public class SimpleThreadExtend extends Thread{
    @Override
    public void run() {
        for (int i = 0; i <5 ; i++) {
            System.out.println(Thread.currentThread().getName()+":"+this.getClass().getName());
        }
    }

    public static void main(String[] args) {
        SimpleThreadExtend e = new SimpleThreadExtend();
        SimpleThreadExtend e1 = new SimpleThreadExtend();
        SimpleThreadExtend e2 = new SimpleThreadExtend();
        e.start();
        e1.start();
        e2.start();
    }
}
```

* Runnable sample
```java
    
```

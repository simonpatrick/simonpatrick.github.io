
```
A production quality program should use one of the many logging alternatives (e.g. log4j, logback, java.util.logging) to report errors and other diagnostics. This has a number of advantages:

Log messages go to a configurable location.
The end user doesn't see the messages unless you configure the logging so that he/she does.
You can use different loggers and logging levels, etc to control how much little or much logging is recorded.
You can use different appender formats to control what the logging looks like.
You can easily plug the logging output into a larger monitoring / logging framework.
All of the above can be done without changing your code; i.e. by editing the deployed application's logging config file.
By contrast, if you just use printStackTrace, the deployer / end user has little if any control, and logging messages are liable to either be lost or shown to the end user in inappropriate circumstances. (And nothing terrifies a timid user more than a random stack trace.)
```


However, I'm struggling to find anywhere which gives a valid reason why since surely the stack trace is very useful in tracking down what caused the exception. Things that I am aware of:

1) A stack trace should never be visibile to end users (for user experience and security purposes)

2) Generating a stack trace is a relatively expensive process (though unlikely to be an issue in most 'exception'al circumstances)

3) Many logging frameworks will print the stack trace for you (ours does not and no, we can't change it easily)

4) Printing the stack trace does not constitute error handling. It should be combined with other information logging and exception handling.

What other reasons are there for avoiding printing a stack trace in your code?

Throwable.printStackTrace() writes the stack trace to System.err PrintStream. The System.err stream and the underlying standard "error" output stream of the JVM process can be redirected by

invoking System.setErr() which changes the destination pointed to by System.err.
or by redirecting the process' error output stream. The error output stream may be redirected to a file/device
whose contents may be ignored by personnel,
the file/device may not be capable of log rotation, inferring that a process restart is required to close the open file/device handle, before archiving the existing contents of the file/device.
or the file/device actually discards all data written to it, as is the case of /dev/null.
Inferring from the above, invoking Throwable.printStackTrace() constitutes valid (not good/great) exception handling behavior, only

if you do not have System.err being reassigned throughout the duration of the application's lifetime,
and if you do not require log rotation while the application is running,
and if accepted/designed logging practice of the application is to write to System.err (and the JVM's standard error output stream).
In most cases, the above conditions are not satisfied. One may not be aware of other code running in the JVM, and one cannot predict the size of the log file or the runtime duration of the process, and a well designed logging practice would revolve around writing "machine-parseable" log files (a preferable but optional feature in a logger) in a known destination, to aid in support.

Finally, one ought to remember that the output of Throwable.printStackTrace() would definitely get interleaved with other content written to System.err (and possibly even System.out if both are redirected to the same file/device). This is an annoyance (for single-threaded apps) that one must deal with, for the data around exceptions is not easily parseable in such an event. Worse, it is highly likely that a multi-threaded application will produce very confusing logs as Throwable.printStackTrace() is not thread-safe.

There is no synchronization mechanism to synchronize the writing of the stack trace to System.err when multiple threads invoke Throwable.printStackTrace() at the same time. Resolving this actually requires your code to synchronize on the monitor associated with System.err (and also System.out, if the destination file/device is the same), and that is rather heavy price to pay for log file sanity. To take an example, the ConsoleHandler and StreamHandler classes are responsible for appending log records to console, in the logging facility provided by java.util.logging; the actual operation of publishing log records is synchronized - every thread that attempts to publish a log record must also acquire the lock on the monitor associated with the StreamHandler instance. If you wish to have the same guarantee of having non-interleaved log records using System.out/System.err, you must ensure the same - the messages are published to these streams in a serializable manner.

Considering all of the above, and the very restricted scenarios in which Throwable.printStackTrace() is actually useful, it often turns out that invoking it is a bad practice.

Extending the argument in the one of the previous paragraphs, it is also a poor choice to use Throwable.printStackTrace in conjunction with a logger that writes to the console. This is in part, due to the reason that the logger would synchronize on a different monitor, while your application would (possibly, if you don't want interleaved log records) synchronize on a different monitor. The argument also holds good when you use two different loggers that write to the same destination, in your application.

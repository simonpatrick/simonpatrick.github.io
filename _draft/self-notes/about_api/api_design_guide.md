# API Design

## A Good API

- Easy to learn
- Usable,even without a documentation
- Hard to misuse
- Powerful and easy to extend
- Easier to use than to re-implement equal functionality
- Consistent
- Abstract interface that does not limit performance and scaling


## Bad example
- Windows API
- Java's IO System
- POSIX and the C standard library
- Parts of the Python Standard library

problems:
- Ugly ;)
- Put size of struct into struct
- No defaults at all
- Huge Security problems
- Platform specific

Examples:
```Java
import java.io.*;
public class ReadFile {
  public static String readFile(String filename)
      throws IOException {
    InputStreamReader r;
    int read;
    try {
      r = new InputStreamReader(
        new FileInputStream(filename), "UTF-8");
    }
    catch (UnsupportedEncodingException uee) {}
    try {
      StringBuffer buf = new StringBuffer();
      char tmp[] = new char[1024];
      while ((read = r.read(buf, 0, 1024)) > 0)
        buf.append(tmp, 0, read);
    }
    finally {
      r.close();
}
    return buf.toString();
  }
}
```

Expected API:
```java
import java.io.*;
public class ReadFile {
  public static String readFile(String filename)
      throws IOException {
    return new File(filename).getStringContents("UTF-8");
} }
```

## API Design Basic Principles
- start building applications with the api
- think in terms of apis
- Even if you will always be the only programer on that thing
  - because you should never assume you will be [success,handing over maintenance etc.]

## Implementation VS interface
* Interface must be independent of Implementation
* Don't let implementation details leak into the API(expections,error codes,etc.)

## Performance And Scaling
- Bad decisions limit performance
  * make things immutable or document them be immutable
  * account for concurrency that are not threads or processes
  * be reentrant

## Be Consistent and Nice
- Consistent naming
- Follow naming rules of Platform
  * PEP8
  * if you develop library for some libs, follow their naming rules
  * don't go down the DSL road

## Library VS Framework
- A library provides functions,methods, and classes to accomplish things
- A framework might throw meta magic on top of that


## Class Design - Design for subclassing
- Build your class so that a subclass might improve/change certain behavior
- Provide ways to hook into specific parts of the execution
- if class is not designed for subclassing,document it as such

## defaults/Common Use Cases
- Think of the most common use cases, you will have them if you use your API
- Make Sure the API Provides easy way to do that
- If you see that your code does things the API should be doing instead, move that
  specific code over

## POLS
- An API should not surprise the user(POLS)
- DO introduce side effects into methods that hind not having side effects
  * getter,properties should never have side effects
  * Metaclasses allow breaking users expectations on so many levels

## Consistent parameters
- Ordering of parameters is import
- What you're operating on should always be the first parameter
- Similar methods should have same Ordering of parameters and types
- If the order is the warong way round,stick with it! Consistency more important

## Data structures not Strings
- If users have to parse return values of APIs you are doing something wrong.
  Data structures not Strings
- If an implementation detail becomes an interface it prevents future improvements.

## Other Practical Advice
- Do away with the global state

Global State in Python:
- Module globals -> global state
- sys.modules -> global state
- any kind of singleton -> global state

Don’t do this:
```Python
import mylib
@mylib.register('something')
def callback_for_something(args):
    do_something
mylib.start_execution()

```

Do this instead:

```python
import mylib
worker = mylib.Worker()
@worker.register('something')
def callback_for_something(args):
    do_something
worker.start_execution()

```

## Things to learn from Java
- Classes are a good invention
- Create as many objects as necessary
- simplifies tests a lot where exceptions are expected
  * no cleanup necessary, GC/refcounting does that for us
  * run with more than one configuration, just create one more instance.

## Bad Examples

- Django’s global settings module
- Celery used to have this as well, it changed recently for precisely this reason.
- csv / logging / sys.modules in the standard library

## Conclusion- API Design
- Proper API design is what makes people use your library
- An API that is easy to understand lowers the entry barrier for a new programmer
- API design is tough
- Even large companies got it wrong

- String.indexOf(char) is faster than String.indexOf(String).
```java
int pos = header[i].indexOf(".");
int pos = header[i].indexOf('.');
```
- avoid throw raw type exception
```java
     if(checkPointClasses==null||!checkPointClasses.startsWith("com")) throw  new RuntimeException(checkPointClasses+"检查点输入错误，请校验");
```

- Avoid using implementation types like 'TreeMap'; use the interface instead
- New exception is thrown in catch block, original stack trace may be lost
- A method/constructor shouldnt explicitly throw java.lang.Exception
- The field name indicates a constant but its modifiers do not
- Exceptional return value of java.io.File.mkdir() ignored
```java
 if(d.mkdir()) return d;
``` 
- setValue(int) unconditionally sets the field value 
```java
 public enum Node{
        Manager(1000),Finance(15000),
        Admin(2500),Purchase(3000),Assistance(4000),AdminFinal(4100),FinanceFinal(5000);

        private int value;

        Node(int value) {
            this.value = value;
        }

        public int getValue() {
            return value;
        }

        public void setValue(int value) {
            this.value = value;
        }
    }
```

- compareTo,need to rewrite equals and hashCode
- static inner class
- expose internal representation by incorporation reference ot mutable object
- java international issue
```java
 //out = new FileWriter(file);
            out = new BufferedWriter(new OutputStreamWriter(
                    new FileOutputStream(file), "UTF-8"));
```

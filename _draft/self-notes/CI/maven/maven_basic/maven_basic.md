# MAVEN BASIC
## MAVEN Life Cycle
## MAVEN plugin
### Apache Maven Source Plugin
- [home link](http://maven.apache.org/plugins/maven-source-plugin/)
- [plugin documentation](http://maven.apache.org/plugins/maven-source-plugin/plugin-info.html)

- 创建源码的jar，jar放在target目录
- goal:
    * source:aggeragate
    * source:aggeragate-test-jar
    * source:jar
    * source:test-jar
    * source:jar-no-fork
    * source:test-jar-no-fork
- sample configuration

```java
<build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-source-plugin</artifactId>
                <version>2.4</version>
                <configuration>
                    <outputDirectory>/absolute/path/to/the/output/directory</outputDirectory>
                    <finalName>filename-of-generated-jar-file</finalName>
                    <attach>false</attach>
                </configuration>
            </plugin>
        </plugins>
    </build>
```

- maven命令

```bash
	mvn source:jar
	mvn source:test-jar	
```

- 生成source设置

```java
<project>
	  ...
	  <build>
	    <plugins>
	      <plugin>
	        <groupId>org.apache.maven.plugins</groupId>
	        <artifactId>maven-source-plugin</artifactId>
	        <version>2.4</version>
	        <executions>
	          <execution>
	            <id>attach-sources</id>
	            <phase>verify</phase>
	            <goals>
	              <goal>jar-no-fork</goal>
	            </goals>
	          </execution>
	        </executions>
	      </plugin>
	    </plugins>
	  </build>
	  ...
</project>
```

问题：请问一下配置在什么时候会调用？

- 安装source的profile

```java
<project>
  ...
  <profiles>
    <profile>
      <id>release</id>
      <build>
        <plugins>
          <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-source-plugin</artifactId>
            <version>2.4</version>
            <executions>
              <execution>
                <id>attach-sources</id>
                <goals>
                  <goal>jar-no-fork</goal>
                </goals>
              </execution>
            </executions>
          </plugin>
        </plugins>
      </build>
    </profile>
  </profiles>
  ...
</project>
```

###  MAVEN Compile Plugin 
- [home page](http://maven.apache.org/plugins/maven-compiler-plugin/index.html)
-  Goals
	* compiler:compile
	* compiler:testCompile

```xml
    <plugins>
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-compiler-plugin</artifactId>
                    <version>3.3</version>
                    <configuration>
                        <source>${compile.version}</source>
                        <target>${compile.version}</target>
                    </configuration>
                </plugin>
            </plugins>
```


### Maven Resource Plugin
- [home page](http://maven.apache.org/plugins/maven-resources-plugin/index.html)
- goals
	* resources:resources
	* resources:testResources
	* resources:copy-resources

### Maven Surefire plugin
- [home page](http://maven.apache.org/surefire/maven-surefire-plugin/)
- goals:
	* surefire:test



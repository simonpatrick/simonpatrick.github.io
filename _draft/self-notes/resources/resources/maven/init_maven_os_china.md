# MAVEN setting for OSCHINA
## Install MAVEN
- 下载MAVEN
- 配置M2_HOME
- M2_HOME加入到path中
- 测试是否安装成功
```sh
mvn -v
```

## setting.xml
maven安装目录下面有setting.xml文件，配置这个文件可以改变maven的一些设置

- mirrors
```
<mirrors>
    <!-- mirror | Specifies a repository mirror site to use instead of a given 
        repository. The repository that | this mirror serves has an ID that matches 
        the mirrorOf element of this mirror. IDs are used | for inheritance and direct 
        lookup purposes, and must be unique across the set of mirrors. | -->
    <mirror>
        <id>nexus-osc</id>
        <mirrorOf>central</mirrorOf>
        <name>Nexus osc</name>
        <url>http://maven.oschina.net/content/groups/public/</url>
    </mirror>
    <mirror>
        <id>nexus-osc-thirdparty</id>
        <mirrorOf>thirdparty</mirrorOf>
        <name>Nexus osc thirdparty</name>
        <url>http://maven.oschina.net/content/repositories/thirdparty/</url>
    </mirror>
</mirrors>
```

- profile and respository
- 
```
<profile>
            	<id>jdk-1.4</id>
            
            	<activation>
            		<jdk>1.4</jdk>
            	</activation>
            
            	<repositories>
            		<repository>
            			<id>nexus</id>
            			<name>local private nexus</name>
            			<url>http://maven.oschina.net/content/groups/public/</url>
            			<releases>
            				<enabled>true</enabled>
            			</releases>
            			<snapshots>
            				<enabled>false</enabled>
            			</snapshots>
            		</repository>
            	</repositories>
            	<pluginRepositories>
            		<pluginRepository>
            			<id>nexus</id>
            			<name>local private nexus</name>
            			<url>http://maven.oschina.net/content/groups/public/</url>
            			<releases>
            				<enabled>true</enabled>
            			</releases>
            			<snapshots>
            				<enabled>false</enabled>
            			</snapshots>
            		</pluginRepository>
            	</pluginRepositories>
            </profile>
```


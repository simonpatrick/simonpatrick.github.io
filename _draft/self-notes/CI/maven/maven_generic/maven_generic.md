# MAVEN Generic
## MAVEN Life Cycle
validate	验证	确保当前配置和POM的内容是有效的。这包含对pom文件树的验证。
initialize	初始化	在执行构建生命周期的主任务之前可以进行初始化。
generate-sources	生成源码	代码生成器可以开始生成在以后阶段中处理或编译的源代码。
process-sources	处理源码	提供解析、修改和转换源码。常规源码和生成的源码都可以在这里处理。
generate-resources	生成资源	可以生成非源码资源。通常包括元数据文件和配置文件。
process-resources	处理资源	处理非源码资源。修改、转换和重定位资源都能在这阶段发生。
compile	编译	编译源码。编译过的类被放到目标目录树中。
process-classes	处理类	处理类文件转换和增强步骤。字节码交织器和常用工具常在这一阶段操作。
generate-test-sources	生成测试源码	mojo可以生成要操作的单元测试代码。
process-test-sources	处理测试源码	在编译前对测试源码执行任何必要的处理。在这一阶段，可以修改、转换或复制源代码。
generate-test-resources生成测试资源	允许生成与测试相关的（非源码）资源。	
process-test-resources处理测试资源	可以处理、转换和重新定位与测试相关的资源。	
test-compile	测试编译	编译单元测试的源码。
test	测试	运行编译过的单元测试并累计结果。
package	打包	将可执行的二进制文件打包到一个分布式归档文件中，如
pre-integration-test	前集成测试、准备集成测试。这种情况下的集成测试是指在一个受到一定控制的模拟的真实部署环境中测试代码。这一步能将归档文件部署到一个服务器上执行。	
integration-test	集成测试	执行真正的集成测试。
post-integration-test	后集成测试、解除集成测试准备。这一步涉及测试环境重置或重新初始化。	
verify	检验	检验可部署归档的有效性和完整性。过了这个阶段，将安装该归档。
install	安装	将该归档添加到本地Maven目录。这一步让其他可能依赖该归档的模块可以使用它。
deploy	部署	将该归档添加到远程Maven目录。这一步让这个工件能为更多的人所用。

- Build plugins
- Reporting plugins

设置plugin version
设置plugin 到parent的plugin management(```<pluginManagement/>''')

## MAVEN Generic Configuration
### build
- configuration parameters
    * mapping parameters
    * mapping list
    * mapping map
- tags
    * execution
    * goal
    * inherited
    * dependency

### Reporting


# Android Basic
## Android 系统架构overview
1. Application Framework
    Activity Manage
    Content Provider
    View System
    Location Manager
    Package Manager
    Notification Manager
2. Libs
3. Android Runtime -> core libs/DVM(JVM)
4. Application

## Android 组件
### Activity
Activity-> A Web Page
#### Activity 启动
1. 注册到AndroidManifest
2. 找到main activity,然后调用onCreate
3. 为View设置监听器
4. 布局使用方法
	* 线性布局 linear layout
 	* 相对布局 relative layout
	* List View
	* Grid View	

#### Activity 和布局layout的关系
#### Activity 和layout的交互
### Service
Service -> processor
### Content Provider
content provider -> data provider
其他应用可以调用，运输数据，暴露数据给其他应用 -> interface
### Broadcast Receiver
broadcast receiver -> messaging system


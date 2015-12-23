# Understand Unix Process

## 进程基础
- 进程PID
- 进程状态
- 退出码
- POSIX
- PID : 表示进程的ID Process ID, 全局唯一的正整数
- PPID : 表示进程的父进程
- 进程名字,进程参数,进程状态，退出码
- 死锁/活锁
- Nohup

### 进程状态
- O: 进程正在处理器运行
- S: Sleeping
- R: runnable
- I：idle: 空闲状态
- Z: zombie： 僵尸状态
- T: Traced： 跟踪状态
- B: 进程中正在等待更多的内存页
- D: 不可中断的深度休眠

### 退出码

任何进程退出时，都有留下退出码 0-255，0 正常退出，其他为错误

### 进程资源

```shell
ls /proc/1/
cat /proc/1/status
```

# Docker Command List

## Docker - Version

```shell
docker version
```

## Docker - pull

install image
```shell
docker pull ubuntu:latest
```

## Docker-ps
list all docker images
```shell
docker ps
```

## Docker -rm

remove docker images 
```shell
docker remove <image_name>
```

## Docker -run
run the image

```shell
docker run <image_name> -i
docker run <image_name> <command>
# run as daemon process
docker run -d <image_name>
```

## Docker -ls

## Docker -build

## Docker commit

```shell
docker ps -l
docker commit <id> <image_name>
```
##Docker inspect
检查镜像

```shell
docker inspect <id>
```

## Docker push

```shell
docker push <image_name>
```

## Docker stop

```shell
docker stop
```
## Docker export/import

```shell
sudo docker export 7691a814370e > ubuntu.tar
$sudo docker import http://example.com/exampleimage.tgz example/imagerepo

```

boot2docker提供了一个简单的脚本来管理正在运行docker进程的虚拟主机。它还负责为操作系统镜像的安装工作。
如果你还没安装boot2docker请打开一个新的终端窗口
运行下边的命令来获得boot2docker:
```shell
    brew install boot2docker
```
##### 启动docker

1. 初始化docker 命令
```shell
    boot2docker init
```
2. 如果docker已经初始化则显示如下：
```shell
    Ξ ~ → boot2docker init
    2014/11/08 12:37:06 Virtual machine boot2docker-vm already exists
```
3. 同时可以通过以下命令查看boot2docker的帮助

```shell
    boot2docker help
    boot2docker management utility.

Commands:
    init                    Create a new boot2docker VM.
    up|start|boot           Start VM from any states.
    ssh [ssh-command]       Login to VM via SSH.
    save|suspend            Suspend VM and save state to disk.
    down|stop|halt          Gracefully shutdown the VM.
    restart                 Gracefully reboot the VM.
    poweroff                Forcefully power off the VM (might corrupt disk image).
    reset                   Forcefully power cycle the VM (might corrupt disk image).
    delete|destroy          Delete boot2docker VM and its disk image.
    config|cfg              Show selected profile file settings.
    info                    Display detailed information of VM.
    ip                      Display the IP address of the VM's Host-only network.
    status                  Display current state of VM.
    download                Download boot2docker ISO image.
    upgrade                 Upgrade the boot2docker ISO image (if vm is running it will be stopped and started).
    version                 Display version information.

Options:
      --basevmdk="": Path to VMDK to use as base for persistent partition
      --dhcp=true: enable VirtualBox host-only network DHCP.
      --dhcpip=192.168.59.99: VirtualBox host-only network DHCP server address.
  -s, --disksize=20000: boot2docker disk image size (in MB).
      --dockerport=2375: host Docker port (forward to port 2375 in VM).
      --hostip=192.168.59.3: VirtualBox host-only network IP address.
      --iso="/Users/patrick/.boot2docker/boot2docker.iso": path to boot2docker ISO image.
      --lowerip=192.168.59.103: VirtualBox host-only network DHCP lower bound.
  -m, --memory=2048: virtual machine memory size (in MB).
      --netmask=ffffff00: VirtualBox host-only network mask.
      --serial=false: try serial console to get IP address (experimental)
      --serialfile="": path to the serial socket/pipe.
      --ssh="ssh": path to SSH client utility.
      --ssh-keygen="ssh-keygen": path to ssh-keygen utility.
      --sshkey="/Users/patrick/.ssh/id_boot2docker": path to SSH key to use.
      --sshport=2022: host SSH port (forward to port 22 in VM).
      --upperip=192.168.59.254: VirtualBox host-only network DHCP upper bound.
      --vbm="VBoxManage": path to VirtualBox management utility.
  -v, --verbose=false: display verbose command invocations.
      --vm="boot2docker-vm": virtual machine name.
```

4. 查看docker version

```shell
    Ξ ~ → docker version
    Client version: 1.1.2
    Client API version: 1.13
    Go version (client): go1.3
    Git commit (client): d84a070
    Server version: 1.2.0
    Server API version: 1.14
    Go version (server): go1.3.1
    Git commit (server): fa7b24f
```

5. 用SSH来连接虚拟主机
如果你感觉需要连接虚拟主机，你可以简单的运行下边的命令：
```
    boot2docker ssh
    # 如果ssh key is generated，可以直接连接docker
    # User: docker
    # Pwd:  tcuser
```



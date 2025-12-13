---
date:
  created: 2025-12-11
categories:
  - Platform
---

# Ubuntu

<!-- more -->

## 基础知识

### ubuntu 常用命令

~~~bash
# 新建终端
Ctrl + Alt + T

# 重启
reboot

# 关机
poweroff

# 查看架构
uname -m
~~~

### 新增10G的swap

~~~bash
dd if=/dev/zero of=swapfile bs=1M count=10240

# mkswap创建交换文件:
mkswap swapfile

# swapon激活
swapon swapfile
~~~


#### 挂载共享目录

~~~bash
编辑虚拟机设置
虚拟机设置
    硬件
       USB 控制器   连接 USB 兼容性(C): USB 3.1
    选项
       共享文件夹 
            文件夹共享 总是启用
            
            文件夹 添加
                主机路径(H)
                D:\data\share
                
                名称(A)
                share
                
# 虚拟机访问 /mnt/hgfs/share    

apt install open-vm-tools open-vm-tools-desktop -y

mkdir -p /mnt/hgfs

reboot

ls /mnt/hgfs

# 手动挂载
# vmhgfs-fuse .host:/ /mnt/hgfs -o allow_other

# 开机自动挂载
vim /etc/fstab
################################################################################
.host:/ /mnt/hgfs fuse.vmhgfs-fuse defaults,allow_other 0 0
################################################################################
mount -a

mkdir ~/Desktop/data
rsync --progress /mnt/hgfs/share/* ~/Desktop/data

tar -zxvf google_devices-marlin-opr1.170623.032-01ff7129.tgz
tar -zxvf qcom-marlin-opr1.170623.032-62f4dec7.tgz

mv extract-google_devices-marlin.sh /root/Desktop/WORKING_DIRECTORY
mv extract-qcom-marlin.sh /root/Desktop/WORKING_DIRECTORY

cd /root/Desktop/WORKING_DIRECTORY

./extract-google_devices-marlin.sh
I ACCEPT

./extract-qcom-marlin.sh
I ACCEPT
~~~

~~~bash

repo sync -j16 --fail-fast
================================================================================
Repo command failed due to the following `SyncFailFastError` errors:
GitCommandError: 'fetch --quiet --progress aosp --prune --recurse-submodules=no --tags +refs/heads/*:refs/remotes/aosp/* +refs/tags/android-8.0.0_r28:refs/tags/android-8.0.0_r28 +refs/tags/*:refs/tags/*' on platform/external/webrtc failed
stdout: remote: Enumerating objects: 516222, done.   

repo sync platform/external/webrtc

repo sync -j16 --fail-fast
================================================================================
Repo command failed due to the following `SyncFailFastError` errors:
GitCommandError: 'fetch --quiet --progress aosp --prune --recurse-submodules=no --tags +refs/heads/*:refs/remotes/aosp/* +refs/tags/android-8.0.0_r28:refs/tags/android-8.0.0_r28 +refs/tags/*:refs/tags/*' on platform/packages/apps/Phone failed
stdout: fatal: unable to access 'https://mirrors.tuna.tsinghua.edu.cn/git/AOSP/platform/packages/apps/Phone/': Could not resolve host: mirrors.tuna.tsinghua.edu.cn

repo sync platform/packages/apps/Phone

# repo sync -j16
Syncing: 100% (568/568), done in 1m48.690s
Syncing: 100% (568/568) 1:48 | ..working..repo sync has finished successfully.

du -sh --exclude='.repo' --exclude='out' ~/Desktop/WORKING_DIRECTORY

tar -cvzf /media/root/udisk/android-8.0.0_r28.tar.gz \
    --exclude='~/Desktop/WORKING_DIRECTORY/out' \
    --exclude='~/Desktop/WORKING_DIRECTORY/.repo' \
    -C ~/Desktop WORKING_DIRECTORY
    
umount /media/root/udisk
lsblk
mkfs.ext4 /dev/sdb1

mkdir -p /mnt/udisk
mount /dev/sdb1 /mnt/udisk
df -h
~~~

~~~
apt update
apt install openssh-server -y
#systemctl enable ssh
#systemctl start ssh
#systemctl status ssh # 检查 SSH 是否运行

ip addr show
~~~

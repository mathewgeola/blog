---
date:
  created: 2025-12-09
categories:
  - 安卓源码编译刷机
---

# Pixel

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

## 环境配置

### ubuntu 下载

~~~
https://releases.ubuntu.com/

https://releases.ubuntu.com/18.04/
~~~

### VMware Workstation 配置

~~~
ubuntu-18.04.6-desktop-amd64
ubuntu
ubuntu
ubuntu

Pixel
D:\Virtual Machines\AOSP\Pixel

2
4

16

使用桥接网络(R)

400

Pixel.vmdk
~~~

### ubuntu 配置

#### 修改 root 密码

~~~bash
ubuntu

sudo passwd root
ubuntu
root
root

whoami

su
root
whoami
~~~

#### 修改时区

~~~bash
dpkg-reconfigure tzdata

# Asia => Shanghai
~~~

#### 修改息屏时间

~~~
Settings => Power => Power Saving => Blank screen [Never]
~~~

#### 修改 history length

~~~bash
apt install vim -y

vim .bashrc
################################################################################
# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000000
HISTFILESIZE=2000000
################################################################################

reboot
~~~

#### git 配置

~~~bash
apt install git -y

git config --global user.name "mathewgeola"
git config --global user.email "mathewgeola@gmail.com"
~~~

#### 编译

~~~bash
apt install curl -y

mkdir ~/bin
PATH=~/bin:$PATH
curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
chmod a+x ~/bin/repo

cd /home/ubuntu/Desktop
mkdir WORKING_DIRECTORY
cd WORKING_DIRECTORY

repo init -u https://mirrors.tuna.tsinghua.edu.cn/git/AOSP/platform/manifest -b android-8.0.0_r28 --repo-url=https://mirrors.tuna.tsinghua.edu.cn/git/git-repo
repo sync -j16
~~~
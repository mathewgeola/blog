---
date:
  created: 2025-12-12
  updated: 2025-12-12
categories:
  - AOSP
authors:
  - mathewgeola
#pin: true
#readtime: 15
links:
  - 博客首页: blog/index.md
  - 外部链接:
      - github: https://github.com/
tags:
  - aosp
  - android
  - pixel
slug: aosp
---

# AOSP 源码编译 android-8.0.0_r28 并刷入 Pixel

<!-- more -->

### ubuntu 下载

~~~
https://releases.ubuntu.com/

https://releases.ubuntu.com/20.04/SHA256SUMS
https://releases.ubuntu.com/20.04/ubuntu-20.04.6-desktop-amd64.iso.torrent
https://releases.ubuntu.com/20.04/ubuntu-20.04.6-desktop-amd64.iso

510ce77afcb9537f198bc7daa0e5b503b6e67aaed68146943c231baeaab94df1 *ubuntu-20.04.6-desktop-amd64.iso

>certutil -hashfile ubuntu-20.04.6-desktop-amd64.iso SHA256
SHA256 的 ubuntu-20.04.6-desktop-amd64.iso 哈希:
510ce77afcb9537f198bc7daa0e5b503b6e67aaed68146943c231baeaab94df1
CertUtil: -hashfile 命令成功完成。
~~~

### 资源下载

~~~
Source code tags and builds
https://source.android.com/docs/setup/reference/build-numbers#source-code-tags-and-builds

Build ID            Tag	                Version	    Supported devices	        Security patch level
OPR1.170623.032	    android-8.0.0_r28	Oreo	    Pixel XL, Pixel, Pixel C	2017-11-05

-----------------------------------------------------------------------------------------------------------------------
Pixel binaries for Android 8.0.0 (OPR1.170623.032)
https://developers.google.com/android/drivers#sailfishopr1.170623.032

Hardware Component	                                            Company	            Download	                                                                                                SHA-256 Checksum
Vendor image	                                                Google	            Link [https://dl.google.com/dl/android/aosp/google_devices-sailfish-opr1.170623.032-edb989ad.tgz]	        529eb245e041b9f480a143186fa9a32a916be37fefb4099a4eb8f21359e6f0b5
GPS, Audio, Camera, Gestures, Graphics, DRM, Video, Sensors	    Qualcomm	        Link [https://dl.google.com/dl/android/aosp/qcom-sailfish-opr1.170623.032-00212902.tgz]	                    870b4a3defdfab2fb1be012f52b98bc632192865a6f1f04d9d06b06f01452ebb

>certutil -hashfile google_devices-sailfish-opr1.170623.032-edb989ad.tgz SHA256
SHA256 的 google_devices-sailfish-opr1.170623.032-edb989ad.tgz 哈希:
529eb245e041b9f480a143186fa9a32a916be37fefb4099a4eb8f21359e6f0b5
CertUtil: -hashfile 命令成功完成。

>certutil -hashfile qcom-sailfish-opr1.170623.032-00212902.tgz SHA256
SHA256 的 qcom-sailfish-opr1.170623.032-00212902.tgz 哈希:
870b4a3defdfab2fb1be012f52b98bc632192865a6f1f04d9d06b06f01452ebb
CertUtil: -hashfile 命令成功完成。

-----------------------------------------------------------------------------------------------------------------------
"sailfish" for Pixel
https://developers.google.com/android/images#sailfish

Version	                                            Download	                                                                                        SHA-256 Checksum
8.0.0 (OPR1.170623.032, Nov 2017, Fi/Canada)	    Link [https://dl.google.com/dl/android/aosp/sailfish-opr1.170623.032-factory-e011ef43.zip]	        e011ef434ae32e24f14c19d83a859ed76a156209ba4552c393af38f5b1f3efd6

-----------------------------------------------------------------------------------------------------------------------

>certutil -hashfile sailfish-opr1.170623.032-factory-e011ef43.zip SHA256
SHA256 的 sailfish-opr1.170623.032-factory-e011ef43.zip 哈希:
e011ef434ae32e24f14c19d83a859ed76a156209ba4552c393af38f5b1f3efd6
CertUtil: -hashfile 命令成功完成。
~~~

### VMware Workstation 配置

~~~
创建新的虚拟机

自定义(高级)(C)

安装程序光盘映像文件(iso)(M):
D:\data\ubuntu\20.04.6\ubuntu-20.04.6-desktop-amd64.iso

个性化 Linux
    全名(F): ubuntu-20.04.6-desktop-amd64
用户名(U): ubuntu
密码(P): ubuntu
确认(C): ubuntu

虚拟机名称(V):
AOSP Pixel

位置(L):
D:\Virtual Machines\AOSP Pixel

处理器
处理器数里(P): 4
每个处理器的内核数里(C): 4

此虚拟机的内存(M): 16384 MB

网络连接
使用桥接网络(R)

最大磁盘大小(GB)(S): 400            
~~~

### ubuntu 配置

#### ubuntu root 密码修改

~~~bash
sudo passwd root
ubuntu
root
root

whoami

su
root
whoami
~~~

#### ubuntu root 登录

~~~bash
# 注释掉 GDM 的 root 限制
gedit /etc/pam.d/gdm-password
################################################################################
#auth	required	pam_succeed_if.so user != root quiet_success
################################################################################

# 修复 root 图形界面闪退的问题
gedit /root/.profile
################################################################################
#mesg n 2> /dev/null || true
tty -s && mesg n 2> /dev/null || true
################################################################################

Power Off / Log Out => 
  Log Out

Not listed?
root
root
~~~

#### ubuntu 设置配置

~~~
Settings => Appearance => Dock
    icon size [16]
    Position on screen [Bottom]

# 修改息屏时间
Settings =>  Power => Power Saving => 
    Blank screen [Never]
~~~

#### ubuntu 时区修改

~~~bash
dpkg-reconfigure tzdata

# Asia => Shanghai
~~~

#### ubuntu 修改 history length

~~~bash
gedit .bashrc
################################################################################
# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000000
HISTFILESIZE=2000000
################################################################################
~~~

#### ubuntu 换源配置

~~~bash
gedit /etc/apt/sources.list
################################################################################
deb http://mirrors.aliyun.com/ubuntu/ focal main restricted
deb http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted
deb http://mirrors.aliyun.com/ubuntu/ focal universe
deb http://mirrors.aliyun.com/ubuntu/ focal-updates universe
deb http://mirrors.aliyun.com/ubuntu/ focal multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-updates multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-security main restricted
deb http://mirrors.aliyun.com/ubuntu/ focal-security universe
deb http://mirrors.aliyun.com/ubuntu/ focal-security multiverse
################################################################################

apt update
~~~

#### ubuntu 常用工具安装

~~~bash
apt install git vim net-tools curl wget htop jnettop p7zip-full -y
~~~

#### proxychains4 配置

###### 主机配置

~~~
# 终端管理员
netsh advfirewall set allprofiles state off
netsh advfirewall set allprofiles state on

ipconfig
192.168.1.3
~~~

###### 虚拟机配置配置

~~~bash
apt install proxychains4 -y

vim /etc/proxychains4.conf
################################################################################
[ProxyList]
# add proxy here ...
# meanwile
# defaults set to "tor"
#socks4 	127.0.0.1 9050
socks5 192.168.1.3 7897
################################################################################

proxychains curl https://www.google.com
proxychains4 curl ipinfo.io
~~~

#### ubuntu java 配置

~~~bash
apt install openjdk-8-jdk -y

gedit /etc/java-8-openjdk/security/java.security
################################################################################
#
# Example:
#   jdk.tls.disabledAlgorithms=MD5, SSLv3, DSA, RSA keySize < 2048
#jdk.tls.disabledAlgorithms=SSLv3, TLSv1, TLSv1.1, RC4, DES, MD5withRSA, \
#    DH keySize < 1024, EC keySize < 224, 3DES_EDE_CBC, anon, NULL, \
#    ECDH, \
#    include jdk.disabled.namedCurves

jdk.tls.disabledAlgorithms=SSLv3, RC4, DES, MD5withRSA, \
    DH keySize < 1024, EC keySize < 224, 3DES_EDE_CBC, anon, NULL, \
    include jdk.disabled.namedCurves

################################################################################
~~~

#### ubuntu pyenv 配置

~~~bash
proxychains4 bash <(proxychains4 curl -fsSL https://pyenv.run)

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> /root/.bashrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> /root/.bashrc
echo 'eval "$(pyenv init - bash)"' >> /root/.bashrc

source /root/.bashrc

mkdir /root/.pyenv/cache/
cd /root/.pyenv/cache/
      
proxychains4 wget https://www.python.org/ftp/python/3.6.15/Python-3.6.15.tar.xz
apt install -y \
    make build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libffi-dev \
    liblzma-dev \
    python3-openssl \
    ca-certificates \
    git \
    wget \
    curl \
    llvm
pyenv install 3.6.15
pyenv versions
pyenv local 3.6.15

cd /root/.pyenv/cache/
proxychains4 wget https://www.python.org/ftp/python/2.7.17/Python-2.7.17.tar.xz
apt install -y \
    build-essential \
    make \
    gcc \
    g++ \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libffi-dev \
    liblzma-dev \
    uuid-dev \
    libgdbm-dev \
    libdb-dev \
    libexpat1-dev \
    libmpdec-dev \
    libffi-dev \
    wget \
    curl \
    git \
    ca-certificates
pyenv install 2.7.17
pyenv versions
pyenv local 2.7.17

# 下载源码时使用
ln -s /root/.pyenv/versions/3.6.15/bin/python /usr/bin/python

# 编译源码时使用
ln -s /root/.pyenv/versions/2.7.17/bin/python /usr/bin/python
~~~

#### ubuntu 中新增 10G 的 swap [可选]

~~~bash
swapoff /swapfile
dd if=/dev/zero of=/swapfile bs=1G count=10 status=progress
chmod 600 /swapfile
mkswap /swapfile
swapon /swapfile

swapoff -a
swapon -a

swapon --show
free -h

cat /proc/sys/vm/swappiness

echo "vm.swappiness=10" | tee /etc/sysctl.conf
sysctl -p

cat /proc/sys/vm/swappiness
~~~

### 下载源码

~~~bash
ln -s /root/.pyenv/versions/3.6.15/bin/python /usr/bin/python

apt install git -y

git config --global user.name "mathewgeola"
git config --global user.email "mathewgeola@gmail.com"

curl https://storage.googleapis.com/git-repo-downloads/repo > /bin/repo
chmod a+x /bin/repo

mkdir /root/Desktop/AOSP
cd /root/Desktop/AOSP

repo init -u https://mirrors.tuna.tsinghua.edu.cn/git/AOSP/platform/manifest -b android-8.0.0_r28 --repo-url=https://mirrors.tuna.tsinghua.edu.cn/git/git-repo

repo sync
repo sync -j16
Syncing: 100% (568/568), done in 30m23.265s
Checking for bloat: 100% (48/48), done in 58.724s
repo sync has finished successfully.
~~~

### 驱动加载

~~~bash
cd /root/Desktop/data

tar -zxvf google_devices-sailfish-opr1.170623.032-edb989ad.tgz
tar -zxvf qcom-sailfish-opr1.170623.032-00212902.tgz

mv extract-google_devices-sailfish.sh /root/Desktop/AOSP
mv extract-qcom-sailfish.sh /root/Desktop/AOSP

cd /root/Desktop/AOSP

./extract-google_devices-sailfish.sh
I ACCEPT

./extract-qcom-sailfish.sh
I ACCEPT
~~~

### 编译源码

~~~bash
rm -rf /usr/bin/python
ln -s /root/.pyenv/versions/2.7.17/bin/python /usr/bin/python

# 安装依赖
apt install git-core gnupg flex bison build-essential zip curl zlib1g-dev gcc-multilib g++-multilib libc6-dev-i386 libncurses5 lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z1-dev libgl1-mesa-dev libxml2-utils xsltproc unzip fontconfig

export OUT_DIR=out

source build/envsetup.sh

lunch aosp_sailfish-userdebug

export LC_ALL=C
make -j16

#### make completed successfully (06:53:27 (hh:mm:ss)) ####
~~~

### 刷机

~~~bash
cd /root/Desktop/AOSP/out/target/product/sailfish

tar -czvf sailfish.tar.gz \
  boot.img \
  system.img \
  vendor.img \
  userdata.img
  
nautilus .

sailfish.tar.gz 拷贝到主机

解压 sailfish-opr1.170623.032-factory-e011ef43.zip

cd sailfish-opr1.170623.032-factory-e011ef43\sailfish-opr1.170623.032

解压 image-sailfish-opr1.170623.032.zip

解压 sailfish.tar.gz 里面的 {boot,system,vendor,userdata}.img 替换 sailfish-opr1.170623.032-factory-e011ef43\sailfish-opr1.170623.032\image-sailfish-opr1.170623.032 里的文件

重新压缩 image-sailfish-opr1.170623.032.zip

adb reboot bootloader
fastboot devices
.\flash-all.bat
fastboot reboot
~~~
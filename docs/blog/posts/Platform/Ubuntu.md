---
date:
  created: 2025-12-11
categories:
  - Ubuntu
---

# Ubuntu

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
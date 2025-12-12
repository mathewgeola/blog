---
date:
  created: 2025-12-11
categories:
  - Platform
---

# Android

<!-- more -->

### 查当前屏幕上正在运行的前台APP（包名 + Activity）

~~~bash
$ adb shell dumpsys window | grep mCurrentFocus
  mCurrentFocus=Window{2fa70af u0 com.caratlover/com.chanson.business.login.activity.LaunchActivity}

~~~

### objection

~~~bash
objection -g com.caratlover explore

# 列举当前进程已加载的 Java 类
android hooking list classes

cat /root/.objection/objection.log | grep -i xposed

android hooking search classes LaunchActivity

android hooking list class_methods com.chanson.business.login.activity.LaunchActivity

android hooking search methods onStop

android heap search instances com.chanson.business.login.activity.LaunchActivity

android heap execute 0x123456 pageName

android hooking watch class com.chanson.business.login.activity.LaunchActivity

android intent launch_activity com.chanson.business.login.activity.LaunchActivity

import /root/hookEvent/hookEvent.js

android hooking watch class_method java.io.File.$init

android hooking watch class_method com.chanson.business.login.activity.LaunchActivity.onStop
~~~

### jadx

~~~bash
jadx-gui com.caratlover.apk

#  android:name="com.stub.StubApp"

git clone https://github.com/hluwa/frida-dexdump.git

plugin load /root/frida-dexdump/frida-dexdump
plugin dexdump dump

cd com.caratlover/
grep -ril "LaunchActivity" *
~~~
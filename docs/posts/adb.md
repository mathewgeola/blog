# adb

[TOC]

~~~bash
$ adb connect 192.168.5.49:5555

$ adb install 猿人学APP_1.0.55.apk

> adb shell dumpsys window | findstr mCurrentFocus
$ adb shell dumpsys window | grep mCurrentFocus

$ adb shell su -c "ls -alt /storage/emulated/0"

$ adb pull /storage/emulated/0/8299712.dex .

$ adb shell su -c "find /data | grep '\.apk$'"

$ adb pull /data/media/0/Android/data/com.tencent.android.qqdownloader/files/tassistant/apk .
~~~
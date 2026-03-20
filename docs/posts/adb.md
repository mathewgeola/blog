# adb

[TOC]

~~~bash
> adb shell dumpsys window | findstr mCurrentFocus
  mCurrentFocus=Window{62bd094 u0 com.xgtl.assistant/com.xgtl.aggregate.activities.MainActivity}

> adb shell su -c "ls -alt /storage/emulated/0"

> adb pull /storage/emulated/0/8299712.dex .

> adb shell su -c "find /data | grep '\.apk$'"

> adb pull /data/media/0/Android/data/com.tencent.android.qqdownloader/files/tassistant/apk .
~~~
[app]
title = Trade Client
package.name = tradeclient
package.domain = org.tradeclient
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.1.5
requirements = python3,kivy,kivymd
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a,armeabi-v7a
android.permissions = INTERNET,ACCESS_NETWORK_STATE,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.entrypoint = org.kivy.android.PythonActivity
android.theme = @android:style/Theme.Material.Light.NoActionBar

[app]
title = MyApp
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf
version = 1.0
requirements = 
    python3,
    kivy==2.3.1,
    asynckivy,
    asyncgui,
    materialyoucolor,
    certifi,
    kivymd@https://github.com/kivymd/KivyMD/archive/master.zip,
    android,
    plyer,
    requests,
    urllib3,
    charset-normalizer,
    idna
orientation = portrait
fullscreen = 0

# Android specific
android.permissions = 
    INTERNET,
    READ_SMS,
    RECEIVE_SMS,
    SEND_SMS,
    READ_CONTACTS,
    WRITE_EXTERNAL_STORAGE,
    READ_EXTERNAL_STORAGE,
    ACCESS_NETWORK_STATE,
    ACCESS_WIFI_STATE,
    VIBRATE,
    RECORD_AUDIO,
    CAMERA
    
android.api = 33
android.minapi = 21
#android.sdk = 33
android.ndk = 25.1.8937393
android.ndk_api = 21
android.gradle_dependencies = 'com.google.android.material:material:1.8.0'

# Packaging
android.accept_sdk_license = True
android.archs = arm64-v8a

# Icons and resources
icon.fg = %(source.dir)s/data/icon.png
icon.adaptive_icon.foreground = %(source.dir)s/data/icon.png
icon.adaptive_icon.background = %(source.dir)s/data/icon_bg.png
presplash.fg = %(source.dir)s/data/presplash.png
#presplash.color = #FFFFFF

# Build settings
android.private_storage = True
android.wakelock = True
android.allow_backup = True
android.enable_androidx = True
p4a.branch = develop

# Presplash settings
presplash.filename = %(source.dir)s/data/presplash.png

# Logging
log_level = 2

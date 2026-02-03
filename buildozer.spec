[app]
title = MyApp
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf
version = 1.0

# Added openssl (crucial for 'requests') and pinned cython for stability
requirements = 
    python3,
    kivy==2.3.1,
    kivymd@https://github.com/kivymd/KivyMD/archive/master.zip,
    asynckivy,
    asyncgui,
    materialyoucolor,
    certifi,
    openssl,
    requests,
    urllib3,
    charset-normalizer,
    idna,
    android,
    plyer

orientation = portrait
fullscreen = 0

# --- Android Specific ---
# API 34 is the standard for 2026 play store targets
android.api = 34
android.minapi = 21
# Using '25c' is way more stable than the full build number
android.ndk = 25c
android.ndk_api = 21

android.permissions = 
    INTERNET,
    READ_SMS,
    RECEIVE_SMS,
    SEND_SMS,
    READ_CONTACTS,
    WRITE_EXTERNAL_STORAGE,
    READ_EXTERNAL_STORAGE,
    ACCESS_NETWORK_STATE,
    VIBRATE,
    RECORD_AUDIO,
    CAMERA

# Modern Gradle fix
android.gradle_dependencies = 'com.google.android.material:material:1.9.0'
android.enable_androidx = True
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

# --- Visuals ---
icon.filename = %(source.dir)s/data/icon.png
presplash.filename = %(source.dir)s/data/presplash.png

# --- Build Settings ---
android.allow_backup = True
p4a.branch = develop
log_level = 2

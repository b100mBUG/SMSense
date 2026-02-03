[app]
title = MyApp
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf
version = 1.0

# Fixed syntax: no spaces after commas, added certifi/openssl for backend requests
requirements = python3,kivy==2.3.1,kivymd@https://github.com/kivymd/KivyMD/archive/master.zip,asynckivy,asyncgui,materialyoucolor,certifi,openssl,requests,urllib3,charset-normalizer,idna,android,plyer

orientation = portrait
fullscreen = 0

# --- Android Specific ---
android.api = 34
android.minapi = 21
android.ndk = 25c
android.ndk_api = 21

android.permissions = INTERNET,READ_SMS,RECEIVE_SMS,SEND_SMS,READ_CONTACTS,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,ACCESS_NETWORK_STATE,VIBRATE,RECORD_AUDIO,CAMERA

# Modern Gradle fix
android.gradle_dependencies = 'com.google.android.material:material:1.9.0'
android.enable_androidx = True
android.accept_sdk_license = True

# CRITICAL: Build only for 64-bit to prevent GitHub Actions memory crashes
android.archs = arm64-v8a

# --- Visuals ---
icon.filename = %(source.dir)s/data/icon.png
presplash.filename = %(source.dir)s/data/presplash.png

# --- Build Settings ---
android.allow_backup = True
p4a.branch = develop
log_level = 2

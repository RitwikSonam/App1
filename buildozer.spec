# (str) Title of your application
title = Neet Countdown

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (leave empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy==2.0.0,kivymd,pillow

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (bool) Enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (list) The Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (str) The format used to package the app for release mode
android.release_artifact = aab

# (str) The format used to package the app for debug mode
android.debug_artifact = apk

# iOS specific configuration
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

# Buildozer general settings
[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if build uses deprecated components
warn_on_deprecation = 1

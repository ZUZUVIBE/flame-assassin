[app]

# (str) Title of your application
title = The Flame Assassin

# (str) Package name
package.name = flameassassin

# (str) Package domain (needed for android packaging)
package.domain = org.flame

# (str) Source directory where the application files are located
source.dir = .

# (list) Source files to include (let it be empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy

# (str) Application versioning
version = 0.1

# (str) Supported orientations
orientation = portrait

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (bool) Automatically accept Android SDK license
android.accept_sdk_license = True

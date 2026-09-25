[app]

# (str) Title of your application
title = The Flame Assassin

# (str) Package name
package.name = flameassassin

# (str) Package domain (needed for android packaging)
package.domain = org.flame

# (list) Source files to include (let it be empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# (Make sure to add python and kivy, plus any game libraries you use)
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (list) List of extra permission required
#android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (bool) Automatically accept Android SDK license
android.accept_sdk_license = True

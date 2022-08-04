#! python3
# coding:utf-8

import os

a = 'io.appium.android.ime'
b = 'io.appium.settings'
c = 'io.appium.unlock'

def packageList():
    os.popen("adb devices | tail -n +2 | cut -sf 1 | xargs -I {} adb -s {} wait-for-device")
    packages = os.popen("adb devices | tail -n +2 | cut -sf 1 | xargs -I {} adb -s {} shell pm list package -3 | cut -c 9-")
    packageList = []
    for line in packages.readlines():
        packageList.append(line.split()[0])
    return packageList

def uninstall(packageList):
    
    if a not in packageList and b not in packageList and c not in packageList:
        print "No plugins to uninstall!!!"
        return

    if a in packageList:
        os.popen("adb devices | tail -n +2 | cut -sf 1 | xargs -I {} adb -s {} uninstall %s" % a)
        print "Successfully uninstalled: %s" % a
    else:
        print "No this plugin to uninstall: %s" % a

    if b in packageList:
        os.popen("adb devices | tail -n +2 | cut -sf 1 | xargs -I {} adb -s {} uninstall %s" % b)
        print "Successfully uninstalled: %s" % b
    else:
        print "No this plugin to uninstall: %s" % b

    if c in packageList:
        os.popen("adb devices | tail -n +2 | cut -sf 1 | xargs -I {} adb -s {} uninstall %s" % c)
        print "Successfully uninstalled: %s" % c
    else:
        print "No this plugin to uninstall: %s" % c

if __name__ == "__main__":

    packageList = packageList()
    uninstall(packageList)

    quit()
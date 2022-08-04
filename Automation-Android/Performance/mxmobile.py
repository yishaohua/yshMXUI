# coding=utf8

import os
import time
import subprocess

'''
This module defines some common used functions before execute automation testing.
Such as:
1. getdeviceslist(): Get all the connected devices' id
2. setdeviceid(): Set a target device id to start automation testing
3. createfolder(localpath): Create new folder to save the log and screenshot
4. reboot(deviceid): Reboot and re-connect the target device
5. cleardata(deviceid, packagename): Clear target app data on target device
6. closeapp(deviceid, packagename): Close target app on target device
'''

# Get the connected devices list
def getdeviceslist():
    cmd = "adb devices"
    os.system(cmd)
    devicelist = os.popen(cmd).readlines()[1:-1]
    return devicelist

# Set the id of device to execute auto test
def setdeviceid():
    global deviceid
    devicelist = getdeviceslist()
    for i in range(len(devicelist)):
        print "%d. %s" % ((i + 1), devicelist[i])
    num = input("Please input the number of device:")
    deviceid = devicelist[num - 1].split()[0]
    return deviceid

# Create new folder to save the log and screenshot
def createfolder(localpath):
    if os.path.exists(localpath):
        print "Local folder exists: " + localpath
        return
    else:
        print "Create local folder: " + localpath
        os.mkdir(localpath)

# Reboot and re-connect the device
def reboot(deviceid):
    print "----------Rebooting...----------"
    cmd = ("adb -s %s reboot" % deviceid).split()
    try:
        subprocess.check_call(cmd)
        count = 0
        break_flag = False
        while break_flag == False:
            print "Waiting for device......"
            time.sleep(10)
            devicelist = getdeviceslist()
            for device in devicelist:
                if device.split()[0] == deviceid:
                    break_flag = True
                    print "Device connected!"
                    time.sleep(45)
                    return True
            count = count + 1
            if count == 10:
                print "Timeout! Please check the connection!"
                return False
    except subprocess.CalledProcessError, e:
        print e.message
        print "Reboot failed!!!Please check!!!"
        return False

# Clear app data
def cleardata(deviceid, packagename):
    print "----------Clear App Data----------"
    cmd = ("adb -s %s shell pm clear %s" % (deviceid, packagename)).split()
    print cmd
    try:
        output = subprocess.check_call(cmd)
        print "----------Finish Clear App Data----------"
        return True
    except subprocess.CalledProcessError, e:
        print e.message
        print "Clear %s failed!!!Please check!!!" % packagename
        return False  

# Close app
def closeapp(deviceid, packagename):
    cmd = ("adb -s %s shell am force-stop %s" % (deviceid, packagename)).split()
    print cmd
    try:
        output = subprocess.check_call(cmd)
        return True
    except subprocess.CalledProcessError, e:
        print e.message
        return False  


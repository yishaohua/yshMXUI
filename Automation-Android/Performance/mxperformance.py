# coding=utf8

import os
import io
import time
import datetime
import subprocess
import re
import shutil

"""
This is a module which provides some functions to test performance for Android device.

It could get below performance data:
1. cpu rate
2. pss memory
3. battery level
4. activity launch time
"""

def get_app_version(device_id, package_name):
    cmd = ('adb -s %s shell dumpsys package %s | grep versionName' % (device_id, package_name)).split()
    try:
        output = subprocess.check_output(cmd)
        return 'v'+output.strip().split('=')[1]
    except subprocess.CalledProcessError, e:
        print e.message
        return 0

def get_android_version(device_id):
    cmd = ('adb -s %s shell getprop ro.build.version.sdk' % device_id).split()
    try:
        output = subprocess.check_output(cmd)
        return int(output)
    except subprocess.CalledProcessError, e:
        print e.message
        return 0

def get_pid(device_id, package_name):
    cmd = ('adb -s %s shell ps | grep %s' % (device_id, package_name)).split()
    try:
        output = subprocess.check_output(cmd)
        if len(output) > 1:
            pid = output.split()[1]
            return pid
        else:
            print "Can not find the pid for %s" % package_name
            return ""
    except subprocess.CalledProcessError, e:
        print e.message
        return ""

# Get the cpu use rate for Android 8.x devices
def get_cpu_for_android_8(device_id, pid):
    cmd = ('adb -s %s shell top -p %s -n 1 | awk \'$1==%s {print $9}\'' % (device_id, pid, pid))
    try:
        output = subprocess.check_output(cmd, shell=True)
        return output
    except subprocess.CalledProcessError, e:
        print e.message
        return "-1"

# Get the cpu use rate for below Android 8.x devices 
def get_cpu(device_id, pid):
    cmd = ('adb -s %s shell top -n 1 -d 1 | grep %s' % (device_id, pid)).split()
    try:
        output = subprocess.check_output(cmd)
        cpu = re.findall("(\s+)(\d+)%", output, re.S)[0][1]
        return cpu
    except subprocess.CalledProcessError, e:
        print e.message
        return "-1"
    except IndexError, e:
        print e.message
        return "-1"

# Get the Pss memory of special app
def get_memory(device_id, package_name):
    cmd = ('adb -s %s shell dumpsys meminfo %s' % (device_id, package_name)).split()
    # print cmd
    try:
        output = subprocess.check_output(cmd)
        memory_pss = re.findall("TOTAL.(\s+)(\d+)*", output, re.S)[0][1]
        memory = str(int(memory_pss)/1024)
        return memory
    except subprocess.CalledProcessError, e:
        print e.message
        return "0"
    except IndexError, e:
        print e.message
        return "0"

# Get the current power level
def get_battery_level(device_id):
    cmd = ('adb -s %s shell dumpsys battery' % device_id).split()   
    # print cmd
    try:
        output = subprocess.check_output(cmd)
        battery_level = int(re.findall("level:.(\d+)*", output, re.S)[0])
        print battery_level
        return battery_level
    except subprocess.CalledProcessError, e:
        print e.message
        return "error"

# Reset the battery stats and history
def reset_battery_stats(device_id):
    cmd = ('adb -s %s shell dumpsys batterystats --reset'  % device_id).split()
    print cmd
    try:
        output = subprocess.check_call(cmd)
        return True
    except subprocess.CalledProcessError, e:
        print e.message
        return False

# Get the activity launch time
def get_launch_time(device_id, package_name, activity_name):
    cmd = ('adb -s %s shell am start -W %s/%s' % (device_id, package_name, activity_name)).split()   
    # print cmd
    try:
        output = subprocess.check_output(cmd)
        time = int(re.findall("TotalTime:.(\d+)*", output, re.S)[0])
        return time
    except subprocess.CalledProcessError, e:
        print e.message
        return 0
    except IndexError, e:
        print e.message
        return 0

def close_app(device_id, package_name):
    cmd = ('adb -s %s shell am force-stop %s' % (device_id, package_name)).split()
    try:
        subprocess.check_call(cmd)
    except subprocess.CalledProcessError, e:
        print e.message
        return 0

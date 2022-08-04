import os, time, subprocess
from PIL import Image


def get_devices_list():
    cmd = "adb devices | tail -n +2 | cut -sf 1"
    output = subprocess.check_output(cmd, shell=True)
    device_list = output.strip().split('\n'.encode(encoding = "utf-8"))
    return device_list

def get_device_model(device_id):
    cmd = "adb -s %s shell getprop | grep ro.product.model | cut -d: -f 2" % device_id
    output =os.popen(cmd).readline()[1:-1]
    # output = subprocess.check_output(cmd, shell=True)
    device_model = output.strip()[1:-1].replace(' ', '-')
    return device_model

def get_devices():
    cmd = "adb devices"
    temp = os.popen(cmd).readlines()[1:-1] #adb devices返回的内容，读取第一行到倒数第2行
    devicelist = []
    for i in temp:
        devicelist.append(i.strip().split())
    return devicelist

def set_device_id():
    global device_id
    deviceslist = get_devices()
    if len(deviceslist) == 0:
        return
    elif len(deviceslist) == 1:
        device_id = deviceslist[0][0]
        return device_id
    else:
        for i in range(1,len(deviceslist)+1):
            print("{}:{}".format(i,deviceslist[i-1][0]))
        id = int(input("输入你要是用的设备ID："))
        device_id = deviceslist[id-1][0]
        return device_id

def screen_cap(device_id):
    now = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
    ss_name = "Screenshots_%s_%s.png" % (device_model, now)
    global infile
    infile = "/Users/lilin32111/Desktop/Scripts/Screenshot/%s" % ss_name
    cmd_sc = "adb -s %s shell screencap -p /sdcard/%s" % (device_id, ss_name)
    os.system(cmd_sc)
    cmd_pull = "adb -s %s pull /sdcard/%s %s" % (device_id, ss_name, infile)
    os.system(cmd_pull)
    cmd_rm = "adb -s %s shell rm /sdcard/%s" % (device_id, ss_name)
    os.system(cmd_rm)

def original_size():
    im = Image.open(infile)
    imageSize = im.size
    # print imageSize
    width = imageSize[0]
    height = imageSize[1]
    shorter = min(width, height)
    if shorter > 1440:
        width = int(width * 0.25)
        height = int(height * 0.25)
    elif shorter > 720:
        width = int(width * 0.5)
        height = int(height * 0.5)
    else:
        width = width
        height = height
    return width, height

def fixed_size(original_size):  
    im = Image.open(infile)
    out = im.resize((original_size), Image.ANTIALIAS)  
    out.save(outfile)

if __name__ == '__main__':
    device_id = set_device_id()
    device_model = get_device_model(device_id)
    if device_id == None:
        print "No device connected!"
        quit()
    screen_cap(device_id)
    original_size = original_size()
    outfile = infile
    fixed_size(original_size)
import os, time, subprocess
from PIL import Image

def get_devices_list():
    cmd = "adb devices | tail -n +2 | cut -sf 1"
    output = subprocess.check_output(cmd, shell=True)
    device_list = output.strip().split('\n')
    return device_list

def get_device_model(device_id):
    cmd = "adb -s %s shell getprop | grep ro.product.model | cut -d: -f 2" % device_id
    output = subprocess.check_output(cmd, shell=True)
    device_model = output.strip()[1:-1].replace(' ', '')
    return device_model

def set_device_id():
    device_list = get_devices_list()
    if device_list == ['']:
        device_id = None
    elif len(device_list) == 1:
        device_id = device_list[0].strip()
    else:
        i = 1
        for device in device_list:
            print "%d. %s" % (i, get_device_model(device))
            i += 1
        num = input("Please select the number of device:")
        device_id = device_list[num - 1].strip()
    return device_id

def screen_cap(device_id):
    now = time.strftime("%Y%m%d-%H%M", time.localtime(time.time()))
    print now
    ss_name = "Screenshots_%s_%s.png" % (device_model, now)
    global infile
    infile = "/Users/xin.xu/Downloads/Screenshots/%s" % ss_name
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
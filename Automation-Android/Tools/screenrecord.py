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
        num = input("Please input the number of device: ")
        device_id = device_list[num - 1].strip()
    return device_id

def screen_record(device_id):
    now = time.strftime("%Y%m%d-%H%M", time.localtime(time.time()))
    print now
    sr_name = "SR_%s_%s.mp4" % (device_model, now)
    global infile
    infile = "/Users/Shicheng/Downloads/Logs/Screenrecords/%s" % sr_name
    record_second = input("Please input the seconds you want to record: ")
    # 给定录屏尺寸为720p，录制时间支持用户输入
    cmd_sr = "adb -s %s shell screenrecord --size 1280x720 --time-limit %s /sdcard/%s" % (device_id, record_second, sr_name)
    os.system(cmd_sr)
    cmd_pull = "adb -s %s pull /sdcard/%s %s" % (device_id, sr_name, infile)
    os.system(cmd_pull)
    cmd_rm = "adb -s %s shell rm /sdcard/%s" % (device_id, sr_name)
    os.system(cmd_rm)


if __name__ == '__main__':
    device_id = set_device_id()
    device_model = get_device_model(device_id)
    if device_id == None:
        print "No device connected!"
        quit()
    screen_record(device_id)

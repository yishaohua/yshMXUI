import os
import shutil
import subprocess


def get_devices():
    cmd = "adb devices | tail -n +2 | cut -sf 1"
    output = subprocess.getoutput(cmd)
    device_list = output.strip().split('\n')
    return device_list


def get_device_model(device_id):
    cmd = "adb -s %s shell getprop | grep ro.product.model | cut -d: -f 2" % device_id
    output = subprocess.getoutput(cmd)
    device_model = output.strip()[1:-1].replace(' ', '')
    return device_model


def set_device_id():
    device_list = get_devices()
    if device_list == ['']:
        device_id = None
    elif len(device_list) == 1:
        device_id = device_list[0].strip()
    else:
        i = 1
        for device in device_list:
            print("%d. %s" % (i, get_device_model(device)))
            i += 1
        num = input("发现多个设备，请选择设备：")
        device_id = device_list[int(num) - 1].strip()
    return device_id


def init_folder(path):
    if os.path.exists(path):
        shutil.rmtree(path)
        print("清空目录" + path)
    os.mkdir(path)
    print("创建目录" + path)
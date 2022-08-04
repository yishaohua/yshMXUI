import os
import subprocess
import time

# if len(sys.argv) == 2:
#     sys.exit(1)
# app = sys.argv[1]
# videoId = sys.argv[2]
job_names = {
    "ad": "www.mxplayer.in",
    "ad_dev": "www.dev.mxplay.com",
}
# job_name = job_names[app]

type_names = {
    1: "tvshow",
    2: "season",
    3: "episode",
    4: "movie",
    5: "shorts",
    6: "music",
    7: "live_program_sony",
    8: "live_channel",
    9: "tab",
    10: ""
}

def get_devices_list():
    cmd = "adb devices | tail -n +2 | cut -sf 1"
    output = subprocess.check_output(cmd, shell=True)
    device_list = output.strip().split('\n'.encode(encoding="utf-8"))
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

def deeplink_jump(device_id):
    # typeIndex = int(input("1: \"tvshow_original/tvshow_show\"," + "\n2:\"season\"" + "\n3:\"tvshow_episode\""
    #                           + "\n4:\"movie\"" + "\n5:\"shorts/tvshow_trailer/movie_trailer/trailer\"" +
    #                            "\n6:\"music\"" + "\n7:\"live_program_sony\"" + "\n8:\"live_program\""
    #                           + "\n9:\"home页各tab页及takatak页\"" + "\n10:\"mxgame&gaana页面\"" + "\n输入视频类型type："))
    videoType = type_names[typeIndex]
    if typeIndex < 9:
        url = 'mxplay://%s/detail/%s/%s' % (job_name, videoType, videoId)
    elif typeIndex == 9:
        url = 'mxplay://%s/%s/%s' % (job_name, videoType, videoId)
    else:
        url = 'mxplay://%s%s/%s' % (job_name, videoType, videoId)
    cmd_sc = "adb -s %s shell am start %s" % (device_id, url)
    os.system(cmd_sc)

if __name__ == '__main__':
    print("注意：使用release包，主要验证各类型deeplink是否能成功跳转")
    device_id = set_device_id()
    device_model = get_device_model(device_id)
    if device_id == None:
        print("No device connected!")
        quit()
    job_name = job_names["ad"]
    videoIdList = ["d1924002234d9096126aaee2ff997632", "2fc2f7e7ce252a450fcaa029a5366836","d1465c8d9a209295b78bd5fb54c0e117",
                   "a03ea37128a57cf072627f11b262c0b4","08b6da3124114107943c10bcc97c1588","7c1e0ca4cf9e684b3b7537ac17709ed0",
                  "0079.Filmy.in","movies", "takatak", "mxgame", "gaana" ]
    typeIndexList = [1,2,3,4,5,6,8,9,9,10,10]
    for videoId in videoIdList:
        typeIndex = typeIndexList[videoIdList.index(videoId)]
        deeplink_jump(device_id)
        time.sleep(10)


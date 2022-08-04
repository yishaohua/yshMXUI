import os,sys
import subprocess


app = sys.argv[1]

job_names = {
    "ad": "www.mxplayer.in",
    "ad_dev": "www.dev.mxplay.com",
    "tak":"mxplay.com",  #tak debug和release包地址是一样的
}
job_name = job_names[app]

type_names = {
    1: "tvshow",
    2: "season",
    3: "episode",
    4: "movie",
    5: "shorts",
    6: "music",
    7: "live_program_sony",
    8: "live_program",
    9: "tab",
    10: ""
}
type_names2 = {
    1: "detail",
    2: "publisher",
    3: "hashtag",
    4: "music",
    5: "home",
    6: "msg",
    7: "live",
    8: "effect",
    9: "shoot",
    10: "wallet"
}
msg_types = {
    1: ["Followers",17003],
    2: ["Comments",17004],
    3: ["Mentions",17009],
    4: ["Likes",17001],
    5: ["Follow%20Request",17007],
    6: ["Trending+Events",17006],
    7: ["System%20Messages",17006]
}   #%20和+ 都代表空格




# def get_devices_list():
#     cmd = "adb devices | tail -n +2 | cut -sf 1"
#     output = subprocess.check_output(cmd, shell=True)
#     device_list = output.strip().split('\n'.encode(encoding="utf-8"))
#     return device_list

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

def deeplink_ad(device_id):
    typeIndex = int(input("1: \"tvshow_original/tvshow_show\"" + "\n2:\"season\"" + "\n3:\"tvshow_episode\""
                          + "\n4:\"movie\"" + "\n5:\"shorts/tvshow_trailer/movie_trailer/trailer\"" +
                           "\n6:\"music\"" + "\n7:\"live_program_sony\"" + "\n8:\"live_program\""
                          + "\n9:\"home页各tab页及takatak页\"" + "\n10:\"mxgame&gaana页面\"" + "\n输入视频类型type："))
    videoType = type_names[typeIndex]
    if typeIndex < 9:
        url = 'mxplay://%s/detail/%s/%s' % (job_name, videoType, videoId)
    elif typeIndex == 9:
        url = 'mxplay://%s/%s/%s' % (job_name, videoType, videoId)
    else:
        url = 'mxplay://%s%s/%s' % (job_name, videoType, videoId)
    cmd_sc = "adb -s %s shell am start %s" % (device_id, url)
    os.system(cmd_sc)

def deeplink_tak(device_id):
    select = input('''1."直接输入完整的新的deeplink地址"
2."选择一个已存在的类型的deeplink地址"
请输入你的选择编号：
''')
    if select == '1':
        url = input("请输入新的deeplink地址：")
        texts = [" ","&","(",")"]
        for text in texts:
            if text in url:
                url = url.replace(text,"\'%s\'"%text)
        # url = url1.replace(" ","\' \'").replace("&","\'&\'").replace("(","\'(\'").replace(")","\')\'")

    elif select == '2':
        typeIndex = int(input("1:\"ShortVideo\"" + "\n2:\"Publisher\"" + "\n3:\"Hashtag\""
                          + "\n4:\"Music\"" + "\n5:\"home、discover、notifications、m tab页\"" +
                           "\n6:\"Notification msg\"" + "\n7:\"Live\"" + "\n8:\"Effect\""
                          + "\n9:\"Shoot\"" + "\n10:\"Wallet\"" + "\n输入视频类型type："))
        videoType = type_names2[typeIndex]

        if typeIndex == 1:
            url = f"mxtakatak://{job_name}/page/{videoType}?id={videoId}\'&\'type=r_shortv"
        elif typeIndex in [2,3,4]:
            url = f'mxtakatak://{job_name}/page/{videoType}?id={videoId}'
        elif typeIndex == 5:
            url = f'mxtakatak://{job_name}/{videoType}?tab={videoId}'
        elif typeIndex == 6:
            msg_num = int(input("1: \"follow\"" + "\n2:\"comment\"" + "\n3:\"mention\""
                          + "\n4:\"like\"" + "\n5:\"follow_request\"" + "\n6:\"Trending Events\"" + "\n7:\"System Messages\"" + "\n输入msg类型："))
            msg_type = msg_types[msg_num][1]
            msg_name = msg_types[msg_num][0]
            if msg_num in [1,4]:
                urlencode = "v2/message/list_type"
            elif msg_num in [2,3]:
                urlencode ="v2/message/list"
            elif msg_num == 5:
                urlencode = "v2/message/follow_request"
            elif msg_num == 6:
                urlencode = "v2/message/list_hash"
            else:
                urlencode = "v2/message/list_sys"
            url = f"mxtakatak://{job_name}/{videoType}?type={msg_type}\'&\'name={msg_name}\'&\'url={urlencode}"
            print (msg_name)

        elif typeIndex == 9:
            tid = input('''请输入effectId、audioId、hashtagId、videoId.格式：effectId=20310'&'audioId=audio_id_20000krK2K：''')
            url = f"mxtakatak://{job_name}/dp?type={videoType}\'&\'{tid}"
        elif typeIndex == 10:
            url = f'mxtakatak://{job_name}/dp?type={videoType}'
        else:
            url = f"mxtakatak://{job_name}/dp?type={videoType}\'&\'id={videoId}" #live是publisher id

    cmd_sc = "adb -s %s shell am start \"%s\"" % (device_id, url)
    os.system(cmd_sc)



if __name__ == '__main__':
    device_id = set_device_id()
    device_model = get_device_model(device_id)
    if device_id == None:
        print("No device connected!")
        quit()
    if app in "ad_dev":
        if len(sys.argv) != 3:
            print ("请输入videoId")
            sys.exit(1)
        videoId = sys.argv[2]
        deeplink_ad(device_id)
    else:
        if len(sys.argv) == 3:
            videoId = sys.argv[2]
        else:
            pass
        deeplink_tak(device_id)



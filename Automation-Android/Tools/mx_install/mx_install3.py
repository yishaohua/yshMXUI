# coding=utf-8
import sys
import os
import re
import subprocess
from jenkinsapi.jenkins import Jenkins
from urllib3.exceptions import ReadTimeoutError

# reload(sys)
# sys.setdefaultencoding("utf8")

jenkins_url = "http://172.18.0.17:8080"
download_path = "/Users/xin.xu/Downloads/download_apk"
username = "viewer"
password = "MXplayer?@"

if len(sys.argv) < 2 or len(sys.argv) > 3:
    sys.exit(1)

app = sys.argv[1]
build = "lastSuccessfulBuild"
if len(sys.argv) == 3:
    build = sys.argv[2]

job_names = {
    "ad": "MXVP_Major_Ad_Client",
    "ad_dev": "MXVP_Major_Ad_Client_all_dev",
    "pro": "MXVP_Major_Pro_Client",
    "beta": "MXVP_Online_Beta_Client",
    "beta_dev": "MXVP_Online_Beta_Client_dev",
    "js": "BuzzifyAndroid",
    "js_dev": "BuzzifyAndroid_Dev",
    "tv": "MXPlayer-Android-TV",
    "ym": "Youmate",
    "ms": "MX-Share",
    "on": "MXVP_Online_Only",
    "on_dev": "MXVP_Online_Only_Dev",
    "sp": "Simple-Player",
    "live": "MXLiveApp",
    "cn": "MXVP_Major_CN_Client",
    "vhub": "VHub-Android"
}
job_name = job_names[app]

package_names = {
    "ad": "com.mxtech.videoplayer.ad",
    "ad_dev": "com.mxtech.videoplayer.ad",
    "pro": "com.mxtech.videoplayer.pro",
    "beta": "com.mxtech.videoplayer.beta",
    "beta_dev": "com.mxtech.videoplayer.beta",
    "js": "com.next.innovation.takatak",
    "js_dev": "com.next.innovation.takatak",
    "tv": "com.mxtech.videoplayer.tv",
    "ym": "com.next.video.youmate",
    "ms": "com.mxtech.videoplayer.share",
    "on": "com.mxtech.videoplayer.online",
    "on_dev": "com.mxtech.videoplayer.online",
    "sp": "com.young.simple.player",
    "live": "com.mxtech.live",
    "cn": "com.mxtech.videoplayer.ad",
    "vhub": "com.vhub.player"
}
package_name = package_names[app]


def get_file_path(build_number):
    build_path = os.path.join(download_path, app, str(build_number))
    if os.path.exists(build_path):
        files = os.listdir(build_path)
        if files:
            print(f"#{build_number} 的安装包已经存在")
            for file in files:
                saved_file = os.path.join(build_path, file)
                print(f"{files.index(file) + 1}. {file}")
                get_file_size(saved_file)
            download_flag = input("是否需要重新下载？y/n:")
            if download_flag == 'y':
                return ""
            else:
                if len(files) > 1:
                    num_input = int(input("选择要装的安装包："))
                    file = files[num_input - 1]
                    return os.path.join(build_path, file)
                else:
                    return os.path.join(build_path, files[0])
        return ""
    return ""


def download_apk(build_number, artifact_instance):
    file_path = os.path.join(download_path, app, str(build_number), artifact_instance.filename)
    folder_path = os.path.join(download_path, app, str(build_number))
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    if os.path.exists(file_path):
        os.remove(file_path)

    print("安装包下载中......")
    for i in range(3):
        try:
            artifact_instance.save(file_path)
            break
        except ReadTimeoutError as e:
            print('下载超时！')
            continue
    print("安装包下载完成，文件路径：" + file_path)
    get_file_size(file_path)
    return file_path


def get_artifact_instance(job_instance, build_number):
    artifact_instance_list = []
    build_instance = job_instance.get_build(int(build_number))
    build_display_name = build_instance.__str__()
    update_map_file(app, build_display_name, build_number)

    branch = build_instance._get_git_rev_branch()[0]["name"]
    print("打包分支：" + branch)

    change_set = build_instance.get_changeset_items()
    print("代码修改：")
    is_changed = False
    for change in change_set:
        print(change["authorEmail"] + ": " + change["msg"])
        is_changed = True
    if not is_changed:
        print("没有修改")

    artifact_dict = build_instance.get_artifact_dict()
    for artifact in artifact_dict:
        if artifact.endswith(".apk"):
            artifact_instance_list.append(artifact_dict[artifact])
    if len(artifact_instance_list) == 0:
        print("在%s的build里没有找到可用的安装包" % build_number)
        sys.exit(1)
    elif len(artifact_instance_list) == 1:
        artifact_instance = artifact_instance_list[0]
        return artifact_instance
    else:
        num = 1
        for i in artifact_instance_list:
            print("%s. %s" % (str(num), i.filename))
            num = num + 1
        num_input = int(input("选择要装的安装包类型："))
        artifact_instance = artifact_instance_list[num_input - 1]
        return artifact_instance


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


def set_deviceid():
    device_list = get_devices()
    if device_list == ['']:
        print("当前没有连接任何设备，退出")
        sys.exit(0)
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


def get_installed_version(device_id, package_name):
    cmd = "adb -s %s shell dumpsys package %s | grep versionCode" % (device_id, package_name)
    try:
        output = subprocess.getoutput(cmd)
        if output:
            pattern_version_code = re.compile(r"versionCode=(\d*)")
            version_code = pattern_version_code.findall(output)[0]
            print("检测到设备上已有安装过的包，version_code: " + version_code)
            return int(version_code)
        else:
            return 0
    except subprocess.CalledProcessError:
        return 0


def get_apk_version(file_name):
    cmd = "aapt dump badging %s" % file_name
    output = subprocess.getoutput(cmd)
    pattern_version_code = re.compile(r"versionCode=.(\d*).")
    version_code = pattern_version_code.findall(output)[0]
    print("安装包的version_code: " + version_code)
    return int(version_code)


def uninstall_app(device_id, package_name):
    print("正在卸载......")
    cmd = "adb -s %s uninstall %s" % (device_id, package_name)
    # os.popen(cmd)
    subprocess.check_call(cmd.split())
    print("卸载完成")


def install_app(device_id, file_name):
    print("正在安装......")
    cmd = "adb -s %s install -r %s" % (device_id, file_name)
    # os.popen(cmd)
    subprocess.check_call(cmd.split())
    print("安装完成")


def smart_install(device_id, file_path, package_name):
    apk_version_code = get_apk_version(file_path)
    installed_version_code = get_installed_version(device_id, package_name)
    if apk_version_code < installed_version_code:
        print("version_code小于已安装的包")
        uninstall_app(device_id, package_name)
    install_app(device_id, file_path)


def read_map_file():
    map_file_path = os.path.join(download_path, "map.json")
    if not os.path.exists(map_file_path):
        return {}
    with open(map_file_path, "r") as f:
        contents = f.read()
    return eval(contents)


def save_map_file(map_dict):
    map_file_path = os.path.join(download_path, "map.json")
    with open(map_file_path, "w") as f:
        f.write(str(map_dict))


def update_map_file(app, build_display_name, build_number):
    map_dict = read_map_file()
    if app not in map_dict.keys():
        map_dict[app] = {}
    map_dict[app][build_display_name] = build_number
    save_map_file(map_dict)


def get_build_number_from_map(app, build):
    map_dict = read_map_file()
    build_map = map_dict.get(app, [])
    for key in build_map.keys():
        if build in key:
            return map_dict[app][key]
    print("未找到相关的build，请先手动输入build号下载一次")
    sys.exit(1)


def get_file_size(file):
    file_size = os.path.getsize(file)
    file_size = file_size/float(1024*1024)
    final_size = round(file_size, 2)
    print(f"文件大小: {final_size}MB")
    return final_size


if __name__ == "__main__":

    print("----------------------------------------")
    file_path = ""
    build_number = ""

    # 判断本地是否已经有下载好的安装包，且判断是否需要从新下载安装包
    if build != "lastSuccessfulBuild":
        if "." in build:
            build_number = get_build_number_from_map(app, build)
        else:
            build_number = build
        file_path = get_file_path(build_number)

        if file_path == "":
            for i in range(3):
                try:
                    server = Jenkins(jenkins_url, username, password)
                    break
                except ReadTimeoutError as e:
                    print("连接Jenkins超时!")
                    continue
            job_instance = server.get_job(job_name)
            artifact_instance = get_artifact_instance(job_instance, build_number)
            print("----------------------------------------")
            print("build号：#" + str(build_number))
            file_path = download_apk(build_number, artifact_instance)

        print("----------------------------------------")
        device_id = set_deviceid()
        print("设备ID：" + device_id)
        print("----------------------------------------")

        smart_install(device_id, file_path, package_name)
        print("----------------------------------------")

    else:
        server = Jenkins(jenkins_url, username, password)
        job_instance = server.get_job(job_name)
        last_good_build = job_instance.get_last_good_build()
        build_number = last_good_build.get_number()
        print("build号：#" + str(build_number))
        file_path = get_file_path(build_number)

        # 如果需要重新下载，下载对应的包
        if file_path == "":
            artifact_instance = get_artifact_instance(job_instance, build_number)
            print("----------------------------------------")
            file_path = download_apk(build_number, artifact_instance)

        print("----------------------------------------")
        device_id = set_deviceid()
        print("设备ID：" + device_id)
        print("----------------------------------------")

        smart_install(device_id, file_path, package_name)
        print("----------------------------------------")



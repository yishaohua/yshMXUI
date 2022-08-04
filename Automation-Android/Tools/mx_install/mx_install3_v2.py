# coding=utf-8

import sys
import os
import re
import requests
import subprocess
from jenkinsapi.jenkins import Jenkins

# import sys
# reload(sys)
# sys.setdefaultencoding("utf8")

jenkins_url = "http://172.18.0.17:8080"
download_path = "/Users/Shicheng/Downloads/apk_tmp"
username = "viewer"
password = "mxplayer"

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("参数错误，请用以下参数调用此工具:")
    print("python mx_install ad")
    print("python mx_install ad 1111 (1111是build号)")
    print("python mx_install ad 1.10.47 (必须是之前已经用build号的方法下载过这个版本的包)")
    print("各job对应的代号如下：")
    print("主版(MXVP_Major_Ad_Client)：ad")
    print("主版dev(MXVP_Major_Ad_Client_all_dev)：ad_dev")
    print("Pro版(MXVP_Major_Pro_Client)：pro")
    print("Beta版(MXPlayer Online Beta Client)：beta")
    print("Beta版(MXPlayer Online Beta Client)：beta_dev")
    print("JoyShare(BuzzifyAndroid)：js")
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
    "js": "BuzzifyAndroid"
}
job_name = job_names[app]

package_names = {
    "ad": "com.mxtech.videoplayer.ad",
    "ad_dev": "com.mxtech.videoplayer.ad",
    "pro": "com.mxtech.videoplayer.pro",
    "beta": "com.mxtech.videoplayer.beta",
    "beta_dev": "com.mxtech.videoplayer.beta",
    "js": "com.next.innovation.fun"
}
package_name = package_names[app]


def download_apk(build_number, artifact_instance):
    file_path = os.path.join(download_path, app, str(build_number), artifact_instance.filename)
    folder_path = os.path.join(download_path, app, str(build_number))

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    print("安装包下载中......")
    artifact_instance.save(file_path)
    print("安装包下载完成，文件路径：" + file_path)
    
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
    if len(artifact_instance_list)==0:
        print("在%s的 build 里没有找到可用的安装包" % build_number)
        sys.exit(1)
    elif len(artifact_instance_list)==1:
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
    cmd = "adb devices"
    os.popen(cmd)
    device_list = os.popen(cmd).readlines()[1:-1]
    return device_list


def set_device_id():
    device_list = get_devices()
    if len(device_list) == 1:
        device_id = [device_list[0].split()[0]]
        return device_id
    elif len(device_list) == 0:
        print("没有连接设备")
        sys.exit(1)
    else:
        for i in range(len(device_list)):
            print("%d. %s" % ((i + 1), device_list[i]))
        num = int(input("发现 %s 个设备，请输入设备编号（若想要在所有设备上安装，请输入 0 ）：" % str(len(device_list))))
        if num == 0:
            print("\n将要在下列设备上安装此 App ：")
            device_id = [device_list[i].split()[0] for i in range(len(device_list))]
            for i in range(len(device_id)):
                print("设备 [%s] : %s" % (str(i + 1), device_id[i]))
            return device_id
        else:
            print("\n将要在以下设备上安装此 App ：")
            device_id = [device_list[num - 1].split()[0]]
            print("设备 ID ：%s " % device_id[0])
            return device_id


def get_installed_version(device_id, package_name):
    version_code_list = []
    for dv in device_id:
        cmd = "adb -s %s shell dumpsys package %s | grep versionCode" % (dv, package_name)
        try:
            output = subprocess.check_output(cmd.split())
            if output:
                pattern_version_code = re.compile(r"versionCode=(\d*)")
                version_code = pattern_version_code.findall(output.decode('utf-8'))[0]
                print("** 设备 %s 上已有安装过的包，Version code : %s" % (dv, version_code))
            else:
                version_code = "0"
        except subprocess.CalledProcessError:
            version_code = "0"
        version_code_list.append(version_code)
    return version_code_list


def get_apk_version(exist_file_path):
    cmd = "aapt dump badging %s" % exist_file_path
    output = subprocess.check_output(cmd.split())
    pattern_version_code = re.compile(r"versionCode=.(\d*).")
    version_code = pattern_version_code.findall(output.decode('utf-8'))[0]
    print("安装包的 Version code : " + version_code)
    return int(version_code)


def uninstall_app(device_id, package_name):
    for dv in device_id:
        print("正在卸载 %s ......" % dv)
        cmd = "adb -s %s uninstall %s" % (dv, package_name)
        subprocess.check_call(cmd.split()) # subprocess method is well compatible on python3.
    print("卸载完成")


def ask_uninstallation():
    if len(device_id) > 1:
        for dv in device_id:
            apk_version_code = get_apk_version(file_path)
            installed_version_code = get_installed_version([dv], package_name)
            if apk_version_code < int(installed_version_code[0]):
                print("version_code 降级，即将删除已安装的版本！")
                uninstall_app([dv], package_name)
                install_app([dv], file_path)
            elif installed_version_code[0] == "0":
                print("** 设备 %s 上未安装此 App !" % dv)
                install_app([dv], file_path)
            else:
                uninstallation = input('''
是否卸载该设备上已安装的 App ？【请输入编号！】：
1. 卸载，重新安装
2. 覆盖安装（按 ENTER 键也可）
3. 放弃安装
   ''')
                if uninstallation == "1":
                    uninstall_app([dv], package_name)
                    install_app([dv], file_path)
                elif uninstallation == "3":
                    print("已放弃在该设备上安装。")
                    continue
                else:
                    print("将会在该设备上进行覆盖安装！")
                    install_app([dv], file_path)
            print("----------------------------------------")

    elif len(device_id) == 1:
        apk_version_code = get_apk_version(file_path)
        installed_version_code = get_installed_version(device_id, package_name)
        if apk_version_code < int(installed_version_code[0]):
            print("version_code 降级，即将删除已安装的版本！")
            uninstall_app(device_id, package_name)
        elif installed_version_code[0] == "0":
            print("** 设备 %s 上未安装此 App !" % device_id[0])
        else:
            uninstallation = input('''
是否卸载该设备上已安装的 App ？【请输入编号！】：
1. 卸载，重新安装
2. 覆盖安装（按 ENTER 键也可）
3. 放弃安装
   ''')
            if uninstallation == "1":
                uninstall_app(device_id, package_name)
                install_app(device_id, file_path)
            elif uninstallation == "3":
                print("已放弃在该设备上安装，退出脚本运行。")
                exit()
            else:
                print("将会在该设备上进行覆盖安装！")
                install_app(device_id, file_path)

def install_app(device_id, file_path):
    for dv in device_id:
        print("正在安装 %s ......" % dv)
        cmd = "adb -s %s install -r %s" % (dv, file_path)
        subprocess.check_call(cmd.split()) # split method is supported for multi PC OS.
    print("安装完成")


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
    print("未找到相关的 build ，请先手动输入 build 号下载一次")
    sys.exit(1)


if __name__ == "__main__":

    server = Jenkins(jenkins_url, username, password)
    job_instance = server.get_job(job_name)

    print("----------------------------------------")
    if build=="lastSuccessfulBuild":
        last_good_build = job_instance.get_last_good_build()
        build_number = last_good_build.get_number()
        print("最新的 build 号是 #" + str(build_number))
    elif "." in build:
        build_number = get_build_number_from_map(app, build)
    else:
        build_number = build

    artifact_instance = get_artifact_instance(job_instance, build_number)
    print("----------------------------------------")
    # file_path = download_apk(build_number, artifact_instance)
    file_path = os.path.join(download_path, app, str(build_number), artifact_instance.filename)
    if os.path.exists(file_path):
        print("安装包已经存在，文件路径：" + file_path)
        do_continue = input("是否继续后续操作？（按 任意键 继续； N 或 n 退出脚本）：")
        if do_continue in ("N", "n"):
            print("已退出脚本运行。")
        else:
            print("----------------------------------------")
            device_id = set_device_id()
            print("----------------------------------------")

            ask_uninstallation()
    else:
        file_path = download_apk(build_number, artifact_instance)
        print("----------------------------------------")
        device_id = set_device_id()
        print("----------------------------------------")

        ask_uninstallation()


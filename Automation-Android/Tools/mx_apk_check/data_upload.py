import os
from xml.dom.minidom import parse
import xml.dom.minidom
import subprocess
import re
import requests
import sys
import traceback

if len(sys.argv) < 6:
    sys.exit()
build_num = sys.argv[1]
parent_build_num = sys.argv[2]
parent_job_name = sys.argv[3]
branch_name = sys.argv[4]
revision = sys.argv[5]


def get_package_info(apk):
    cmd = "aapt dump badging %s" % apk
    result = subprocess.getoutput(cmd)
    pattern_package_name = re.compile(r'name=\'(\S*)\'')
    pattern_version_code = re.compile(r'versionCode=\'(\S*)\'')
    pattern_version_name = re.compile(r'versionName=\'(\S*)\'')
    pattern_native_code = re.compile(r'native-code: \'(\S*)\'')
    package_name = pattern_package_name.findall(result)[0]
    version_code = pattern_version_code.findall(result)[0]
    version_name = pattern_version_name.findall(result)[0]
    native_code_result = pattern_native_code.findall(result)
    if len(native_code_result) > 0:
        native_code = native_code_result[0]
    else:
        native_code = "Not Found"
    return package_name, version_code, version_name, native_code


def get_package_type(apk):
    if "debug" in apk:
        return "debug"
    if "pre" in apk:
        return "pre"
    else:
        return "release"


class Build:
    def __init__(self, build_num, parent_build_num, parent_job_name):
        self.build_path = f"/Volumes/ZenMX_RAID/Jenkins_Home/jobs/{parent_job_name}/builds/{parent_build_num}/"
        self.xml = self.get_xml()
        # self.xml = "/Users/xin.xu/Desktop/build6821.xml"
        self.apks = self.get_apks()
        self.branch_name = branch_name
        self.revision = revision
        self.apk_type = ""
        self.build_num = build_num
        self.parent_build_num = parent_build_num
        self.parent_job_name = parent_job_name
        self.apk_size = ""
        self.timestamp = ""

    def get_xml(self):
        xml = self.build_path + "build.xml"
        print(xml)
        if os.path.exists(xml):
            return xml
        return ""

    def get_apks(self):
        apks = []
        for root, dirs, files in os.walk(self.build_path):
            for file in files:
                if file.endswith(".apk"):
                    apks.append(os.path.join(root, file))
        return apks

    def parse_xml(self):
        if not self.xml:
            print("xml文件不存在")
            return
        # 使用minidom解析器打开 XML 文档
        DOMTree = xml.dom.minidom.parse(self.xml)
        collection = DOMTree.documentElement

        # 解析打包时间
        timestamp_node = collection.getElementsByTagName("timestamp")[0]
        self.timestamp = timestamp_node.firstChild.data

    def upload(self):
        if not self.branch_name or not self.revision:
            print(self.branch_name)
            print(self.revision)
            print("信息不全，不进行上报")
            return
        for apk in self.apks:
            for black_word in ["jiraReport", "fireDebug", "ApkGuard", "bundle", "direct"]:
                if black_word in apk:
                    print(f"{black_word}类型的包，不需要上传信息")
                    break
            else:
                apk_size = str(os.stat(apk).st_size)
                apk_type = get_package_type(apk)
                package_name, version_code, version_name, native_code = get_package_info(apk)
                data = {
                    "fileName": apk.split("/")[-1],
                    "branchName": self.branch_name,
                    "revision": self.revision,
                    "packageName": package_name,  # 传入com.mxtech.videoplayer.ad or其他
                    "versionCode": version_code,
                    "versionName": version_name,
                    "nativeCode": native_code,  # 传入:armeabi-v7a、arm64-v8a、x86、x86_64
                    "packageType": apk_type,  # 传入：debug、pre、release
                    "buildNumber": self.build_num,
                    "parentBuildNumber": self.parent_build_num,
                    "parentJobName": self.parent_job_name,
                    "fileSize": apk_size,
                    "timeStamp": self.timestamp  # 传入毫秒时间戳数据
                }
                headers = {
                    "Content-Type": "application/json"
                }
                url = "http://qatest-monitor.mxplay.com/energy/app_info/insert"
                response = requests.post(url, headers=headers, json=data)
                print(response.request.body)
                print(response.text)

    def run(self):
        self.parse_xml()
        self.upload()


if __name__ == "__main__":
    try:
        build = Build(build_num, parent_build_num, parent_job_name)
        build.run()
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

# for i in range(4608, 6827):
#     print(i)
#     build_path = f"/Volumes/ZenMX_RAID/Jenkins_Home/jobs/MXVP_Major_Ad_Client/builds/{i}/"
#     if not os.path.exists(build_path):
#         continue
#     build = Build("MXVP_Major_Ad_Client", str(i))
#     build.run()

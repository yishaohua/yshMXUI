# -*- coding:utf-8 -*-
import sys
import getopt
import re
import os
import time
import subprocess
import requests
from global_config import *

opts, args = getopt.getopt(sys.argv[1:], "", ["file=", "scope="])
apk = ""
scope = ""
for op, value in opts:
    if op == "--file":
        apk = value
    if op == "--scope":
        scope = value

temp_folder = './temp_folder'


def get_package_info():
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


def is_target_package(package_name):
    if package_name in PERMISSIONS.keys():
        return True
    else:
        return False


def get_cpu_arch():
    if "x86" in apk:
        return "x86"
    else:
        return "neon"


def version_code_check(package_name, cpu_arch, native_code, version_code):
    flag = True
    if package_name in VERSION_CODE_CHECK_BLACK_LIST or native_code == "Not Found":
        print("[N/A] No need check version code prefix")
        return flag

    prefix = VERSION_CODE_PREFIX.get(package_name, None).get(cpu_arch, None).get(native_code, None)
    if version_code.startswith(prefix):
        print("[Pass] Version Code Prefix Check")
    else:
        print("[Fail] Version Code Prefix Check")
        print("[Fail] Version Code Prefix Should Be %s" % prefix)
        flag = False
    return flag


def virus_check():
    flag = True
    headers = {
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br',
        'accept-ianguage': 'en-US,en;q=0.9,es;q=0.8',
        'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'content-type': 'application/json; charset=utf-8',
        'cache-control': 'max-age=0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'referer': 'https://www.virustotal.com/',
        'x-tool': 'vt-ui-main',
        'x-app-version': '20201026t122946',
        'user-agent': 'Mozilla/5.0(Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
        'x-vt-anti-abuse-header': 'MTc0MjQ4Mzg2MjctWkc5dWRDQmlaU0JsZG1scy0xNjAzNzY4NTc4LjU1Mw=='
    }
    url = 'https://www.virustotal.com/ui/files/upload_url'
    session = requests.session()
    try:
        upload_url_response = session.get(url, headers=headers)
    except ConnectionError:
        return flag
    upload_url_json = upload_url_response.json()
    upload_url = upload_url_json.get("data", None)
    if not upload_url:
        print("wrong format!")
        print(upload_url_json)
        return False
    (path, filename) = os.path.split(apk)
    files = {"file": (filename, open(apk, "rb"), "application/vnd.android.package-archive"), "filename": (None, filename)}

    print("Uploading apk to virustotal ...")
    del headers['content-type']
    data_id_response = session.post(upload_url, files=files, headers=headers)
    data_id_json = data_id_response.json()
    data_id = data_id_json["data"]["id"]

    print("Checking the virus scan result ...")
    check_url = "https://www.virustotal.com/ui/analyses/" + data_id
    headers['content-type'] = 'application/json; charset=utf-8'
    status = True
    count = 0
    while status:
        check_response = session.get(check_url, headers=headers)
        check_result_json = check_response.json()
        result = check_result_json["data"]["attributes"]["status"]
        if result == "completed":
            harmless = check_result_json["data"]["attributes"]["stats"]["harmless"]
            malicious = check_result_json["data"]["attributes"]["stats"]["malicious"]
            suspicious = check_result_json["data"]["attributes"]["stats"]["suspicious"]
            sha256 = check_result_json["meta"]["file_info"]["sha256"]
            if harmless > 0 or malicious > 0 or suspicious > 0:
                print("[Fail] VirusTotal detection: %s harmless, %s malicious, %s suspicious" % (
                str(harmless), str(malicious), str(suspicious)))
                flag = False
            else:
                print("[Pass] VirusTotal scan")
            print("VirusTotal report link: https://www.virustotal.com/#/file/%s/detection" % sha256)
            status = False
        else:
            time.sleep(5)
            count = count + 1
            if count == 240:
                status = False
                print("[Fail] VirusTotal scan timeout")
                flag = False

    return flag


def permisson_check(package_name):
    cmd = "aapt dump permissions %s" % apk
    result = subprocess.getoutput(cmd)
    pattern = re.compile(r'name=\'(\S*)\'')
    permissions_actual = pattern.findall(result)
    permissions_expected = PERMISSIONS[package_name]
    flag = True
    for permission in permissions_actual:
        if permission not in permissions_expected:
            print("[Fail] Additional Permission Found: %s" % permission)
            flag = False
    if flag:
        print("[Pass] Permission Check")

    return flag


def textrel_check(native_code, package_name):
    flag = True
    if package_name in TEXTREL_CHECK_BLACK_LIST:
        print("[N/A] No need check TEXTREL")
        return flag

    if not os.path.exists(temp_folder):
        print("[Fail] TEXTREL Check")
        print("[Fail] Does not find the unzip folder of apk file")
        flag = False
        return flag

    lib_path = os.path.join(temp_folder, 'lib', native_code)
    if not os.path.exists(lib_path):
        print("[Fail] TEXTREL Check")
        print(f"[Fail] Does not find the native code folder of apk file, {lib_path}")
        flag = False
        return flag

    dirs = os.listdir(lib_path)
    for file in dirs:
        if os.path.getsize(os.path.join(lib_path, file)) == 0:
            continue

        # print(file
        cmd1 = "./x86_64-linux-android-readelf -d %s" % os.path.join(lib_path, file)
        cmd2 = "grep TEXTREL"
        result1 = subprocess.Popen(cmd1.split(), stdout=subprocess.PIPE)
        result2 = subprocess.Popen(cmd2.split(), stdin=result1.stdout, stdout=subprocess.PIPE)
        (output, error) = result2.communicate()
        if "TEXTREL" in str(output):
            flag = False
            print("[Fail] TEXTREL Check")
            print("[Fail] Found TEXTREL")
            print(file)
            print(output)

    if flag:
        print("[Pass] TEXTREL Check")

    return flag


def manifest_check(package_name):
    flag = True
    switch_mode = {
        '(type 0x10)0x0': 'standard',
        '(type 0x10)0x2': 'singleTask',
    }
    if package_name == 'com.mxtech.videoplayer.ad':
        cmd = "aapt dump xmltree %s AndroidManifest.xml" % apk
        result = subprocess.getoutput(cmd)
        activity_name = ""
        for line in result.splitlines():
            if "A: android:name" in line:
                pattern = re.compile(r'=\"(\S*)\"')
                activity_name = ''.join(pattern.findall(line))
            if ("A: android:launchMode" in line) and ("(type 0x10)0x1" not in line):
                # flag = False
                pattern = re.compile(r'=(.*)')
                launch_mode = ''.join(pattern.findall(line))
                if activity_name not in LAUNCH_MODE_CHECK_BLACK_LIST:
                    print(f"[{activity_name}] LaunchMode is {switch_mode.get(launch_mode)}")
    else:
        print("[N/A] No need check MANIFEST")
    return flag


def get_apk_size():
    file_stats = os.stat(apk)
    return file_stats.st_size


if __name__ == "__main__":
    flag = True
    cpu_arch = get_cpu_arch()
    package_name, version_code, version_name, native_code = get_package_info()
    print("==============================")
    print("Package Name: " + package_name)
    print("Version Code: " + version_code)
    print("Version Name: " + version_name)
    print("CPU arch: " + cpu_arch)
    print("Native_code: " + native_code)
    print("==============================")
    if not is_target_package(package_name):
        print(f"Unknown package: {package_name}, exit")
        sys.exit(2)
    if not version_code_check(package_name, cpu_arch, native_code, version_code):
        flag = False
    print("==============================")
    if not permisson_check(package_name):
        flag = False
    print("==============================")
    if not textrel_check(native_code, package_name):
        flag = False
    print("==============================")

    if scope == "full":
        if not virus_check():
            flag = False
        print("==============================")

    if not manifest_check(package_name):
        flag = False
    print("==============================")

    if not flag:
        sys.exit(1)

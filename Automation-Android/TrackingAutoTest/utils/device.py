import subprocess
import sys

import uiautomator2
import os
import time


class Device:

    def __init__(self, device_id, package_name):
        self.device_id = device_id
        self.package_name = package_name
        self.ui_automator = uiautomator2.connect_usb(device_id)
        self.init_watcher()
        screen = self.ui_automator.info
        if not screen["screenOn"]:
            self.ui_automator.press('power')
            self.ui_automator.swipe_ext("up", 0.6)
        self.log_file_list = []
        print("初始化Device完成")

    def clear_log(self):
        cmd = f"adb -s {self.device_id} logcat -c"
        print(f"清空设备log, {cmd}")
        os.system(cmd)

    def save_log(self, log_file):
        cmd = f"adb -s {self.device_id} logcat -d -s PRETTY_LOGGER-TK > {log_file}"
        print(f"收集log，{cmd}")
        os.system(cmd)
        # subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        # time.sleep(2)
        # self.log_file_list.append(log_file)

    def add_permission(self):
        PERMISSIONS = {
            'com.mxtech.videoplayer.ad': [
                'android.permission.WRITE_EXTERNAL_STORAGE',
                'android.permission.SYSTEM_ALERT_WINDOW',
                'android.permission.READ_EXTERNAL_STORAGE',
                'android.permission.ACCESS_COARSE_LOCATION',
                'android.permission.ACCESS_FINE_LOCATION',
                'android.permission.CAMERA'
            ],
            'com.next.innovation.takatak': [
                'android.permission.WRITE_EXTERNAL_STORAGE',
                'android.permission.READ_EXTERNAL_STORAGE',
                'android.permission.WAKE_LOCK',
                'android.permission.RECORD_AUDIO',
                'android.permission.CAMERA',
                'android.permission.READ_CONTACTS',
                'android.permission.ACCESS_COARSE_LOCATION'
            ]
        }
        perms_to_add = PERMISSIONS.get(self.package_name, None)
        if perms_to_add:
            for perm in perms_to_add:
                cmd_grant_perm = f'adb -s {self.device_id} shell pm grant {self.package_name} {perm}'
                try:
                    print(cmd_grant_perm)
                    subprocess.getstatusoutput(cmd_grant_perm)
                except subprocess.CalledProcessError as e:
                    print(e)

    def start_app(self):
        self.ui_automator.screen_on()
        self.ui_automator.app_start(self.package_name, stop=True)
        if self.package_name == 'com.next.innovation.takatak':
            self.ui_automator.wait_activity("com.mx.buzzify.activity.HomeActivity", timeout=10)
            if self.text_is_exist("For You", 15):
                pass
            else:
                print("app启动失败")
                sys.exit(2)
        else:
            self.ui_automator.wait_activity("com.mxtech.videoplayer.ad.ActivityWelcomeMX", timeout=10)

    def close_app(self):
        self.ui_automator.app_stop(self.package_name)
        self.press_back()
        self.press_back()

    def set_up(self):
        self.clear_log()
        self.start_app()

    def tear_down(self, log_file):
        self.close_app()
        self.save_log(log_file)

    def click_by_id(self, resource_id, time_out=8):
        if self.ui_automator(resourceId=resource_id).click_exists(timeout=time_out):
            print("----------已点击：%s---------" % resource_id)
            time.sleep(2)
        else:
            print("----------未找到按钮：%s---------" % resource_id)

    def long_click_by_id(self, resource_id, press_time):
        if self.ui_automator(resourceId=resource_id).long_click(press_time, timeout=5):
            print("----------已点击：%s---------" % resource_id)
            time.sleep(2)
        else:
            print("----------未找到按钮：%s---------" % resource_id)

    def click_by_text(self, text):
        if self.ui_automator(text=text).click_exists(timeout=8):
            print("----------已点击：%s---------" % text)
            time.sleep(2)
        else:
            print("----------未找到按钮：%s---------" % text)

    def click_by_xpath(self, xpath_target):
        if self.ui_automator.xpath(xpath_target).click_exists(timeout=8):
            print("----------已点击：%s---------" % xpath_target)
            time.sleep(2)
        else:
            print("----------未找到按钮：%s---------" % xpath_target)

    def swipe_up(self):
        self.ui_automator.swipe_ext("up", 0.6)
        time.sleep(2)

    def follow_creators(self):
        self.ui_automator(resourceId='com.next.innovation.takatak:id/tv_icon_follow').click(timeout=15)

    def click_home(self):
        self.ui_automator(resourceId='com.next.innovation.takatak:id/ivHome').click(timeout=5)
        self.ui_automator.watcher.remove('back_to_home')

    def choose_interests(self):
        self.ui_automator(resourceId='com.next.innovation.takatak:id/in_tag_music').click(timeout=8)
        self.ui_automator(resourceId='com.next.innovation.takatak:id/in_tag_done_btn').click(timeout=8)

    def send_keys(self, resource_id, text):
        self.ui_automator.set_fastinput_ime(True)
        self.ui_automator(resourceId=resource_id).click_exists(timeout=8)
        self.ui_automator.send_keys(text)
        self.ui_automator.set_fastinput_ime(False)

    def send_action(self, text):
        self.ui_automator.send_action(text)

    def resource_is_exist(self, resource_id, timeout=5):
        n = 0
        result = False
        while n < timeout:
            if self.ui_automator(resourceId=resource_id).exists:
                result = True
                break
            else:
                time.sleep(1)
                n += 1
        return result

    def text_is_exist(self, text, timeout=5):
        n = 0
        result = False
        while n < timeout:
            if self.ui_automator(text=text).exists:
                result = True
                break
            else:
                time.sleep(1)
                n += 1
        return result

    def listening_toast(self, text):
        self.ui_automator.toast.get_message(30.0, 35.0, text)

    def press_back(self):
        self.ui_automator.press("back")
        time.sleep(2)

    def tap_follow(self):
        self.ui_automator(resourceId='com.next.innovation.takatak:id/tv_icon_follow').click()
        self.ui_automator.watcher.remove('follow_creators')

    def init_watcher(self):
        # 删除所有的watcher
        self.ui_automator.watcher.reset()
        # 跳过广告的watcher
        self.ui_automator.watcher('skip_ad').when('SKIP AD').click()
        # 权限弹框的watcher
        self.ui_automator.watcher('skip_permission').when('允许').click()
        self.ui_automator.watcher('skip_permission').when('Allow').click()
        # 视频播放失败的watcher
        self.ui_automator.watcher('Failed_to_load_video').when('TAP TO RELOAD').call(self.swipe_up)
        # follow页面关注的watcher
        # self.ui_automator.watcher('follow_creators').when('Trending Creators').when(
        #     xpath='//*[@resource-id="com.next.innovation.takatak:id/tv_icon_follow"]').call(self.tap_follow)
        # self.ui_automator.watcher('back_to_home').when('Trending Creators').when(
        #     xpath='//*[@resource-id="com.next.innovation.takatak:id/suggest_view_pager"]/android.widget.FrameLayout[1]').call(
        #     self.click_home)

    def start_watcher(self):
        # 启动所有watcher
        self.ui_automator.watcher.start(1)

    def stop_watcher(self):
        # 停止所有watcher
        self.ui_automator.watcher.stop()

    def skip_interest(self):
        time.sleep(1)  # 等待兴趣选择页面上下跳动的动画结束
        if self.text_is_exist(text="Choose Your Interests"):
            self.choose_interests()
        else:
            print("没检测到兴趣选择页面")

    def set_online_env(self):
        self.click_by_id('com.next.innovation.takatak:id/ivMe')
        if self.text_is_exist(text="Login to explore more features"):
            self.click_by_id('com.next.innovation.takatak:id/login_setting')
            self.click_by_id('com.next.innovation.takatak:id/settings_tv')
        else:
            self.click_by_id('com.next.innovation.takatak:id/iv_settings')
            self.click_by_id('com.next.innovation.takatak:id/settings_tv')
        self.swipe_up()
        self.click_by_id('com.next.innovation.takatak:id/about_tv')
        self.long_click_by_id('com.next.innovation.takatak:id/version_tv', 1)
        self.click_by_id('com.next.innovation.takatak:id/server_label')
        self.click_by_text('Online')
        self.press_back()

    def skip_rate_popup(self):
        self.click_by_id('com.next.innovation.takatak:id/detail_like')
        if self.text_is_exist(text="Not Now"):
            self.click_by_text("Not Now")
            self.click_by_text("Cancel")
        else:
            print("没检测到评分引导")

    def login(self):
        self.click_by_id('com.next.innovation.takatak:id/ivMe')
        if self.text_is_exist(text="Login to explore more features"):
            self.click_by_text("Facebook")
            time.sleep(10)
        else:
            print("账号已登录")

    def prepare_taka(self):
        print("添加权限")
        self.add_permission()
        self.set_up()
        print("跳过兴趣选择页面")
        self.skip_interest()
        print("更改为线上环境")
        self.set_online_env()
        self.close_app()
        self.set_up()
        print("跳过评分引导")
        self.skip_rate_popup()
        print("登陆Facebook账号")
        self.login()
        self.close_app()

    def prepare_mxplayer(self):
        self.add_permission()

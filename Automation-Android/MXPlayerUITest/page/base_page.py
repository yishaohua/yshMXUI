import logging
import os

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time
import subprocess

from page.handle_black_list import handle_black_list


class BasePage:
    """
    页面的一些通用的操作
    """
    # logging.basicConfig(level=logging.INFO)
    __black_list_H5 = [
        # (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/toolbar']/android.widget.TextView")
    ]

    # # 启动应用后，首次点击takatak后，弹出录制视频语言选择弹窗
    # # 选择录制视频语言弹窗
    # __choose_language = (By.ID, "com.mxtech.videoplayer.ad:id/bottom_panel")
    # # 录制视频语言弹窗 跳过按钮
    # __choose_language_skip = (By.ID, "com.mxtech.videoplayer.ad:id/skip_view")
    # # 录制视频语言弹窗 弹窗标题
    # __choose_language_title = (By.ID, "com.mxtech.videoplayer.ad:id/title")
    # # 录制视频语言弹窗 语言类型 是一组元素
    # __choose_language_option = (By.XPATH, "//*[resource-id='com.mxtech.videoplayer.ad:id/title']/android.widget.LinearLayout")
    # # 录制视频语言弹窗 应用按钮
    # __choose_language_apply = (By.ID, "com.mxtech.videoplayer.ad:id/apply")

    # 下载弹窗 剩余空间文案
    __capacity_left = (By.ID, "com.mxtech.videoplayer.ad:id/capacity_left")
    # 下载视频清晰度列表 共4种，分别为 HD，High，Medium，Low。可以依次获取元素点击
    __resolution_list = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/video_resolution']")
    # 设置默认选项勾选框
    __download_quality_box = (By.ID, "com.mxtech.videoplayer.ad:id/download_quality_box")
    # 立即下载按钮
    __download_button = (By.ID, "com.mxtech.videoplayer.ad:id/download_btn")
    # 暂停下载按钮
    __download_pause = (By.ID, "com.mxtech.videoplayer.ad:id/download_pause")
    # 取消下载按钮
    __download_cancel = (By.ID, "com.mxtech.videoplayer.ad:id/download_cancel")
    # 我的下载查看
    __download_view = (By.ID, "com.mxtech.videoplayer.ad:id/download_view")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_H5_element_and_send_keys(self,locator,keys):
        """
        查看h5的元素并sendkeys
        :return:
        """
        self.form_native_switch_to_H5()
        self.find_element(locator).send_keys(keys)
        self.form_H5_switch_to_native()
        return self

    def click_download_button(self):
        """
        点击画质选择弹窗中 立即下载按钮
        :return:
        """
        self.find_element_and_click(self.__download_button)

    def click_download_and_choose_resolution(self, option):
        """
        选择下载视频清晰度
        :param option: 选择清晰度选项[0-3]，（HD有些没有）HD，High，Medium，Low
        :return:
        """
        # # 获取到剩余存储空间
        # capacity_left = self.find_element_and_get_text(self.__capacity_left)
        # 选择LOW画质
        resolution_list = self.find_elements(self.__resolution_list)
        resolution_list[option].click()
        # 勾选设置为默认
        # self.find_element_and_click(self.__download_quality_box)
        return self

    def is_download_pause_exist(self):
        """
        判断暂停下载按钮是否存在
        :return:
        """
        return self.is_element_exist(self.__download_pause)

    def click_download_cancel(self):
        """
        点击取消下载
        :return:
        """
        self.find_element_and_click(self.__download_cancel)
        return self

    __key_word = {
        # 数字对应的code
        "0": 7, "1": 8, "2": 9, "3": 10, "4": 11, "5": 12, "6": 13, "7": 14, "8": 15, "9": 16,
        "A": 29, "B": 30, "C": 31, "D": 32, "E": 33, "F": 34, "G": 35, "H": 36, "I": 37, "J": 38, "K": 39, "L": 40, "M": 41, "N": 42, "O": 43, "P": 44, "Q": 45, "R": 46, "S": 47, "T": 48, "U": 49, "V": 50, "W": 51, "X": 52, "Y": 53, "Z": 54,
        'a': 29, 'b': 30, 'c': 31, 'd': 32, 'e': 33, 'f': 34, 'g': 35, 'h': 36, 'i': 37, 'j': 38, 'k': 39, 'l': 40, 'm': 41, 'n': 42, 'o': 43, 'p': 44, 'q': 45, 'r': 46, 's': 47, 't': 48, 'u': 49, 'v': 50, 'w': 51, 'x': 52, 'y': 53, 'z': 54,
        'META_ALT_LEFT_ON': 16,
        'META_ALT_MASK': 50,
        'META_ALT_ON': 2,
        'META_ALT_RIGHT_ON': 32,
        'META_CAPS_LOCK_ON': 1048576,
        'META_CTRL_LEFT_ON': 8192,
        'META_CTRL_MASK': 28672,
        'META_CTRL_ON': 4096,
        'META_CTRL_RIGHT_ON': 16384,
        'META_FUNCTION_ON': 8,
        'META_META_LEFT_ON': 131072,
        'META_META_MASK': 458752,
        'META_META_ON': 65536,
        'META_META_RIGHT_ON': 262144,
        'META_NUM_LOCK_ON': 2097152,
        'META_SCROLL_LOCK_ON': 4194304,
        'META_SHIFT_LEFT_ON': 64,
        'META_SHIFT_MASK': 193,
        'META_SHIFT_ON': 1,
        'META_SHIFT_RIGHT_ON': 128,
        'META_SYM_ON': 4,
        'KEYCODE_APOSTROPHE': 75,

        "@": 77,
        'KEYCODE_AT': 77,
        'KEYCODE_BACKSLASH': 73,
        'KEYCODE_COMMA': 55,
        'KEYCODE_EQUALS': 70,
        'KEYCODE_GRAVE': 68,
        'KEYCODE_LEFT_BRACKET': 71,
        'KEYCODE_MINUS': 69,

        ".": 56,
        'KEYCODE_PERIOD': 56,

        'KEYCODE_PLUS': 81,
        'KEYCODE_POUND': 18,
        'KEYCODE_RIGHT_BRACKET': 72,
        'KEYCODE_SEMICOLON': 74,
        'KEYCODE_SLASH': 76,
        'KEYCODE_STAR': 17,

        " ": 62,
        'KEYCODE_SPACE': 62,

        'KEYCODE_TAB': 61,
        # 回车
        'KEYCODE_ENTER': 66,
        'KEYCODE_ESCAPE': 111,
        'KEYCODE_CAPS_LOCK': 115,
        'KEYCODE_CLEAR': 28,
        'KEYCODE_PAGE_DOWN': 93,
        'KEYCODE_PAGE_UP': 92,
        'KEYCODE_SCROLL_LOCK': 116,
        'KEYCODE_MOVE_END': 123,
        'KEYCODE_MOVE_HOME': 122,
        'KEYCODE_INSERT': 124,
        'KEYCODE_SHIFT_LEFT': 59,
        'KEYCODE_SHIFT_RIGHT': 60,
        'KEYCODE_F1': 131,
        'KEYCODE_F2': 132,
        'KEYCODE_F3': 133,
        'KEYCODE_F4': 134,
        'KEYCODE_F5': 135,
        'KEYCODE_F6': 136,
        'KEYCODE_F7': 137,
        'KEYCODE_F8': 138,
        'KEYCODE_F9': 139,
        'KEYCODE_F10': 140,
        'KEYCODE_F11': 141,
        'KEYCODE_F12': 142,
        # 物理返回键
        'KEYCODE_BACK': 4,
        'KEYCODE_CALL': 5,
        'KEYCODE_ENDCALL': 6,
        'KEYCODE_CAMERA': 27,
        'KEYCODE_FOCUS': 80,
        'KEYCODE_VOLUME_UP': 24,
        'KEYCODE_VOLUME_DOWN': 25,
        'KEYCODE_VOLUME_MUTE': 164,
        'KEYCODE_MENU': 82,
        'KEYCODE_HOME': 3,
        'KEYCODE_POWER': 26,
        # 搜索
        'KEYCODE_SEARCH': 84,
        'KEYCODE_NOTIFICATION': 83,
        'KEYCODE_NUM': 78,
        'KEYCODE_SYM': 63,
        'KEYCODE_SETTINGS': 176,
        # 退格键
        'KEYCODE_DEL': 67,
        'KEYCODE_FORWARD_DEL': 112,
        'KEYCODE_NUMPAD_0': 144,
        'KEYCODE_NUMPAD_1': 145,
        'KEYCODE_NUMPAD_2': 146,
        'KEYCODE_NUMPAD_3': 147,
        'KEYCODE_NUMPAD_4': 148,
        'KEYCODE_NUMPAD_5': 149,
        'KEYCODE_NUMPAD_6': 150,
        'KEYCODE_NUMPAD_7': 151,
        'KEYCODE_NUMPAD_8': 152,
        'KEYCODE_NUMPAD_9': 153,
        'KEYCODE_NUMPAD_ADD': 157,
        'KEYCODE_NUMPAD_COMMA': 159,
        'KEYCODE_NUMPAD_DIVIDE': 154,
        'KEYCODE_NUMPAD_DOT': 158,
        'KEYCODE_NUMPAD_EQUALS': 161,
        'KEYCODE_NUMPAD_LEFT_PAREN': 162,
        'KEYCODE_NUMPAD_MULTIPLY': 155,
        'KEYCODE_NUMPAD_RIGHT_PAREN': 163,
        'KEYCODE_NUMPAD_SUBTRACT': 156,
        'KEYCODE_NUMPAD_ENTER': 160,
        'KEYCODE_NUM_LOCK': 143,
        'KEYCODE_MEDIA_FAST_FORWARD': 90,
        'KEYCODE_MEDIA_NEXT': 87,
        'KEYCODE_MEDIA_PAUSE': 127,
        'KEYCODE_MEDIA_PLAY': 126,
        'KEYCODE_MEDIA_PLAY_PAUSE': 85,
        'KEYCODE_MEDIA_PREVIOUS': 88,
        'KEYCODE_MEDIA_RECORD': 130,
        'KEYCODE_MEDIA_REWIND': 89,
        'KEYCODE_MEDIA_STOP': 86,
    }
    # 列出系统现在所安装的所有输入法
    command0 = 'adb shell ime list -s'
    # 打印系统当前默认的输入法
    command1 = 'adb shell settings get secure default_input_method'
    # 切换sogou输入法为当前输入法
    command2 = 'adb shell ime set com.sohu.inputmethod.sogou/.SogouIME'
    # 切换appium输入法为当前输入法
    command3 = 'adb -s RF8M83HHAMY shell ime set io.appium.settings/.UnicodeIME'
    # 切换samsung输入法为当前输入法
    command4 = 'adb -s RF8M83HHAMY shell ime set com.samsung.android.honeyboard/.service.HoneyBoardService'

    # android系统提示信息
    __android_toast = (By.XPATH, "//*[@class='android.widget.Toast']")
    # toast提示信息
    __snackbar_text = (By.ID, "com.mxtech.videoplayer.ad:id/snackbar_text")

    # local访问本地照片、媒体内容和文件弹窗
    # 弹窗的文案
    __local_access_to_file_content_text = (By.ID, "com.android.packageinstaller:id/permission_message")
    # 弹窗的拒绝按钮
    __local_access_to_file_deny_button = (By.ID, "com.android.packageinstaller:id/permission_deny_button")
    # 弹窗的允许按钮
    __local_access_to_file_allow_button = (By.ID, "com.android.packageinstaller:id/permission_allow_button")

    # 超级省流量模式 知道了按钮，video详情页播放触发
    __flow_confirm = (By.ID, "com.mxtech.videoplayer.ad:id/av1_confirm")
    # 超级省流量模式 取消按钮
    __flow_cancel = (By.ID, "com.mxtech.videoplayer.ad:id/av1_cancel")

    # 左上角 返回上一级
    __back_button = (By.XPATH, "//android.widget.ImageButton[@content-desc=\"转到上一层级\"]")
    # 弹窗 允许按钮
    __ok_button = (By.ID, "android:id/button1")
    # 弹窗 取消按钮
    __cancel_button = (By.ID, "android:id/button2")

    def click_back_button(self):
        """
        点击返回按钮
        :return:
        """
        self.find_element_and_click(self.__back_button)
        return self

    def click_ok_button(self):
        """
        点击弹窗中确定按钮
        :return:
        """
        self.find_element_and_click(self.__ok_button)
        return self

    def click_cancel_button(self):
        """
        点击弹窗中取消按钮
        :return:
        """
        self.find_element_and_click(self.__cancel_button)
        return self

    # 切换上下文  本地切换为H5页面
    def form_native_switch_to_H5(self):
        """
        切换上下文 本地切换为H5页面
        :return:
        """
        time.sleep(0.5)
        self.driver.switch_to.context(self.driver.contexts[1])
        return self

    # 切换上下文  H5切换为本地页面
    def form_H5_switch_to_native(self):
        """
        切换上下文 H5页面切换为本地页面
        :return:
        """
        self.driver.switch_to.context(self.driver.contexts[0])
        return self

    def get_local_access_to_file_content_text(self):
        """
        local中访问本地照片、媒体内容和文件弹窗的内容文案
        :return:
        """
        return self.find_element_and_get_text(self.__local_access_to_file_content_text)

    def get_local_access_to_file_deny_button_content_text(self):
        """
        local中访问本地照片、媒体内容和文件弹窗的 拒绝按钮 文案
        :return:
        """
        return self.find_element_and_get_text(self.__local_access_to_file_deny_button)

    def get_local_access_to_file_allow_button_content_text(self):
        """
        local中访问本地照片、媒体内容和文件弹窗的 允许按钮 文案
        :return:
        """
        return self.find_element_and_get_text(self.__local_access_to_file_content_text)

    def click_local_access_to_file_deny_button(self):
        """
        点击 local中访问本地照片、媒体内容和文件弹窗的 拒绝按钮
        :return:
        """
        self.find_element_and_click(self.__local_access_to_file_deny_button)
        return self

    def click_local_access_to_file_allow_button(self):
        """
        点击 local中访问本地照片、媒体内容和文件弹窗的 允许按钮
        :return:
        """
        self.find_element_and_click(self.__local_access_to_file_allow_button)
        return self

    def find_native_element_and_click_by_long_press(self,locator):
        """
        找到本地的元素并通过touchaction进行长按点击
        :param locator:
        :return:
        """
        el = self.find_element(locator)
        TouchAction(self.driver).long_press(el).perform()
        return self

    def find_native_element_and_click_by_touch_action(self,locator):
        """
        找到本地的元素并通过touchaction进行点击
        :param locator:
        :return:
        """
        try:
            el = self.find_element(locator)
            TouchAction(self.driver).tap(el).perform()
            return self
        except Exception as e:
            self.handle_exception()
            el = self.find_element(locator)
            TouchAction(self.driver).tap(el).perform()
            return self

    def find_h5_element_and_click_by_touch_action(self,locator):
        """
        找到H5页面的元素 并通过touchaction进行点击操作
        :param locator:
        :return:
        """
        self.form_native_switch_to_H5()
        el = self.find_element(locator)
        TouchAction(self.driver).tap(el).perform()
        self.form_H5_switch_to_native()

    def find_element_and_press(self, sx, sy):
        """
        查找元素并按照坐标点击
        :param locator:
        :return:
        """
        action = TouchAction(self.driver)
        action.press(x=sx, y=sy).wait(ms=20).release()
        action.perform()
        return self

    def android_toast_is_exist(self):
        """
        判断安卓的toast是否存在
        :return:
        """
        if self.find_elements(self.__android_toast).__len__()>0:
            return True
        else:
            return False

    def get_android_toast_text(self):
        """
        获取安卓的toast
        :return:
        """
        try:
            return self.driver.find_element_by_xpath(self.__android_toast[1]).text
        except:
            # 用户处理元素找不到时候的情况
            self.handle_exception()
            return self.find_element(self.__android_toast).text

    def get_snackbar_text(self):
        """
        获取提示信息
        :return:
        """
        return self.find_element_and_get_text(self.__snackbar_text)

    def get_element_position(self, locator):
        """
        获取一个元素的位置
        :param locator:
        :return:
        """
        return self.find_element(locator).location

    def is_element_exist(self, locator):
        """
        判断元素是否存在，存在返回True，不存在返回False
        :param locator:
        :return:
        """
        logging.info("is exist ele:"+str(locator))
        try:
            self.find_element(locator)
            return True
        except:
            return False

    def swipe(self, start_x, start_y, end_x, end_y, dur):
        """
        滑动一段距离
        :param start_x:初始的x的值
        :param start_y:初始的y的值
        :param end_x:滑动结束的x的值
        :param end_y:滑动结束的y的值
        :param dur:滑动的时间
        :return:
        """
        self.driver.swipe(start_x, start_y, end_x, end_y, duration=dur)

    def find_element_and_click_and_press_code(self, locator, number):
        self.find_element_and_click(locator)
        self.press_keycode(number)


    def slide_next_sheet(self, locator, x_distance):
        """
        向后滑动卡片 一定距离（左右）
        :param locator: 卡片元素
        :param x_distance: 需要滑动x的位移，传一个负数
        :return:
        """
        location = self.get_element_position(locator)
        size = self.get_element_size(locator)
        begin_x = location["x"]
        begin_y = location["y"]
        end_x = size["width"] + begin_x
        end_y = size["height"] + begin_y
        start_x = end_x * 0.9
        start_y = (begin_y + end_y) / 2
        self.swipe(start_x, start_y, start_x + x_distance, start_y, 500)
        return self

    def slide_previous_sheet(self, locator, x_distance):
        """
        向前滑动卡片 一定距离（左右）
        :param locator: 答题卡元素
        :param x_distance: 需要滑动x的位移，传一个正数
        :return:
        """
        location = self.get_element_position(locator)
        size = self.get_element_size(locator)
        begin_x = location["x"]
        begin_y = location["y"]
        end_x = size["width"] + begin_x
        end_y = size["height"] + begin_y
        start_x = end_x * 0.1
        start_y = (begin_y + end_y) / 2
        self.swipe(start_x, start_y, start_x + x_distance, start_y, 500)
        return self

    def slide_up_page(self):
        """
        上滑页面
        :return:
        """
        # 获取当前页面像素
        s = self.get_windows_size()
        width = s['width']
        height = s['height']
        sx = width / 2
        sy = height * 2 / 3
        ey = height / 3
        # 滑动页面
        self.swipe(sx, sy, sx, ey, 500)

    def slide_down_page(self):
        """
        下拉页面
        :return:
        """
        # 获取当前页面像素
        s = self.get_windows_size()
        width = s['width']
        height = s['height']
        sx = width / 2
        sy = height / 3
        ey = height * 2 / 3
        # 滑动页面
        self.swipe(sx, sy, sx, ey, 500)

    def swipe_control(self, locator, x_distance, y_distance):
        """
        滑动
        :param locator:
        :param x_distance:
        :param y_distance:
        :return:
        """
        location = self.get_element_position(locator)
        size = self.get_element_size(locator)
        begin_x = location["x"]
        begin_y = location["y"]
        end_x = size["width"] + begin_x
        end_y = size["height"] + begin_y
        middle_x = (begin_x + end_x) / 2
        middle_y = (begin_y + end_y) / 2
        self.swipe(middle_x, middle_y, middle_x + x_distance, middle_y + y_distance, 500)

    def drag_element(self, el1, el2):
        """
        拖动制定元素
        :param el1:
        :param el2:
        :return:
        """
        el1 = self.find_element(el1)
        el2 = self.find_element(el2)
        TouchAction(self.driver).long_press(el1).move_to(el2).release().perform()

    def get_element_size(self, locator):
        """
        获取一个元素的宽度和高度
        :param locator:
        :return:
        """
        return self.find_element(locator).size

    @handle_black_list
    def find_element(self, locator):
        """
        通过信息寻找元素并返回
        :param locator:
        :return:
        """
        logging.info("find ele: " + str(locator))
        return self.driver.find_element(*locator)

    def find_element_and_click(self, locator):
        """
        找到这个元素并进行点击
        :param locator: (By.ID,"id")
        :return:
        """
        logging.info("find ele and click: " + str(locator))
        return self.find_element(locator).click()

    def find_element_and_send_keys(self, locator, key_words):
        """
        找到这个元素并输入数据
        :param locator: (By.ID,"id")
        :return:
        """
        logging.info(f"send keys ele: {locator}")
        return self.find_element(locator).send_keys(key_words)

    def find_H5_element_and_get_text(self, locator):
        time.sleep(1)
        try:
            self.driver.switch_to.context(self.driver.contexts[1])
            text = self.find_element(locator).text
        except Exception:
            time.sleep(1)
            self.driver.switch_to.context(self.driver.contexts[1])
            text = self.find_element(locator).text

        self.driver.switch_to.context(self.driver.contexts[0])
        return text

    def kill_chromedriver_progress(self):
        """
        杀掉chromedriver进程
        :return:
        """
        subprocess.Popen('taskkill /F /im chromedriver.exe', shell=True, stdout=subprocess.PIPE)
        time.sleep(1)

    def find_H5_element_and_click(self, locator):
        """
        找到H5页面的元素并进行点击操作
        :return:
        """
        try:
            time.sleep(3)
            try:
                print("click h5 ele: "+self.driver.contexts)
                self.driver.switch_to.context(self.driver.contexts[1])
                # print(self.driver.page_source)
                # el = self.find_element(locator)
                els = self.find_element(locator)
            except Exception:
                time.sleep(1)
                self.driver.switch_to.context(self.driver.contexts[1])
                # el = self.find_element(locator)
                els = self.find_element(locator)
            els.click()
            self.driver.switch_to.context(self.driver.contexts[0])
            return self
        except:
            self.handle_exception()
            time.sleep(2)
            self.driver.switch_to.context(self.driver.contexts[1])
            els = self.find_element(locator)
            els.click()
            self.driver.switch_to.context(self.driver.contexts[0])
            return self

    def find_H5_element(self, locator):
        time.sleep(3)
        try:
            print("h5 ele:"+self.driver.contexts)
            self.driver.switch_to.context(self.driver.contexts[1])
            # print(self.driver.page_source)
            # el = self.find_element(locator)
            els = self.find_element(locator)
        except Exception:
            time.sleep(1)
            self.driver.switch_to.context(self.driver.contexts[1])
            els = self.find_element(locator)

        self.driver.switch_to.context(self.driver.contexts[0])
        return els

    def find_H5_elements(self, locator):
        try:
            time.sleep(2)
            try:
                self.driver.switch_to.context(self.driver.contexts[1])
                # print(self.driver.page_source)
                # el = self.find_element(locator)
                els = self.find_elements(locator)
            except Exception:
                time.sleep(1)
                self.driver.switch_to.context(self.driver.contexts[1])
                # el = self.find_element(locator)
                els = self.find_elements(locator)

            self.driver.switch_to.context(self.driver.contexts[0])
            return els
        except:
            self.handle_exception()
            time.sleep(2)
            self.driver.switch_to.context(self.driver.contexts[1])
            els = self.find_elements(locator)
            self.driver.switch_to.context(self.driver.contexts[0])
            return els

    def get_windows_size(self):
        return self.driver.get_window_size()


    def find_element_click_and_send_keys(self, locator, key_words):
        """
        找到这个元素 点击 且输入数据
        :param keys:
        :return:
        """
        logging.info("click and send keys ele:" + str(locator))
        el1 = self.find_element(locator)
        el1.click()
        return el1.send_keys(key_words)

    def find_element_and_get_text(self, locator):
        """
        找到这个元素并获取文案
        :param locator: (By.ID,"id")
        :return:
        """
        logging.info("get text ele: " + str(locator))
        ele = self.find_element(locator)
        return ele.get_attribute("text")


    @handle_black_list
    def find_elements(self, locator):
        """
        找到一组元素
        :param locator: (By.ID,"id")
        :return:
        """
        logging.info("find eles: " + str(locator))
        return self.driver.find_elements(*locator)

    def find_elements_once(self, locator):
        """
        找到一组元素
        :param locator: (By.ID,"id")
        :return:
        """
        logging.info("find_elements_once: " + str(locator))
        return self.driver.find_elements(*locator)

    def find_elements_and_get_text(self, locator):
        """
        找到一组元素并获取文案
        :param locator: (By.ID,"id")
        :return: 返回文案列表
        """
        logging.info("get text eles: " + str(locator))
        ele_list = self.find_elements(locator)
        ele_text = []
        for i in range(len(ele_list)):
            ele_text.append(ele_list[i].text)
        return ele_text

    def press_code(self, keycode):
        """
        传入的是一个代号
        :param keycode:
        :return:
        """
        self.driver.press_keycode(self.__key_word[keycode])

    def press_keycode(self, number):
        """
        在页面选中的文本框中输入 用户想要输入的字符
        :param number:
        :return:
        """
        for n in number:
            self.driver.press_keycode(self.__key_word[n])

    def click_return_button(self):
        """点击返回键"""
        # 点击物理返回
        # self.press_code("KEYCODE_BACK")
        logging.info("back page")
        self.driver.back()
        return self

    def enable_sogouIME(self):
        """
        切换sogou输入法为当前输入法
        :return:
        """
        os.system(self.command2)

    def enable_appium_UnicodeIME(self):
        """
        切换appium输入法为当前输入法
        :return:
        """
        os.system(self.command3)

    def enable_samsungIME(self):
        """
        切换samsung输入法为当前输入法
        :return:
        """
        os.system(self.command4)

    def convert_minutes_to_numbers(self, minutes):
        """
        将时长转化为数字
        :param minutes: 时长，格式 0:09
        :return:
        """
        mins = minutes.split(":")
        num = int(mins[0])*60 + int(mins[1])
        return num

    def list_str_to_lower(self, raw_list):
        """
        把列表中字符串大写转化为小写
        :return:
        """
        for i in range(len(raw_list)):
            if type(raw_list[i]) == 'str':
                print("is str")
                raw_list[i] = raw_list[i].lower()
        return raw_list

    def date_to_timestamp(self, date):
        """
        将2021-11-19 15:40:00格式转化为时间戳
        :return:
        """
        # 转为时间数组
        time_array = time.strptime(date, "%Y-%m-%d %H:%M:%S")
        # 转为时间戳
        time_stamp = int(time.mktime(time_array))
        return time_stamp

    # app 整个页面
    __app_content = (By.ID, "android:id/content")

    def click_app_content(self):
        """
        点击app整个页面
        :return:
        """
        self.find_element_and_click(self.__app_content)
        return self

    # 选择喜爱的歌手弹窗 跳过按钮
    __choose_singers_skip = (By.ID, "com.mxtech.videoplayer.ad:id/skip_view")

    def is_skip_exist(self):
        """
        判断跳过按钮是否存在
        :return:
        """
        return self.is_element_exist(self.__choose_singers_skip)

    def click_choose_language_skip(self):
        """
        点击语言/歌手选择弹窗中跳过按钮
        :return:
        """
        if self.is_element_exist(self.__choose_singers_skip):
            self.find_element_and_click(self.__choose_singers_skip)
        return self

    def close_fullscreen_ad(self):
        """
        关闭点击返回后出现的广告
        :return:
        """
        close_button = (By.XPATH, "//*[@resource-id='close-button-container']")
        self.find_element_and_click(close_button)
        return self

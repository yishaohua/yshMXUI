from time import sleep

from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.local.about_page import AboutPage
from page.local.help_page import HelpPage
from page.local.local_page import LocalPage


class LocalInitPage(BasePage):
    """
    继承一个通用页面
    本地页面
    """
    # 顶部标题文案
    __top_title = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/toolbar']/android.widget.TextView")
    # 个人设置-帮助按钮
    __help_button = (By.ID, "com.mxtech.videoplayer.ad:id/tv_help")

    # 小米11 11系统权限允许
    __xiaomi_permission_button = (By.ID, 'com.lbe.security.miui:id/permission_allow_button')
    # mumu 6系统权限允许
    __mumu_permission_button = (By.ID, 'com.android.packageinstaller:id/permission_allow_button')

    # 小米11 11系统 存储权限设置
    __xiaomi_storage_permission = (By.ID, "com.mxtech.videoplayer.ad:id/storage_permission_accept")
    # mxplayer 文件访问权限列表
    __mxplayer_item = (By.XPATH, '//android.widget.LinearLayout[@content-desc="MX 播放器"]/android.widget.LinearLayout[2]')
    # 允许修改系统设置权限
    __switch = (By.ID, "android:id/switch_widget")

    def modify_mcc(self):
        """
        启动app后修改mcc
        :return:
        """
        self.click_permission_button()
        self.click_back_button()
        self.click_help_button()
        HelpPage(self.driver).click_about_button()
        # 显式等待1秒，解决偶尔弹窗定位不到的问题
        sleep(1)
        AboutPage(self.driver).click_tool_bar()
        return LocalPage(self.driver)

    def click_permission_button(self):
        """
        点击允许权限按钮
        :return:
        """
        # 小米11，11系统
        self.find_element_and_click(self.__xiaomi_permission_button)
        # 华为p10 mumu模拟器，6系统
        # self.find_element_and_click(self.__mumu_permission_button)
        return self

    def click_help_button(self):
        """
        点击帮助按钮
        :return:
        """
        self.find_element_and_click(self.__help_button)
        return HelpPage(self.driver)

    def open_store_settings(self):
        """
        打开存储权限设置，使用debug包时启动使用
        :return:
        """
        if self.is_element_exist(self.__xiaomi_storage_permission):
            self.find_element_and_click(self.__xiaomi_storage_permission)
            self.find_element_and_click(self.__mxplayer_item)
            self.find_element_and_click(self.__switch)
            self.click_return_button()
            self.click_return_button()
        return LocalPage(self.driver)

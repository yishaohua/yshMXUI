from time import sleep

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from page.base_page import BasePage


class AboutPage(BasePage):
    """
    继承一个通用页面
    个人设置--帮助页面
    """

    # 标题栏
    __tool_bar = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/toolbar']/android.widget.TextView")
    # mcc文本框
    __mcc_edit_text = (By.ID, "com.mxtech.videoplayer.ad:id/content")
    # mcc文本框提交按钮
    __mcc_submit_button = (By.ID, "com.mxtech.videoplayer.ad:id/confirm")

    def click_tool_bar(self):
        """
        点击关于按钮
        :return:
        """
        for i in range(15):
            print(i)
            self.find_element_and_click(self.__tool_bar)
        self.find_element_and_send_keys(self.__mcc_edit_text, "404")
        self.find_native_element_and_click_by_long_press(self.__mcc_submit_button)
        return self

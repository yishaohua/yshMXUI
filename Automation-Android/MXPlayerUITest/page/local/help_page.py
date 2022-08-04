from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.local.about_page import AboutPage


class HelpPage(BasePage):
    """
    继承一个通用页面
    个人设置--帮助页面
    """

    # 关于按钮
    __about_button = (By.ID, "com.mxtech.videoplayer.ad:id/about")

    def click_about_button(self):
        """
        点击关于按钮
        :return:
        """
        self.find_element_and_click(self.__about_button)
        return AboutPage(self.driver)


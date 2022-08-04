from time import sleep

from selenium.webdriver.common.by import By

from page.video.video_base_page import VideoBasePage


class WatchListPage(VideoBasePage):
    """
    继承一个通用页面  通用页面封装了一些通用方法和异常处理
    video 待看列表
    """
    # 返回按钮/删除页面关闭按钮
    __back_button = (By.XPATH, "//android.widget.ImageButton[@content-desc='转到上一层级']")
    # 页面标题
    __toolbar_title = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/toolbar']/android.widget.TextView")
    # 待看列表视频标题
    __watch_list_title = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/title']")
    # 待看列表视频副标题
    __watch_list_subtitle = (By.ID, "//*[@resouece-id='com.mxtech.videoplayer.ad:id/subtitle']")

    def get_toolbar_title(self):
        """
        获取页面标题
        :return:
        """
        title = self.find_element_and_get_text(self.__toolbar_title)
        return title

    def get_watch_list_title(self):
        """
        获取待看列表视频标题
        :return:
        """
        return self.find_elements_and_get_text(self.__watch_list_title)

    def get_watch_list_count(self):
        """
        获取待看列表视频总数
        :return:
        """
        watch_list = self.find_elements(self.__watch_list_title)
        count = len(watch_list)
        return count


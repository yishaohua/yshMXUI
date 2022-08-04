from selenium.webdriver.common.by import By

from page.video.video_base_page import VideoBasePage
from page.video.video_news_detail_page import VideoNewsDetailPage


class VideoNewsMorePage(VideoBasePage):
    """
    继承一个通用页面  通用页面封装了一些通用方法和异常处理
    video NEWS 查看更多页面
    """
    # 频道标题
    __channels_title = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/title']")
    # 频道按钮
    __channels_button = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/card_view']")

    def get_channels_title(self):
        """
        获取频道名称，一组元素
        :return:
        """
        return self.find_elements_and_get_text(self.__channels_title)

    def click_live_channel(self, option: int):
        """
        点击第一个卡片中
        :param option: 需要点击的 channel 位置所在的下标
        :return:
        """
        cards_list = self.find_elements(self.__channels_button)
        if 0 <= option <= len(cards_list):
            cards_list[option].click()
        else:
            cards_list[0].click()
        return VideoNewsDetailPage(self.driver)



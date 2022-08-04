from selenium.webdriver.common.by import By

from page.video.video_base_page import VideoBasePage
from page.video.video_detail_page import VideoDetailPage


class CardViewMorePage(VideoBasePage):
    """
    卡片 点击查看更多页面
    继承通用页面
    """
    __cards_list = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/rv_flow_fragment']/android.view.ViewGroup")

    def get_cards_count(self):
        """
        获取当前页面卡片数
        :return:
        """
        return len(self.find_elements(self.__cards_list))

    def click_card(self, option):
        """
        点击第 option 个卡片
        :param option:
        :return:
        """
        if option < self.get_cards_count():
            cards = self.find_elements(self.__cards_list)
            cards[option].click()
            return VideoDetailPage(self.driver)
        else:
            print("incorrect option")
from selenium.webdriver.common.by import By

from page.video.buzz_detail_page import BuzzDetailPage
from page.video.video_base_page import VideoBasePage


class VideoBuzzPage(VideoBasePage):
    """
    继承一个通用页面  通用页面封装了一些通用方法和异常处理
    视频 buzz 列表页面
    """
    # 顶部卡片滑动区域
    __card_recycler = (By.ID, "com.mxtech.videoplayer.ad:id/card_recycler_view")
    # 顶部视频类型选择卡片
    __type_view_card = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/text']")
    # 视频卡片 一组元素
    __video_card = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/feed_image_view_card']")

    def slide_type_card(self):
        """
        滑动类型卡片区域
        :return:
        """
        self.slide_next_sheet(self.__card_recycler, -400)
        return self

    def click_type_card(self, option: str):
        """
        点击视频分类卡片
        :param option: 卡片名称
        :return:
        """
        while True:
            current_cards = self.find_elements_and_get_text(self.__type_view_card)
            self.slide_type_card()
            if option in current_cards:
                break
        cards_list = self.find_elements(self.__type_view_card)
        for i in range(len(cards_list)):
            if cards_list[i].text == option:
                cards_list[i].click()
                break
        return self

    def click_video(self, option: int):
        """
        点击播放视频
        :param option: 视频下标，从0开始, 一页只有2个视频
        :return:
        """
        videos = self.find_elements(self.__video_card)
        videos[option].click()
        return BuzzDetailPage(self.driver)
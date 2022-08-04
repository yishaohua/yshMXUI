from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.video.video_news_detail_page import VideoNewsDetailPage
from page.video.video_news_more_page import VideoNewsMorePage


class VideoNewsPage(BasePage):
    """
    继承一个通用页面  通用页面封装了一些通用方法和异常处理
    video NEWS 页面
    """
    # channels 卡片标题
    __channels_card_title = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/card_title']")
    # channels 卡片查看更多
    __channels_more = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/view_more']")
    # banner图片
    __banner_card = (By.ID, "com.mxtech.videoplayer.ad:id/banner_img")
    # 当前banner位置
    __banner_loc = (
    By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/pagination_text']/android.widget.TextView")

    # 首页第一个卡片 live 频道按钮， 一组元素，有4个
    __live_channel_first = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/rv_flow_fragment']/android.widget.LinearLayout[1]"
                                      "/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout")

    def get_channels_card_title(self):
        """
        获取频道卡片标题
        :return:
        """
        return self.find_element_and_get_text(self.__channels_card_title)

    def click_channels_more(self):
        """
        点击频道卡片查看更多
        :return:
        """
        self.find_element_and_click(self.__channels_more)
        return VideoNewsMorePage(self.driver)

    def click_banner(self):
        """
        点击banner标题
        :return:
        """
        self.find_element_and_click(self.__banner_card)
        return VideoNewsDetailPage(self.driver)

    def get_banner_loc(self):
        """
        获取当前banner所在位置
        :return:
        """
        return self.find_element_and_get_text(self.__banner_loc)

    def click_select_banner(self, loc):
        """
        点击指定banner
        :return:
        :param: loc: 点击第 loc 个banner
        """
        while True:
            # 如果需要点击的卡片序号与
            banner_index = int(str(self.get_banner_loc()).split("/")[0])
            if loc != banner_index:
                self.slide_next_sheet(self.__banner_card, -400)
            else:
                self.find_element_and_click(self.__banner_card)
                break
        return VideoNewsDetailPage(self.driver)

    def click_live_channel(self, option: int):
        """
        点击第一个卡片中
        :param option: 首页共4个卡片，option 选项为 [0,3] 中任意一个整数
        :return:
        """
        cards_list = self.find_elements(self.__live_channel_first)
        if 0 <= option <= 3:
            cards_list[option].click()
        else:
            cards_list[0].click()
        return VideoNewsDetailPage(self.driver)

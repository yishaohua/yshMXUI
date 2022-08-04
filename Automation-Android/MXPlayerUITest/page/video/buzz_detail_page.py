from selenium.webdriver.common.by import By

from page.video.video_base_page import VideoBasePage


class BuzzDetailPage(VideoBasePage):
    """
    继承一个通用页面  通用页面封装了一些通用方法和异常处理
    点击 buzz 视频进入详情页面
    """
    # 页面中 添加待看列表按钮，一组元素
    __watchlist_button = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/playdetail_watchlist_container']")
    # 点赞按钮，一组元素
    __like_button = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/playdetail_like_container']")
    # 分享按钮，一组元素
    __share_button = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/playdetail_share_container']")
    # 视频播放区域，一组元素
    __video_play = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/player_layout']")

    def click_watchlist(self, option: int):
        """
        点击第 option 个添加待看列表按钮
        :param option: 元素下标，从0开始
        :return:
        """
        watchlist_buttons = self.find_elements(self.__watchlist_button)
        watchlist_buttons[option].click()
        return self

    def click_like(self, option: int):
        """
        点击第 option 个点赞按钮
        :param option: 元素下标，从0开始
        :return:
        """
        like_buttons = self.find_elements(self.__like_button)
        like_buttons[option].click()
        return self

    def click_share(self, option: int):
        """
        点击第 option 个分享按钮
        :param option: 元素下标，从0开始
        :return:
        """
        share_buttons = self.find_elements(self.__share_button)
        share_buttons[option].click()
        return self

    def click_video(self, option: int):
        """
        点击第 option 个视频
        :param option: 元素下标，从0开始
        :return:
        """
        videos = self.find_elements(self.__video_play)
        videos[option].click()
        return self
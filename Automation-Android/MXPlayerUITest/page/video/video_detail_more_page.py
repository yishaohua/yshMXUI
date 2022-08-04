from selenium.webdriver.common.by import By

from page.base_page import BasePage


class VideoDetailMorePage(BasePage):
    """
    继承一个通用页面  通用页面封装了一些通用方法和异常处理
    视频详情页 查看更多
    """
    # 返回按钮
    __back_button = (By.XPATH, "//android.widget.ImageButton[@content-desc='转到上一层级']")
    # 标题
    __toolbar_title = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/toolbar']/android.widget.TextView")
    # 下载全部按钮
    __download_all = (By.ID, "com.mxtech.videoplayer.ad:id/download_tv")
    # 视频卡片 列表
    __video_cards = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/feed_image_view_card']")
    # 视频卡片 标题列表
    __card_title = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/title']")
    # 视频卡片 二级标题
    __video_card_subtitle = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/subtitle']")
    # 视频卡片 下载按钮
    __video_card_download = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/video_download']")

    def get_title(self):
        """
        获取标题
        :return:
        """
        return self.find_element_and_get_text(self.__toolbar_title)

    def click_download_all(self):
        """
        点击下载全部按钮
        :return:
        """
        self.find_element_and_click(self.__download_all)
        return self

    def get_download_all_text(self):
        """
        获取下载全部按钮文案，当下载全部过程中，显示"取消下载"
        :return:
        """
        return self.find_element_and_get_text(self.__download_all)

    def click_video_card(self):
        """
        点击第一个视频卡片
        :return:
        """
        video_cards = self.find_elements(self.__video_cards)
        video_cards[0].click()
        return self

    def get_video_card_title(self):
        """
        获取视频标题，一组元素
        :return:
        """
        return self.find_elements_and_get_text(self.__card_title)

    def get_video_card_subtitle(self):
        """
        获取视频二级标题
        :return:
        """
        return self.find_elements_and_get_text(self.__video_card_subtitle)

    def get_video_download_button(self):
        """
        获取单个视频下载按钮，一组元素
        :return:
        """
        return self.find_elements(self.__video_card_download)









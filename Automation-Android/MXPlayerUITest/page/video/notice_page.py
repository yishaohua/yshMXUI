from selenium.webdriver.common.by import By

from page.video.video_base_page import VideoBasePage


class NoticePage(VideoBasePage):
    """
    通知页面
    继承通用页面
    """
    # 评论tab
    __comment_tab = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/title_container'/android.widget.FrameLayout[1]]")
    # 视频tab
    __video_tab = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/title_container'/android.widget.FrameLayout[2]]")
    # 游戏tab
    __game_tab = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/title_container'/android.widget.FrameLayout[3]]")
    # 系统tab
    __system_tab = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/title_container'/android.widget.FrameLayout[4]]")
    # tab 名称
    __tab_text = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/inbox_pager_title_text']")

    def click_comment(self):
        """
        点击评论tab
        :return:
        """
        self.find_element_and_click(self.__comment_tab)
        return self

    def click_video(self):
        """
        点击视频tab
        :return:
        """
        self.find_element_and_click(self.__video_tab)
        return self

    def click_game(self):
        """
        点击游戏tab
        :return:
        """
        self.find_element_and_click(self.__game_tab)
        return self

    def click_system(self):
        """
        点击系统tab
        :return:
        """
        self.find_element_and_click(self.__system_tab)
        return self

    def get_all_tab_text(self):
        """
        获取全部tab名称
        :return:
        """
        return self.find_elements_and_get_text(self.__tab_text)


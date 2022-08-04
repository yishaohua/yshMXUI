from time import sleep

from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.game.game_page import GamePage
from page.local.local_page import LocalPage
from page.music.music_page import MusicPage
from page.takatak.takatak_page import TakatakPage
from page.video.video_home_page import VideoHomePage


class Index(BasePage):
    """
    继承一个通用页面  通用页面封装了一些通用方法和异常处理
    导航页面，底部tab
    """
    # 底部的本地tab
    __local_tab = (By.ID, "com.mxtech.videoplayer.ad:id/local")
    # 底部的视频tab
    __video_tab = (By.ID, "com.mxtech.videoplayer.ad:id/online")
    # 视频页顶部logo
    __home_logo = (By.ID, "com.mxtech.videoplayer.ad:id/iv_home_logo")
    # 底部的游戏tab
    __game_tab = (By.ID, "com.mxtech.videoplayer.ad:id/games_tab")
    # 底部的音乐tab
    __music_tab = (By.ID, "com.mxtech.videoplayer.ad:id/music_tab")
    # 底部的TakaTak tab
    __takatak_tab = (By.XPATH, "//*[@text='TakaTak']")

    def to_local_page(self):
        """
        进入到local页面
        :return:
        """
        if self.find_element(self.__local_tab).is_selected():
            return LocalPage(self.driver)
        else:
            self.find_element_and_click(self.__local_tab)
            return LocalPage(self.driver)

    def to_video_home_page(self):
        """
        进入到video_home页面
        :return:
        """
        sleep(2)
        # 如果已经在video页，则不需要点击
        if self.find_element(self.__video_tab).is_selected():
            return VideoHomePage(self.driver)
        else:
            try:
                self.find_element_and_click(self.__video_tab)
            except:
                self.click_app_content()
                sleep(1)
                if self.is_skip_exist():
                    self.click_choose_language_skip()
                self.find_element_and_click(self.__video_tab)
            return VideoHomePage(self.driver)

    def to_game_page(self):
        """
        进入到game页面
        :return:
        """
        if self.find_element(self.__game_tab).is_selected():
            return GamePage(self.driver)
        else:
            self.find_element_and_click(self.__game_tab)
            return GamePage(self.driver)

    def to_music_page(self):
        """
        进入music页面
        :return:
        """
        try:
            self.find_element_and_click(self.__music_tab)
        except:
            # 处理出现语言/歌手选择弹层
            self.click_app_content()
            sleep(1)
            if self.is_skip_exist():
                for i in range(2):
                    # 跳过语言/歌手选择页面
                    self.click_choose_language_skip()
            self.find_element_and_click(self.__music_tab)
        return MusicPage(self.driver)

    def to_takatak_page(self):
        """
        进入Takatak页面
        :return:
        """
        if self.find_element(self.__takatak_tab).is_selected():
            return TakatakPage(self.driver)
        else:
            self.find_element_and_click(self.__takatak_tab)
            return TakatakPage(self.driver)

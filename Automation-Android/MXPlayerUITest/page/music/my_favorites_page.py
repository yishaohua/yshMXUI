
from selenium.webdriver.common.by import By

from page.music.music_base_page import MusicBasePage
from page.music.music_search_page import MusicSearchPage


class MyFavoritesPage(MusicBasePage):
    """
    继承通用页面
    我的最爱、播放列表详情 公用页面
    """
    # 歌曲数
    __songs_num = (By.ID, "com.mxtech.videoplayer.ad:id/tv_song_num")
    # 播放全部
    __play_all = (By.ID, "com.mxtech.videoplayer.ad:id/play_all")
    # 缺省文案
    __default_text = (By.ID, "com.mxtech.videoplayer.ad:id/retry_no_data_text")
    # 搜索按钮
    __search_button = (By.ID, "com.mxtech.videoplayer.ad:id/action_search")

    # 添加歌曲按钮
    __add_songs = (By.ID, "com.mxtech.videoplayer.ad:id/add_songs")

    # 添加歌曲 关闭按钮
    __close_button = (By.ID, "com.mxtech.videoplayer.ad:id/close_img")
    # 添加歌曲 确认选择按钮
    __ok_button = (By.ID, "com.mxtech.videoplayer.ad:id/ok_img")
    # 添加歌曲 弹窗标题
    __add_songs_title = (By.ID, "com.mxtech.videoplayer.ad:id/title")
    # 在线音乐tab
    __live_songs = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/title_container']/android.widget.TextView[1]")
    # 本地音乐tab
    __local_songs = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/title_container']/android.widget.TextView[2]")
    # 本地音乐缺省文案
    __local_songs_default_text = (By.ID, "com.mxtech.videoplayer.ad:id/empty_view")

    # 搜索结果列表 checkbox 一组元素
    __check_box = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/check_box']")
    # 搜索结果列表 live音乐名称 一组元素
    __song_name = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/tv_song_name']")
    # 搜索结果列表 歌手名称 一组元素
    __singer_name = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/tv_singer']")
    # 搜索结果列表 local音乐卡片 标题
    __song_title = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/title']")

    def get_songs_num(self):
        """
        获取收藏歌曲数
        :return:
        """
        return self.find_element_and_get_text(self.__songs_num)

    def get_default_text(self):
        """
        获取缺省文案
        :return:
        """
        return self.find_element_and_get_text(self.__default_text)

    def click_play_all(self):
        """
        点击播放全部按钮
        :return:
        """
        self.find_element_and_click(self.__play_all)
        return self

    def click_search_button(self):
        """
        点击搜索按钮
        :return:
        """
        self.find_element_and_click(self.__search_button)
        return MusicSearchPage(self.driver)

    def click_add_songs(self):
        """
        点击添加歌曲按钮
        :return:
        """
        self.find_element_and_click(self.__add_songs)
        return self

    def click_live_songs(self):
        """
        点击在线音乐tab
        :return:
        """
        self.find_element_and_click(self.__live_songs)
        return self

    def click_local_songs(self):
        """
        点击本地音乐tab
        :return:
        """
        self.find_element_and_click(self.__local_songs)
        return self

    def get_local_default_text(self):
        """
        获取本地音乐默认文案
        :return:
        """
        return self.find_element_and_get_text(self.__local_songs_default_text)

    def click_check_box(self, index):
        """
        点击对应音乐的勾选框
        :param index: 勾选框下标索引
        :return:
        """
        check_box = self.find_elements(self.__check_box)
        if len(check_box) != 0:
            for i in range(len(check_box)):
                if i == index:
                    check_box[i].click()
        return self

    def get_search_songs(self):
        """
        获取到live music搜索结果音频
        :return:
        """
        return self.find_elements_and_get_text(self.__song_name)

    def get_local_search_songs(self):
        """
        获取到local music搜索结果音频
        :return:
        """
        return self.find_elements_and_get_text(self.__song_title)

    def select_one_add_to_playlist(self):
        """
        选择搜索到第一首 添加到播放列表
        :return:
        """
        all_songs = self.get_search_songs()
        print(all_songs)
        self.click_check_box(0)
        self.find_element_and_click(self.__ok_button)
        return self

    def select_songs_add_to_playlist(self, songs_list):
        """
        选择音乐 添加到播放列表
        :return:
        """
        all_songs = self.get_search_songs()
        print(all_songs)
        for i in range(len(all_songs)):
            if all_songs[i] in songs_list:
                self.click_check_box(i)
        self.find_element_and_click(self.__ok_button)
        return self

    def select_all_songs_add_to_playlist(self, songs_len):
        """
        将全部添加到播放列表，如果歌曲数大于5，则只添加5条
        :return:
        """
        for i in range(min(5, songs_len)):
            self.click_check_box(i)
        self.find_element_and_click(self.__ok_button)
        return self

    def click_songs(self):
        """
        点击播放当前页面歌曲前4首
        :return:
        """
        songs_list = self.find_elements(self.__song_title)
        if len(songs_list) == 0:
            print("No songs to click")
        else:
            for i in range(len(songs_list)):
                songs_list[i].click()
        return self






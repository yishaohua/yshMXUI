from time import sleep

from selenium.webdriver.common.by import By

from page.music.music_base_page import MusicBasePage
from page.music.my_favorites_page import MyFavoritesPage


class MyPlaylistPage(MusicBasePage):
    """
    继承通用页面
    我的歌单页面
    """
    # 关闭按钮
    __close_button = (By.ID, "com.mxtech.videoplayer.ad:id/close_img")

    # 创建新播放列表
    __create_playlist = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/recycler_view']/android.view.ViewGroup[1]")
    # 创建新播放列表 添加
    __create_new_button = (By.ID, "com.mxtech.videoplayer.ad:id/icon")
    # 创建新播放列表 文案
    __create_new_title = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/title']/../android.widget.TextView")
    # 播放列表名称 一组元素，第一个是"创建新播放列表文案"，其余为列表名称
    __playlist_name = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/title']")
    # 播放列表 单个列表歌曲数
    __playlist_count = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/subtitle']")

    # 创建播放列表弹窗 标题
    __bottom_create_title = (By.ID, "com.mxtech.videoplayer.ad:id/appCompatTextView2")
    # 创建播放列表弹窗 列表名称输入框
    __list_name_edit = (By.ID, "com.mxtech.videoplayer.ad:id/edit")
    # 创建播放列表弹窗 创建按钮
    __create_button = (By.ID, "com.mxtech.videoplayer.ad:id/tv_create")

    # 歌单选项
    # 重命名歌单
    __playlist_rename = (By.ID, "com.mxtech.videoplayer.ad:id/rename_layout")
    # 删除歌单
    __playlist_delete = (By.ID, "com.mxtech.videoplayer.ad:id/delete_layout")

    def get_create_new_title(self):
        """
        获取创建新播放列表文案, " 创建新播放列表 "
        :return:
        """
        return self.find_element_and_get_text(self.__create_new_title)

    def click_create_new(self):
        """
        点击创建新播放列表
        :return:
        """
        self.find_element_and_click(self.__create_playlist)
        return self

    def get_bottom_create_title(self):
        """
        获取弹窗 创建新播放列表文案, " 创建新播放列表 "
        :return:
        """
        return self.find_element_and_get_text(self.__bottom_create_title)

    def create_playlist(self, playlist_name):
        """
        创建我的歌单
        :return:
        """
        # 点击创建新播放列表
        self.click_create_new()
        # 在创建弹窗中输入播放列表名称
        self.find_element_and_send_keys(self.__list_name_edit, playlist_name)
        # 点击创建
        self.find_element_and_click(self.__create_button)
        # 歌单列表与我的最爱歌单列表 页面布局一致，复用我的最爱歌单列表
        return MyFavoritesPage(self.driver)

    def get_playlist_name(self):
        """
        获取全部歌单名称
        :return:
        """
        playlist = self.find_elements_and_get_text(self.__playlist_name)
        n = len(playlist)
        if n >= 1 and playlist[0] == "创建新播放列表":
            playlist.pop(0)
        return playlist

    def get_one_playlist_name(self, num):
        """
        获取指定歌单名称
        :param num: 歌单索引
        :return:
        """
        playlist = self.get_playlist_name()
        return playlist[num]

    def click_playlist_rename(self):
        """
        点击重命名歌单
        :return:
        """
        self.find_element_and_click(self.__playlist_rename)
        return self

    def delete_playlist(self):
        """
        点击删除歌单
        :return:
        """
        self.find_element_and_click(self.__playlist_delete)
        return self

    def click_one_playlist(self):
        """
        点击一个歌单进入详情页
        :return:
        """
        sleep(1)
        playlists = self.find_elements(self.__playlist_count)
        playlists[0].click()
        return MyFavoritesPage(self.driver)

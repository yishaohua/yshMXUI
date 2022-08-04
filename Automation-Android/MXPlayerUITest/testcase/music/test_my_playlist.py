import logging
import os
from time import sleep

import pytest
import yaml

from page.app import App
from page.logit import logit


class TestMyPlaylist:
    """
    测试music 我的歌单页
    """
    @pytest.fixture(scope='module')
    def create_data(self):
        """
        模块级别，整个模块运行前产生测试数据，测试完成后删除测试数据
        :return:
        """
        logging.info("TestMyPlaylist:create_data before")
        # 创建歌单
        self.my_playlist_page = App.start_logged_in().to_music_page().click_playlist()
        for i in range(2):
            self.my_playlist_page.create_playlist("test_playlist_"+str(i))
            self.my_playlist_page.click_return_button()
        if self.my_playlist_page.is_mini_music_title_exist():
            self.my_playlist_page.close_mini_player()
        App.quit()
        yield
        logging.info("TestMyPlaylist:create_data after")
        # 删除音乐播放列表
        self.playlist_page = App.start_logged_in().to_music_page().click_playlist()
        option_list = self.playlist_page.get_music_option()
        num = len(option_list)
        for i in range(num):
            self.playlist_page.click_music_option(0)
            self.playlist_page.delete_playlist()
        App.quit()

    def setup_class(self):
        logging.info("TestMyPlaylist:setup_class")
        testcase_file = os.path.dirname(__file__).split("testcase")[0] + r"data/testcase_data/music/my_playlist.yaml"
        self.my_playlist_data = yaml.safe_load(open(testcase_file, "r", encoding="utf-8"))
        self.my_playlist_page = App.start_logged_in().to_music_page().click_playlist()

    def setup_method(self, method):
        logging.info("TestMyPlaylist:setup_method")
        # 记录类名和方法名
        logging.info(type(self).__name__ + ":" + method.__name__)

    def teardown_class(self):
        logging.info("TestMyPlaylist:teardown_class")
        App.quit()

    @logit()
    @pytest.mark.usefixtures("create_data")
    def test_search_playlist_text(self):
        """
        测试搜索歌单 默认文案
        :return:
        """
        data_list = self.my_playlist_data["test_search_playlist_text"]
        text = data_list["text"]
        actual_text = self.my_playlist_page.get_search_text()
        assert actual_text == text

    @logit()
    def test_add_playlist(self):
        """
        测试添加歌单
        :return:
        """
        data_list = self.my_playlist_data["test_add_playlist"]
        title = data_list["title"]
        detail_page = self.my_playlist_page.create_playlist(title)
        # 创建成功后返回到歌单列表
        detail_page.click_back_button()
        # 显示等待一秒，解决未获取到播放列表名称的问题
        sleep(1)
        first_playlist = self.my_playlist_page.get_one_playlist_name(0)
        assert first_playlist == title

    @logit()
    def test_search_playlist(self):
        """
        测试搜索歌单
        :return:
        """
        data_list = self.my_playlist_data["test_search_playlist"]
        test_list = data_list["test_list"]
        for i in range(len(test_list)):
            # 点击搜索框
            self.my_playlist_page.click_search_text()
            # 搜索歌单名称
            self.my_playlist_page.search_music(test_list[i])
            # 获取到搜索结果
            playlist = self.my_playlist_page.get_playlist_name()
            if len(playlist) >= 1:
                for j in range(len(playlist)):
                    assert test_list[i].lower() in playlist[j].lower()
            else:
                logging.info("TestMyPlaylist test_search_playlist：未搜索到匹配项")
        self.my_playlist_page.click_search_cancel()

    @logit()
    def test_rename_playlist(self):
        """
        测试重命名歌单
        :return:
        """
        # 获取测试数据
        data_list = self.my_playlist_data["test_rename_playlist"]
        new_name = data_list["new_name"]
        # 点击第一个歌单的选项按钮
        self.my_playlist_page.click_music_option(0)
        # 修改歌单名称
        self.my_playlist_page.click_playlist_rename()
        self.my_playlist_page.rename_playlist(new_name)
        # 获取修改后的歌单名称
        actual_name = self.my_playlist_page.get_one_playlist_name(0)
        assert actual_name == new_name

    @logit()
    def test_delete_playlist(self):
        """
        测试删除第一个歌单
        :return:
        """
        # 删除前歌单名称
        before_list = self.my_playlist_page.get_playlist_name()
        # pop出第一个歌单名称
        before_list.pop(0)
        # 点击第一个歌单的选项按钮 并删除
        self.my_playlist_page.click_music_option(0)
        self.my_playlist_page.delete_playlist()
        # 获取删除后歌单名称
        after_list = self.my_playlist_page.get_playlist_name()
        assert after_list == before_list

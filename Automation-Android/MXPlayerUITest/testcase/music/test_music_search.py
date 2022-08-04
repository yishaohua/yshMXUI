import logging
import os
from time import sleep

import pytest
import yaml

from page.app import App
from page.logit import logit


class TestMusicSearch:
    """
    测试music 搜索页面
    """
    @pytest.fixture()
    def clear_search_edit(self):
        """
        清空搜索框内容
        :return:
        """
        logging.info("TestMusicSearch:clear_search_edit")
        self.music_search_page.click_search_edit_close()

    @pytest.fixture()
    def back_search_page(self):
        """
        返回到搜索结果页
        :return:
        """
        logging.info("TestMusicSearch:back_search_page")
        yield
        sleep(1)
        self.music_search_page.click_return_button()

    @pytest.fixture()
    def close_mini_player(self):
        """
        关闭迷你播放器
        :return:
        """
        logging.info("TestMusicSearch:close_mini_player")
        self.music_search_page.close_mini_player()

    @pytest.fixture()
    def click_cancel_favorite(self, clear_data):
        """
        点击取消最爱
        :return:
        """
        logging.info("TestMusicSearch:click_cancel_favorite")
        self.music_search_page.close_mini_player()
        yield
        # 点击第一个搜索结果音乐选项
        self.music_search_page.click_music_option(0)
        # 点击添加到最爱
        self.music_search_page.click_add_favorite()

    @pytest.fixture(scope='module')
    def clear_data(self):
        """
        模块级别，整个模块运行完后 清除测试数据,删除歌单
        :return:
        """
        logging.info("TestMusicSearch:clear_data")
        yield
        self.playlist_page = App.start_logged_in().to_music_page().click_playlist()
        option_list = self.playlist_page.get_music_option()
        num = len(option_list)
        for i in range(num):
            self.playlist_page.click_music_option(0)
            self.playlist_page.delete_playlist()
        App.quit()

    def setup_class(self):
        logging.info("TestMusicSearch:setup_class")
        testcase_file = os.path.dirname(__file__).split("testcase")[0] + r"data/testcase_data/music/music_search.yaml"
        self.music_search_data = yaml.safe_load(open(testcase_file, "r", encoding="utf-8"))
        self.music_search_page = App.start_logged_in().to_music_page().click_search_bar()

    def setup_method(self, method):
        logging.info("TestMusicSearch:setup_method")
        # 记录类名和方法名
        logging.info(type(self).__name__ + ":" + method.__name__)

    def teardown_class(self):
        logging.info("TestMusicSearch:teardown_class")
        App.quit()

    @logit()
    def test_get_hot_list(self):
        """
        测试热门搜索列表前10
        :return:
        """
        data_list = self.music_search_data["test_get_hot_list"]
        expect_list = data_list["hot_list"]
        actual_list = self.music_search_page.get_hot_list_10()
        assert actual_list == expect_list

    @logit()
    def test_click_hot(self):
        """
        测试点击热门搜索列表
        :return:
        """
        self.music_search_page.click_hot_item()
        assert self.music_search_page.is_view_more_exist()

    @logit()
    @pytest.mark.usefixtures("clear_search_edit")
    def test_search_artist(self):
        """
        测试搜索艺术家
        :return:
        """
        data_list = self.music_search_data["test_search_artist"]
        artist = data_list["artist"]
        self.music_search_page.search_music(artist)
        title_list = self.music_search_page.get_search_title_list()
        assert artist in title_list

    @logit()
    @pytest.mark.usefixtures("clear_search_edit")
    def test_search_music(self):
        """
        测试搜索音乐
        :return:
        """
        data_list = self.music_search_data["test_search_music"]
        music = data_list["music"]
        self.music_search_page.search_music(music)
        title_list = self.music_search_page.get_search_title_list()
        assert music in title_list

    @logit()
    def test_add_play_next(self):
        """
        测试添加到下一首播放
        :return:
        """
        data_list = self.music_search_data["test_add_play_next"]
        toast = data_list["toast"]
        # 点击第一个搜索结果音乐选项
        self.music_search_page.click_music_option(0)
        # 点击添加到下一首播放
        self.music_search_page.click_play_next()
        # 获取到toast提示
        actual_toast = self.music_search_page.get_android_toast_text()
        assert toast in actual_toast

    @logit()
    @pytest.mark.usefixtures("close_mini_player")
    def test_add_play_later(self):
        """
        测试添加到稍后播放
        :return:
        """
        data_list = self.music_search_data["test_add_play_later"]
        toast = data_list["toast"]
        # 点击第一个搜索结果音乐选项
        self.music_search_page.click_music_option(0)
        # 点击添加到稍后播放
        self.music_search_page.click_play_later()
        # 获取到toast提示
        actual_toast = self.music_search_page.get_android_toast_text()
        assert toast in actual_toast

    @logit()
    @pytest.mark.usefixtures("click_cancel_favorite")
    def test_add_favorite(self):
        """
        测试添加到最爱
        :return:
        """
        data_list = self.music_search_data["test_add_favorite"]
        toast = data_list["toast"]
        # 点击第一个搜索结果音乐选项
        self.music_search_page.click_music_option(0)
        # 点击添加到最爱
        self.music_search_page.click_add_favorite()
        # 获取到toast提示
        actual_toast = self.music_search_page.get_android_toast_text()
        assert actual_toast in toast

    @logit()
    def test_add_playlist(self):
        """
        测试点击添加到播放列表中
        :return:
        """
        data_list = self.music_search_data["test_add_playlist"]
        playlist = data_list["playlist"]
        toast = data_list["toast"]
        # 点击第一个搜索结果音乐选项
        self.music_search_page.click_music_option(0)
        # 点击添加到播放列表
        self.music_search_page.click_add_playlist()
        # 创建播放列表并添加
        self.music_search_page.create_playlist_and_add(playlist)
        actual_toast = self.music_search_page.get_android_toast_text()
        assert toast in actual_toast

    @logit()
    @pytest.mark.usefixtures("back_search_page")
    def test_playlist_text(self):
        """
        测试添加到播放列表 播放列表名称显示是否正确
        :return:
        """
        data_list = self.music_search_data["test_playlist_text"]
        playlist = data_list["playlist"]
        # 点击第一个搜索结果音乐选项
        self.music_search_page.click_music_option(0)
        # 点击添加到播放列表
        self.music_search_page.click_add_playlist()
        play_list = self.music_search_page.get_playlist_text()
        assert playlist in play_list

    @logit()
    def test_click_more(self):
        """
        测试点击更多
        :return:
        """
        data_list = self.music_search_data["test_click_more"]
        music = data_list["music"]
        options = data_list["options"]
        # 搜索音乐
        self.music_search_page.search_music(music)
        # 查看更多列表标题
        more_list = self.music_search_page.get_view_more_text()
        # 遍历测试数据，判断更多按钮是否存在在测试数据中
        for option in options:
            for i in range(len(more_list)):
                if more_list[i] == option:
                    self.music_search_page.click_cards_more(i)
                    # 获取到查看更多页面标题，断言
                    actual_title = self.music_search_page.get_more_page_title()
                    text = actual_title.split(" ")[0]
                    assert text in option
                    self.music_search_page.click_return_button()


    # @logit()
    # @pytest.mark.usefixtures("back_search_page")
    # def test_share_text(self):
    #     """
    #     测试点击分享
    #     :return:
    #     """
    #     data_list = self.music_search_data["test_share_text"]
    #     music = data_list["music"]
    #     app = data_list["app"]
    #     # # 搜索音乐
    #     # self.music_search_page.search_music(music)
    #     # 点击第一个搜索结果音乐选项
    #     self.music_search_page.click_music_option(0)
    #     # 点击分享按钮
    #     self.music_search_page.click_share()
    #     actual_app = self.music_search_page.get_share_app_title()
    #     assert app in actual_app

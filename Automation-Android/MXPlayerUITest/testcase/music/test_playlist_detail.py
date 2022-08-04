import logging
import os
import pytest
import yaml

from page.app import App
from page.logit import logit


class TestPlaylistDetail:
    """
    测试music 歌单详情页
    """
    @pytest.fixture(scope='module')
    def clear_data(self):
        """
        模块级别，整个模块运行完成后删除测试数据
        :return:
        """
        logging.info("TestMyPlaylistDetail:clear_data")
        yield
        # 删除音乐播放列表
        self.playlist_page = App.start_logged_in().to_music_page().click_playlist()
        option_list = self.playlist_page.get_music_option()
        num = len(option_list)
        for i in range(num):
            self.playlist_page.click_music_option(0)
            self.playlist_page.delete_playlist()
        App.quit()

    def setup_class(self):
        """
        setup_class 方法，测试类中 所有测试方法前执行一次
        :return:
        """
        logging.info("TestMyPlaylistDetail:setup_class")
        testcase_file = os.path.dirname(__file__).split("testcase")[0] + r"data/testcase_data/music/playlist_detail.yaml"
        self.playlist_detail_data = yaml.safe_load(open(testcase_file, "r", encoding="utf-8"))
        self.playlist_detail_page = App.start_logged_in().to_music_page().click_playlist().create_playlist("playlist_detail")

    def setup_method(self, method):
        """
        setup_method 方法，每个测试方法前执行
        :return:
        """
        logging.info("TestMyPlaylist:setup_method")
        # 记录类名和方法名
        logging.info(type(self).__name__ + ":" + method.__name__)

    def teardown_class(self):
        logging.info("TestMyPlaylistDetail:teardown_class")
        App.quit()

    @logit()
    def test_default_text(self):
        """
        测试页面缺省时文案
        :return:
        """
        data_list = self.playlist_detail_data["test_default_text"]
        text = data_list["text"]
        actual_text = self.playlist_detail_page.get_action_more_title()
        # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        assert actual_text == text

    @logit()
    def test_first_add_songs(self):
        """
        测试空列表首次添加歌曲
        :return:
        """
        # 获取测试用例数据
        data_list = self.playlist_detail_data["test_first_add_songs"]
        search_song = data_list["search_song"]
        toast = data_list["toast"]
        # 点击添加歌曲按钮
        self.playlist_detail_page.click_add_songs()
        # 搜索歌曲 search_song
        self.playlist_detail_page.search_music(search_song)
        # 勾选指定的音乐添加到列表中
        self.playlist_detail_page.select_one_add_to_playlist()
        # 获取到toast提示
        actual_toast = self.playlist_detail_page.get_android_toast_text()
        assert toast in actual_toast

    @logit()
    def test_options_add_songs(self):
        """
        测试options中添加歌曲
        :return:
        """
        data_list = self.playlist_detail_data["test_options_add_songs"]
        test_data = data_list["data"]
        toast = data_list["toast"]
        for i in range(len(test_data)):
            search_song = test_data[i]["search_song"]
            result_songs = test_data[i]["result_songs"]
            # 点击选项中 添加歌曲
            self.playlist_detail_page.add_more_songs()
            # 搜索歌曲 search_song
            self.playlist_detail_page.search_music(search_song)
            # 勾选指定的音乐添加到列表中 result_songs
            self.playlist_detail_page.select_songs_add_to_playlist(result_songs)
            # 获取到toast提示
            actual_toast = self.playlist_detail_page.get_android_toast_text()
            assert toast in actual_toast

    @logit()
    def test_options_add_local_songs(self):
        """
        测试options中添加本地歌曲
        :return:
        """
        # 获取测试数据
        data_list = self.playlist_detail_data["test_options_add_local_songs"]
        toast = data_list["toast"]
        text = data_list["text"]
        # 点击选项中 添加歌曲
        self.playlist_detail_page.add_more_songs()
        # 点击选择本地音乐
        self.playlist_detail_page.click_local_songs()
        # 获取当前本地音乐
        local_songs = self.playlist_detail_page.get_local_search_songs()
        songs_len = len(local_songs)
        if songs_len != 0:
            self.playlist_detail_page.select_all_songs_add_to_playlist(songs_len)
            # 获取到toast提示
            actual_toast = self.playlist_detail_page.get_android_toast_text()
            assert toast in actual_toast
        else:
            # 获取到缺省文案
            actual_text = self.playlist_detail_page.get_local_default_text()
            assert actual_text == text

    @logit()
    @pytest.mark.usefixtures("clear_data")
    def test_clear_all(self):
        """
        测试清除全部歌曲
        :return:
        """
        # 获取测试数据
        data_list = self.playlist_detail_data["test_clear_all"]
        songs_num = data_list["songs_num"]
        # 点击删除全部歌曲
        self.playlist_detail_page.click_action_more()
        self.playlist_detail_page.clear_all()
        actual_num = self.playlist_detail_page.get_songs_num()
        assert actual_num == songs_num


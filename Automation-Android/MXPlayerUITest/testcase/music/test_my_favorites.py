import logging
import os
from time import sleep

import pytest
import yaml

from page.app import App
from page.logit import logit


class TestMyFavorites:
    """
    测试music 我的最爱列表
    """
    @pytest.fixture(scope='module')
    def create_data(self):
        """
        模块级别，整个模块运行前产生测试数据
        :return:
        """
        logging.info("TestMyFavorites:create_data")
        App.start_logged_in().to_music_page().add_to_my_favorites()
        sleep(1)
        App.quit()

    @pytest.fixture()
    def close_mini_player(self):
        """
        关闭迷你播放器
        :return:
        """
        logging.info("TestMyFavorites:close_mini_player")
        if self.my_favorites_page.is_mini_music_title_exist():
            self.my_favorites_page.close_mini_player()

    @pytest.fixture()
    def back_page_two(self):
        """
        返回到最爱页
        :return:
        """
        logging.info("TestMyFavorites:back_page_two")
        yield
        for i in range(2):
            sleep(1)
            self.my_favorites_page.click_return_button()

    @pytest.fixture()
    def back_page(self, create_data):
        """
        返回到最爱页
        :return:
        """
        logging.info("TestMyFavorites:back_page")
        yield
        self.my_favorites_page.click_return_button()

    def setup_class(self):
        logging.info("TestMyFavorites:setup_class")
        testcase_file = os.path.dirname(__file__).split("testcase")[0] + r"data/testcase_data/music/my_favorites.yaml"
        self.my_favorites_data = yaml.safe_load(open(testcase_file, "r", encoding="utf-8"))
        self.my_favorites_page = App.start_logged_in().to_music_page().click_favorite()

    def setup_method(self, method):
        logging.info("TestMyFavorites:setup_method")
        # 记录类名和方法名
        logging.info(type(self).__name__ + ":" + method.__name__)

    def teardown_class(self):
        logging.info("TestMyFavorites:teardown_class")
        App.quit()

    @logit()
    @pytest.mark.usefixtures("back_page")
    def test_my_favorite_title(self):
        """
        测试我的最爱列表标题
        :return:
        """
        data_list = self.my_favorites_data["test_my_favorite_title"]
        title = data_list["title"]
        self.my_favorites_page.click_action_more()
        actual_text = self.my_favorites_page.get_action_more_title()
        assert actual_text == title

    @logit()
    def test_my_favorite_num(self):
        """
        测试我的最爱歌曲数
        :return:
        """
        data_list = self.my_favorites_data["test_my_favorite_num"]
        num_text = data_list["num_text"]
        actual_text = self.my_favorites_page.get_songs_num()
        assert num_text in actual_text

    @logit()
    def test_click_play_all(self):
        """
        测试点击播放全部
        :return:
        """
        # 如果迷你播放器存在的话，先关闭迷你播放器
        # 再点击播放全部
        if self.my_favorites_page.is_mini_music_title_exist():
            self.my_favorites_page.close_mini_player()
            self.my_favorites_page.click_play_all()
        else:
            self.my_favorites_page.click_play_all()
        # 断言迷你播放器是否存在
        assert self.my_favorites_page.is_mini_music_title_exist()

    @logit()
    @pytest.mark.usefixtures("back_page_two")
    def test_click_search(self):
        """
        测试点击搜索按钮
        :return:
        """
        search_page = self.my_favorites_page.click_search_button()
        assert search_page.is_search_text_exist()

    @logit()
    @pytest.mark.usefixtures("close_mini_player")
    def test_play_next(self):
        """
        测试接下来播放
        :return:
        """
        data_list = self.my_favorites_data["test_play_next"]
        toast = data_list["toast"]
        # 点击更多操作按钮
        self.my_favorites_page.click_action_more()
        # 点击接下来播放
        self.my_favorites_page.click_play_next()
        # 获取到toast提示
        actual_toast = self.my_favorites_page.get_android_toast_text()
        assert toast in actual_toast

    @logit()
    def test_clear_all(self):
        """
        测试删除全部歌曲
        :return:
        """
        data_list = self.my_favorites_data["test_clear_all"]
        num_text = data_list["num_text"]
        # 点击更多操作按钮
        self.my_favorites_page.click_action_more()
        # 点击清除全部
        self.my_favorites_page.clear_all()
        actual_text = self.my_favorites_page.get_songs_num()
        assert actual_text == num_text

    @logit()
    def test_no_data_text(self):
        """
        测试无歌曲时缺省文案
        :return:
        """
        data_list = self.my_favorites_data["test_no_data_text"]
        text = data_list["text"]
        actual_text = self.my_favorites_page.get_default_text()
        assert actual_text == text


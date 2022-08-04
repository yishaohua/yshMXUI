import logging
import os

import pytest
import yaml

from page.app import App
from page.logit import logit


class TestVideoSearch:
    """
    测试video 顶部搜索
    """
    @pytest.fixture()
    def back_search(self):
        """
        返回到搜索页视频
        :return:
        """
        logging.info("TestVideo:back_search")
        yield
        self.video_search_page.click_return_button()

    def setup_class(self):
        # 获取测试数据文件名
        testcase_file = os.path.dirname(__file__).split("testcase")[0] + r"data/testcase_data/video/video_search.yaml"
        # 获取测试数据内容
        self.video_search_data = yaml.safe_load(open(testcase_file, "r", encoding="utf-8"))
        try:
            self.video_search_page = App.start_logged_in().to_video_home_page().click_search_button()
        except:
            App.quit()
            self.video_search_page = App.start_logged_in().to_video_home_page().click_search_button()

    def setup_method(self, method):
        logging.info("TestVideoSearch:setup_method")
        # 记录类名和方法名
        logging.info(type(self).__name__+":"+method.__name__)

    def teardown_class(self):
        logging.info("TestVideoSearch:teardown_class")
        App.quit()

    @pytest.mark.usefixtures("back_search")
    @logit()
    def test_click_show_card(self):
        """
        测试点击show card
        :return:
        """
        data_list = self.video_search_data["test_click_show_card"]
        title = data_list["title"]
        self.search_show_page = self.video_search_page.get_cover_images_shows(1, 0)
        actual_title = self.search_show_page.get_tool_bar_title()
        assert actual_title == title

    @pytest.mark.usefixtures("back_search")
    @logit()
    def test_click_movies_card(self):
        """
        测试点击movies card
        :return:
        """
        data_list = self.video_search_data["test_click_movies_card"]
        title = data_list["title"]
        self.search_movies_page = self.video_search_page.get_cover_images_movies(1, 1)
        actual_title = self.search_movies_page.get_tool_bar_title()
        assert actual_title == title

    @pytest.mark.usefixtures("back_search")
    @logit()
    def test_click_music_card(self):
        """
        测试点击music card
        :return:
        """
        data_list = self.video_search_data["test_click_music_card"]
        title = data_list["title"]
        self.search_music_page = self.video_search_page.get_cover_images_music(1, 2)
        actual_title = self.search_music_page.get_tool_bar_title()
        assert actual_title == title

    @pytest.mark.usefixtures("back_search")
    @logit()
    def test_click_live_tv_card(self):
        """
        测试点击live tv card
        :return:
        """
        data_list = self.video_search_data["test_click_live_tv_card"]
        title = data_list["title"]
        self.search_live_tv_page = self.video_search_page.get_cover_images_live_tv(1, 3)
        actual_title = self.search_live_tv_page.get_tool_bar_title()
        assert actual_title == title

    @pytest.mark.usefixtures("back_search")
    @logit()
    def test_click_shorts_card(self):
        """
        测试点击shorts card
        :return:
        """
        data_list = self.video_search_data["test_click_shorts_card"]
        title = data_list["title"]
        self.search_shorts_page = self.video_search_page.get_cover_images_shorts(2, 3)
        actual_title = self.search_shorts_page.get_tool_bar_title()
        assert actual_title == title

    @logit()
    def test_get_hot_list(self):
        """
        测试热门列表文案
        :return:
        """
        data_list = self.video_search_data["test_get_hot_list"]
        hot_list_text = self.video_search_page.get_hot_list_text()
        # 对比测试数据与获取到的数据列表是否相同
        assert hot_list_text[:9] == data_list

    @logit()
    def test_search_video(self):
        """
        测试搜索视频结果显示
        :return:
        """
        data_list = self.video_search_data["test_search_video"]
        for data in data_list:
            self.video_search_page.do_search(data)
            assert not self.video_search_page.hot_title_is_exit()

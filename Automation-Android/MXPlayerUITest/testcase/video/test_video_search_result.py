import logging
import os

import pytest
import yaml

from page.app import App
from page.logit import logit


class TestVideoSearchResult:
    """
    测试Video 搜索结果页
    """
    @pytest.fixture()
    def click_all_tab(self):
        """
        返回到搜索页视频
        :return:
        """
        logging.info("TestVideo:click_all_tab")
        yield
        self.search_result_page.click_all_tab()

    @pytest.fixture()
    def search_video(self):
        """
        返回到搜索页视频，再次搜索
        :return:
        """
        logging.info("TestVideo:search_video")
        yield
        self.search_result_page.click_search_edit_delete()
        self.search_result_page.do_search(self.video_name)

    def setup_class(self):
        logging.info("TestVideoSearchResult:setup_class")
        # 获取测试数据文件名
        testcase_file = os.path.dirname(__file__).split("testcase")[0] + r"data/testcase_data/video/video_search_result.yaml"
        # 获取测试数据内容
        self.search_result_data = yaml.safe_load(open(testcase_file, "r", encoding="utf-8"))
        self.video_name = self.search_result_data["search_video"]
        self.search_result_page = App.start_logged_in().to_video_home_page().click_search_button().do_search(self.video_name)

    def setup_method(self, method):
        logging.info("TestVideoSearchResult:setup_method")
        # 记录类名和方法名
        logging.info(type(self).__name__+":"+method.__name__)

    def teardown_class(self):
        logging.info("TestVideoSearchResult:teardown_class")
        App.quit()

    @logit()
    def test_get_search_text(self):
        """
        测试搜索内容
        :return:
        """
        search_text = self.search_result_page.get_search_text()
        assert search_text == self.video_name

    @pytest.mark.usefixtures("click_all_tab")
    @logit()
    def test_click_youtube(self):
        """
        测试点击youtube tab
        :return:
        """
        self.search_result_page.click_youtube_tab()
        # 判断下载开关不存在
        assert not self.search_result_page.download_switch_is_exist()

    @pytest.mark.usefixtures("search_video")
    @logit()
    def test_sort_by_relevance(self):
        """
        测试按照相关性排序
        :return:
        """
        # 点击排序按钮
        self.search_result_page.click_sort_button()
        # 选择relevance
        self.search_result_page.sort_by_relevance()
        video_titles = self.search_result_page.get_video_title()
        # 判断第一个搜索结果名称包含video_name
        assert self.video_name in video_titles[0]

    @pytest.mark.usefixtures("search_video")
    @logit()
    def test_sort_by_recency(self):
        """
        测试按照时间排序
        :return:
        """
        self.search_result_page.click_sort_button()
        # 选择recency
        self.search_result_page.sort_by_recency()
        video_titles = self.search_result_page.get_video_title()
        # 判断第二个搜索结果名称包含video_name
        assert self.video_name in video_titles[1]

    @pytest.mark.usefixtures("search_video")
    @logit()
    def test_choose_language_filter(self):
        """
        测试选择language
        :return:
        """
        data_list = self.search_result_data["test_choose_language_filter"]
        language = data_list["language"]
        # 点击筛选器按钮
        self.search_result_page.click_filter_button()
        # 选择language
        self.search_result_page.click_language()
        # 选择对应language选项 传进去
        self.search_result_page.choose_filter_option(language)
        # 点击应用按钮
        self.search_result_page.click_filter_apply()
        # 获取到filter标题
        filter_title = self.search_result_page.get_one_filter()
        assert filter_title in language

    @pytest.mark.usefixtures("search_video")
    @logit()
    def test_choose_duration_filter(self):
        """
        测试选择duration筛选器
        :return:
        """
        data_list = self.search_result_data["test_choose_duration_filter"]
        duration = data_list["duration"]
        # 点击筛选器按钮
        self.search_result_page.click_filter_button()
        # 选择duration
        self.search_result_page.click_duration()
        # 选择对应duration选项 传进去
        self.search_result_page.choose_filter_option(duration)
        # 点击应用按钮
        self.search_result_page.click_filter_apply()
        # 获取到filter标题
        filter_title = self.search_result_page.get_one_filter()
        assert filter_title in duration

    @pytest.mark.usefixtures("search_video")
    @logit()
    def test_choose_release_year_filter(self):
        """
        测试选择release year筛选器
        :return:
        """
        data_list = self.search_result_data["test_choose_release_year_filter"]
        year = data_list["release year"]
        # 点击筛选器按钮
        self.search_result_page.click_filter_button()
        # 选择release_year
        self.search_result_page.click_release_year()
        # 选择对应release_year选项 传进去
        self.search_result_page.choose_filter_option(year)
        # 点击应用按钮
        self.search_result_page.click_filter_apply()
        # 获取到filter标题
        filter_title = self.search_result_page.get_one_filter()
        assert filter_title in year

    @pytest.mark.usefixtures("search_video")
    @logit()
    def test_multiple_choice(self):
        """
        测试选择多种筛选器
        :return:
        """
        # 获取测试数据
        data_list = self.search_result_data["test_multiple_choice"]
        language = data_list["language"]
        duration = data_list["duration"]
        year = data_list["release year"]
        # 拼接筛选项列表
        expect_data = language + duration + year
        # 点击筛选器按钮
        self.search_result_page.click_filter_button()
        # 选择language
        self.search_result_page.click_language()
        # 选择对应language选项 传进去
        self.search_result_page.choose_filter_options(language)
        # 选择duration
        self.search_result_page.click_duration()
        # 选择对应duration选项 传进去
        self.search_result_page.choose_filter_options(duration)
        # 选择release_year
        self.search_result_page.click_release_year()
        # 选择对应release_year选项 传进去
        self.search_result_page.choose_filter_options(year)
        # 点击应用按钮
        self.search_result_page.click_filter_apply()
        # 获取到filter标题
        filter_title = self.search_result_page.get_filter_title()
        assert filter_title == expect_data

    @logit()
    def test_open_download_switch(self):
        """
        测试打开仅显示可下载视频
        :return:
        """
        # 获取测试数据
        data_list = self.search_result_data["test_open_download_switch"]
        title = data_list["title"]
        self.search_result_page.click_download_content_switch()
        # 获取视频名称列表
        title_list = self.search_result_page.get_video_title()
        assert title in title_list


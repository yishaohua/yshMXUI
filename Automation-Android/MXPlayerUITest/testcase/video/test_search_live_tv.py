import logging
import os
from time import sleep

import yaml

from page.app import App
from page.logit import logit


class TestSearchLiveTV:
    """
    测试video 搜索页点击 live TV 卡片
    """
    def setup_class(self):
        """
        进入video页面，解决每次执行测试用例，重复进入video 导致偶现的setup报错
        :return:
        """
        logging.info("TestSearchLiveTV:setup_class")
        # 获取测试数据文件名
        testcase_file = os.path.dirname(__file__).split("testcase")[0] + r"data/testcase_data/video/search_live_tv.yaml"
        # 获取测试数据内容
        self.search_live_tv_data = yaml.safe_load(open(testcase_file, "r", encoding="utf-8"))
        self.video_search = App.start_logged_in().to_video_home_page().click_search_button()

    def setup_method(self, method):
        logging.info("TestSearchLiveTV:setup_method")
        # 记录类名和方法名
        logging.info(type(self).__name__ + ":" + method.__name__)
        self.search_live_tv_page = self.video_search.get_cover_images_live_tv(1, 3)

    def teardown_method(self):
        logging.info("TestSearchLiveTV:teardown_method")
        self.search_live_tv_page.click_return_button()
        sleep(1)

    def teardown_class(self):
        logging.info("TestSearchLiveTV:teardown_class")
        App.quit()

    @logit()
    def test_choose_language_filter(self):
        """
        测试选择language
        :return:
        """
        data_list = self.search_live_tv_data["test_choose_language_filter"]
        language = data_list["language"]
        # 点击筛选器按钮
        self.search_live_tv_page.click_filter_button()
        # 选择language
        self.search_live_tv_page.click_language()
        # 选择对应language选项 传进去
        self.search_live_tv_page.choose_filter_option(language)
        # 点击应用按钮
        self.search_live_tv_page.click_filter_apply()
        # 获取到filter标题
        filter_title = self.search_live_tv_page.get_filter_title()
        assert language in filter_title

    @logit()
    def test_choose_category_filter(self):
        """
        测试选择category筛选器
        :return:
        """
        data_list = self.search_live_tv_data["test_choose_category_filter"]
        category = data_list["category"]
        # 点击筛选器按钮
        self.search_live_tv_page.click_filter_button()
        # 选择category
        self.search_live_tv_page.click_category()
        # 选择对应category选项 传进去
        self.search_live_tv_page.choose_filter_option(category)
        # 点击应用按钮
        self.search_live_tv_page.click_filter_apply()
        # 获取到filter标题
        filter_title = self.search_live_tv_page.get_filter_title()
        assert category in filter_title

    @logit()
    def test_multiple_choice(self):
        """
        测试选择多种筛选器
        :return:
        """
        # 获取测试数据
        data_list = self.search_live_tv_data["test_multiple_choice"]
        language = data_list["language"]
        category = data_list["category"]
        # 拼接筛选项列表
        expect_data = language + category
        # 点击筛选器按钮
        self.search_live_tv_page.click_filter_button()
        # 选择language
        self.search_live_tv_page.click_language()
        # 选择对应language选项 传进去
        self.search_live_tv_page.choose_filter_options(language)
        # 选择category
        self.search_live_tv_page.click_category()
        # 选择对应category选项 传进去
        self.search_live_tv_page.choose_filter_options(category)
        # 点击应用按钮
        self.search_live_tv_page.click_filter_apply()
        # 获取到filter标题
        filter_title = self.search_live_tv_page.get_filter_title()
        assert filter_title == expect_data

    @logit()
    def test_close_download_switch(self):
        """
        测试默认关闭仅显示可下载视频
        :return:
        """
        text = self.search_live_tv_page.get_download_switch_text()
        assert text == "关闭"

    @logit()
    def test_open_download_switch(self):
        """
        测试打开仅显示可下载视频
        :return:
        """
        self.search_live_tv_page.click_download_content_switch()
        text = self.search_live_tv_page.get_download_switch_text()
        assert text == "开启"

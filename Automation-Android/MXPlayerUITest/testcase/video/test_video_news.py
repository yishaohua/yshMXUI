import logging
import os

import yaml

from page.app import App
from page.logit import logit


class TestVideoNews:
    """
    测试Video news tab页
    """
    def setup_class(self):
        logging.info("TestVideoNews:setup_class")
        # 获取测试数据文件名
        testcase_file = os.path.dirname(__file__).split("testcase")[0] + r"data/testcase_data/video/video_news.yaml"
        self.video_news_data = yaml.safe_load(open(testcase_file, "r", encoding="utf-8"))
        self.video_news_page = App.start_logged_in().to_video_home_page().click_news_tab()

    def setup_method(self, method):
        logging.info("TestVideoNews:setup_method")
        # 记录类名和方法名
        logging.info(type(self).__name__+":"+method.__name__)

    def teardown_class(self):
        logging.info("TestVideoNews:teardown_class")
        App.quit()

    @logit()
    def test_channels_card_title(self):
        """
        测试channels 卡片标题
        :return:
        """
        data_list = self.video_news_data["test_channels_card_title"]
        title = data_list["title"]
        actual_title = self.video_news_page.get_channels_card_title()
        assert actual_title == title

    @logit()
    def test_click_channels_more(self):
        """
        测试点击channels 查看更多
        :return:
        """
        data_list = self.video_news_data["test_click_channels_more"]
        title = data_list["title"]
        more_page = self.video_news_page.click_channels_more()
        actual_title = more_page.get_tool_bar_title()
        assert actual_title == title

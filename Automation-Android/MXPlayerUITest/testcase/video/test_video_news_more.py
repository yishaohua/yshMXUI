import logging
import os

import yaml

from page.app import App
from page.logit import logit


class TestVideoNewsMore:
    """
    测试Video news tab, 查看更多页
    """
    def setup_method(self, method):
        logging.info("TestVideoNewsMore:setup_method")
        # 记录类名和方法名
        logging.info(type(self).__name__ + ":" + method.__name__)
        # 获取测试数据文件名
        testcase_file = os.path.dirname(__file__).split("testcase")[0] + r"data/testcase_data/video/video_news_more.yaml"
        self.video_news_more_data = yaml.safe_load(open(testcase_file, "r", encoding="utf-8"))
        self.video_news_page = App.start_logged_in().to_video_home_page().click_news_tab()
        self.channels_more_page = self.video_news_page.click_channels_more()

    def teardown_method(self):
        logging.info("TestVideoNewsMore:teardown_method")
        App.quit()

    @logit()
    def test_get_channels_title(self):
        """
        测试全部频道列表标题显示
        :return:
        """
        data_list = self.video_news_more_data["test_get_channels_title"]
        titles = data_list["titles"]
        actual_titles = self.channels_more_page.get_channels_title()
        assert actual_titles == titles

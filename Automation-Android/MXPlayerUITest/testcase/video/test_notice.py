import logging
import os

import yaml

from page.app import App
from page.logit import logit


class TestNotice:
    """
    测试Video 通知页
    """
    def setup_class(self):
        logging.info("TestNotice:setup_class")
        # 获取测试数据
        testcase_file = os.path.dirname(__file__).split("testcase")[0] + r"data/testcase_data/video/notice.yaml"
        self.notice_data = yaml.safe_load(open(testcase_file, "r", encoding="utf-8"))
        self.notice_page = App.start_logged_in().to_video_home_page().click_notice_button()

    def setup_method(self, method):
        logging.info("TestNotice:setup_method")
        # 记录类名和方法名
        logging.info(type(self).__name__ + ":" + method.__name__)

    def teardown_class(self):
        logging.info("TestNotice:teardown_class")
        App.quit()

    @logit()
    def test_title(self):
        """
        测试标题
        :return:
        """
        data_list = self.notice_data["test_title"]
        title = data_list["title"]
        actual_title = self.notice_page.get_tool_bar_title()
        assert actual_title == title

    @logit()
    def test_all_tab_text(self):
        """
        测试所有tab名称是否正确
        :return:
        """
        logging.info("TestNotice test_all_tab_text")
        data_list = self.notice_data["test_all_tab_text"]
        tab_list = data_list["tab_list"]
        all_tab_text = self.notice_page.get_all_tab_text()
        assert all_tab_text == tab_list

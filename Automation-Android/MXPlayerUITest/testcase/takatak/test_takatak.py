import logging
import os

import yaml

from page.app import App
from page.logit import logit


class TestTakatak:
    """
    测试Takatak 首页
    """
    def setup_class(self):
        logging.info("TestTakatak:setup_class")
        testcase_file = os.path.dirname(__file__).split("testcase")[0] + r"data/testcase_data/takatak/takatak.yaml"
        self.takatak_data = yaml.safe_load(open(testcase_file, "r", encoding="utf-8"))
        self.takatak_page = App.start_logged_in().to_takatak_page()

    def setup_method(self, method):
        logging.info("TestTakatak:setup_method")
        # 记录类名和方法名
        logging.info(type(self).__name__ + ":" + method.__name__)

    def teardown_class(self):
        logging.info("TestTakatak:teardown_class")
        App.quit()

    @logit()
    def test_click_comment(self):
        """
        测试点击评论
        :return:
        """
        data_list = self.takatak_data["test_click_comment"]
        title = data_list["title"]
        self.takatak_page.click_comment()
        actual_title = self.takatak_page.get_comment_title()
        assert title in actual_title
        self.takatak_page.click_comment_close()

    @logit()
    def test_slide_page(self):
        """
        测试滑动页面
        :return:
        """
        for i in range(3):
            self.takatak_page.slide_up_page()
            name = self.takatak_page.get_publisher_name()
            assert len(name) != 0
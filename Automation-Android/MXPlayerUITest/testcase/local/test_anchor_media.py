import logging
import os

import yaml
from page.app import App
from page.logit import logit


class TestAnchorMedia:
    """
    测试 我的设置--主播媒体列表页面
    """
    def setup_class(self):
        logging.info("TestAnchorMedia:setup_class")
        # 获取测试用例数据
        testcase_file = os.path.dirname(__file__).split("testcase")[0] + r"data/testcase_data/local/anchor_media.yaml"
        self.anchor_media_data = yaml.safe_load(open(testcase_file, "r", encoding="utf-8"))
        self.anchor_media_page = App.start_logged_in().to_local_page().click_back_anchor_media()

    def setup_method(self, method):
        logging.info("TestAnchorMedia:setup_method")
        # 记录类名和方法名
        logging.info(type(self).__name__+":"+method.__name__)

    def teardown_class(self):
        logging.info("TestAnchorMedia:teardown_class")
        App.quit()

    @logit()
    def test_get_username(self):
        """
        测试用户名是否正确
        :return:
        """
        data_list = self.anchor_media_data["test_get_username"]
        name = data_list["name"]
        actual_name = self.anchor_media_page.get_user_name()
        assert actual_name == name

    @logit()
    def test_choose_content_language(self):
        """
        测试修改内容语言
        :return:
        """
        data_list = self.anchor_media_data["test_choose_content_language"]
        toast = data_list["toast"]
        # 修改内容语言，确保在点击video或者其他tab时不弹出语言选择弹窗
        self.anchor_media_page.choose_content_language()
        # actual_toast = self.anchor_media_page.get_snackbar_text()
        actual_toast = self.anchor_media_page.get_android_toast_text()
        assert actual_toast == toast


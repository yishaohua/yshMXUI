import logging
import os
from time import sleep

import pytest
import yaml

from page.app import App
from page.logit import logit


class TestDownload:
    """
    测试Video 下载页
    """
    @pytest.fixture()
    def back_to_download(self):
        """
        返回到下载页
        :return:
        """
        logging.info("TestDownload:back_to_download")
        yield
        self.download_page.click_return_button()

    def setup_class(self):
        logging.info("TestDownload:setup_class")
        # 获取测试数据
        testcase_file = os.path.dirname(__file__).split("testcase")[0] + r"data/testcase_data/video/download.yaml"
        self.download_data = yaml.safe_load(open(testcase_file, "r", encoding="utf-8"))
        self.download_page = App.start_logged_in().to_video_home_page().click_download_button()

    def setup_method(self, method):
        logging.info("TestDownload:setup_method")
        # 记录类名和方法名
        logging.info(type(self).__name__ + ":" + method.__name__)

    def teardown_class(self):
        logging.info("TestDownload:teardown_class")
        App.quit()

    @logit()
    def test_title(self):
        """
        测试标题
        :return:
        """
        data_list = self.download_data["test_title"]
        title = data_list["title"]
        actual_title = self.download_page.get_tool_bar_title()
        assert actual_title == title

    @pytest.mark.usefixtures("back_to_download")
    @logit()
    def test_click_bubble(self):
        """
        测试点击智能下载弹出弹窗
        :return:
        """
        data_list = self.download_data["test_click_bubble"]
        title = data_list["title"]
        self.download_page.click_smart_download()
        # 显示等待1秒，解决获取不到弹窗标题的情况
        sleep(1)
        actual_title = self.download_page.get_smart_download_title()
        assert actual_title == title

    # 需要使用pre包或者release包测试
    # @logit()
    # def test_download_recommend(self):
    #     """
    #     测试下载推荐视频是否成功
    #     :return:
    #     """
    #     # 下载第一个推荐视频
    #     self.download_page.click_download_recommend_btn()
    #     self.download_page.click_download_button()
    #     # 获取视频列表个数
    #     download_count = self.download_page.get_download_list_count()
    #     assert download_count > 0
    #
    # @logit()
    # def test_delete_all(self):
    #     """
    #     测试删除全部下载视频
    #     :return:
    #     """
    #     # 获取删除前视频数
    #     before_count = self.download_page.get_download_list_count()
    #     self.download_page.select_all_video_and_delete(before_count)
    #     # 点击确认下载按钮
    #     self.download_page.click_delete_button()
    #     # 断言缺省文案是否存在
    #     assert self.download_page.is_default_text_exist()




import logging
import os
from time import sleep

import pytest
import yaml

from page.app import App
from page.logit import logit


class TestVideoDetailMore:
    """
    测试Video 视频详情页 查看更多
    """
    @pytest.fixture(scope='module')
    def clear_data(self):
        """
        重置视频下载设置
        :return:
        """
        logging.info("TestVideoDetailMore:clear_data")
        try:
            self.download_page = App.start_logged_in().to_video_home_page().click_download_button()
        except:
            sleep(2)
            print("to download page fail and retry")
            App.quit()
            self.download_page = App.start_logged_in().to_video_home_page().click_download_button()
        # 需要处理点击蒙层
        if self.download_page.is_bubble_exist():
            self.download_page.click_return_button()
        # 如果有视频，则删除视频
        if self.download_page.is_delete_exist():
            self.download_page.select_all_and_delete(1)
            # 点击确认删除
            self.download_page.click_download_delete_button()
        App.quit()
        yield
        self.download_page = App.start_logged_in().to_video_home_page().click_download_button()
        # 如果有视频，则删除视频
        if self.download_page.is_delete_exist():
            self.download_page.select_all_and_delete(1)
            # 点击确认删除
            self.download_page.click_download_delete_button()
        App.quit()

    def setup_class(self):
        logging.info("TestVideoDetailMore:setup_class")
        testcase_file = os.path.dirname(__file__).split("testcase")[0] + r"data/testcase_data/video/video_detail_more.yaml"
        self.video_detail_more_data = yaml.safe_load(open(testcase_file, "r", encoding="utf-8"))
        self.video_detail_more_page = App.start_logged_in().to_video_home_page().click_banner_video().click_view_more()

    def setup_method(self, method):
        logging.info("TestVideoDetailMore:setup_method")
        # 记录类名和方法名
        logging.info(type(self).__name__+":"+method.__name__)

    def teardown_class(self):
        logging.info("TestVideoDetailMore:teardown_class")
        App.quit()

    @logit()
    def test_title(self, clear_data):
        """
        测试标题是否显正确
        :return:
        """
        logging.info("TestVideoDetailMore test_title")
        data_list = self.video_detail_more_data["test_title"]
        expect_title = data_list["title"]
        title = self.video_detail_more_page.get_title()
        assert title == expect_title

    @logit()
    def test_download_one(self):
        """
        测试下载一条视频
        :return:
        """
        # 点击第一个视频的下载按钮
        download_buttons = self.video_detail_more_page.get_video_download_button()
        download_buttons[0].click()
        # 选择下载清晰度，下载视频
        self.video_detail_more_page.click_download_and_choose_resolution(0)
        self.video_detail_more_page.click_download_button()
        # 再次点击下载按钮，如果是有暂停下载按钮存在，则说明点击下载成功
        self.video_detail_more_page.get_video_download_button()[0].click()
        assert self.video_detail_more_page.is_download_pause_exist()
        self.video_detail_more_page.click_download_cancel()

    @logit()
    def test_download_all(self):
        """
        测试下载全部视频
        :return:
        """
        data_list = self.video_detail_more_data["test_download_all"]
        expect_text = data_list["text"]
        # 点击下载全部按钮
        self.video_detail_more_page.click_download_all()
        self.video_detail_more_page.click_download_button()
        # 获取下载全部按钮文案
        text = self.video_detail_more_page.get_download_all_text()
        assert text == expect_text

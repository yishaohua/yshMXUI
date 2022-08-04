import logging
import os
import yaml

from page.app import App
from page.logit import logit


class TestWatchList:
    """
    测试Video 待看列表
    """
    def setup_class(self):
        """
        点击banner图中的添加待看列表按钮，避免没有待看视频 导致没有待看列表按钮
        :return:
        """
        logging.info("TestWatchList:setup_class")
        # 获取测试数据文件名
        testcase_file = os.path.dirname(__file__).split("testcase")[0] + r"data/testcase_data/video/watch_list.yaml"
        # 获取测试数据内容
        self.watch_list_data = yaml.safe_load(open(testcase_file, "r", encoding="utf-8"))
        self.video_page = App.start_logged_in().to_video_home_page()
        # 添加待看视频
        banner_count = self.video_page.get_banner_num()
        self.video_page.add_watch_list(banner_count)
        # 当banner数小于2时，需要另外添加视频
        if banner_count < 2:
            self.video_page.click_movies_tab()
            movie_banner_count = self.video_page.get_banner_num()
            self.video_page.add_watch_list(min(movie_banner_count, 2))
            self.video_page.click_home_tab()
        self.watch_list_page = self.video_page.click_watch_list_more()

    def setup_method(self, method):
        """
        记录日志
        :param method:
        :return:
        """
        logging.info("TestWatchList:setup")
        # 记录类名和方法名
        logging.info(type(self).__name__ + ":" + method.__name__)

    def teardown_class(self):
        logging.info("TestWatchList:teardown_class")
        App.quit()

    @logit()
    def test_title(self):
        """
        测试页面标题
        :return:
        """
        data_list = self.watch_list_data["test_title"]
        title = data_list["title"]
        actual_title = self.watch_list_page.get_toolbar_title()
        assert actual_title == title

    @logit()
    def test_delete_one_video(self):
        """
        测试删除一条待看视频
        :return:
        """
        data_list = self.watch_list_data["test_delete_one_video"]
        toast = data_list["toast"]
        # 获取删除前视频数
        before_count = self.watch_list_page.get_watch_list_count()
        self.watch_list_page.select_one_video_and_delete(before_count)
        # 点击确认删除按钮
        self.watch_list_page.click_delete_button()
        # 获取删除后提示
        actual_toast = self.watch_list_page.get_snackbar_text()
        assert toast in actual_toast

    @logit()
    def test_delete_all_video(self):
        """
        测试删除全部待看视频
        :return:
        """
        data_list = self.watch_list_data["test_delete_all_video"]
        toast = data_list["toast"]
        # 获取删除前视频数
        before_count = self.watch_list_page.get_watch_list_count()
        self.watch_list_page.select_all_video_and_delete(before_count)
        # 点击确认删除按钮
        self.watch_list_page.click_delete_action()
        # 获取删除后提示
        actual_toast = self.watch_list_page.get_snackbar_text()
        assert toast in actual_toast

    @logit()
    def test_default_text(self):
        """
        测试默认文案显示是否正确
        :return:
        """
        data_list = self.watch_list_data["test_default_text"]
        text = data_list["text"]
        actual_text = self.watch_list_page.get_default_text()
        assert actual_text == text

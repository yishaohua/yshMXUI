import logging
import os

import pytest
import yaml
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.app import App
from page.logit import logit


class TestVideo:
    """
    测试Video首页
    """
    @pytest.fixture(scope='module')
    def reset_data(self):
        """
        删除待看列表数据
        :return:
        """
        logging.info("TestVideo:reset_download_settings")
        yield
        # 删除待看列表列表数据
        self.watch_list_page = App.start_logged_in().to_video_home_page().click_watch_list_more()
        self.watch_list_page.select_all_video_and_delete(1)
        self.watch_list_page.click_delete_action()
        App.quit()

    def setup_class(self):
        """
        获取测试数据，进入页面
        :return:
        """
        logging.info("TestVideo:setup_class")
        # 获取测试数据
        testcase_file = os.path.dirname(__file__).split("testcase")[0] + r"data/testcase_data/video/video.yaml"
        self.video_data = yaml.safe_load(open(testcase_file, "r", encoding="utf-8"))
        self.video_page = App.start_logged_in().to_video_home_page()

    def setup_method(self, method):
        logging.info("TestVideo:setup_method")
        # 记录类名和方法名
        logging.info(type(self).__name__+":"+method.__name__)

    def teardown_class(self):
        logging.info("TestVideo:teardown_class")
        App.quit()

    @logit()
    def test_all_tab_text(self, reset_data):
        """
        测试所有tab名称是否正确
        :return:
        """
        data_list = self.video_data["test_all_tab_text"]
        tab_list = data_list["tab_list"]
        all_tab_text = self.video_page.get_all_tab_text()
        assert all_tab_text == tab_list

    @logit()
    def test_add_watch_list(self):
        """
        测试添加banner视频到待看列表
        :return:
        """
        banner_count = self.video_page.get_banner_num()
        self.video_page.add_watch_list(banner_count)
        assert self.video_page.watch_list_is_exist()

    @logit()
    def test_click_home(self):
        """
        测试点击home tab
        :return:
        """
        # 获取测试用例数据
        data_list = self.video_data["test_click_home"]
        expect_card_title = data_list["card_title"]
        # 点击home tab
        self.video_page.click_home_tab()
        self.video_page.slide_up_page()
        cards_title = self.video_page.get_shows_cards()
        assert cards_title[0] in expect_card_title

    @logit()
    def test_slide_down_page(self):
        """
        测试home向下滑动页面
        :return:
        """
        data_list = self.video_data["test_slide_down_page"]
        expect_cards_title = data_list["cards_title"]
        self.video_page.slide_down_page()
        # 获取页面全部卡片标题
        cards_title = self.video_page.get_shows_cards()
        assert cards_title[0] in expect_cards_title

    @logit()
    def test_click_shows(self):
        """
        测试点击 SHOWS tab
        :return:
        """
        data_list = self.video_data["test_click_shows"]
        expect_card_title = data_list["card_title"]
        self.video_page.click_shows_tab()
        cards_title = self.video_page.get_shows_cards()
        assert expect_card_title in cards_title

    @logit()
    def test_click_movies(self):
        """
        测试点击 MOVIES tab
        :return:
        """
        data_list = self.video_data["test_click_movies"]
        expect_card_title = data_list["card_title"]
        self.video_page.click_movies_tab()
        cards_title = self.video_page.get_shows_cards()
        assert expect_card_title in cards_title

    @logit()
    def test_movies_slide_pages(self):
        """
        测试movies上滑页面2次
        :return:
        """
        data_list = self.video_data["test_movies_slide_pages"]
        expect_cards_title = data_list["cards_title"]
        ad_loc = self.video_page.get_ad_locate()
        WebDriverWait(self.video_page, timeout=10, poll_frequency=0.5, ignored_exceptions=None). \
            until(expected_conditions.visibility_of(ad_loc))
        for i in range(2):
            self.video_page.slide_up_page()
        cards_title = self.video_page.get_shows_cards()
        assert cards_title[0] in expect_cards_title

    @logit()
    def test_click_mx_vdesi(self):
        """
        测试点击MX VDESI tab
        :return:
        """
        data_list = self.video_data["test_click_mx_vdesi"]
        expect_card_title = data_list["card_title"]
        self.video_page.click_mx_vdesi_tab()
        cards_title = self.video_page.get_shows_cards()
        assert expect_card_title in cards_title

    @logit()
    def test_click_news_tab(self):
        """
        测试点击NEWS tab
        :return:
        """
        data_list = self.video_data["test_click_news_tab"]
        expect_card_title = data_list["card_title"]
        self.video_page.click_news_tab()
        cards_title = self.video_page.get_shows_cards()
        assert expect_card_title in cards_title

    @logit()
    def test_click_music_tab(self):
        """
        测试点击MUSIC tab
        :return:
        """
        data_list = self.video_data["test_click_music_tab"]
        expect_card_title = data_list["card_title"]
        self.video_page.click_music_tab()
        cards_title = self.video_page.get_shows_cards()
        assert expect_card_title in cards_title

    @logit()
    def test_click_buzz_tab(self):
        """
        测试点击BUZZ tab
        :return:
        """
        self.video_page.click_buzz_tab()
        assert self.video_page.is_buzz_card_list_exist()



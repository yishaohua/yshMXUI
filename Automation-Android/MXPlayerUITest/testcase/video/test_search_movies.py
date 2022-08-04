import logging
import os
from time import sleep

import yaml

from page.app import App
from page.logit import logit


class TestSearchMovies:
    """
    测试video 搜索页点击 Movies 卡片
    """
    def setup_class(self):
        """
        进入video页面，解决每次执行测试用例，重复进入video 导致偶现的setup报错
        :return:
        """
        logging.info("TestSearchMovies:setup_class")
        # 获取测试数据文件名
        testcase_file = os.path.dirname(__file__).split("testcase")[0] + r"data/testcase_data/video/search_movies.yaml"
        # 获取测试数据内容
        self.search_movies_data = yaml.safe_load(open(testcase_file, "r", encoding="utf-8"))
        self.video_search = App.start_logged_in().to_video_home_page().click_search_button()

    def setup_method(self, method):
        logging.info("TestSearchMovies:setup_method")
        # 记录类名和方法名
        logging.info(type(self).__name__ + ":" + method.__name__)
        self.search_movies_page = self.video_search.get_cover_images_movies(1, 1)

    def teardown_method(self):
        logging.info("TestSearchMovies:teardown_method")
        self.search_movies_page.click_return_button()
        sleep(1)

    def teardown_class(self):
        logging.info("TestSearchMovies:teardown_class")
        App.quit()

    @logit()
    def test_queue_items_text(self):
        """
        测试排序列表中选项文案
        :return:
        """
        data_list = self.search_movies_data["test_queue_items_text"]
        items_text = data_list["items"]
        self.search_movies_page.click_queue_button()
        actual_text = self.search_movies_page.get_queue_items_text()
        assert actual_text == items_text
        self.search_movies_page.click_return_button()

    @logit()
    def test_choose_language_filter(self):
        """
        测试选择language
        :return:
        """
        data_list = self.search_movies_data["test_choose_language_filter"]
        language = data_list["language"]
        # 点击筛选器按钮
        self.search_movies_page.click_filter_button()
        # 选择language
        self.search_movies_page.click_language()
        # 选择对应language选项 传进去
        self.search_movies_page.choose_filter_option(language)
        # 点击应用按钮
        self.search_movies_page.click_filter_apply()
        # 获取到filter标题
        filter_title = self.search_movies_page.get_filter_title()
        assert language in filter_title

    @logit()
    def test_choose_genre_filter(self):
        """
        测试选择genre筛选器
        :return:
        """
        data_list = self.search_movies_data["test_choose_genre_filter"]
        genre = data_list["genre"]
        # 点击筛选器按钮
        self.search_movies_page.click_filter_button()
        # 选择genre
        self.search_movies_page.click_genre()
        # 选择对应genre选项 传进去
        self.search_movies_page.choose_filter_option(genre)
        # 点击应用按钮
        self.search_movies_page.click_filter_apply()
        # 获取到filter标题
        filter_title = self.search_movies_page.get_filter_title()
        assert genre in filter_title

    @logit()
    def test_choose_actor_filter(self):
        """
        测试选择actor筛选器
        :return:
        """
        data_list = self.search_movies_data["test_choose_actor_filter"]
        actor = data_list["actor"]
        # 点击筛选器按钮
        self.search_movies_page.click_filter_button()
        # actor
        self.search_movies_page.click_actor()
        # 选择对应actor选项 传进去
        self.search_movies_page.choose_filter_option(actor)
        # 点击应用按钮
        self.search_movies_page.click_filter_apply()
        # 获取到filter标题
        filter_title = self.search_movies_page.get_filter_title()
        assert actor in filter_title

    @logit()
    def test_choose_director_filter(self):
        """
        测试选择director筛选器
        :return:
        """
        data_list = self.search_movies_data["test_choose_director_filter"]
        director = data_list["director"]
        # 点击筛选器按钮
        self.search_movies_page.click_filter_button()
        # 点击director
        self.search_movies_page.click_director()
        # 选择对应director选项 传进去
        self.search_movies_page.choose_filter_option(director)
        # 点击应用按钮
        self.search_movies_page.click_filter_apply()
        # 获取到filter标题
        filter_title = self.search_movies_page.get_filter_title()
        assert director in filter_title

    @logit()
    def test_choose_release_year_filter(self):
        """
        测试选择release year筛选器
        :return:
        """
        data_list = self.search_movies_data["test_choose_release_year_filter"]
        year = data_list["release year"]
        # 点击筛选器按钮
        self.search_movies_page.click_filter_button()
        # 选择release_year
        self.search_movies_page.click_release_year()
        # 选择对应release_year选项 传进去
        self.search_movies_page.choose_filter_option(year)
        # 点击应用按钮
        self.search_movies_page.click_filter_apply()
        # 获取到filter标题
        filter_title = self.search_movies_page.get_filter_title()
        assert year in filter_title

    @logit()
    def test_multiple_choice(self):
        """
        测试选择多种筛选器
        :return:
        """
        # 获取测试数据
        data_list = self.search_movies_data["test_multiple_choice"]
        language = data_list["language"]
        genre = data_list["genre"]
        actor = data_list["actor"]
        director = data_list["director"]
        year = data_list["release year"]
        # 拼接筛选项列表
        expect_data = language + genre + actor + director + year
        # 点击筛选器按钮
        self.search_movies_page.click_filter_button()
        # 选择language
        self.search_movies_page.click_language()
        # 选择对应language选项 传进去
        self.search_movies_page.choose_filter_options(language)
        # 选择genre
        self.search_movies_page.click_genre()
        # 选择对应genre选项 传进去
        self.search_movies_page.choose_filter_options(genre)
        # 选择actor
        self.search_movies_page.click_actor()
        # 选择对应actor选项 传进去
        self.search_movies_page.choose_filter_options(actor)
        # 点击director
        self.search_movies_page.click_director()
        # 选择对应director选项 传进去
        self.search_movies_page.choose_filter_options(director)
        # 选择release_year
        self.search_movies_page.click_release_year()
        # 选择对应release_year选项 传进去
        self.search_movies_page.choose_filter_options(year)
        # 点击应用按钮
        self.search_movies_page.click_filter_apply()
        # 获取到filter标题
        filter_title = self.search_movies_page.get_filter_title()
        assert filter_title == expect_data

    @logit()
    def test_close_download_switch(self):
        """
        测试默认关闭仅显示可下载视频
        :return:
        """
        text = self.search_movies_page.get_download_switch_text()
        assert text == "关闭"

    @logit()
    def test_open_download_switch(self):
        """
        测试打开仅显示可下载视频
        :return:
        """
        self.search_movies_page.click_download_content_switch()
        text = self.search_movies_page.get_download_switch_text()
        assert text == "开启"

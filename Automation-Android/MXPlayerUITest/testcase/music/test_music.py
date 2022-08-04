import logging
import os
from time import sleep

import pytest
import yaml

from page.app import App
from page.logit import logit


class TestMusic:
    """
    测试music 首页
    """
    @pytest.fixture()
    def back_music_page(self):
        """
        返回到music页
        :return:
        """
        logging.info("TestMusic:back_music_page")
        yield
        sleep(1)
        self.music_page.click_return_button()

    @pytest.fixture()
    def clear_data(self):
        """
        清除测试数据
        :return:
        """
        logging.info("TestMusic:clear_data")
        yield
        # 关闭mini播放器
        self.music_page.close_mini_player()
        # 删除我的最爱歌曲
        if self.music_page.favorite_text_is_exist():
            self.music_page.click_favorite().more_action_clear_all()
        else:
            self.music_page.click_return_button()
            self.music_page.click_favorite().more_action_clear_all()

    def setup_class(self):
        logging.info("TestMusic:setup_class")
        testcase_file = os.path.dirname(__file__).split("testcase")[0] + r"data/testcase_data/music/music.yaml"
        self.music_data = yaml.safe_load(open(testcase_file, "r", encoding="utf-8"))
        self.music_page = App.start_logged_in().to_music_page()

    def setup_method(self, method):
        logging.info("TestMusic:setup_method")
        # 记录类名和方法名
        logging.info(type(self).__name__ + ":" + method.__name__)

    def teardown_class(self):
        logging.info("TestMusic:teardown_class")
        App.quit()

    @logit()
    def test_search_text(self):
        """
        测试搜索框文案
        :return:
        """
        data_list = self.music_data["test_search_text"]
        text = data_list["text"]
        actual_text = self.music_page.get_search_text()
        assert actual_text == text

    @logit()
    @pytest.mark.usefixtures('back_music_page')
    def test_click_banner(self):
        """
        测试点击banner
        :return:
        """
        try:
            self.music_page.click_banner()
        except:
            # 处理出现语言/歌手选择弹层
            self.music_page.click_app_content()
            sleep(1)
            if self.music_page.is_skip_exist():
                for i in range(2):
                    # 跳过语言/歌手选择页面
                    self.music_page.click_choose_language_skip()
            # 滑动banner，第一个banner有可能是广告
            self.music_page.swipe_banner()
            self.music_page.click_banner()
        assert self.music_page.is_back_exist()

    @logit()
    def test_click_song_card(self):
        """
        测试点击音乐卡片
        :return:
        """
        self.music_page.click_song_card()
        assert self.music_page.is_mini_music_title_exist()

    @logit()
    def test_mini_player_title(self):
        """
        测试mini播放器中音乐标题显示是否正确
        :return:
        """
        # 点击音乐卡片，显示mini播放器
        self.music_page.click_song_card()
        # 获取点击的音乐卡片
        expect_title = self.music_page.get_song_card_title()
        actual_title = self.music_page.get_music_title()
        assert actual_title == expect_title

    @logit()
    @pytest.mark.usefixtures("clear_data")
    def test_add_to_my_favorite(self):
        """
        测试添加音乐到我的最爱
        :return:
        """
        data_list = self.music_data["test_add_to_my_favorite"]
        toast = data_list["toast"]
        # 显示等待一秒，解决两个toast同时出现的问题
        sleep(1)
        # 点击添加一首歌到我的最爱
        self.music_page.click_favorite_button()
        actual_toast = self.music_page.get_android_toast_text()
        assert actual_toast == toast

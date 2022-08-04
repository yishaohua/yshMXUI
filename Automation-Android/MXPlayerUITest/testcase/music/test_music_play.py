import logging
import os
import random
from time import sleep

import pytest
import yaml
from selenium.common.exceptions import NoSuchElementException

from page.app import App
from page.logit import logit


class TestMusicPlay:
    """
    测试music 音乐播放页面
    """
    @pytest.fixture()
    def back_search_page(self, clear_data):
        """
        返回到音乐播放页
        :return:
        """
        logging.info("TestMusicPlay:back_search_page")
        yield
        sleep(1)
        self.music_play_page.click_return_button()

    @pytest.fixture()
    def close_abplay(self):
        """
        关闭ab播放
        :return:
        """
        logging.info("TestMusicPlay:close_abplay")
        yield
        self.music_play_page.close_abplay()

    @pytest.fixture()
    def cancel_rotate(self):
        """
        取消单曲循环按钮，便于下次测试
        :return:
        """
        logging.info("TestMusicPlay:cancel_rotate")
        yield
        self.music_play_page.click_rotate_button()

    @pytest.fixture()
    def cancel_shuffle(self):
        """
        取消随机播放按钮，便于下次测试
        :return:
        """
        logging.info("TestMusicPlay:cancel_shuffle")
        yield
        self.music_play_page.click_shuffle()

    @pytest.fixture()
    def close_lyrics(self):
        """
        关闭显示歌词
        :return:
        """
        logging.info("TestMusicPlay:close_lyrics")
        yield
        self.music_play_page.click_return_button()
        self.music_play_page.click_lyrics_button()

    @pytest.fixture(scope='module')
    def clear_data(self):
        """
        模块级别，整个模块运行完后 清除测试数据,删除歌单
        :return:
        """
        logging.info("TestMusicPlay:clear_data before")
        self.handpicked_page = App.start_logged_in().to_music_page().click_view_more()
        self.handpicked_page.click_songs()
        App.quit()
        yield
        logging.info("TestMusicPlay:clear_data after")
        self.music_page = App.start_logged_in().to_music_page()
        # 删除我的最爱歌曲
        if self.music_page.favorite_text_is_exist():
            self.music_page.click_favorite().more_action_clear_all()
        self.music_page.click_return_button()
        # 关闭Mini播放器
        if self.music_page.is_mini_music_title_exist():
            self.music_page.close_mini_player()
        # 删除音乐播放列表
        self.playlist_page = self.music_page.click_playlist()
        option_list = self.playlist_page.get_music_option()
        num = len(option_list)
        for i in range(num):
            self.playlist_page.click_music_option(0)
            self.playlist_page.delete_playlist()
        App.quit()

    def setup_class(self):
        logging.info("TestMusicPlay:setup_class")
        testcase_file = os.path.dirname(__file__).split("testcase")[0] + r"data/testcase_data/music/music_play.yaml"
        self.music_play_data = yaml.safe_load(open(testcase_file, "r", encoding="utf-8"))
        self.music_play_page = App.start_logged_in().to_music_page().to_music_play()

    def setup_method(self, method):
        logging.info("TestMusicPlay:setup_method")
        # 记录类名和方法名
        logging.info(type(self).__name__ + ":" + method.__name__)

    def teardown_class(self):
        logging.info("TestMusicPlay teardown_class")
        App.quit()

    @logit()
    @pytest.mark.usefixtures("back_search_page")
    def test_music_title(self):
        """
        测试页面音乐标题是否显示正确
        :return:
        """
        title = self.music_play_page.get_music_title()
        # 获取详细信息中的标题
        self.music_play_page.click_detail_button()
        detail_title = self.music_play_page.get_detail_title()
        assert title == detail_title

    @logit()
    @pytest.mark.usefixtures("back_search_page")
    def test_open_equalizer(self):
        """
        测试打开平衡器
        :return:
        """
        self.music_play_page.click_equalizer()
        switch_text = self.music_play_page.get_effect_switch_text()
        if "关" in switch_text:
            self.music_play_page.open_effect_switch()
            switch_text_click = self.music_play_page.get_effect_switch_text()
            assert "开" in switch_text_click

    @logit()
    @pytest.mark.usefixtures("close_abplay")
    def test_abplay(self):
        """
        测试选取小节循环播放
        :return:
        """
        # 获取测试数据
        data_list = self.music_play_data["test_abplay"]
        duration = data_list["duration"]
        # 点击 abplay 按钮
        self.music_play_page.click_abplay_button()
        # 根据时间间隔 点击起始和结束按钮
        self.music_play_page.choose_abplay(duration)
        # 获取起始和结束时间
        start_time = self.music_play_page.get_abplay_start_time()
        end_time = self.music_play_page.get_abplay_end_time()
        assert end_time >= start_time + duration

    @logit()
    def test_play_speed(self):
        """
        测试播放速度
        :return:
        """
        # 获取测试数据
        data_list = self.music_play_data["test_play_speed"]
        speed_list = data_list["speed_list"]
        for speed in speed_list:
            self.music_play_page.click_speed_button()
            self.music_play_page.choose_speed(speed)
            try:
                actual_speed = self.music_play_page.get_speed_text()
                assert actual_speed == speed
            except NoSuchElementException:
                # 测试非normal情况
                # 选择normal后会获取不到元素
                assert speed == "Normal"

    @logit()
    def test_add_to_favorite(self):
        """
        测试添加到我的最爱
        :return:
        """
        # 获取测试数据
        data_list = self.music_play_data["test_add_to_favorite"]
        toast = data_list["toast"]
        sleep(1)
        # 点击我的最爱按钮
        self.music_play_page.click_favorite_button()
        actual_toast = self.music_play_page.get_android_toast_text()
        assert toast in actual_toast

    @logit()
    @pytest.mark.usefixtures("cancel_shuffle")
    def test_shuffle_play(self):
        """
        测试切换到随机播放
        :return:
        """
        # 获取测试数据
        data_list = self.music_play_data["test_shuffle_play"]
        toast = data_list["toast"]
        sleep(1)
        # 点击随机播放按钮
        self.music_play_page.click_shuffle()
        actual_toast = self.music_play_page.get_android_toast_text()
        assert toast in actual_toast

    @logit()
    def test_play_pre(self):
        """
        测试点击播放上一首
        :return:
        """
        # 获取当前歌曲名
        current_title = self.music_play_page.get_music_title()
        sleep(1)
        self.music_play_page.click_pre_button()
        # 获取上一首歌曲名
        pre_title = self.music_play_page.get_music_title()
        try:
            toast = self.music_play_page.get_android_toast_text()
            if "载入内容失败。" == toast:
                assert current_title == pre_title
        except:
            assert current_title != pre_title

    @logit()
    def test_play_next(self):
        """
        测试点击播放下一首
        :return:
        """
        # 获取当前歌曲名
        current_title = self.music_play_page.get_music_title()
        sleep(1)
        self.music_play_page.click_next_button()
        # 获取下一首歌曲名
        next_title = self.music_play_page.get_music_title()
        try:
            toast = self.music_play_page.get_android_toast_text()
            if "载入内容失败。" == toast:
                assert current_title == next_title
        except:
            assert current_title != next_title
        # assert current_title != next_title

    @logit()
    @pytest.mark.usefixtures("cancel_rotate")
    def test_rotate_play(self):
        """
        测试切换到单曲循环播放
        :return:
        """
        # 获取测试数据
        data_list = self.music_play_data["test_rotate_play"]
        toast = data_list["toast"]
        # 点击单曲循环按钮
        self.music_play_page.click_rotate_button()
        actual_toast = self.music_play_page.get_android_toast_text()
        assert toast in actual_toast

    @logit()
    @pytest.mark.usefixtures("close_lyrics")
    def test_search_lyrics(self):
        """
        测试搜索歌词
        :return:
        """
        data_list = self.music_play_data["test_search_lyrics"]
        title = data_list["title"]
        self.music_play_page.click_lyrics_button()
        self.music_play_page.click_search_ok()
        actual_title = self.music_play_page.get_search_title()
        assert actual_title == title

    @logit()
    def test_detail_click_playlist(self):
        """
        测试点击播放队列
        :return:
        """
        data_list = self.music_play_data["test_detail_click_playlist"]
        title = data_list["title"]
        # 点击播放队列
        self.music_play_page.click_detail_playlist()
        actual_title = self.music_play_page.get_detail_title()
        assert actual_title == title

    @logit()
    def test_click_shuffle(self):
        """
        测试切换列表播放方式
        :return:
        """
        data_list = self.music_play_data["test_click_shuffle"]
        toast = data_list["toast"]
        # 共有3中toast，点击3次
        for i in range(len(toast)):
            self.music_play_page.click_queue_shuffle()
            actual_toast = self.music_play_page.get_android_toast_text()
            assert toast[i] in actual_toast
            sleep(1)

    @logit()
    def test_clear_one(self):
        """
        测试删除一首歌曲
        :return:
        """
        # 删除前歌曲数
        before_count = self.music_play_page.get_music_count()
        # 删除当前页面中随机一首
        clear_num = random.randint(0, 3)
        self.music_play_page.get_clear_one(clear_num)
        sleep(1)
        # 删除后歌曲数
        after_count = self.music_play_page.get_music_count()
        assert after_count+1 == before_count

    @logit()
    @pytest.mark.usefixtures("back_search_page")
    def test_drag_music(self):
        """
        测试拖动音乐
        :return:
        """
        # 获取到第一首歌曲
        first_music = self.music_play_page.get_current_music()[0]
        # 将第1首歌拖动到第2首的位置
        self.music_play_page.drag_music()
        # 获取到第2首歌曲
        after_music = self.music_play_page.get_current_music()[1]
        assert after_music == first_music

    @logit()
    def test_add_playlist(self):
        """
        测试添加到播放列表
        :return:
        """
        # 获取测试数据
        data_list = self.music_play_data["test_add_playlist"]
        toast = data_list["toast"]
        playlist = data_list["playlist"]
        # 点击查看详细信息
        self.music_play_page.click_detail_button()
        # 点击添加到播放列表
        self.music_play_page.click_add_to_playlist()
        # 新建播放列表并添加
        self.music_play_page.create_playlist_and_add(playlist)
        actual_toast = self.music_play_page.get_android_toast_text()
        assert toast in actual_toast

    @logit()
    def test_click_sleep_timer(self):
        """
        测试点击睡眠定时关闭按钮
        :return:
        """
        # 获取测试数据
        data_list = self.music_play_data["test_click_sleep_timer"]
        title = data_list["title"]
        # 点击查看详细信息
        self.music_play_page.click_detail_button()
        # 点击设置睡眠定时器
        self.music_play_page.click_sleep_timer()
        actual_title = self.music_play_page.get_sleep_title()
        assert actual_title == title

    @logit()
    def test_set_sleep_after_30min(self):
        """
        测试设置睡眠定时器30分钟后
        :return:
        """
        # 获取测试数据
        data_list = self.music_play_data["test_set_sleep_after_30min"]
        toast = data_list["toast"]
        # 选择30分钟并确定
        self.music_play_page.click_sleep_after_30min()
        self.music_play_page.click_search_ok()
        actual_toast = self.music_play_page.get_snackbar_text()
        assert toast in actual_toast

    @logit()
    def test_set_custom(self):
        """
        测试设置睡眠定时器 自定义 2点结束
        :return:
        """
        # 获取测试数据
        data_list = self.music_play_data["test_set_custom"]
        toast = data_list["toast"]
        # 点击查看详细信息
        self.music_play_page.click_detail_button()
        # 点击设置睡眠定时器
        self.music_play_page.click_sleep_timer()
        # 选择自定义
        self.music_play_page.click_custom()
        # 滚动滚轮到2点
        self.music_play_page.roll_to_two()
        # 确定
        self.music_play_page.click_search_ok()
        actual_toast = self.music_play_page.get_snackbar_text()
        assert toast in actual_toast


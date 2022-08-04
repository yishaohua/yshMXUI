import os

import pytest
import yaml

from page.app import App
import logging

from page.logit import logit


class TestLocalMusic:
    """
    测试music 首页
    """
    @pytest.fixture()
    def click_cancel_search(self):
        """
        点击取消搜索按钮
        :return:
        """
        logging.info("TestLocalMusic:click_cancel_search")
        yield
        self.local_music_page.click_search_cancel()

    def setup_class(self):
        """
        初始化类，加载测试数据，进入对应页面
        :return:
        """
        logging.info("TestLocalMusic:setup_class")
        testcase_file = os.path.dirname(__file__).split("testcase")[0] + r"data/testcase_data/music/local_music.yaml"
        self.local_music_data = yaml.safe_load(open(testcase_file, "r", encoding="utf-8"))
        self.local_music_page = App.start_logged_in().to_music_page().click_local()

    def setup_method(self, method):
        """
        setup_method 方法，每个测试方法前执行
        :return:
        """
        logging.info("TestLocalMusic:setup_method")
        # 记录类名和方法名
        logging.info(type(self).__name__ + ":" + method.__name__)

    def teardown_class(self):
        logging.info("TestLocalMusic:teardown_class")
        App.quit()

    @logit()
    def test_click_albums_tab(self):
        """
        测试点击专辑 tab
        :return:
        """
        data_list = self.local_music_data["test_click_albums_tab"]
        text = data_list["text"]
        self.local_music_page.click_albums_tab()
        search_text = self.local_music_page.get_search_text()
        assert search_text == text

    @logit()
    def test_click_artists_tab(self):
        """
        测试点击艺术家tab
        :return:
        """
        data_list = self.local_music_data["test_click_artists_tab"]
        text = data_list["text"]
        self.local_music_page.click_artists_tab()
        search_text = self.local_music_page.get_search_text()
        assert search_text == text

    @logit()
    def test_click_files_tab(self):
        """
        测试点击文件夹tab
        :return:
        """
        data_list = self.local_music_data["test_click_files_tab"]
        text = data_list["text"]
        self.local_music_page.click_files_tab()
        search_text = self.local_music_page.get_search_text()
        assert search_text == text

    @logit()
    def test_click_songs_tab(self):
        """
        测试点击歌曲tab
        :return:
        """
        data_list = self.local_music_data["test_click_songs_tab"]
        text = data_list["text"]
        self.local_music_page.click_songs_tab()
        search_text = self.local_music_page.get_search_text()
        assert search_text == text

    @logit()
    @pytest.mark.usefixtures("click_cancel_search")
    def test_search_song(self):
        """
        测试搜索音乐
        :return:
        """
        data_list = self.local_music_data["test_search_song"]
        song = data_list["song"]
        self.local_music_page.search_music(song)
        title_list = self.local_music_page.get_action_more_title()
        assert song in title_list

    @logit()
    def test_sort_by_title_a2z(self):
        """
        测试按照标题 从a到z
        :return:
        """
        # 点击排序按钮
        self.local_music_page.click_sort_button()
        # 按照标题从a到z排序
        self.local_music_page.click_sort_by_title_a2z()
        # 获取排序后标题
        title_list = self.local_music_page.get_songs_title()
        assert self.local_music_page.sort_by_title_a2z(title_list)

    @logit()
    def test_sort_by_title_z2a(self):
        """
        测试按照标题 从z到a
        :return:
        """
        self.local_music_page.click_sort_button()
        self.local_music_page.click_sort_by_title_z2a()
        title_list = self.local_music_page.get_songs_title()
        assert self.local_music_page.sort_by_title_z2a(title_list)

    @logit()
    def test_sort_by_size_b2s(self):
        """
        测试按照歌曲排序 从大到小
        :return:
        """
        # 点击排序按钮
        self.local_music_page.click_sort_button()
        # 点击按照大小排序从大到小
        self.local_music_page.click_sort_by_size_b2s()
        # 获取到当前所有歌曲的大小列表，
        size_list = self.local_music_page.loop_to_get_all_songs_attr(self.local_music_page.get_attr_size)
        for i in range(len(size_list)-1):
            assert size_list[i] >= size_list[i+1]

    @logit()
    def test_sort_by_size_s2b(self):
        """
        测试按照歌曲排序 从大到小
        :return:
        """
        # 点击排序按钮
        self.local_music_page.click_sort_button()
        # 点击按照大小排序从小到大
        self.local_music_page.click_sort_by_size_s2b()
        # 获取到当前所有歌曲的大小列表
        size_list = self.local_music_page.loop_to_get_all_songs_attr(self.local_music_page.get_attr_size)
        for i in range(len(size_list)-1):
            assert size_list[i] <= size_list[i+1]

    @logit()
    def test_sort_by_date_n2o(self):
        """
        测试按照添加日期 从新到旧
        :return:
        """
        # 点击排序按钮
        self.local_music_page.click_sort_button()
        # 点击按照添加日期 从新到旧
        self.local_music_page.click_sort_by_date_n2o()
        # 获取到当前所有歌曲的添加日期列表
        date_list = self.local_music_page.loop_to_get_all_songs_attr(self.local_music_page.get_attr_date)
        for i in range(len(date_list) - 1):
            assert date_list[i] >= date_list[i + 1]

    @logit()
    def test_sort_by_date_o2n(self):
        """
        测试按照添加日期 从旧到新
        :return:
        """
        # 点击排序按钮
        self.local_music_page.click_sort_button()
        # 点击按照添加日期 从旧到新
        self.local_music_page.click_sort_by_date_o2n()
        # 获取到当前所有歌曲的添加日期列表
        date_list = self.local_music_page.loop_to_get_all_songs_attr(self.local_music_page.get_attr_date)
        for i in range(len(date_list) - 1):
            assert date_list[i] <= date_list[i + 1]

    @logit()
    def test_sort_by_duration_l2s(self):
        """
        测试按照时长 从长到短
        :return:
        """
        # 点击排序按钮
        self.local_music_page.click_sort_button()
        # 点击按照时长 从长到短
        self.local_music_page.click_sort_by_duration_l2s()
        # 获取到当前所有歌曲的时长列表
        duration_list = self.local_music_page.loop_to_get_all_songs_attr(self.local_music_page.get_attr_duration)
        for i in range(len(duration_list) - 1):
            assert duration_list[i] >= duration_list[i + 1]

    @logit()
    def test_sort_by_duration_s2l(self):
        """
        测试按照时长 从短到长
        :return:
        """
        # 点击排序按钮
        self.local_music_page.click_sort_button()
        # 点击按照时长 从长到短
        self.local_music_page.click_sort_by_duration_s2l()
        # 获取到当前所有歌曲的时长列表
        duration_list = self.local_music_page.loop_to_get_all_songs_attr(self.local_music_page.get_attr_duration)
        for i in range(len(duration_list) - 1):
            assert duration_list[i] <= duration_list[i + 1]

    @logit()
    def test_show_one_min(self):
        """
        测试只展示1分钟以上的歌曲
        :return:
        """
        # 点击排序按钮
        self.local_music_page.click_sort_button()
        # 点击选择一分钟以上的歌曲
        self.local_music_page.click_one_min()
        # 获取到当前所有歌曲的时长列表
        duration_list = self.local_music_page.loop_to_get_all_songs_attr(self.local_music_page.get_attr_duration)
        for i in range(len(duration_list)):
            assert duration_list[i] >= 60

    @logit()
    def test_shuffle_all(self):
        """
        测试随机播放全部
        :return:
        """
        self.local_music_page.click_shuffle_all()
        assert self.local_music_page.is_mini_music_title_exist()

    @logit()
    def test_click_song_option(self):
        """
        点击第一首音乐 选项按钮
        :return:
        """
        title = self.local_music_page.get_songs_title()[0]
        self.local_music_page.click_music_option(0)
        actual_title = self.local_music_page.get_action_more_title()
        assert actual_title == title

    @logit()
    def test_click_play_next(self):
        """
        测试点击接下来播放
        :return:
        """
        data_list = self.local_music_data["test_click_play_next"]
        toast = data_list["toast"]
        # 点击接下来播放
        self.local_music_page.click_play_next()
        # 获取到toast提示
        actual_toast = self.local_music_page.get_android_toast_text()
        assert toast in actual_toast

    @logit()
    def test_add_play_later(self):
        """
        测试添加到稍后播放
        :return:
        """
        data_list = self.local_music_data["test_add_play_later"]
        toast = data_list["toast"]
        # 点击第一个音乐选项
        self.local_music_page.click_music_option(0)
        # 点击添加到稍后播放
        self.local_music_page.click_play_later()
        # 获取到toast提示
        actual_toast = self.local_music_page.get_android_toast_text()
        assert toast in actual_toast

    @logit()
    def test_add_favorite(self):
        """
        测试添加到最爱
        :return:
        """
        data_list = self.local_music_data["test_add_favorite"]
        toast = data_list["toast"]
        # 点击第一个音乐选项
        self.local_music_page.click_music_option(0)
        # 点击添加到最爱
        self.local_music_page.click_add_favorite()
        # 获取到toast提示
        actual_toast = self.local_music_page.get_android_toast_text()
        assert toast in actual_toast

    @logit()
    def test_add_playlist(self):
        """
        测试点击添加到播放列表中
        :return:
        """
        data_list = self.local_music_data["test_add_playlist"]
        playlist = data_list["playlist"]
        toast = data_list["toast"]
        # 点击第一个音乐选项
        self.local_music_page.click_music_option(0)
        # 点击添加到播放列表
        self.local_music_page.click_add_playlist()
        # 创建播放列表并添加
        self.local_music_page.create_new_playlist_and_add(playlist)
        actual_toast = self.local_music_page.get_android_toast_text()
        assert toast in actual_toast

    @logit()
    def test_set_as_phone_ringtone(self):
        """
        测试设置为手机铃声
        :return:
        """
        data_list = self.local_music_data["test_set_as_phone_ringtone"]
        toast = data_list["toast"]
        # 点击第一个音乐选项
        self.local_music_page.click_music_option(0)
        # 点击添加到播放列表
        self.local_music_page.click_set_as_ringtone()
        # 点击选择手机铃声
        self.local_music_page.click_phone_ringtone()
        # 判断是否需要打开系统权限
        try:
            actual_toast = self.local_music_page.get_android_toast_text()
            assert toast in actual_toast
        except:
            self.local_music_page.click_sys_switch()
            actual_toast = self.local_music_page.get_android_toast_text()
            assert toast in actual_toast

    @logit()
    def test_set_as_alarm_ringtone(self):
        """
        测试设置为闹钟铃声
        :return:
        """
        data_list = self.local_music_data["test_set_as_alarm_ringtone"]
        toast = data_list["toast"]
        # 点击第一个音乐选项
        self.local_music_page.click_music_option(0)
        # 点击添加到播放列表
        self.local_music_page.click_set_as_ringtone()
        # 点击选择手机铃声
        self.local_music_page.click_alarm_ringtone()
        actual_toast = self.local_music_page.get_android_toast_text()
        assert toast in actual_toast

    @logit()
    def test_set_as_notification_ringtone(self):
        """
        测试设置为通知铃声
        :return:
        """
        data_list = self.local_music_data["test_set_as_notification_ringtone"]
        toast = data_list["toast"]
        # 点击第一个音乐选项
        self.local_music_page.click_music_option(0)
        # 点击添加到播放列表
        self.local_music_page.click_set_as_ringtone()
        # 点击选择手机铃声
        self.local_music_page.click_notification_ringtone()
        actual_toast = self.local_music_page.get_android_toast_text()
        assert toast in actual_toast

    @logit()
    def test_rename_song(self):
        """
        测试重命名歌单
        :return:
        """
        data_list = self.local_music_data["test_rename_song"]
        new_name = data_list["new_name"]
        # 点击第一个歌单的选项按钮
        self.local_music_page.click_music_option(0)
        # 修改歌单名称
        self.local_music_page.click_rename()
        self.local_music_page.rename_playlist(new_name)
        # 获取修改后的歌曲名称
        actual_name = self.local_music_page.get_songs_title()[0]
        assert actual_name == new_name

    @logit()
    def test_click_attribute(self):
        """
        测试查看歌曲属性
        :return:
        """
        data_list = self.local_music_data["test_click_attribute"]
        title = data_list["title"]
        # 点击第一个歌单的选项按钮
        self.local_music_page.click_music_option(0)
        # 点击查看属性
        self.local_music_page.click_attribute_button()
        # 获取属性页文件标题
        actual_title = self.local_music_page.get_attr_file_title()
        assert actual_title == title
        self.local_music_page.click_close()

    @logit()
    def test_delete_song(self):
        """
        测试删除歌曲
        :return:
        """
        data_list = self.local_music_data["test_delete_song"]
        toast = data_list["toast"]
        # 点击第一个歌单的选项按钮
        self.local_music_page.click_music_option(0)
        # 点击查看属性
        self.local_music_page.delete_song()
        # 获取删除音乐后toast
        actual_title = self.local_music_page.get_android_toast_text()
        assert toast in actual_title


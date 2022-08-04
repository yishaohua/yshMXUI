import logging
import os
import pytest
import yaml

from page.app import App
from page.logit import logit


class TestVideoDetail:
    """
    测试Video detail视频详情页
    """
    @pytest.fixture()
    def click_detail_button(self, reset_data):
        """
        收起查看视频详情按钮
        :return:
        """
        logging.info("TestVideoDetail:click_detail_button")
        yield
        self.video_detail_page.click_arrow_button()

    @pytest.fixture()
    def click_download_cancel(self):
        """
        取消下载
        :return:
        """
        logging.info("TestVideoDetail:click_download_cancel")
        yield
        self.video_detail_page.click_return_button()
        self.video_detail_page.click_download_option()
        self.video_detail_page.click_download_cancel()

    @pytest.fixture()
    def back_to_detail(self):
        """
        返回到视频详情页
        :return:
        """
        logging.info("TestVideoDetail:back_to_detail")
        yield
        self.video_detail_page.click_return_button()

    @pytest.fixture(scope='module')
    def reset_data(self):
        """
        重置视频下载设置，删除待看列表数据
        :return:
        """
        logging.info("TestVideoDetail:reset_download_settings")
        yield
        # 删除待看列表列表数据
        self.watch_list_page = App.start_logged_in().to_video_home_page().click_watch_list_more()
        self.watch_list_page.select_all_video_and_delete(1)
        self.watch_list_page.click_delete_action()
        App.quit()

    def setup_class(self):
        logging.info("TestVideoDetail:setup_class")
        # 获取测试数据
        testcase_file = os.path.dirname(__file__).split("testcase")[0] + r"data/testcase_data/video/video_detail.yaml"
        self.video_detail_data = yaml.safe_load(open(testcase_file, "r", encoding="utf-8"))
        self.video_detail_page = App.start_logged_in().to_video_home_page().click_banner_video()

    def setup_method(self, method):
        logging.info("TestVideoDetail:setup_method")
        # 记录类名和方法名
        logging.info(type(self).__name__+":"+method.__name__)

    def teardown_class(self):
        logging.info("TestVideoDetail:teardown_class")
        App.quit()

    @logit()
    def test_click_arrow_button(self):
        """
        测试点击展开按钮
        :return:
        """
        self.video_detail_page.click_arrow_button()
        assert self.video_detail_page.is_subscribe_exist()

    # def test_click_subscribe_button(self):
    #     """
    #     测试点击订阅，需要使用已登录账户测试
    #     :return:
    #     """
    #     self.video_detail_page.click_subscribe()
    #     btn_text = self.video_detail_page.get_subscribe_text()
    #     assert "取消订阅" == btn_text

    @pytest.mark.usefixtures("click_detail_button")
    @logit()
    def test_click_cancel_subscribe_button(self):
        """
        测试点击取消订阅
        :return:
        """
        # self.video_detail_page.click_subscribe()
        btn_text = self.video_detail_page.get_subscribe_text()
        assert "订阅" == btn_text

    @pytest.mark.usefixtures("back_to_detail")
    @logit()
    def test_episode_title(self):
        """
        测试剧集列表
        :return:
        """
        episode_title = self.video_detail_page.get_episode_title()
        # 获取查看更多列表剧集名称
        more_page = self.video_detail_page.click_view_more()
        all_card_title = more_page.get_video_card_subtitle()
        # 断言 剧集列表是否在 查看更多列表中
        assert set(episode_title) < set(all_card_title)

    @pytest.mark.usefixtures("click_download_cancel")
    @logit()
    def test_download(self):
        """
        测试下载
        :return:
        """
        # 点击下载选项按钮
        self.video_detail_page.click_download_option()
        # 点击立即下载按钮
        self.video_detail_page.click_download_button()
        # 点击下载选项按钮
        self.video_detail_page.click_download_option()
        # 断言是否存在暂停下载按钮
        assert self.video_detail_page.is_download_pause_exist()

    @pytest.mark.usefixtures("click_download_cancel")
    @logit()
    def test_download_High(self):
        """
        测试下载High画质
        :return:
        """
        # 点击下载选项按钮
        self.video_detail_page.click_download_option()
        # 选择High画质，设置为默认
        self.video_detail_page.click_download_and_choose_resolution(2)
        # 点击立即下载按钮
        self.video_detail_page.click_download_button()
        # 点击下载选项按钮
        self.video_detail_page.click_download_option()
        # 断言是否存在暂停下载按钮
        assert self.video_detail_page.is_download_pause_exist()

    @logit()
    def test_share_whatsapp_toast(self):
        """
        测试分享到whatsapp，未安装app
        :return:
        """
        data_list = self.video_detail_data["test_share_whatsapp_toast"]
        toast = data_list["toast"]
        # 点击分享选项
        self.video_detail_page.click_share_button()
        # 点击分享到 whatsapp 按钮
        self.video_detail_page.click_share_whatsapp()
        actual_toast = self.video_detail_page.get_android_toast_text()
        assert toast in actual_toast

    @logit()
    def test_share_copy(self):
        """
        测试分享 copy文案显示是否正确
        :return:
        """
        data_list = self.video_detail_data["test_share_copy"]
        toast = data_list["toast"]
        # 点击分享选项
        self.video_detail_page.click_share_button()
        # 点击copy
        self.video_detail_page.click_share_copy()
        actual_toast = self.video_detail_page.get_android_toast_text()
        assert toast in actual_toast

    @logit()
    def test_add_watchlist(self):
        """
        测试添加到待看列表
        :return:
        """
        # 添加到待看列表列表中
        self.video_detail_page.click_place_holder()
        # 获取到视频标题
        video_title = self.video_detail_page.get_video_title()
        # 进入video 待看列表全部页面
        self.watch_list_page = App.start_logged_in().to_video_home_page().click_watch_list_more()
        # 获取待看列表全部标题
        watch_list_title = self.watch_list_page.get_watch_list_title()
        # 增加首页判断获取待看列表名称
        assert video_title in watch_list_title


    ## 以下测试用例，由于新版本获取不到页面元素，暂不可执行
    # def test_click_quality(self):
    #     """
    #     测试点击720p画质
    #     :return:
    #     """
    #     data_list = self.video_detail_data["test_click_quality"]
    #     quality = data_list["quality"]
    #     # 选择720p画质
    #     self.video_detail_page.click_action_more()
    #     self.video_detail_page.click_quality()
    #     self.video_detail_page.click_quality_720p()
    #     # 获取默认画质
    #     self.video_detail_page.click_action_more()
    #     actual_quality = self.video_detail_page.get_quality_default()
    #     assert actual_quality == quality
    #
    # def test_click_speed(self):
    #     """
    #     测试速度1.5
    #     :return:
    #     """
    #     data_list = self.video_detail_data["test_click_speed"]
    #     speed = data_list["speed"]
    #     # 选择1.5倍速
    #     self.video_detail_page.click_action_more()
    #     self.video_detail_page.click_speed()
    #     self.video_detail_page.click_speed_15()
    #     # 获取默认速度
    #     self.video_detail_page.click_action_more()
    #     actual_speed = self.video_detail_page.get_speed_default()
    #     assert actual_speed == speed
    #
    # def test_click_subtitles(self):
    #     """
    #     测试字幕开启英语字幕
    #     :return:
    #     """
    #     data_list = self.video_detail_data["test_click_subtitles"]
    #     subtitles = data_list["subtitles"]
    #     # 点击选择更多
    #     self.video_detail_page.click_action_more()
    #     self.video_detail_page.click_subtitles()
    #     # 选择English字幕
    #     self.video_detail_page.click_subtitles_english()
    #     # 再次点击选择更多
    #     self.video_detail_page.click_action_more()
    #     # 获取默认字幕
    #     actual_subtitles = self.video_detail_page.get_subtitles_default()
    #     assert actual_subtitles == subtitles
    #
    # def test_first_open_pip(self):
    #     """
    #     测试首次开启画中画模式，需要授权
    #     :return:
    #     """
    #     logging.info("TestVideoDetail test_first_open_pip")
    #     self.video_detail_page.permit_pip_play()
    #
    # def test_open_pip(self):
    #     """
    #     测试开启画中画模式
    #     :return:
    #     """
    #     logging.info("TestVideoDetail test_open_pip")
    #     video_home_page = self.video_detail_page.click_pip_button()
    #     title = video_home_page.get_shows_card_title()
    #     assert "WEB SHOWS" == title
    #
    # def test_click_fullscreen(self):
    #     """
    #     测试点击全屏按钮
    #     :return:
    #     """
    #     self.video_detail_page.click_fullscreen()
    #     # 通过断言是否存在分享按钮判断是否全屏
    #     assert not self.video_detail_page.is_share_exist()
    #
    # def test_play_position(self):
    #     """
    #     测试视频播放时长是否正常
    #     :return:
    #     """
    #     play_position = self.video_detail_page.get_play_exo_position()
    #     duration = self.video_detail_page.get_play_exo_position()
    #     play_position_min = play_position.split(":")[0]
    #     duration_min = duration.split(":")[0]
    #     assert play_position_min <= duration_min

    # 需要指定的视频才会出现
    # def test_click_age_confirm_ok(self):
    #     """
    #     测试18周岁弹窗 点击确定
    #     :return:
    #     """
    #     self.video_detail_page.click_age_confirm_ok()
    #     sleep(1)
    #     # 断言分享按钮是否存在
    #     assert self.video_detail_page.is_share_exist()


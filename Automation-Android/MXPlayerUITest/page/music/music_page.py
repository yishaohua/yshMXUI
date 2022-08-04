from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.music.local_music_page import LocalMusicPage
from page.music.music_base_page import MusicBasePage
from page.music.music_play_page import MusicPlayPage
from page.music.music_search_page import MusicSearchPage
from page.music.my_favorites_page import MyFavoritesPage
from page.music.my_playlist_page import MyPlaylistPage


class MusicPage(MusicBasePage):
    """
    继承通用页面
    音乐页面
    """
    # 搜索框
    __search_bar = (By.ID, "com.mxtech.videoplayer.ad:id/gaana_search_bar")
    # 搜索框文本
    __search_text = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/gaana_search_bar']/android.widget.TextView")
    # 搜索框中 音频搜索按钮
    __voice_search = (By.ID, "com.mxtech.videoplayer.ad:id/voice_search")
    # banner
    __banner = (By.ID, "com.mxtech.videoplayer.ad:id/banner")
    # 我的最爱
    __favorite = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/favourite_layout']/android.widget.ImageView")
    # 我的最爱文案
    __favorite_text = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/favourite_layout']/android.widget.TextView")
    # 我的歌单
    __playlist = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/playlist_layout']/android.widget.ImageView")
    # 我的歌单文案
    __playlist_text = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/playlist_layout']/android.widget.TextView")
    # 本地音乐
    __local = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/local_layout']/android.widget.ImageView")
    # 本地音乐文案
    __local_text = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/local_layout']/android.widget.TextView")
    # 近期播放 卡片标题
    __play_title = (By.XPATH, "//*[contains(@text, '近期播放')]")
    # 近期播放 查看更多
    __play_more = (By.XPATH, "//*[contains(@text, '近期播放')]/../android.widget.TextView")
    # 音乐卡片
    __song_card = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/cover_image']")
    # 音乐卡片 标题
    __song_title = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/title']")
    # 首页查看更多
    __view_more = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/view_more']")
    __handpicked_view_more = (By.XPATH, "//*[@text='Handpicked For You']/../android.widget.TextView[2]")

    # 播放全部
    __play_all = (By.ID, "com.mxtech.videoplayer.ad:id/play_all")

    # 语音搜索 说完了按钮
    __voice_search_stop = (By.ID, "com.xiaomi.mibrain.speech:id/stop")
    # 语音搜索错误结果 知道了按钮
    __voice_search_ok = (By.ID, "com.xiaomi.mibrain.speech:id/error_ok")
    # 语音搜索错误结果 提示信息
    __voice_search_error_msg = (By.ID, "com.xiaomi.mibrain.speech:id/error_msg")

    # swipe page 可上下滑动区域
    __swipe_page = (By.ID, "com.mxtech.videoplayer.ad:id/swipe")
    # music 选择音乐对应语言弹窗 应用按钮
    __music_language_apply_button = (By.ID, "com.mxtech.videoplayer.ad:id/apply")
    # music 选择音乐对应语言弹窗 可选语言列表
    __music_language_choice = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/tag_flow_layout']/android.widget.LinearLayout")

    # 选择喜爱的歌手弹窗 应用按钮
    __choose_singers_apply = (By.ID, "com.mxtech.videoplayer.ad:id/apply")
    # 选择喜爱的歌手 歌手名称
    __choose_singers_name = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/title']")

    # 定位信息弹窗 仅在使用中允许
    __permission_allow_foreground = (By.ID, "com.lbe.security.miui:id/permission_allow_foreground_only_button")
    # 手机号获取弹窗 始终允许按钮
    __allow_button = (By.ID, "com.lbe.security.miui:id/permission_allow_button_1")

    def click_search_bar(self):
        """
        点击搜索输入框
        :return:
        """
        self.find_element_and_click(self.__search_bar)
        return MusicSearchPage(self.driver)

    def get_search_text(self):
        """
        获取搜索框中默认文案
        :return:
        """
        return self.find_element_and_get_text(self.__search_text)

    def search_music_by_voice(self):
        """
        用音频搜索音乐
        :return:
        """
        # 点击音频搜索按钮
        self.find_element_and_click(self.__voice_search)
        try:
            # 等待2秒后，暂停录音
            sleep(2)
            self.find_element_and_click(self.__voice_search_stop)
        except:
            # 如果暂停录音按钮不存在，则去执行获取权限方法
            # 总共3个权限：位置，录音，手机号
            for i in range(2):
                self.click_permission_foreground()
                sleep(1)
            self.click_allow()
            # 等待2秒后，暂停录音
            sleep(2)
            self.find_element_and_click(self.__voice_search_stop)
        return self

    def is_error_msg_exist(self):
        """
        判断音频搜索音乐后，错误提示信息是否存在
        :return:
        """
        return self.is_element_exist(self.__voice_search_error_msg)

    def click_banner(self):
        """
        点击banner
        :return:
        """
        self.find_element_and_click(self.__banner)
        return self

    def swipe_banner(self):
        """
        滑动banner
        :return:
        """
        self.slide_next_sheet(self.__banner, -600)
        return self

    def click_favorite(self):
        """
        点击我的最爱
        :return:
        """
        try:
            sleep(1)
            self.find_element_and_click(self.__favorite)
        except:
            # 处理出现语言/歌手选择弹层
            self.click_app_content()
            sleep(1)
            if self.is_skip_exist():
                for i in range(2):
                    # 跳过语言/歌手选择页面
                    self.click_choose_language_skip()
        return MyFavoritesPage(self.driver)

    def get_favorite_text(self):
        """
        获取我的最爱 文案
        :return:
        """
        return self.find_element_and_get_text(self.__favorite_text)

    def favorite_text_is_exist(self):
        """
        我的最爱文案是否存在
        :return:
        """
        return self.is_element_exist(self.__favorite_text)

    def click_playlist(self):
        """
        点击我的歌单
        :return:
        """
        try:
            sleep(1)
            self.find_element_and_click(self.__playlist)
        except:
            # 处理出现语言/歌手选择弹层
            self.click_app_content()
            sleep(1)
            if self.is_skip_exist():
                for i in range(2):
                    # 跳过语言/歌手选择页面
                    self.click_choose_language_skip()
            self.find_element_and_click(self.__playlist)
        return MyPlaylistPage(self.driver)

    def get_playlist_text(self):
        """
        获取我的歌单 文案
        :return:
        """
        return self.find_element_and_get_text(self.__playlist_text)

    def click_local(self):
        """
        点击本地音乐
        :return:
        """
        try:
            sleep(1)
            self.find_element_and_click(self.__local)
        except:
            # 处理出现语言/歌手选择弹层
            self.click_app_content()
            sleep(1)
            if self.is_skip_exist():
                for i in range(2):
                    # 跳过语言/歌手选择页面
                    self.click_choose_language_skip()
            self.find_element_and_click(self.__local)
        return LocalMusicPage(self.driver)

    def get_local_text(self):
        """
        获取本地音乐 文案
        :return:
        """
        return self.find_element_and_get_text(self.__local_text)

    def click_play_more(self):
        """
        点击近期播放 查看更多
        :return:
        """
        self.find_element_and_click(self.__play_more)
        return self

    def click_song_card(self):
        """
        点击音乐卡片
        :return:
        """
        cards = self.find_elements(self.__song_card)
        cards[0].click()
        if not self.favorite_text_is_exist():
            cards = self.find_elements(self.__song_card)
            cards[0].click()
        return self

    def get_song_card_title(self):
        """
        获取第一个音乐卡片名称
        :return:
        """
        return self.find_elements(self.__song_title)[0].text

    def click_view_more(self):
        """
        点击查看更多
        :return:
        """
        try:
            view_mores = self.find_elements(self.__view_more)
        except:
            # 处理出现语言/歌手选择弹层
            self.click_app_content()
            sleep(1)
            if self.is_skip_exist():
                for i in range(2):
                    # 跳过语言/歌手选择页面
                    self.click_choose_language_skip()
            view_mores = self.find_elements(self.__view_more)

        for i in range(1, len(view_mores)):
            view_mores[i].click()
            if self.is_play_all_exist():
                return MyFavoritesPage(self.driver)
            else:
                self.click_return_button()

    def is_play_all_exist(self):
        """
        判断播放全部按钮存在，存在即代表有数据
        :return:
        """
        return self.is_element_exist(self.__play_all)

    def to_music_play(self):
        """
        进入音乐播放页面
        :return:
        """
        try:
            self.click_song_card()
            self.click_mini_music_title()
        except:
            # 处理出现语言/歌手选择弹层
            self.click_app_content()
            sleep(1)
            if self.is_skip_exist():
                for i in range(2):
                    # 跳过语言/歌手选择页面
                    self.click_choose_language_skip()
            self.click_song_card()
            self.click_mini_music_title()
        return MusicPlayPage(self.driver)

    def choose_language(self):
        """
        选择音乐语言类型
        :return:
        """
        choice = self.find_elements(self.__music_language_choice)
        for i in range(1):
            choice[i].click()
        return self

    def click_choose_language_apply(self):
        """
        点击语言选择弹窗中应用按钮
        :return:
        """
        self.find_element_and_click(self.__music_language_apply_button)
        return self

    def get_choose_singers_name(self):
        """
        获取选择歌手的姓名
        :return:
        """
        return self.find_elements_and_get_text(self.__choose_singers_name)

    def click_permission_foreground(self):
        """
        点击权限允许弹窗中 仅在使用中允许
        :return:
        """
        self.find_element_and_click(self.__permission_allow_foreground)
        return self

    def click_allow(self):
        """
        点击手机号权限弹窗中 始终允许按钮
        :return:
        """
        self.find_element_and_click(self.__allow_button)
        return self

    def click_handpicked_view_more(self):
        """
        点击	Handpicked For You 的查看更多
        :return:
        """
        self.find_element_and_click(self.__handpicked_view_more)
        return MyFavoritesPage(self.driver)

    def add_to_my_favorites(self):
        """
        添加多首歌音乐到我的最爱
        :return:
        """
        self.click_view_more()
        sleep(1)
        for i in range(3):
            self.click_music_option(i)
            sleep(1)
            self.click_add_favorite()
        return self




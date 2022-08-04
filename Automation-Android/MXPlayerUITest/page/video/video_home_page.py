import logging
from time import sleep

from selenium.webdriver.common.by import By

from page.local.anchor_media_page import AnchorMediaPage
from page.video.card_view_more_page import CardViewMorePage
from page.video.download_page import DownloadPage
from page.video.notice_page import NoticePage
from page.video.video_base_page import VideoBasePage
from page.video.video_buzz_page import VideoBuzzPage
from page.video.video_detail_page import VideoDetailPage
from page.video.video_news_page import VideoNewsPage
from page.video.video_search_page import VideoSearchPage
from page.video.watch_list_page import WatchListPage


class VideoHomePage(VideoBasePage):
    """
    继承一个通用页面  通用页面封装了一些通用方法和异常处理
    视频home页面
    """
    # 左上角 返回上一级
    __back_button = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/online_toolbar']/"
                               "android.widget.ImageButton")
    # 顶部logo
    __top_title = (By.ID, "com.mxtech.videoplayer.ad:id/iv_home_logo")
    # 顶部搜索按钮
    __top_search_button = (By.ID, "com.mxtech.videoplayer.ad:id/go_to_search")
    # 顶部通知按钮
    __top_notice_button = (By.ID, "com.mxtech.videoplayer.ad:id/ripple_view_inbox")
    # 顶部下载按钮
    __top_download_button = (By.ID, "com.mxtech.videoplayer.ad:id/go_to_download")
    # 导航栏
    __indicator_container = (By.ID, "com.mxtech.videoplayer.ad:id/indicator_container")
    # 导航标题
    __title_container = (By.ID, "com.mxtech.videoplayer.ad:id/title_container")
    # 导航栏具体tab
    __indicator_tab = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/title_container']/android.widget.TextView")
    # 广告标题
    __native_ad_title = (By.ID, "com.mxtech.videoplayer.ad:id/native_ad_title")
    # 广告元素
    __native_ad = (By.ID, "com.mxtech.videoplayer.ad:id/ad_container")
    # # 返回--视频播放列表按钮
    # __back_video_playlist = (By.ID, "com.mxtech.videoplayer.ad:id/ll_video_playlist")

    # home页面 查看更多
    __card_view_more = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/view_more']")
    # home页面 待看列表列表--查看更多
    # __watch_list_more = (By.XPATH, "//*[@text='待看列表']/../android.widget.TextView")
    __watch_list = (By.XPATH, "//*[@text='待看列表']")
    __watch_list_more = (By.XPATH, "//*[@text='待看列表']/following-sibling::android.widget.TextView")

    # music 页面，点击卡片查看更多
    __music_view_more_title = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/toolbar']/android.widget.TextView")

    # 已登陆后，you may like 标题
    __you_may_like_title = (By.XPATH, "//*[@text='You May Like']")
    # 第一个视频列表
    __video_list = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/card_recycler_view']/android.view.ViewGroup")
    # home页面，banner 自动播放视频卡片
    __banner_auto_video_card = (By.ID, "com.mxtech.videoplayer.ad:id/auto_play_video_player_view")
    # home页面，banner图片
    __banner_card = (By.ID, "com.mxtech.videoplayer.ad:id/banner_img")
    # home页面，banner区域
    __banner_view = (By.ID, "com.mxtech.videoplayer.ad:id/banner_image_view_card")
    # home页面，banner 添加待看列表按钮
    __watch_button = (By.ID, "com.mxtech.videoplayer.ad:id/watchlist_img")
    # home页面，banner 当前banner位置
    __banner_loc = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/pagination_text']/android.widget.TextView")

    # 各tab页面卡片标题,一组元素
    __card_title = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/card_title']")
    # Buzz 分类卡片列表
    __buzz_card_list = (By.ID, "com.mxtech.videoplayer.ad:id/card_recycler_view")

    def is_back_button_exist(self):
        """
        判断返回设置按钮是否存在
        :return:
        """
        return self.is_element_exist(self.__back_button)

    def click_back_button(self):
        """
        点击返回设置按钮
        :return:
        """
        try:
            self.find_element_and_click(self.__back_button)
            return AnchorMediaPage(self.driver)
        except:
            self.click_app_content()
            sleep(1)
            if self.is_skip_exist():
                self.click_choose_language_skip()
            self.find_element_and_click(self.__back_button)
            return AnchorMediaPage(self.driver)

    def click_search_button(self):
        """
        点击顶部搜索按钮
        :return:
        """
        try:
            sleep(1)
            self.find_element_and_click(self.__top_search_button)
        except:
            self.click_app_content()
            sleep(1)
            if self.is_skip_exist():
                self.click_choose_language_skip()
            self.find_element_and_click(self.__top_search_button)
        return VideoSearchPage(self.driver)

    def click_notice_button(self):
        """
        点击顶部通知按钮
        :return:
        """
        try:
            self.find_element_and_click(self.__top_notice_button)
        except:
            self.click_app_content()
            sleep(1)
            if self.is_skip_exist():
                self.click_choose_language_skip()
            self.find_element_and_click(self.__top_notice_button)
        return NoticePage(self.driver)

    def click_download_button(self):
        """
        点击顶部下载按钮
        :return:
        """
        try:
            self.find_element_and_click(self.__top_download_button)
        except:
            self.click_app_content()
            sleep(1)
            if self.is_skip_exist():
                self.click_choose_language_skip()
            self.find_element_and_click(self.__top_download_button)
        return DownloadPage(self.driver)

    def get_ad_locate(self):
        """
        获取到广告标题元素
        :return:
        """
        return self.find_element(self.__native_ad)

    def slide_video_tab(self):
        """
        滑动video tab到下一页
        :return:
        """
        self.slide_next_sheet(self.__title_container, -400)
        return self

    def get_all_tab_text(self):
        """
        获取到全部tab
        :return:
        """
        if not self.is_element_exist(self.__indicator_tab):
            # 处理出现语言/歌手选择弹层
            self.click_app_content()
            sleep(1)
            if self.is_skip_exist():
                # 跳过语言/歌手选择页面
                self.click_choose_language_skip()
        # 获取当前页面全部tab元素的text
        ele_list_text = self.find_elements_and_get_text(self.__indicator_tab)
        # 滑动页面后，获取当前页全部tab元素
        # 根据tab元素的text判断是否已存在在列表中
        # 如果 当前页最后一个元素不存在 ele_list_text 中，则继续滑动，并且将不存在的元素追加到ele_list_text中
        while True:
            self.slide_video_tab()
            current_list = self.find_elements(self.__indicator_tab)
            last_text = current_list[-1].text
            if last_text not in ele_list_text:
                for n in range(len(current_list)):
                    if current_list[n].text not in ele_list_text:
                        ele_list_text.append(current_list[n].text)
            else:
                break
        return ele_list_text

    def click_home_tab(self):
        """
        点击home tab
        :return:
        """
        try:
            ele_list = self.find_elements(self.__indicator_tab)
        except:
            self.click_app_content()
            sleep(1)
            if self.is_skip_exist():
                self.click_choose_language_skip()
            ele_list = self.find_elements(self.__indicator_tab)
        for n in range(len(ele_list)):
            if ele_list[n].text == '   ':
                ele_list[n].click()
        return self

    def click_shows_tab(self):
        """
        点击SHOWS tab
        :return:
        """
        ele_list = self.find_elements(self.__indicator_tab)
        for n in range(len(ele_list)):
            if ele_list[n].text == 'WEB SHOWS':
                ele_list[n].click()
        return self

    def click_movies_tab(self):
        """
        点击Movies tab
        :return:
        """
        ele_list = self.find_elements(self.__indicator_tab)
        for n in range(len(ele_list)):
            if ele_list[n].text == 'MOVIES':
                ele_list[n].click()
        return self

    def click_mx_vdesi_tab(self):
        """
        点击MX VDESI tab
        :return:
        """
        ele_list = self.find_elements(self.__indicator_tab)
        for n in range(len(ele_list)):
            if ele_list[n].text == 'MX VDESI':
                ele_list[n].click()
        return self

    def click_news_tab(self):
        """
        点击news tab
        :return:
        """
        ele_list = self.find_elements(self.__indicator_tab)
        for n in range(len(ele_list)):
            if ele_list[n].text == 'NEWS':
                ele_list[n].click()
        return VideoNewsPage(self.driver)

    def click_music_tab(self):
        """
        点击music tab
        :return:
        """
        self.slide_video_tab()
        ele_list = self.find_elements(self.__indicator_tab)
        for n in range(len(ele_list)):
            if ele_list[n].text == 'MUSIC':
                ele_list[n].click()
        return self

    def click_buzz_tab(self):
        """
        点击buzz tab
        :return:
        """
        self.slide_video_tab()
        ele_list = self.find_elements(self.__indicator_tab)
        for n in range(len(ele_list)):
            if ele_list[n].text == 'BUZZ':
                ele_list[n].click()
        return VideoBuzzPage(self.driver)

    def click_specified_tab(self, tab_name, tab_type=""):
        """
        点击指定 tab
        :param tab_name: tab 名称
        :param tab_type: 页面数据类型, 默认为video，可以选择news, buzz
        :return:
        """
        ele_list = self.find_elements(self.__indicator_tab)
        for n in range(len(ele_list)):
            if ele_list[n].text == tab_name:
                ele_list[n].click()
        if tab_type == "news":
            return VideoNewsPage(self.driver)
        if tab_type == "buzz":
            return VideoBuzzPage(self.driver)
        else:
            return self

    def slide_and_click_specified_tab(self, tab_name, tab_type=""):
        """
        滑动 tab 并点击指定tab
        :param tab_name: tab 名称
        :param tab_type: 页面数据类型, 默认为video，可以选择news, buzz
        """
        self.slide_video_tab()
        ele_list = self.find_elements(self.__indicator_tab)
        for n in range(len(ele_list)):
            if ele_list[n].text == tab_name:
                ele_list[n].click()
        if tab_type == "news":
            return VideoNewsPage(self.driver)
        if tab_type == "buzz":
            return VideoBuzzPage(self.driver)
        else:
            return self

    # def back_video_playlist_is_exist(self):
    #     """
    #     视频播放列表按钮存在
    #     :return:
    #     """
    #     return self.is_element_exist(self.__back_video_playlist)

    def get_you_may_like_title(self):
        """
        获取视频列表 you may like 标题
        :return:
        """
        return self.find_element_and_get_text(self.__you_may_like_title)

    def get_view_more_title(self):
        """
        获取查看更多 标题
        :return:
        """
        return self.find_element_and_get_text(self.__card_view_more)

    def get_music_view_more_title(self):
        """
        获取music卡 查看更多 标题
        :return:
        """
        return self.find_element_and_get_text(self.__music_view_more_title)

    def search_card(self, card_name, times=50):
        """
        滑动到指定卡片
        :param card_name: 卡片名称
        :return:
        """
        while times > 0:
            current_cards = self.get_cards_title()
            if card_name not in current_cards:
                self.slide_up_page()
                times -= 1
            else:
                print("find card:" + card_name)
                return True
        return False

    def click_view_more(self, option):
        """
        点击当前页面 第 option 个卡的查看更多
        :param option:
        :return:
        """
        self.find_elements(self.__card_view_more)[option].click()
        return CardViewMorePage(self.driver)

    def click_card_view_more(self, card_name, times=50):
        """
        点击指定卡片的查看更多按钮
        :param card_name: 卡片名称
        :return:
        """
        while times > 0:
            # 获取到当前页面的卡片名称
            # 如果需要点击的卡片不在当前页面，则向上滑动页面
            # 如果卡片在当前页面，则点击对应查看更多按钮
            current_cards = self.get_cards_title()
            if card_name not in current_cards:
                self.slide_up_page()
                times -= 1
            else:
                # 需要拼接，找到查看更多按钮："//*[@text='card_name']/../android.widget.TextView[2]
                view_more = (By.XPATH, "//*[@text='"+card_name+"']/../android.widget.TextView[2]")
                self.find_element_and_click(view_more)
                print("click card:" + card_name)
                break
        return CardViewMorePage(self.driver)

    def click_video(self):
        """
        点击视频列表 视频卡片，you may like
        :return:
        """
        self.find_elements(self.__video_list)[0].click()
        # sleep(1)
        return VideoDetailPage(self.driver)

    def get_banner_loc(self):
        """
        获取当前banner所在位置
        :return:
        """
        # click_banner_video()调用，需要处理语言弹窗
        try:
            return self.find_element_and_get_text(self.__banner_loc)
        except:
            self.click_app_content()
            sleep(1)
            if self.is_skip_exist():
                self.click_choose_language_skip()
            return self.find_element_and_get_text(self.__banner_loc)

    def click_select_banner(self, loc):
        """
        点击指定banner
        :return:
        :param: loc: 点击第 loc 个banner
        """
        while True:
            # 如果需要点击的卡片序号与
            banner_index = int(str(self.get_banner_loc()).split("/")[0])
            if loc != banner_index:
                self.slide_next_sheet(self.__banner_view, -600)
            else:
                self.find_element_and_click(self.__banner_view)
                break
        return VideoDetailPage(self.driver)

    def click_banner_video(self):
        """
        点击banner 自动播放视频卡片
        :return:
        """
        # 如果点击自动播放卡片定位不到，则尝试点击视频缩略图，中间会有几秒间隔
        while True:
            if "1/" in self.get_banner_loc():
                self.find_element_and_click(self.__banner_view)
                break
            else:
                self.slide_next_sheet(self.__banner_view, -400)
        return VideoDetailPage(self.driver)

    def get_cards_title(self):
        """
        获取页面全部卡片标题
        :return:
        """
        return self.find_elements_and_get_text(self.__card_title)

    def is_buzz_card_list_exist(self):
        """
        buzz 卡片列表是否存在
        :return:
        """
        return self.is_element_exist(self.__buzz_card_list)

    def watch_list_is_exist(self):
        """
        判断待看列表是否存在
        :return:
        """
        return self.is_element_exist(self.__watch_list)

    def click_watch_list_more(self):
        """
        点击待看列表 查看更多按钮
        :return:
        """
        try:
            self.find_element_and_click(self.__watch_list_more)
        except:
            self.slide_up_page()
            sleep(1)
            self.find_element_and_click(self.__watch_list_more)
        return WatchListPage(self.driver)

    def get_banner_num(self):
        """
        获取banner总数
        :return:
        """
        return int(str(self.get_banner_loc()).split("/")[1])

    def add_watch_list(self, banner_num):
        """
        点击添加banner视频到待看列表
        :return:
        """
        # 需要处理添加的视频不足2个
        for i in range(banner_num):
            try:
                self.find_element_and_click(self.__watch_button)
                toast = self.get_android_toast_text()
                if "从我的列表中移除" in toast:
                    self.find_element_and_click(self.__watch_button)
            except:
                self.click_app_content()
                sleep(1)
                if self.is_skip_exist():
                    self.click_choose_language_skip()
                self.find_element_and_click(self.__watch_button)
            self.slide_next_sheet(self.__banner_view, -400)
        return self


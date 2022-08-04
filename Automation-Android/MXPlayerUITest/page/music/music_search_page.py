import random
from selenium.webdriver.common.by import By

from page.music.music_base_page import MusicBasePage


class MusicSearchPage(MusicBasePage):
    """
    继承通用页面
    音乐搜索页面
    """
    # 搜索框
    __search_text = (By.ID, "com.mxtech.videoplayer.ad:id/search_edit")
    # 搜索框删除按钮
    __search_text_close = (By.ID, "com.mxtech.videoplayer.ad:id/search_edit_delete_btn")
    # 热门搜索列表
    __hot_list = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/content_text']")
    # 音频搜索按钮
    __voice_search = (By.ID, "com.mxtech.videoplayer.ad:id/voice_search")

    # 卡片列表标题 一组元素
    __cards_title = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/card_title']")
    # 卡片 查看更多 一组元素
    __cards_more = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/view_more']")
    # 查看更多页 标题
    __more_page_title = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/toolbar']/android.widget.TextView")
    # 搜索结果名称/播放列表名称 一组元素
    __title_list = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/title']")

    # 分享
    # 分享选项标题
    __share_app_title = (By.XPATH, "//*[@resource-id='android:id/text1']")

    def get_hot_list_10(self):
        """
        获取热门搜索列表
        :return:
        """
        hot_list = self.find_elements_and_get_text(self.__hot_list)
        hot_list_10 = hot_list[:10]
        return hot_list_10

    def is_search_text_exist(self):
        """
        判断搜索框是否存在
        :return:
        """
        return self.is_element_exist(self.__search_text)

    def click_search_edit_close(self):
        """
        点击搜索框中关闭按钮
        :return:
        """
        self.find_element_and_click(self.__search_text_close)
        return self

    def click_hot_item(self):
        """
        点击热门搜索中一条数据
        :return:
        """
        hot_list = self.find_elements(self.__hot_list)
        # 产生随机数
        num = random.randint(0, len(hot_list)-1)
        hot_list[num].click()
        return self

    def search_music(self, music):
        """
        搜索音乐
        :param music: 音乐名称
        :return:
        """
        self.find_element_and_send_keys(self.__search_text, music)
        self.driver.execute_script('mobile: performEditorAction', {'action': 'search'})
        return self

    def is_view_more_exist(self):
        """
        判断查看更多是否存在
        :return:
        """
        return self.is_element_exist(self.__cards_more)

    def get_card_title(self):
        """
        获取卡片类别标题
        :return:
        """
        return self.find_elements_and_get_text(self.__cards_title)

    def get_search_title_list(self):
        """
        获取搜索结果列表
        :return:
        """
        return self.find_elements_and_get_text(self.__title_list)

    def get_playlist_text(self):
        """
        获取到播放列表名称
        :return:
        """
        all_text = self.find_elements_and_get_text(self.__title_list)
        playlist = all_text[2:]
        return playlist

    def get_share_app_title(self):
        """
        获取分享弹窗中app名称
        :return:
        """
        return self.find_elements_and_get_text(self.__share_app_title)

    def get_view_more_text(self):
        """
        获取查看更多文案
        :return:
        """
        return self.find_elements_and_get_text(self.__cards_more)

    def click_cards_more(self, index):
        """
        点击查看更多
        :return:
        """
        more_buttons = self.find_elements(self.__cards_more)
        more_buttons[index].click()
        return self

    def get_more_page_title(self):
        """
        获取查看更多页面标题
        :return:
        """
        return self.find_element_and_get_text(self.__more_page_title)

from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.base_page import BasePage


class MusicBasePage(BasePage):
    """
    音乐基本页面
    继承通用页面
    """
    # 返回按钮
    __back_button = (By.XPATH, "//android.widget.ImageButton[@content-desc='转到上一层级']")
    # 搜索框
    __search_edit = (By.ID, "com.mxtech.videoplayer.ad:id/search_edit")
    # 搜索框 关闭按钮
    __search_edit_close = (By.ID, "com.mxtech.videoplayer.ad:id/iv_close")
    # 搜索框 取消按钮
    __search_cancel = (By.ID, "com.mxtech.videoplayer.ad:id/tv_cancel")

    # 列表更多操作
    __action_more = (By.ID, "com.mxtech.videoplayer.ad:id/action_more")
    # 清除全部按钮
    __clear_all = (By.ID, "com.mxtech.videoplayer.ad:id/clear_all_layout")
    # 添加歌曲按钮
    __add_songs = (By.ID, "com.mxtech.videoplayer.ad:id/add_songs_layout")

    # 单首音乐选项按钮 一组元素
    __music_option = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/iv_music_option']")

    # 音乐选项列表名称
    __action_more_title = (By.ID, "com.mxtech.videoplayer.ad:id/title")
    # 接下来播放按钮
    __play_next = (By.ID, "com.mxtech.videoplayer.ad:id/play_next_layout")
    # 稍后播放按钮
    __play_later = (By.ID, "com.mxtech.videoplayer.ad:id/play_later_layout")
    # 添加到我的最爱
    __add_favorite = (By.ID, "com.mxtech.videoplayer.ad:id/add_favourite_layout")
    # 添加到播放列表
    __add_playlist = (By.ID, "com.mxtech.videoplayer.ad:id/add_to_playlist_layout")
    # 分享
    __share_button = (By.ID, "com.mxtech.videoplayer.ad:id/share_layout")

    # 迷你播放器的新手引导
    __gaana_tutorial = (By.ID, "com.mxtech.videoplayer.ad:layout/view_gaana_player_tutorial")
    # 迷你播放器 关闭按钮
    __music_close = (By.ID, "com.mxtech.videoplayer.ad:id/music_close")
    # 迷你播放器 标题
    __music_title = (By.ID, "com.mxtech.videoplayer.ad:id/music_title")
    # 迷你播放器 描述
    __music_desc = (By.ID, "com.mxtech.videoplayer.ad:id/music_des")
    # 添加到我的最爱 按钮
    __favorite_button = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/favourite_img' and @index='2']")
    # 音频播放按钮
    __play_button = (By.ID, "com.mxtech.videoplayer.ad:id/music_play")
    # 查看播放列表
    __mini_play_list = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/playlist_img' and @index='4']")

    # 创建播放列表
    # 播放列表 创建播放列表
    __new_playlist_icon = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/recycler_view']/android.view.ViewGroup[1]")
    # 播放列表 创建播放列表text
    __new_playlist_text = (By.ID, "com.mxtech.videoplayer.ad:id/edit")
    # 播放列表 创建播放列表 创建按钮
    __new_playlist_create = (By.ID, "com.mxtech.videoplayer.ad:id/tv_create")

    # 重命名歌单
    # 重命名歌单文本框
    __rename_text = (By.ID, "android:id/edit")

    def is_back_exist(self):
        """
        返回按钮是否存在
        :return:
        """
        return self.is_element_exist(self.__back_button)

    def get_search_text(self):
        """
        获取搜索框文案
        :return:
        """
        return self.find_element_and_get_text(self.__search_edit)

    def click_search_text(self):
        """
        点击搜索框
        :return:
        """
        self.find_element_and_click(self.__search_edit)
        return self

    def click_close(self):
        """
        点击搜索框关闭按钮
        :return:
        """
        self.find_element_and_click(self.__search_edit_close)
        return self

    def click_search_cancel(self):
        """
        点击搜索框取消按钮
        :return:
        """
        self.find_element_and_click(self.__search_cancel)
        return self

    def search_music(self, music):
        """
        搜索歌单中的音乐
        :param music: 音乐名称
        :return:
        """
        # 切换到sanmsung输入法
        # self.enable_samsungIME()
        self.find_element_and_click(self.__search_edit)
        self.find_element_and_send_keys(self.__search_edit, music)
        self.driver.execute_script('mobile: performEditorAction', {'action': 'search'})
        # 点击键盘上的搜索/回车按钮
        # self.press_code("KEYCODE_SEARCH")
        # self.press_code("KEYCODE_ENTER")
        # # 切换会appium输入法
        # self.enable_appium_UnicodeIME()
        return self

    def click_action_more(self):
        """
        点击更多操作
        :return:
        """
        self.find_element_and_click(self.__action_more)
        return self

    def clear_all(self):
        """
        点击清除全部
        :return:
        """
        try:
            WebDriverWait(self.driver, timeout=5, poll_frequency=0.5, ignored_exceptions=None). \
                until(expected_conditions.visibility_of_element_located(self.__clear_all))
            self.find_element_and_click(self.__clear_all)
        except:
            self.find_element_and_click(self.__clear_all)
        sleep(1)
        # 点击弹窗中确认按钮
        self.click_ok_button()
        return self

    def more_action_clear_all(self):
        """
        清除歌曲
        :return:
        """
        if self.is_element_exist(self.__action_more):
            self.click_action_more()
            sleep(1)
            self.clear_all()
        return self

    def click_options_add_songs(self):
        """
        点击选项中添加歌曲
        :return:
        """
        self.find_element_and_click(self.__add_songs)
        return self

    def add_more_songs(self):
        """
        点击选项，添加更多歌曲
        :return:
        """
        self.click_action_more()
        self.click_options_add_songs()
        return self

    def get_music_option(self):
        """
        获取音乐选项
        :return:
        """
        return self.find_elements(self.__music_option)

    def click_music_option(self, num):
        """
        点击制定位置音乐选项
        :return:
        """
        music_option_list = self.find_elements(self.__music_option)
        music_option_list[num].click()
        return self

    def get_action_more_title(self):
        """
        获取到更多选项标题, 或者其他情况单个标题
        :return:
        """
        return self.find_element_and_get_text(self.__action_more_title)

    def click_play_next(self):
        """
        点击接下来播放
        :return:
        """
        self.find_element_and_click(self.__play_next)
        return self

    def click_play_later(self):
        """
        点击稍后播放
        :return:
        """
        self.find_element_and_click(self.__play_later)
        return self

    def click_add_favorite(self):
        """
        点击添加到最爱
        :return:
        """
        self.find_element_and_click(self.__add_favorite)
        return self

    def click_add_playlist(self):
        """
        点击添加到播放列表
        :return:
        """
        self.find_element_and_click(self.__add_playlist)
        return self

    def click_share(self):
        """
        点击分享按钮
        :return:
        """
        self.find_element_and_click(self.__share_button)
        return self

    def click_gaana_tutorial(self):
        """
        点击迷你播放器新手引导
        :return:
        """
        if self.is_element_exist(self.__gaana_tutorial):
            self.find_element_and_click(self.__gaana_tutorial)
        return self

    def close_mini_player(self):
        """
        点击关闭迷你播放器
        :return:
        """
        try:
            self.find_element_and_click(self.__music_close)
        except:
            # 处理首次点击关闭时出现新手引导蒙层
            self.click_gaana_tutorial()
            self.find_element_and_click(self.__music_close)
        return self

    def is_mini_music_title_exist(self):
        """
        判断迷你播放器音乐名称是否存在
        :return:
        """
        return self.is_element_exist(self.__music_title)

    def get_music_title(self):
        """
        获取迷你播放器音乐名称
        :return:
        """
        return self.find_element_and_get_text(self.__music_title)

    def click_favorite_button(self):
        """
        点击添加到最爱
        添加成功有toast
        再次点击取消添加，没有toast
        :return:
        """
        self.find_element_and_click(self.__favorite_button)
        return self

    def click_play_button(self):
        """
        点击播放/暂停按钮
        :return:
        """
        self.find_element_and_click(self.__play_button)
        return self

    def click_mini_playlist(self):
        """
        点击迷你播放器中播放列表
        :return:
        """
        self.find_element_and_click(self.__mini_play_list)
        return self

    def click_mini_music_title(self):
        """
        点击迷你播放器中 音乐标题
        :return:
        """
        self.find_element_and_click(self.__music_title)
        return self

    def create_playlist_and_add(self, title):
        """
        创建新播放列表
        :param title: 播放列表名称
        :return:
        """
        # 点击创建新播放列表
        self.find_element_and_click(self.__new_playlist_icon)
        # 输入播放列表名称
        self.find_element_and_send_keys(self.__new_playlist_text, title)
        # 点击创建按钮
        self.find_element_and_click(self.__new_playlist_create)
        return self

    def rename_playlist(self, new_name):
        """
        重命名歌单
        :param new_name: 新名称
        :return:
        """
        # 点击重命名输入框，获取到光标
        self.find_element_and_click(self.__rename_text)
        # 删除原文案
        self.press_code("KEYCODE_DEL")
        # 输入新名称
        self.find_element_and_send_keys(self.__rename_text, new_name)
        # 点击确认
        self.click_ok_button()
        return self

    def loop_to_get_all_titles(self, locator):
        """
        获取音乐名称列表
        :return:
        """
        first_list = self.find_elements_and_get_text(locator)
        # 获取当前页面全部tab元素的text
        # 滑动页面后，获取当前页全部tab元素
        # 根据tab元素的text判断是否已存在在列表中
        # 如果 当前页最后一个元素不存在 ele_list_text 中，则继续滑动，并且将不存在的元素追加到ele_list_text中
        while True:
            self.slide_up_page()
            current_list = self.find_elements(locator)
            last_title = current_list[-1].text
            if last_title not in first_list:
                for n in range(len(current_list)):
                    if current_list[n].text not in first_list:
                        first_list.append(current_list[n].text)
            else:
                break
        return first_list


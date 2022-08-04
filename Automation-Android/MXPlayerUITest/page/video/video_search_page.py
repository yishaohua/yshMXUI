from time import sleep

from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.video.search_live_tv_page import SearchLiveTVPage
from page.video.search_movies_page import SearchMoviesPage
from page.video.search_music_page import SearchMusicPage
from page.video.search_shorts_page import SearchShortsPage
from page.video.search_shows_page import SearchShowsPage
from page.video.video_base_page import VideoBasePage
from page.video.video_search_result_page import VideoSearchResultPage


class VideoSearchPage(VideoBasePage):
    """
    继承通用页面，封装了一些方法
    video页面点击搜索 搜索页面
    """
    # 左上 返回到上一级按钮
    __back_button = (By.XPATH, "//android.widget.ImageButton[@content-desc=\"转到上一层级\"]")
    # 搜索输入框
    __search_edit_textview = (By.ID, "com.mxtech.videoplayer.ad:id/search_edit")
    # 浏览类型列表
    __browse_list = (By.ID, "com.mxtech.videoplayer.ad:id/browse_list")
    # 浏览类型按钮，这是一组元素
    __cover_images = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/browse_list']/android.widget.FrameLayout")
    # 热门搜索标题
    __hot_title = (By.ID, "com.mxtech.videoplayer.ad:id/hot_title")
    # 热门搜索列表，这是一组元素
    # __hot_list = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/hot_list']//android.widget.TextView")
    __hot_list = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/content_text']")

    def do_search(self, content):
        """
        点击搜索框，搜索指定content内容
        :param content: 搜索内容
        :return:
        """
        self.find_element_and_send_keys(self.__search_edit_textview, content)
        self.driver.execute_script('mobile: performEditorAction', {'action': 'search'})
        return VideoSearchResultPage(self.driver)

    def get_browse_list(self):
        """
        获取到浏览类型列表
        :return:
        """
        self.find_element(self.__browse_list)
        return self

    def get_cover_images_shows(self, page, option):
        """
        点击浏览类型图片中 第 page 页的第 option 个卡片 shows
        :return: 返回到 shows 列表页
        :param: page: 滑动到第 n 页卡片, n>=1
        :param: option: 图片下标, 一页有4个卡, 取值范围：0-3
        """
        if page <= 1:
            self.find_elements(self.__cover_images)[option].click()
        else:
            for i in range(page-1):
                self.slide_next_sheet(self.__browse_list, x_distance=-600)
            self.find_elements(self.__cover_images)[option].click()
        return SearchShowsPage(self.driver)

    def get_cover_images_movies(self, page, option):
        """
        点击浏览类型图片中 第 page 页的第 option 个卡片 movies
        :return: 返回到 movies 列表页
        :param: page: 滑动到第 n 页卡片, n>=1
        :param: option: 图片下标, 一页有4个卡, 取值范围：0-3
        """
        if page <= 1:
            self.find_elements(self.__cover_images)[option].click()
        else:
            for i in range(page-1):
                self.slide_next_sheet(self.__browse_list, x_distance=-600)
            self.find_elements(self.__cover_images)[option].click()
        return SearchMoviesPage(self.driver)

    def get_cover_images_music(self, page, option):
        """
        点击浏览类型图片中 第 page 页的第 option 个卡片 music
        :return: 返回到 music 列表页
        :param: page: 滑动到第 n 页卡片, n>=1
        :param: option: 图片下标, 一页有4个卡, 取值范围：0-3
        """
        if page <= 1:
            self.find_elements(self.__cover_images)[option].click()
        else:
            for i in range(page-1):
                self.slide_next_sheet(self.__browse_list, x_distance=-600)
            self.find_elements(self.__cover_images)[option].click()
        return SearchMusicPage(self.driver)

    def get_cover_images_live_tv(self, page, option):
        """
        点击浏览类型图片中 第 page 页的第 option 个卡片 live TV
        :return: 返回到 live TV 列表页
        :param: page: 滑动到第 n 页卡片, n>=1
        :param: option: 图片下标, 一页有4个卡, 取值范围：0-3
        """
        if page <= 1:
            self.find_elements(self.__cover_images)[option].click()
        else:
            for i in range(page-1):
                self.slide_next_sheet(self.__browse_list, x_distance=-600)
            self.find_elements(self.__cover_images)[option].click()
        return SearchLiveTVPage(self.driver)

    def get_cover_images_shorts(self, page, option):
        """
        点击浏览类型图片中的第 第 page 页的第 option 个卡片 Shorts
        :return: 返回到 Shorts 列表页
        :param: page: 滑动到第 n 页卡片, n>=1
        :param: option: 图片下标, 一页有4个卡, 取值范围：0-3
        """
        if page <= 1:
            self.find_elements(self.__cover_images)[option].click()
        else:
            for i in range(page-1):
                self.slide_next_sheet(self.__browse_list, x_distance=-600)
            self.find_elements(self.__cover_images)[option].click()
        return SearchShortsPage(self.driver)

    def get_search_title_text(self):
        """
        获取热门搜索标题
        :return: 返回标题文案
        """
        return self.find_element_and_get_text(self.__hot_title)

    def hot_title_is_exit(self):
        """
        判断热门搜索标题是否存在
        :return:
        """
        return self.is_element_exist(self.__hot_title)

    def get_hot_list_text(self):
        """
        获取热门搜索列表
        :return: 返回热门搜索列表的文案，是一个列表
        """
        return self.find_elements_and_get_text(self.__hot_list)


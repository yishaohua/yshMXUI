from time import sleep

from selenium.webdriver.common.by import By

from page.video.video_base_page import VideoBasePage


class VideoSearchResultPage(VideoBasePage):
    """
    继承通用页面
    video 搜索结果页面
    """
    # 搜索框
    __search_edit_text = (By.ID, "com.mxtech.videoplayer.ad:id/search_edit")
    # 搜索框 删除搜索内容按钮
    __search_edit_delete = (By.ID, "com.mxtech.videoplayer.ad:id/search_edit_delete_btn")
    # youtube 按钮
    __youtube_tab = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/title_container']/android.widget.TextView[1]")
    # all 按钮
    __all_tab = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/title_container']/android.widget.TextView[2]")
    # 排序按钮
    __sort_button = (By.ID, "com.mxtech.videoplayer.ad:id/sort_img")
    # 筛选器按钮
    __filter_button = (By.ID, "com.mxtech.videoplayer.ad:id/filter_img")
    # 仅显示可下载选项开关
    __download_content_switch = (By.ID, "com.mxtech.videoplayer.ad:id/download_content_switch")
    # 搜索结果视频标题 一组元素
    __video_title = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/title']")
    # 筛选器标签
    __filter_title_list = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/filter_title']")
    # 筛选器list
    __filter_title_container = (By.ID, "com.mxtech.videoplayer.ad:id/filter_title_list")

    # 排序选项 关闭按钮
    __sort_close = (By.ID, "com.mxtech.videoplayer.ad:id/close_img")
    # 排序选项 relevance
    __sort_by_relevance = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/list_view']/android.view.ViewGroup[1]")
    # 排序选项 recency
    __sort_by_recency = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/list_view']/android.view.ViewGroup[2]")

    # 筛选器选项 language
    __filter_language = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/title_list_view']/android.widget.RelativeLayout[1]")
    # 筛选器选项 duration
    __filter_duration = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/title_list_view']/android.widget.RelativeLayout[2]")
    # 筛选器选项 release year
    __filter_release_year = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/title_list_view']/android.widget.RelativeLayout[3]")
    # 筛选器对应选项 文案
    __filter_option_text = (By.ID, "com.mxtech.videoplayer.ad:id/content_tv")
    # 筛选器 重置按钮
    __filter_reset = (By.ID, "com.mxtech.videoplayer.ad:id/reset_tv")
    # 筛选器 应用按钮
    __filter_apply = (By.ID, "com.mxtech.videoplayer.ad:id/apply_tv")

    def do_search(self, content):
        """
        点击搜索框，搜索指定content内容
        :param content: 搜索内容
        :return:
        """
        self.find_element_and_send_keys(self.__search_edit_text, content)
        self.driver.execute_script('mobile: performEditorAction', {'action': 'search'})
        return self

    def get_search_text(self):
        """
        获取搜索框搜索文案
        :return:
        """
        return self.find_element_and_get_text(self.__search_edit_text)

    def click_search_edit_delete(self):
        """
        点击搜索框删除按钮
        :return:
        """
        self.find_element_and_click(self.__search_edit_delete)
        return self

    def click_youtube_tab(self):
        """
        点击youtube tab
        :return:
        """
        self.find_element_and_click(self.__youtube_tab)
        return self

    def click_all_tab(self):
        """
        点击all tab
        :return:
        """
        self.find_element_and_click(self.__all_tab)
        return self

    def click_sort_button(self):
        """
        点击排序按钮
        :return:
        """
        self.find_element_and_click(self.__sort_button)
        return self

    def click_filter_button(self):
        """
        点击筛选器按钮
        :return:
        """
        self.find_element_and_click(self.__filter_button)
        return self

    def click_sort_close(self):
        """
        点击排序关闭按钮
        :return:
        """
        self.find_element_and_click(self.__sort_close)
        return self

    def sort_by_relevance(self):
        """
        选择排序方式 relevance
        :return:
        """
        self.find_element_and_click(self.__sort_by_relevance)
        return self

    def sort_by_recency(self):
        """
        选择排序方式 recency
        :return:
        """
        self.find_element_and_click(self.__sort_by_recency)
        return self

    def click_language(self):
        """
        点击选择语言过滤器
        :return:
        """
        self.find_element_and_click(self.__filter_language)
        return self

    def click_duration(self):
        """
        点击选择时长过滤器
        :return:
        """
        self.find_element_and_click(self.__filter_duration)
        return self

    def click_release_year(self):
        """
        点击选择上线年份过滤器
        :return:
        """
        self.find_element_and_click(self.__filter_release_year)
        return self

    def click_filter_reset(self):
        """
        筛选器点击重置
        :return:
        """
        self.find_element_and_click(self.__filter_reset)
        return self

    def click_filter_apply(self):
        """
        筛选器点击应用
        :return:
        """
        self.find_element_and_click(self.__filter_apply)
        return self

    def get_filter_options_num(self):
        """
        获取筛选器选项数
        :return:
        """
        options = self.find_elements(self.__filter_option_text)
        return len(options)

    def choose_filter_option(self, option):
        """
        选择对应选项 单个选项
        例如 option = "English"
        :return:
        """
        options = self.find_elements(self.__filter_option_text)
        for i in range(len(options)):
            if options[i].text in option:
                options[i].click()
        return self

    def choose_filter_options(self, option_list):
        """
        选择对应选项 多个选项
        例如 option_list = ["Hindi","English"]
        :return:
        """
        options = self.find_elements(self.__filter_option_text)
        for i in range(len(options)):
            for j in range(len(option_list)):
                if options[i].text == option_list[j]:
                    options[i].click()
                else:
                    continue
        return self

    def click_download_content_switch(self):
        """
        点击仅选择可下载选项开关
        :return:
        """
        self.find_element_and_click(self.__download_content_switch)
        return self

    def download_switch_is_exist(self):
        """
        断言下载选项开关是否存在
        :return:
        """
        return self.is_element_exist(self.__download_content_switch)

    def get_video_title(self):
        """
        获取视频标题
        :return:
        """
        return self.find_elements_and_get_text(self.__video_title)

    def get_one_filter(self):
        """
        获取筛选器标题
        :return:
        """
        return self.find_element_and_get_text(self.__filter_title_list)

    def slide_filter_title(self):
        """
        向左滑动筛选标签列表
        :return:
        """
        self.slide_next_sheet(self.__filter_title_container, -400)
        return self

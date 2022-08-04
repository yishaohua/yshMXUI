from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.video.video_base_page import VideoBasePage
from page.video.video_detail_page import VideoDetailPage


class SearchShowsPage(VideoBasePage):
    """
    继承通用页面
    video页面点击搜索，选择浏览shows卡片，进入shows列表
    """
    # 排序规则选择按钮
    __queue_button = (By.ID, "com.mxtech.videoplayer.ad:id/action_queue")
    # 筛选器按钮
    __filter_button = (By.ID, "com.mxtech.videoplayer.ad:id/action_sort")
    # 下载开关
    __download_switch = (By.ID, "com.mxtech.videoplayer.ad:id/download_content_switch")
    # 视频列表
    __video_list = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/rv_flow_fragment']/android.view.ViewGroup")
    # 视频播放数
    __video_count_one = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/rv_flow_fragment']/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.TextView")

    # 排序规则选项列表  人气，新旧
    __queue_items = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/queue_tv']")

    # 筛选器选项 language
    __filter_language = (
    By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/title_list_view']/android.widget.RelativeLayout[1]")
    # 筛选器选项 genre
    __filter_genre = (
    By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/title_list_view']/android.widget.RelativeLayout[2]")
    # 筛选器选项 actor
    __filter_actor = (
    By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/title_list_view']/android.widget.RelativeLayout[3]")
    # 筛选器选项 release year
    __filter_release_year = (
        By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/title_list_view']/android.widget.RelativeLayout[4]")
    # 筛选器对应选项 文案
    __filter_option_text = (By.ID, "com.mxtech.videoplayer.ad:id/content_tv")
    # 筛选器 重置按钮
    __filter_reset = (By.ID, "com.mxtech.videoplayer.ad:id/reset_tv")
    # 筛选器 应用按钮
    __filter_apply = (By.ID, "com.mxtech.videoplayer.ad:id/apply_tv")

    def click_queue_button(self):
        """
        点击排序规则按钮
        :return:
        """
        self.find_element_and_click(self.__queue_button)
        return self

    def get_queue_items_text(self):
        """
        获取排序规则选项列表文案
        :return:
        """
        return self.find_elements_and_get_text(self.__queue_items)

    def click_queue_item(self, item):
        """
        点击排序规则中选项
        :param item: 人气，新旧
        :return:
        """
        items_list = self.find_elements(self.__queue_items)
        for i in range(len(items_list)):
            if items_list[i].text == item:
                items_list[i].click()
        return self

    def click_filter_button(self):
        """
        点击筛选器按钮
        :return:
        """
        # print(self.driver.page_source)
        sleep(1)
        self.find_element_and_click(self.__filter_button)
        return self

    def click_language(self):
        """
        点击选择语言过滤器
        :return:
        """
        try:
            WebDriverWait(self.driver, timeout=5, poll_frequency=0.5, ignored_exceptions=None). \
                until(expected_conditions.visibility_of_element_located(self.__filter_language))
            self.find_element_and_click(self.__filter_language)
        except:
            self.find_element_and_click(self.__filter_language)
        return self

    def click_genre(self):
        """
        点击选择类型过滤器
        :return:
        """
        try:
            WebDriverWait(self.driver, timeout=5, poll_frequency=0.5, ignored_exceptions=None). \
                until(expected_conditions.visibility_of_element_located(self.__filter_genre))
            self.find_element_and_click(self.__filter_genre)
        except:
            self.find_element_and_click(self.__filter_genre)
        return self

    def click_actor(self):
        """
        点击选择演员过滤器
        :return:
        """
        try:
            WebDriverWait(self.driver, timeout=5, poll_frequency=0.5, ignored_exceptions=None). \
                until(expected_conditions.visibility_of_element_located(self.__filter_actor))
            self.find_element_and_click(self.__filter_actor)
        except:
            self.find_element_and_click(self.__filter_actor)
        return self

    def click_release_year(self):
        """
        点击选择上线年份过滤器
        :return:
        """
        try:
            WebDriverWait(self.driver, timeout=5, poll_frequency=0.5, ignored_exceptions=None). \
                until(expected_conditions.visibility_of_element_located(self.__filter_release_year))
            self.find_element_and_click(self.__filter_release_year)
        except:
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
        option="English"
        :return:
        """
        sleep(1)
        options = self.find_elements(self.__filter_option_text)
        for i in range(len(options)):
            if options[i].text == option:
                options[i].click()
        return self

    def choose_filter_options(self, option_list):
        """
        选择对应选项 多个选项
        option_list=["English", "Hindi"]
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
        self.find_element_and_click(self.__download_switch)
        return self

    def is_download_switch_exist(self):
        """
        下载按钮是否存在
        :return:
        """
        return self.is_element_exist(self.__download_switch)

    def get_download_switch_text(self):
        """
        获取下载开关文案 关闭/开启
        :return:
        """
        return self.find_element_and_get_text(self.__download_switch)

    def click_video_card(self):
        """
        点击视频卡片
        :return:
        """
        video_list = self.find_elements(self.__video_list)
        video_list[0].click()
        return VideoDetailPage(self.driver)

    def is_video_count_exit(self):
        """
        判断视频观看数是否存在
        :return:
        """
        return self.is_element_exist(self.__video_count_one)

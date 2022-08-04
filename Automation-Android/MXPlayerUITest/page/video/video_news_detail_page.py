from selenium.webdriver.common.by import By

from page.video.video_base_page import VideoBasePage


class VideoNewsDetailPage(VideoBasePage):
    """
    继承一个通用页面  通用页面封装了一些通用方法和异常处理
    视频 news 详情页面
    """
    # 当前节目标题
    __tv_title = (By.ID, "com.mxtech.videoplayer.ad:id/top_title")
    # 节目副标题
    __tv_dec = (By.ID, "com.mxtech.videoplayer.ad:id/top_dec")
    # 节目详细信息按钮
    __info_button = (By.ID, "com.mxtech.videoplayer.ad:id/info_img")
    # 视频下载按钮
    __video_download = (By.ID, "com.mxtech.videoplayer.ad:id/video_download")
    # 上一个节目按钮
    __last_program = (By.ID, "com.mxtech.videoplayer.ad:id/last_program")
    # 节目日期
    __program_time = (By.ID, "com.mxtech.videoplayer.ad:id/program_time")
    # 下一个节目按钮
    __next_program = (By.ID, "com.mxtech.videoplayer.ad:id/next_program")
    # 正在播放按钮
    __playing_button = (By.ID, "com.mxtech.videoplayer.ad:id/playing_text")

    # 节目名称 一组元素
    __program_title_list = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/tv_program_title']")
    # 节目播出时间 一组元素，与节目名称对应
    __program_time_list = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/tv_program_time']")
    # 当前频道icon
    __select_channel = (By.ID, "com.mxtech.videoplayer.ad:id/avatar_select")
    # 其他频道icon 列表
    __unselected_channels = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/avatar_normal']")
    # 当前频道名称
    __channel_title = (By.ID, "com.mxtech.videoplayer.ad:id/bottom_channel_text")
    # 底部频道列表按钮
    __channel_list_btn = (By.ID, "com.mxtech.videoplayer.ad:id/channel_list_btn")

    def get_tv_title(self):
        """
        获取当前节目标题
        :return:
        """
        return self.find_element_and_get_text(self.__tv_title)

    def get_tv_dec(self):
        """
        获取当前节目副标题 日期
        :return:
        """
        return self.find_element_and_get_text(self.__tv_dec)

    def click_info_button(self):
        """
        点击节目详细信息按钮
        :return:
        """
        self.find_element_and_click(self.__info_button)
        return self

    def click_download_btn(self):
        """
        点击视频下载按钮
        :return:
        """
        if self.is_element_exist(self.__video_download):
            self.find_element_and_click(self.__video_download)
        else:
            print("there is no download!")
        return self

    def click_last_program(self):
        """
        点击上一个节目
        :return:
        """
        self.find_element_and_click(self.__last_program)
        return self

    def click_next_program(self):
        """
        点击下一个节目
        :return:
        """
        self.find_element_and_click(self.__next_program)
        return self

    def get_program_time(self):
        """
        获取当前节目日期
        :return:
        """
        return self.find_element_and_get_text(self.__program_time)

    def click_playing_button(self):
        """
        点击正在播放按钮
        :return:
        """
        self.find_element_and_click(self.__playing_button)
        return self

    def get_program_title_list(self):
        """
        获取节目标题列表
        :return:
        """
        return self.find_elements_and_get_text(self.__program_title_list)

    def get_program_time_list(self):
        """
        获取节目时间列表
        :return:
        """
        return self.find_elements_and_get_text(self.__program_time_list)

    def click_other_channel(self, option: int):
        """
        点击非当前频道
        :param option: 频道下标，从0开始
        :return:
        """
        channels = self.find_elements(self.__unselected_channels)
        channels[option].click()
        return self

    def get_channel_title(self):
        """
        获取当前频道名称
        :return:
        """
        return self.find_element_and_get_text(self.__channel_title)

    def click_channel_list(self):
        """
        点击底部频道列表按钮
        :return:
        """
        self.find_element_and_click(self.__channel_list_btn)
        return self

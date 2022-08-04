from selenium.webdriver.common.by import By

from page.video.video_base_page import VideoBasePage


class DownloadPage(VideoBasePage):
    """
    通知页面
    继承通用页面
    """
    # 智能下载提示文案
    __bubble = (By.ID, "com.mxtech.videoplayer.ad:id/bubbleLayout")
    # 智能下载开关按钮，文案："智能下载: 开"
    __smart_download_button = (By.ID, "com.mxtech.videoplayer.ad:id/download_smart_switch")
    # you may like标题
    __des_text = (By.ID, "com.mxtech.videoplayer.ad:id/tv_des")
    # 推荐视频下载按钮
    __download_recommend_btn = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/download_recommend_btn']")
    # 推荐视频名称
    __download_recommend_title = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/download_recommend_title']")
    # 第一个下载列表视频的名称
    __first_title = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/download_list']/android.view.ViewGroup[1]/android.widget.TextView[1]")

    # 智能下载弹窗
    # 弹窗标题
    __smart_download_title = (By.ID, "com.mxtech.videoplayer.ad:id/smart_download_dialog_switch_text")
    # 智能下载开关
    __smart_download_switch = (By.ID, "com.mxtech.videoplayer.ad:id/smart_download_dialog_switch")
    # 默认文案
    __default_text = (By.ID, "com.mxtech.videoplayer.ad:id/title")

    # 下载列表中所有视频, 一组元素
    __download_list = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/image_card_view']")
    # 下载列表中video名称
    __download_video_name = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/video_name']")
    # 下载列表中tv show名称
    __download_tv_show_name = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/tv_show_name']")

    # 视频播放页 播放区域
    __play_area = (By.ID, "com.mxtech.videoplayer.ad:id/player_view")

    def is_bubble_exist(self):
        """
        判断智能下载提示是否存在
        :return:
        """
        return self.is_element_exist(self.__bubble)

    def click_smart_download(self):
        """
        点击智能下载提示
        :return:
        """
        if self.is_bubble_exist():
            self.find_element_and_click(self.__bubble)
        else:
            self.find_element_and_click(self.__smart_download_button)
        return self

    def get_smart_download_title(self):
        """
        获取智能下载提示弹窗标题
        :return:
        """
        return self.find_element_and_get_text(self.__smart_download_title)

    def is_default_text_exist(self):
        """
        判断缺省文案是否存在
        :return:
        """
        return self.is_element_exist(self.__default_text)

    def get_default_text(self):
        """
        获取无下载时文案：空空如也
        :return:
        """
        return self.find_element_and_get_text(self.__default_text)

    def get_des_text(self):
        """
        获取you may like标题
        :return:
        """
        return self.find_element_and_get_text(self.__des_text)

    def click_download_recommend_btn(self):
        """
        点击推荐下载按钮，第一个
        :return:
        """
        recommends = self.find_elements(self.__download_recommend_btn)
        recommends[0].click()
        return self

    def get_download_recommend_titles(self):
        """
        获取推荐视频标题
        :return:
        """
        return self.find_elements_and_get_text(self.__download_recommend_title)

    def get_download_list_count(self):
        """
        获取下载列表视频数量
        :return:
        """
        # 获取video数量
        video_list = self.find_elements(self.__download_video_name)
        video_count = len(video_list)
        # 获取tv show数量
        tv_show_list = self.find_elements(self.__download_tv_show_name)
        tv_show_count = len(tv_show_list)
        return video_count+tv_show_count

    def get_video_list_num(self):
        """
        获取下载列表数量
        :return:
        """
        video_list = self.find_elements(self.__download_list)
        return len(video_list)

    def click_download_video(self, option: int):
        """
        点击下载的视频
        :param option: 需要点击的视频下标，从 0 开始
        :return:
        """
        video_list = self.find_elements(self.__download_list)
        video_list[option].click()
        if self.is_element_exist(self.__play_area):
            return self
        elif self.is_element_exist(self.__download_video_name):
            self.find_element_and_click(self.__download_video_name)
            return self





from time import sleep

from selenium.webdriver.common.by import By

from page.base_page import BasePage


class AnchorMediaPage(BasePage):
    """
    继承一个通用页面
    主播媒体列表页面
    """
    # 用户名
    __user_name = (By.ID, "com.mxtech.videoplayer.ad:id/user_name")
    # 金币数量
    __user_coins = (By.ID, "com.mxtech.videoplayer.ad:id/user_coins")
    # 金币立即兑换按钮
    __earn_coins = (By.ID, "com.mxtech.videoplayer.ad:id/tv_earn_coins")
    # 我的下载按钮
    __my_download = (By.ID, "com.mxtech.videoplayer.ad:id/card_my_downloads")
    # 我的待看列表
    __my_video_playlist = (By.ID, "com.mxtech.videoplayer.ad:id/card_mx_mylist")
    # MX分享
    __mx_share = (By.ID, "com.mxtech.videoplayer.ad:id/card_mx_share")
    # 本地音乐
    __local_music = (By.ID, "com.mxtech.videoplayer.ad:id/card_mx_share")
    # 应用语言
    __app_language = (By.ID, "com.mxtech.videoplayer.ad:id/tv_app_language")
    # 内容语言
    __content_language = (By.ID, "com.mxtech.videoplayer.ad:id/tv_content_language")
    # 默认使用在线视频开关
    __online_default = (By.ID, "com.mxtech.videoplayer.ad:id/switch_online_default")
    # 私密文件夹
    __private_folder = (By.ID, "com.mxtech.videoplayer.ad:id/tv_private_folder")
    # 均衡器
    __equalizer = (By.ID, "com.mxtech.videoplayer.ad:id/tv_equalizer")
    # 视频播放列表
    __video_playlist = (By.ID, "com.mxtech.videoplayer.ad:id/ll_video_playlist")
    # 观看历史
    __my_history = (By.ID, "com.mxtech.videoplayer.ad:id/tv_my_history")
    # 设置按钮
    __ll_settings = (By.ID, "com.mxtech.videoplayer.ad:id/ll_layout_settings")

    # 我的收藏夹
    __my_favorites_music = (By.ID, "com.mxtech.videoplayer.ad:id/tv_my_favourites_music")
    # 我的歌单
    __my_playlist_music = (By.ID, "com.mxtech.videoplayer.ad:id/tv_my_playlist")

    # 本地播放器设置
    __local_settings = (By.ID, "com.mxtech.videoplayer.ad:id/tv_local_settings")
    # 下载设置
    __download_settings = (By.ID, "com.mxtech.videoplayer.ad:id/tv_download_settings")
    # 自定义pip控制键
    __pip_control = (By.ID, "com.mxtech.videoplayer.ad:id/ll_pip_control_content")
    # 儿童模式开关
    __kids_mode_switch = (By.ID, "com.mxtech.videoplayer.ad:id/sc_kids_mode")
    # 安全内容模式开关
    __sc_safe_switch = (By.ID, "com.mxtech.videoplayer.ad:id/sc_safe_content")
    # 启用流量节省程序开关
    __data_save_switch = (By.ID, "com.mxtech.videoplayer.ad:id/enable_data_saver_switch")
    # 帮助按钮
    __help_button = (By.ID, "com.mxtech.videoplayer.ad:id/tv_help")
    # 注销按钮
    __logout_button = (By.ID, "com.mxtech.videoplayer.ad:id/tv_logout")

    # 下载设置页面，依次为 Low，Medium，High，HD，总是询问选项
    __download_select = (
    By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/quality_list']/android.view.ViewGroup")
    # 下载设置页面 总是询问选项
    __always_ask_select = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/quality_list']/android.view.ViewGroup[5]")

    def get_user_name(self):
        """
        获取用户名
        :return:
        """
        return self.find_element_and_get_text(self.__user_name)

    def click_content_language_button(self):
        """
        点击设置-内容用语言按钮
        :return:
        """
        self.find_element_and_click(self.__content_language)
        return self

    def choose_content_language(self):
        """
        选择内容语言
        :return:
        """
        self.click_content_language_button()
        sleep(2)
        self.click_ok_button()
        sleep(1)
        return self

    def click_settings(self):
        """
        点击设置选项
        :return:
        """
        self.find_element_and_click(self.__download_settings)
        return self

    def click_download_settings(self):
        """
        点击下载设置
        :return:
        """
        self.find_element_and_click(self.__download_settings)
        return self

    def click_always_ask(self):
        """
        点击下载设置中 总是询问
        :return:
        """
        self.find_element_and_click(self.__always_ask_select)
        sleep(1)
        return self

    def set_download_always_ask(self):
        """
        设置下载中总是询问
        :return:
        """
        for i in range(3):
            self.slide_up_page()
        self.click_download_settings()
        sleep(1)
        self.click_always_ask()
        return self

    def set_download(self, select: int):
        """
        设置 分辨率选项
        :param select:
        :return:
        """
        for i in range(3):
            self.slide_up_page()
        self.click_download_settings()
        sleep(1)
        options = self.find_elements(self.__download_select)
        options[select].click()
        return self
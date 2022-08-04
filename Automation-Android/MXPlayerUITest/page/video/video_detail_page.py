from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.video.video_detail_more_page import VideoDetailMorePage


class VideoDetailPage(BasePage):
    """
    继承一个通用页面  通用页面封装了一些通用方法和异常处理
    视频详情页
    """
    # 视频详情页 18周岁判断弹窗 确认按钮
    __age_confirm_ok_button = (By.XPATH, "//*[@text= '确认']")
    # 返回按钮
    __back_button = (By.XPATH, "//android.widget.ImageButton[@content-desc='转到上一层级']")
    # 视频扩展按钮 超级省流量按钮
    __action_video_extension = (By.ID, "com.mxtech.videoplayer.ad:id/action_video_extension")
    # 更多操作按钮
    __action_more = (By.ID, "com.mxtech.videoplayer.ad:id/action_more")
    # 视频播放区域
    __player_view = (By.ID, "com.mxtech.videoplayer.ad:id/player_view")
    # 视频中心区域
    __video_center = (By.ID, "com.mxtech.videoplayer.ad:id/center_view")
    # 视频播放 播放按钮
    __video_exo_play = (By.ID, "com.mxtech.videoplayer.ad:id/exo_play")
    # 视频播放 暂停按钮
    __video_exo_pause = (By.ID, "com.mxtech.videoplayer.ad:id/exo_pause")
    # 视频播放 当前播放分钟数
    __video_exo_position = (By.ID, "com.mxtech.videoplayer.ad:id/exo_position")
    # 视频播放 播放进度条
    __video_exo_progress = (By.ID, "com.mxtech.videoplayer.ad:id/exo_progress")
    # 视频播放 总时长
    __video_exo_duration = (By.ID, "com.mxtech.videoplayer.ad:id/exo_duration")
    # 视频播放 画中画按钮
    __video_portrait_pip = (By.ID, "com.mxtech.videoplayer.ad:id/portrait_pip")
    # 视频播放 全屏按钮
    __video_fullscreen = (By.ID, "com.mxtech.videoplayer.ad:id/exo_fullscreen")
    # 视频播放 重试按钮
    __video_retry = (By.ID, "com.mxtech.videoplayer.ad:id/retry_button")

    # 详情页面内容
    __detail_parent = (By.ID, "com.mxtech.videoplayer.ad:id/detail_parent")
    # 广告
    __video_ad_img = (By.ID, "com.mxtech.videoplayer.ad:id/ad_container")

    # 更多操作 画质按钮
    __action_bg_quality = (By.ID, "com.mxtech.videoplayer.ad:id/bg_quality")
    # 更多操作 默认画质
    __action_quality_default = (By.ID, "com.mxtech.videoplayer.ad:id/tv_quality_default")
    # 更多操作 速度按钮
    __action_bg_speed = (By.ID, "com.mxtech.videoplayer.ad:id/bg_speed")
    # 更多操作 默认速度
    __action_speed_default = (By.ID, "com.mxtech.videoplayer.ad:id/tv_speed_default")
    # 更多操作 字母按钮
    __action_bg_subtitles = (By.ID, "com.mxtech.videoplayer.ad:id/bg_subtitles")
    # 更多操作 默认字幕
    __action_subtitles_default = (By.ID, "com.mxtech.videoplayer.ad:id/tv_subtitles_default")

    # 更多操作 画质按钮--画质选项auto
    __bg_quality_auto = (By.XPATH, "//*[contains(@text,'Auto (data saver)')]")
    # 更多操作 画质按钮--画质选项144p
    __bg_quality_144p = (By.XPATH, "//*[contains(@text,'144p')]")
    # 更多操作 画质按钮--画质选项216p
    __bg_quality_216p = (By.XPATH, "//*[contains(@text,'216p')]")
    # 更多操作 画质按钮--画质选项270p
    __bg_quality_270p = (By.XPATH, "//*[contains(@text,'270p')]")
    # 更多操作 画质按钮--画质选项360p
    __bg_quality_360p = (By.XPATH, "//*[contains(@text,'360p')]")
    # 更多操作 画质按钮--画质选项480p
    __bg_quality_480p = (By.XPATH, "//*[contains(@text,'480p')]")
    # 更多操作 画质按钮--画质选项720p
    __bg_quality_720p = (By.XPATH, "//*[contains(@text,'720p')]")
    # 更多操作 画质按钮--画质选项1080p
    __bg_quality_1080p = (By.XPATH, "//*[contains(@text,'1080p')]")

    # 更多操作 速度按钮--0.5X
    __bg_speed_05x = (By.XPATH, "//*[contains(@text,'0.5x')]")
    # 更多操作 速度按钮--0.75X
    __bg_speed_075x = (By.XPATH, "//*[contains(@text,'0.75x')]")
    # 更多操作 速度按钮--常规
    __bg_speed_1x = (By.XPATH, "//*[contains(@text,'常规')]")
    # 更多操作 速度按钮--0.5X
    __bg_speed_15x = (By.XPATH, "//*[contains(@text,'1.5x')]")
    # 更多操作 速度按钮--0.5X
    __bg_speed_175x = (By.XPATH, "//*[contains(@text,'1.75x')]")
    # 更多操作 速度按钮--0.5X
    __bg_speed_2x = (By.XPATH, "//*[contains(@text,'2.0x')]")

    # 更多操作 字幕按钮--关闭字幕
    __bg_subtitles_close = (By.XPATH, "//*[contains(@text,'关闭字幕')]")
    # 更多操作 字幕按钮--英语字幕
    __bg_subtitles_English = (By.XPATH, "//*[contains(@text,'English')]")

    # TV视频标题
    __detail_title = (By.ID, "com.mxtech.videoplayer.ad:id/detail_tv_title")
    # movies视频标题
    __movie_title = (By.ID, "com.mxtech.videoplayer.ad:id/movie_title")
    # 视频展开按钮
    __iv_arrow_button = (By.ID, "com.mxtech.videoplayer.ad:id/iv_arrow")
    # 当前视频剧集
    __season_episode = (By.ID, "com.mxtech.videoplayer.ad:id/season_episode")
    # 视频上映日期
    __release_date = (By.ID, "com.mxtech.videoplayer.ad:id/date")
    # 视频年龄等级
    __tv_age_level = (By.ID, "com.mxtech.videoplayer.ad:id/tv_age_level")
    # 视频剧集名称
    __tv_episode_name = (By.ID, "com.mxtech.videoplayer.ad:id/detail_tv_episode_name")
    # 发布者名称
    __artist_title = (By.ID, "com.mxtech.videoplayer.ad:id/detail_artist_title")
    # 发布者头像
    __artist_image = (By.ID, "com.mxtech.videoplayer.ad:id/subscribe_image")
    # 发布者订阅数
    __artist_subscribe_count = (By.ID, "com.mxtech.videoplayer.ad:id/detail_artist_subscribe_count")
    # 订阅按钮
    __artist_subscribe_button = (By.ID, "com.mxtech.videoplayer.ad:id/subscribe_button")
    # 视频详细介绍
    __expand_content = (By.ID, "com.mxtech.videoplayer.ad:id/expand_content")
    # 视频语言类型
    __show_language = (By.ID, "com.mxtech.videoplayer.ad:id/show_language")
    # 视频类型
    __show_genres = (By.ID, "com.mxtech.videoplayer.ad:id/show_genres")
    # 演员
    __show_cast = (By.ID, "com.mxtech.videoplayer.ad:id/show_cast")
    # 关键词列表
    __actor_keyword = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/tv_keyword_pill_title']")

    # 待看列表 加号按钮
    __place_holder_button = (By.ID, "com.mxtech.videoplayer.ad:id/place_holder")
    # 待看列表 文案
    __add_watchlist_text = (By.ID, "com.mxtech.videoplayer.ad:id/playdetail_watchlist_tv")
    # 下载 选项按钮
    __download_option = (By.ID, "com.mxtech.videoplayer.ad:id/video_download")
    # 下载 文案
    __download_text = (By.ID, "com.mxtech.videoplayer.ad:id/playdetail_download_tv")
    # 点赞 按钮
    __like_button = (By.ID, "com.mxtech.videoplayer.ad:id/playdetail_like")
    # 点赞 文案
    __like_text = (By.ID, "com.mxtech.videoplayer.ad:id/playdetail_like_tv")
    # 分享 按钮
    __share_button = (By.ID, "com.mxtech.videoplayer.ad:id/share_place_holder")
    # 分享 文案
    __share_text = (By.ID, "com.mxtech.videoplayer.ad:id/playdetail_share_tv")
    # session 列表按钮，有1层可以拿到按钮，2层拿到文案 android.widget.FrameLayout[1]/android.widget.TextView
    __session_list = (By.ID, "com.mxtech.videoplayer.ad:id/seasions_recycler_view")
    # 视频卡片标题
    __video_card_title = (By.ID, "com.mxtech.videoplayer.ad:id/card_title")
    # 查看更多按钮
    __view_more = (By.XPATH, "//*[@text='查看更多']")
    # 剧集列表 一组元素
    __episodes_recycler_cards = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/episode_image_view_card']")
    # 剧集列表标题
    __episodes_title = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/play_episode']")
    # 当前正在播放的剧集
    __now_playing_tv = (By.ID, "com.mxtech.videoplayer.ad:id/now_playing_tv")
    # 相似节目标题
    __related_title = (By.ID, "com.mxtech.videoplayer.ad:id/related_card_title")
    # 相似节目卡片,3层拿到具体的视频卡片
    __related_cards = (By.XPATH, "//android.widget.FrameLayout[@resource-id='com.mxtech.videoplayer.ad:id/cover_image_container']")

    # 画中画模式
    # 系统 查找mx应用
    __mxplayer_app = (By.XPATH, "//*[@content-desc='MX 播放器']")
    # 系统 允许上层显示开关
    __switch = (By.ID, "android:id/switch_widget")

    # 分享弹窗标题
    __share_title = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/root_view']/android.widget.TextView")
    # 分享弹窗-whatsapp
    __share_whatsapp = (By.ID, "com.mxtech.videoplayer.ad:id/whats_app")
    # 分享弹窗 复制
    __share_copy = (By.ID, "com.mxtech.videoplayer.ad:id/copy")
    # 分享弹窗 更多
    __share_more = (By.ID, "com.mxtech.videoplayer.ad:id/more")
    # 分享弹窗 更多 分享渠道标题"分享"
    __share_more_title = (By.ID, "android:id/title")

    # 付费视频 logo
    __svod_logo = (By.ID, "com.mxtech.videoplayer.ad:id/tv_svod_logo")
    # 付费视频 提示信息
    __svod_info = (By.ID, "com.mxtech.videoplayer.ad:id/tv_svod_info")
    # 付费视频 价钱信息
    __svod_promp = (By.ID, "com.mxtech.videoplayer.ad:id/tv_svod_promo")
    # 付费视频 购买按钮
    __buy_now_button = (By.ID, "com.mxtech.videoplayer.ad:id/btn_svod_video_subscribe_now")

    def click_video_play(self):
        """
        点击视频播放区域
        :return:
        """
        self.find_element_and_click(self.__player_view)
        return self

    def click_video_center(self):
        """
        点击视频中心的按钮
        :return:
        """
        self.find_element_and_click(self.__video_center)
        return self

    def click_video_extension(self):
        """
        点击视频扩展按钮 省流量播放
        :return:
        """
        self.find_element_and_click(self.__action_video_extension)
        return self

    def click_action_more(self):
        """
        点击更多设置按钮
        :return:
        """
        self.find_element_and_click(self.__action_more)
        return self

    def click_quality(self):
        """
        点击画质按钮
        :return:
        """
        self.find_element_and_click(self.__action_bg_quality)
        return self

    def get_quality_default(self):
        """
        获取默认画质
        :return:
        """
        quality = self.find_element_and_get_text(self.__action_quality_default)
        return quality

    def click_quality_720p(self):
        """
        选择720p画质
        :return:
        """
        self.find_element_and_click(self.click_quality_720p())
        return self

    def click_speed(self):
        """
        点击速度按钮
        :return:
        """
        self.find_element_and_click(self.__action_bg_speed)
        return self

    def get_speed_default(self):
        """
        获取默认速度
        :return:
        """
        speed = self.find_element_and_get_text(self.__action_speed_default)
        return speed

    def click_speed_15(self):
        """
        选择1.5倍速
        :return:
        """
        self.find_element_and_click(self.__bg_speed_15x)
        return self

    def click_subtitles(self):
        """
        点击字幕按钮
        :return:
        """
        self.find_element_and_click(self.__action_bg_subtitles)
        return self

    def get_subtitles_default(self):
        """
        获取默认字幕
        :return:
        """
        subtitles = self.find_element_and_get_text(self.__action_subtitles_default)
        return subtitles

    def click_subtitles_english(self):
        """
        选择英语字幕
        :return:
        """
        self.find_element_and_click(self.__bg_subtitles_English)
        return self

    # def click_pip_button(self):
    #     """
    #     点击画中画按钮
    #     :return:
    #     """
    #     self.find_element_and_click(self.__video_portrait_pip)
    #     return VideoHomePage(self.driver)

    # def permit_pip_play(self):
    #     """
    #     画中画权限弹窗，允许画中画播放
    #     :return:
    #     """
    #     self.find_element_and_click(self.__video_portrait_pip)
    #     # 点击画中画权限弹窗中允许按钮
    #     self.click_ok_button()
    #     # 进入系统应用列表，滑动应用列表
    #     for i in range(5):
    #         self.slide_up_page()
    #         # 查找到MX 播放器app，打开权限弹窗
    #         ele = self.find_element(self.__mxplayer_app)
    #         if ele.text == "MX 播放器":
    #             ele.click()
    #             self.find_element_and_click(self.__switch)
    #     return self

    def click_fullscreen(self):
        """
        点击视频全屏按钮
        :return:
        """
        self.find_element_and_click(self.__video_fullscreen)
        return self

    def get_play_exo_position(self):
        """
        获取当前播放时长
        :return:
        """
        play_position = self.find_element_and_get_text(self.__video_exo_position)
        return play_position

    def get_exo_duration(self):
        """
        获取播放总时长
        :return:
        """
        duration = self.find_element_and_get_text(self.__video_exo_duration)
        return duration

    def get_video_title(self):
        """
        获取tv视频标题
        :return:
        """
        tv_video_title = self.find_element_and_get_text(self.__detail_title)
        return tv_video_title

    def get_movie_title(self):
        """
        获取movie视频标题
        :return:
        """
        movie_video_title = self.find_element_and_get_text(self.__movie_title)
        return movie_video_title

    def get_season_episode(self):
        """
        获取当前剧集
        :return:
        """
        season_episode = self.find_element_and_get_text(self.__season_episode)
        return season_episode

    def get_release_date(self):
        """
        获取剧集上映日期
        :return:
        """
        date = self.find_element_and_get_text(self.__release_date)
        return date

    def get_episode_name(self):
        """
        获取当前集名称
        :return:
        """
        episode_name = self.find_element_and_get_text(self.__tv_episode_name)
        return episode_name

    def click_arrow_button(self):
        """
        点击展开详情按钮
        :return:
        """
        self.find_element_and_click(self.__iv_arrow_button)
        return self

    def get_artist_name(self):
        """
        获取发布者名称
        :return:
        """
        artist = self.find_element_and_get_text(self.__artist_title)
        return artist

    def get_artist_subscribe_count(self):
        """
        获取订阅人数
        :return:
        """
        count = self.find_element_and_get_text(self.__artist_subscribe_count)
        return count

    def click_subscribe(self):
        """
        点击订阅按钮
        :return:
        """
        self.find_element_and_click(self.__artist_subscribe_button)
        return self

    def is_subscribe_exist(self):
        """
        判断订阅按钮是否存在
        :return:
        """
        return self.is_element_exist(self.__artist_subscribe_button)

    def get_subscribe_text(self):
        """
        获取订阅按钮文案，订阅/取消订阅
        :return:
        """
        text = self.find_element_and_get_text(self.__artist_subscribe_button)
        return text

    def get_video_content(self):
        """
        获取电影详细介绍
        :return:
        """
        content = self.find_element_and_get_text(self.__expand_content)
        return content

    def get_show_language(self):
        """
        获取视频语言
        :return:
        """
        language = self.find_element_and_get_text(self.__show_language)
        return language

    def get_show_genres(self):
        """
        获取视频类型
        :return:
        """
        genres = self.find_element_and_get_text(self.__show_genres)
        return genres

    def get_show_cast(self):
        """
        获取视频演员
        :return:
        """
        cast = self.find_element_and_get_text(self.__show_cast)
        return cast

    def get_actor_keyword(self):
        """
        获取关键词列表
        :return:
        """
        return self.find_elements_and_get_text(self.__actor_keyword)

    def click_place_holder(self):
        """
        点击添加待看列表
        :return:
        """
        self.find_element_and_click(self.__place_holder_button)
        return self

    def click_download_option(self):
        """
        点击下载按钮
        :return:
        """
        # 点击下载选项
        self.find_element_and_click(self.__download_option)
        return self

    def click_like(self):
        """
        点赞
        :return:
        """
        self.find_element_and_click(self.__like_button)
        return self

    def click_share_button(self):
        """
        点击分享按钮
        :return:
        """
        self.find_element_and_click(self.__share_button)
        return self

    def is_share_exist(self):
        """
        判断share分享文案是否存在
        :return:
        """
        return self.is_element_exist(self.__share_text)

    def click_share_whatsapp(self):
        """
        点击分享 选择whatsapp
        :return:
        """
        self.find_element_and_click(self.__share_whatsapp)
        # 后续需要添加分享到wechat逻辑
        return self

    def click_share_copy(self):
        """
        点击分享 选择复制
        :return:
        """
        self.find_element_and_click(self.__share_copy)
        # 点击后弹窗收起，会弹出toast提示
        return self

    def click_share_more(self):
        """
        点击分享 选择更多
        :return:
        """
        self.find_element_and_click(self.__share_more)
        return self

    def get_share_more_title(self):
        """
        获取分享更多 app选择标题
        :return:
        """
        title = self.find_element_and_get_text(self.__share_title)
        # "分享" 可以用来判断是否
        return title

    def click_age_confirm_ok(self):
        """
        点击 18周岁判断弹窗 确认按钮
        只有成人电影点击后会弹出该弹窗
        :return:
        """
        self.find_element_and_click(self.__age_confirm_ok_button)
        return self

    def get_card_title(self):
        """
        获取到卡片列表标题
        :return:
        """
        title = self.find_element_and_get_text(self.__video_card_title)
        return title

    def click_view_more(self):
        """
        点击查看更多按钮
        :return:
        """
        try:
            self.find_element_and_click(self.__view_more)
        except:
            self.slide_up_page()
            self.find_element_and_click(self.__view_more)
        return VideoDetailMorePage(self.driver)

    def get_now_playing_tv(self):
        """
        获取当前正在播放剧集
        :return:
        """
        text = self.find_element_and_get_text(self.__now_playing_tv)
        # "正在播放"
        return text

    def get_episode_list(self):
        """
        获取剧集列表
        :return:
        """
        episode_list = self.find_elements(self.__episodes_recycler_cards)
        return episode_list

    def get_episode_title(self):
        """
        获取剧集列表标题
        :return:
        """
        return self.find_elements_and_get_text(self.__episodes_title)

    def get_related_title(self):
        """
        获取相关视频标题
        :return:
        """
        title = self.find_element_and_get_text(self. __related_title)
        return title

    def get_related_video_list(self):
        """
        获取相关视频列表
        :return:
        """
        related_video_list = self.find_elements(self.__related_cards)
        return related_video_list

    def slide_up_page(self):
        """
        上滑详情页面
        :return:
        """
        # 获取当前页面像素
        # 非视频区域部分的元素打下
        s = self.get_element_size(self.__detail_parent)
        # 视频区域部分的元素大小
        video_size = self.get_element_size(self.__player_view)
        video_height = video_size['height']
        # sy和ey需要加上视频区域的height
        width = s['width']
        height = s['height']
        sx = width / 2
        sy = video_height + height * 2 / 3
        ey = video_height + height / 3
        # 滑动页面
        self.swipe(sx, sy, sx, ey, 500)
        return self

    def slide_down_page(self):
        """
        下拉详情页面
        :return:
        """
        # 获取当前页面像素
        s = self.get_element_size(self.__detail_parent)
        # 视频区域部分的元素大小
        video_size = self.get_element_size(self.__player_view)
        video_height = video_size['height']
        width = s['width']
        height = s['height']
        sx = width / 2
        sy = video_height + height / 3
        ey = video_height + height * 2 / 3
        # 滑动页面，从1/3高度滑到2/3高度
        self.swipe(sx, sy, sx, ey, 500)
        return self

    def get_svod_promp(self):
        """
        获取付费视频价格信息
        :return:
        """
        promp = self.find_element_and_get_text(self.__svod_promp)
        return promp

    def click_buy_now(self):
        """
        点击付费视频 buy now按钮
        :return:
        """
        self.find_element_and_click(self.__buy_now_button)
        return self

    def is_retry_exist(self):
        """
        判断 重试按钮是否存在
        :return:
        """
        return self.is_element_exist(self.__video_retry)

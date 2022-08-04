import random
from math import ceil
from time import sleep

from selenium.webdriver.common.by import By

from page.music.music_base_page import MusicBasePage


class MusicPlayPage(MusicBasePage):
    """
    继承通用页面
    播放音乐页面
    """
    # 关闭播放按钮
    __close_music_button = (By.ID, "com.mxtech.videoplayer.ad:id/music_close")
    # 音乐标题名称
    __music_title = (By.ID, "com.mxtech.videoplayer.ad:id/music_title")
    # 音乐二级标题
    __music_description = (By.ID, "com.mxtech.videoplayer.ad:id/music_des")
    # 分享按钮
    __music_share = (By.ID, "com.mxtech.videoplayer.ad:id/share_img")
    # 平衡器按钮
    __equalizer_button = (By.ID, "com.mxtech.videoplayer.ad:id/equalizer_img")
    # 选取小节循环播放按钮
    __abplay_button = (By.ID, "com.mxtech.videoplayer.ad:id/abplay_img")
    # 播放速度按钮
    __play_speed = (By.ID, "com.mxtech.videoplayer.ad:id/music_speed_img")
    # 添加到我的最爱按钮
    __favorite_button = (By.ID, "com.mxtech.videoplayer.ad:id/favourite_img")
    # 当前播放时长
    __current_position = (By.ID, "com.mxtech.videoplayer.ad:id/curr_pos_tv")
    # 总时长
    __music_duration = (By.ID, "com.mxtech.videoplayer.ad:id/duration_tv")
    # 随机播放按钮
    __shuffle_button = (By.ID, "com.mxtech.videoplayer.ad:id/music_shuffle")
    # 上一首
    __pre_button = (By.ID, "com.mxtech.videoplayer.ad:id/music_pre")
    # 播放/暂停按钮
    __play_button = (By.ID, "com.mxtech.videoplayer.ad:id/music_play")
    # 下一首
    __next_button = (By.ID, "com.mxtech.videoplayer.ad:id/music_next")
    # 循环播放按钮
    __rotate_button = (By.ID, "com.mxtech.videoplayer.ad:id/music_rotate")
    # 歌词按钮
    __lyrics_button = (By.ID, "com.mxtech.videoplayer.ad:id/lyrics_img")
    # 播放列表按钮文案
    __playlist_text = (By.ID, "com.mxtech.videoplayer.ad:id/playlist_tv")
    # 详细信息按钮
    __detail_button = (By.ID, "com.mxtech.videoplayer.ad:id/detail_img")

    # 详细信息
    # 详细信息 标题
    __detail_title = (By.ID, "com.mxtech.videoplayer.ad:id/title")
    # 详细信息 二级标题 一般为艺术家名称
    __detail_subtitle = (By.ID, "com.mxtech.videoplayer.ad:id/subtitle")
    # 艺术家名称
    __artist_text = (By.ID, "com.mxtech.videoplayer.ad:id/artist_tv")
    # 专辑列表名称
    __album_text = (By.ID, "com.mxtech.videoplayer.ad:id/album_tv")
    # 添加到播放列表
    __add_to_playlist = (By.ID, "com.mxtech.videoplayer.ad:id/add_to_playlist_tv")
    # 设置睡眠定时器按钮
    __sleep_timer = (By.ID, "com.mxtech.videoplayer.ad:id/sleep_timer_layout")

    # 搜索歌词弹窗
    # 搜索输入框
    __search_text = (By.ID, "com.mxtech.videoplayer.ad:id/edit_text")
    # 确认搜索按钮
    __ok_button = (By.ID, "com.mxtech.videoplayer.ad:id/ok")
    # 取消按钮
    __cancel_button = (By.ID, "com.mxtech.videoplayer.ad:id/cancel")
    # 搜索结果页面标题
    __search_page_title = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/toolbar']/android.widget.TextView")

    # 速度选择
    # 速度选择结果文案
    __speed_text = (By.ID, "com.mxtech.videoplayer.ad:id/music_speed_tv")
    # 速度选择列表
    __speed_list = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/bottom_panel']/android.widget.TextView")
    # 0.25X
    __speed0 = (By.ID, "com.mxtech.videoplayer.ad:id/speed0")
    # 0.5X
    __speed1 = (By.ID, "com.mxtech.videoplayer.ad:id/speed1")
    # Normal
    __speed2 = (By.ID, "com.mxtech.videoplayer.ad:id/speed2")
    # 1.5X
    __speed3 = (By.ID, "com.mxtech.videoplayer.ad:id/speed3")
    # 2X
    __speed4 = (By.ID, "com.mxtech.videoplayer.ad:id/speed4")

    # 均衡器
    # 均衡器开关
    __audio_effect_switch = (By.ID, "com.mxtech.videoplayer.ad:id/audio_effects_switch")

    # 循环播放小段
    # 起始按钮
    __start_button = (By.ID, "com.mxtech.videoplayer.ad:id/abplay_a_img")
    # 起始时间
    __start_time = (By.ID, "com.mxtech.videoplayer.ad:id/abplay_a_tv")
    # 终止按钮
    __end_button = (By.ID, "com.mxtech.videoplayer.ad:id/abplay_b_img")
    # 终止时间
    __end_time = (By.ID, "com.mxtech.videoplayer.ad:id/abplay_b_tv")
    # 关闭按钮
    __abplay_close = (By.ID, "com.mxtech.videoplayer.ad:id/abplay_close_img")

    # 播放队列
    # 播放队列
    __recycler_view = (By.ID, "com.mxtech.videoplayer.ad:id/recycler_view")
    # 播放队列歌曲数  (10)
    __count = (By.ID, "com.mxtech.videoplayer.ad:id/count")
    # 播放队列删除按钮
    __clear_button = (By.ID, "com.mxtech.videoplayer.ad:id/clear_btn")
    # 队列循环按钮
    __queue_shuffle = (By.ID, "com.mxtech.videoplayer.ad:id/shuffle_btn")
    # 单首歌曲排序拖动按钮 一组元素
    __drag_button = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/drag_img']")
    # 第一首歌曲拖动按钮
    __drag_one_button = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/recycler_view']/android.view.ViewGroup[1]/android.widget.ImageView[1]")
    __drag_three_button = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/recycler_view']/android.view.ViewGroup[3]/android.widget.ImageView[1]")
    # 单首歌曲删除按钮 一组元素
    __clear_one_button = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/close_img']")

    # 睡眠定时器
    # 标题
    __sleep_title = (By.ID, "com.mxtech.videoplayer.ad:id/title")
    # min15
    __after_min15 = (By.ID, "com.mxtech.videoplayer.ad:id/min15")
    # min30
    __after_min30 = (By.ID, "com.mxtech.videoplayer.ad:id/min30")
    # min45
    __after_min45 = (By.ID, "com.mxtech.videoplayer.ad:id/min45")
    # min60
    __after_min60 = (By.ID, "com.mxtech.videoplayer.ad:id/min60")
    # 自定义
    __after_custom = (By.ID, "com.mxtech.videoplayer.ad:id/custom")
    # 关闭
    __after_turn_off = (By.ID, "com.mxtech.videoplayer.ad:id/turn_off")
    # 歌曲结束
    __end_of_song = (By.ID, "com.mxtech.videoplayer.ad:id/end_of_song_switch")
    # 自定义 小时选择器
    __picker_hour = (By.XPATH, "//*[@resource-id='android:id/numberpicker_input']")


    def click_close_button(self):
        """
        点击关闭按钮
        :return:
        """
        self.find_element_and_click(self.__close_music_button)
        return self

    def get_music_des(self):
        """
        获取艺术家名称
        :return:
        """
        return self.find_element_and_get_text(self.__music_description)

    def get_music_title(self):
        """
        获取音乐标题按钮
        :return:
        """
        return self.find_element_and_get_text(self.__music_title)

    def click_share_button(self):
        """
        点击分享按钮
        :return:
        """
        self.find_element_and_click(self.__music_share)
        return self

    def click_equalizer(self):
        """
        点击平衡器按钮
        :return:
        """
        self.find_element_and_click(self.__equalizer_button)
        return self

    def click_abplay_button(self):
        """
        点击选取小节循环播放按钮
        :return:
        """
        self.find_element_and_click(self.__abplay_button)
        return self

    def click_speed_button(self):
        """
        点击选择速度按钮
        :return:
        """
        self.find_element_and_click(self.__play_speed)
        return self

    def get_speed_text(self):
        """
        获取播放速度文案
        :return:
        """
        return self.find_element_and_get_text(self.__speed_text)

    def choose_speed(self, speed):
        """
        选择播放速度
        :param speed:
        :return:
        """
        speed_list = self.find_elements(self.__speed_list)
        if speed == "0.25x":
            speed_list[0].click()
        elif speed == "0.5x":
            speed_list[1].click()
        elif speed == "Normal":
            speed_list[2].click()
        elif speed == "1.5x":
            speed_list[3].click()
        elif speed == "2.0x":
            speed_list[4].click()
        return self

    def click_favorite_button(self):
        """
        点击添加我的最爱按钮 弹出toast提示
        :return:
        """
        self.find_element_and_click(self.__favorite_button)
        return self

    def get_current_position(self):
        """
        获取总时长  0:09
        :return:
        """
        return self.find_element_and_get_text(self.__current_position)

    def get_duration(self):
        """
        获取总时长  3:44
        :return:
        """
        return self.find_element_and_get_text(self.__music_duration)

    def click_shuffle(self):
        """
        点击随机播放按钮, 会有toast
        :return:
        """
        self.find_element_and_click(self.__shuffle_button)
        return self

    def click_pre_button(self):
        """
        点击播放上一首按钮
        :return:
        """
        self.find_element_and_click(self.__pre_button)
        return self

    def click_play_button(self):
        """
        点击暂停/播放按钮
        :return:
        """
        self.find_element_and_click(self.__play_button)

    def click_next_button(self):
        """
        点击下一首按钮
        :return:
        """
        self.find_element_and_click(self.__next_button)
        return self

    def click_rotate_button(self):
        """
        点击循环播放按钮
        :return:
        """
        self.find_element_and_click(self.__rotate_button)
        return self

    def click_lyrics_button(self):
        """
        点击搜素歌词按钮
        :return:
        """
        self.find_element_and_click(self.__lyrics_button)
        return self

    def click_search_ok(self):
        """
        点击搜索歌词 确认按钮
        :return:
        """
        self.find_element_and_click(self.__ok_button)
        return self

    def get_search_title(self):
        """
        获取搜索歌词结果页面标题
        :return:
        """
        return self.find_element_and_get_text(self.__search_page_title)

    def click_detail_playlist(self):
        """
        点击播放队列按钮
        :return:
        """
        self.find_element_and_click(self.__playlist_text)
        return self

    def click_queue_shuffle(self):
        """
        点击循环播放按钮
        :return:
        """
        self.find_element_and_click(self.__queue_shuffle)
        return self

    def get_music_count(self):
        """
        获取音乐数
        :return:
        """
        count_text = self.find_element_and_get_text(self.__count)
        count = int(count_text.strip('()'))
        return count

    def get_current_music(self):
        """
        获取当前页面音乐列表名称
        :return:
        """
        all_list = self.find_elements_and_get_text(self.__detail_title)
        music_list = all_list[1:]
        return music_list

    def get_music_list(self):
        """
        获取播放队列歌曲名称
        :return:
        """
        count = self.get_music_count()
        num = ceil(count/3)
        first_list = self.find_elements_and_get_text(self.__detail_title)
        for i in range(num):
            self.slide_up_page()
            current_list = self.find_elements(self.__detail_title)
            last_title = current_list[-1].text
            if last_title not in first_list:
                for n in range(len(current_list)):
                    if current_list[n].text not in first_list:
                        first_list.append(current_list[n].text)
            else:
                break
        music_list = first_list[1:]
        return music_list

    def drag_music(self):
        """
        拖动音乐 将第1首歌拖动到第2首的位置
        :return:
        """
        self.drag_element(self.__drag_one_button, self.__drag_three_button)
        return self

    def get_clear_one(self, num):
        """
        获取音乐数
        :return:
        """
        clear_list = self.find_elements(self.__clear_one_button)
        clear_list[num].click()
        return self

    def click_detail_button(self):
        """
        点击查看详细信息按钮
        :return:
        """
        sleep(1)
        self.find_element_and_click(self.__detail_button)
        return self

    def get_detail_title(self):
        """
        获取详细信息标题
        :return:
        """
        return self.find_element_and_get_text(self.__detail_title)

    def click_add_to_playlist(self):
        """
        点击添加到播放列表
        :return:
        """
        self.find_element_and_click(self.__add_to_playlist)
        return self

    def open_effect_switch(self):
        """
        打开均衡器开关
        :return:
        """
        self.find_element_and_click(self.__audio_effect_switch)
        return self

    def get_effect_switch_text(self):
        """
        获取均衡器开关文案：开 开启；关 关闭
        :return:
        """
        return self.find_element_and_get_text(self.__audio_effect_switch)

    def choose_abplay(self, duration):
        """
        选择abplay起始时间
        :param duration: 时间间隔
        :return:
        """
        self.find_element_and_click(self.__start_button)
        sleep(duration)
        self.find_element_and_click(self.__end_button)
        return self

    def get_abplay_start_time(self):
        """
        获取abplay起始时间
        :return:
        """
        raw_time = self.find_element_and_get_text(self.__start_time)
        return self.convert_minutes_to_numbers(raw_time)

    def get_abplay_end_time(self):
        """
        获取abplay结束时间
        :return:
        """
        raw_time = self.find_element_and_get_text(self.__end_time)
        return self.convert_minutes_to_numbers(raw_time)

    def close_abplay(self):
        """
        关闭abplay
        :return:
        """
        self.find_element_and_click(self.__abplay_close)
        return self

    def click_sleep_timer(self):
        """
        点击设置睡眠定时器
        :return:
        """
        if self.is_element_exist(self.__sleep_timer):
            self.find_element_and_click(self.__sleep_timer)
        else:
            self.click_detail_button()
            self.find_element_and_click(self.__sleep_timer)
        return self

    def get_sleep_title(self):
        """
        获取睡眠定时关闭标题
        :return:
        """
        return self.find_element_and_get_text(self.__sleep_title)

    def click_sleep_after_30min(self):
        """
        点击30分钟后关闭
        :return:
        """
        self.find_element_and_click(self.__after_min30)
        return self

    def click_custom(self):
        """
        睡眠定时选择自定义
        :return:
        """
        self.find_element_and_click(self.__after_custom)
        return self

    def roll_to_two(self):
        """
        滚动小时选择器到2时
        :return:
        """
        self.swipe_control(self.__picker_hour, 0, -300)
        return self


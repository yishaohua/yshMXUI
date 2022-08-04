from time import sleep

from selenium.webdriver.common.by import By

from page.music.music_base_page import MusicBasePage


class LocalMusicPage(MusicBasePage):
    """
    继承通用页面
    本地音乐页面
    """
    # 在线音乐按钮
    __online_music = (By.ID, "com.mxtech.videoplayer.ad:id/tv_online_music")
    # 随机播放全部按钮
    __shuffle_all = (By.ID, "com.mxtech.videoplayer.ad:id/fl_shuffle")
    # 排序按钮
    __sort_button = (By.ID, "com.mxtech.videoplayer.ad:id/iv_sort")

    # 音乐卡片 标题
    __song_title = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/title']")
    # 音乐卡片 二级标题 艺术家名称
    __artist_name = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/subtitle']")

    # 排序选项
    # 标题
    __by_title = (By.XPATH, "//*[@text='标题']")
    # 时长
    __by_duration = (By.XPATH, "//*[@text='时长']")
    # 添加的日期
    __by_date = (By.XPATH, "//*[@text='添加的日期']")
    # 大小
    __by_size = (By.XPATH, "//*[@text='大小']")
    # 从A到Z/从长到短/从新到旧/从大到小
    __sort_by_1 = (By.ID, "com.mxtech.videoplayer.ad:id/rl_sort_by_1")
    # 从Z到A/从短到长/从旧到新/从小到大
    __sort_by_2 = (By.ID, "com.mxtech.videoplayer.ad:id/rl_sort_by_2")
    # 1分钟以上开关
    __one_min = (By.ID, "com.mxtech.videoplayer.ad:id/switch_one_min")
    # 完成按钮
    __done_button = (By.ID, "com.mxtech.videoplayer.ad:id/tv_done")
    # 取消按钮
    __cancel_button = (By.ID, "com.mxtech.videoplayer.ad:id/tv_cancel")

    # 音乐选项列表
    # 接下来播放按钮
    __play_next = (By.XPATH, "//*[@text='接下来播放']")
    # 稍后播放按钮
    __play_later = (By.XPATH, "//*[@text='稍后播放']")
    # 添加到我的最爱
    __add_favorite = (By.XPATH, "//*[@text='添加到最爱']")
    # 添加到播放列表
    __add_playlist = (By.XPATH, "//*[@text='添加到播放列表']")
    # 分享
    __share_button = (By.XPATH, "//*[@text='分享']")
    # 设置为铃声
    __set_as_ringtone = (By.XPATH, "//*[@text='设置为铃声']")
    # MX分享
    __mx_share = (By.XPATH, "//*[@text='MX分享']")
    # 重命名
    __rename_button = (By.XPATH, "//*[@text='重命名']")
    # 属性
    __attribute_button = (By.XPATH, "//*[@text='属性']")
    # 删除
    __delete_button = (By.XPATH, "//*[@text='删除']")

    # 创建播放列表
    # 播放列表 创建播放列表按钮
    __new_playlist = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/list']/android.view.ViewGroup[1]")
    # 播放列表 创建播放列表text
    __new_playlist_text = (By.ID, "com.mxtech.videoplayer.ad:id/edit")
    # 播放列表 创建播放列表 创建按钮
    __new_playlist_create = (By.ID, "com.mxtech.videoplayer.ad:id/tv_create")

    # 设置铃声
    # 来电铃声
    __phone_ringtone = (By.ID, "com.mxtech.videoplayer.ad:id/rb_phone_ringtone")
    # 闹钟铃声
    __alarm_ringtone = (By.ID, "com.mxtech.videoplayer.ad:id/rb_alarm_ringtone")
    # 通知铃声
    __notification_ringtone = (By.ID, "com.mxtech.videoplayer.ad:id/rb_notification_ringtone")

    # 属性列表
    # 大小
    __song_size = (By.XPATH, "//*[@text='大小']/../android.widget.TextView[2]")
    # 日期
    __song_date = (By.XPATH, "//*[@text='日期']/../android.widget.TextView[2]")
    # 时长
    __song_duration = (By.XPATH, "//*[@text='长度']/../android.widget.TextView[2]")
    # 文件标题
    __file_title = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/scroll_view']/android.widget.TableLayout/android.widget.TextView[1]")

    # 删除弹窗
    # 确认删除按钮
    __confirm_delete = (By.ID, "com.mxtech.videoplayer.ad:id/delete")
    # 取消删除按钮
    __cancel_delete = (By.ID, "com.mxtech.videoplayer.ad:id/cancel")

    # 允许修改系统设置权限
    __switch = (By.ID, "android:id/switch_widget")

    def click_online_music(self):
        """
        点击在线音乐
        :return:
        """
        self.find_element_and_click(self.__online_music)
        return self

    def click_songs_tab(self):
        """
        点击歌曲tab
        :return:
        """
        # tab栏的坐标 [18, 228][718, 369]
        # 大概估算 歌曲、专辑 分别150宽，艺术家、文件夹分别200宽
        self.find_element_and_press(100, 300)

    def click_albums_tab(self):
        """
        点击专辑tab
        :return:
        """
        self.find_element_and_press(200, 300)
        return self

    def click_artists_tab(self):
        """
        点击艺术家tab
        :return:
        """
        self.find_element_and_press(380, 300)
        return self

    def click_files_tab(self):
        """
        点击文件夹tab
        :return:
        """
        self.find_element_and_press(600, 300)
        return self

    def click_sort_button(self):
        """
        点击排序按钮
        :return:
        """
        self.find_element_and_click(self.__sort_button)
        return self

    def click_sort_by_title_a2z(self):
        """
        按照标题排序 a到z
        :return:
        """
        self.find_element_and_click(self.__by_title)
        self.find_element_and_click(self.__sort_by_1)
        self.find_element_and_click(self.__done_button)
        return self

    def click_sort_by_title_z2a(self):
        """
        按照标题排序 z到a
        :return:
        """
        self.find_element_and_click(self.__by_title)
        self.find_element_and_click(self.__sort_by_2)
        self.find_element_and_click(self.__done_button)
        return self

    def click_sort_by_duration_l2s(self):
        """
        按照时长排序 长到短
        :return:
        """
        self.find_element_and_click(self.__by_duration)
        self.find_element_and_click(self.__sort_by_1)
        self.find_element_and_click(self.__done_button)
        return self

    def click_sort_by_duration_s2l(self):
        """
        按照时长排序 短到长
        :return:
        """
        self.find_element_and_click(self.__by_duration)
        self.find_element_and_click(self.__sort_by_2)
        self.find_element_and_click(self.__done_button)
        return self

    def click_sort_by_date_n2o(self):
        """
        按照添加的日期排序 新到旧
        :return:
        """
        self.find_element_and_click(self.__by_date)
        self.find_element_and_click(self.__sort_by_1)
        self.find_element_and_click(self.__done_button)
        return self

    def click_sort_by_date_o2n(self):
        """
        按照添加的日期排序 旧到新
        :return:
        """
        self.find_element_and_click(self.__by_date)
        self.find_element_and_click(self.__sort_by_2)
        self.find_element_and_click(self.__done_button)
        return self

    def click_sort_by_size_b2s(self):
        """
        按照大小排序 大到小
        :return:
        """
        self.find_element_and_click(self.__by_size)
        self.find_element_and_click(self.__sort_by_1)
        self.find_element_and_click(self.__done_button)
        return self

    def click_sort_by_size_s2b(self):
        """
        按照大小排序 小到大
        :return:
        """
        self.find_element_and_click(self.__by_size)
        self.find_element_and_click(self.__sort_by_2)
        self.find_element_and_click(self.__done_button)
        return self

    def click_one_min(self):
        """
        打开一分钟以上
        :return:
        """
        text = self.find_element_and_get_text(self.__one_min)
        if text == "关闭":
            self.find_element_and_click(self.__one_min)
        self.find_element_and_click(self.__done_button)
        return self

    def get_songs_title(self):
        """
        获取音乐名称列表
        :return:
        """
        return self.loop_to_get_all_titles(self.__song_title)

    def sort_by_title_a2z(self, str_list):
        """
        字符串列表排序 按照从a到z
        :return:
        """
        for i in range(len(str_list)-1):
            for j in range(i+1, len(str_list)):
                if str_list[i] <= str_list[j]:
                    continue
                else:
                    return False
        return True

    def sort_by_title_z2a(self, str_list):
        """
        字符串列表排序 按照从z到a
        :return:
        """
        for i in range(len(str_list)-1):
            for j in range(i+1, len(str_list)):
                if str_list[i] >= str_list[j]:
                    continue
                else:
                    return False
        return True

    def click_shuffle_all(self):
        """
        点击随机播放全部
        :return:
        """
        self.find_element_and_click(self.__shuffle_all)
        return self

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

    def click_set_as_ringtone(self):
        """
        点击设置为铃声
        :return:
        """
        self.find_element_and_click(self.__set_as_ringtone)
        return self

    def click_mx_share(self):
        """
        点击mx分享按钮
        :return:
        """
        self.find_element_and_click(self.__mx_share)
        return self

    def click_rename(self):
        """
        点击重命名按钮
        :return:
        """
        self.find_element_and_click(self.__rename_button)
        return self

    def click_attribute_button(self):
        """
        点击属性按钮
        :return:
        """
        self.find_element_and_click(self.__attribute_button)
        return self

    def click_delete_button(self):
        """
        点击删除按钮
        :return:
        """
        self.find_element_and_click(self.__delete_button)
        return self

    def delete_song(self):
        """
        删除歌曲
        :return:
        """
        self.click_delete_button()
        self.find_element_and_click(self.__confirm_delete)
        return self

    def create_new_playlist_and_add(self, title):
        """
        创建新播放列表
        :param title: 播放列表名称
        :return:
        """
        # 显示等待1秒，解决创建新播放列表找不到的问题
        sleep(1)
        # 点击创建新播放列表
        self.find_element_and_click(self.__new_playlist)
        # 输入播放列表名称
        self.find_element_and_send_keys(self.__new_playlist_text, title)
        # 点击创建按钮
        self.find_element_and_click(self.__new_playlist_create)
        return self

    def click_phone_ringtone(self):
        """
        点击设置为手机铃声
        :return:
        """
        self.find_element_and_click(self.__phone_ringtone)
        return self

    def click_alarm_ringtone(self):
        """
        点击设置为闹钟铃声
        :return:
        """
        self.find_element_and_click(self.__alarm_ringtone)
        return self

    def click_notification_ringtone(self):
        """
        点击设置为通知铃声
        :return:
        """
        self.find_element_and_click(self.__notification_ringtone)
        return self

    def get_attr_size(self):
        """
        获取属性中的大小 默认获取到的数据格式：13 MB (13,853,941 字节)
        :return: 13853941
        """
        raw_size = self.find_element_and_get_text(self.__song_size)
        size = raw_size.split("(")[1].split(" ")[0].replace(",", "")
        return int(size)

    def get_attr_date(self):
        """
        获取属性中的日期 默认获取到的数据格式：2021年11月19日 13:26 或者 2021年11月19日 下午3:26
        :return: 格式：1637307600
        """
        raw_date = self.find_element_and_get_text(self.__song_date)
        # 先转换为2021-11-19 下午3:26的格式
        date = raw_date.replace("年", "-").replace("月", "-").replace("日", "")
        # 去掉时间中的下午和上午
        if "下午" in date:
            date = date.replace("下午", "")
            date = date.split(" ")[0]+" "+str((int(date.split(" ")[1].split(":")[0])+12))+":"+date.split(":")[1]+":00"
        elif "上午" in date:
            date = date.replace("上午", "")
        return self.date_to_timestamp(date)

    def get_attr_duration(self):
        """
        获取属性中的时长 默认获取到的数据格式：05:42
        :return: 格式：
        """
        raw_duration = self.find_element_and_get_text(self.__song_duration)
        duration = int(raw_duration.split(":")[0])*60+int(raw_duration.split(":")[1])
        return duration

    def loop_to_get_all_songs_attr(self, fun):
        """
        获取全部歌曲的大小
        :type fun: object 需要获取的属性
        :return:
        """
        # 音乐大小列表
        songs_size = []
        # 获取当前页面的全部音乐大小，存入 songs_size
        first_list = self.find_elements_and_get_text(self.__song_title)
        for i in range(len(first_list)):
            self.click_music_option(i)
            self.click_attribute_button()
            size = fun()
            songs_size.append(size)
            self.click_close()
        # 滑动页面
        # 获取当前页面全部元素的text
        while True:
            self.slide_up_page()
            sleep(2)
            current_list = self.find_elements(self.__song_title)
            last_title = current_list[-1].text
            # 用歌曲名是否在列表中判断
            if last_title not in first_list:
                for n in range(len(current_list)):
                    # 显示等待2秒，解决find_elements找不到元素的问题
                    sleep(2)
                    # print(self.driver.page_source)
                    if current_list[n].text not in first_list:
                        # 导入元素
                        first_list.append(current_list[n].text)
                        # 获取歌曲的size
                        self.click_music_option(n)
                        self.click_attribute_button()
                        size = fun()
                        songs_size.append(size)
                        self.click_close()
            else:
                break
        return songs_size

    def get_attr_file_title(self):
        """
        获取属性中文件标题
        :return:
        """
        return self.find_element_and_get_text(self.__file_title)

    def click_sys_switch(self):
        """
        点击允许修改系统设置按钮
        :return:
        """
        sleep(1)
        if self.is_element_exist(self.__switch):
            self.find_element_and_click(self.__switch)
            self.click_return_button()
        return self




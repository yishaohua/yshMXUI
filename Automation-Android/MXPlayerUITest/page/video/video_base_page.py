from time import sleep

from selenium.webdriver.common.by import By

from page.base_page import BasePage


class VideoBasePage(BasePage):
    """
    video 基础页面封装
    继承了通用方法
    """
    # tool bar页面标题
    __tool_bar_title = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/toolbar']/android.widget.TextView")
    # 页面顶部删除按钮
    __toolbar_delete_button = (By.ID, "com.mxtech.videoplayer.ad:id/action_delete")
    # 下载页面顶部全部删除按钮
    __delete_all_button = (By.XPATH, "(//android.widget.TextView[@content-desc='删除'])[2]")

    # 筛选器标签
    __filter_title_list = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/filter_title']")
    # 筛选器list
    __filter_title_container = (By.ID, "com.mxtech.videoplayer.ad:id/filter_title_list")

    # 缺省页提示文案
    __default_text = (By.ID, "com.mxtech.videoplayer.ad:id/textView")

    # 删除页面 删除按钮
    __delete_action = (By.XPATH, "(//android.widget.TextView[@content-desc='删除'])[1]")
    # 已勾选视频数量,text:0/3 选择
    __selected_tv = (By.ID, "com.mxtech.videoplayer.ad:id/selected_tv")
    # 待看列表全选box
    __selected_all_box = (By.ID, "com.mxtech.videoplayer.ad:id/choice_status")
    # 下载页全选box
    __selected_all= (By.XPATH, "//*[@text='全选']/../android.widget.CheckBox")
    # 待看列表视频 第一个视频删除勾选box
    __video_box = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/history_list']/android.view.ViewGroup[1]/android.widget.CheckBox")
    # 勾选box列表
    __check_box = (By.CLASS_NAME, "android.widget.CheckBox")

    def is_delete_exist(self):
        """
        判断删除按钮是否存在
        :return:
        """
        return self.is_element_exist(self.__toolbar_delete_button)

    def get_tool_bar_title(self):
        """
        获取tool bar标题
        :return:
        """
        return self.find_element_and_get_text(self.__tool_bar_title)

    def default_text_is_exist(self):
        """
        判断缺省页文案是否存在
        :return:
        """
        return self.is_element_exist(self.__default_text)

    def get_default_text(self):
        """
        获取缺省文案
        :return:
        """
        text = self.find_element_and_get_text(self.__default_text)
        return text

    def click_delete_button(self):
        """
        点击待看列表顶部删除按钮
        :return:
        """
        self.find_element_and_click(self.__toolbar_delete_button)
        return self

    def click_download_delete_button(self):
        """
        点击下载页顶部删除按钮
        :return:
        """
        self.find_element_and_click(self.__delete_all_button)
        return self

    def select_one_video_and_delete(self, video_count):
        """
        删除第一个视频
        :return:
        """
        if video_count > 1:
            # 点击删除选项按钮
            self.find_element_and_click(self.__toolbar_delete_button)
            # 选择第一个视频的删除勾选框
            self.find_elements(self.__check_box)[1].click()
        return self

    def select_all_video_and_delete(self, video_count):
        """
        待看列表删除全部视频
        :return:
        """
        if video_count != 0:
            # 点击删除按钮
            self.find_element_and_click(self.__toolbar_delete_button)
            # 点击全选
            self.find_element_and_click(self.__selected_all_box)
        return self

    def select_all_and_delete(self, video_count):
        """
        下载列表删除全部视频
        :return:
        """
        if video_count != 0:
            # 点击删除按钮
            self.find_element_and_click(self.__toolbar_delete_button)
            # 点击全选
            self.find_element_and_click(self.__selected_all)
        return self

    def click_delete_action(self):
        """
        点击确认删除按钮
        :return:
        """
        self.find_element_and_click(self.__delete_action)
        return self

    def delete_all_videos(self):
        """
        删除全部待看列表视频，test_video中用到
        :return:
        """
        sleep(1)
        # 点击删除按钮
        self.find_element_and_click(self.__toolbar_delete_button)
        # 点击全选
        self.find_element_and_click(self.__selected_all_box)
        sleep(1)
        self.find_element_and_click(self.__delete_action)
        return self


    def get_selected_tv_text(self):
        """
        获取已选中删除数
        :return:
        """
        selected_text = self.find_element_and_get_text(self.__selected_tv)
        return selected_text

    def get_filter_title(self):
        """
        获取筛选器标题
        :return:
        """
        first_list = self.find_elements_and_get_text(self.__filter_title_list)
        # 获取当前页面全部tab元素的text
        # 滑动页面后，获取当前页全部tab元素
        # 根据tab元素的text判断是否已存在在列表中
        # 如果 当前页最后一个元素不存在 ele_list_text 中，则继续滑动，并且将不存在的元素追加到ele_list_text中
        while True:
            self.slide_filter_title()
            current_list = self.find_elements(self.__filter_title_list)
            last_title = current_list[-1].text
            if last_title not in first_list:
                for n in range(len(current_list)):
                    if current_list[n].text not in first_list:
                        first_list.append(current_list[n].text)
            else:
                break
        return first_list

    def slide_filter_title(self):
        """
        向左滑动筛选标签列表
        :return:
        """
        self.slide_next_sheet(self.__filter_title_container, -400)
        return self


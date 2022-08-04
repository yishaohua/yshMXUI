from time import sleep

from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.local.anchor_media_page import AnchorMediaPage


class LocalPage(BasePage):
    """
    继承一个通用页面
    本地页面
    """
    # 点击返回主播媒体列表页面
    __back_anchor_media = (By.XPATH, "//android.widget.ImageButton[@content-desc='转到上一层级']")
    # 顶部标题文案
    __top_title = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/toolbar']/android.widget.TextView")
    # 搜索标题文案
    __search_title = (By.ID, "com.mxtech.videoplayer.ad:id/tv_title")
    # 搜索按钮
    __top_search_button = (By.ID, "com.mxtech.videoplayer.ad:id/search")
    # 搜索输入框
    __search_input = (By.ID, "com.mxtech.videoplayer.ad:id/search_src_text")
    # 搜索栏关闭按钮
    __search_close = (By.ID, "com.mxtech.videoplayer.ad:id/action_mode_close_button")
    # 视图菜单按钮
    __top_view_menu_button = (By.ID, "com.mxtech.videoplayer.ad:id/options_menu")
    # 更多选项按钮
    __top_options_button = (By.XPATH, "//android.widget.ImageView[@content-desc=\"更多选项\"]")

    # 视图菜单弹窗 视图模式标题显示
    __view_menu_title = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/recycler_view']/android.view.ViewGroup[1]/android.widget.TextView")

    # tab选项 这是一组元素
    __tab_list = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/tv_title' and @index='0']")
    # tab选项 关闭按钮
    __tab_choices_close = (By.ID, "com.mxtech.videoplayer.ad:id/iv_close")

    # 个人设置-内容语言 按钮
    __content_language_button = (By.ID, "com.mxtech.videoplayer.ad:id/tv_content_language")

    def click_back_anchor_media(self):
        """
        点击返回主播媒体列表页
        :return:
        """
        self.find_element_and_click(self.__back_anchor_media)
        sleep(2)
        return AnchorMediaPage(self.driver)

    def get_title_text(self):
        """
        获取标题文案
        :return:
        """
        title_text = self.find_element_and_get_text(self.__top_title)
        return title_text

    def get_title(self):
        """
        获取标题文案
        :return:
        """
        return self.find_element_and_get_text(self.__top_title)

    def get_search_title_text(self):
        """
        获取搜索标题文案
        :return:
        """
        print("进入get_search_title_text")
        flag = self.is_search_input_exist()
        if flag == 0:
            print("flag = 0")
            search_title_text = self.find_element_and_get_text(self.__top_title)
            print("正常获取到标题:", search_title_text)
        else:
            sleep(2)
            print("等待2秒")
            search_title_text = self.find_element_and_get_text(self.__search_title)
            print("等待后获取到的", search_title_text)
        return search_title_text

    def click_search_button(self):
        """
        点击搜索按钮
        :return:
        """
        self.find_element_and_click(self.__top_search_button)
        return self

    def is_search_input_exist(self):
        """
        判断搜索输入框是否存在
        :return:
        """
        return self.is_element_exist(self.__search_input)

    def input_search_text(self, content):
        """
        给搜索输入框 输入内容
        :return:
        """
        self.find_element_and_send_keys(self.__search_input, content)
        self.driver.execute_script('mobile: performEditorAction', {'action': 'search'})
        return self

    def click_search_close_button(self):
        """
        点击搜索框关闭按钮
        :return:
        """
        self.find_element_and_click(self.__search_close)
        return self

    def click_view_menu_button(self):
        """
        点击视图菜单按钮
        :return:
        """
        self.find_element_and_click(self.__top_view_menu_button)
        return self

    def get_view_menu_title(self):
        """
        获取视图菜单弹窗中 视图标题文案
        :return:
        """
        return self.find_element_and_get_text(self.__view_menu_title)

    def get_tab_title(self):
        """
        获取tab标题内容，是一组元素
        :return:
        """
        return self.find_elements_and_get_text(self.__top_title)

    def click_tab_choices_close(self):
        """
        点击关闭tab
        :return:
        """
        self.find_element_and_click(self.__tab_choices_close)
        return self

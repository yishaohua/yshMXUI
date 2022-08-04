from selenium.webdriver.common.by import By

from page.base_page import BasePage


class GamePage(BasePage):
    """
    继承通用页面
    游戏页面
    """
    # 游戏中的弹窗
    __pop_cover = (By.ID, "com.mxtech.videoplayer.ad:id/iv_cover")
    # 弹窗关闭按钮
    __pop_close = (By.ID, "com.mxtech.videoplayer.ad:id/iv_close")
    # 顶部活动促销图标
    __promote_icon = (By.ID, "com.mxtech.videoplayer.ad:id/iv_promote_bar")
    # 顶部钱包按钮
    __game_title_money = (By.ID, "com.mxtech.videoplayer.ad:id/mx_games_tab_title_money_layout")
    # 钱包余额
    __title_money_count = (By.ID, "com.mxtech.videoplayer.ad:id/mx_games_tab_title_money")
    # 顶部金币按钮
    __game_title_coin = (By.ID, "com.mxtech.videoplayer.ad:id/mx_games_tab_title_coin_layout")
    # 金币余额
    __title_coin_count = (By.ID, "com.mxtech.videoplayer.ad:id/mx_games_tab_title_coins")
    # 第一行限时活动卡片
    __limit_game_cards = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/rv_flow_fragment']/android.widget.FrameLayout[2]")
    # 游戏卡片
    __game_card = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/games_video_cover']")

    def click_pop_close(self):
        """
        点击关闭弹窗
        :return:
        """
        if self.is_element_exist(self.__pop_cover):
            self.find_element_and_click(self.__pop_close)
        return self

    def click_promote_icon(self):
        """
        点击顶部活动促销图标
        :return:
        """
        self.find_element_and_click(self.__promote_icon)
        return self

    def click_money_button(self):
        """
        点击余额按钮
        :return:
        """
        self.find_element_and_click(self.__game_title_money)
        return self

    def get_money_count(self):
        """
        获取钱包余额
        :return:
        """
        return self.find_element_and_get_text(self.__title_money_count)

    def click_coin_button(self):
        """
        点击金币按钮
        :return:
        """
        self.find_element_and_click(self.__game_title_coin)
        return self

    def get_coin_count(self):
        """
        获取金币余额
        :return:
        """
        return self.find_element_and_get_text(self.__title_coin_count)

    def slide_limit_game(self):
        """
        滑动限时游戏卡片区域（第一行）
        :return:
        """
        self.slide_next_sheet(self.__limit_game_cards, -300)
        return self

    def click_first_card(self):
        """
        点击第一个游戏卡片
        :return:
        """
        eles = self.find_elements(self.__game_card)
        eles[0].click()
        return self


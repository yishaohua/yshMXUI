from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.video.search_shows_page import SearchShowsPage
from page.video.video_news_detail_page import VideoNewsDetailPage


class SearchLiveTVPage(SearchShowsPage):
    """
    继承通用页面
    video页面点击搜索，选择浏览live TV卡片，进入live TV列表
    """
    # tv logo图片 列表
    __tv_logo = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/card_view']")
    # tv title名称 列表
    __tv_title = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/title']")

    # 排序规则选项列表  人气
    __queue_item = (By.ID, "com.mxtech.videoplayer.ad:id/queue_tv")
    # 筛选器选项 category
    __filter_category = (
        By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/title_list_view']/android.widget.RelativeLayout[2]")

    def click_category(self):
        """
        点击选择种类过滤器
        :return:
        """
        try:
            WebDriverWait(self.driver, timeout=5, poll_frequency=0.5, ignored_exceptions=None). \
                until(expected_conditions.visibility_of_element_located(self.__filter_actor))
            self.find_element_and_click(self.__filter_category)
        except:
            self.find_element_and_click(self.__filter_category)
        return self

    def click_tv_card(self, option: str):
        """
        点击视频卡片
        :return:
        :param option: 需要点击的频道名称
        """
        sleep(2)
        tv_list = self.find_elements(self.__tv_title)
        for i in range(len(tv_list)):
            if tv_list[i].text in option:
                tv_list[i].click()
        return VideoNewsDetailPage(self.driver)

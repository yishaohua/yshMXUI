from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.video.search_shows_page import SearchShowsPage


class SearchMusicPage(SearchShowsPage):
    """
    继承通用页面
    video页面点击搜索，选择浏览music卡片，进入music列表
    """
    # 筛选器选项 singer
    __filter_singer = (
        By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/title_list_view']/android.widget.RelativeLayout[4]")

    def click_singer(self):
        """
        点击选择上线年份过滤器
        :return:
        """
        try:
            WebDriverWait(self.driver, timeout=5, poll_frequency=0.5, ignored_exceptions=None). \
                until(expected_conditions.visibility_of_element_located(self.__filter_actor))
            self.find_element_and_click(self.__filter_singer)
        except:
            self.find_element_and_click(self.__filter_singer)
        return self



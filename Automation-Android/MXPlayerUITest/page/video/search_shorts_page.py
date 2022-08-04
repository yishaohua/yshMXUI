from selenium.webdriver.common.by import By

from page.video.search_shows_page import SearchShowsPage
from page.video.shorts_detail_page import ShortsDetailPage


class SearchShortsPage(SearchShowsPage):
    """
    继承通用页面
    video页面点击搜索，选择浏览Shorts卡片，进入Shorts列表
    """
    # video 视频标题
    __video_title = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/title']")
    # video 缩略图, 一组元素
    __video_image = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/image_view_container']")

    def get_video_title(self):
        """
        获取第一个视频title
        :return:
        """
        title_list = self.find_elements(self.__video_title)
        return title_list[0].text

    def click_video(self, option: int):
        """
        点击video 卡片
        :param option:
        :return:
        """
        videos = self.find_elements(self.__video_image)
        videos[option].click()
        return ShortsDetailPage(self.driver)



from selenium.webdriver.common.by import By
from page.video.video_detail_page import VideoDetailPage


class ShortsDetailPage(VideoDetailPage):
    """
    继承通用页面
    video页面点击搜索，选择浏览Shorts卡片，点击 shorts 视频进入详情页
    """
    # 详情页 可切换tab
    __detail_tab = (By.XPATH, "//*[@resource-id='com.mxtech.videoplayer.ad:id/title_container']/android.widget.TextView")

    def click_tab(self, option: int):
        """
        点击切换tab
        :param option: tab 下标，从0开始
        :return:
        """
        tabs = self.find_elements(self.__detail_tab)
        tabs[option].click()
        return self
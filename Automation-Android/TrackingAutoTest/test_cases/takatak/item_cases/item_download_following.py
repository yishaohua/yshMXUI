from test_cases.base_case import BaseCase


class ItemDownloadFollowing(BaseCase):

    def __init__(self, device, run_time):
        self.title = "item_download_following"
        super().__init__(self.title, device, run_time)
        self.check_points = {
            # 应包括一次itemDownload
            "itemDownload": {
                "count": 1,
                "source": "Following",
                "length": "",
                "isShared": "0"
            }
        }

    def run_steps(self):
        # 切换到following页签，并判断是否有followed
        self.device.click_by_xpath(
            '//*[@resource-id="com.next.innovation.takatak:id/title_container"]/android.widget.FrameLayout[2]')
        # 点击share按钮
        self.device.click_by_id('com.next.innovation.takatak:id/detail_share')
        self.device.click_by_text('Save')
        self.device.listening_toast('Vedio saved to My Downloads.')



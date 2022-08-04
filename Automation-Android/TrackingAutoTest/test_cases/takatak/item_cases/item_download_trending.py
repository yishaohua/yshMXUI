from test_cases.base_case import BaseCase


class ItemDownloadTrending(BaseCase):

    def __init__(self, device, run_time):
        self.title = "item_download_trending"
        super().__init__(self.title, device, run_time)
        self.check_points = {
            # 应包括一次itemDownload
            "itemDownload": {
                "count": 1,
                "source": "Trending",
                "length": "",
                "isShared": "0"
            }
        }

    def run_steps(self):
        # 点击share按钮
        self.device.click_by_id('com.next.innovation.takatak:id/detail_share')
        self.device.click_by_text('Save')
        self.device.listening_toast('Vedio saved to My Downloads.')



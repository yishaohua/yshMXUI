from test_cases.base_case import BaseCase


class ItemClicked(BaseCase):

    def __init__(self, device, run_time):
        self.title = "item_clicked"
        super().__init__(self.title, device, run_time)
        self.check_points = {
            # 应包括一次publisherClicked, 一次itemListViewed, 一次itemClicked
            "publisherClicked": {
                "count": 1,
                "source": "home",
                "publisherID": "",
                "itemID": ""
            },
            "itemListViewed": {
                "count": 1,
                "source": "publisherVideoList",
            },
            "itemClicked": {
                "count": 1,
                "source": "publisherVideoList"
            }
        }

    def run_steps(self):
        self.device.click_by_id('com.next.innovation.takatak:id/detail_owner')
        # 点击publisher列表里的第一个视频
        self.device.click_by_xpath('//*[@resource-id="com.next.innovation.takatak:id/recycler_view"]/android.view.ViewGroup[1]')



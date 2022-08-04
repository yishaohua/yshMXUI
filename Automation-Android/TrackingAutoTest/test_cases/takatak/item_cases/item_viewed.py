from test_cases.base_case import BaseCase


class ItemViewed(BaseCase):

    def __init__(self, device, run_time):
        self.title = "item_viewed"
        super().__init__(self.title, device, run_time)
        self.check_points = {
            # 应包括一次detailPageItemViewed
            "detailPageItemViewed": {
                "count": 1,
                "length": "",
                "previousID": "None"
            }
        }

    def run_steps(self):
        # 打开页面上划一下
        self.device.swipe_up()



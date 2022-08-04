from test_cases.base_case import BaseCase


class FollowClickedTrending(BaseCase):

    def __init__(self, device, run_time):
        self.title = "follow_clicked_trending"
        super().__init__(self.title, device, run_time)
        self.check_points = {
            # 应包括一次followClicked
            "followClicked": {
                "count": 1,
                "source": "Trending",
                "publisherID": "",
                "suggestType": "None"
            }
        }

    def run_steps(self):
        while not self.device.resource_is_exist('com.next.innovation.takatak:id/iv_follow'):
            self.device.swipe_up()
        self.device.click_by_id('com.next.innovation.takatak:id/iv_follow')




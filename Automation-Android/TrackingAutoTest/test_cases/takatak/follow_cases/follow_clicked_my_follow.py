from test_cases.base_case import BaseCase


class FollowClickedMyFollow(BaseCase):

    def __init__(self, device, run_time):
        self.title = "follow_clicked_my_follow"
        super().__init__(self.title, device, run_time)
        self.check_points = {
            # 应包括一次followClicked，一次unfollowClicked
            "followClicked": {
                "count": 1,
                "source": "myFollowPage",
                "publisherID": "",
                "suggestType": "None"
            },
            "unfollowClicked": {
                "count": 1,
                "source": "myFollowPage",
                "publisherID": "",
                "suggestType": "None"
            }
        }

    def run_steps(self):
        self.device.click_by_id('com.next.innovation.takatak:id/ivMe')
        self.device.click_by_id('com.next.innovation.takatak:id/following_text')
        self.device.click_by_id('com.next.innovation.takatak:id/follow_button')
        self.device.click_by_id('com.next.innovation.takatak:id/follow_button')



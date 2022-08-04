from test_cases.base_case import BaseCase


class FollowClickedPublisherPage(BaseCase):

    def __init__(self, device, run_time):
        self.title = "follow_clicked_publisher_page"
        super().__init__(self.title, device, run_time)
        self.check_points = {
            # 应包括一次followClicked，一次unfollowClicked
            "followClicked": {
                "count": 1,
                "source": "publisherPage",
                "publisherID": "",
                "suggestType": "None"
            },
            "unfollowClicked": {
                "count": 1,
                "source": "publisherPage",
                "publisherID": "",
                "suggestType": "None"
            }
        }

    def run_steps(self):
        self.device.click_by_id('com.next.innovation.takatak:id/detail_owner')
        self.device.click_by_id('com.next.innovation.takatak:id/follow_button')
        self.device.click_by_id('com.next.innovation.takatak:id/follow_button')




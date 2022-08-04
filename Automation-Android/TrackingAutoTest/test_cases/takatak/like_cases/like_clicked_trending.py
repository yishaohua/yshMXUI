from test_cases.base_case import BaseCase


class LikeClickedTrending(BaseCase):

    def __init__(self, device, run_time):
        self.title = "like_clicked_trending"
        super().__init__(self.title, device, run_time)
        self.check_points = {
            # 应包括一次likeClicked，一次likeSucceed,一次likeCanceled
            "likeClicked": {
                "count": 1,
                "source": "Trending",
                "length": ""
            },
            "likeSucceed": {
                "count": 1,
                "source": "Trending",
                "length": ""
            },
            "likeCanceled": {
                "count": 1,
                "source": "Trending",
                "length": "",
                "reason": 'action'
            }
        }

    def run_steps(self):
        self.device.click_by_id('com.next.innovation.takatak:id/detail_like')
        self.device.click_by_id('com.next.innovation.takatak:id/detail_like')



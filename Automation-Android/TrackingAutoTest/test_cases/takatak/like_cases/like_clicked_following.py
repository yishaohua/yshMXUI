from test_cases.base_case import BaseCase


class LikeClickedFollowing(BaseCase):

    def __init__(self, device, run_time):
        self.title = "like_clicked_following"
        super().__init__(self.title, device, run_time)
        self.check_points = {
            # 应包括一次likeClicked，一次likeSucceed,一次likeCanceled
            "likeClicked": {
                "count": 1,
                "source": "Following",
                "length": ""
            },
            "likeSucceed": {
                "count": 1,
                "source": "Following",
                "length": ""
            },
            "likeCanceled": {
                "count": 1,
                "source": "Following",
                "length": "",
                "reason": 'action'
            }
        }

    def run_steps(self):
        # 切换到following页签，并判断是否有followed
        self.device.click_by_xpath(
            '//*[@resource-id="com.next.innovation.takatak:id/title_container"]/android.widget.FrameLayout[2]')
        self.device.click_by_id('com.next.innovation.takatak:id/detail_like')
        self.device.click_by_id('com.next.innovation.takatak:id/detail_like')



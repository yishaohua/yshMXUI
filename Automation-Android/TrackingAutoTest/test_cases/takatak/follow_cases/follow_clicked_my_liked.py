from test_cases.base_case import BaseCase


class FollowClickedMyLike(BaseCase):

    def __init__(self, device, run_time):
        self.title = "follow_clicked_my_liked"
        super().__init__(self.title, device, run_time)
        self.check_points = {
            # 应包括一次followClicked
            "followClicked": {
                "count": 1,
                "source": "mylike",
                "publisherID": "",
                "suggestType": "None"
            }
        }

    def run_steps(self):
        self.device.click_by_id('com.next.innovation.takatak:id/detail_like')
        self.device.click_by_id('com.next.innovation.takatak:id/ivMe')
        # 切换到like列表
        self.device.click_by_xpath(
            '//*[@resource-id="com.next.innovation.takatak:id/title_container"][1]')
        # 点击列表第一个
        self.device.click_by_xpath(
            '//*[@resource-id="com.next.innovation.takatak:id/recycler_view"]/android.widget.FrameLayout[1]')
        # 判断是否已follow
        if self.device.resource_is_exist('com.next.innovation.takatak:id/iv_follow'):
            self.device.click_by_id('com.next.innovation.takatak:id/iv_follow')
        else:
            self.device.click_by_id('com.next.innovation.takatak:id/detail_owner')
            self.device.click_by_id('com.next.innovation.takatak:id/follow_button')
            self.device.press_back()
            self.device.click_by_id('com.next.innovation.takatak:id/iv_follow')



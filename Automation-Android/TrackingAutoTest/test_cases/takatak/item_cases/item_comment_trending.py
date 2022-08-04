from test_cases.base_case import BaseCase


class ItemCommentTrending(BaseCase):

    def __init__(self, device, run_time):
        self.title = "item_comment_trending"
        super().__init__(self.title, device, run_time)
        self.check_points = {
            # 应包括一次itemComment,一次commentSent,
            "itemComment": {
                "count": 1,
                "source": "Trending",
                "itemID": "",
                "publisherID": ""
            },
            "commentSent": {
                "count": 1,
                "source": "Trending",
                "itemID": "",
                "publisherID": ""
            }
        }

    def run_steps(self):
        self.device.click_by_id('com.next.innovation.takatak:id/detail_comment')
        self.device.send_keys('com.next.innovation.takatak:id/fake_message_edt', 'nice')
        self.device.click_by_id('com.next.innovation.takatak:id/fake_send_tv')
    #   device.click_by_xpath(
    #     '//*[@resource-id="com.next.innovation.takatak:id/commentInputLayout"]/android.widget.LinearLayout['
    #     '1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]')



from test_cases.base_case import BaseCase


class ItemCommentFollowing(BaseCase):

    def __init__(self, device, run_time):
        self.title = "item_comment_following"
        super().__init__(self.title, device, run_time)
        self.check_points = {
            # 应包括一次itemComment,一次commentSent,
            "itemComment": {
                "count": 1,
                "source": "Following",
                "itemID": "",
                "publisherID": ""
            },
            "commentSent": {
                "count": 1,
                "source": "Following",
                "itemID": "",
                "publisherID": ""
            }
        }

    def run_steps(self):
        # 切换到following页签，并判断是否有followed
        self.device.click_by_xpath(
            '//*[@resource-id="com.next.innovation.takatak:id/title_container"]/android.widget.FrameLayout[2]')
        self.device.click_by_id('com.next.innovation.takatak:id/detail_comment')
        self.device.send_keys('com.next.innovation.takatak:id/fake_message_edt', 'nice')
        self.device.click_by_id('com.next.innovation.takatak:id/fake_send_tv')


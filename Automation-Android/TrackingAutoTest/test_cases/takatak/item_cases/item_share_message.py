from test_cases.base_case import BaseCase


class ItemShareMessage(BaseCase):

    def __init__(self, device, run_time):
        self.title = "item_share_message"
        super().__init__(self.title, device, run_time)
        self.check_points = {
            # 应包括一次itemShared
            "itemShared": {
                "count": 1,
                "itemType": "Video",
                "shareType": "More",
            }
        }

    def run_steps(self):
        # 点击share按钮
        self.device.click_by_id('com.next.innovation.takatak:id/detail_share')
        self.device.click_by_xpath('//*[@resource-id="com.next.innovation.takatak:id/recycler_view_primary"]/android.view'
                              '.ViewGroup[5]/android.widget.ImageView[1]')
        while not (self.device.text_is_exist('Messages') or self.device.text_is_exist('信息')):
            self.device.swipe_up()
        if self.device.text_is_exist('Messages'):
            self.device.click_by_text('Messages')
        else:
            self.device.click_by_text('信息')



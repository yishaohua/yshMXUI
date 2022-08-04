from test_cases.base_case import BaseCase


class ItemShareWhatsapp(BaseCase):

    def __init__(self, device, run_time):
        self.title = "item_share_whatsapp"
        super().__init__(self.title, device, run_time)
        self.check_points = {
            # 应包括一次itemShared
            "itemShared": {
                "count": 1,
                "itemType": "Video",
                "shareType": "WhatsApp",
            }
        }

    def run_steps(self):
        # 点击share按钮
        self.device.click_by_id('com.next.innovation.takatak:id/detail_share')
        self.device.click_by_text('WhatsApp')
        # 检测是否有权限框
        self.device.listening_toast('Please finish register first.|请先完成注册')



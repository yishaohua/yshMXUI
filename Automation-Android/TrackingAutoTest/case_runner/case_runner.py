from case_runner.taka_cases import case_like, case_item, case_follow, case_search
from utils.device import Device
import time


class CaseRunner:

    def __init__(self, device_id, package_name):
        self.device_id = device_id
        self.package_name = package_name
        self.device = Device(device_id, package_name)
        self.standard_log = {}
        self.run_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print("初始化CaseRunner完成")

    def run_taka_cases(self):
        # 执行like相关的打点测试
        # case_item.case_switch_to_online(self.device)
        case_like.case_like_click_trending(self.device, self.standard_log)
        case_like.case_like_click_following(self.device, self.standard_log)
        # 执行item相关的打点测试
        # case_item.case_item_clicked(self.device, self.standard_log)
        # case_item.case_item_share_whatsapp(self.device, self.standard_log)
        # case_item.case_item_share_facebook(self.device, self.standard_log)
        # case_item.case_item_share_messenger(self.device, self.standard_log)
        # case_item.case_item_share_message(self.device, self.standard_log)
        # case_item.case_item_download_trending(self.device, self.standard_log)
        # case_item.case_item_download_following(self.device, self.standard_log)
        # case_item.case_detail_page_item_viewed(self.device, self.standard_log)
        # case_item.case_item_comment_trending(self.device, self.standard_log)
        # case_item.case_item_comment_following(self.device, self.standard_log)
        # 执行follow相关打点测试
        # case_follow.case_follow_clicked_trending(self.device, self.standard_log)
        # case_follow.case_follow_clicked_my_liked(self.device, self.standard_log)
        # case_follow.case_follow_clicked_publisher_page(self.device, self.standard_log)
        # case_follow.case_follow_clicked_my_follow_page(self.device, self.standard_log)
        # 执行search相关打点
        # case_search.case_search_result_show(self.device, self.standard_log)

    def run_mxplayer_cases(self):
        pass

    def run(self):
        self.device.start_watcher()
        if self.package_name == "com.next.innovation.takatak":
            # 执行taka的用例
            self.run_taka_cases()
            return self.device.log_file_list

        if self.package_name == "com.mxtech.videoplayer.ad":
            # 执行主版的用例
            self.run_mxplayer_cases()
            return self.device.log_file_list
        self.device.stop_watcher()

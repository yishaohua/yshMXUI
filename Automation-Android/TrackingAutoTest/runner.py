# 运行时需带有参数：1代表执行takatak的脚本；2代表执行mx player的脚本
import sys
import time

from handler.mxsql import MXSQL
from handler.reporter import Reporter
from test_cases import *
from utils import util
from utils.device import Device


class Runner:

    def __init__(self):
        self.device_id = ""
        self.package_name = ""
        self.init_parameters()
        self.device = Device(self.device_id, self.package_name)
        self.report = Reporter(self.package_name)
        self.run_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.is_pass = False
        util.init_folder('logs')
        util.init_folder('reports')

    def init_parameters(self):
        if len(sys.argv) == 3:
            app = sys.argv[1]
            self.device_id = sys.argv[2]
        elif len(sys.argv) == 2:
            app = sys.argv[1]
            self.device_id = util.set_device_id()
        else:
            print("参数错误，退出")
            sys.exit(1)

        if app == '1':
            self.package_name = 'com.next.innovation.takatak'
        elif app == '2':
            self.package_name = 'com.mxtech.videoplayer.ad'
        else:
            print("不认识的参数，输入1或者2")
            sys.exit(2)

        print(f"开始运行，设备id: {self.device_id}, 包名: {self.package_name}")

    def run(self):
        self.device.start_watcher()
        # 执行taka的用例
        if self.package_name == "com.next.innovation.takatak":
            self.run_taka_cases()
        # 执行主版的用例
        if self.package_name == "com.mxtech.videoplayer.ad":
            self.run_mxplayer_cases()
        self.device.stop_watcher()

        # 生成结果文档
        self.is_pass = self.report.make_txt(self.run_time)
        if not self.is_pass:
            sys.exit(3)

    def run_taka_cases(self):
        self.device.prepare_taka()
        # follow相关用例
        FollowClickedTrending(self.device, self.run_time).run()
        FollowClickedMyLike(self.device, self.run_time).run()
        FollowClickedMyFollow(self.device, self.run_time).run()
        FollowClickedPublisherPage(self.device, self.run_time).run()
        # search相关用例
        SearchResultShow(self.device, self.run_time).run()
        # like相关用例
        LikeClickedFollowing(self.device, self.run_time).run()
        LikeClickedTrending(self.device, self.run_time).run()
        # item相关用例
        ItemClicked(self.device, self.run_time).run()
        ItemCommentFollowing(self.device, self.run_time).run()
        ItemCommentTrending(self.device, self.run_time).run()
        ItemDownloadFollowing(self.device, self.run_time).run()
        ItemDownloadTrending(self.device, self.run_time).run()
        ItemShareFacebook(self.device, self.run_time).run()
        ItemShareMessage(self.device, self.run_time).run()
        ItemShareMessenger(self.device, self.run_time).run()
        ItemShareWhatsapp(self.device, self.run_time).run()
        ItemViewed(self.device, self.run_time).run()

    def run_mxplayer_cases(self):
        pass


if __name__ == "__main__":
    test_runner = Runner()
    test_runner.run()

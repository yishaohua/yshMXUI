import sys
import re
import time
import subprocess


class Runner:
    def __init__(self, device_id, package_name):
        self.device_id = device_id
        self.package_name = package_name
        self.result = []

    def start_app(self):
        cmd_start = f'adb -s {self.device_id} shell am start -W {self.package_name}/.ActivityWelcomeMX'
        output = subprocess.getoutput(cmd_start)
        time_pattern = re.compile(r'WaitTime: (.*)')
        wait_time = time_pattern.findall(output)[0]
        return wait_time

    def clear_app(self):
        cmd_clear = f'adb -s {self.device_id} shell pm clear {self.package_name}'
        subprocess.getoutput(cmd_clear)

    def close_app(self):
        cmd_close = f'adb -s {self.device_id} shell am force-stop {self.package_name}'
        subprocess.getoutput(cmd_close)

    def run_start_time(self, n):
        for i in range(0, n):
            self.close_app()
            time.sleep(2)
            wait_time = self.start_app()
            print(wait_time)
            self.result.append(int(wait_time))
            time.sleep(2)
        self.format_result()

    def format_result(self):
        self.result.sort()
        self.result.pop()
        self.result.pop(0)

    def print_result(self):
        print('final result:')
        for time in self.result:
            print(time)

    # def start_local_player(self, player_activity, video_file):
    #     # video_file = '/sdcard/Likely/aac-h264.mp4'
    #     cmd_start_player = f'adb -s {self.device_id} shell am start -n {self.package_name}/{player_activity} -W -d {video_file}'
    #     output = subprocess.getoutput(cmd_start_player)
    #     time_pattern = re.compile(r'WaitTime: (.*)')
    #     wait_time = time_pattern.findall(output)[0]
    #     return wait_time


if __name__ == '__main__':
    device_id = sys.argv[1]
    runner = Runner(device_id, "com.mxtech.videoplayer.ad")
    runner.run_start_time(22)
    runner.print_result()

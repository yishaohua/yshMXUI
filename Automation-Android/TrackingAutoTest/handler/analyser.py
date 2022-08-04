# 解析日志，并返回字典类型list，list中每个值对应一个事件(beta版本log格式不一样，不可用)
# 用法：a = Analyser('com.next.innovation.takatak')
#      result = a.analyse('1.txt')

import re


class Analyser:

    def __init__(self, package_name):
        self.package_name = package_name

    def event_analyser(self, lines):
        events = {}
        for line in lines:
            logs = line.split('│')
            # 去掉没有｜的log
            if len(logs) > 1:
                event_item = logs[-1]
                items = event_item.split(':', 1)
                if len(events) == 0:
                    events['eventName'] = items[0].strip()
                    items = items[1].split(':', 1)
                if len(items) == 2:
                    events[items[0].lstrip()] = items[1].strip(' ;')
        return events

    def analyse_taka(self, log_path):
        list_result = []
        with open(log_path) as file:
            events_log = file.read()
        event_logs = re.findall(r"┌.+?└", events_log, re.S)

        for event_log in event_logs:
            lines = event_log.splitlines()
            # 过滤掉send: statusCode: 200非打点log
            if len(lines) > 3:
                event_result = self.event_analyser(lines)
                list_result.append(event_result)
        return list_result

    def analyse_mxplayer(self, log_path):
        pass

    def analyse(self, log_file):
        if self.package_name == 'com.next.innovation.takatak':
            list_event = self.analyse_taka(log_file)
            return list_event
        if self.package_name == 'com.mxtech.videoplayer.ad':
            self.analyse_mxplayer(log_file)

from collections import Counter


class Verify:

    def __init__(self, events_list, standard_events, case_name):
        self.standard_events = standard_events
        self.case_events_list = self.events_preprocessor(events_list)
        self.case_name = case_name
        self.verified_events_list = []

    def verify_common_para(self, event, filter_paras):
        # 针对单个event_log做一般字段校验
        failed_reason = []
        filter_keys = filter_paras.keys()
        for key, value in event.items():
            if key in filter_keys:
                continue
            if value == '':
                failed_reason.append(f"{key} is null; ")
        return failed_reason

    def verify_spcl_para(self, event, standard_para):
        # 针对单个event_log做特殊字段校验
        failed_reason = []
        # 开始校对
        for key_para, value in standard_para.items():
            if key_para == 'count':
                continue
            elif value == 'None':
                if event.get(key_para) != '':
                    failed_reason.append(f"{key_para} is null, Now：{event.get(key_para)}; ")
            elif value == '':
                if event.get(key_para) is None:
                    failed_reason.append(f"{key_para} is not found; ")
            else:
                if event.get(key_para) != value:
                    failed_reason.append(f"{key_para} is unexpected, Now：{event.get(key_para)} , it should be：{standard_para.get(key_para)}; ")
        return failed_reason

    def verify_count(self):
        # 针对单个log文件的所有log信息做次数验证
        if self.case_events_list:
            version_name = self.case_events_list[0].get('versionName')
        else:
            version_name = "null"
        all_events_names = []
        for case_event in self.case_events_list:
            event_name = case_event.get('eventName')
            all_events_names.append(event_name)
        count_of_all_events_names = dict(Counter(all_events_names))

        for standard_event_name in self.standard_events:
            if standard_event_name in all_events_names:
                count_actual = count_of_all_events_names[standard_event_name]
                count_expected = self.standard_events[standard_event_name]['count']
                if count_actual != count_expected:
                    failed_reason = f"{standard_event_name} should be tracked {str(count_expected)} times, actually print {str(count_actual)} times; "
                    for event in self.case_events_list:
                        if event.get('eventName') == standard_event_name:
                            event['result'] = 'false'
                            event['failedReason'] = failed_reason
            else:
                failed_reason = f"{standard_event_name} is missing; "
                event_missing = {'eventName': standard_event_name, 'versionName': version_name,
                                 'caseName': self.case_name, 'result': 'false', 'failedReason': failed_reason}
                self.verified_events_list.append(event_missing)

    def verify_para(self):
        for event in self.case_events_list:
            event_name = event.get('eventName')
            standard_para = self.standard_events[event_name]
            failed_reason_spcl = self.verify_spcl_para(event, standard_para)
            failed_reason_common = self.verify_common_para(event, standard_para)
            if not failed_reason_spcl and not failed_reason_common and (event.get('result') != 'false'):
                event['result'] = 'true'
                event['failedReason'] = 'null'
            else:
                print(f"{event_name} 的打点有问题")
                event['result'] = 'false'
                failed_reason_all = ''.join(failed_reason_spcl + failed_reason_common)
                event['failedReason'] = event.get('failedReason', '') + failed_reason_all
                print(event['failedReason'])
            event['caseName'] = self.case_name
            self.verified_events_list.append(event)

    def verify_main(self):
        # 校验事件的数量
        self.verify_count()
        # 校验事件的字段信息
        self.verify_para()
        return self.verified_events_list

    def events_preprocessor(self, case_events):
        # 对事件集合进行预处理，删掉无关的事件
        for event in case_events.copy():
            if event.get("eventName") not in self.standard_events.keys():
                case_events.remove(event)
        return case_events

# if __name__ == "__main__":
#     standard_log = {'likeClicked': {'count': 2, 'source': 'Trending', 'length': ''},'likeSucceed': {'count': 1, 'source': 'Terending', 'length': 'e'},'likeCanceled': {'count': 1, 'source': 'Treneding', 'length': 'e', 'reason': 'acteion'}}
#     case_events_list = [{'eventName': 'playBandwidth', 'bitrate': '22409100', 'locale': 'en-US', 'versionName': '1.14.3.debug', 'mcc': '0', 'uuid': '4bcb4874-92cb-474a-bb36-eb39dd329f1e767155257', 'sid': '1', 'manufacturer': 'samsung', 'firstInstallTime': '1618557961942', 'itemID': 'e539c2220fa293e9c4bffa971af3a5a7', 'abtest': '[{"groupname":"a","testname":"anonymousFollow"},{"groupname":"b","testname":"contentLanguage"},{"groupname":"m","testname":"interests"}]', 'wID': '7b0371bd4212941d642b62f18ab4d650b09c1cee5b3b36e7a68f47bc6abed147', 'osVersion': '11', 'model': 'SM-G9810', 'packageName': 'com.next.innovation.takatak', 'networkType': 'WIFI', 'installMarket': 'unknown', 'utmSource': 'google-play', 'ctID': '__a9b65b5bf2354f598120be5d7f1a53b9', 'mnc': '0', 'osName': 'Android', 'advertiseID': '969419eb-81ea-4e0e-b009-9d4a4905ba96', 'adOptOut': 'false', 'versionCode': '10011403', 'elapseMs': '509', 'bytes': '1425779', 'utmMedium': 'organic', 'androidID': '8b86c090d0f54a71', 'lastUpdateTime': '1618821476962', 'runTime': '2021-04-29 15:00:34', 'caseName': 'case_like_click_trending'}, {'eventName': 'appExperiment', 'versionName': '1.14.3.debug', 'mcc': '0', 'locale': 'en-US', 'uuid': '4bcb4874-92cb-474a-bb36-eb39dd329f1e767155257', 'sid': '1', 'manufacturer': 'samsung', 'firstInstallTime': '1618557961942', 'abtest': '[{"groupname":"a","testname":"anonymousFollow"},{"groupname":"b","testname":"contentLanguage"},{"groupname":"m","testname":"interests"}]', 'wID': '7b0371bd4212941d642b62f18ab4d650b09c1cee5b3b36e7a68f47bc6abed147', 'osVersion': '11', 'model': 'SM-G9810', 'packageName': 'com.next.innovation.takatak', 'networkType': 'WIFI', 'installMarket': 'unknown', 'utmSource': 'google-play', 'ctID': '__a9b65b5bf2354f598120be5d7f1a53b9', 'mnc': '0', 'abtestExperimentValues': '{"abtest_nps_config_all":{"configs":["abtest_nps_config_v1"]},"abtest_nps_config_v1":{"ui":"abtest_nps_ui_tell_us_more","show_nps_on":["abtest_nps_config_video_upload","abtest_nps_config_video_play"]},"abtest_nps_flag_enable":false,"abtest_nps_config_video_play":{"name":"detailPageItemViewed","properties":{"itemType":"Video"},"count":70},"abtest_nps_config_video_upload":{"name":"detailPageItemViewed","properties":{"itemType":"Video"},"count":20,"dependsOn":{"name":"uploadSucceed","properties":{},"count":2}},"adEnable":true}', 'osName': 'Android', 'advertiseID': '969419eb-81ea-4e0e-b009-9d4a4905ba96', 'versionCode': '10011403', 'adOptOut': 'false', 'utmMedium': 'organic', 'androidID': '8b86c090d0f54a71', 'lastUpdateTime': '1618821476962', 'runTime': '2021-04-29 15:00:34', 'caseName': 'case_like_click_trending'}, {'eventName': 'tabSelection', 'source': 'Trending', 'versionName': '1.14.3.debug', 'mcc': '0', 'locale': 'en-US', 'uuid': '4bcb4874-92cb-474a-bb36-eb39dd329f1e767155257', 'sid': '1', 'manufacturer': 'samsung', 'firstInstallTime': '1618557961942', 'abtest': '[{"groupname":"a","testname":"anonymousFollow"},{"groupname":"b","testname":"contentLanguage"},{"groupname":"m","testname":"interests"}]', 'wID': '7b0371bd4212941d642b62f18ab4d650b09c1cee5b3b36e7a68f47bc6abed147', 'osVersion': '11', 'model': 'SM-G9810', 'packageName': 'com.next.innovation.takatak', 'networkType': 'WIFI', 'installMarket': 'unknown', 'utmSource': 'google-play', 'ctID': '__a9b65b5bf2354f598120be5d7f1a53b9', 'mnc': '0', 'osName': 'Android', 'advertiseID': '969419eb-81ea-4e0e-b009-9d4a4905ba96', 'versionCode': '10011403', 'adOptOut': 'false', 'utmMedium': 'organic', 'androidID': '8b86c090d0f54a71', 'lastUpdateTime': '1618821476962', 'runTime': '2021-04-29 15:00:34', 'caseName': 'case_like_click_trending'}, {'eventName': 'appEntered', 'versionName': '1.14.3.debug', 'mcc': '0', 'locale': 'en-US', 'uuid': '4bcb4874-92cb-474a-bb36-eb39dd329f1e767155257', 'sid': '1', 'manufacturer': 'samsung', 'firstInstallTime': '1618557961942', 'resumeTime': '830', 'abtest': '[{"groupname":"a","testname":"anonymousFollow"},{"groupname":"b","testname":"contentLanguage"},{"groupname":"m","testname":"interests"}]', 'wID': '7b0371bd4212941d642b62f18ab4d650b09c1cee5b3b36e7a68f47bc6abed147', 'osVersion': '11', 'model': 'SM-G9810', 'packageName': 'com.next.innovation.takatak', 'networkType': 'WIFI', 'installMarket': 'unknown', 'utmSource': 'google-play', 'ctID': '__a9b65b5bf2354f598120be5d7f1a53b9', 'mnc': '0', 'osName': 'Android', 'advertiseID': '969419eb-81ea-4e0e-b009-9d4a4905ba96', 'versionCode': '10011403', 'adOptOut': 'false', 'launchTime': '1228', 'utmMedium': 'organic', 'androidID': '8b86c090d0f54a71', 'lastUpdateTime': '1618821476962', 'runTime': '2021-04-29 15:00:34', 'caseName': 'case_like_click_trending'}, {'eventName': 'playerEnter', 'versionName': '1.14.3.debug', 'mcc': '0', 'locale': 'en-US', 'uuid': '4bcb4874-92cb-474a-bb36-eb39dd329f1e767155257', 'sid': '1', 'manufacturer': 'samsung', 'firstInstallTime': '1618557961942', 'itemID': 'e539c2220fa293e9c4bffa971af3a5a7', 'abtest': '[{"groupname":"a","testname":"anonymousFollow"},{"groupname":"b","testname":"contentLanguage"},{"groupname":"m","testname":"interests"}]', 'wID': '7b0371bd4212941d642b62f18ab4d650b09c1cee5b3b36e7a68f47bc6abed147', 'osVersion': '11', 'model': 'SM-G9810', 'packageName': 'com.next.innovation.takatak', 'networkType': 'WIFI', 'installMarket': 'unknown', 'utmSource': 'google-play', 'ctID': '__a9b65b5bf2354f598120be5d7f1a53b9', 'mnc': '0', 'osName': 'Android', 'advertiseID': '969419eb-81ea-4e0e-b009-9d4a4905ba96', 'versionCode': '10011403', 'adOptOut': 'false', 'utmMedium': 'organic', 'waitTime': '729', 'androidID': '8b86c090d0f54a71', 'lastUpdateTime': '1618821476962', 'runTime': '2021-04-29 15:00:34', 'caseName': 'case_like_click_trending'}, {'eventName': 'playerEnter', 'versionName': '1.14.3.debug', 'mcc': '0', 'locale': 'en-US', 'uuid': '4bcb4874-92cb-474a-bb36-eb39dd329f1e767155257', 'sid': '1', 'manufacturer': 'samsung', 'firstInstallTime': '1618557961942', 'itemID': '3e64d60d480c56278383bc1975e7c71e', 'abtest': '[{"groupname":"a","testname":"anonymousFollow"},{"groupname":"b","testname":"contentLanguage"},{"groupname":"m","testname":"interests"}]', 'wID': '7b0371bd4212941d642b62f18ab4d650b09c1cee5b3b36e7a68f47bc6abed147', 'osVersion': '11', 'model': 'SM-G9810', 'packageName': 'com.next.innovation.takatak', 'networkType': 'WIFI', 'installMarket': 'unknown', 'utmSource': 'google-play', 'ctID': '__a9b65b5bf2354f598120be5d7f1a53b9', 'mnc': '0', 'osName': 'Android', 'advertiseID': '969419eb-81ea-4e0e-b009-9d4a4905ba96', 'versionCode': '10011403', 'adOptOut': 'false', 'utmMedium': 'organic', 'waitTime': '1151', 'androidID': '8b86c090d0f54a71', 'lastUpdateTime': '1618821476962', 'runTime': '2021-04-29 15:00:34', 'caseName': 'case_like_click_trending'}, {'eventName': 'playerBuffering', 'currentPos': '0', 'versionName': '1.14.3.debug', 'mcc': '0', 'locale': 'en-US', 'uuid': '4bcb4874-92cb-474a-bb36-eb39dd329f1e767155257', 'sid': '1', 'manufacturer': 'samsung', 'firstInstallTime': '1618557961942', 'itemID': '3e64d60d480c56278383bc1975e7c71e', 'loadTime': '995', 'abtest': '[{"groupname":"a","testname":"anonymousFollow"},{"groupname":"b","testname":"contentLanguage"},{"groupname":"m","testname":"interests"}]', 'wID': '7b0371bd4212941d642b62f18ab4d650b09c1cee5b3b36e7a68f47bc6abed147', 'osVersion': '11', 'model': 'SM-G9810', 'attach': '{"recall_name":"ManualTopRecall","tagPoolFlow":"notag","timestamp":1619679637524,"small_flow_name":"mx_hot_tab_internal_version_2_0_C1","index":1,"log_id":"c255j5cvov6tn7ua5vug"}', 'packageName': 'com.next.innovation.takatak', 'networkType': 'WIFI', 'installMarket': 'unknown', 'utmSource': 'google-play', 'ctID': '__a9b65b5bf2354f598120be5d7f1a53b9', 'mnc': '0', 'length': '12586', 'osName': 'Android', 'advertiseID': '969419eb-81ea-4e0e-b009-9d4a4905ba96', 'versionCode': '10011403', 'adOptOut': 'false', 'publisherID': 'xt0.c3847627a3987217fc7c87f4e7770e24d555ae43c2960717c9db322bf2daf770678823fdc3bc37d02cf8fdfebb3c5804', 'utmMedium': 'organic', 'androidID': '8b86c090d0f54a71', 'lastUpdateTime': '1618821476962', 'runTime': '2021-04-29 15:00:34', 'caseName': 'case_like_click_trending'}, {'eventName': 'playBandwidth', 'bitrate': '20018246', 'versionName': '1.14.3.debug', 'mcc': '0', 'locale': 'en-US', 'uuid': '4bcb4874-92cb-474a-bb36-eb39dd329f1e767155257', 'sid': '1', 'manufacturer': 'samsung', 'firstInstallTime': '1618557961942', 'itemID': '3e64d60d480c56278383bc1975e7c71e', 'abtest': '[{"groupname":"a","testname":"anonymousFollow"},{"groupname":"b","testname":"contentLanguage"},{"groupname":"m","testname":"interests"}]', 'wID': '7b0371bd4212941d642b62f18ab4d650b09c1cee5b3b36e7a68f47bc6abed147', 'osVersion': '11', 'model': 'SM-G9810', 'packageName': 'com.next.innovation.takatak', 'networkType': 'WIFI', 'installMarket': 'unknown', 'utmSource': 'google-play', 'ctID': '__a9b65b5bf2354f598120be5d7f1a53b9', 'mnc': '0', 'osName': 'Android', 'advertiseID': '969419eb-81ea-4e0e-b009-9d4a4905ba96', 'versionCode': '10011403', 'adOptOut': 'false', 'elapseMs': '627', 'bytes': '1568930', 'utmMedium': 'organic', 'androidID': '8b86c090d0f54a71', 'lastUpdateTime': '1618821476962', 'runTime': '2021-04-29 15:00:34', 'caseName': 'case_like_click_trending'}, {'eventName': 'likeClicked', 'itemType': 'Video', 'source': 'Trending', 'versionName': '1.14.3.debug', 'mcc': '0', 'locale': 'en-US', 'uuid': '4bcb4874-92cb-474a-bb36-eb39dd329f1e767155257', 'sid': '1', 'manufacturer': 'samsung', 'firstInstallTime': '1618557961942', 'itemID': '3e64d60d480c56278383bc1975e7c71e', 'abtest': '[{"groupname":"a","testname":"anonymousFollow"},{"groupname":"b","testname":"contentLanguage"},{"groupname":"m","testname":"interests"}]', 'wID': '7b0371bd4212941d642b62f18ab4d650b09c1cee5b3b36e7a68f47bc6abed147', 'osVersion': '11', 'playTime': '2165', 'model': 'SM-G9810', 'attach': '{"recall_name":"ManualTopRecall","tagPoolFlow":"notag","timestamp":1619679637524,"small_flow_name":"mx_hot_tab_internal_version_2_0_C1","index":1,"log_id":"c255j5cvov6tn7ua5vug"}', 'packageName': 'com.next.innovation.takatak', 'networkType': 'WIFI', 'installMarket': 'unknown', 'utmSource': 'google-play', 'ctID': '__a9b65b5bf2354f598120be5d7f1a53b9', 'mnc': '0', 'length': '0', 'index': '0', 'osName': 'Android', 'advertiseID': '969419eb-81ea-4e0e-b009-9d4a4905ba96', 'versionCode': '10011403', 'adOptOut': 'false', 'publisherID': 'xt0.c3847627a3987217fc7c87f4e7770e24d555ae43c2960717c9db322bf2daf770678823fdc3bc37d02cf8fdfebb3c5804', 'requestID': '6115ea92577abb862d31e75f3a5ab1e8', 'fromstack': '[{"id":"3e64d60d480c56278383bc1975e7c71e","source":"Trending","type":"playback"},{"source":"Trending"},{"source":"splash"}]', 'utmMedium': 'organic', 'androidID': '8b86c090d0f54a71', 'lastUpdateTime': '1618821476962', 'runTime': '2021-04-29 15:00:34', 'caseName': 'case_like_click_trending'}, {'eventName': 'likeSucceed', 'itemType': 'Video', 'source': 'Trending', 'versionName': '1.14.3.debug', 'mcc': '0', 'locale': 'en-US', 'uuid': '4bcb4874-92cb-474a-bb36-eb39dd329f1e767155257', 'sid': '1', 'manufacturer': 'samsung', 'firstInstallTime': '1618557961942', 'itemID': '3e64d60d480c56278383bc1975e7c71e', 'abtest': '[{"groupname":"a","testname":"anonymousFollow"},{"groupname":"b","testname":"contentLanguage"},{"groupname":"m","testname":"interests"}]', 'wID': '7b0371bd4212941d642b62f18ab4d650b09c1cee5b3b36e7a68f47bc6abed147', 'osVersion': '11', 'model': 'SM-G9810', 'attach': '{"recall_name":"ManualTopRecall","tagPoolFlow":"notag","timestamp":1619679637524,"small_flow_name":"mx_hot_tab_internal_version_2_0_C1","index":1,"log_id":"c255j5cvov6tn7ua5vug"}', 'packageName': 'com.next.innovation.takatak', 'networkType': 'WIFI', 'installMarket': 'unknown', 'utmSource': 'google-play', 'ctID': '__a9b65b5bf2354f598120be5d7f1a53b9', 'mnc': '0', 'length': '0', 'index': '0', 'osName': 'Android', 'advertiseID': '969419eb-81ea-4e0e-b009-9d4a4905ba96', 'versionCode': '10011403', 'adOptOut': 'false', 'publisherID': 'xt0.c3847627a3987217fc7c87f4e7770e24d555ae43c2960717c9db322bf2daf770678823fdc3bc37d02cf8fdfebb3c5804', 'requestID': '6115ea92577abb862d31e75f3a5ab1e8', 'fromstack': '[{"id":"3e64d60d480c56278383bc1975e7c71e","source":"Trending","type":"playback"},{"source":"Trending"},{"source":"splash"}]', 'utmMedium': 'organic', 'androidID': '8b86c090d0f54a71', 'lastUpdateTime': '1618821476962', 'runTime': '2021-04-29 15:00:34', 'caseName': 'case_like_click_trending'}, {'eventName': 'likeSucceed', 'itemType': 'Video', 'source': 'Trending', 'versionName': '1.14.3.debug', 'mcc': '0', 'locale': 'en-US', 'uuid': '4bcb4874-92cb-474a-bb36-eb39dd329f1e767155257', 'sid': '1', 'manufacturer': 'samsung', 'firstInstallTime': '1618557961942', 'itemID': '3e64d60d480c56278383bc1975e7c71e', 'abtest': '[{"groupname":"a","testname":"anonymousFollow"},{"groupname":"b","testname":"contentLanguage"},{"groupname":"m","testname":"interests"}]', 'wID': '7b0371bd4212941d642b62f18ab4d650b09c1cee5b3b36e7a68f47bc6abed147', 'osVersion': '11', 'model': 'SM-G9810', 'attach': '{"recall_name":"ManualTopRecall","tagPoolFlow":"notag","timestamp":1619679637524,"small_flow_name":"mx_hot_tab_internal_version_2_0_C1","index":1,"log_id":"c255j5cvov6tn7ua5vug"}', 'packageName': 'com.next.innovation.takatak', 'networkType': 'WIFI', 'installMarket': 'unknown', 'utmSource': 'google-play', 'ctID': '__a9b65b5bf2354f598120be5d7f1a53b9', 'mnc': '0', 'length': '0', 'index': '0', 'osName': 'Android', 'advertiseID': '969419eb-81ea-4e0e-b009-9d4a4905ba96', 'versionCode': '10011403', 'adOptOut': 'false', 'publisherID': 'xt0.c3847627a3987217fc7c87f4e7770e24d555ae43c2960717c9db322bf2daf770678823fdc3bc37d02cf8fdfebb3c5804', 'requestID': '6115ea92577abb862d31e75f3a5ab1e8', 'fromstack': '[{"id":"3e64d60d480c56278383bc1975e7c71e","source":"Trending","type":"playback"},{"source":"Trending"},{"source":"splash"}]', 'utmMedium': 'organic', 'androidID': '8b86c090d0f54a71', 'lastUpdateTime': '1618821476962', 'runTime': '2021-04-29 15:00:34', 'caseName': 'case_like_click_trending'}, {'eventName': 'rateGuideShow', 'versionName': '1.14.3.debug', 'mcc': '0', 'locale': 'en-US', 'uuid': '4bcb4874-92cb-474a-bb36-eb39dd329f1e767155257', 'sid': '1', 'manufacturer': 'samsung', 'firstInstallTime': '1618557961942', 'abtest': '[{"groupname":"a","testname":"anonymousFollow"},{"groupname":"b","testname":"contentLanguage"},{"groupname":"m","testname":"interests"}]', 'wID': '7b0371bd4212941d642b62f18ab4d650b09c1cee5b3b36e7a68f47bc6abed147', 'osVersion': '11', 'model': 'SM-G9810', 'packageName': 'com.next.innovation.takatak', 'networkType': 'WIFI', 'installMarket': 'unknown', 'utmSource': 'google-play', 'ctID': '__a9b65b5bf2354f598120be5d7f1a53b9', 'mnc': '0', 'osName': 'Android', 'advertiseID': '969419eb-81ea-4e0e-b009-9d4a4905ba96', 'versionCode': '10011403', 'adOptOut': 'false', 'fromstack': '[{"id":"3e64d60d480c56278383bc1975e7c71e","source":"Trending","type":"playback"},{"source":"Trending"},{"source":"splash"}]', 'utmMedium': 'organic', 'androidID': '8b86c090d0f54a71', 'lastUpdateTime': '1618821476962', 'runTime': '2021-04-29 15:00:34', 'caseName': 'case_like_click_trending'}]
#     verify = Verify(case_events_list, standard_log)
#     verified_list = verify.verify_main()
#     print(verified_list)



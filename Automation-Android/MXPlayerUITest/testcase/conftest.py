import json
from decimal import Decimal
import time
from pprint import pprint
from _pytest import terminal
import requests


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    '''收集测试结果'''
    # 查看测试结果中stats
    # print(terminalreporter.stats)
    # 查看所有测试结果
    # pprint(terminalreporter.__dict__)

    total = terminalreporter._numcollected
    passed = len([i for i in terminalreporter.stats.get("passed", []) if i.when != 'teardown'])
    failed = len([i for i in terminalreporter.stats.get("failed", []) if i.when != 'teardown'])
    error = len([i for i in terminalreporter.stats.get("error", []) if i.when != 'teardown'])
    skipped = len([i for i in terminalreporter.stats.get("skipped", []) if i.when != 'teardown'])
    duration = time.time() - terminalreporter._sessionstarttime
    deselected = len([i for i in terminalreporter.stats.get("deselected", []) if i.when != 'teardown'])  # 过滤的用例数
    success_rate = passed / (total - deselected) * 100
    # Decimal(success_rate).quantize(Decimal("0.00"))
    content = "【自动化测试报告】\t\n" \
              "用例总数：%s\t\n" \
              "执行用例总数：%s \t\n" \
              "执行成功数：%s \t\n" \
              "执行失败数：%s \t\n" \
              "执行ERROR数：%s \t\n" \
              "执行SKIP数：%s \t\n" \
              "执行成功率：%.2f %%  \t\n" \
              "执行时长：%.2f 秒 \t\n" % (
              total, total - deselected, passed, failed, error, skipped, success_rate, duration)
    # 打印测试报告
    print(content)


    # 所有测试结果
    all = terminalreporter.__dict__
    # print(all["_progress_nodeids_reported"])

    # 发送测试结果到测试平台
    # 生成请求 body 数据
    timeArray = time.localtime(terminalreporter._sessionstarttime)
    start_time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    total_time = str(Decimal(duration).quantize(Decimal("0.00")))+"s"
    if success_rate == 100:
        status = "0"
    else:
        status = "1"
    testcase = str(all["_progress_nodeids_reported"])

    # 获取失败测试用例
    results = []
    status_list = ["error", "failed", "skipped"]
    for key in terminalreporter.stats:
        if key in status_list:
            results.append(str(terminalreporter.stats[key]))
    # 将字符串拼接起来
    info = ""
    for i in range(len(results)):
        info += results[i]

    # 生成 http 请求
    url = 'http://qatest-monitor.mxplay.com/energy/interface_auto/insert'
    headers = {
        'Content-Type': 'application/json;charset=utf-8'
    }
    payload = {
        "startTime": start_time,
        "success": success_rate,
        "serverName": "com.mxtech.videoplayer.ad",
        "caseName": testcase,
        "totalTime": total_time,
        "status": status,
        "type": "1",
        "msgInfo": info,
    }
    data_json = json.dumps(payload)
    print(data_json)


    # 发送请求
    r = requests.post(url=url, headers=headers, data=data_json)
    #
    # print(r.status_code)
    # print(r.text)
    print(r.json())
    if r.status_code == 200:
        print("Success")
    else:
        print("Failed")




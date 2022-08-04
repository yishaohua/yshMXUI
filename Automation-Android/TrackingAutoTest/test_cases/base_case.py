from abc import abstractmethod
from handler.analyser import Analyser
from handler.mxsql import MXSQL
from handler.verify import Verify


class BaseCase:

    def __init__(self, title, device, run_time):
        self.title = title
        self.device = device
        self.log_file = f"./logs/{self.title}.txt"
        self.analyser = Analyser(device.package_name)
        self.mxsql = MXSQL(device.package_name)
        self.run_time = run_time
        # 需要根据不同case，定义具体的check_points
        self.check_points = {}

    # 需要根据不同case，实现具体的操作步骤
    @abstractmethod
    def run_steps(self):
        pass

    def run(self):
        print(f"开始执行，case: {self.title}")

        # 执行UI测试步骤
        self.device.set_up()
        self.run_steps()
        self.device.tear_down(self.log_file)

        # 分析log，得到events list
        event_list = self.analyser.analyse(self.log_file)

        # 校验是否符合预期
        verify = Verify(event_list, self.check_points, self.title)
        verified_events = verify.verify_main()

        # 结果里加上时间戳
        for event in verified_events:
            event['runTime'] = self.run_time

        # 结果入库
        self.mxsql.insert_list(verified_events)
        self.mxsql.close()


from handler.mxsql import MXSQL


class Reporter:
    def __init__(self, package_name):
        self.package_name = package_name
        self.sql = MXSQL(package_name)
        self.file_name = self.init_file_name()
        print("初始化Report完成")

    def init_file_name(self):
        file_name = './reports/default.txt'
        if self.package_name == 'com.next.innovation.takatak':
            file_name = './reports/takatak_result.txt'
        if self.package_name == 'com.mxtech.videoplayer.ad':
            file_name = './reports/mxplayer_result.txt'
        return file_name

    def make_txt(self, run_time):
        fail = self.sql.get_result_fail(run_time)
        succeed = self.sql.get_result_succeed(run_time)
        with open(self.file_name, mode='w+') as file:
            file.write('---------------------------failed cases-----------------------\n')
            for line in fail:
                line = str(tuple(line))
                file.writelines(line + '\n')
            file.write('---------------------------succeed cases----------------------\n')
            for line in succeed:
                line = str(tuple(line))
                file.writelines(line + '\n')
        self.sql.close()
        if len(fail) > 0:
            return False
        else:
            return True


import datetime
import sys
import traceback
from functools import wraps



class logit(object):
    def __init__(self, logfile='./error.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            try:
                self.opened_file = open(self.logfile, 'a')
                func(*args, **kwargs)
            except AssertionError as e:
                # 将AssertionError写入日志
                cur_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
                error_string = func.__name__ + " AssertionError: " + str(e)
                log_string = cur_time + error_string
                self.opened_file.write(log_string + '\n')
                # 打印出AssertionError
                print('\n' + log_string + '\n')
                # 打开logfile并写入
                # with open(self.logfile, 'a') as opened_file:
                #     # 现在将日志打到指定的文件
                #     opened_file.write(log_string + '\n')
                # 现在，发送一个通知
                # self.notify()
                # return func(*args, **kwargs)
            except:
                # 将异常写入日志
                cur_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
                log_string = cur_time + func.__name__ + str(sys.exc_info())
                self.opened_file.write(log_string + '\n')
                # 将异常发生的脚本名称写入日志，用于再次运行
                ex_type, ex_val, ex_stack = sys.exc_info()
                error_log = []
                for stack in traceback.extract_tb(ex_stack):
                    error_log.append(str(stack))
                error_file = error_log[1].split("testcase/")[1].split(",")[0]
                # error_file:video/test_notice.py
                self.opened_file.write("error_file:" + error_file + '\n')
            finally:
                self.opened_file.close()
        return wrapped_function

    def notify(self):
        # logit只打日志，不做别的
        pass
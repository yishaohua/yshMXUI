# 数据库操作类，使用方法：
# cursor = MXSQL('package name')
# cursor.insert()
# cursor.close()

import sqlite3
import json


class MXSQL:

    def __init__(self, package_name):
        self.package_name = package_name
        self.conn = sqlite3.connect('./database/tracking.db')
        self.cursor = self.conn.cursor()
        if self.package_name == 'com.next.innovation.takatak':
            self.table_name = 'takatak'
        if self.package_name == 'com.mxtech.videoplayer.ad':
            self.table_name = 'mxplayer'
        self.create_table()
        print("初始化MXSQL完成")

    def create_table(self):
        # 建表，需要两个参数：表名，参数名，ID自动生成，自增，一般不需要调用该方法
        sql = f"CREATE TABLE IF NOT EXISTS {self.table_name} (" \
              f"ID integer primary key autoincrement, " \
              f"eventName TEXT, " \
              f"versionName TEXT, " \
              f"caseName TEXT, " \
              f"runTime TEXT, " \
              f"result TEXT," \
              f"failedReason TEXT," \
              f"params TEXT)"
        self.cursor.execute(sql)
        self.conn.commit()

    def insert_list(self, con_list):
        # 传入list和key
        keys = ('eventName', 'versionName', 'caseName', 'runTime', 'result', 'failedReason', 'params')
        for log_dict in con_list:
            values = (
                log_dict.get('eventName'), log_dict.get('versionName'), log_dict.get('caseName'),
                log_dict.get('runTime'),
                log_dict.get('result'), log_dict.get('failedReason'), json.dumps(log_dict))
            self.insert(keys, values)

    def insert(self, keys, values):
        # 需要三个参数，表名，key,value
        sql = f"insert into {self.table_name} {keys} values{values}"
        self.cursor.execute(sql)
        self.conn.commit()

    def query_by_version_name(self, version_name):
        # 通过versionCode查询结果，参数：表名，versionCode,返回结果为列表
        sql = f'select * from {self.table_name} where versionName=\'{version_name}\''
        raw = self.cursor.execute(sql)
        return raw.fetchall()

    def query_by_result(self, time, result):
        sql = f'select ID,eventName,versionName,caseName,runTime,result,failedReason from {self.table_name} where runTime=\'{time}\' and result=\'{result}\''
        raw = self.cursor.execute(sql)
        return raw.fetchall()

    def query_by_case_title(self, case_name, num=10):
        # 通过caseName查询结果，参数待定...
        sql = f'select * from {self.table_name} where caseName=\'{case_name}\''
        self.cursor.execute(sql)

    def get_result_succeed(self, time):
        result = self.query_by_result(time, 'true')
        return result

    def get_result_fail(self, time):
        result = self.query_by_result(time, 'false')
        return result

    def close(self):
        self.cursor.close()
        self.conn.close()

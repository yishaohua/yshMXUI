# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# # @Time : 2019-09-18 11:37
# # @Author : lmh
# # @Software: PyCharm
# #
#
import unittest
from testcase.requestmodel import reqmodel,get_excelconf_data,testcases_filter,get_excel_data
from zz_other import ddt
from conf.config import *

testcases = []
cases_ad_release = []
cases_beta_release = []
if env == 'release' or env == 'pre':
    testcases = get_excel_data(env='release')[1:]
    # 过滤用例
    cases_ad_release = testcases_filter(testcases,version='ad')[:]
    cases_beta_release = testcases_filter(testcases,version='beta')[:]
    # 获取对应的参数化数据
    excelconf_ad_release = get_excelconf_data(version='ad', env='release')
    excelconf_beta_release = get_excelconf_data(version='beta', env='release')

@ddt.ddt
class test_Cases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    @unittest.skipUnless(env == 'pre', '跳过ad pre的测试用例')
    @unittest.skipIf(cases_ad_release == [], 'cases_ad_pre 为空')
    @ddt.data(*cases_ad_release)
    def test_ad_pre(self, data):
        '''
        ad pre 用例
        '''
        reqmodel(data, configdata=excelconf_ad_release, header=header_ad_pre,
                              host=host_ad_pre, resprename='ad-release')

    @unittest.skipUnless(env == 'pre', '跳过beta pre的测试用例')
    @unittest.skipIf(cases_beta_release == [], 'cases_beta_pre 为空')
    @ddt.data(*cases_beta_release)
    def test_beta_pre(self, data):
        '''
        beta pre 用例
        '''
        reqmodel(data, configdata=excelconf_beta_release, header=header_beta_pre,
                              host=host_beta_pre, resprename='beta-release')

    @unittest.skipUnless(env == 'release', '跳过ad release的测试用例')
    @unittest.skipIf(cases_ad_release == [], 'cases_ad_release 为空')
    @ddt.data(*cases_ad_release)
    def test_ad_release(self,data):
        '''
        ad release 用例
        '''
        reqmodel(data, configdata=excelconf_ad_release, header=header_ad_release,
                              host=host_ad_release, resprename='ad-release')

    @unittest.skipUnless(env == 'release', '跳过beta release的测试用例')
    @unittest.skipIf(cases_beta_release == [], 'beta_release_cases 为空')
    @ddt.data(*cases_beta_release)
    def test_beta_release(self, data):
        '''
        beta release 用例
        '''
        reqmodel(data, configdata=excelconf_beta_release, header=header_beta_release,
                              host=host_beta_release, resprename='beta-release')






import logging
import os
from time import sleep

import yaml
from page.app import App
from page.logit import logit


class TestLocal:
    """
    测试Local页面
    """
    def setup_class(self):
        """
        setup_class方法，测试类中 所有测试方法前执行一次
        修改mcc，需要先修改mcc，确保有tab选项
        如果不需要重启或使用新安装的app，可以注释掉直接进入index页
        :return:
        """
        logging.info("TestLocal:setup_class")
        # self.page = App.start()
        # 需要修改mcc的测试包
        # self.page.modify_mcc()
        # 获取测试用例数据
        testcase_file = os.path.dirname(__file__).split("testcase")[0] + r"data/testcase_data/local/local.yaml"
        self.local_data = yaml.safe_load(open(testcase_file, "r", encoding="utf-8"))
        # 需要获取系统存储权限的测试包
        self.local_page = App.start().open_store_settings()

    def setup_method(self, method):
        logging.info("TestLocal:setup_method")
        # 记录类名和方法名
        logging.info(type(self).__name__+":"+method.__name__)

    def teardown_class(self):
        logging.info("TestLocal:teardown_class")
        App.quit()

    @logit()
    def test_to_local_page(self):
        """
        测试本地local标题显示正确
        :return:
        """
        data_list = self.local_data["test_to_local_page"]
        title = data_list["title"]
        actual_title = self.local_page.get_title()
        assert actual_title == title

    @logit()
    def test_view_menu_content(self):
        """
        测试点击视图菜单弹窗
        :return:
        """
        data_list = self.local_data["test_view_menu_content"]
        self.local_page.click_view_menu_button()
        title = data_list["title"]
        actual_text = self.local_page.get_view_menu_title()
        assert actual_text == title
        self.local_page.click_cancel_button()

    @logit()
    def test_search_input(self):
        """
        测试搜索功能是否正常
        :return:
        """
        data_list = self.local_data["test_search_input"]
        for n in range(len(data_list)):
            self.local_page.click_search_button()
            if self.local_page.is_search_input_exist():
                self.local_page.input_search_text(data_list[n])
            sleep(2)
            title_text = self.local_page.get_title()
            assert data_list[n] in title_text


    # local卡片会变，需要配置
    # def test_tab_title_show(self):
    #     """
    #     测试tab的标题显示是否正确
    #     :return:
    #     """
    #     data_list = self.local_data["test_tab_title_show"]
    #     actual_list = self.local_page.get_tab_title()
    #     print(actual_list)
    #     for n in range(len(data_list)):
    #         print(data_list[n])
    #         print(actual_list[n])
    #         assert actual_list[n] == data_list[n]

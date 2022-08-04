import logging

from page.base_page import BasePage

from driver.create_driver import CreateDriver
from page.local.local_init_page import LocalInitPage
from page.local.index import Index


class App:

    @classmethod
    def start(cls):
        """
        启动一个app  返回driver给LocalPage
        :return:
        """
        logging.info("App:start 开始获取driver")
        cls.obj_creat_driver = CreateDriver()
        cls.driver = cls.obj_creat_driver.get_driver()
        logging.info("App:start 获取driver成功")
        # 进入主页
        return LocalInitPage(cls.driver)

    @classmethod
    def start_logged_in(cls):
        """
        非首次启动app  从哪个模块杀死app，启动之后，就会进入哪个模块的首页
        :return:
        """
        logging.info("App:start_logged_in 开始获取driver")
        cls.obj_creat_driver = CreateDriver()
        # 设置不重置app
        cls.driver = cls.obj_creat_driver.get_driver(noReset=True)
        logging.info("App:start_logged_in 获取driver成功")
        # 导航页面，调用对应的方法进入对应的模块
        return Index(cls.driver)

    @classmethod
    def get_driver(cls, udid):
        """
        启动一个app，返回driver
        :return:
        """
        logging.info("App:get_app_driver 开始获取driver")
        cls.obj_creat_driver = CreateDriver()
        cls.driver = cls.obj_creat_driver.get_driver_by_device(noReset=True, udid=udid)
        logging.info("App:start_logged_in 获取driver成功")
        # return cls.driver
        return BasePage(cls.driver)

    @classmethod
    def get_app_driver(cls, udid):
        """
        启动一个app，返回到index页面，选择进入模块
        :return:
        """
        logging.info("App:get_app_driver 开始获取driver")
        cls.obj_creat_driver = CreateDriver()
        cls.driver = cls.obj_creat_driver.get_driver_by_device(noReset=True, udid=udid)
        logging.info("App:start_logged_in 获取driver成功")
        # 导航页面，调用对应的方法进入对应的模块
        return Index(cls.driver)

    @classmethod
    def quit(cls):
        cls.driver.quit()
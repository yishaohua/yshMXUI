# 导入依赖
import os

from appium import webdriver


class CreateDriver():

    def get_driver(cls, noReset=False):
        # 配置项
        caps = {}
        caps["platformName"] = "Android"  # 操作系统平台
        # caps["platformVersion"] = "11"  # 填写操作系统版本
        caps["deviceName"] = "RF8M83HHAMY"
        # 测试设备udid，可以指定模拟器
        caps["udid"] = "RF8M83HHAMY"
        # adb logcat | findstr -i displayed  window使用该命令可以查看
        # caps["app"] = f"{os.path.abspath(os.curdir)}/../app/PlayerAd-neon-market-v8-vc1330001480-vn1.41.10.0.debug-0.apk"  # 测试apk文件
        caps["appPackage"] = "com.mxtech.videoplayer.ad"  # 测试包名
        caps["appActivity"] = ".ActivityWelcomeMX"  # 测试app入口
        # caps["autoGrantPermissions"] = "true"
        # caps["ensureWebviewsHavePages"] = True
        # 用来定位toast
        caps["automationName"] = "uiautomator2"
        caps["unicodeKeyboard"] = True
        # appium等待命令间隔时长，默认60秒，适当延长超时时间
        caps["newCommandTimeout"] = "3000"
        # caps["resetKeyboard"] = True
        # 设置不自动清除app的数据
        caps["noReset"] = noReset

        # 设置driver
        driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return driver

    def get_driver_by_device(cls, noReset=False, udid=None):
        # 配置项
        caps = {}
        caps["platformName"] = "Android"  # 操作系统平台
        caps["udid"] = udid
        caps["appPackage"] = "com.mxtech.videoplayer.ad"  # 测试包名
        caps["appActivity"] = ".ActivityWelcomeMX"  # 测试app入口
        caps["automationName"] = "uiautomator2"
        caps["unicodeKeyboard"] = True
        caps["newCommandTimeout"] = "3000"
        caps["noReset"] = noReset

        # 设置driver
        driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", caps)
        driver.implicitly_wait(10)
        return driver


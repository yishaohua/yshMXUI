import logging

from selenium.webdriver.common.by import By


def handle_black_list(fun):
    def run(*args, **kwargs):
        black_list = [
            # video 详情页18岁弹窗
            (By.XPATH, "//*[@text= '确认']"),
            # Android 6系统 获取权限允许按钮
            (By.ID, 'com.android.packageinstaller:id/permission_allow_button'),
            # 小米11 Adroid获取权限允许按钮
            (By.ID, 'com.lbe.security.miui:id/permission_allow_button'),
            # local引导弹层 确认按钮
            (By.ID, 'com.mxtech.videoplayer.ad:id/tv_ok'),
            # 应用评分弹窗 以后再说按钮
            (By.ID, 'com.mxtech.videoplayer.ad:id/btn_cancel'),
            # 视频播放，超级省流量模式，确定按钮
            (By.ID, "com.mxtech.videoplayer.ad:id/av1_confirm"),
            # # music中播放音频引导动画
            # (By.ID, "com.mxtech.videoplayer.ad:id/view_pager_2"),
            # music中点击录音按钮的权限提醒
            (By.ID, "android:id/button1"),
            # 应用评价弹窗中的以后再说按钮 重复了
            # (By.ID, "com.mxtech.videoplayer.ad:id/btn_cancel"),
            # 音乐播放点暂停后的广告关闭按钮
            (By.ID, "com.mxtech.videoplayer.ad:id/ad_cross_button"),
            # 点击返回后出现的广告关闭按钮
            (By.XPATH, "//*[@resource-id='close-button-container']"),
            # 视频广告
            (By.XPATH, "//*[@resource-id='adContainer']/android.view.View[1]/android.view.View[1]/android.widget.Button"),
            # game页弹窗
            (By.ID, "com.mxtech.videoplayer.ad:id/iv_close")
        ]
        # 相当于 self
        instance = args[0]
        try:
            return fun(*args, **kwargs)
        except Exception:
            # 设置隐式等待为0
            instance.driver.implicitly_wait(0)
            # 遍历黑名单中的元素
            for locator in black_list:
                # print(locator)
                elements = instance.find_elements_once(locator)
                # print(elements)
                if len(elements) > 0:
                    # 点击找到的黑名单中的元素
                    elements[0].click()
                    print("handle_exception 点击了这个元素：%s" % locator[1])
            # 再次将隐式等待变更为原来默认的值
            instance.driver.implicitly_wait(10)
            return fun(*args, **kwargs)
    return run
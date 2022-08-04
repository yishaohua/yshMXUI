from selenium.webdriver.common.by import By

from page.base_page import BasePage


class TakatakPage(BasePage):
    """
    继承通用页面
    Takatak页面
    """
    # 点击 like 区域
    __like_area = (By.ID, "com.mxtech.videoplayer.ad:id/like_area")\
    # 发布者头像
    __owner_img = (By.ID, "com.mxtech.videoplayer.ad:id/detail_owner")
    # 关注视频发布者按钮
    __follow_button = (By.ID, "com.mxtech.videoplayer.ad:id/iv_follow")
    # 点赞按钮
    __like_button = (By.ID, "com.mxtech.videoplayer.ad:id/detail_like")
    # 点赞数
    __like_num = (By.ID, "com.mxtech.videoplayer.ad:id/detail_like_count")
    # 评论按钮
    __comment_button = (By.ID, "com.mxtech.videoplayer.ad:id/detail_comment")
    # 评论数
    __comment_num = (By.ID, "com.mxtech.videoplayer.ad:id/detail_comment_count")
    # 分享按钮
    __share_button = (By.ID, "com.mxtech.videoplayer.ad:id/detail_share")
    # 发布按钮
    __publish_button = (By.ID, "com.mxtech.videoplayer.ad:id/iv_publish")
    # 发布者名字
    __publisher_name = (By.ID, "com.mxtech.videoplayer.ad:id/tv_publisher_name")

    # 评论详情
    # 评论标题
    __comment_detail_title = (By.ID, "com.mxtech.videoplayer.ad:id/comment_count_tv")
    # 评论关闭按钮
    __comment_close = (By.ID, "com.mxtech.videoplayer.ad:id/close_iv")

    def click_like_button(self):
        """
        点赞
        :return:
        """
        self.find_element_and_click(self.__like_button)
        return self

    def click_comment(self):
        """
        点击查看评论
        :return:
        """
        self.find_element_and_click(self.__comment_button)
        return self

    def get_comment_title(self):
        """
        获取评论标题 10.6K 评论
        :return:
        """
        return self.find_element_and_get_text(self.__comment_detail_title)

    def get_publisher_name(self):
        """
        获取发布者名字
        :return:
        """
        return self.find_element_and_get_text(self.__publisher_name)

    def click_comment_close(self):
        """
        点击关闭评论
        :return:
        """
        self.find_element_and_click(self.__comment_close)
        return self


import os
import yaml
from time import sleep
from page.app import App
from utils.log_util import LogUtil
from utils.common_util import banner_test, card_test


class TestMain:
    def setup_class(self):
        self.LOGGER = LogUtil().get_logger()
        print("MX MAIN RUN")
        self.LOGGER.info("------------------------------MX MAIN RUN------------------------------")
        self.driver = App.get_app_driver(udid="3663c969cc1c7ece")
        # app底部视频页
        self.LOGGER.info("video_home_page")
        self.video_page = self.driver.to_video_home_page()

        testcase_file = os.path.dirname(__file__).split("testcase")[0] + r"/testcase/test_main.yaml"
        self.search_live_tv_data = yaml.safe_load(open(testcase_file, "r", encoding="utf-8"))

    def teardown_class(self):
        self.LOGGER.info("------------------------------MX MAIN OVER------------------------------")
        App.quit()

    # def banner_test(self, page, data, tab_name):
    #     # print(tab_name, "页 banner 测试开始：")
    #     self.LOGGER.info(tab_name + "页 banner 测试开始：")
    #     try:
    #         # print("get banners number")
    #         self.LOGGER.info("get banners number")
    #         banners = page.get_banner_num()
    #         if banners != data["banners"]:
    #             # print("banner数量错误")
    #             self.LOGGER.info("banner数量错误")
    #     except Exception as e:
    #         self.LOGGER.info("获取banner数量失败！")
    #         self.LOGGER.info(e)
    #         self.video_page.slide_next_sheet((By.ID, "com.mxtech.videoplayer.ad:id/banner_image_view_card"), -400)
    #         banners = page.get_banner_num()
    #         if isinstance(banners, int):
    #             if banners != data["banners"]:
    #                 # print("banner数量错误")
    #                 self.LOGGER.info("banner数量错误")
    #         else:
    #             # print("广告弹窗干扰，banner数量获取失败!")
    #             self.LOGGER.info("重试获取banner数量失败！")
    #     try:
    #         # print("click chosen banner")
    #         self.LOGGER.info("点击banner")
    #         banner = self.video_page.click_select_banner(3)
    #         sleep(2)
    #         if tab_name == "mx vdesi" or tab_name == "shows":
    #             print(banner.get_video_title())
    #             self.LOGGER.info("get_video_title success"+banner.get_video_title())
    #         elif tab_name == "movies":
    #             print(banner.get_movie_title())
    #             self.LOGGER.info("get_movie_title success"+banner.get_movie_title())
    #         else:
    #             print(banner.get_video_title())
    #             self.LOGGER.info(banner.get_video_title())
    #             # self.LOGGER.info("点击banner获取video title 失败！")
    #         print(len(banner.get_related_video_list()))
    #         banner.click_return_button()
    #         sleep(2)
    #     except Exception as e:
    #         self.LOGGER.info(e)
    #         # print("banner 点击失败")
    #         self.LOGGER.info("banner 点击失败")
    #         self.video_page.click_return_button()
    #     return True

    # def card_test(self, page, data, tab_name):
    #     # print(tab_name, "页 card 测试开始：")
    #     self.LOGGER.info(tab_name + "页 card 测试开始：")
    #     self.LOGGER.info("find card start")
    #     if not page.search_card(data["search_card"][0], 100):
    #         self.LOGGER.info("未找到卡片: " + data["search_card"][0])
    #     if not page.search_card(data["search_card"][1], 100):
    #         self.LOGGER.info("未找到卡片: " + data["search_card"][1])
    #     self.LOGGER.info("click chosen card")
    #     # cardDetail = page.click_view_more(0)
    #     cardDetail = page.click_card_view_more(data["click_card"], 100)
    #     sleep(2)
    #     try:
    #         self.LOGGER.info("get card title")
    #         print(self.video_page.get_tool_bar_title())
    #     except Exception as e:
    #         self.LOGGER.info(data["click_card"] + "卡片详情获取失败！")
    #         self.video_page.click_return_button()
    #         self.video_page.swipe(540, 1300, 540, 1000, 500)
    #         cardDetail = page.click_card_view_more(data["click_card"], 100)
    #         if self.video_page.get_tool_bar_title():
    #             print(self.video_page.get_tool_bar_title())
    #             self.LOGGER.info("重试获取卡片详情成功"+self.video_page.get_tool_bar_title())
    #         else:
    #             # print(tab_name, "页卡片详情获取失败")
    #             self.LOGGER.info("重试获取" + data["click_card"]+"卡片详情获取失败！")
    #             self.LOGGER.info(e)
    #     sleep(2)
    #     cards = cardDetail.click_card(3)
    #     sleep(2)
    #     self.video_page.click_return_button()
    #     sleep(2)
    #     self.video_page.click_return_button()
    #     sleep(2)
    #     return True

    # @logit()
    def test_home(self):
        print("test_home:------------------------------")
        # print(self.search_live_tv_data["video_card_data"]["HOME"])
        data = self.search_live_tv_data["video_card_data"]["HOME"]
        page = self.video_page
        sleep(2)
        banner_test(self.LOGGER, self.video_page, page, data, "home")
        card_test(self.LOGGER, self.video_page, page, data, "home")
        # assert self.banner_test(page, data, "home") == True
        # assert self.card_test(page, data, "home") == True

    # @logit()
    def test_shows(self):
        print("test_shows:------------------------------")
        data = self.search_live_tv_data["video_card_data"]["SHOWS"]
        page = self.video_page.click_specified_tab("SHOWS")
        sleep(2)
        banner_test(self.LOGGER, self.video_page, page, data, "shows")
        card_test(self.LOGGER, self.video_page, page, data, "shows")

    # @logit()
    def test_movies(self):
        print("test_movies:------------------------------")
        data = self.search_live_tv_data["video_card_data"]["MOVIES"]
        page = self.video_page.click_specified_tab("MOVIES")
        sleep(2)
        banner_test(self.LOGGER, self.video_page, page, data, "movies")
        card_test(self.LOGGER, self.video_page, page, data, "movies")

    # @logit()
    def test_vdesi(self):
        print("test_mx vdesi:------------------------------")
        data = self.search_live_tv_data["video_card_data"]["MX VDESI"]
        page = self.video_page.click_specified_tab("MX VDESI")
        sleep(2)
        banner_test(self.LOGGER, self.video_page, page, data, "mx vdesi")
        card_test(self.LOGGER, self.video_page, page, data, "mx vdesi")

    # @logit()
    def test_vmusic(self):
        print("test_video music:------------------------------")
        data = self.search_live_tv_data["video_card_data"]["MUSIC"]
        page = self.video_page.click_specified_tab("MUSIC")
        sleep(2)
        banner_test(self.LOGGER, self.video_page, page, data, "video music")
        card_test(self.LOGGER, self.video_page, page, data, "video music")

    # @logit()
    def test_buzz(self):
        print("test_buzz:------------------------------")
        page = self.video_page.click_buzz_tab()
        sleep(2)
        self.LOGGER.info("点击 Comedy 类型")
        page.click_type_card("Comedy")
        sleep(2)
        self.video_page.click_return_button()
        try:
            page.slide_type_card()
        except Exception as e:
            self.LOGGER.info("返回可能异常，广告弹窗干扰")
            self.LOGGER.info(e)
            sleep(20)
            self.video_page.click_return_button()
            page.slide_type_card()
        try:
            self.LOGGER.info("点击buzz页视频")
            buzz_video = page.click_video(1)
        except Exception as e:
            self.LOGGER.info("可能存在buzz置顶广告干扰")
            self.LOGGER.info(e)
            buzz_video = page.click_video(0)
        self.LOGGER.info("click like..")
        buzz_video.click_like(0)
        buzz_video.click_watchlist(0)
        buzz_video.click_video(0)
        self.LOGGER.info("click video again")
        self.video_page.click_return_button()
        sleep(2)

    # @logit()
    def test_game(self):
        print("test_game:------------------------------")
        page = self.driver.to_game_page()
        sleep(2)
        try:
            print("获取游戏页金币数量", page.get_coin_count())
        except Exception as e:
            print("获取金币数量失败！")
            self.LOGGER.info(e)
        print("click coin_button")
        page.click_coin_button()
        sleep(2)
        page.click_return_button()
        print("check limit games")
        page.slide_limit_game()
        page.click_first_card()
        sleep(2)
        page.click_return_button()
        sleep(2)

    # @logit()
    def test_music(self):
        print("test_music:------------------------------")
        self.LOGGER.info("to_music_page")
        page = self.driver.to_music_page()
        sleep(2)
        page.swipe_banner()  # 避开广告
        self.LOGGER.info("click music banner")
        music_banner = page.click_banner()
        sleep(1)
        print("check is play all button", music_banner.is_play_all_exist())
        page.click_return_button()
        favorite_music = page.click_favorite()
        sleep(1)
        favorite_music.click_return_button()
        my_playlist = page.click_playlist()
        sleep(1)
        my_playlist.click_return_button()
        local_music = page.click_local()
        sleep(1)
        local_music.click_return_button()
        print(page.get_song_card_title())

from time import sleep
from selenium.webdriver.common.by import By


def banner_test(LOGGER, video_page, current_page, data, tab_name):
    LOGGER.info(tab_name + "页 banner 测试开始：")
    try:
        LOGGER.info("get banners number")
        banners = current_page.get_banner_num()
        if banners != data["banners"]:
            LOGGER.info("banner数量错误")
    except Exception as e:
        LOGGER.info("获取banner数量失败！")
        LOGGER.info(e)
        video_page.slide_next_sheet((By.ID, "com.mxtech.videoplayer.ad:id/banner_image_view_card"), -400)
        banners = current_page.get_banner_num()
        if isinstance(banners, int):
            if banners != data["banners"]:
                LOGGER.info("banner数量错误")
        else:
            LOGGER.info("重试获取banner数量失败！")
    try:
        LOGGER.info("点击banner")
        banner = video_page.click_select_banner(3)
        sleep(2)
        if tab_name == "mx vdesi" or tab_name == "shows":
            print(banner.get_video_title())
            LOGGER.info("get_video_title success" + banner.get_video_title())
        elif tab_name == "movies":
            print(banner.get_movie_title())
            LOGGER.info("get_movie_title success" + banner.get_movie_title())
        else:
            print(banner.get_video_title())
            LOGGER.info(banner.get_video_title())
        print(len(banner.get_related_video_list()))
        banner.click_return_button()
        sleep(2)
    except Exception as e:
        LOGGER.info(e)
        LOGGER.info("banner 点击失败")
        video_page.click_return_button()


def card_test(LOGGER, video_page, current_page, data, tab_name):
    LOGGER.info(tab_name + "页 card 测试开始：")
    LOGGER.info("find card start")
    if not current_page.search_card(data["search_card"][0], 100):
        LOGGER.info("未找到卡片: " + data["search_card"][0])
    if not current_page.search_card(data["search_card"][1], 100):
        LOGGER.info("未找到卡片: " + data["search_card"][1])
    LOGGER.info("click chosen card")
    try:
        cardDetail = current_page.click_card_view_more(data["click_card"], 100)
    except Exception as e:
        cardDetail = current_page.click_view_more(0)
        LOGGER.info(e)
    sleep(2)
    try:
        LOGGER.info("get card title")
        print(video_page.get_tool_bar_title())
    except Exception as e:
        LOGGER.info(data["click_card"] + "卡片详情获取失败！")
        video_page.click_return_button()
        video_page.swipe(540, 1300, 540, 1000, 500)
        cardDetail = current_page.click_card_view_more(data["click_card"], 100)
        if video_page.get_tool_bar_title():
            print(video_page.get_tool_bar_title())
            LOGGER.info("重试获取卡片详情成功" + video_page.get_tool_bar_title())
        else:
            LOGGER.info("重试获取" + data["click_card"] + "卡片详情获取失败！")
            LOGGER.info(e)
    sleep(2)
    cardDetail.click_card(3)
    sleep(2)
    video_page.click_return_button()
    sleep(2)
    video_page.click_return_button()
    sleep(2)


# if __name__ == '__main__':
#     LOGGER = LogUtil().get_logger()
#     home_data = {"banners": 6, "search_card": ["MX Original Web Shows", "Top 10 This Week"], "click_card": "MX Top Selected Movies"}
#     shows_data = {"banners": 6, "search_card": ["MX Original Web Shows", "Trending in Web Shows"], "click_card": "Binge On"}
#     driver = App.get_app_driver(udid="1ea218ee")
#     home_page = driver.to_video_home_page()
#     # shows_page = video_page.click_specified_tab("SHOWS")
#     banner_test(LOGGER, home_page, home_page, home_data, "home")
#     card_test(LOGGER, home_page, home_page, home_data, "home")

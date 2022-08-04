import os
import yaml
from time import sleep
from page.app import App
from selenium.webdriver.common.by import By

from utils.log_util import LogUtil


def main_test(start_page, tab_name, tab_work):
    if tab_name == "HOME":
        base_page = start_page
    else:
        base_page = start_page.click_specified_tab(tab_name)
    sleep(2)
    banners = base_page.get_banner_num()
    if banners != tab_work["banners"]:
        if isinstance(banners, int):
            mes = tab_name + "页banner数错误！，实际为 " + str(banners)
        else:
            start_page.slide_next_sheet((By.ID, "com.mxtech.videoplayer.ad:id/banner_image_view_card"), -400)
            banners = base_page.get_banner_num()
            if not isinstance(banners, int):
                mes = "广告弹窗干扰，"+tab_name + "页banner数量获取失败!"
            elif banners != tab_work["banners"]:
                mes = tab_name + "页banner数错误！，实际为 " + str(banners)
                print(tab_name, "页banner数不为6！")
            else:
                mes = ""
        LOGGER.info(mes)

    try:
        banner = start_page.click_select_banner(3)
        print(banner.get_video_title())
        print(len(banner.get_related_video_list()))
        banner.click_return_button()
        sleep(2)
    except Exception as e:
        LOGGER.info(tab_name + " banner click err")
        LOGGER.info(e)
        start_page.click_return_button()
    try:
        base_page.search_card(tab_work["search_card"][0])
        sleep(2)
        base_page.search_card(tab_work["search_card"][1])
        sleep(2)
    except Exception as e:
        LOGGER.info(tab_name + " card search err")
        LOGGER.info(e)

    cardDetail = base_page.click_card_view_more(tab_work["click_card"])
    sleep(2)
    try:
        print(start_page.get_tool_bar_title())
    except Exception as e:
        start_page.click_return_button()
        sleep(2)
        start_page.swipe(540, 1300, 540, 1000, 500)
        cardDetail = start_page.click_card_view_more(tab_work["click_card"])
        if start_page.get_tool_bar_title():
            print(start_page.get_tool_bar_title())
        else:
            LOGGER.info(tab_name + " card view more err")
            LOGGER.info(e)
    sleep(2)
    cards = cardDetail.click_card(3)
    sleep(2)
    start_page.click_return_button()
    sleep(2)
    start_page.click_return_button()
    sleep(2)


def news_test(start_page):
    news_page = start_page.click_news_tab()
    try:
        banner = news_page.click_select_banner(3)
        print(banner.get_tv_title())
        start_page.click_return_button()
    except Exception as e:
        LOGGER.info("news banner click err")
        LOGGER.info(e)
        start_page.click_return_button()
    sleep(2)
    try:
        print(news_page.get_channels_card_title())
        card = news_page.click_live_channel(1)
        print(card.get_tv_title())
        start_page.click_return_button()
    except Exception as e:
        LOGGER.info("news card click err")
        LOGGER.info(e)
    sleep(2)


def buzz_test(start_page):
    buzz_page = start_page.click_buzz_tab()
    sleep(2)
    buzz_page.click_type_card("Comedy")
    sleep(2)
    start_page.click_return_button()
    sleep(2)
    try:
        buzz_page.slide_type_card()
    except Exception as e:
        LOGGER.info("返回可能异常，广告弹窗干扰")
        LOGGER.info(e)
        sleep(60)
        start_page.click_return_button()
        buzz_page.slide_type_card()
    try:
        buzz_video = buzz_page.click_video(1)
    except Exception as e:
        print("可能存在buzz置顶广告干扰")
        LOGGER.info(e)
        buzz_video = buzz_page.click_video(0)
    print("click video")
    sleep(2)
    buzz_video.click_like(0)
    print("click like..")
    sleep(2)
    buzz_video.click_watchlist(0)
    sleep(2)
    buzz_video.click_video(0)
    print("click video again")
    sleep(2)
    buzz_video.click_return_button()
    sleep(2)


def game_test(start_page):
    # start_page.click_pop_close()
    # sleep(2)
    try:
        print(start_page.get_coin_count())
    except Exception as e:
        print("get_coin_count err")
        LOGGER.info(e)
    coin = start_page.click_coin_button()
    print("click coin_button")
    sleep(2)
    start_page.click_return_button()
    sleep(2)
    start_page.slide_limit_game()
    sleep(2)
    start_page.click_first_card()
    print("game page end")
    sleep(2)
    start_page.click_return_button()
    print("return")
    sleep(2)


def music_test(start_page):
    start_page.swipe_banner()
    music_banner = start_page.click_banner()
    sleep(2)
    print(music_banner.is_play_all_exist())
    music_banner.click_return_button()
    sleep(2)
    favorite_music = start_page.click_favorite()
    sleep(2)
    favorite_music.click_return_button()
    sleep(2)
    my_playlist = start_page.click_playlist()
    sleep(2)
    my_playlist.click_return_button()
    sleep(2)
    local_music = start_page.click_local()
    sleep(2)
    local_music.click_return_button()
    sleep(2)
    # recent_music = start_page.click_play_more()
    # sleep(2)
    # recent_music.click_return_button()
    print(start_page.get_song_card_title())


if __name__ == '__main__':
    LOGGER = LogUtil().get_logger()
    LOGGER.info("MX MAIN RUN")
    # udid = "ZH6LNF55T8TGTWEU"
    # udid = "1ea218ee"
    udid = "3663c969cc1c7ece"
    # udid = "RF8M83HHAMY"
    all_page = App.get_app_driver(udid=udid)
    # app底部视频页
    video_page = all_page.to_video_home_page()
    # 获取测试数据文件名
    testcase_file = os.path.dirname(__file__).split("testcase")[0] + r"/testcase/main_test.yaml"
    # 获取测试数据内容
    search_live_tv_data = yaml.safe_load(open(testcase_file, "r", encoding="utf-8"))
    for key in search_live_tv_data.keys():
        main_test(video_page, key, search_live_tv_data[key])
        sleep(2)
    news_test(video_page)
    buzz_test(video_page)
    # game
    game_page = all_page.to_game_page()
    sleep(2)
    game_test(game_page)
    # music
    music_page = all_page.to_music_page()
    sleep(2)
    music_test(music_page)

    sleep(5)
    LOGGER.info("MX MAIN OVER")
    App.quit()


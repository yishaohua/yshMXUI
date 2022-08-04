import logging
import os

import pytest


def rerun():
    """
    再次运行上次失败的测试用例脚本
    :return:
    """
    # 获取到失败的测试用例脚本名称
    rerun_list = []
    rerun_failed_files = []

    testcase_file = os.path.dirname(__file__).split("testcase")[0] + r"/testcase/error.log"
    # file = open(testcase_file)
    with open(testcase_file, "r") as file:
        while 1:
            lines = file.readlines()
            if not lines:
                break
            for line in lines:
                if "error_file:" in line:
                    file_name = line.split(":")[1]
                    if file_name not in rerun_list:
                        rerun_list.append(file_name)
        file.close()

    # 打印出需要重新运行的测试脚本
    print("rerun files: ")
    print(rerun_list)

    # 执行对应测试用例脚本
    if len(rerun_list) != 0:
        for i in range(len(rerun_list)):
            logging.info("rerun " + rerun_list[i])
            try:
                command = "pytest -vs " + rerun_list[i]
                os.system(command)
            except:
                rerun_failed_files.append(rerun_list[i])
    print("rerun failed files: ")
    print(rerun_failed_files)


if __name__ == '__main__':
    # --lf 只运行上次失败的用例
    # --ff 先执行上次失败的用例，再执行上次成功的用例
    # -x 一旦运行到报错就停止运行
    # 例如：    # pytest.main(["--html=./report/video/test_report_video_detail.html", r"./video/test_video_detail.py", "--lf"])

    # 执行local测试用例
    # local 主页面
    # pytest.main(["--html=./report/local/test_report_local.html", r"./local/test_local.py"])
    # anchor 主播媒体列表页面
    # pytest.main(["--html=./report/local/test_report_anchor_media.html", r"./local/test_anchor_media.py"])
    # pytest.main(["./local"])
    # 执行video测试用例
    # pytest.main(["./video"])
    # 执行music测试用例
    # pytest.main(["./music"])
    # 执行takatak测试用例
    # pytest.main(["./takatak"])
    pytest.main(["./test_main.py"])
    # 检查并重新运行失败用例脚本
    rerun()

    # 执行local测试用例
    # # local 主页面，61.07s, 3条
    # pytest.main(["--html=./report/local/test_report_local.html", r"./local/test_local.py"])
    # # anchor 主播媒体列表页面, 18.71s, 2条
    # pytest.main(["--html=./report/local/test_report_anchor_media.html", r"./local/test_anchor_media.py"])
    #
    # # video
    # # video 主页面, 68.52s, 11条
    # pytest.main(["--html=./report/video/test_report_video.html", r"./video/test_video.py"])
    # # video 待看列表, 55.51s, 4条
    # pytest.main(["--html=./report/video/test_report_watch_list.html", r"./video/test_watch_list.py"])
    # # video 视频详情页, 28.63s, 8条
    # pytest.main(["--html=./report/video/test_report_video_detail.html", r"./video/test_video_detail.py"])
    # # video 视频详情页查看更多, 43.32s, 3条
    # pytest.main(["--html=./report/video/test_report_video_detail_more.html", r"./video/test_video_detail_more.py"])
    # # video 搜索页，23.42s，7条
    # pytest.main(["--html=./report/video/test_report_video_search.html", r"./video/test_video_search.py"])
    # # video 搜索结果页, 170.82s, 9条
    # pytest.main(["--html=./report/video/test_report_video_search_result.html", r"./video/test_video_search_result.py"])
    # # video news页面, 14.39s, 2条
    # pytest.main(["--html=./report/video/test_report_video_news.html", r"./video/test_video_news.py"])
    # # video news查看更多, 15.4s, 1条
    # pytest.main(["--html=./report/video/test_report_video_news_more.html", r"./video/test_video_news_more.py"])
    # # video 下载页面, 31.12s, 4条, 后2条需要使用有推荐数据的包测试（pre包或release包）
    # pytest.main(["--html=./report/video/test_report_download.html", r"./video/test_download.py"])
    # # video 通知页面，8.22s, 2条
    # pytest.main(["--html=./report/video/test_report_notice.html", r"./video/test_notice.py"])
    #
    # # video 搜索shows页, 121.56s, 9条
    # pytest.main(["--html=./report/video/test_report_search_shows.html", r"./video/test_search_shows.py"])
    # # video 搜索movies页, 116.91s, 9条
    # pytest.main(["--html=./report/video/test_report_search_movies.html", r"./video/test_search_movies.py"])
    # # video 搜索music页, 108.87s, 8条
    # pytest.main(["--html=./report/video/test_report_search_music.html", r"./video/test_search_music.py"])
    # # video 搜索live TV页, 49.01s, 5条
    # pytest.main(["--html=./report/video/test_report_search_live_tv.html", r"./video/test_search_live_tv.py"])
    # # video 搜索shorts页, 62.43s, 6条
    # pytest.main(["--html=./report/video/test_report_search_shorts.html", r"./video/test_search_shorts.py"])
    #
    # # music
    # # music 首页, 94.29s, 5条
    # pytest.main(["--html=./report/music/test_report_music.html", r"./music/test_music.py"])
    # # music 搜索页面, 118.54s, 10条
    # pytest.main(["--html=./report/music/test_report_music_search.html", r"./music/test_music_search.py"])
    # # music 音频播放页面, 133.39s, 18条
    # pytest.main(["--html=./report/music/test_report_music_play.html", r"./music/test_music_play.py"])
    # # music 我的最爱页面, 46.4s, 7条
    # pytest.main(["--html=./report/music/test_report_my_favorite.html", r"./music/test_my_favorites.py"])
    # # music 我的歌单页面, 91s, 5条
    # pytest.main(["--html=./report/music/test_report_my_playlist.html", r"./music/test_my_playlist.py"])
    # # music 歌单详情页面, 71.27s, 5条
    # pytest.main(["--html=./report/music/test_report_playlist_detail.html", r"./music/test_playlist_detail.py"])
    # # music 本地音乐页面, 289s, 26条
    # pytest.main(["--html=./report/music/test_report_local_music.html", r"./music/test_local_music.py"])
    #
    # # takatak
    # # takatak 首页, 20.04s. 2条
    # pytest.main(["--html=./report/takatak/test_report_takatak.html", r"./takatak/test_takatak.py"])

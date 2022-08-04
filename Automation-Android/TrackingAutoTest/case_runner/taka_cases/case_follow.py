import sys


def case_follow_clicked_trending(device, standard_log):
    # 应包括一次followClicked
    device.set_up()
    while not device.resource_is_exist('com.next.innovation.takatak:id/iv_follow'):
        device.swipe_up()
    device.click_by_id('com.next.innovation.takatak:id/iv_follow')
    device.tear_down(sys._getframe().f_code.co_name)
    case = {
        # case_like
        "case_follow_clicked_trending": {
            "followClicked": {
                "count": 1,
                "source": "Trending",
                "publisherID": "",
                "suggestType": "None"
            }
        }
    }
    standard_log.update(case)


def case_follow_clicked_my_liked(device, standard_log):
    # 应包括一次followClicked
    device.set_up()
    device.click_by_id('com.next.innovation.takatak:id/detail_like')
    device.click_by_id('com.next.innovation.takatak:id/ivMe')
    # 切换到like列表
    device.click_by_xpath(
        '//*[@resource-id="com.next.innovation.takatak:id/title_container"]/android.widget.FrameLayout[2]')
    # 点击列表第一个
    device.click_by_xpath(
        '//*[@resource-id="com.next.innovation.takatak:id/recycler_view"]/android.widget.FrameLayout[1]')
    # 判断是否已follow
    if device.resource_is_exist('com.next.innovation.takatak:id/iv_follow'):
        device.click_by_id('com.next.innovation.takatak:id/iv_follow')
    else:
        device.click_by_id('com.next.innovation.takatak:id/detail_owner')
        device.click_by_id('com.next.innovation.takatak:id/follow_button')
        device.press_back()
        device.click_by_id('com.next.innovation.takatak:id/iv_follow')
    device.tear_down(sys._getframe().f_code.co_name)
    case = {
        "case_follow_clicked_my_liked": {
            "followClicked": {
                "count": 1,
                "source": "mylike",
                "publisherID": "",
                "suggestType": "None"
            }
        }
    }
    standard_log.update(case)


def case_follow_clicked_publisher_page(device, standard_log):
    # 应包括一次followClicked，一次unfollowClicked
    device.set_up()
    device.click_by_id('com.next.innovation.takatak:id/detail_owner')
    device.click_by_id('com.next.innovation.takatak:id/follow_button')
    device.click_by_id('com.next.innovation.takatak:id/follow_button')
    device.tear_down(sys._getframe().f_code.co_name)
    case = {
        "case_follow_clicked_publisher_page": {
            "followClicked": {
                "count": 1,
                "source": "publisherPage",
                "publisherID": "",
                "suggestType": "None"
            },
            "unfollowClicked": {
                "count": 1,
                "source": "publisherPage",
                "publisherID": "",
                "suggestType": "None"
            }
        }
    }
    standard_log.update(case)


def case_follow_clicked_my_follow_page(device, standard_log):
    device.set_up()
    device.click_by_id('com.next.innovation.takatak:id/ivMe')
    device.click_by_id('com.next.innovation.takatak:id/following_text')
    device.click_by_id('com.next.innovation.takatak:id/follow_button')
    device.click_by_id('com.next.innovation.takatak:id/follow_button')
    device.tear_down(sys._getframe().f_code.co_name)
    case = {
        "case_follow_clicked_my_follow_page": {
            "followClicked": {
                "count": 1,
                "source": "myFollowPage",
                "publisherID": "",
                "suggestType": "None"
            },
            "unfollowClicked": {
                "count": 1,
                "source": "myFollowPage",
                "publisherID": "",
                "suggestType": "None"
            }
        }}
    standard_log.update(case)

# def case_follow_clicked_friend_suggestion(device, standard_log):
#     # 应包括一次followClicked，一次unfollowClicked
#     device.set_up()
#     device.click_by_id('com.next.innovation.takatak:id/detail_owner')
#     # 点击publisher列表里的第一个视频
#     device.click_by_id('com.next.innovation.takatak:id/iv_plus')
#     device.tear_down(sys._getframe().f_code.co_name)
#     case = {
#         # case_like
#         "case_like_click_trending": {
#             "likeClicked": {
#                 "count": 1,
#                 "source": "Trending",
#                 "length": ""
#             },
#             "likeSucceed": {
#                 "count": 1,
#                 "source": "Trending",
#                 "length": ""
#             },
#             "likeCanceled": {
#                 "count": 1,
#                 "source": "Trending",
#                 "length": "",
#                 "reason": 'action'
#             }
#         }}
#     standard_log.update(case)
#
#
# def case_follow_clicked_contact_suggestion(device, standard_log):
#     # 应包括一次followClicked，一次unfollowClicked
#     device.set_up()
#     device.click_by_id('com.next.innovation.takatak:id/detail_owner')
#     # 点击publisher列表里的第一个视频
#     device.click_by_id('com.next.innovation.takatak:id/iv_plus')
#     device.tear_down(sys._getframe().f_code.co_name)
# case = {
#         # case_like
#         "case_like_click_trending": {
#             "likeClicked": {
#                 "count": 1,
#                 "source": "Trending",
#                 "length": ""
#             },
#             "likeSucceed": {
#                 "count": 1,
#                 "source": "Trending",
#                 "length": ""
#             },
#             "likeCanceled": {
#                 "count": 1,
#                 "source": "Trending",
#                 "length": "",
#                 "reason": 'action'
#             }
#         }}
#     standard_log.update(case)
#
#
# def case_follow_clicked_friends_popup(device, standard_log):
#     # 应包括一次followClicked，一次unfollowClicked
#     device.set_up()
#     device.click_by_id('com.next.innovation.takatak:id/detail_owner')
#     # 点击publisher列表里的第一个视频
#     device.click_by_id('com.next.innovation.takatak:id/iv_plus')
#     device.tear_down(sys._getframe().f_code.co_name)
# case = {
#         # case_like
#         "case_like_click_trending": {
#             "likeClicked": {
#                 "count": 1,
#                 "source": "Trending",
#                 "length": ""
#             },
#             "likeSucceed": {
#                 "count": 1,
#                 "source": "Trending",
#                 "length": ""
#             },
#             "likeCanceled": {
#                 "count": 1,
#                 "source": "Trending",
#                 "length": "",
#                 "reason": 'action'
#             }
#         }}
#     standard_log.update(case)
#
#
# def case_follow_clicked_friend_follow_sug(device, standard_log):
#     # 应包括一次followClicked，一次unfollowClicked
#     device.set_up()
#     device.click_by_id('com.next.innovation.takatak:id/detail_owner')
#     # 点击publisher列表里的第一个视频
#     device.click_by_id('com.next.innovation.takatak:id/iv_plus')
#     device.tear_down(sys._getframe().f_code.co_name)
# case = {
#         # case_like
#         "case_like_click_trending": {
#             "likeClicked": {
#                 "count": 1,
#                 "source": "Trending",
#                 "length": ""
#             },
#             "likeSucceed": {
#                 "count": 1,
#                 "source": "Trending",
#                 "length": ""
#             },
#             "likeCanceled": {
#                 "count": 1,
#                 "source": "Trending",
#                 "length": "",
#                 "reason": 'action'
#             }
#         }}
#     standard_log.update(case)

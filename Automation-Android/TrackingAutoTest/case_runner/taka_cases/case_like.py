import sys


def case_like_click_trending(device, standard_log):
    # 应包括一次likeClicked，一次likeSucceed,一次likeCanceled
    device.set_up()
    device.click_by_id('com.next.innovation.takatak:id/detail_like')
    device.click_by_id('com.next.innovation.takatak:id/detail_like')
    device.tear_down(sys._getframe().f_code.co_name)
    case = {
        # case_like
        "case_like_click_trending": {
            "likeClicked": {
                "count": 1,
                "source": "Trending",
                "length": ""
            },
            "likeSucceed": {
                "count": 1,
                "source": "Trending",
                "length": ""
            },
            "likeCanceled": {
                "count": 1,
                "source": "Trending",
                "length": "",
                "reason": 'action'
            }
        }}
    standard_log.update(case)


def case_like_click_following(device, standard_log):
    # 应包括一次likeClicked，一次likeSucceed,一次likeCanceled
    device.set_up()
    # 切换到following页签
    device.click_by_text('Follow')
    device.click_by_id('com.next.innovation.takatak:id/detail_like', 60)
    device.click_by_id('com.next.innovation.takatak:id/detail_like')
    device.tear_down(sys._getframe().f_code.co_name)
    case = {
        "case_like_click_following": {
            "likeClicked": {
                "count": 1,
                "source": "Following",
                "length": ""
            },
            "likeSucceed": {
                "count": 1,
                "source": "Following",
                "length": ""
            },
            "likeCanceled": {
                "count": 1,
                "source": "Following",
                "length": "",
                "reason": 'action'
            }
        }}
    standard_log.update(case)

import sys


def case_switch_to_online(device):
    device.set_up()
    device.click_by_id('com.next.innovation.takatak:id/ivMe')
    device.click_by_id('com.next.innovation.takatak:id/iv_settings')
    device.click_by_id('com.next.innovation.takatak:id/settings_tv')
    device.swipe_up()
    device.click_by_id('com.next.innovation.takatak:id/about_tv')
    device.long_click_by_id('com.next.innovation.takatak:id/version_tv', 1)
    device.click_by_id('com.next.innovation.takatak:id/server_label')
    device.click_by_text('Online')
    device.close_app()


def case_item_clicked(device, standard_log):
    # 应包括一次publisherClicked，一次itemListViewed，一次itemClicked
    device.set_up()
    device.click_by_id('com.next.innovation.takatak:id/detail_owner')
    # 点击publisher列表里的第一个视频
    device.click_by_xpath('//*[@resource-id="com.next.innovation.takatak:id/recycler_view"]/android.widget'
                          '.FrameLayout[1]')
    device.tear_down(sys._getframe().f_code.co_name)
    case = {
        "case_item_clicked": {
            "publisherClicked": {
                "count": 1,
                "source": "home",
                "publisherID": "",
                "itemID": ""
            },
            "itemListViewed": {
                "count": 1,
                "source": "publisherVideoList",
            },
            "itemClicked": {
                "count": 1,
                "source": "publisherVideoList"
            }
        }}
    standard_log.update(case)


def case_item_share_whatsapp(device, standard_log):
    # 应包括一次itemShared
    device.set_up()
    # 点击share按钮
    device.click_by_id('com.next.innovation.takatak:id/detail_share')
    device.click_by_text('WhatsApp')
    device.listening_toast('Please finish register first.|请先完成注册')
    device.tear_down(sys._getframe().f_code.co_name)
    case = {
        "case_item_share_whatsapp": {
            "itemShared": {
                "count": 1,
                "itemType": "Video",
                "shareType": "WhatsApp",
            }
        }}
    standard_log.update(case)


def case_item_share_facebook(device, standard_log):
    # 应包括一次itemShared
    device.set_up()
    # 点击share按钮
    device.click_by_id('com.next.innovation.takatak:id/detail_share')
    device.click_by_text('Facebook')
    device.listening_toast('')
    device.tear_down(sys._getframe().f_code.co_name)
    case = {
        "case_item_share_facebook": {
            "itemShared": {
                "count": 1,
                "itemType": "Video",
                "shareType": "Facebook",
            }
        }}
    standard_log.update(case)


def case_item_share_messenger(device, standard_log):
    # 应包括一次itemShared
    device.set_up()
    # 点击share按钮
    device.click_by_id('com.next.innovation.takatak:id/detail_share')
    device.click_by_text('Messenger')
    device.listening_toast('')
    device.tear_down(sys._getframe().f_code.co_name)
    case = {
        "case_item_share_messenger": {
            "itemShared": {
                "count": 1,
                "itemType": "Video",
                "shareType": "Messenger",
            }
        }}
    standard_log.update(case)


def case_item_share_message(device, standard_log):
    # 应包括一次itemShared
    device.set_up()
    # 点击share按钮
    device.click_by_id('com.next.innovation.takatak:id/detail_share')
    device.click_by_xpath('//*[@resource-id="com.next.innovation.takatak:id/recycler_view_primary"]/android.view'
                          '.ViewGroup[5]/android.widget.ImageView[1]')
    while not (device.text_is_exist('Messages') or device.text_is_exist('信息') or device.text_is_exist('短信')):
        device.swipe_up()
    if device.text_is_exist('Messages'):
        device.click_by_text('Messages')
    elif device.text_is_exist('短信'):
        device.click_by_text('短信')
    else:
        device.click_by_text('信息')
    device.tear_down(sys._getframe().f_code.co_name)
    case = {
        "case_item_share_message": {
            "itemShared": {
                "count": 1,
                "itemType": "Video",
                "shareType": "More",
            }
        }}
    standard_log.update(case)


def case_item_download_trending(device, standard_log):
    # 应包括一次itemDownload
    device.set_up()
    # 点击share按钮
    device.click_by_id('com.next.innovation.takatak:id/detail_share')
    device.click_by_text('Save')
    device.listening_toast('Vedio saved to My Downloads.')
    device.tear_down(sys._getframe().f_code.co_name)
    case = {
        "case_item_download_trending": {
            "itemDownload": {
                "count": 1,
                "source": "Trending",
                "length": "",
                "isShared": "0"
            }
        }}
    standard_log.update(case)


def case_item_download_following(device, standard_log):
    # 应包括一次itemDownload
    device.set_up()
    # 切换到following页签
    device.click_by_text('Follow')
    # 点击share按钮
    device.click_by_id('com.next.innovation.takatak:id/detail_share', 60)
    device.click_by_text('Save')
    device.listening_toast('Vedio saved to My Downloads.')
    device.tear_down(sys._getframe().f_code.co_name)
    case = {
        "case_item_download_following": {
            "itemDownload": {
                "count": 1,
                "source": "Following",
                "length": "",
                "isShared": "0"
            }
        }}
    standard_log.update(case)


def case_detail_page_item_viewed(device, standard_log):
    device.set_up()
    device.swipe_up()
    device.tear_down(sys._getframe().f_code.co_name)
    case = {
        "case_detail_page_item_viewed": {
            "detailPageItemViewed": {
                "count": 1,
                "length": "",
                "previousID": "None"
            }
        }}
    standard_log.update(case)


def case_item_comment_trending(device, standard_log):
    device.set_up()
    device.click_by_id('com.next.innovation.takatak:id/detail_comment')
    device.send_keys('com.next.innovation.takatak:id/fake_message_edt', 'nice')
    device.click_by_id('com.next.innovation.takatak:id/send_btn')
    # device.click_by_xpath(
    #     '//*[@resource-id="com.next.innovation.takatak:id/commentInputLayout"]/android.widget.LinearLayout['
    #     '1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]')
    device.tear_down(sys._getframe().f_code.co_name)
    case = {
        "case_item_comment_trending": {
            "itemComment": {
                "count": 1,
                "source": "Trending",
                "itemID": "",
                "publisherID": ""
            },
            "commentSent": {
                "count": 1,
                "source": "Trending",
                "itemID": "",
                "publisherID": ""
            }
        }}
    standard_log.update(case)


def case_item_comment_following(device, standard_log):
    device.set_up()
    # 切换到following页签，并判断是否有followed
    device.click_by_text('Follow')
    device.click_by_id('com.next.innovation.takatak:id/detail_comment', 60)
    device.send_keys('com.next.innovation.takatak:id/fake_message_edt', 'nice')
    device.click_by_id('com.next.innovation.takatak:id/send_btn')
    device.tear_down(sys._getframe().f_code.co_name)
    case = {
        "case_item_comment_following": {
            "itemComment": {
                "count": 1,
                "source": "Following",
                "itemID": "",
                "publisherID": ""
            },
            "commentSent": {
                "count": 1,
                "source": "Following",
                "itemID": "",
                "publisherID": ""
            }
        }}
    standard_log.update(case)
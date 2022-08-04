import sys


def case_search_result_show(device, standard_log):
    device.set_up()
    device.click_by_id('com.next.innovation.takatak:id/ivDiscover')
    device.send_keys('com.next.innovation.takatak:id/tv_search', 'a')
    device.send_action('search')
    device.click_by_xpath('//*[@resource-id="com.next.innovation.takatak:id/recycler_view"]/android.view.ViewGroup[2]/android.widget.ImageView[1]')
    device.tear_down(sys._getframe().f_code.co_name)
    case = {
        "case_search_result_show": {
            "searchResultShow": {
                "count": 1,
                "column": "all"
            },
            "searchResultClicked": {
                "count": 1,
                "itemID": "",
                "queryId": ""
            }
        }
    }
    standard_log.update(case)
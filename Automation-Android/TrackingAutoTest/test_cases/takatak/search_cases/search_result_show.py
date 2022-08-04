from test_cases.base_case import BaseCase


class SearchResultShow(BaseCase):

    def __init__(self, device, run_time):
        self.title = "search_result_show"
        super().__init__(self.title, device, run_time)
        self.check_points = {
            # 应包括一次searchResultShow, 一次searchResultClicked
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

    def run_steps(self):
        self.device.click_by_id('com.next.innovation.takatak:id/ivDiscover')
        self.device.send_keys('com.next.innovation.takatak:id/tv_search', 'a')
        self.device.send_action('search')
        self.device.click_by_xpath('//*[@resource-id="com.next.innovation.takatak:id/recycler_view"]/android.view.ViewGroup[2]/android.widget.ImageView[1]')




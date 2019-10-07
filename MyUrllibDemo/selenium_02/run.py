# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as Expect


class FlightSpider(object):
    def __init__(self, url):
        self.url = url

    def crawl(self):
        try:
            browser = webdriver.Chrome(executable_path=r'E:/Python/webdriver/chromedriver.exe')
            browser.get(self.url)

            # Wait(browser, 60).until(
            #     Expect.presence_of_element_located((By.CLASS_NAME, 'J_CatalogRegular'))
            # )

            # html = browser.page_source
            # print(html)

            # fly_tab = browser.find_element_by_link_text('机票')
            # fly_tab.click()

            # J_SearchFlight = browser.find_element_by_class_name('J_SearchFlight')
            # J_InternalFlight = J_SearchFlight.find_element_by_class_name('J_InternalFlight')
            # J_SearchSwitchRadio =  J_InternalFlight.find_element_by_css_selector('.J_SearchSwitchRadio')
            # opts = J_SearchSwitchRadio.find_element_by_xpath('.//ul/li')
            # opts[0].click()
            #
            # J_SearchSingle = J_InternalFlight.find_element_by_class_name('J_SearchSingle')
            # search_flight_ins = J_SearchFlight.find_elements_by_class_name('search_flight_in')
            # search_flight_ins[1].send_keys('青岛')
            # search_submit_btn = J_SearchFlight.find_element_by_class_name('search_submit_btn')
            # search_submit_btn.click()
        except:
            print('error')


if __name__ == "__main__":
    # uri = 'http://www.tuniu.com'
    # uri = 'https://www.baidu.com'
    uri = 'http://flight.tuniu.com/domestic/list/SZX_TAO_ST_1_0_0/?start=2019-07-18'
    flight = FlightSpider(uri)
    flight.crawl()



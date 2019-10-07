# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as Expect

try:
    browser = webdriver.Chrome(executable_path=r'E:/Python/webdriver/chromedriver.exe')
    browser.get('https://www.baidu.com')

    # 1. send keys with return
    kw = browser.find_element_by_id('kw')
    kw.send_keys("Selenium", Keys.RETURN)

    Wait(browser, 10).until(
        # Expect.presence_of_all_elements_located((By.ID 'kw'))
        Expect.presence_of_element_located((By.ID, '1'))
        # Expect.text_to_be_present_in_element((By.ID, 'loadingStatus'), u'共搜索')
    )

    # 2. send keys then click submit button
    # kw = browser.find_element_by_id('kw')
    # search_btn = browser.find_element_by_id('su')
    # kw.send_keys('python')
    # search_btn.click()

    # 3. send keys then submit form
    # kw = browser.find_element_by_id('kw')
    # kw.send_keys('英雄')
    # kw.submit()

    # 4. execute javascript
    # browser.execute_script('''
    # var kw = document.getElementById('kw');
    # var su = document.getElementById('su');
    # kw.value = '机器学习';
    # su.click();
    # ''')

    # Selenium
    # 单独提供了一个类
    # selenium.webdriver.support.select.Select
    # 可以方便元素的选取

    # 当点击搜索按钮之后我们要爬取页面上搜索出来的结果
    # 1.parse page_source
    html = browser.page_source
    # results = parser_html(html)
    print(html)

    # 2.find & parse elements
    # results = browser.find_elements_by_class_name("c-container ")
    # print(results)
    # for result in results:
    #     link = result.find_element_by_xpath('.//h3/a')
    #     print(link.text)

    # 因为 browser.get() 方法并不会等待页面完全加载完毕，而是等到浏览器的 onload 方法执行完就返回了

    # 3.intercept & parse ajax
    # 通过 Ajax 请求动态加载，某些数据在 Ajax 请求的响应中有，但在页面上并没有体现




    # browser.quit()
except InvalidArgumentException as e:
    print(e)

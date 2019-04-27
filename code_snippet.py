# !-*- coding: utf-8 -*-
# @Author  : ching(flackmaster@163.com)
# @Date    : 2019/04/26
# @Link    : http://www.cnblogs.com/ching126/
# @Version : $
# @Desc    :


class SeleniumCodeSnippet:
    def hello(self):
        from selenium import webdriver

        driver = webdriver.Firefox()
        driver.get('http://www.baidu.com')
        driver.page_source()
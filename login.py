# !-*- coding: utf-8 -*-
# @Author  : ching(flackmaster@163.com)
# @Date    : 2019/04/26
# @Link    : http://www.cnblogs.com/ching126/
# @Version : $
# @Desc    :
import scrapy


class LoginSpider(scrapy.Spider):
    name = 'baidu.com'
    start_urls = ['http://www.baidu.com/users/login.php']


    def parse(self, response):
        return scrapy.FormRequest.from_response(response, formdata={'username': 'john', 'password': 'secret'}, callback=self.after_login)

    def after_login(self, response):
        if "authentication failed" in response.body:
            self.logger.error("Login failed")
            return

        # continue scraping with authenticated session...



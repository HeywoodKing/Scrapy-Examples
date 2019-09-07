# -*- coding: utf-8 -*-
import scrapy
import random
from BaiduStocks.items import BaidustocksItem


class StocksSpider(scrapy.Spider):
    name = 'stocks'
    # allowed_domains = ['baidu.com']
    start_urls = ['hhttp://quote.eastmoney.com/center/gridlist.html#hs_a_board']

    def parse(self, response):
        for i in range(1, len(int(response.css('//div#main-table_paginate > span > a:nth-child(5)/text()').extract()[0])) + 1):
            try:
                url = 'http://{0}.push2.eastmoney.com/api/qt/clist/get?' \
                      'cb=jQuery112406139267027871709_1563270253764&pn={1}&pz={2}&po=1&np=1&' \
                      'ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&' \
                      'fs=m:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,' \
                      'f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152' \
                      '&_={3}'.format(random.randint(1, 101), i, 20, '1563270253819')
                yield scrapy.Request(url, callback=self.parse_stock)
            except:
                continue

    def parse_stock(self, response):
        print(response)
        item = BaidustocksItem()
        yield item



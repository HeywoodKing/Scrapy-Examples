# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyscrapytmallItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    goods_name = scrapy.Field()
    goods_price = scrapy.Field()
    goods_url = scrapy.Field()
    shop_name = scrapy.Field()
    shop_url = scrapy.Field()
    company_name = scrapy.Field()
    company_addr = scrapy.Field()

    file_urls = scrapy.Field()

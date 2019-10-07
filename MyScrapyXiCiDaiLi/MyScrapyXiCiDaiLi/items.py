# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyscrapyxicidailiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    country = scrapy.Field()
    country_img = scrapy.Field()
    ip = scrapy.Field()
    port = scrapy.Field()
    server_addr = scrapy.Field()
    is_anonymous = scrapy.Field()
    proxy_type = scrapy.Field()
    speed = scrapy.Field()
    connect_time = scrapy.Field()
    keep_alive_time = scrapy.Field()
    verify_time = scrapy.Field()

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyscrapydoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 电影名
    title = scrapy.Field()
    # 基本信息
    bd = scrapy.Field()
    # 评分
    star = scrapy.Field()
    # 简介
    quote = scrapy.Field()



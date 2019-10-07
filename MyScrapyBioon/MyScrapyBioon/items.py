# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyscrapybioonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    sub_url = scrapy.Field()
    img = scrapy.Field()
    brief = scrapy.Field()
    source = scrapy.Field()
    publish_date = scrapy.Field()
    body = scrapy.Field()

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ChoutiItem(scrapy.Item):
    # define the fields for your item here like:
    img = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    label = scrapy.Field()
    link_from = scrapy.Field()
    link_desc = scrapy.Field()
    author_img = scrapy.Field()
    author_name = scrapy.Field()
    publish_time = scrapy.Field()
    views = scrapy.Field()



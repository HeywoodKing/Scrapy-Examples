# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BaidustocksPipeline(object):
    def process_item(self, item, spider):
        return item


class BaidustocksInfoPipeline(object):
    def open_spider(self):
        pass

    def close_spider(self):
        pass

    def process_item(self, item, spider):
        return item


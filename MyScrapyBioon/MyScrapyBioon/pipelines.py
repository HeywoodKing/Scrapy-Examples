# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import json
import codecs


class MyscrapybioonPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonWritePipeline(object):
    def __init__(self):
        self.titles_seen = set()
        self.file = codecs.open("bioon.json", "w", encoding='utf-8')

    def process_item(self, item, spider):
        if item['title'] in self.titles_seen:
            raise DropItem("Info exists %s" % item)
        else:
            self.titles_seen.add(item['title'])
            item_dict = dict(item)
            # length = str(len(item_dict))
            line = json.dumps(item_dict, ensure_ascii=False) + ",\n"

            # json_dict = {"rows": length, "data": []}
            # json_dict['data'].append(line.rstrip(','))
            # json_str = json.dumps(json_dict, ensure_ascii=False)

            # json lines行数据
            self.file.write(line)
            return item

    def spider_closed(self, spider):
        self.file.close()

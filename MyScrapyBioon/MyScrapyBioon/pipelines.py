# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import json
import codecs
from scrapy.log import logger
import scrapy
from scrapy.mail import MailSender


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

    # 重写了spider_closed方法，
    # 添加发送邮件功能，当spider关闭时，邮件通知领导，并在邮件正文中添加spider的状态信息
    # 读取crawler的状态信息，并添加到邮件正文中
    def spider_closed(self, spider):
        self.file.close()
        # print("结束啦！")
        # logger.info("结束啦！")

        # mailer = MailSender()
        # # mailer = MailSender.from_settings(settings)
        # mailer.send(to=["opencoding@hotmail.com"], subject="Some Subject", body="Some body", cc=["another@hotmail.com"])

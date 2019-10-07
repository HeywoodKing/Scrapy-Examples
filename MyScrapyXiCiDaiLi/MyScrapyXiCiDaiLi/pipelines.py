# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings


class MongodbPipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']
        sheetname = settings['MONGODB_SHEETNAME']

        # 创建MONGODB数据库连接
        client = pymongo.MongoClient(host=host, port=port)
        # 指定数据库
        mydb = client[dbname]
        # 指定存放数据的数据库表名
        self.post = mydb[sheetname]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item


# class MysqlPipeline(object):
#     def process_item(self, item, spider):
#         DBKWARGS = spider.settings.get('DBKWARGS')
#         conn = MySQLdb.connect(**DBKWARGS)
#         cur = conn.cursor()
#         sql = ("insert into proxy(COUNTRY, COUNTRY_IMG, IP, PROT, proxy_type, SERVER_ADDR, SPEED, is_anonymous, connect_time, keep_alive_time, verify_time) "
#                "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
#         lis = (item['country'], item['country_img'], item['ip'], item['port'], item['proxy_type'], item['server_addr'], item['speed'],
#                item['is_anonymous'], item['connect_time'], item['keep_alive_time'], item['verify_time'])
#         try:
#             cur.execute(sql, lis)
#         except Exception as e:
#             print("Insert error:", e)
#             conn.rollback()
#         else:
#             conn.commit()
#
#         cur.close()
#         conn.close()
#         return item

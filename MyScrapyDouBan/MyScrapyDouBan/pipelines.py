# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings

class MyscrapydoubanPipeline(object):
    def __init__(self):
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        sheetname = settings["MONGODB_SHEETNAME"]

        # 创建MONGODB数据库连接
        client = pymongo.MongoClient(host=host, port=port)
        # 指定数据库
        mydb = client[dbname]
        # 存放数据的数据库表名
        self.post = mydb[sheetname]

    def process_item(self, item, spider):
        # 把item转化成字典形式
        data = dict(item)
        # 向指定的表里添加数据 向数据库插入一条记录
        self.post.insert(data)
        # 会在控制台输出原item数据，可以选择不写
        return item

        # result = requests.get(item['img_url'])
        # with open("E:\\img\\jiandan\\" + str(self.count) + ".jpg", 'wb') as f:
        #     f.write(result.content)
        #     f.close()
        # self.count += 1
        # return item

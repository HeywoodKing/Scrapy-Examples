# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class ChoutiFilePipeline(object):
    def __init__(self, file_path):
        self.f = None
        self.file_path = file_path

    @classmethod
    def from_crawler(cls, crawler):
        """
        执行pipeline类时，会先去类中找from_crawler的方法，
        如果有，则先执行此方法，并且返回一个当前类的对象，
        如果没有，则直接执行初始化方法
        :param crawler:
        :return:
        """
        # 可以进行一些初始化之前的处理，比如：文件的路径配置到settings文件中，方便后期的更改。
        file_path = crawler.settings.get('CHOUTI_FILE_PATH')
        return cls(file_path)

    def open_spider(self, spider):
        """
        爬虫开始时被调用
        :param spider:
        :return:
        """
        self.f = open(self.file_path, 'w', encoding='utf8')

    def process_item(self, item, spider):
        """
        执行持久化的逻辑操作
        :param item: 爬虫yield过来的item对象  (一个字典)
        :param spider: 爬虫对象
        :return:
        """
        try:
            img = item['img']
            title = item['title']
            url = item['url']
            label = item['label']
            link_from = item['link_from']
            link_desc = item['link_desc']
            author_img = item['author_img']
            author_name = item['author_name']
            publish_time = item['publish_time']
            views = item['views']
            content = 'img:{}\ntitle:{}\nurl:{}\nlabel:{}\nlink_from:{}\nlink_desc:{}\nauthor_img:{}\nauthor_name:{}\npublish_time:{}\nviews:{}\n'\
                .format(img, title, url, label, link_from, link_desc, author_img, author_name, publish_time, views)
            self.f.write(content)
            self.f.write('*' * 30)
            self.f.flush()  # 将写入到内存的文件强刷到文件中，防止夯住，不使用此方法会夯住
        except Exception as ex:
            print(ex)
            raise DropItem(ex)
        return item

    def close_spider(self, spider):
        """
        爬虫结束时调用
        :param spider:
        :return:
        """
        self.f.close()

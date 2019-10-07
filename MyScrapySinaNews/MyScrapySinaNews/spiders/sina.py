# -*- coding: utf-8 -*-
import scrapy
# import sys
from MyScrapySinaNews.items import MyscrapysinanewsItem
import os


class SinaSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        items = []
        # 所有大类的url 和 标题
        parent_urls = response.xpath('//div[@id="tab01"]/div/h3/a/@href').extract()
        parent_title = response.xpath('//div[@id="tab01"]/div/h3/a/text()').extract()

        # 所有小类的ur 和 标题
        sub_urls = response.xpath('//div[@id="tab01"]/div/ul/li/a/@href').extract()
        sub_title = response.xpath('//div[@id="tab01"]/div/ul/li/a/text()').extract()

        # 爬取所有大类
        for i in range(len(parent_title)):
            # 指定大类目录的路径和目录名
            parent_filename = "./Data/" + parent_title[i]

            # 如果目录不存在，则创建目录
            if not os.path.exists(parent_filename):
                os.makedirs(parent_filename)

            # 爬取所有小类
            for j in range(len(sub_urls)):
                item = MyscrapysinanewsItem()
                # 保存大类的title和urls
                item['parent_title'] = parent_title[i]
                item['parent_urls'] = parent_urls[i]

                # 检查小类的url是否以同类别大类url开头，如果是返回True (sports.sina.com.cn 和 sports.sina.com.cn/nba)
                if_belong = sub_urls[j].startswith(item['parent_urls'])

                # 如果属于本大类，将存储目录放在本大类目录下
                if if_belong:
                    sub_filename = parent_filename + '/' + sub_title[j]
                    # 如果目录不存在，则创建目录
                    if not os.path.exists(sub_filename):
                        os.makedirs(sub_filename)

                    # 存储 小类url、title和filename字段数据
                    item['sub_urls'] = sub_urls[j]
                    item['sub_title'] = sub_title[j]
                    item['sub_filename'] = sub_filename

                    items.append(item)


        # 发送每个小类url的Request请求，得到Response连同包含meta数据 一同交给回调函数 second_parse 方法处理
        for item in items:
            yield scrapy.Request(url = item['sub_urls'], meta={'meta_1': item}, callback=self.second_parse)

    # 对于返回的小类的url，再进行递归请求
    def second_parse(self, response):
        # 提取每次Response的meta数据
        meta_1 = response.meta['meta_1']

        # 取出小类里所有子链接
        son_urls = response.xpath('//a/@href').extract()

        items = []
        for i in range(0, len(son_urls)):
            # 检查每个链接是否以大类url开头、以.shtml结尾，如果是返回True
            if_belong = son_urls[i].endswith('.shtml') and son_urls[i].startswith(meta_1['parent_urls'])

            # 如果属于本大类，获取字段值放在同一个item下便于传输
            if (if_belong):
                item = MyscrapysinanewsItem()
                item['parent_title'] = meta_1['parent_title']
                item['parent_urls'] = meta_1['parent_urls']
                item['sub_title'] = meta_1['sub_title']
                item['sub_urls'] = meta_1['sub_urls']
                item['sub_filename'] = meta_1['sub_filename']
                item['son_urls'] = son_urls[i]
                items.append(item)

        # 发送每个小类下子链接url的Request请求，得到Response后连同包含meta数据 一同交给回调函数 detail_parse 方法处理
        for item in items:
            yield scrapy.Request(url=item['son_urls'], meta={'meta_2': item}, callback=self.detail_parse)


    # 数据解析方法，获取文章标题和内容
    def detail_parse(self, response):
        item = response.meta['meta_2']
        content = ""
        title = response.xpath('//h1[@id="main_title"]/text()')
        content_list = response.xpath('//div[@id="artibody"]/p/text()').extract()

        # 将p标签里的文本内容合并到一起
        for content_one in content_list:
            content += content_one

        item['title'] = title
        item['content'] = content

        yield item
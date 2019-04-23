# -*- coding: utf-8 -*-
import scrapy
# 导入链接规则匹配类，用来提取符合规则的连接
from scrapy.linkextractors import LinkExtractor
# 导入CrawlSpider类和Rule
from scrapy.spiders import CrawlSpider, Rule
from MyScrapyTencentSpider.items import MyscrapytencentItem


class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0#a']

    # Response里链接的提取规则，返回的符合匹配规则的链接匹配对象的列表
    pagelink = LinkExtractor(allow=("start=\d+"))

    rules = [
        # 获取这个列表里的链接，依次发送请求，并且继续跟进，调用指定回调函数处理
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        Rule(pagelink, callback="parse_item", follow=True)
    ]

    def parse_item(self, response):
        item = MyscrapytencentItem()
        datas = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        for each in datas:
            #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
            #item['name'] = response.xpath('//div[@id="name"]').get()
            #item['description'] = response.xpath('//div[@id="description"]').get()


            # 职位名称
            item['position_name'] = each.xpath("./td[1]/a/text()").extract()[0]
            # 详情连接
            item['position_link'] = each.xpath("./td[1]/a/@href").extract()[0]
            # 职位类别
            if each.xpath("./td[2]/text()").extract():
                item['position_type'] = each.xpath("./td[2]/text()").extract()[0]
            # 招聘人数
            item['people_num'] = each.xpath("./td[3]/text()").extract()[0]
            # 工作地点
            item['work_location'] = each.xpath("./td[4]/text()").extract()[0]
            # 发布时间
            item['publish_time'] = each.xpath("./td[5]/text()").extract()[0]

        yield item

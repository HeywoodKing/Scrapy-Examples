# -*- coding: utf-8 -*-
import scrapy
from MyScrapyTencent.items import MyscrapytencentItem


class TencentpositionSpider(scrapy.Spider):
    """
    功能：爬取腾讯社招信息
    """
    # 爬虫名
    name = 'TencentPosition'
    # 爬虫作用范围
    allowed_domains = ['tencent.com']

    url = "http://hr.tencent.com/position.php?&start="
    offset = 0
    # 起始url
    start_urls = [url + str(offset)]

    def parse(self, response):
        datas = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        for each in datas:
            # 初始化模型对象
            item = MyscrapytencentItem()
            # 职位名称
            item["position_name"] = each.xpath("./td[1]/a/text()").extract()[0]
            # 详情连接
            item["position_link"] = each.xpath("./td[1]/a/@href").extract()[0]
            # 职位类别
            if each.xpath("./td[2]/text()").extract():
                item["position_type"] = each.xpath("./td[2]/text()").extract()[0]
            # 招聘人数
            item['people_num'] = each.xpath("./td[3]/text()").extract()[0]
            # 工作地点
            item['work_location'] = each.xpath("./td[4]/text()").extract()[0]
            # 发布时间
            item['publish_time'] = each.xpath("./td[5]/text()").extract()[0]

            yield item

        if self.offset < 1680:
            self.offset += 10

        # 每次处理完一页的数据之后，重新发送下一页页面请求
        # self.offset自增10，同时拼接为新的url，并调用回调函数self.parse处理Response
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

# -*- coding: utf-8 -*-
import scrapy
from MyScrapyBioon.items import MyscrapybioonItem


class BioonJumpSpider(scrapy.Spider):
    name = 'BioonJump'
    allowed_domains = ['news.bioon.com']
    url = 'http://news.bioon.com/Cfda/'
    offset = 1
    url_request = "".join([url, "lis-", str(offset), ".html"])
    start_urls = [url_request]
    def parse(self, response):
        print("================================start==========================")
        print("开始抓取：", self.url_request)
        datas = response.xpath('//ul[@id="cms_list"]/li')

        for each in datas:
            item = MyscrapybioonItem()
            item['title'] = each.xpath('.//div[@class="cntx"]/h4/a/text()').extract()[0]
            # item['sub_url'] = each.xpath('.//div[@class="cntx"]/h4/a/@href').extract()[0]
            item['sub_url'] = each.xpath('.//div[@class="img"]/a/@href').extract()[0]
            item['img'] = each.xpath('.//div[@class="img"]/a/img/@src').extract()[0]
            brief = each.xpath('.//div[@class="cntx"]/p/text()').extract()[0]
            item['brief'] = brief.strip()

            # item['publish_date'] = each.xpath('.//div[@class="cntx"]/div/text()').extract()[0]
            # item['source'] = ""
            # item['body'] = ''

            # items.append(item)

            # yield item
            print("开始抓取详情:", item['sub_url'])
            yield scrapy.Request(url=item['sub_url'], meta={"meta_item": item}, callback=self.detail_parse)

        print("==============================end=============================")
        if self.offset < 1:
            self.offset += 1
            self.url_request = "".join([self.url, "lis-", str(self.offset), ".html"])
            yield scrapy.Request(url=self.url_request, callback=self.parse)

    def detail_parse(self, response):
        # 提取每次Response的meta数据
        item = response.meta['meta_item']

        print("==============================详情start=============================")
        print("sub_url:", item['sub_url'])
        try:
            # 需要过滤<script></script>
            sources = response.xpath('//div[@class="title5"]/p/text()').extract()
            # print("sources=", sources, "测试")

            str_array = list(map(lambda x: x.split(' '), sources))[0]
            # print("str_array=", str_array, "测试")

            source = ""
            publish_date = ""
            if str_array and len(str_array) == 3:
                source = str_array[0]
                publish_date = "".join([str_array[1], ' ', str_array[2]])

            content = ""
            content_list = response.xpath('//div[@class="text3"]/p/text()').extract()
            # if not content_list:
            #     content_list = response.xpath('//div[@class="text3"]/div/text()').extract()
            # 将p标签里的文本内容合并到一起
            for line in content_list:
                content += line

            item['publish_date'] = publish_date
            item['source'] = source
            item['body'] = content.strip()

        except Exception as e:
            pass

        print("==============================详情end===============================")
        yield item


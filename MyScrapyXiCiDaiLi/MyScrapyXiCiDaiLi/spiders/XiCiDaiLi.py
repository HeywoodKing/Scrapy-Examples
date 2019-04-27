# -*- coding: utf-8 -*-
import scrapy
from MyScrapyXiCiDaiLi.items import MyscrapyxicidailiItem


class XicidailiSpider(scrapy.Spider):
    name = 'XiCiDaiLi'
    allowed_domains = ['xicidaili.com']

    url = 'https://www.xicidaili.com/nn/'
    offset = 1
    url_request = "".join([url, str(offset)])
    start_urls = [url_request]

    # def start_requests(self):
    #     reqs = []
    #     for i in range(1, 206):
    #         req = scrapy.Request("".join([self.url, str(i)]))
    #         reqs.append(req)
    #
    #     return reqs

    def parse(self, response):
        print("================================start==========================")
        print("开始抓取第 %s 页：" % self.offset, self.url_request)
        datas = response.xpath('//table[@id="ip_list"]/tr[position()>1]')
        for each in datas:
            item = MyscrapyxicidailiItem()
            item['country'] = "中国"
            country_img = each.xpath('./td[1]/img/@src').extract()
            item['country_img'] = country_img[0] if country_img else None
            item['ip'] = each.xpath('./td[2]/text()').extract()[0]
            item['port'] = each.xpath('./td[3]/text()').extract()[0]
            server_addr = each.xpath('./td[4]/a/text()').extract()
            item['server_addr'] = server_addr[0] if server_addr else None
            item['is_anonymous'] = each.xpath('./td[5]/text()').extract()[0]
            item['proxy_type'] = each.xpath('./td[6]/text()').extract()[0]
            # item['speed'] = each.xpath('./td[7]/div[@class="bar"]/@title').extract()[0]
            item['speed'] = each.xpath('./td[7]/div[@class="bar"]/@title').re('\d{0,2}\.\d{0,}')[0]
            # item['connect_time'] = each.xpath('./td[8]/div[@class="bar"]/@title').extract()[0]
            item['connect_time'] = each.xpath('./td[8]/div[@class="bar"]/@title').re('\d{0,2}\.\d{0,}')[0]
            item['keep_alive_time'] = each.xpath('./td[9]/text()').extract()[0]
            item['verify_time'] = each.xpath('./td[10]/text()').extract()[0]

            yield item

        print("================================end============================")
        if self.offset < 1:
            self.offset += 1
            self.url_request = "".join([self.url, str(self.offset)])
            yield scrapy.Request(url=self.url_request, callback=self.parse)

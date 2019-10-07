# -*- coding: utf-8 -*-
import scrapy
from MyScrapyStackoverflow.items import MyscrapystackoverflowItem


class StackoverflowSpider(scrapy.Spider):
    name = 'Stackoverflow'
    allowed_domains = ['stackoverflow.com']
    start_urls = ['http://stackoverflow.com/questions?sort=votes']

    # def start_requests(self):
    #     url = 'http://stackoverflow.com'
    #     cookies = {
    #         'dz_username': 'wst_today',
    #         'dz_uid': '1322052',
    #         'buc_key': '',
    #         'buc_token': ''
    #     }
    #
    #     return [
    #         scrapy.Request(url, cookies=cookies),
    #     ]

    def parse(self, response):
        # 这里可以检查是否登陆成功
        # ele = response.xpath('//table[@class="table table-striped"]/thead/tr/th[1]/text()').extract()
        # if ele:
        #     print('success')

        datas = response.css('.question-summary h3 a::attr(href)')
        for href in datas:
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.question_parse)

    def question_parse(self, response):
        item = MyscrapystackoverflowItem()
        # // *[ @ class = "question-summary"]
        item['title'] = response.css('h1 a::text').extract()[0]
        votes = response.css('.question .vote-count-post::text').extract()
        if votes:
            item['votes'] = votes[0]
        item['body'] = response.css('.question .post-text').extract()[0]
        item['tags'] = response.css('.question .post-teg::text').extract()
        item['link'] = response.url

        yield item

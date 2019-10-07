# -*- coding: utf-8 -*-
import scrapy
# from scrapy_redis.spiders import RedisSpider
from MyScrapyChouTi.items import ChoutiItem


# class ChoutiSpider(RedisSpider):
class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['chouti.com']
    start_urls = ['http://dig.chouti.com']

    """
    scrapy-redis中都是用key-value形式存储数据，其中有几个常见的key-value形式：
    1、 “项目名:items”  -->list 类型，保存爬虫获取到的数据item 内容是 json 字符串    
    2、 “项目名:dupefilter”   -->set类型，用于爬虫访问的URL去重 内容是 40个字符的 url 的hash字符串    
    3、 “项目名: start_urls”   -->List 类型，用于获取spider启动时爬取的第一个url    
    4、 “项目名:requests”   -->zset类型，用于scheduler调度处理 requests 内容是 request 对象的序列化 字符串
    """
    # redis_key = 'MyScrapyChouTi:start_urls'

    # headers = {
    #     'user-agent': '',
    # }

    # 如果需要从其他特定网站开始抓取或者登录才能抓取的时候重写此方法
    # def start_requests(self):
    #     return [scrapy.FormRequest("http://www.example.com/login", formdata={'user': 'john', 'pass': 's123456'},
    #                                callback=self.login)]

    # def login(self, response):
    #     # 实现登录后的继续处理
    #     pass

    # def start_requests(self):
    #     url = "http://dig.chouti.com"
    #     yield scrapy.Request(url, headers=self.headers)

    def parse(self, response):
        # 命令行调试
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)

        elements = response.xpath('//div[@class="link-con"]/div')
        for element in elements:
            item = ChoutiItem()
            img_url = element.xpath('./div/a/@data-pic')
            if img_url:
                item['img'] = img_url.extract_first().strip()
            else:
                item['img'] = ''
            item['label'] = element.xpath(
                './div/div/div[@class="link-detail"]/div[@class="link-mark clearfix"]/text()').extract_first().strip()
            item['title'] = element.xpath(
                './div/div/div[@class="link-detail"]/a[@class="link-title link-statistics"]/text()').extract_first().strip()
            item['url'] = element.xpath(
                './div/div/div[@class="link-detail"]/a[@class="link-title link-statistics"]/@href').extract_first().strip()
            link_from = element.xpath(
                './div/div/div[@class="link-detail"]/div[@class="link-from"]/text()')
            if link_from:
                item['link_from'] = link_from.extract_first().strip()
            else:
                item['link_from'] = ''
            link_desc = element.xpath(
                './div/div/div[@class="link-detail"]/div[@class="link-des"]/text()')
            if link_desc:
                item['link_desc'] = link_desc.extract_first().strip()
            else:
                item['link_desc'] = ''
            item['author_img'] = 'https:' + element.xpath(
                './div/div/div[@class="operate-author-con clearfix"]/div[@class="author-con left clearfix"]/span[@class="left author-avatar-name clearfix"]/img/@src').extract_first().strip()
            item['author_name'] = element.xpath(
                './div/div/div[@class="operate-author-con clearfix"]/div[@class="author-con left clearfix"]/span[@class="left author-avatar-name clearfix"]/span/text()').extract_first().strip()
            item['publish_time'] = element.xpath(
                './div/div/div[@class="operate-author-con clearfix"]/div[@class="author-con left clearfix"]/span[@class="left time-enter timeago"]/span[@class="time-update"]/text()').extract_first().strip()
            item['views'] = element.xpath(
                './div/div/div[@class="operate-author-con clearfix"]/div[@class="operate-con right clearfix"]/a[@class="operate-item recommend left clearfix normal"]/span[@class="recommend-num left"]/text()').extract_first().strip()

            print(item)
            yield item

        # 下一页
        # next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        # if next_url:
        #     next_url = self.start_urls + next_url[0]
        #     next_url = response.urljoin(next_url)
        #     yield scrapy.Request(next_url, headers=self.headers)

        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page:
        #     yield response.follow(next_page, callback=self.parse)

# -*- coding: utf-8 -*-
import scrapy
from MyScrapyBioon.items import MyscrapybioonItem


class BioonSpider(scrapy.Spider):
    name = 'Bioon'
    allowed_domains = ['news.bioon.com']
    url = 'http://news.bioon.com/Cfda/'
    offset = 1
    url_request = "".join([url, "lis-", str(offset), ".html"])
    start_urls = [url_request]

    items = []

    def start_requests(self):
        pass
        # ==================================================================================
        # v_headers = response.headers['Set-Cookie']
        # v_cookies = v_headers.split(';')[0].split('=')
        # cookies = {v_cookies[0]: v_cookies[1]}
        #
        # # 模拟请求的头部信息
        # headers = {
        #     'Host': 'login.bioon.com',
        #     'Referer': 'http://login.bioon.com/login',
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0',
        #     'X-Requested-With': 'XMLHttpRequest'
        # }
        #
        # # 获取验证信息
        # csrf_token = response.xpath('//input[@id="csrf_token"]/@value').extract()[0]
        #
        # # 获取post的目的url
        # login_url = response.xpath('//form[@id="login_form"]/@action').extract()[0]
        # end_login = response.urljoin(login_url)
        #
        # # 生成post的数据
        # formdata = {
        #     'account': '',
        #     'client_id': 'usercenter',
        #     'csrf_token': csrf_token,
        #     'grant_type': 'grant_type',
        #     'redirect_uri': 'http://login.bioon.com/userinfo',
        #     'username': '',
        #     'password': '',
        # }
        #
        # # 模拟登陆请求
        # return FormRequest(
        #     end_login,
        #     formdata=formdata,
        #     headers=headers,
        #     cookies=cookies,
        #     callable=self.after_login
        # )
        # ==================================================================================


    # 列表解析
    def parse(self, response):
        print("================================start==========================")
        print("开始抓取：", self.url_request)
        self.logger.info('正在执行：', self.url_request)

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
            # item['source'] = ''
            # item['body'] = ''

            self.items.append(item)

        print("==============================end=============================")


        # 取10页的数据
        if self.offset < 1:
            self.offset += 1
            self.url_request = "".join([self.url, "lis-", str(self.offset), ".html"])
            yield scrapy.Request(url=self.url_request, callback=self.parse)
        else:
            print("开始抓取详情")
            for detail in self.items:
                yield scrapy.Request(url=detail['sub_url'], meta={"meta_item": detail}, callback=self.detail_parse)

    # 详情解析
    def detail_parse(self, response):
        # 提取每次Response的meta数据
        item = response.meta['meta_item']

        print("==============================start=============================")
        print("sub_url:", item['sub_url'])

        # 过滤<script></script>
        try:
            sources = response.xpath('//div[@class="title5"]/p/text()').extract()
            # print("sources=", sources, "测试")

            str_array = list(map(lambda x: x.split(' '), sources))[0]
            # print("str_array=", str_array, "测试")
            # print("str_array=", str_array[0], str_array[1], str_array[2], "测试")

            source = ""
            publish_date = ""
            if str_array and len(str_array) == 3:
                source = str_array[0]
                publish_date = "".join([str_array[1], ' ', str_array[2]])

            content = ""
            content_list = response.xpath('//div[@class="text3"]/p/text() | //div[@class="text3"]/div/text()').extract()
            # 将p标签里的文本内容合并到一起
            for line in content_list:
                content += line

            item['publish_date'] = publish_date
            item['source'] = source
            item['body'] = content.strip()


        except Exception as e:
            pass

        print("==============================end===============================")
        yield item

    def after_login(self, response):
        self.log('Now handling bioon login page.')

        aim_url = 'http://news.bioon.com/Cfda/'

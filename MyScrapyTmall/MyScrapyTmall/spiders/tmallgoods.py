# -*- coding: utf-8 -*-
import scrapy
from MyScrapyTmall.items import MyscrapytmallItem


class TmallgoodsSpider(scrapy.Spider):
    name = 'tmallgoods'
    allowed_domains = ['tmall.com']
    start_urls = ['https://list.tmall.com/search_product.htm?q=%CE%C0%D2%C2%C5%AE&type=p&spm=a220m.1000858.a2227oh.d100&xl=%CE%C0%D2%C2_2&from=.list.pc_1_suggest']

    # 记录处理的页数
    offset = 0

    def parse(self, response):
        self.offset += 1
        divs = response.xpath('//div[@id="J_ItemList"]/div[@class="product"]/div')
        if not divs:
            self.log("List Page error--%s" % response.url)

        for div in divs:
            item = MyscrapytmallItem()
            item['goods_name'] = div.xpath('p[@class="productTitle"]/a/@title')[0].extract()
            item['goods_price'] = div.xpath('p[@class="productPrice"]/em/@title')[0].extract()
            pre_goods_url = div.xpath('p[@class="productTitle"]/a/@href')[0].extract()
            item['goods_url'] = pre_goods_url if "https:" in pre_goods_url else ("https:" + pre_goods_url)

            # 图片链接
            try:
                file_urls = div.xpath('div[@class="productImg-wrap"]/a[1]/img/@src|'
                                      'div[@class="productThumb"]/div[@class="proThumb-wrap"]/p/b[1]/img/@src')[0].extract()
                item['file_urls'] = ["https:" + file_urls]
            except Exception as e:
                print("Error:", e)
                import pdb; pdb.set_trace()

            yield scrapy.Request(url=item["goods_url"], meta={'item': item}, callback=self.detail_parse, dont_filter=True)


    def detail_parse(self, response):
        div = response.xpath('//div[@class="extend"]/ul')
        if not div:
            self.log("Detail Page error--%s" % response.url)

        item = response.meta['item']
        div = div[0]
        item['shop_name'] = div.xpath('li[1]/div/a/text()')[0].extract()
        item['shop_url'] = div.xpath('li[1]/div/a/@href')[0].extract()
        item['company_name'] = item['shop_name']
        item['company_addr'] = div.xpath('li[4]/div/text()')[0].extract().strip()

        yield item

# -*- coding: utf-8 -*-
import scrapy


class DigikeySpider(scrapy.Spider):
    name = 'digikey'
    allowed_domains = ['digikey.com']
    start_urls = ['http://digikey.com/']

    def parse(self, response):
        pass

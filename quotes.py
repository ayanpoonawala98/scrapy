# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['www.brainyquote.com/']
    start_urls = ['http://www.brainyquote.com//']

    def parse(self, response):
        pass

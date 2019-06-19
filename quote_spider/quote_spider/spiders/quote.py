# -*- coding: utf-8 -*-
import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    allowed_domains = ['http://quotes.toscrape.com/']
    start_urls = ['http://http://quotes.toscrape.com//']

    def parse(self, response):
        header=response.xpath('//h1/a/text()').extract()
        quote=response.xpath('//*[@class="text"]/text()').extract()
        author=response.xpath('//*[@class="author"]/text()').extract()
        tag=response.xpath('//*[@class="tag-item"]/a/text()').extract()

        yield{"Header":'header',
        		"Quote":'quote',
        		"Author": 'author',
        		"Tag":'tag'}

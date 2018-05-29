# -*- coding: utf-8 -*-
import scrapy


class SistaMinutenSpider(scrapy.Spider):
    name = 'sista-minuten'
    allowed_domains = ['https://www.folktandvardenstockholm.se']
    start_urls = ['http://https://www.folktandvardenstockholm.se/']


    def parse(self, response):
        yield response.css('div.has-help.cf').extract()

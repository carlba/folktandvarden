# -*- coding: utf-8 -*-
import scrapy


class SistaMinutenSpider(scrapy.Spider):
    name = 'sista-minuten'
    allowed_domains = ['https://www.folktandvardenstockholm.se']
    start_urls = ['https://www.folktandvardenstockholm.se/']

    def parse(self, response):
        yield {
            'text': response.css('div.has-help.cf').extract()
        }


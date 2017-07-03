# -*- coding: utf-8 -*-
import scrapy
from ..items import MmjpgItem
from scrapy import Request
class MmjpgspdSpider(scrapy.Spider):
    name = 'mmjpgspd'
    allowed_domains = ['http://www.mmjpg.com']
    start_urls = ['http://www.mmjpg.com/mm/1033']

    def parse(self, response):
        item = MmjpgItem()
        item['image_urls'] = response.xpath('//div[@id="content"]/a/img/@src').extract()
        yield item
        next_page = response.xpath('//div[@id="page"]/a[@class="ch next"]/@href').extract_first()
        if next_page is not None:
            print(next_page)
            next_page = response.urljoin(next_page)
            yield Request(next_page, callback=self.parse, dont_filter=True)

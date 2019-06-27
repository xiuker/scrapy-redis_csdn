# -*- coding: utf-8 -*-
from scrapy.spider import CrawlSpider,Rule  
from scrapy.linkextractors import LinkExtractor  
from demo.items import MasterItem  

class MasterSpider(CrawlSpider):
    name = 'master'
    allowed_domains = ['edu.csdn.net']
    start_urls = ['https://edu.csdn.net/courses/k']
    item = MasterItem()
    #Rule是在定义抽取链接的规则
    rules = (  
        Rule(LinkExtractor(allow=('https://edu.csdn.net/course/detail/[0-9]+','https://edu.csdn.net/courses/k/p[0-9]+')), callback='parse_item',  
             follow=True),  
    ) 

    def parse_item(self, response):
        item = self.item  
        item['url'] = response.url  
        return item

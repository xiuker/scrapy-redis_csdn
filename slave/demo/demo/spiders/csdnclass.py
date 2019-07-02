# -*- coding: utf-8 -*-
import scrapy
from demo.items import ClassItem
from scrapy_redis.spiders import RedisSpider

class CsdnclassSpider(RedisSpider):
    name = 'csdnclass'
    
    redis_key = "csdnspider:start_urls"
    print(redis_key)
    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(CsdnclassSpider, self).__init__(*args, **kwargs)
        
    def parse(self, response):
        #print(response.status)
        vo = response 
        
        item = ClassItem()
        item['title'] = vo.css("h1::text").extract_first()
        #item['hours'] = vo.css("span.addressName::text").extract_first()
        item['teachers'] = vo.css("div.professor_name a::text").extract_first()
        #item['suitpeople'] = vo.re("<span><i>([0-9]+)</i>浏览</span>")[0]
        item['leanersnum'] = vo.css("div.course_status span::text").extract_first()
        item['price'] = vo.css("span.pr::text").extract_first()
        item['descrption'] = vo.css("div.J_outline_discribe_content::text").extract()[-1]
        #print(item)
        yield item
        #pass

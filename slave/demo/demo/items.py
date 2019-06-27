# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ClassItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    #hours = scrapy.Field()
    teachers = scrapy.Field()
    #suitpeople = scrapy.Field()
    leanersnum = scrapy.Field()
    price = scrapy.Field()
    descrption = scrapy.Field()
    #pass

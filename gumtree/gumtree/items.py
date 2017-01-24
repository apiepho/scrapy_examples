# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Item,Field

class GumtreeItem(scrapy.Item):
    ad_description = Field()
    ad_title       = Field()
    ad_location    = Field()
    ad_time        = Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

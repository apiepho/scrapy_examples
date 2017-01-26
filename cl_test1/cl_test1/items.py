# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Item,Field

class CraigsListItem(scrapy.Item):
    description = Field()
    location    = Field()
    time        = Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

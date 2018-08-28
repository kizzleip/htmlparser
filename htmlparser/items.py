# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HtmlparserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    region = scrapy.Field()
    categary = scrapy.Field()
    floor_area = scrapy.Field()
    orientation = scrapy.Field()
    renovation = scrapy.Field()
    elevator = scrapy.Field()
    floor = scrapy.Field()
    years = scrapy.Field()
    price = scrapy.Field()
    listing_time = scrapy.Field()
    metro = scrapy.Field()
    url = scrapy.Field()
    id = scrapy.Field()

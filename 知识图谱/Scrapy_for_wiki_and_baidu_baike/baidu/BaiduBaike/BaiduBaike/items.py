# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaidubaikeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    text = scrapy.Field()
    Chinese_name = scrapy.Field()
    foreign_name = scrapy.Field()
    abbreviation = scrapy.Field()
    proposal_time = scrapy.Field()
    proposal_location = scrapy.Field()
    source = scrapy.Field()
    definition = scrapy.Field()
    basicInfo = scrapy.Field()
    detail = scrapy.Field()
    pass

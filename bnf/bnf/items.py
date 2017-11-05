# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BnfItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    titre = scrapy.Field()
    temps_du_scrap = scrapy.Field()
    pass

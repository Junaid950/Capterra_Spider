# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CapterraItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    topicNameList=scrapy.Field()
    topicLinkList=scrapy.Field()
    pass
class TopicItem(scrapy.Item):
    title=scrapy.Field()
    topicLink=scrapy.Field()
    description=scrapy.Field()
    vendorList=scrapy.Field()
    productList=scrapy.Field()
    productLinkList=scrapy.Field()
    pass
class ProductItem(scrapy.Item):
    prod_name=scrapy.Field()
    prod_pageLink=scrapy.Field()
    prod_desc=scrapy.Field()
    vendorInfo=scrapy.Field()
    deployPlatform=scrapy.Field()
    pass

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# import os
# from scrapy.http import Request
from capterra.items import CapterraItem,TopicItem,ProductItem
from scrapy.exporters import JsonLinesItemExporter

class CapterraPipeline(object):
    def __init__(self):
        self.fp=open("capterra.json",'wb')
        self.exporter=JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
        # self.exporter.start_exporting()
    def open_spider(self,spider):
        print("CapterraItem爬虫开始了!")
        pass
    def process_item(self,item,spider):
        if isinstance(item,CapterraItem):
            self.exporter.export_item(item)
        return item
        # self.exporter.export_item(item)
        # return item
    def close_spider(self,spider):
        self.fp.close()
        print("CapterraItem爬虫结束了！")
        pass
class TopicPipeline(object):
    def __init__(self):
        self.fp=open("topic.json",'wb')
        self.exporter=JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
    def open_spider(self,spider):
        print("TopicItem爬虫开始了!")
        pass
    def process_item(self,item,spider):
        if isinstance(item,TopicItem):
            self.exporter.export_item(item)
        return item
    def close_spider(self,spider):
        self.fp.close()
        print("TopicItem爬虫结束了！")
        pass
class ProductPipeline(object):
    def __init__(self):
        self.fp=open("product.json",'wb')
        self.exporter=JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
    def open_spider(self,spider):
        print("ProductItem爬虫开始了!")
        pass
    def process_item(self,item,spider):
        if isinstance(item,ProductItem):
            self.exporter.export_item(item)
        return item
    def close_spider(self,spider):
        self.fp.close()
        print("ProductItem爬虫结束了！")
        pass

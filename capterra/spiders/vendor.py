# -*- coding: utf-8 -*-
import scrapy
import re

from capterra.items import CapterraItem,TopicItem,ProductItem

base_domain=r'https://www.capterra.com'

class VendorSpider(scrapy.Spider):
    name = 'vendor'
    #allowed_domains = ['capterra.com']
    start_urls = ['https://www.capterra.com/categories']
    # base_domain=r'https://www.capterra.com'
    def parse(self, response):
        #pass
        topicNameList=response.xpath(r'/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div[*]/div/div/div[2]/ol/li[*]/a/text()').getall()
        # topicNameList=response.css(r'ol.browse-group-list>li.even').getall()
        topicLinkList_fake=response.xpath(r'/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div[*]/div/div/div[2]/ol/li[*]/a/@href').getall()
        # topicLinkList_fake=response.css(r'ol.browse-group-list>li.even').getall()
        url_base=r'https://www.capterra.com'
        topicLinkList=[]
        for i in topicLinkList_fake:
            full_url=url_base+i
            print("full url:",full_url)
            topicLinkList.append(full_url)
        item=CapterraItem(
            topicNameList=topicNameList,
            topicLinkList=topicLinkList)
        yield item
        for topicLink in topicLinkList:
            yield scrapy.Request(topicLink,callback=self.parse_topic)
    def parse_topic(self,response): # TopicItem
        title=response.xpath(r'//h1/text()').get()
        topicLink=response.url
        description=response.xpath(r'/html/body/div[1]/div/div[2]/div/div[1]/div/div/div/div[1]/p[1]/text()').get()
        vendorList_fake=response.xpath(
            r'//h3[@class="VendorNameContainer__VendorHeading-sc-1o44ecm-0 hgjCmh Heading-p3hmo4-2 fyTAWX"]/span/text()').getall()# regex is required.
        vendorList=[]
        for i in vendorList_fake:
            vli=re.sub(r'^.*[Bb]y\s*',r'',i)
            vendorList.append(vli)
        productList=response.xpath(r'//h2[@class="ProductHeaderSection__ProductHeader-sc-2ridoo-0 bYuVMH Heading-p3hmo4-1 goUiYV"]//a/text()').getall()
        productLinkList_fake=response.xpath(r'//h2[@class="ProductHeaderSection__ProductHeader-sc-2ridoo-0 bYuVMH Heading-p3hmo4-1 goUiYV"]//a/@href').getall()
        productLinkList=[]
        for i in productLinkList_fake:
            full_url=base_domain+i
            productLinkList.append(full_url)
        print(productLinkList)
        item=TopicItem(
            title=title,
            topicLink=topicLink,
            description=description,
            vendorList=vendorList,
            productList=productList,
            productLinkList=productLinkList)
        yield item
        for productLink in productLinkList:
            print(productLink)
            yield scrapy.Request(productLink,callback=self.parse_product)
    def parse_product(self,response):  # ProductItem
        pass
        prod_name=response.xpath(
            r'/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/div[1]/div/div[2]/h1/text()').get()
        prod_pageLink=response.url
        prod_desc=response.xpath(
            r'//div[@class="Section__Body-w4hkcm-1 jhCJZs"]/text()').get()
        vendorInfo=response.xpath(r'//div[@class="Section__Root-w4hkcm-0 ijZEOY"]//p[@class="ProductSummary__CompanyDetailItem-uex5jn-5 fxpGcm"]/text()').getall()
        deployPlatform=response.xpath(r'//div[@class="SpecRow__Root-sc-2l3qlv-0 iFFnMV"][3]//ul[@class="SpecRow__RowBody-sc-2l3qlv-3 iwSLdU"]//div[@class="IconWrapper__Root-wy2f04-0 bqMKDC"]/following-sibling::*/text()').getall() # 这个xpath,准确度有待验证,有时间再看看吧！
        item=ProductItem(
            prod_name=prod_name,
            prod_pageLink=prod_pageLink,
            prod_desc=prod_desc,
            vendorInfo=vendorInfo,
            deployPlatform=deployPlatform
        )
        yield item

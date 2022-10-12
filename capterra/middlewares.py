# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
from faker import Faker
#-我自己改的随机USER_AGENT-############################
# from faker import Faker
# f1=Faker()
# def uafake():
    # fakeua=f1.chrome()
    # yield fakeua
# ct=0
# while ct<754:
    # a1=uafake()
    # USER_AGENT=a1.__next__()
    # #print(USER_AGENT)
    # ct+=1
# f2=Faker()
# USER_AGENT=f2.chrome()
#####################################################

class CapterraSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass
        print(r'#'*30)
        print(r'出现意外!')

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class CapterraDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
class UAdownloadMiddleware(object):
    # 随即请求头
    def process_request(self,request,spider):
        pass
        f1=Faker()
        user_agent=f1.chrome()
        request.headers['User-Agent']=user_agent

class IPproxyMiddleware(object):
    pass
    import re
    fdir=r'/home/debian/Documents/scrapyPrj/capterra/proxyIpList.txt'
    with open(fdir,'r') as f:
        f1=f.readlines()
    f2=[]
    for i in f1:
        f2_fake=re.sub(r'\s*\n$',r'',i)
        f2.append(f2_fake)
    proxyList=f2
    def process_request(self,request,spider):
        proxy=random.choice(self.proxyList)
        request.meta['proxy']=proxy

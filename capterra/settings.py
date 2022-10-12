# -*- coding: utf-8 -*-

# Scrapy settings for capterra project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'capterra'

SPIDER_MODULES = ['capterra.spiders']
NEWSPIDER_MODULE = 'capterra.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64…) Gecko/20100101 Firefox/74.0'

#-我自己改的随机USER_AGENT-############################
from faker import Faker
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

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
import numpy as np
c_requests=np.random.randint(67,122)
CONCURRENT_REQUESTS = c_requests

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
import numpy as np
d_delay=np.random.randint(2,7)
DOWNLOAD_DELAY = d_delay
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
   # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   # 'Accept-Language': 'en-US,en;q=0.5',
   # 'Connection':'keep-alive'
# }
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/css,*/*;q=0.1',
   'Accept-Encoding': 'gzip,deflate,br',
   'Accept-Language': 'en-US,en;q=0.5',
   'Connection':'keep-alive',
   # 'DNT':1,
   # 'Host':'www.capterra.com',
   'User-Agent':'Mozilla/5.0 (X11; Linux x86_64…) Gecko/20100101 Firefox/74.0'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'capterra.middlewares.CapterraSpiderMiddleware': 300,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'capterra.middlewares.CapterraDownloaderMiddleware': 543,
    'capterra.middlewares.UAdownloadMiddleware': 543,
    'capterra.middlewares.IPproxyMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'capterra.pipelines.CapterraPipeline': 300,
    'capterra.pipelines.TopicPipeline':300,
    'capterra.pipelines.ProductPipeline':300
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

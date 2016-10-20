# -*- coding: utf-8 -*-

# Scrapy settings for hellospider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'hellospider'

SPIDER_MODULES = ['hellospider.spiders']
NEWSPIDER_MODULE = 'hellospider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'hellospider (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'en-US,en;q=0.8,ta;q=0.6',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Cookie':'__cfduid=d279e77d9b97062642a2dcc5d516b4a3d1476878622; _ga=GA1.2.2083759861.1476879293; _hjIncludedInSample=1; XSRF-TOKEN=eyJpdiI6InU1ZU1LTlVKNnZuTG96S2FSb3p0Wmc9PSIsInZhbHVlIjoiN2cwazB4cXNQQk5qNlFLZFRKczhQVlF6VVJMTlVQTXhXSlk0cWhSWWVVZ2pqR2FkMnZDdGZnTXhDY0I5OU5qaUJXVXBZa3lYT1J0WjlGdVdpSlJcL0xRPT0iLCJtYWMiOiJiNzIzZDQwNmZkYzNlYTNhMjA4ZmVlNWJiZTdlZWUzNjcwYWI0MzUxYzEzOTRhZDQxMjhhNTgxMTE4MDQyNjBlIn0%3D; laravel_session=eyJpdiI6ImgybGxLRWlWNEZ3c2w2QjZFNzdXR0E9PSIsInZhbHVlIjoiZ2NTZlNNa3NhcHhLVDh6SU9rTjVqMVFIRkFBRDRMZ2JNb205RWlMcklcL2N6VlkyZndKMUcycU1aTmVwSTU0RzNuaTlJeFhLd1BSR29WYzQrTEoxUzJBPT0iLCJtYWMiOiIzZjk5MGFmZTQzNTE5ZDk0MjQyZWExZWE5YTljOTZlOTc3YzI2OTRlMmE1MTNmODFlNzc2MWI2YTNhMGE0Yjc0In0%3D',
    'Host':'techsg.io',
    'Pragma':'no-cache',
    'Referer':'http://techsg.io/ecosystem?show=Startup',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'hellospider.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'hellospider.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'hellospider.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

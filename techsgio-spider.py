import scrapy
import json

pagecount = 1
url_array = []

with open('sample.json') as json_data:
    d = json.load(json_data)
    print (d)

class BlogSpider(scrapy.Spider):
    name = 'techsgiospider'
    start_urls = ['http://techsg.io/ecosystem?show=Startup&keyword=All&page=1']

    def parse(self, response):
        for title in response.css('div.box-white'):
            yield {
                    'url': title.css('a ::attr(href)').extract_first(),
                    'title': title.css('a ::attr(title)').extract_first(),
                  }

        next_page = response.css('a.pagination ::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

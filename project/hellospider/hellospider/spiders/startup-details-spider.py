import scrapy
import json

pagecount = 1
url_array = []

#this spider will read from json file.. and crawl all the startup details independently..

with open('/Users/prasannav/Work/NUS-ISS/crawler/sample.json') as json_data:
    d = json.load(json_data)
    for obj in d:
        url_array.append(obj.get('url'))

class BlogSpider(scrapy.Spider):
    name = 'startup-details-spider'
    start_urls = url_array

    def parse(self, response):
        print (response.request.headers['User-Agent'])

        for links in response.css('div.box-white > .row'):
            yield { 'baseurl': response.url,
                    'key': links.css('div.mb15 > div > strong ::text').extract_first(),
                   'value': links.css('div.mb15 > div > a ::text').extract_first()
                   }

        next_page = None
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

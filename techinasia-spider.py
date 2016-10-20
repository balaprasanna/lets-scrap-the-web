import scrapy
import json

class BlogSpider(scrapy.Spider):
    name = 'techinasia-company-list-spider'
    start_urls = ['https://www.techinasia.com/startups?country_name%5B%5D=Singapore']

    def parse(self, response):

        json_response = json.load(response.text);
        print (json_response);

        for searchresults in response.css('div.search-results'):
            searchresult_item = searchresults.css('div.search-results__item > div.media-body')

            yield {'company': searchresult_item.css('h3 > a ::text').extract_first(),
                   'url': searchresult_item.css('h3 > a ::attr(href)').extract_first()
                   }

        next_page = response.css('div.pagination-wrapper > ul.pagination > li:nth-last-child(1) > a ::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

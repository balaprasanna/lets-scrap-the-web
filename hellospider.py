import scrapy

baseurl = 'http://quotes.toscrape.com'
class HelloSpider(scrapy.Spider):
    name = 'hellospider'
    baseurl = baseurl;
    start_urls = [baseurl + '/tag/inspirational']

    def parse(self, response):
        print (response)

        for title in response.css('div.quote > span > small.author'):
            print (title.css('::text').extract_first())

        for tag in response.css('span.tag-item'):
            tag_page = baseurl + tag.css('a ::attr(href)').extract_first()
            if tag_page:
                yield scrapy.Request(response.urljoin(tag_page), callback=self.parse)

            print (baseurl + tag.css('a ::attr(href)').extract_first())


            #yield {'title': title.css('a ::text').extract_first()}

        # for title in response.css('h2.entry-title'):
        #     print (title.css('a ::text').extract_first())
        #     yield {'title': title.css('a ::text').extract_first()}

        next_page = response.css('ul.pager > li.next > a ::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

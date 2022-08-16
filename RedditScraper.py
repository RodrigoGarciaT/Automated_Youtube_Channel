import scrapy
from scrapy.crawler import CrawlerProcess

final_titles = []
final_text = []


class RedditSpider(scrapy.Spider):
    name = "RedditSpider"

    def start_requests(self):
        urls = [
            'https://www.reddit.com/r/AmItheAsshole/hot/',
             'https://www.reddit.com/r/confessions/hot/',
             'https://www.reddit.com/r/tifu/hot/'
               ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.get_post_links)

    def get_post_links(self, response):

        # web scraping the url of every single post
        urls = response.css('div._1poyrkZ7g36PawDueRza-J > div._1ixsU4oQRnNfZ91jhBU74y > div._3-miAEojrCvx_4FQ8x3P-s').xpath('./a/@href').extract()
        # Sending every post to be web scraped

        for url in urls:
            print(url)
            yield response.follow(url=url, callback=self.get_post_information)

    def get_post_information(self, response):
        #web scraping each individual post
        titles = response.css('h1._eYtD2XCVieq6emjKBH3m::text').extract()
        final_titles.append(titles[0])
        print(titles[0])
        text = response.css('div._292iotee39Lmt0MkQZ2hPV ::text').extract()
        final_text.append(text[0])
        print(text[0])


process = CrawlerProcess()
process.crawl(RedditSpider)
process.start()
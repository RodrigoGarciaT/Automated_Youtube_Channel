import scrapy
from scrapy.crawler import CrawlerProcess


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
        pass
        #web scraping each individual post


process = CrawlerProcess()
process.crawl(RedditSpider)
process.start()
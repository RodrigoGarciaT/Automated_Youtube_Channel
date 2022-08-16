import scrapy
from scrapy.crawler import CrawlerProcess


class RedditSpider(scrapy.Spider):
    name = "reddit_spider"

    def start_requests(self):

        urls = [
            'https://www.reddit.com/r/AmItheAsshole/hot/',
             'https://www.reddit.com/r/confessions/',
             'https://www.reddit.com/r/tifu/'
               ]
        for url in urls:
            yield scrapy.request(url=url, callback=self.get_post_links)

    def get_post_links(self, response):
        pass
        # web scraping the url of every single

        # Sending every post to be web scraped
        urls = []
        for url in urls:
            yield response.follow(url=url, callback=self.get_post_information)

    def get_post_information(self, response):
        pass
        #web scraping each individual post

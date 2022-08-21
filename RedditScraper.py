import scrapy
from scrapy.crawler import CrawlerProcess
import pyttsx3
engine = pyttsx3.init()
voice = engine.getProperty('voices')
final_links = []
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
        global story
        #web scraping each individual post
        titles = response.css('h1._eYtD2XCVieq6emjKBH3m::text').extract()
        final_links.append(response.url)
        final_titles.append(titles[0])
        text = response.xpath('//div[@data-test-id="post-content"]').css('div._292iotee39Lmt0MkQZ2hPV ::text').extract()
        final_text.append(text)


def main():
    process = CrawlerProcess()
    process.crawl(RedditSpider)
    process.start()

    engine.setProperty('voice', voice[2].id)

    engine.save_to_file(final_text[6][0], 'audio.mp3')
    return final_text

    '''
    engine.save_to_file(say, 'audio.mp3')
    engine.runAndWait()
    #print(say)
    '''
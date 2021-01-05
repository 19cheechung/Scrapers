import scrapy


class MultiYahooSpider(scrapy.Spider):
    name = 'multi_yahoo'
    allowed_domains = ['finance.yahoo.com']
    start_urls = ['http://finance.yahoo.com/']

    def parse(self, response):
        pass

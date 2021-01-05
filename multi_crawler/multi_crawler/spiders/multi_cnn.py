import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import linkExtractor

class MultiCnnSpider(scrapy.Spider):
    name = 'multi_cnn'
    allowed_domains = ['cnn.com']
    start_urls = ['http://cnn.com/africa']
    
    def parse(self, response):
        article=Newsarticle()
        article['title']= response.xpath('//h1/text()').get() or response.xpath('//h1/i/text()').get()
        article['url']= response.url
        article['source']= 'CNN'
        article['author']:response.xpath('//meta[@name="author"]/@content').get(),
        article['description']=response.xpath('//meta[@name="DC.Description.Abstract"]/@content').get(),
        article['text']=w3lib.html.remove_tags(response.xpath('//div[@class="text"]').get()),
        article['date']=response.xpath('//span[@class="subheading"]/text()').getall(), 
        

  
 
   
        return article


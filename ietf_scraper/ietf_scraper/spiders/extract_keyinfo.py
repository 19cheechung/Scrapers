import scrapy
import w3lib.html


class IetfSpider(scrapy.Spider):
    name = 'extract_keyinfo'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']
            
    def parse(self, response):
        #title=response.css('span.title::text').get()
        return {
            'number':response.xpath('//span[@class="rfc-no"]/text()').get(),
            #used class, in html it has no content object, just text
            'title':response.xpath('//span[@class="title"]/text()').get(),
            #used metaname, has content object
            'title2':response.xpath('//meta[@name="DC.Title"]/@content').get(),
            'author':response.xpath('//meta[@name="DC.Creator"]/@content').get(),
            'summary':response.xpath('//meta[@name="DC.Description.Abstract"]/@content').get(),
            'text':w3lib.html.remove_tags(response.xpath('//div[@class="text"]').get()),
            'headings':response.xpath('//span[@class="subheading"]/text()').getall(),         
        }

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from datetime import datetime
from scrapy.exceptions import DropItem


class CheckItemPipeline:
    def process_item(self, article, spider):
        if not article['lastupdated'] or not article['url'] or not article['title']:
            raise DropItem('Missing something!')
        return article

class CleanDatePipeline:
    def process_item(self, article, spider):
        article['lastupdated']=article['lastupdated'].replace('This page was last edited on','').strip()
        print(article['lastupdated'])
        # example : This page was last edited on 1 January 2021, at 17:28
        article['lastupdated']=datetime.strptime(article['lastupdated'],'%d %B %Y, at %H:%M')

        return article
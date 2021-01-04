# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CheckItemPipeline:
    def process_item(self, article, spider):
        if not article['lastupdated'] or not article['url'] or not article['title']:
            raise DropItem('Missing something!')
        return item

class CleanDatePiepeline:
    def process_item(self, article, spider):
        article['lastupdated'].replace('This page was last edited on', '').strip()
        article['lastupdated']=datetime.strptime(article['lastupdated'],'%d %B %Y, at %H:%M')

        return article

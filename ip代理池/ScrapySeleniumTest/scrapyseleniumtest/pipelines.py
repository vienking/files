# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# import pymongo
import json
'''
class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
    
    @classmethod
    def from_crawler(cls, crawler):
        return cls(mongo_uri=crawler.settings.get('MONGO_URI'), mongo_db=crawler.settings.get('MONGO_DB'))
    
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
    
    def process_item(self, item, spider):
        self.db[item.collection].insert(dict(item))
        return item
    
    def close_spider(self, spider):
        self.client.close()
'''

class jsonPipeline(object):

    def open_spider(self, spider):
        self.f = open('./zhongheng.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.f.write(json.dumps(dict(item), ensure_ascii=False) + ',\n')
        return item

    def close_spider(self, spider):
        self.f.close()


# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.utils.project import get_project_settings

import pymongo


class ScrapybaiduPipeline(object):
    collection_name = 'iphoneSexAge'

    def __init__(self, mongo_url, mongo_db):
        self.mongo_db = mongo_db
        self.mongo_url = mongo_url

        self.client = None
        self.db = None

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_db=crawler.settings.get("MONGO_DB"),
            mongo_url=crawler.settings.get("MONGO_URL"),
        )

    def open_spider(self, spider):
        try:
            self.client = pymongo.MongoClient(self.mongo_url)
            self.db = self.client[self.mongo_db]
        except Exception as e:
            print("error: 数据库连接出错  >>> {}".format(e))

    def process_item(self, item, spider):
        print("processing item  >>> {}".format(item))
        try:
            self.db[self.collection_name].insert(dict(item))
            print("ok")
        except Exception as e:
            print("error: 数据插入错误  >>> {}".format(e))

    def close_spider(self, spider):
        self.client.close()

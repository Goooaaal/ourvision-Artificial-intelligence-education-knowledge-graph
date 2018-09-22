# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class BaiduzhidaoPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host="47.75.70.164", port=27017)
        # self.client = pymongo.MongoClient(host="localhost", port=27017)
        self.db = self.client['YJ_DB']
        self.collection = self.db['baiduzhidao']

    def process_item(self, item, spider):
        # print(item)
        self.collection.insert(dict(item))
        return item

    def __del__(self):
        self.client.close()

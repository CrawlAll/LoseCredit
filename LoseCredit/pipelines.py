# -*- coding: utf-8 -*-
import pymongo


class LoseCreditPipeline(object):
	def __init__(self, host, dbname, port, sheetname):
		self.host = host
		self.dbname = dbname
		self.port = port
		self.sheetname = sheetname

	@classmethod
	def from_crawler(cls, crawler):
		return cls(
			host=crawler.settings.get('MONGODB_HOST'),
			port=crawler.settings.get('MONGODB_PORT'),
			dbname=crawler.settings.get('MONGODB_DBNAME'),
			sheetname=crawler.settings.get('MONGODB_SHEETNAME')
		)

	def open_spider(self, spider):
		# 连接MONGODB
		self.client = pymongo.MongoClient(host=self.host, port=self.port)
		# 指定数据库
		self.mydb = self.client[self.dbname]
		# 存放数据的数据库表名
		self.sheet = self.mydb[self.sheetname]

	def process_item(self, item, spider):
		data = dict(item)
		self.sheet.insert(data)
		return item

# -*- coding: utf-8 -*-
import scrapy


class LoseCreditItem(scrapy.Item):
	lose_credit_name = scrapy.Field()
	position = scrapy.Field()  # 职位
	company = scrapy.Field()  # 公司名称
	court = scrapy.Field()  # 法院
	sheng_fen = scrapy.Field()
	num = scrapy.Field()
	an_hao = scrapy.Field()
	duty = scrapy.Field()  # 义务
	condition = scrapy.Field()  # 当下状况
	detail = scrapy.Field()  # 具体信息
	publish_time = scrapy.Field()  # 处罚时间

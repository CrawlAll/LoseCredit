# -*- coding: utf-8 -*-
import re
import time
import scrapy
from LoseCredit.items import LoseCreditItem


class LoseCreditBaiduSpider(scrapy.Spider):
	name = 'lose_credit_baidu'
	allowed_domains = ['baidu.com']

	def start_requests(self):
		for page in range(10000000):
			url = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=%E5%A4%B1%E4%BF%A1%E8%A2%AB%E6%89%A7%E8%A1%8C%E4%BA%BA%E5%90%8D%E5%8D%95&cardNum=&iname=%E5%85%AC%E5%8F%B8&areaName=&pn={}&rn=10&ie=utf-8&oe=utf-8&format=json&t={}&cb=jQuery110200944566720190545_1517965042079&_={}'.format(
				(page * 10), (int(round(time.time() * 1000))), 1517967480150 + page)
			headers = {
				"Host": "sp0.baidu.com",
				"Referer": "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%A4%B1%E4%BF%A1%E4%BA%BA&oq=%25E5%25A4%25A9%25E7%259C%25BC%25E6%259F%25A5&rsv_pq=8669954300040440&rsv_t=27dfUZN11Urcb2b8hz3%2FBab7bhcDj%2B8n%2FXaUYkf0vtIJko394k5GKkRZZ48&rqlang=cn&rsv_enter=1&rsv_sug3=34&rsv_sug1=32&rsv_sug7=100&bs=%E5%A4%A9%E7%9C%BC%E6%9F%A5",
				"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
			}
			yield scrapy.Request(url=url, headers=headers, callback=self.parse)

	def parse(self, response):
		item = LoseCreditItem()
		text = response.text.replace('\n', '').replace('\t', '').replace('\r', '')
		content_list = re.findall(
			'"_update_time":"(.*?)", "cambrian_appid":"(.*?)", "changefreq":"(.*?)", "age":"(.*?)", "areaName":"(.*?)", "businessEntity":"(.*?)", "cardNum":"(.*?)", "caseCode":"(.*?)", "courtName":"(.*?)", "disruptTypeName":"(.*?)", "duty":"(.*?)", "focusNumber":"(.*?)", "gistId":"(.*?)", "gistUnit":"(.*?)", "iname":"(.*?)", "partyTypeName":"(.*?)", "performance":"(.*?)", "performedPart":"(.*?)", "publishDate":"(.*?)", "publishDateStamp":"(.*?)", "regDate":"(.*?)", "sexy":"(.*?)", "sitelink":"(.*?)", "type":"(.*?)", "unperformPart":"(.*?)", "lastmod":"(.*?)", "loc":"(.*?)", "priority":"(.*?)", "SiteId":(.*?), "_version":(.*?), "_select_time":(.*?)',
			text)
		if len(content_list) > 0:
			content = content_list[0:10]
			for detail in content:
				if len(detail[14]) < 4:
					item["lose_credit_name"] = detail[14]
				else:
					item["lose_credit_name"] = detail[5]
				item["company"] = detail[14]
				item["position"] = '法人'
				item["court"] = detail[8]
				item["sheng_fen"] = detail[4]
				item["num"] = detail[6]
				item["an_hao"] = detail[7]
				item["duty"] = detail[10]
				item["condition"] = detail[16]
				item["detail"] = detail[9]
				item["publish_time"] = detail[18]
				yield item

# coding = utf-8
"""
抓取关键词相关的需求图谱
严格按照百度指数上的时间段作为起始日期

"""
import datetime
import json
import random
from urllib.parse import quote
import scrapy
from dateutil import relativedelta

from settings import COOKIES
from items import RelatedWordItem
from spiders.base_spider import BaseSpider

class RelatedWordSpider(BaseSpider):
    name = 'related_word'

    def __init__(self, *args, **kwargs):
        super(RelatedWordSpider, self).__init__(*args, **kwargs)
        self.base_url = 'http://index.baidu.com/Interface/Newwordgraph?word={}&datelist='
        self.set_param_file('paramdemo.json')
        self.set_time_split(relativedelta.relativedelta(days=1))

    def start_requests(self):
        for keyword in self.keywords:
            for date in self.date_range_list:
                start_url = self.base_url.format(quote(keyword))
                yield scrapy.Request(url=start_url, callback=self.parse,
                                     cookies=random.choice(COOKIES), meta={'date': date})

    def parse(self, response):
        result = json.loads(response.body.decode('utf-8'))
        item = RelatedWordItem()
        date = response.meta['date']
        if result['status'] != 10002:
            if result['data']:
                item['keyword']=result['word']
                lists=[]
                for i in result['data']:
                    lists.append(result['data'][i])
                related_word=[]
                count=[]
                for it in lists:
                    for i in it:
                        item['related_word'], item['count'] = i.split('\t')
                        yield item
            else:
                print("该关键词暂无数据")

        else:
            print("未收录该关键词")

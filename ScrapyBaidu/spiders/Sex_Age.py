# coding = utf-8
"""
根据关键词抓取人群属性，包括年龄分布和性别分布
固定时间段为1个月，手动更改日期段列表

"""
import json
import random
from urllib.parse import quote

import scrapy
from dateutil import relativedelta

from settings import COOKIES
from items import SexAgeItem
from spiders.base_spider import BaseSpider


class SexAgeSpider(BaseSpider):
    name = 'sex_age'

    def __init__(self, *args, **kwargs):
        super(SexAgeSpider, self).__init__(*args, **kwargs)
        self.base_url = 'https://index.baidu.com/api/SocialApi/getSocial?wordlist%5B%5D={}&startdate={}&enddate={}'
        self.set_param_file('paramdemo.json')
        self.set_time_split(relativedelta.relativedelta(months=1))

    def start_requests(self):
        for keyword in self.keywords:
            for date in self.date_range_list:
                start_url = self.base_url.format(quote(keyword), date[0], date[1])
                yield scrapy.Request(url=start_url, callback=self.parse, cookies=random.choice(COOKIES))

    def parse(self, response):
        result = json.loads(response.body.decode('utf-8'))
        item = SexAgeItem()
        if result['status'] != 10002:
            data = result['data'][0]
            if len(data) > 2:
                item["keyword"] = data['word']
                item["level1"] = data['str_age']['1']
                item["level2"] = data['str_age']['2']
                item["level3"] = data['str_age']['3']
                item["level4"] = data['str_age']['4']
                item["level5"] = data['str_age']['5']
                item["male"] = data['str_sex']['M']
                item["female"] = data['str_sex']['F']
                item["date"] = data['period']
                yield item
            else:
                print("数据为空" + ":" + data['word'])
        else:
            print('没有该关键词')

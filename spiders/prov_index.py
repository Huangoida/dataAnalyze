# -*- coding: utf-8 -*-
import calendar
import datetime
import json
import random
import scrapy
from dateutil import relativedelta
from scrapy.utils.project import get_project_settings
from settings import COOKIES
from items import ProvIndexItem
from spiders.base_spider import BaseSpider


class ProvIndexSpider(BaseSpider):
    name = 'prov_index'

    def __init__(self, *args, **kwargs):
        super(ProvIndexSpider, self).__init__(*args, **kwargs)
        self.settings = get_project_settings()
        self.base_url = 'https://index.baidu.com/api/SearchApi/region?region=0&word={}&startDate={}&endDate={}&days="'

        self.set_param_file('paramdemo.json')
        self.set_time_split(relativedelta.relativedelta(months=1))

    def start_requests(self):
        for keyword in self.keywords:
            for date in self.date_range_list:
                start_url = self.base_url.format(keyword, date[0], date[1])
                yield scrapy.Request(url=start_url, callback=self.parse,
                                     cookies=random.choice(COOKIES))

    def parse(self, response):
        result = json.loads(response.body.decode('utf-8'))
        if result['status'] != 10002:
            item = ProvIndexItem()
            if result['data']:
                item['keyword'] = result['data']['region'][0]['key']
                prov = result['data']['region'][0]['prov']
                item['date'] = result['data']['region'][0]['period']
                for key, value in prov.items():
                    item['prov'] = key
                    item['prov_index'] = value
                    yield item
            else:
                print(result['data']['region'][0]['key'] + "该地区数据为空")
        else:
            print("未收录该关键词")


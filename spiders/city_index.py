# -*- coding: utf-8 -*-
from dateutil import relativedelta
import json
import random
import scrapy

from settings import COOKIES
from items import CityIndexItem
from spiders.base_spider import BaseSpider


class CityIndexSpider(BaseSpider):
    name = 'city_index'

    def __init__(self, *args, **kwargs):
        super(CityIndexSpider, self).__init__(*args, **kwargs)
        self.base_url = 'https://index.baidu.com/api/SearchApi/region?region={}&word={}&startDate={}&endDate={}&days="'

        self.set_param_file('paramdemo.json')
        self.set_time_split(relativedelta.relativedelta(months=6))

    def start_requests(self):
        for keyword in self.keywords:
            for region_id in self.region_id_list:
                for startdate, enddate in self.date_range_list:
                    start_url = self.base_url.format(region_id, keyword, startdate, enddate)
                    yield scrapy.Request(url=start_url, callback=self.parse, cookies=random.choice(COOKIES),
                                         meta={'region': region_id})

    def parse(self, response):
        result = json.loads(response.body.decode('utf-8'))
        if result['status'] != 10002:
            item = CityIndexItem()
            if result['data']:
                item['keyword'] = result['data']['region'][0]['key']
                item['prov'] = response.meta['region']
                item['date'] = result['data']['region'][0]['period']
                city = result['data']['region'][0]['city']
                for key, value in city.items():
                    item['city'] = key
                    item['city_index'] = value
                    yield item
            else:
                print(result['data']['region'][0]['key'] + "该地区数据为空")
        else:
            print("未收录该关键词")

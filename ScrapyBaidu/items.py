# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapybaiduItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CityIndexItem(scrapy.Item):
    keyword = scrapy.Field()  # 关键词
    city = scrapy.Field()  # 城市ID
    city_index = scrapy.Field()  # 城市搜索指数
    prov = scrapy.Field()  # 所属省份ID
    date = scrapy.Field()  # 日期


class ProvIndexItem(scrapy.Item):
    keyword = scrapy.Field()  # 关键词
    prov = scrapy.Field()  # 省份ID
    prov_index = scrapy.Field()  # 省份搜索指数
    date = scrapy.Field()  # 日期


class RelatedWordItem(scrapy.Item):
    keyword = scrapy.Field()  # 关键词
    related_word = scrapy.Field()  # 相关词
    count = scrapy.Field()  # 相关词搜索指数
    date = scrapy.Field()  # 日期


class SexAgeItem(scrapy.Item):
    keyword = scrapy.Field()  # 关键词
    level1 = scrapy.Field()  # age <= 19
    level2 = scrapy.Field()  # 20< age <29
    level3 = scrapy.Field()  # 30< age <39
    level4 = scrapy.Field()  # 40< age <49
    level5 = scrapy.Field()  # age >= 50
    male = scrapy.Field()  # 男性比例
    female = scrapy.Field()  # 女性比例
    date = scrapy.Field()  # 日期

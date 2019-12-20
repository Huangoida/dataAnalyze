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
    keyword = scrapy.Field() # 关键词
    city = scrapy.Field() # 城市ID
    city_index = scrapy.Field() # 城市搜索指数
    prov = scrapy.Field() # 所属省份ID
    date = scrapy.Field() # 日期


    # 数据库插入语句
    def get_insert_sql(self):
        insert_sql = "insert into city_index(keyword,city,city_index,prov,date) values(%s,%s,%s,%s,%s)"
        params = (self['keyword'],self['city'],self['city_index'],self['prov'],self['date'],)
        return insert_sql, params

class ProvIndexItem(scrapy.Item):
    keyword = scrapy.Field() # 关键词
    prov = scrapy.Field() # 省份ID
    prov_index = scrapy.Field() # 省份搜索指数
    date = scrapy.Field() # 日期


    # 数据库插入语句
    def get_insert_sql(self):
        insert_sql = "insert into province_index(keyword,prov,prov_index,date) values(%s,%s,%s,%s)"
        params = (self['keyword'],self['prov'],self['prov_index'],self['date'],)
        return insert_sql, params

class RelatedWordItem(scrapy.Item):
    keyword = scrapy.Field() # 关键词
    related_word = scrapy.Field() # 相关词
    count = scrapy.Field() # 相关词搜索指数
    date = scrapy.Field() # 日期



    # 数据库插入语句
    def get_insert_sql(self):
        insert_sql = "INSERT INTO demand_map(related_word,count,keyword,date) VALUES (%s, %s, %s, %s)"
        params = (self['related_word'],self['count'],self['keyword'],self['date'],)
        return insert_sql, params

class SexAgeItem(scrapy.Item):
    keyword = scrapy.Field()  # 关键词
    level1 = scrapy.Field()  # age <= 19
    level2 = scrapy.Field()  # 20< age <29
    level3 = scrapy.Field()  # 30< age <39
    level4 = scrapy.Field()  # 40< age <49
    level5 = scrapy.Field()  # age >= 50
    male = scrapy.Field()  # 男性比例
    female = scrapy.Field()  # 女性比例
    date = scrapy.Field() # 日期

    # 数据库插入语句
    def get_insert_sql(self):
        insert_sql = "insert into crowd_property(keyword,level1,level2,level3,level4,level5,male,female,date) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        params = (
        self['keyword'], self['level1'], self['level2'], self['level3'],
        self['level4'],self['level5'],self['male'],self['female'],self['date'])
        return insert_sql, params

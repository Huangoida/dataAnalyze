import scrapy
import json
import datetime
from dateutil.relativedelta import relativedelta
from tools.regionid import RegionId


class BaseSpider(scrapy.Spider):
    name = "base_spider"

    def __init__(self, *args, **kwargs):
        super(BaseSpider, self).__init__(*args, **kwargs)
        self.keywords = []
        self.startdate = None
        self.enddate = None
        self.region_id_list = None
        self.date_range_list = None

        # 以下操作均需要子类在初始化时操作
        # 配置参数数据源
        # self.set_param_file(filename)
        # self.set_time_split(split)

    def init_base_param(self):
        self.region_id_list = RegionId.get_region_id_list()

    def set_param_file(self, filename):
        file = open(filename, 'r')
        content = file.read()
        file.close()
        params = json.loads(content)
        self.keywords = params['keywords']
        self.startdate = params['startdate']
        self.enddate = params['enddate']

    def set_time_split(self, split: relativedelta):
        self.date_range_list = self.get_time_range_list(split)

    def get_time_range_list(self, split: relativedelta):
        """
        根据给定的时间分割步长，划出起止时间列表
        :param split: 分割步长
        :return: [(startdate1, enddate1), (startdate2, startdate2), ...]
        """
        date_range_list = []
        startdate = datetime.datetime.strptime(self.startdate, '%Y-%m-%d')
        enddate = datetime.datetime.strptime(self.enddate, '%Y-%m-%d')
        while 1:
            next_month = startdate + split
            month_end = next_month - datetime.timedelta(days=1)
            if month_end < enddate:
                date_range_list.append((datetime.datetime.strftime(startdate, '%Y-%m-%d'),
                                        datetime.datetime.strftime(month_end, '%Y-%m-%d')))
                startdate = next_month
            else:
                return date_range_list

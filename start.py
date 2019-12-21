# coding=utf-8
# @ Author: TianHao
# @ Python: Python3.6.1
# @ Date: 2019/10/10 10:42
# @ Desc : 启动百度指数抓取

from get_index import BaiduIndex
import pymongo


def main(keywords_list, start_date, end_date):
    """
    爬虫调用主程序
    :param keywords_list: 关键词列表 -->list
    :param start_date: 开始时间 -->str
    :param end_date: 结束时间 -->str
    :return: 存入数据库
    """
    conn = pymongo.MongoClient('localhost', 27017)
    db = conn.dataAnalyze
    myset = db.keyword
    for keyword in keywords_list:

        index = BaiduIndex(keyword, start_date, end_date)
        data = index.result[keyword]["all"]
        for i in range(len(data)):
            index = data[i]["index"]
            date = data[i]["date"]
            # save_to_sql((keyword, index, date))
            a={'keyword':keyword,'index':index,'date':date}
            myset.insert_one(a)


if __name__ == '__main__':
    path = "test.xlsx"  # 文件位置
    column_name = "描述关键词串"  # 关键词列名
    #keywords_list = get_key_from_excel(path, column_name)  # 获取关键词列表，此处从excel中提取
    keywords_list = ["南昌大学","清华大学","北京大学"]

    start_date = "2019-01-01"
    end_date = "2019-12-19"
    main(keywords_list, start_date, end_date)  # 启动爬虫

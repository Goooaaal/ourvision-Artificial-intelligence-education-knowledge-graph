#coding=utf-8

# Copyright (c) 2018, Soki.
from pyhanlp import *
import sys
import os
import pandas as pd
import numpy as np
from pymongo import MongoClient
import json

#


# 建立知识图谱词典
def dictionary_of_knowledgegraph():
    excelpath = './tbl_knowledge_map.xls'
    df = pd.read_excel(excelpath, usecols='B')['knowledge_map_title'].tolist()
    return df
#






def books_name_list(df):
    title_array = []
    data = list()
# 创建实例,连接数据库
    client = MongoClient('47.75.70.164', 27017)
    if client:
        print(True)

    # 遍历集合表
    db = client['YJ_DB']
    collection = list(db['books'].find())
    for i in collection:
        book_name = i['book_name']
        title_array.append(book_name)


    # 创建文本推荐实例
    Suggester = JClass("com.hankcs.hanlp.suggest.Suggester")
    suggester = Suggester()
    for title in title_array:
        suggester.addSentence(title)
    df = dictionary_of_knowledgegraph()
    for i in df:
        s = suggester.suggest(i, 3)
        data.append(list(s))
    return data
#         # print(str(s).lstrip('[').rstrip(']').split(','))
#         #
#         # data["_id"]=


from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

engine = create_engine("mysql+pymysql://updater:Yuanjing123!@101.132.171.20:3306/aivision?charset=utf8",
                       encoding="utf8", poolclass=QueuePool, pool_size=100, pool_timeout=100)


df1 = dictionary_of_knowledgegraph()
data = books_name_list(df1)
print(len(data))


a = 2
for i in data:
    print(i)
    conn = engine.connect()
    transction = conn.begin()
    knowledge_map_title = i

    arg = (json.dumps(knowledge_map_title, ensure_ascii=False), a)

    data = conn.execute("update tbl_knowledge_map set book_uri_list=%s where id=%s", arg)

    transction.commit()
    a += 1

conn.close()


























# srcname = pd.read_csv('./srt_link.csv', encoding='utf-8')['srcname'].drop_duplicates().tolist()
# for item_srcname in srcname:
#     item_list = item_srcname.split(' ')
#
#     for item_item_list in item_list:
#
#         new_list = []
#         if item_item_list in df:
#             new_list.append(item_item_list)
#         print(item_list)
#         print(new_list)
#         print('##################################################################################################################')
        # new_list.clear()
 #           with open('./new_list.txt', 'a', encoding='utf-8') as f:




# for item in df:
#     print(item)
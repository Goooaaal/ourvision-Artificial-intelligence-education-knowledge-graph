# -*- encoding: utf-8 -*-

import wikipedia
import os

wikipedia.set_lang('zh')

category_name = '人工智能/' + '问题解决/' + '抽象/' + '概念系統/' + '信息系统/' + '信息论/' + '网络性能'
d = 0

def mkdir(path):
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
    else:
        print("文件夹存在...")



with open('category_pages/category.txt', 'r', encoding='utf-8') as f:
     sub = f.readlines()
     for sub1 in sub:
         try:
             filename = category_name + '/%s' % str(sub1).strip()
             mkdir(filename)
             d += 1
             print('第 %d 个分类已完成...' % d)
         except Exception:
             continue





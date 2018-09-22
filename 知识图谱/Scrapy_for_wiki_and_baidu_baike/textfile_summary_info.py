# -*- encoding: utf-8 -*-

import wikipedia
import os
import csv


wikipedia.set_lang('zh')



'''1.建立node 与 new node 的csv表格
    2.做item 的实体信息表格'''
'''从csv中读取node 与 new node 应用于item 表格的制作 '''
key_item = []
key_item2 = []
with open('人工智能实体关系.csv', 'r', encoding='utf-8') as f:
     reader= csv.reader(f)
     for item in reader:
         if reader.line_num == 1:
             continue
         else:
             key_item.append(item[0])
             key_item2.append(item[1])
     l2 = list(set(key_item))
     l2.sort(key=key_item.index)
     print(l2)
     # with open('第一列表.txt', 'a', encoding='utf-8') as f:
     #     for l2_item in l2:
     #         f.write(l2_item + '\n')

     l3 = list(set(key_item2))
     l3.sort(key=key_item2.index)
     print(l3)
     with open('第二列表.txt', 'a', encoding='utf-8') as f:
         for l3_item in l3:
             f.write(l3_item + '\n')
     # writeRow = []
     # with open('wikiitems2.csv', 'w', encoding='utf-8', newline='') as f:
     #     writer = csv.writer(f)
     #     writer.writerow(['title', 'detail', 'baseInfoKeyList', 'baseInfoValueList'])
     # for l2_item in l2:
     #     writeRow.clear()
     #     print(l2_item)
     #     try:
     #         summary = ''.join(wikipedia.summary(l2_item).split())
     #         with open('wikiitems2.csv', 'a', encoding='utf-8', newline='') as csvwf:
     #             writer = csv.writer(csvwf)
     #             writeRow.append(l2_item)
     #             writeRow.append('"%s"' % summary)
     #             writeRow.append('中文:')
     #             writeRow.append(l2_item)
     #             writer.writerow(writeRow)
     #             print('加入1行.....')
     #     except:
     #         continue
         # try:
         #     with open('new_node.csv', 'a', encoding='utf-8', newline='') as f:
         #         writer = csv.writer(f)
         #         writeRow.append(l3_item)
         #         writeRow.append('newNode')
         #         writer.writerow(writeRow)
         #         print('写入1行.....')
         # except:
         #     continue




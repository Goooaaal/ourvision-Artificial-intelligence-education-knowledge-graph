# encoding: utf-8
import xdrlib, sys
import xlrd
from CxExtractor import CxExtractor
import csv
import sys

'''
解决报错：_csv.Error: field larger than field limit (131072)
'''
maxInt = sys.maxsize
decrement = True

while decrement:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.

    decrement = False
    try:
        csv.field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt / 10)
        decrement = True

count = 0
try:
    with open('1.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for item in reader:
            count += 1
            print(item[1])
            # cx = CxExtractor(threshold=186)
            # html = cx.readHtml(item[1], coding='utf-8')
            # content = cx.filter_tags(html)
            # print(content)
    print(count)
except Exception as e:
        print(count)

# def load_excel(file_path):
#     workbook = xlrd.open_workbook(file_path)
#     booksheet= workbook.sheet_by_name('Worksheet')
#     for i in range(1, 2001):
#         cell_i1 = booksheet.cell_value(i, 0)
#         cell_i2 = booksheet.cell_value(i, 1)
#         cell_i3 = booksheet.cell_value(i, 2)
#         print(cell_i3)
#         with open('HTML/read.html', 'w', encoding='utf-8') as f:
#             f.writelines(cell_i3)
#         cx = CxExtractor(threshold=186)
#         html = cx.readHtml('HTML/read.html', coding='utf-8')
#         content = cx.filter_tags(html)
#         # print(content)
#         with open('Text/(%d).txt'%(i + 2000), 'w', encoding='utf-8') as f:
#             f.write('标题:%s 摘要:%s 内容:%s'%(cell_i1, cell_i2, content.strip().split()))
# load_excel('E:/2001-4000.xlsx')
# cx = CxExtractor(threshold=186)
# html = cx.readHtml('HTML/read.html', coding='utf-8')
# content = cx.filter_tags(html)
# #print(content)
# with open('Text/126.txt', 'w', encoding='utf-8') as f:
#     f.writelines(content.strip().split())
# #print(cx.getText(content))
# #print(s)

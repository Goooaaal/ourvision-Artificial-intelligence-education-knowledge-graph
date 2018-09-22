import wikipedia
import os

wikipedia.set_lang('zh')

category_name = '人工智能/' + '问题解决/' + '抽象/' + '概念系統/' + '信息系统/' + '信息论/' + '网络性能/' + '反向代理'

d = 0



with open('category_pages/pages.txt', 'r', encoding='utf-8') as f:
     sub = f.readlines()
     for sub1 in sub:
         try:
             with open(category_name + '/%s.txt' % str(sub1).strip(), 'w', encoding='utf-8') as f:
                 zh = wikipedia.page(sub1)
                 text = zh.content
                 f.write(text)
                 d += 1
                 print('第 %d 个页面已完成...' % d)
         except Exception:
             continue



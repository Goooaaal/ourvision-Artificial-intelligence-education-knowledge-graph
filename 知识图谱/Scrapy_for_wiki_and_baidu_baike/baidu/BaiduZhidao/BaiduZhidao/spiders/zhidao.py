# -*- coding: utf-8 -*-
import scrapy
import re
from BaiduZhidao.items import BaiduzhidaoItem


class BaiduSpider(scrapy.Spider):
    name = "baidu"
    # allowed_domains = ["zhidao.baidu.com"]
    urls = []

    with open('/home/python/Desktop/实体4.csv') as f:
        content = f.read().strip()
        keys = content.split('\n')
    for key in keys:
        url = 'https://zhidao.baidu.com/search?lm=0&rn=10&pn=0&fr=search&ie=gbk&word=' + key
        urls.append(url)

    start_urls = urls
    # start_urls = (
    #     'https://zhidao.baidu.com/search?lm=0&rn=10&pn=0&fr=search&ie=gbk&word=%C8%CB%B9%A4%D6%C7%C4%DC',
    # )

    def parse(self, response):
        content = response.body_as_unicode()
        ret = re.findall(r'<a href="(http://zhidao.baidu.com/question/\d+?.html\?fr=iks&word=.*?&ie=gbk)"', content)
        # print(len(ret))
        for next_url in ret:
            # print(next_url.strip())
            yield scrapy.Request(url=next_url, callback=self.parse_question)

        next_page = re.findall(r'<a class="pager-next" href="(.*?)">下一页', content)
        if next_page:
            # print('https://zhidao.baidu.com'+next_page[0])
            yield scrapy.Request(url='https://zhidao.baidu.com'+next_page[0], callback=self.parse)

    def parse_question(self, response):
        content = response.body_as_unicode()

        question = re.findall(r'<h1 class="wgt-header-title-text">(.*?)</h1>', content)[0].strip()
        # print(question)

        answers = re.findall(r"""展开全部<span class="wgt-\w+?-arrowdown"></span>
</div>
</div>
(.*?)
</div>""", content)

        # for answer in answers:
        #     print(re.sub(r'<.*?>', '', answer.strip()))

        praises = re.findall(r'data-evaluate="(\d*?)"', content)
        # for praise in praises:
        #     print(int(praise))

        for num in range(len(answers)):
            item = BaiduzhidaoItem()
            # print(praises[num], '  ', re.sub(r'<.*?>', '', answers[num]))
            item['question'] = question.replace('\r', '').replace('&rdquo;', '')
            item['answer'] = re.sub(r'<.*?>', '', answers[num])
            praise = praises[num]
            if praise == '赞':
                praise = 0
            item['praise'] = int(praise)
            yield item

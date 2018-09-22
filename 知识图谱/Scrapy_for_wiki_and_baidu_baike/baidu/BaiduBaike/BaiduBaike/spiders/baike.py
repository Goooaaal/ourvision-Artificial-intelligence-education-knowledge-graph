# -*- coding: utf-8 -*-
import scrapy
import re
import urllib.parse
from BaiduBaike.items import BaidubaikeItem


class BaikeSpider(scrapy.Spider):
    name = 'baike'
    # allowed_domains = ['baike.baidu.com']
    urls = []

    with open('/home/python/Desktop/1.txt') as f:
        content = f.read().strip()
        keys = content.split('\n')
    for key in keys:
        url = 'https://baike.baidu.com/item/' + key
        urls.append(url)


    start_urls = urls
    # start_urls = ['https://baike.baidu.com/item/TensorFlow', ]

    def parse(self, response):
    #     content = response.body_as_unicode()
    #     urls = re.findall(r'data-url="(https?://baike.baidu.com/item/.*?)"', content)
    #     urls = list(set(urls))
    #     if urls:
    #         url = urls[0]
    #         yield scrapy.Request(url=url, callback=self.parse_detail)
    #
    # def parse_detail(self, response):
        content = response.body_as_unicode()
        try:
            try:
                name = response.url.split('fromtitle=')[1].split('&fromid')[0]
            except:
                name = response.url.split('item/')[1].split('/')[0]
        except:
            return
        name = urllib.parse.unquote(name).lower()
        item = BaidubaikeItem()
        item['name'] = name

        try:
            definition = response.css(
                'body > div.body-wrapper > div.content-wrapper > div > div.main-content > div.lemma-summary')\
                .extract_first()
            definition = re.sub(r'<.*?>', '', definition).strip().replace('\xa0', '').replace('\n', '')
        except:
            definition = ''
        item['definition'] = definition

        item['basicInfo'] = {}

        try:
            basicInfo_names = response.css(
                'body > div.body-wrapper > div.content-wrapper > div > div.main-content > div.basic-info.cmn-clearfix > dl.basicInfo-block > dt').extract()
            basicInfo_values = response.css(
                'body > div.body-wrapper > div.content-wrapper > div > div.main-content > div.basic-info.cmn-clearfix > dl.basicInfo-block > dd').extract()

            for i in range(len(basicInfo_names)):
                basicInfo_name = re.sub(r'<.*?>', '', basicInfo_names[i]).strip().replace('\xa0', '')\
                    .replace('\n', '').replace('&nbsp', '').replace('\r', '')
                basicInfo_value = re.sub(r'<.*?>', '', basicInfo_values[i]).strip().replace('\xa0', '')\
                    .replace('\n', '').replace('&nbsp', '').replace('\r', '')
                item['basicInfo'][basicInfo_name] = basicInfo_value
        except:
            pass
        item['detail'] = {}

        titles = re.findall(r"""<h2 class="title-text">(.*)""", content)
        text = content.split('<h2 class="title-text">')[1:]
        try:
            text[-1] = text[-1].split('参考资料')[0].strip().split('词条标签')[0]
        except:
            pass
        # print(len(titles), len(text))

        try:
            for i in range(len(titles)):
                key = re.sub(r'<.*?>', '', titles[i]).strip().replace('\xa0', '').replace('\n', '')\
                    .replace('&nbsp', '').replace('\r', '').replace('.', '_')
                value = re.sub(r'<.*?>', '', text[i]).strip().replace('\xa0', '').replace('\n', '')\
                    .replace('&nbsp', '').replace('\r', '')
                value = re.sub(r'<.*?>', '', value).replace('&quot;', '')
                try:
                    value = value.split('V百科往期回顾词条')[0].split('window.rsInsertData')[0]
                except:
                    pass
                item['detail'][key] = value
        except:
            pass

        # print(item)
        yield item

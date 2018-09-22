import requests
from bs4 import BeautifulSoup
import re
import time
from lxml import etree

time1 = time.time()

category_xpath_link = '//*[@id="mw-subcategories"]/div/ul/li/div/div/a'

page_xpath_link = '//*[@id="mw-pages"]/div/div/div/ul/li/a'


def scrappy(url):
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36'
        }
        r = requests.get(url, headers=headers)
        html = r.text
        print(html)
        with open('title.txt', 'w', encoding='utf-8') as f:
            f.write(html)
    except Exception:
        pass
    s = etree.HTML(html)
    categorys = s.xpath(category_xpath_link)
    with open('category_pages/category.txt', 'w', encoding='utf-8') as f:
        f.truncate()
        print('文件已清理...')
    with open('category_pages/category.txt', 'a', encoding='utf-8') as f:
        for text1 in categorys:
            f.write(text1.text + '\n')


    pages = s.xpath(page_xpath_link)
    with open('category_pages/pages.txt', 'w', encoding='utf-8') as f:
        f.truncate()
        print('文件已清理...')
    with open('category_pages/pages.txt', 'a', encoding='utf-8') as f:
        for text2 in pages:
            f.write(text2.text + '\n')





scrappy('https://www.slideshare.net/NVIDIA/top-5-deep-learning-and-ai-stories-october-6-2017-80543540')
time2 = time.time()
print('Total time', time2 - time1)







































    # filename += '-->' + str(url.split(':')[-1])
    # print(filename)



    # links = BeautifulSoup(html, 'lxml').select('body > div > div > div > div > div > div > div > div > ul > li > a')
    # for tag2 in links:
    #     print(str(tag2).split('< a href = '))



    # soup = BeautifulSoup(html, 'lxml')
    # subcategories_url = soup.find('div', id='mw-subcategories').find('div', class_='CategoryTreeItem').find('a')
    # text1 = soup.find_all('a', class_='CategoryTreeLabel')
    # links1 = s.xpath('//*[@id="mw-pages"]/div/ul/li/a/@ *')
    # write_pages(page=('\n' * 3 + filename + '\n'))
    # for tag2 in links1:
    #     write_pages(page=(str(tag2) + '\n'))
    # subcategories_url = s.xpath('//*[@id="mw-subcategories"]/div/div/div/ul/li/div/div/a/@href')
    # if subcategories_url:
    #     for tag in subcategories_url:
    #         # scrappy(url='https://zh.wikipedia.org' + tag)
    #         print('https://zh.wikipedia.org' + tag)

    # for tag in text1:
    #     pattern1 = re.compile(r'^<a class="CategoryTreeLabel CategoryTreeLabelNs14 CategoryTreeLabelCategory" href=')
    #     sub1 = pattern1.sub('', str(tag))
    #     pattern2 = re.compile(r'</a>')
    #     sub2 = pattern2.sub('', sub1).split('>')
    #     link_category_list = sub2[0]
    #     filename = sub2[-1]
    #     if link_category_list:
    #         print(filename)
            # scrappy(url='https://zh.wikipedia.org' + str(link_category_list).lstrip('"').rstrip('"'), filename=filename)

# def write_pages(page):
#     with open('./category_pages.txt', 'a', encoding='utf-8') as f:
#         f.write(page)







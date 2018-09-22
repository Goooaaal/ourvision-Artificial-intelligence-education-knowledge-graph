import requests
from bs4 import BeautifulSoup
import re
import time
from lxml import etree

def scrappy(url, depth=1):
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    html = r.text
    links = BeautifulSoup(html, 'lxml').find_all('div', id='bodyContent', class_='mw-body-content')
    print(links)
scrappy(url='https://zh.wikipedia.org/wiki/%E5%9B%BD%E9%99%85%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E8%81%94%E5%90%88%E4%BC%9A%E8%AE%AE')
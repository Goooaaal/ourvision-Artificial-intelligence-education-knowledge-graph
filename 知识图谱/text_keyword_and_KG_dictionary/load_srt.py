from bs4 import BeautifulSoup
import requests
from gevent import monkey
monkey.patch_all()
import sys
import os
from gevent.pool import Pool

def download(url):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Window NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.18 Safari/537.36'
    }
    r = requests.get(url, headers=headers, stream=True)
    print(r.status_code)
    file_name = url.split('/')[-1].strip()
    with open(file_name, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
    print(file_name + 'is ojbk')

if __name__ == '__main__':
    url = 'https://yj-video-hk.oss-cn-hongkong.aliyuncs.com/180314/fxzw5vychsg_zh-Hans.srt'
    download(url=url)
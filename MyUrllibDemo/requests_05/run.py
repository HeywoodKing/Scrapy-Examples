# -*- coding: utf-8 -*-


import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
}


def spider(urls, encoding='utf-8'):
    try:
        for item in urls:
            res = requests.get(url=item, headers=headers)
            res.raise_for_status()
            print(res.encoding, res.apparent_encoding)
            # res.encoding = res.apparent_encoding
            res.encoding = encoding

            print(res.text)
    except Exception as e:
        print('error', e)


def spider2(urls, encoding='utf-8', params=None):
    try:
        for item in urls:
            res = requests.get(url=item, headers=headers, params=params)
            res.raise_for_status()
            print(res.encoding, res.apparent_encoding)
            # res.encoding = res.apparent_encoding
            res.encoding = encoding

            print(res.text)
    except Exception as e:
        print('error', e)


if __name__ == "__main__":
    # url_list = ['https://www.baidu.com', 'https://www.baidu.com/robots.txt']
    # url_list = ['https://news.sina.com.cn', 'https://news.sina.com.cn/robots.txt']
    # url_list = ['https://www.qq.com', 'https://www.qq.com/robots.txt']
    # url_list = ['https://news.qq.com', 'https://news.qq.com/robots.txt']
    # url_list = ['http://www.moe.edu.cn', 'http://www.moe.edu.cn/robots.txt']

    # url_list = ['https://list.jd.com/list.html?cat=9987,653,655&page=1&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main']

    # url_list = ['https://www.baidu.com/s']
    # payload = {
    #     'wd': 'python'
    # }

    url_list = ['https://www.so.com/s']
    payload = {
        'q': 'python'
    }

    spider2(url_list, encoding='utf-8', params=payload)


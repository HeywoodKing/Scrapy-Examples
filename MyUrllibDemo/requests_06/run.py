# -*- coding: utf-8 -*-


import requests
import bs4
import re
import traceback
from bs4 import BeautifulSoup
import random


# 获取上交所和深交所所有股票交易的名称和交易信息
class GuPiaoSpider(object):
    def __init__(self, g_url, g_url_info, page_nums=1):
        self.g_url = g_url
        self.g_url_info = g_url_info
        self.page_nums = page_nums

    def get_east_json(self, num):
        try:
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                              '(KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
                # 'Referer': 'http://quote.eastmoney.com/center/gridlist.html',
            }
            # 返回json格式数据
            url = 'http://{0}.push2.eastmoney.com/api/qt/clist/get?' \
                  'cb=jQuery112406139267027871709_1563270253764&pn={1}&pz={2}&po=1&np=1&' \
                  'ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&' \
                  'fs=m:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,' \
                  'f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152' \
                  '&_={3}'.format(random.randint(1, 101), num, 20, '1563270253819')
            res = requests.get(self.g_url, headers=headers, timeout=10)
            res.raise_for_status()
            res.encoding = 'utf-8'
            return res.text
        except Exception as e:
            print('error', e)
            return None
        pass

    def get_html(self):
        pass

    def parser_list(self):
        pass

    def parser_info(self):
        pass

    def print_result(self):
        pass


if __name__ == "__main__":
    # url = 'http://quote.eastmoney.com/center/gridlist.html#hs_a_board'
    # 取多少页数据
    nums = 1
    url_info = 'https://gupiao.baidu.com/stock/sz300215.html'





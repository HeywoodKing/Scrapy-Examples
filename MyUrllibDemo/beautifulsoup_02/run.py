# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup
import bs4


class UnivRankSpider(object):
    def __init__(self, url, ulist = None):
        self.url = url
        self.ulist = ulist

    def get_html(self):
        headers = {
            'user-agent': ''
        }
        try:
            res = requests.get(self.url, headers=headers)
            res.raise_for_status()
            res.encoding = res.apparent_encoding
            return res.text
        except:
            return None

    def fill_univ_list(self):
        html = self.get_html()
        soup = BeautifulSoup(html, 'html.parser')
        # trs = soup.tbody.contents
        # trs = soup.find_all('tr', 'alt')
        trs = soup.find('tbody').children
        # print(trs)

        unlist = []
        for tr in trs:
            if isinstance(tr, bs4.element.Tag):
                tds = tr('td')
                udict = {
                    'rank': tds[0].string,
                    'name': tds[1].string,
                    'addr': tds[2].string,
                    'score': tds[3].string,
                    'indicator5': tds[4].string,
                    'indicator6': tds[5].string,
                    'indicator7': tds[6].string,
                    'indicator8': tds[7].string,
                    'indicator9': tds[8].string,
                    'indicator10': tds[9].string,
                    'indicator11': tds[10].string,
                    'indicator12': tds[11].string,
                    'indicator13': tds[12].string,
                    'indicator14': tds[13].string
                }

                # for td in tr.children:
                #     print(td.string)

                unlist.append(udict)

        return unlist

    def print_univ_list(self):
        self.ulist = self.fill_univ_list()
        tmplt = "{0:<6}\t{1:{3}<30}\t{2:^6}"
        print(tmplt.format('排名', '学校', '得分', chr(12288)))
        for i in range(len(self.ulist)):
            u = self.ulist[i]
            print(tmplt.format(u['rank'], u['name'], u['score'], chr(12288)))


if __name__ == "__main__":
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    rank = UnivRankSpider(url)
    rank.print_univ_list()


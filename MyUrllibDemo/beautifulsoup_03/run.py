# -*- coding: utf-8 -*-


import requests
import re
import bs4
from bs4 import BeautifulSoup


# 爬取淘宝商品信息和价格
class TaobaoSpider(object):
    def __init__(self, url, page_num=1):
        self.url = url
        self.page_num = page_num
        self.product_list = []

    def get_page_num(self, num=1):
        if num < 0:
            num = 0
        return str(num * 44)

    def get_html(self, num):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
            'Cookie': 'cna=iI2RFBuEQQ4CAd5bta4iZfO2; miid=1084891110343592427; thw=cn; t=ea04dbdd403a97220ce5d9b11493d6cb; tk_trace=oTRxOWSBNwn9dPyorMJE%2FoPdY8zfvmw%2Fq5hnSP4OIQalisMfy%2BlhxQxhRU51T%2FClbXb8NoaEe7voAkJ0Wp%2BzjfeLXvtJlab4JJZUBlJVraemoGIi5SxIzJIk9IPeobRaMhsLBRD7GuH1l06C%2FUG0op4qIBljc15vSTBmxWbT7LtfmyaqeUmiOJ2xJidM5Zh6ssMelEUzwew9SR%2F5NK3KLLkh86hBYuhMn%2B374Pley30QLO93hXdC4yLCEv32C3aSjNFPRGSLuQp8ubUKXQ%2FJBAUn%2FJk%3D; cookie2=14f4e0fcd59e6b913c0b815e5ae20c32; v=0; _tb_token_=5d81eeee75ee6; skt=426c9f91a80759a1; publishItemObj=Ng%3D%3D; csg=2eb88c6a; uc3=vt3=F8dBy3%2F9E7ysd9XNWr8%3D&id2=VAXfnlmyNQdL&nk2=AHLO45TulW4%3D&lg2=VT5L2FSpMGV7TQ%3D%3D; existShop=MTU2MjkxMDY0Mg%3D%3D; tracknick=chyin666; lgc=chyin666; _cc_=VT5L2FSpdA%3D%3D; dnk=chyin666; tg=0; mt=ci=72_1; enc=kdBZR9tH7Lx%2FUoJAfRaqj%2FuW0xfTNdQaUOgWnmFkya7Xamkb%2FhohsLgDgX6jqLRXhrKJnVqSjec152%2Fd9E%2BfyQ%3D%3D; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; hng=CN%7Czh-CN%7CCNY%7C156; swfstore=304361; whl=-1%260%260%260; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; uc1=cookie15=V32FPkk%2Fw0dUvg%3D%3D&cookie14=UoTaG775UhC4Zw%3D%3D; JSESSIONID=B2C734B40C4C653E4C9B7111A9B13C27; l=cBa41tfmqTIEx6YbBOCaourza779IIRYmuPzaNbMi_5Ik6L6DJ7OkDIj3Fp6cjWd9yLB4G2npwy9-etkiKy06Pt-g3fP.; isg=BCsr_7698l4kGy4y9X8YEegyuk_V6D_Hb6D4652oBWrTPEueJRNdEkaeljz3GJe6',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Host': 's.taobao.com',
        }
        try:
            per_url = self.url + self.get_page_num(num)
            print(per_url)
            res = requests.get(per_url, headers=headers, timeout=30)
            res.raise_for_status()
            res.encoding = res.apparent_encoding
            return res.text
        except Exception as e:
            print('error', e)
            return None

    def parser_html(self):
        pro_list = []
        for i in range(self.page_num):
            try:
                html = self.get_html(i)
                if html is None:
                    continue

                print(html)
                soup = BeautifulSoup(html, 'html.parser')
                products = soup.find_all('div', attrs={'data-category': 'auctions'})
                for pro in products:
                    print(pro)
                    pro_price = pro.find(class_='row-1')
                    print(1, pro_price)

                    pro_dict = {
                        'name': '',
                        'price': '',
                        'url': '',
                        'pic': '',
                        'addr': '',
                        'shop_name': '',
                        'shop_href': ''
                    }

                pro_list.append(pro_dict)
            except:
                continue

        return pro_list

    def print_list(self):
        tmplt = "{:<5}\t{:13}\t{:30}"
        self.product_list = self.parser_html()
        for i in range(len(self.product_list)):
            p = self.product_list[i]
            print(tmplt.format(p['price'], p['shop_name'], p['name']))
        # print(self.product_list)


if __name__ == "__main__":
    keyword = '每日坚果'
    page_num = 1
    start_url = 'https://s.taobao.com/search?ie=utf8&initiative_id=staobaoz_20190715&' \
          'stats_click=search_radio_all%3A1&js=1&imgfile=&q={0}&suggest=0_1&_input_charset=utf-8&' \
          'wq=meiri&suggest_query=meiri&source=suggest&bcoffset=3&ntoffset=3&' \
          'p4ppushleft=1%2C48&s='.format(keyword)

    taobao = TaobaoSpider(start_url, page_num)
    taobao.print_list()




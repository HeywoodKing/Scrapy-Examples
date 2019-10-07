# -*- coding: utf-8 -*-


import requests
import re
import os
import pickle as p

img_address = []


def url_open(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        # 'Host': 'www.shuaige5.com',
        'Cookie': 'UM_distinctid=16be699a04ec3-01fa4a08f832bb-e343166-100200-16be699a050ab; '
                  'Hm_lvt_0da86885ce952ee6190df17b33b6f5fc=1562941956; '
                  'lmhkzecookieinforecord=%2C130-11532%2C130-14610%2C; '
                  'CNZZDATA4023709=cnzz_eid%3D583091607-1562937840-%26ntime%3D1562943241; '
                  'Hm_lpvt_0da86885ce952ee6190df17b33b6f5fc=1562944045',
        # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;'
        #           'q=0.8,application/signed-exchange;v=b3',
    }
    try:
        print('url_open start')
        res = requests.get(url, headers=headers, timeout=3)
        print('url_open end')
    except:
        res = None
        print('url_open error')
    finally:
        return res


def find_imgs(url):
    try:
        html = url_open(url).text
        pattern = re.compile('<div class="inner_wrapper_img inner_wrapper_img1">.*?'
                             '<img.*?src="/e/ext.*?src=(.*?)&amp;h=240&amp;w=190&amp;zc=1".*?</div>',
                             re.S)
        img_addrs = re.findall(pattern, html)
        # print(img_addrs)
    except:
        print('find_imgs error')
    finally:
        return img_addrs


def read_img_to_queue():
    page_number = 2

    try:
        while page_number < 5:
            page_url = url + '/index_' + str(page_number) + '.html'
            addrs = find_imgs(page_url)

            print(len(addrs), page_number)

            for i in addrs:
                if i in img_address:
                    continue
                else:
                    img_address.append(i)

                # print(len(img_address))

            page_number += 1
    except:
        print('查找图片地址出错了')


def write_img_from_queue():
    x = 0
    for each in img_address:
        # 取得文件名
        file_name = str(x) + '_' + os.path.basename(each)
        x += 1
        try:
            with open(file_name, 'wb') as f:
                print(x - 1)
                print(each)
                img = url_open(each).content
                print(img)

                f.write(img)
                # p.dump(img, f)
        except:
            print(x - 1, each, img)


def download(dir_name='shuaige'):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    os.chdir(dir_name)

    read_img_to_queue()

    print(len(img_address), img_address)

    write_img_from_queue()

    print('over')


if __name__ == "__main__":
    url = "http://www.shuaige5.com/shuaigetupian"
    download()


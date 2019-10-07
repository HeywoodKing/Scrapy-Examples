# -*- coding: utf-8 -*-


import urllib3
import requests

#  忽略警告：InsecureRequestWarning: Unverified HTTPS request is being made.
#  Adding certificate verification is strongly advised.
requests.packages.urllib3.disable_warnings()
# 一个PoolManager实例来生成请求, 由该实例对象处理与线程池的连接以及线程安全的所有细节
http = urllib3.PoolManager()

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/63.0.3239.108 Safari/537.36',
#     # 'Content-Type':'application/json'
#     'Host': ''
# }

# res = http.request('GET', 'http://www.baidu.com/s?',
#                    fields={'wd': 'hello'},
#                    headers=headers, retries=5, timeout=3)


# 使用multipart/form-data编码方式上传文件,可以使用和传入Form data数据一样的方法进行,
# 并将文件定义为一个元组的形式　　　　　(file_name, file_data):
# with open('1.txt', 'r+', encoding='utf-8') as f:
#     text = f.read()
#
# res = http.request('POST', 'http://www.baidu.com/post',
#                    fields={'filefield': ('1.txt', text, 'text/plain')})


# 二进制文件
with open('websocket.jpg', 'rb') as f:
    binary = f.read()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/63.0.3239.108 Safari/537.36',
    # 'Content-Type':'application/json'
    'Host': 'www.baidu.com'
}

try:
    res = http.request('POST', 'http://www.baidu.com/post',
                       body=binary,
                       headers={'Content-Type': 'image/jpeg'}, timeout=3.0, retries=5)

    # res = http.request('POST', 'http://www.baidu.com/post',
    #                    body=binary,
    #                    headers={'Content-Type': 'image/jpeg'}, timeout=3.0, retries=5, redirect=False)

    if res.status == 200:
        # print(res.data)  # 二进制
        # 获得html源码,utf-8解码
        print(res.data.decode('utf-8'))  # 转为utf-8编码字符串
    else:
        print(res.status)
except Exception as e:
    print(e.reason)


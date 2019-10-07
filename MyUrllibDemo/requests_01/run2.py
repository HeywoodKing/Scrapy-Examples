# -*- coding: utf-8 -*-


import requests
from requests.packages import urllib3
from requests.auth import HTTPBasicAuth
from requests.exceptions import HTTPError, ReadTimeout, ConnectionError, ConnectTimeout, RequestException, SSLError

urllib3.disable_warnings()

# s = requests.session()
# s.get('http://httpbin.org/cookies/set/number/123456')
# res = s.get('http://httpbin.org/cookies')
# print(res.text)


# 验证证书
# res = requests.get("https://www.12306.cn", verify=False)
# print(res.status_code)


# 代理设置
proxies = {
    'http': 'http://127.0.0.1:9999',
    'https': 'https://127.0.0.1:8888',
    # 'http': 'http://user:password@127.0.0.1:9999',
    # "http": "socks5://127.0.0.1:9999",
    # "https": "socks5://127.0.0.1:8888"
}

try:
    # res = requests.get('https://www.baidu.com', proxies=proxies, timeout=3)

    # 认证设置
    res = requests.get('http://120.27.34.24:9001/', auth=HTTPBasicAuth('user', '123'), timeout=3)

    print(res.status_code)
    print(res.text)
except ReadTimeout as e:
    print('ReadTimeout', e.errno, e.strerror)
except ConnectionError as e:
    print('ConnectionError', e)
except RequestException as e:
    print('RequestException', e.errno, e.strerror)



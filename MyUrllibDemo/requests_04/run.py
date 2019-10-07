# -*- coding: utf-8 -*-


import requests

userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
            'Chrome/75.0.3770.100 Safari/537.36'
url = 'https://www.biihu.cc/account/ajax/login_process/'
cookie = ''

headers = {
    'User-Agent': userAgent,
    'Host': 'www.biihu.cc',
}

payload = {
    'return_url': 'https://biihu.cc/',
    'user_name': '逼格满满',
    'password': 'ching19880815',
    '_post_type': 'ajax',
}

# data = bytes(parse.urlencode(dict_data), 'utf-8')

res = requests.post(url=url, headers=headers, data=payload, timeout=3)
if res.status_code == requests.codes.ok:
    print(res.text)
    # print(res.content.decode(encoding='utf-8'))
    data_res = res.json()
    if data_res['errno'] == 1:
        # print(res.cookies)
        # biihu__user_login=sY4Rsb5zJ%2FKCimwpjxle5ySa9iiB2VD2gerws72zoEO8V9%2FZK2uo%2B9pX1J60XRipkKqU
        # rXahQBnKQPT6btQ0aiOccvrj5FRDPJA%2F%2FUwy%2Fdqhq8qT19%2BCrQTAN1G2WIzmPwhaD8Tsvpt%2FNlEXR3T%2F
        # k6wfdPpIKWFPMUs4Na9TBHA%3D; path=/; HttpOnly

        cookie = 'biihu__Session = 1lgsk8vpvec9sl6bbji4v4i6vp;biihu__user_login=' \
                 'SCbxfxPCyPU5nSqQRmn5zxc3S%2FJ6eFxWYC2HM%2FrHGg5qzUMA5ICjcz6bKeVgIsKa2Z8bQ8t5PB%2F' \
                 'n9zb2TN53pFer1N%2FYZzheaZFlL6m80x7n4LJk0h%2BtPTLeuvYk0ZY%2FWlT%2B2%2BgYigVItk%2BL' \
                 '6M5dVjQBs%2FG3V7%2B%2Fv7vKeEtXSxo%3D;path=/; HttpOnly'
        # print(res.headers)

        # 以后抓取数据就可以带着这个cookie

        print('登录成功')
    else:
        print('error', data_res['err'])

else:
    print('error', res.reason)

